---
globs: "**/*.py"
---

# Python Backend Conventions

## Code Style
- Follow PEP 8. Use ruff for linting and formatting.
- All functions and methods must have type hints for parameters and return values.
- Prefer `async def` for route handlers and I/O-bound operations.
- Use Pydantic `BaseModel` for all request/response schemas — never pass raw dicts across boundaries.
- Use dependency injection via FastAPI's `Depends()` for database sessions, auth, and config.
- Raise `HTTPException` with specific status codes — never return error dicts manually.
- Keep route handlers thin: validate input, call a service function, return the result.
- Business logic lives in `services/`, not in route handlers or models.
- Database queries go through repository functions or SQLAlchemy ORM — no raw SQL unless justified with a comment.
- Use `logging` module (not print) for all diagnostic output.
- Imports: stdlib first, then third-party, then local — ruff enforces this.

## Documentation
- Every module must have a module-level docstring describing its purpose and responsibility.
- Every public function and method must have a Google-style docstring with: summary line, Args, Returns, and Raises sections.
- Every class must have a class-level docstring explaining what it represents and its key behavior.
- Use inline comments only for non-obvious logic — explain "why", not "what".
- API route handlers must include a `summary` and `description` parameter for OpenAPI docs.
- Pydantic models must use `Field(description=...)` for every field to generate clear API documentation.
- Keep a `README.md` in each major package directory (`api/`, `services/`, `models/`) explaining the package's role and listing its key modules.
- Update docstrings when changing function signatures or behavior — stale docs are worse than no docs.
