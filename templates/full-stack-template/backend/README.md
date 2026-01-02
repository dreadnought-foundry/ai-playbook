# Backend - FastAPI + GraphQL

Python backend using FastAPI, SQLAlchemy 2.0, and Strawberry GraphQL.

## Quick Start

```bash
# Install dependencies
pip install -e .[dev]

# Copy environment file
cp .env.example .env

# Start database (from root directory)
docker-compose up -d postgres

# Run migrations
alembic upgrade head

# Start development server
uvicorn src.api.app:app --reload
```

The API will be available at:
- GraphQL: http://localhost:8000/graphql
- Health: http://localhost:8000/health

## Project Structure

```
backend/
├── src/
│   ├── api/
│   │   ├── app.py              # FastAPI application
│   │   └── graphql/            # GraphQL schema
│   ├── db/
│   │   ├── base.py             # SQLAlchemy base and mixins
│   │   ├── models.py           # Database models
│   │   └── session.py          # Session factory
│   └── config/
│       └── settings.py         # Application settings
├── alembic/                    # Database migrations
├── tests/                      # Tests
└── pyproject.toml             # Dependencies
```

## Key Patterns

### Database Models (SQLAlchemy 2.0)

Models use modern SQLAlchemy 2.0 style:

```python
from src.db.base import Base, UUIDMixin, TimestampMixin

class MyModel(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "my_models"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
```

### GraphQL Schema

Types are separate from database models:

```python
# GraphQL type
@strawberry.type
class MyType:
    uuid: UUID
    name: str

# Resolver
@strawberry.field
async def my_items(self, info: strawberry.Info) -> list[MyType]:
    session = info.context["session"]
    # Query database and convert to GraphQL types
```

### Database Migrations

```bash
# Create a new migration
alembic revision --autogenerate -m "Add new table"

# Apply migrations
alembic upgrade head

# Rollback one migration
alembic downgrade -1
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test
pytest tests/test_models.py::test_create_tenant
```

## Common Tasks

### Add a New Model

1. Edit `src/db/models.py`
2. Create migration: `alembic revision --autogenerate -m "Add model"`
3. Apply migration: `alembic upgrade head`
4. Add GraphQL type in `src/api/graphql/types.py`
5. Add query/mutation in `src/api/graphql/schema.py`

### Environment Variables

See `.env.example` for all available settings. Key variables:

- `DATABASE_URL` - PostgreSQL connection string
- `CORS_ORIGINS` - Allowed frontend origins (comma-separated)
- `DEBUG` - Enable debug mode

## Tech Stack

- **FastAPI** - Modern async web framework
- **SQLAlchemy 2.0** - Async ORM
- **Strawberry GraphQL** - Code-first GraphQL
- **Alembic** - Database migrations
- **Pytest** - Testing framework
- **Ruff** - Linting and formatting
