# Full Stack Template

Opinionated starter template for building modern web applications with Python and Next.js.

## Quick Start

```bash
# 1. Clone and initialize
git clone <your-repo-url>
cd full-stack-template
make init

# 2. Start database
make db

# 3. Run migrations
make migrate

# 4. Start everything
make dev
```

Visit:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- GraphQL Playground: http://localhost:8000/graphql

## What's Included

### Backend
- **FastAPI** - Modern Python web framework with async support
- **Strawberry GraphQL** - Code-first GraphQL schema
- **SQLAlchemy 2.0** - Async ORM with type hints
- **Alembic** - Database migrations
- **PostgreSQL** - With PostGIS extension
- **Pytest** - Testing framework with 85% coverage threshold

### Frontend
- **Next.js 14** - React framework with App Router
- **TypeScript** - Full type safety
- **Tailwind CSS** - Utility-first styling
- **shadcn/ui** - Beautiful, accessible components
- **Apollo Client** - GraphQL client with caching
- **GraphQL Code Generator** - Auto-generated TypeScript types

### DevOps
- **Docker Compose** - Local development environment
- **Makefile** - Common commands
- **Pre-configured linting** - Ruff (Python), ESLint (TypeScript)

## Project Structure

```
full-stack-template/
├── backend/                   # Python FastAPI backend
│   ├── src/
│   │   ├── api/              # FastAPI app and GraphQL schema
│   │   ├── db/               # SQLAlchemy models and session
│   │   └── config/           # Settings
│   ├── alembic/              # Database migrations
│   ├── tests/                # Pytest tests
│   └── pyproject.toml        # Python dependencies
│
├── frontend/                  # Next.js frontend
│   ├── src/
│   │   ├── app/              # Next.js App Router pages
│   │   ├── components/       # React components (shadcn/ui)
│   │   ├── lib/              # Utilities and Apollo Client
│   │   └── types/            # Generated GraphQL types
│   └── package.json          # Node dependencies
│
├── docker-compose.yml         # Local development stack
├── Makefile                   # Common commands
└── README.md                  # This file
```

## Common Commands

```bash
# Development
make dev          # Start all services
make backend      # Backend only (kills port 8000 first)
make frontend     # Frontend only (kills port 3000 first)
make db           # Database only

# Database
make migrate      # Run migrations

# Testing
make test         # Run all tests

# Cleanup
make clean        # Stop services and remove volumes
```

## Architecture Decisions

See [STACK.md](./STACK.md) for:
- Why these technology choices
- When to use alternatives
- Architecture patterns explained

## Development Workflow

### 1. Adding a New Feature

```bash
# Create a sprint file (if using playbook workflow)
/sprint-new "My Feature"

# Follow the development sequence:
# 1. Database models (backend/src/db/models.py)
# 2. Migration (alembic revision --autogenerate)
# 3. GraphQL schema (backend/src/api/graphql/)
# 4. Frontend types (npm run codegen)
# 5. Frontend pages (frontend/src/app/)
```

### 2. Database Changes

```bash
# 1. Edit models in backend/src/db/models.py
# 2. Create migration
cd backend
alembic revision --autogenerate -m "Add new table"

# 3. Review migration in alembic/versions/
# 4. Apply migration
alembic upgrade head
```

### 3. GraphQL Changes

```bash
# 1. Update backend schema (backend/src/api/graphql/)
# 2. Restart backend
# 3. Generate TypeScript types
cd frontend
npm run codegen
```

## Tech Stack Details

See [STACK.md](./STACK.md) for detailed explanations.

**Backend:**
- Python 3.11+
- FastAPI + Strawberry GraphQL
- SQLAlchemy 2.0 (async)
- PostgreSQL + PostGIS

**Frontend:**
- Next.js 14 (App Router)
- React 18
- TypeScript 5+
- Tailwind CSS + shadcn/ui

## AI Development

This template is designed for AI-assisted development with Claude Code.

See [CLAUDE.md](./CLAUDE.md) for:
- Project instructions for Claude
- Sprint workflow integration
- Common patterns and standards

## Testing

### Backend
```bash
cd backend
pytest                    # Run all tests
pytest --cov             # With coverage
pytest tests/test_models.py  # Specific file
```

### Frontend
```bash
cd frontend
npm test                 # Run tests (when added)
```

## Production Deployment

This template includes:
- Health check endpoints (`/health`)
- Environment-based configuration
- Production-ready Docker images

For deployment guides, see the [ai-playbook](https://github.com/smeed652/ai-playbook):
- AWS ECS deployment
- Database migrations in production
- Environment variable management

## Customization

### 1. Rename the Project
```bash
# Update these files:
# - backend/pyproject.toml (name)
# - frontend/package.json (name)
# - docker-compose.yml (container names)
# - CLAUDE.md (project name)
```

### 2. Add shadcn/ui Components
```bash
cd frontend
npx shadcn-ui@latest add [component-name]
```

### 3. Add Database Extensions

Edit `docker-compose.yml` to add PostgreSQL extensions:
```yaml
postgres:
  image: postgis/postgis:15-3.4  # Already includes PostGIS
  # For TimescaleDB, use: timescale/timescaledb-ha:pg15
```

## Common Issues

### Port Already in Use

```bash
# Kill processes on ports 3000 or 8000
make backend   # Automatically kills port 8000
make frontend  # Automatically kills port 3000
```

### Database Connection Issues

```bash
# Ensure database is running
docker-compose ps

# Restart database
docker-compose restart postgres
```

### Frontend Can't Reach Backend

Check:
1. Backend is running: http://localhost:8000/health
2. CORS is configured in backend/.env
3. Frontend .env.local has correct NEXT_PUBLIC_GRAPHQL_URL

## Next Steps

1. **Customize for your domain:**
   - Edit `backend/src/db/models.py` (add your models)
   - Create migrations: `make migrate`
   - Update GraphQL schema in `backend/src/api/graphql/`

2. **Add authentication:**
   - See playbook patterns for Cognito/Auth0 integration
   - Implement user model and permissions

3. **Deploy:**
   - Follow playbook deployment guides
   - Set up CI/CD pipeline
   - Configure production environment

## Contributing

This template is part of the [ai-playbook](https://github.com/smeed652/ai-playbook) project.

## License

MIT
