# [PROJECT_NAME]

## Overview
[ONE_SENTENCE_DESCRIPTION]

## Tech Stack
- **Backend**: Python 3.12+ / FastAPI / SQLAlchemy / Alembic
- **Frontend**: React 18+ / TypeScript / Vite
- **Database**: [DATABASE — e.g., PostgreSQL 16]
- **Testing**: pytest (backend), Vitest + React Testing Library (frontend)
- **Linting**: ruff (backend), ESLint + Prettier (frontend)

## Commands
```bash
# Backend
cd backend && pip install -e ".[dev]"   # Install
pytest                                   # Test all
pytest tests/unit                        # Unit tests
pytest tests/integration                 # Integration tests
pytest -x -k "test_name"                # Single test
ruff check . && ruff format --check .   # Lint
uvicorn app.main:app --reload           # Run dev server

# Frontend
cd frontend && npm install              # Install
npm test                                # Test all
npm run dev                             # Run dev server
npm run build                           # Production build
npm run lint                            # Lint
```

## Project Structure
```
[PROJECT_NAME]/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/          # Route handlers
│   │   ├── models/       # SQLAlchemy models
│   │   ├── schemas/      # Pydantic schemas
│   │   ├── services/     # Business logic
│   │   └── core/         # Config, deps, security
│   └── tests/
│       ├── unit/
│       ├── integration/
│       └── conftest.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── pages/
│   │   ├── services/     # API client
│   │   └── types/
│   └── tests/
└── TODO.md
```

## Architecture
- [DESCRIBE_KEY_ARCHITECTURAL_DECISIONS]
- REST API with versioned endpoints (`/api/v1/`)
- JWT authentication with refresh tokens
- Repository pattern for data access

## Coding Conventions
- TDD: write failing test first, then implement, then refactor
- All functions have type hints (Python) or TypeScript types
- No `Any` types unless unavoidable — add a comment explaining why
- Commits: conventional commits format (`feat:`, `fix:`, `test:`, etc.)

## Documentation Standards
- Every module/file: top-level docstring describing purpose and responsibility
- Every public function/method: Google-style docstring (Python) or JSDoc (TypeScript) with params, returns, and raises/throws
- Every class/component: docstring explaining what it represents and key behavior
- Package directories (`api/`, `services/`, `models/`, `components/`, `hooks/`): include a `README.md` listing key modules and the package's role
- API endpoints: `summary` and `description` for OpenAPI; Pydantic fields use `Field(description=...)`
- Tests: module docstring, descriptive names, comment references to bug tickets where applicable
- Inline comments: explain "why", never "what" — if the code needs a "what" comment, refactor for clarity
- Stale docs are worse than no docs — update documentation whenever behavior changes

## Environment
- Python virtual env: `backend/.venv`
- Node version: 20+ (via `.nvmrc`)
- Environment variables: see `backend/.env.example`
