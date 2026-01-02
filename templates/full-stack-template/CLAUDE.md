# Project Instructions for Claude Code

## Tech Stack

**Backend:**
- Python 3.11+, FastAPI, Strawberry GraphQL, SQLAlchemy 2.0 (async)
- PostgreSQL with PostGIS extension
- Alembic for migrations
- Pytest for testing

**Frontend:**
- Next.js 14 (App Router), React 18, TypeScript 5
- Tailwind CSS + shadcn/ui components
- Apollo Client for GraphQL
- GraphQL Code Generator for type safety

## Code Standards

### Backend (Python)

**Required:**
- Type hints on all function signatures
- SQLAlchemy 2.0 style: `Mapped[type]` and `mapped_column()`
- Async everywhere (`async def`, `await`)
- 85% test coverage minimum
- Docstrings on public functions/classes

**Example:**
```python
from sqlalchemy.orm import Mapped, mapped_column

class User(Base, UUIDMixin, TimestampMixin):
    """User model with tenant relationship."""
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
```

### Frontend (TypeScript)

**Required:**
- TypeScript strict mode (no `any` without reason)
- Use generated GraphQL types from codegen
- "use client" directive for client components
- Tailwind utility classes (no inline styles)

**Example:**
```tsx
"use client";

import { useQuery } from "@apollo/client";
import { GetItemsQuery } from "@/types/graphql";

export default function ItemsPage() {
  const { data, loading, error } = useQuery<GetItemsQuery>(GET_ITEMS);
  // ...
}
```

## Development Sequence

When adding a new feature, follow this order:

### 1. Database Models (Backend)
```python
# backend/src/db/models.py
class MyModel(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "my_models"
    name: Mapped[str] = mapped_column(String(255), nullable=False)
```

### 2. Database Migration
```bash
cd backend
alembic revision --autogenerate -m "Add my_model table"
alembic upgrade head
```

### 3. GraphQL Schema (Backend)
```python
# backend/src/api/graphql/types.py
@strawberry.type
class MyType:
    uuid: UUID
    name: str

# backend/src/api/graphql/schema.py
@strawberry.field
async def my_items(self, info: strawberry.Info) -> list[MyType]:
    session = info.context["session"]
    # Query and return
```

### 4. Generate Frontend Types
```bash
cd frontend
npm run codegen
```

### 5. Frontend Pages
```tsx
// frontend/src/app/my-page/page.tsx
"use client";

import { useQuery, gql } from "@apollo/client";

const GET_MY_ITEMS = gql`
  query GetMyItems {
    myItems {
      uuid
      name
    }
  }
`;

export default function MyPage() {
  const { data } = useQuery(GET_MY_ITEMS);
  return <div>{/* render */}</div>;
}
```

## Key Patterns

### Database Session Injection

**GraphQL resolvers:**
```python
@strawberry.field
async def items(self, info: strawberry.Info) -> list[Item]:
    session = info.context["session"]  # Get session from context
    result = await session.execute(select(ItemModel))
    return [convert_to_graphql_type(item) for item in result.scalars()]
```

**FastAPI routes (if you add REST):**
```python
@app.get("/items")
async def get_items(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(ItemModel))
    return result.scalars().all()
```

### GraphQL Type Conversion

**Always convert SQLAlchemy models to GraphQL types:**

```python
# WRONG - Don't return ORM models directly
@strawberry.field
async def items(self, info: strawberry.Info) -> list[Item]:
    result = await session.execute(select(ItemModel))
    return result.scalars().all()  # ❌ Returns SQLAlchemy models

# CORRECT - Convert to GraphQL types
@strawberry.field
async def items(self, info: strawberry.Info) -> list[Item]:
    result = await session.execute(select(ItemModel))
    return [
        Item(
            uuid=item.uuid,
            name=item.name,
        )
        for item in result.scalars()
    ]  # ✅ Returns Strawberry types
```

### shadcn/ui Components

**Add new components:**
```bash
npx shadcn-ui@latest add [component-name]
```

**Use components:**
```tsx
import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";

<Card>
  <CardHeader>
    <CardTitle>Title</CardTitle>
  </CardHeader>
  <CardContent>
    <Button>Click me</Button>
  </CardContent>
</Card>
```

## Testing

### Backend Tests

```python
# tests/test_my_feature.py
import pytest
from sqlalchemy import select
from src.db.models import MyModel

@pytest.mark.asyncio
async def test_create_item(session):
    """Test creating an item."""
    item = MyModel(name="Test")
    session.add(item)
    await session.commit()

    result = await session.execute(select(MyModel))
    assert len(result.scalars().all()) == 1
```

**Run tests:**
```bash
cd backend
pytest                      # All tests
pytest --cov               # With coverage
pytest tests/test_my_feature.py  # Specific file
```

## Common Tasks

### Add a Database Column

1. Edit `backend/src/db/models.py`
2. Create migration: `alembic revision --autogenerate -m "Add column"`
3. Review migration in `alembic/versions/`
4. Apply: `alembic upgrade head`
5. Update GraphQL types in `backend/src/api/graphql/types.py`
6. Regenerate frontend types: `cd frontend && npm run codegen`

### Add a New Page

1. Create `frontend/src/app/my-page/page.tsx`
2. Add navigation: `<Link href="/my-page">My Page</Link>`
3. Style with Tailwind and shadcn/ui components

### Add Authentication

See `ai-playbook/patterns/` for:
- Cognito integration
- JWT token handling
- Protected routes
- Role-based access

## Project Structure

```
full-stack-template/
├── backend/
│   ├── src/
│   │   ├── api/
│   │   │   ├── app.py              # FastAPI app, GraphQL router
│   │   │   └── graphql/
│   │   │       ├── schema.py       # Queries and mutations
│   │   │       └── types.py        # Strawberry types
│   │   ├── db/
│   │   │   ├── base.py             # Base class, mixins
│   │   │   ├── models.py           # SQLAlchemy models
│   │   │   └── session.py          # Session factory
│   │   └── config/
│   │       └── settings.py         # Environment config
│   ├── alembic/                    # Migrations
│   ├── tests/                      # Pytest tests
│   └── pyproject.toml             # Dependencies
│
└── frontend/
    ├── src/
    │   ├── app/                    # Next.js pages (App Router)
    │   ├── components/ui/          # shadcn/ui components
    │   ├── lib/
    │   │   ├── apollo-wrapper.tsx  # Apollo Client setup
    │   │   └── utils.ts            # Utilities (cn helper)
    │   └── types/
    │       └── graphql.ts          # Generated types (don't edit!)
    └── package.json
```

## Sprint Workflow Integration

This template works with the AI Playbook sprint workflow:

```bash
# Using playbook commands
/sprint-start <N>      # Initialize sprint
/sprint-next <N>       # Advance to next step
/sprint-complete <N>   # Complete sprint with checklist
```

**Sprint execution order:**
1. **Planning:** Read requirements, design architecture
2. **Database:** Add models, create migration
3. **Backend:** GraphQL schema and resolvers
4. **Frontend:** Generate types, create pages
5. **Testing:** Write tests, verify coverage
6. **Documentation:** Update README if needed

## Anti-Patterns

### ❌ Don't: Use raw SQL
```python
# WRONG
await session.execute(text("INSERT INTO users ..."))
```

Use ORM models instead - they catch schema mismatches early.

### ❌ Don't: Return ORM models from GraphQL
```python
# WRONG
@strawberry.field
async def users(self, info) -> list[UserModel]:  # ❌ SQLAlchemy model
    ...
```

Always convert to Strawberry types.

### ❌ Don't: Use `any` type in TypeScript
```typescript
// WRONG
const data: any = await fetch(...)
```

Use generated GraphQL types instead.

### ❌ Don't: Mix Tailwind and CSS modules
```tsx
// WRONG
<div className="flex gap-4" style={{ color: 'red' }}>
```

Use Tailwind utilities consistently: `className="flex gap-4 text-red-500"`

## Environment Variables

**Backend (.env):**
- `DATABASE_URL` - PostgreSQL connection
- `CORS_ORIGINS` - Allowed frontend origins
- `DEBUG` - Enable debug logging

**Frontend (.env.local):**
- `NEXT_PUBLIC_GRAPHQL_URL` - Backend GraphQL endpoint

## Pre-Push Checklist

Before committing:

- [ ] Backend tests pass: `cd backend && pytest`
- [ ] No linting errors: `cd backend && ruff check src/`
- [ ] Frontend builds: `cd frontend && npm run build`
- [ ] GraphQL types generated: `cd frontend && npm run codegen`
- [ ] Migrations created: `alembic revision --autogenerate` (if schema changed)

## For More Information

See the [AI Playbook](https://github.com/smeed652/ai-playbook):
- **Patterns:** Detailed implementation guides
- **Workflows:** Sprint-based development
- **Playbooks:** Step-by-step task guides
- **Standards:** Coding standards and best practices
