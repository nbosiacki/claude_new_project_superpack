---
name: generate-todo
description: Create or update TODO.md with a phased project roadmap. Phase 1 has detailed checkboxes, later phases are high-level.
user_invocable: true
---

# Generate TODO

Create or update `TODO.md` with a structured, phased roadmap.

## Steps

1. **Read current state**: Read `CLAUDE.md` for project scope and `TODO.md` if it exists.

2. **Analyze the codebase**: Use Glob and Grep to understand what's already been implemented. Check for existing tests, models, routes, and components.

3. **Generate the roadmap**:

   **Phase 1** — detailed checkboxes:
   - Group tasks by category (Scaffolding, Data Model, Auth, Core API, Basic UI, CI/CD, Documentation)
   - Each task is a `- [ ]` checkbox item
   - Mark completed tasks as `- [x]` based on what already exists
   - Include documentation tasks in every category (docstrings, READMEs, API docs)
   - Add dependency notes between categories

   **Phases 2+** — high-level only:
   - 3-5 bullet points per phase describing goals, not tasks
   - Each phase builds on the previous one

4. **Apply status markers** to each phase:
   - `NOT STARTED` — no tasks begun
   - `IN PROGRESS` — at least one task checked
   - `DONE` — all tasks checked
   - `BLOCKED` — cannot proceed (add reason)

5. **Write TODO.md**: Use the exact format from the project's existing `TODO.md` template if one exists.

## Output Format

```markdown
# Project Roadmap

## Phase 1: [Name] — `STATUS`
### [Category]
- [ ] Task description
- [x] Completed task

### Documentation
- [ ] Write module docstrings for all new files
- [ ] Add package README.md files
- [ ] Document API endpoints in OpenAPI
- [ ] Create developer onboarding guide

> **Dependencies**: [Note any ordering requirements]

---

## Phase 2: [Name] — `NOT STARTED`
- Goal description
- Goal description
```

## Rules
- Phase 1 must be actionable — each checkbox should be completable in one coding session.
- Every category must include at least one documentation task.
- Don't over-plan future phases — they'll be detailed when the current phase nears completion.
- Preserve existing checkbox state when updating.
