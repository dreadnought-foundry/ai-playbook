---
sprint: 2
title: "Task Priority UI"
status: todo
epic: 1
type: fullstack
created: 2026-01-02
started: null
completed: null
hours: null
---

# Sprint 2: Task Priority UI

## Overview

| Field | Value |
|-------|-------|
| Sprint | 2 |
| Title | Task Priority UI |
| Epic | 01 - Task Management |
| Type | fullstack |
| Status | Todo |
| Created | 2026-01-02 |

## Goal

Add UI controls for setting and filtering tasks by priority, using the priority field added in Sprint 1.

## Background

Sprint 1 added the priority field to the backend. Now we need to expose it in the UI so users can:
1. Set priority when creating a task
2. See priority badges on task cards
3. Filter tasks by priority
4. Sort tasks by priority

## Dependencies

- **Sprint 1 (Add Task Priority Field)** must be complete
- Backend must have priority field and GraphQL support

## Tasks

### Phase 1: Type Generation
- [ ] Run `npm run codegen` to get updated GraphQL types
- [ ] Verify Priority enum is available in frontend types

### Phase 2: Task Creation Form
- [ ] Add priority select dropdown to create task form
- [ ] Add priority badge component (color-coded)
- [ ] Default to "medium" priority

### Phase 3: Task Display
- [ ] Show priority badge on task cards
- [ ] Color code: low=green, medium=yellow, high=red
- [ ] Add priority icon (lucide-react)

### Phase 4: Filtering
- [ ] Add priority filter dropdown to task list
- [ ] Support multiple priority selection
- [ ] Update GraphQL query to use priority filter
- [ ] Add "All Priorities" option

### Phase 5: Sorting
- [ ] Add sort by priority option
- [ ] High → Medium → Low order
- [ ] Combine with existing date sort

## UI Components

```tsx
// New component: PriorityBadge
<PriorityBadge priority="high" />

// New component: PrioritySelect
<PrioritySelect
  value={priority}
  onChange={setPriority}
/>

// Modified: TaskCard
<TaskCard task={task}>
  <PriorityBadge priority={task.priority} />
  {/* ... */}
</TaskCard>
```

## Acceptance Criteria

- [ ] Can set priority when creating task
- [ ] Priority badge displays correctly (color-coded)
- [ ] Can filter by one or more priorities
- [ ] Can sort by priority
- [ ] GraphQL types generated and used
- [ ] No TypeScript errors
- [ ] Responsive on mobile
- [ ] Tests pass (when added)
- [ ] No lint errors

---

## Team Strategy

*Populated by Plan agent during sprint start*

### Sprint Type
- **Type**: fullstack
- **Parallelism**: No (frontend depends on Sprint 1 backend completion)

### Agent Assignments

| Agent | Role | Files Owned | Skills |
|-------|------|-------------|--------|
| product-engineer | Frontend developer | frontend/src/components/ui/priority-badge.tsx<br>frontend/src/components/ui/priority-select.tsx<br>frontend/src/app/tasks/page.tsx<br>frontend/src/app/tasks/create/page.tsx | validate-graphql |

### File Ownership

```
Frontend agent owns:
  frontend/src/components/ui/priority-badge.tsx (create)
  frontend/src/components/ui/priority-select.tsx (create)
  frontend/src/app/tasks/page.tsx (modify - add filtering/sorting)
  frontend/src/app/tasks/create/page.tsx (modify - add priority select)
  frontend/src/types/graphql.ts (generate via codegen)
```

### Integration Strategy

Sequential implementation:
1. Type generation (verify Sprint 1 schema)
2. UI components (PriorityBadge, PrioritySelect)
3. Task creation form integration
4. Task list filtering/sorting
5. Visual testing

### TDD Approach

- [ ] **Strict TDD** (tests before code)
- [x] **Flexible TDD** (tests alongside code) - Default for this sprint
- [ ] **Coverage-based** (tests after, hit 75%)

**Justification**: UI feature, flexible TDD with manual testing is appropriate.

---

## Design Notes

**Priority Colors (Tailwind):**
- Low: `bg-green-100 text-green-800 border-green-200`
- Medium: `bg-yellow-100 text-yellow-800 border-yellow-200`
- High: `bg-red-100 text-red-800 border-red-200`

**Icons (lucide-react):**
- Low: `ChevronDown`
- Medium: `Minus`
- High: `ChevronUp`

**Filter UI:**
- Multi-select checkbox dropdown (shadcn/ui)
- Position: Top of task list, next to search

**Sort Options:**
- Priority (High → Low)
- Priority (Low → High)
- Date created
- Due date (if added later)

---

## Notes

**Priority**: High (visible user feature)
**Estimated Effort**: 3-4 hours
**Dependencies**: Sprint 1 must be complete and deployed

Reference: Similar UI patterns in vericorr Sprint 89 (asset filtering).
