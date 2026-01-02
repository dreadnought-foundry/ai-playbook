---
sprint: 1
title: "Add Task Priority Field"
status: todo
epic: 1
type: backend-only
created: 2026-01-02
started: null
completed: null
hours: null
---

# Sprint 1: Add Task Priority Field

## Overview

| Field | Value |
|-------|-------|
| Sprint | 1 |
| Title | Add Task Priority Field |
| Epic | 01 - Task Management |
| Type | backend-only |
| Status | Todo |
| Created | 2026-01-02 |

## Goal

Add a priority field to the Task model allowing users to mark tasks as low, medium, or high priority.

## Background

Users need to prioritize their tasks. Currently, there's no way to mark task importance in the system. This is a foundational field that will be used for sorting and filtering in future sprints.

## Tasks

### Phase 1: Database Changes
- [ ] Add `priority` column to Task model (low/medium/high)
- [ ] Create Alembic migration
- [ ] Add index on priority column (for filtering)
- [ ] Update seed data to include priorities

### Phase 2: GraphQL Updates
- [ ] Add PriorityEnum to GraphQL types
- [ ] Update Task GraphQL type with priority field
- [ ] Update CreateTaskInput to accept priority
- [ ] Add priority filter to tasks query

### Phase 3: Testing
- [ ] Test creating task with priority
- [ ] Test filtering by priority
- [ ] Test default priority (medium)
- [ ] Verify migration up/down

## Model Schema

```python
# backend/src/db/models.py
class Task(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "tasks"

    project_uuid: Mapped[UUID] = mapped_column(ForeignKey("projects.uuid"))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="todo", nullable=False)
    priority: Mapped[str] = mapped_column(String(20), default="medium", nullable=False, index=True)  # NEW
    completed: Mapped[bool] = mapped_column(default=False, nullable=False)
```

## Acceptance Criteria

- [ ] Priority field added to database
- [ ] Migration applied successfully
- [ ] GraphQL query returns priority
- [ ] Can create task with priority
- [ ] Can filter tasks by priority
- [ ] Tests pass with >= 75% coverage
- [ ] No lint errors

---

## Team Strategy

*Populated by Plan agent during sprint start*

### Sprint Type
- **Type**: backend-only
- **Parallelism**: No (simple sequential implementation)

### Agent Assignments

| Agent | Role | Files Owned | Skills |
|-------|------|-------------|--------|
| product-engineer | Backend developer | backend/src/db/models.py<br>backend/src/api/graphql/types.py<br>backend/src/api/graphql/schema.py<br>backend/alembic/versions/*.py | run-migrations |

### File Ownership

```
Backend agent owns:
  backend/src/db/models.py (modify Task model)
  backend/src/api/graphql/types.py (add PriorityEnum, modify Task type)
  backend/src/api/graphql/schema.py (add priority filter)
  backend/alembic/versions/xxx_add_priority.py (create)
  backend/tests/test_sprint01_priority.py (create)
```

### Integration Strategy

Sequential implementation:
1. Database model changes
2. Migration creation and testing
3. GraphQL schema updates
4. Tests

### TDD Approach

- [ ] **Strict TDD** (tests before code)
- [x] **Flexible TDD** (tests alongside code) - Default for this sprint
- [ ] **Coverage-based** (tests after, hit 75%)

**Justification**: Simple field addition, flexible TDD is appropriate.

---

## Notes

**Priority**: High (blocking Sprint 2 which needs priority for UI)
**Estimated Effort**: 2-3 hours
**Dependencies**: None

Reference: Similar pattern used in vericorr Sprint 45 (adding status field).
