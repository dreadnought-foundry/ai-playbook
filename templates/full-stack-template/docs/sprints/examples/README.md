# Example Sprint Files

This directory contains example sprint files showing different patterns and types.

## Examples Included

### 1. sprint-01_example-backend-only.md
**Type:** backend-only
**Pattern:** Simple field addition
**Shows:**
- Database model changes
- Migration creation
- GraphQL schema updates
- Backend-only workflow

**Use this pattern for:**
- Adding fields to existing models
- Database schema changes
- GraphQL API additions
- Backend utilities

### 2. sprint-02_example-fullstack.md
**Type:** fullstack
**Pattern:** Feature with backend + frontend
**Shows:**
- Frontend depending on backend sprint
- UI component creation
- Type generation from GraphQL
- Filtering and sorting

**Use this pattern for:**
- Complete user-facing features
- UI + API work
- Features that span multiple layers

## Sprint Types

Based on claude-maestro workflow, we use these sprint types:

| Type | When to Use | Example |
|------|-------------|---------|
| **backend-only** | Database, API, or backend logic changes | Adding a field, migration, GraphQL query |
| **frontend-only** | UI changes using existing API | New page layout, component styling |
| **fullstack** | Feature requiring both backend and frontend | Complete feature: data + UI |
| **integration** | Connecting to external services | Provider pattern, external API |
| **data-layer** | Database-specific work | Migrations, seeding, PostGIS setup |

## Sprint File Structure

Every sprint follows this structure (from claude-maestro):

```markdown
---
sprint: {N}
title: "{TITLE}"
status: todo | in-progress | done | blocked | abandoned
epic: {EPIC_NUMBER}
type: backend-only | frontend-only | fullstack | integration | data-layer
created: YYYY-MM-DD
started: null | YYYY-MM-DDTHH:MM:SSZ
completed: null | YYYY-MM-DDTHH:MM:SSZ
hours: null | {number}
---

# Sprint {N}: {TITLE}

## Overview
## Goal
## Background
## Dependencies (if any)
## Tasks
## Model Schema (if applicable)
## Acceptance Criteria

---

## Team Strategy
(Populated by Plan agent during sprint start)

---

## Postmortem
(Populated after sprint completion)
```

## How to Use These Examples

### 1. Copy and Customize

```bash
# Copy example to your sprint directory
cp docs/sprints/examples/sprint-01_example-backend-only.md \
   docs/sprints/1-todo/sprint-03_add-due-dates.md

# Edit:
# - Sprint number
# - Title
# - Epic number
# - Tasks specific to your feature
```

### 2. Use the Sprint Template

```bash
# Use the sprint template for new sprints
cp docs/sprints/sprint-template.md \
   docs/sprints/1-todo/sprint-04_my-feature.md
```

### 3. Follow the Pattern

1. **Planning Phase:**
   - Fill in Overview, Goal, Background
   - List Tasks in logical phases
   - Define Acceptance Criteria

2. **Execution Phase:**
   - Update status: todo → in-progress
   - Let Plan agent fill Team Strategy
   - Work through tasks
   - Update timestamps

3. **Completion Phase:**
   - Mark status: done
   - Fill in hours
   - Complete Postmortem section
   - Move file to 3-done/

## Sprint Workflow Commands

```bash
# Create new sprint
/sprint-new "My Feature" --epic=1

# Start sprint
/sprint-start 1

# Check status
/sprint-status 1

# Move to next step
/sprint-next 1

# Complete sprint
/sprint-complete 1

# Generate postmortem
/sprint-postmortem 1
```

## Best Practices

From claude-maestro and vericorr experience:

1. **Keep Sprints Small:** 2-6 hours each
2. **Backend First:** Always build API before UI
3. **Clear Dependencies:** List what must be done first
4. **Specific Tasks:** Break down into 15-30 minute chunks
5. **Testable Criteria:** Acceptance criteria should be verifiable
6. **Track Time:** Record actual hours for planning future sprints

## Epic Organization

Sprints should be organized into epics:

```
docs/sprints/
├── 2-in-progress/
│   └── epic-01_task-management/
│       ├── sprint-01_add-priority-field/
│       │   └── sprint-01_add-priority-field.md
│       └── sprint-02_priority-ui/
│           └── sprint-02_priority-ui.md
```

See the sprint workflow documentation in ai-playbook for details.

## References

- **Sprint Template:** `docs/sprints/sprint-template.md`
- **Claude-Maestro:** Real sprints showing this pattern in action
- **Vericorr:** 109 sprints across 13 epics as reference
- **Playbook Workflows:** `ai-playbook/workflows/sprint-workflow-v2.md`
