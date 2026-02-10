# Initial Project Bootstrap

Paste everything below into your first Claude Code session.

---

Enter planning mode. Do NOT write any implementation code. Your job is to plan only.

## Project Details

- **Project name**: [PROJECT_NAME]
- **Description**: [WHAT_DOES_THIS_PROJECT_DO]
- **Core features**: [LIST_3_TO_5_CORE_FEATURES]
- **User roles**: [e.g., admin, regular user, anonymous]
- **External APIs/services**: [e.g., Stripe, SendGrid, S3 — or "none"]
- **MVP scope**: [WHAT_IS_THE_MINIMUM_VIABLE_PRODUCT]

## What to Do

1. **Read** `CLAUDE.md` and `TODO.md` to understand the current project configuration.

2. **Scaffold directories** matching the project structure in `CLAUDE.md`:
   - Create all backend and frontend directories
   - Create `__init__.py` files in all Python packages
   - Create test directories mirroring the source structure
   - Add placeholder `conftest.py` files

3. **Generate TODO.md** using the `/generate-todo` skill:
   - Phase 1: detailed tasks with checkboxes for scaffolding, data model, auth, core API, basic UI, CI/CD
   - Phase 2+: high-level goals only (3-5 bullets per phase)

4. **Update CLAUDE.md**:
   - Replace all remaining `[BRACKETED]` placeholders with actual values
   - Update the project structure section to match what was scaffolded

5. **Output your plan** as a structured summary:
   - Proposed data models (entities and key fields)
   - API endpoint list (method, path, description)
   - Frontend page/component tree
   - Key technical decisions and trade-offs
   - Questions or ambiguities to resolve before implementation

Remember: **planning only** — no implementation code in this session.
