# Stack Decisions

This document explains **why** we chose these technologies and when you might choose differently.

## Philosophy

**Opinionated, but flexible.** This template makes strong choices to help you start fast. But every choice can be swapped out if your needs differ.

## Backend: FastAPI + GraphQL + SQLAlchemy

### Why FastAPI?

**Chosen for:**
- Modern async Python (handles concurrent requests efficiently)
- Automatic API documentation (OpenAPI/Swagger)
- Type hints everywhere (catches bugs early)
- Fast to develop with
- Production-ready (Uber, Microsoft, Netflix use it)

**Alternative: Django**
- Choose Django if: Building a traditional web app with admin panel, forms, and server-rendered HTML
- Stick with FastAPI if: Building an API for mobile/SPA frontend, need async, or want maximum flexibility

### Why GraphQL (Strawberry)?

**Chosen for:**
- Frontend controls what data it needs (no over-fetching)
- Single endpoint (simpler than many REST routes)
- Type safety from backend to frontend
- Perfect for React/Next.js apps

**Alternative: REST API**
- Choose REST if: Public API for third parties, simpler requirements, team unfamiliar with GraphQL
- Stick with GraphQL if: Complex data relationships, mobile app, frequent UI iterations

**Why Strawberry specifically?**
- Code-first (write Python, GraphQL schema auto-generated)
- Dataclasses integration
- Great FastAPI integration

### Why SQLAlchemy 2.0?

**Chosen for:**
- Industry standard Python ORM
- Async support (required for FastAPI async patterns)
- Type hints with Mapped[] types
- Powerful query builder
- Supports complex relationships

**Alternative: Raw SQL or Prisma**
- Choose raw SQL if: Maximum performance, simple queries, small project
- Choose Prisma if: Coming from Node.js, want Prisma Studio GUI
- Stick with SQLAlchemy if: Complex queries, Python ecosystem, proven at scale

### Why PostgreSQL + PostGIS?

**Chosen for:**
- Most popular open-source SQL database
- Excellent JSON support (for flexible fields)
- PostGIS for spatial data (if needed)
- TimescaleDB extension available (for time-series)
- Free and scalable

**Alternative: MySQL, MongoDB, DynamoDB**
- Choose MySQL if: Hosting on cPanel, simple queries, legacy requirements
- Choose MongoDB if: Truly schema-less data, rapid prototyping
- Choose DynamoDB if: AWS-only, extreme scale, key-value access
- Stick with Postgres if: Relational data, ACID compliance, spatial/time-series

## Frontend: Next.js + shadcn/ui + Tailwind

### Why Next.js 14?

**Chosen for:**
- React Server Components (better performance)
- App Router (modern routing)
- Server-side rendering (better SEO, faster initial load)
- API routes (can add REST if needed)
- Vercel deployment (easiest hosting)
- Best-in-class developer experience

**Alternative: Vite + React, Remix**
- Choose Vite if: Client-only SPA, no SEO needed, maximum flexibility
- Choose Remix if: Prefer web standards, edge deployment, nested routes
- Stick with Next.js if: Want SSR, large ecosystem, proven at scale

### Why shadcn/ui?

**Chosen for:**
- Not a component library (you own the code)
- Built on Radix UI (accessibility built-in)
- Beautiful defaults
- Fully customizable (Tailwind-based)
- Copy what you need (no bloat)

**Alternative: Material UI, Chakra, Ant Design**
- Choose MUI if: Need Material Design, comprehensive components
- Choose Chakra if: Want component library with good DX
- Choose Ant Design if: Enterprise dashboard, opinionated design
- Stick with shadcn if: Want full control, modern design, accessibility

### Why Tailwind CSS?

**Chosen for:**
- Utility-first (fast to prototype)
- No naming decisions (no CSS modules vs styled-components debate)
- Consistent design system (spacing, colors from config)
- Tree-shakeable (small production bundle)
- IDE autocomplete

**Alternative: CSS Modules, styled-components, vanilla CSS**
- Choose CSS Modules if: Prefer traditional CSS, scoped styles
- Choose styled-components if: Need dynamic styling, props-based styles
- Stick with Tailwind if: Want speed, consistency, no CSS naming debates

### Why TypeScript?

**Not negotiable.** Type safety catches bugs before runtime. GraphQL Code Generator makes backend and frontend types match automatically.

## Development Tools

### Why Alembic?

**Chosen for:**
- SQLAlchemy's official migration tool
- Auto-generates migrations from model changes
- Version control for database schema
- Downgrade support

**Alternative: Django migrations, Prisma Migrate**
- Stick with Alembic: It's the standard for SQLAlchemy

### Why Apollo Client?

**Chosen for:**
- Industry standard GraphQL client
- Excellent caching
- DevTools for debugging
- Large ecosystem

**Alternative: urql, TanStack Query + graphql-request**
- Choose urql if: Want smaller bundle, simpler API
- Choose TanStack Query if: Prefer REST-like API, very flexible
- Stick with Apollo if: Complex caching needs, subscriptions, proven scale

### Why Docker Compose?

**Chosen for:**
- Consistent development environment
- Easy PostgreSQL setup
- Reproducible across team
- Production-like locally

**Not for production.** Use ECS/Kubernetes/Railway for production.

## Architecture Patterns

### Three-Layer Database

```
Frontend → GraphQL → SQLAlchemy → PostgreSQL
```

**Why:**
- Clear separation of concerns
- Type safety at each layer
- Easy to test each layer independently

See: `ai-playbook/patterns/three-layer-database.md`

### Provider Pattern (Optional)

For external data sources (APIs, third-party services):

```python
# Abstract interface
class DataProvider:
    async def get_data(self): ...

# Real implementation
class RealProvider(DataProvider): ...

# Mock for testing
class MockProvider(DataProvider): ...
```

See: `ai-playbook/patterns/provider-pattern.md`

### Session Factory Pattern

Database sessions injected via dependency:

```python
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
```

Used in:
- FastAPI routes: `session: AsyncSession = Depends(get_session)`
- GraphQL context: `info.context["session"]`

## When to Deviate

### Use REST Instead of GraphQL If:

- Public API for third-party developers
- Very simple CRUD operations
- Team unfamiliar with GraphQL and timeline is tight
- File uploads (use REST endpoint alongside GraphQL)

### Skip PostgreSQL If:

- Extremely simple app (use SQLite)
- Already committed to MongoDB (stick with it)
- AWS-only and want DynamoDB (valid choice)

### Skip Next.js If:

- Building an internal tool (Vite might be simpler)
- No SEO requirements at all (SPA is fine)
- Team only knows Vue (use Nuxt instead)

## Technology Versions

This template uses:
- Python 3.11+ (required for modern type hints)
- Node.js 20+ (LTS)
- PostgreSQL 15
- Next.js 14
- React 18

## Related Playbook Patterns

For detailed implementation guides:

- **Three-Layer Database:** `ai-playbook/patterns/three-layer-database.md`
- **GraphQL Schema Design:** `ai-playbook/patterns/graphql-schema.md`
- **Provider Pattern:** `ai-playbook/patterns/provider-pattern.md`
- **Session Factory:** `ai-playbook/patterns/session-factory-testing.md`

## Questions?

See the main [ai-playbook](https://github.com/smeed652/ai-playbook) for:
- Detailed pattern implementations
- Sprint workflow
- Deployment guides
- Common issues and solutions
