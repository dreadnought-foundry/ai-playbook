# Using This Template

## For New Projects

### Option 1: Copy the Template (Recommended)

```bash
# From the ai-playbook directory
cp -r templates/full-stack-template ../my-new-project
cd ../my-new-project

# Initialize
make init
make db
make migrate
make dev
```

### Option 2: Use as Reference

Copy individual files/patterns as needed rather than the full template.

## First Steps After Copying

### 1. Customize for Your Project

```bash
# Update project names
# - backend/pyproject.toml: Change "name" from "app-backend"
# - frontend/package.json: Change "name" from "app-frontend"
# - docker-compose.yml: Update container names
# - README.md: Update title and description
```

### 2. Customize Domain Models

```python
# backend/src/db/models.py
# Replace the sample models (Tenant, User, Asset) with your domain models

# Example: For a task management app
class Project(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "projects"
    name: Mapped[str] = mapped_column(String(255), nullable=False)

class Task(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "tasks"
    project_uuid: Mapped[UUID] = mapped_column(ForeignKey("projects.uuid"))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
```

### 3. Create Initial Migration

```bash
cd backend
alembic revision --autogenerate -m "Initial schema"
alembic upgrade head
```

### 4. Update GraphQL Schema

```python
# backend/src/api/graphql/types.py
# Add your GraphQL types

# backend/src/api/graphql/schema.py
# Add your queries and mutations
```

### 5. Generate Frontend Types

```bash
cd frontend
npm run codegen
```

### 6. Build Your First Page

```tsx
// frontend/src/app/projects/page.tsx
"use client";

import { useQuery, gql } from "@apollo/client";

const GET_PROJECTS = gql`
  query GetProjects {
    projects {
      uuid
      name
    }
  }
`;

export default function ProjectsPage() {
  const { data } = useQuery(GET_PROJECTS);
  return <div>{/* Your UI */}</div>;
}
```

## What to Keep vs Remove

### Always Keep
- ✅ Project structure
- ✅ Configuration files (pyproject.toml, tsconfig.json, etc.)
- ✅ Database session factory pattern
- ✅ GraphQL setup (even if you modify schema)
- ✅ Tailwind + shadcn/ui setup
- ✅ Docker Compose setup
- ✅ Makefile commands
- ✅ Testing setup

### Customize for Your Domain
- 🔄 `backend/src/db/models.py` - Replace sample models
- 🔄 `backend/src/api/graphql/types.py` - Add your types
- 🔄 `backend/src/api/graphql/schema.py` - Add your queries
- 🔄 `frontend/src/app/` - Replace sample pages
- 🔄 README.md - Update for your project

### Optional (Remove if Not Needed)
- ❓ PostGIS extension (if no spatial data)
  - Edit `docker-compose.yml`: Change postgres image to `postgres:15`
- ❓ Sample pages (tenants page)
  - Delete `frontend/src/app/tenants/`
- ❓ Sample models (Tenant, User, Asset)
  - Replace with your domain models

## Adding Features

### Example: Add Authentication

See `ai-playbook/patterns/authentication.md` for:
1. Add auth models (User, Session)
2. Integrate Cognito/Auth0
3. Add protected routes
4. Add middleware

### Example: Add File Upload

1. Add REST endpoint (alongside GraphQL):
```python
# backend/src/api/app.py
@app.post("/upload")
async def upload_file(file: UploadFile):
    # Handle file upload
```

2. Frontend:
```tsx
const formData = new FormData();
formData.append('file', file);
await fetch('http://localhost:8000/upload', {
  method: 'POST',
  body: formData
});
```

### Example: Add Real-Time (Subscriptions)

1. Add Strawberry subscriptions support
2. Use WebSockets
3. See `ai-playbook/patterns/websockets.md`

## Integration with AI Playbook

### Using Sprint Workflow

```bash
# Install playbook commands first
cd ../ai-playbook
./scripts/setup-claude.sh

# In your project
/sprint-new "Add authentication"
/sprint-start 1
# Follow sprint workflow...
/sprint-complete 1
```

### Reference Patterns

Your project can reference playbook patterns:

- **Database migrations:** `ai-playbook/workflows/database-migrations.md`
- **GraphQL schema design:** `ai-playbook/patterns/graphql-schema.md`
- **Provider pattern:** `ai-playbook/patterns/provider-pattern.md`
- **Testing strategy:** `ai-playbook/workflows/testing-strategy.md`

## Common Customizations

### Switch from GraphQL to REST

If you decide GraphQL isn't right for you:

1. Keep FastAPI, remove Strawberry
2. Add REST routes in `backend/src/api/app.py`
3. Use Pydantic models for request/response
4. Frontend: Replace Apollo with fetch/axios

### Add MongoDB instead of PostgreSQL

1. Replace SQLAlchemy with Motor (async MongoDB)
2. Update docker-compose.yml
3. Remove Alembic (use MongoDB schema-less approach)

### Use Vite instead of Next.js

1. Replace `frontend/` with Vite React app
2. Keep Tailwind and shadcn/ui (they work with Vite)
3. Remove SSR-specific code

## For Your Cousin

Hey! This template is a starting point. Here's the quickest way to get going:

1. **Copy this template** to a new directory
2. **Run `make init && make dev`** - see it working
3. **Read STACK.md** - understand why we chose these technologies
4. **Modify `backend/src/db/models.py`** - add your data models
5. **Follow the playbook** - use sprint workflow for features

Don't try to understand everything at once. Start with:
1. What data do you need? (models)
2. What queries do you need? (GraphQL schema)
3. What pages do you need? (Next.js pages)

## Getting Help

- **Template issues:** Check STACK.md for alternatives
- **Pattern questions:** See ai-playbook/patterns/
- **Sprint workflow:** See ai-playbook/workflows/
- **Claude Code help:** Ask "/help" or check CLAUDE.md

## Next Steps

1. Copy template to new project
2. Customize for your domain
3. Create first migration
4. Build first feature using sprint workflow
5. Deploy (see ai-playbook/cloud/deployment.md)

Happy building! 🚀
