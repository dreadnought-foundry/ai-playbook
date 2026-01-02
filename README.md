# ai-playbook

Battle-tested patterns, workflows, and tools for AI-assisted software development with Claude Code.

## Quick Start

### Option 1: Start a New Full-Stack Project (Recommended)

```bash
# Clone the playbook
git clone https://github.com/smeed652/ai-playbook.git
cd ai-playbook

# Create a new project from template
./scripts/init-from-template.sh my-project "My Project Name"
cd my-project

# Start development
make init && make dev
```

Visit http://localhost:3000 - you now have a working FastAPI + Next.js app!

### Option 2: Add Sprint Workflow to Existing Project

```bash
# Clone the playbook
git clone https://github.com/smeed652/ai-playbook.git
cd ai-playbook

# Set up Claude Code symlinks
./scripts/setup-claude.sh

# In your project directory
/project-create
```

## What's Included

```
ai-playbook/
├── templates/
│   └── full-stack-template/       # 🆕 Complete FastAPI + Next.js starter
│       ├── backend/                # FastAPI + GraphQL + SQLAlchemy
│       ├── frontend/               # Next.js + shadcn/ui + Tailwind
│       ├── docker-compose.yml      # Local dev environment
│       ├── .github/workflows/      # CI/CD configuration
│       ├── docs/sprints/examples/  # Example sprint files
│       └── README.md, STACK.md, CLAUDE.md
│
├── playbooks/                      # 🆕 Step-by-step guides
│   ├── project-bootstrap-guide.md  # How to start a new project
│   ├── pattern-implementation-sequence.md  # What order to build things
│   ├── adding-external-data-source.md
│   ├── creating-rest-endpoint.md
│   └── ...
│
├── commands/                       # Slash commands for Claude Code
│   ├── sprint-*.md                 # Sprint lifecycle commands
│   ├── epic-*.md                   # Epic management commands
│   └── project-*.md                # Project setup commands
│
├── agents/                         # Specialized agent definitions
│   ├── context-fetcher.md
│   ├── date-checker.md
│   ├── file-creator.md
│   └── test-runner.md
│
├── skills/                         # Reusable skill definitions
│   ├── validate-graphql.md
│   ├── validate-mcp.md
│   ├── run-migrations.md
│   └── ...
│
├── patterns/                       # Code pattern documentation
│   ├── three-layer-database.md
│   ├── graphql-schema.md
│   ├── provider-pattern.md
│   └── ...
│
├── workflows/                      # Development process documentation
│   ├── sprint-workflow-v2.md
│   ├── development-sequence.md
│   └── ...
│
├── scripts/
│   ├── init-from-template.sh      # 🆕 Create project from template
│   └── setup-claude.sh            # Set up ~/.claude symlinks
│
├── sprint-steps.json               # Sprint workflow step definitions
└── ADR-SYNTHESIS.md                # Architecture decision reference
```

## Full-Stack Template 🆕

Get a production-ready FastAPI + Next.js application in 30 seconds:

**Includes:**
- ✅ FastAPI + Strawberry GraphQL backend
- ✅ Next.js 14 + TypeScript + shadcn/ui frontend
- ✅ SQLAlchemy 2.0 (async) + Alembic migrations
- ✅ Docker Compose for local development
- ✅ GitHub Actions CI/CD
- ✅ Pre-commit hooks (ruff, eslint, commitlint)
- ✅ Example sprint files following claude-maestro format
- ✅ Comprehensive documentation (README, STACK, CLAUDE)

**Tech Stack:**
- Backend: Python 3.11+, FastAPI, GraphQL, PostgreSQL
- Frontend: Next.js 14, React 18, TypeScript, Tailwind CSS
- DevOps: Docker, GitHub Actions, pre-commit

See [templates/full-stack-template/README.md](templates/full-stack-template/README.md) for details.

## Sprint Workflow

The playbook includes a complete sprint workflow system:

```bash
/sprint-start 1      # Initialize sprint, spawn Plan agent
/sprint-next 1       # Advance to next step
/sprint-status 1     # Check current progress
/sprint-complete 1   # Finish sprint with checklist
```

### Workflow Phases

| Phase | Steps | Description |
|-------|-------|-------------|
| 1. Planning | 1.1-1.4 | Read sprint, design architecture, clarify requirements |
| 2. Implementation | 2.1-2.4 | TDD: write tests, implement, run tests, fix failures |
| 3. Validation | 3.1-3.4 | Verify migrations, quality review, refactor |
| 4. Documentation | 4.1 | Generate dialog examples |
| 5. Commit | 5.1 | Stage and commit changes |
| 6. Completion | 6.1-6.4 | Update sprint file, checklist, close |

See example sprints in [templates/full-stack-template/docs/sprints/examples/](templates/full-stack-template/docs/sprints/examples/)

## Epic Management

Organize sprints into epics:

```bash
/epic-new            # Create new epic
/epic-start 1        # Start working on epic
/epic-status 1       # Check epic progress
/epic-complete 1     # Complete epic
```

## Commands Reference

### Sprint Commands
| Command | Description |
|---------|-------------|
| `/sprint-new` | Create a new sprint from template |
| `/sprint-start <N>` | Initialize and start sprint N |
| `/sprint-next <N>` | Advance to next step |
| `/sprint-status <N>` | Show current progress |
| `/sprint-complete <N>` | Run checklist and complete |
| `/sprint-blocked <N>` | Mark as blocked |
| `/sprint-abandon <N>` | Abandon sprint |

### Epic Commands
| Command | Description |
|---------|-------------|
| `/epic-new` | Create new epic |
| `/epic-start <N>` | Start epic |
| `/epic-status <N>` | Show epic status |
| `/epic-list` | List all epics |
| `/epic-complete <N>` | Complete epic |
| `/epic-archive <N>` | Archive completed epic |

### Project Commands
| Command | Description |
|---------|-------------|
| `/project-create` | Initialize new project |
| `/project-update` | Sync workflow updates |

## Documentation

### 🆕 Getting Started Guides
- **[Project Bootstrap Guide](playbooks/project-bootstrap-guide.md)** - Complete step-by-step guide to starting a new project (Phase 0-6, ~4 hours first time)
- **[Pattern Implementation Sequence](playbooks/pattern-implementation-sequence.md)** - What order to implement patterns, decision trees, epic sizing

### Workflows
- [Sprint Workflow v2](workflows/sprint-workflow-v2.md) - Complete sprint lifecycle
- [Development Infrastructure](workflows/development-infrastructure.md) - Agents, skills, commands
- [Development Sequence](workflows/development-sequence.md) - Day-to-day workflow
- [Documentation Approach](workflows/documentation-approach.md) - How to document

### Patterns
- [Three-Layer Database](patterns/three-layer-database.md) - PostgreSQL + SQLAlchemy + GraphQL
- [GraphQL Schema](patterns/graphql-schema.md) - GraphQL with Strawberry
- [Provider Pattern](patterns/provider-pattern.md) - External data abstraction
- [MCP Tool Registry](patterns/mcp-tool-registry.md) - LLM tool definitions
- [Session Factory Testing](patterns/session-factory-testing.md) - Async database sessions

### Playbooks
- **[Project Bootstrap Guide](playbooks/project-bootstrap-guide.md)** - Start a new project from scratch
- **[Pattern Implementation Sequence](playbooks/pattern-implementation-sequence.md)** - What to build in what order
- [Adding External Data Source](playbooks/adding-external-data-source.md)
- [Onboarding MCP Tool](playbooks/onboarding-mcp-tool.md)
- [Project Execution Lessons](playbooks/project-execution-lessons.md) - Learnings from 109 sprints

## How It Works

### For New Projects

Use the full-stack template to start a new project:

```bash
./scripts/init-from-template.sh my-app "My App Name"
```

This creates a complete project with:
- Working backend and frontend
- Docker development environment
- CI/CD configured
- Sprint workflow ready
- Example sprints to learn from

### For Existing Projects

The playbook uses symlinks to integrate with Claude Code:

```
~/.claude/
├── commands -> /path/to/ai-playbook/commands/
├── agents -> /path/to/ai-playbook/agents/
├── skills -> /path/to/ai-playbook/skills/
├── templates -> /path/to/ai-playbook/templates/
└── sprint-steps.json -> /path/to/ai-playbook/sprint-steps.json
```

This means:
- **Single source of truth**: All commands live in the playbook repo
- **Easy updates**: `git pull` updates all your commands
- **Portable**: Clone on new machine, run setup script, done

## Real-World Examples

This playbook is battle-tested on real projects:

- **vericorr**: 109 sprints, 13 epics, 6 weeks - Full pipeline integrity platform
- **claude-maestro**: Active development - Sprint workflow v3.0 system

Example sprint files follow the proven patterns from these projects.

## Learning Path

### Day 1: Bootstrap (30 minutes)
1. Run `./scripts/init-from-template.sh`
2. Start with `make dev`
3. See it working at http://localhost:3000

### Day 2-3: Learn (2-3 hours)
1. Read [STACK.md](templates/full-stack-template/STACK.md) - understand WHY
2. Read [Project Bootstrap Guide](playbooks/project-bootstrap-guide.md) - learn HOW
3. Look at example sprints - see the pattern

### Week 1: Build (5-10 hours)
1. Customize domain models
2. Create first sprint
3. Follow [Pattern Implementation Sequence](playbooks/pattern-implementation-sequence.md)

### Week 2+: Ship
- Use sprint workflow for all features
- Reference patterns as needed
- Deploy with included CI/CD

## Architecture Decisions

See [ADR-SYNTHESIS.md](ADR-SYNTHESIS.md) for a complete reference of architectural decisions from the vericorr project, organized by category with playbook mapping.

## Contributing

1. Fork the repo
2. Make changes to commands/patterns/workflows/templates
3. Test with a real project
4. Submit PR

## License

MIT
