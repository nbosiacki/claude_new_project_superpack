---
alwaysApply: true
---

# TDD Conventions (Always Active)

## Workflow: Red → Green → Refactor
1. **Red**: Write a failing test that describes the desired behavior.
2. **Green**: Write the minimum code to make the test pass.
3. **Refactor**: Clean up while keeping tests green.

Never skip step 1. If you're about to write implementation code without a test, stop and write the test first.

## Test Naming
- Python: `test_<what>_<condition>_<expected>` — e.g., `test_create_user_duplicate_email_raises_conflict`
- TypeScript: `describe("<Component>")` → `it("should <behavior> when <condition>")` — e.g., `it("should show error when email is invalid")`

## Test Structure
- Arrange / Act / Assert (Python) or Given / When / Then (TS)
- One assertion per test when possible — multiple assertions only if testing a single logical behavior
- Use fixtures and factories for test data — no hardcoded values scattered across tests

## Test Organization
- Mirror source directory structure: `app/services/user.py` → `tests/unit/services/test_user.py`
- Unit tests: no I/O, no database, mock external dependencies
- Integration tests: real database (test DB), real HTTP calls to the app
- E2E tests: browser automation for critical user flows

## What to Test
- All public functions and API endpoints
- Edge cases: empty inputs, boundary values, error conditions
- Auth: both authorized and unauthorized paths
- Do NOT test private/internal functions directly — test them through public interfaces

## Test Documentation
- Every test file must have a module-level docstring describing what module/component it tests and the testing strategy used.
- Test function names must be self-documenting — a reader should understand the scenario without reading the test body.
- Use comments within complex test setups to explain what scenario is being constructed and why.
- For integration tests, document any required external dependencies (database, services) and setup/teardown expectations.
- `conftest.py` files must document each fixture: what it provides, its scope, and any side effects.
- When a test covers a specific bug fix, include a comment referencing the issue number or a brief description of the bug.
