---
name: plan-project
description: Enter planning mode to analyze the project state and create a structured implementation plan for the next task.
user_invocable: true
---

# Plan Project

Enter planning mode and create a structured implementation plan.

## Steps

1. **Read context**: Read `CLAUDE.md` and `TODO.md` to understand the project configuration and current progress.

2. **Identify next task**: Find the first unchecked item in the current phase of `TODO.md`. If the current phase is complete, identify the transition to the next phase.

3. **Analyze dependencies**: Check what existing code, tests, and infrastructure the task depends on. Read relevant source files.

4. **Create plan**: Output a structured plan with these sections:

   ### Task
   One-line description of what we're implementing.

   ### Context
   What exists already that this task builds on.

   ### Approach
   Numbered steps to implement, including:
   - Which files to create or modify
   - Test files to write first (TDD)
   - Documentation to write or update (docstrings, README sections, API docs)
   - Key design decisions and trade-offs

   ### Documentation Checklist
   - [ ] Module docstrings for all new files
   - [ ] Function/method docstrings (Google-style for Python, JSDoc for TS)
   - [ ] Update relevant package README.md
   - [ ] Update API documentation if endpoints change
   - [ ] Update CLAUDE.md if project structure changes

   ### Acceptance Criteria
   - [ ] Checklist of what "done" looks like
   - [ ] Include "all tests pass" as a criterion
   - [ ] Include "all new code is documented" as a criterion

   ### Risks / Open Questions
   Anything that might block progress or needs clarification.

5. **Wait for approval**: Do not proceed to implementation until the user approves the plan.

## Tools
Use only read-only tools: Read, Glob, Grep, Bash (for `git log`, `git status` only). Do not modify any files.
