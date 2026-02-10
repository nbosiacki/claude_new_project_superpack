---
name: code-review
description: Review code for bugs, style violations, security issues, documentation gaps, and test coverage. Outputs a structured review with severity levels.
user_invocable: true
---

# Code Review

Perform a structured code review on specified files or recent changes.

## Steps

1. **Identify scope**: If the user specifies files, review those. Otherwise, use `git diff` to find recently changed files.

2. **Review each file** for:
   - **Bugs**: Logic errors, off-by-one, null/undefined access, race conditions, resource leaks
   - **Style**: Violations of project conventions in `.claude/rules/`
   - **Security**: Injection, auth bypass, data exposure, insecure defaults (OWASP Top 10)
   - **Performance**: N+1 queries, unnecessary re-renders, missing indexes, large payloads
   - **Documentation**: Missing or stale docstrings, undocumented public APIs, missing JSDoc/Google-style docs, missing module docstrings, unclear parameter descriptions
   - **Test coverage**: Missing tests for new functionality, untested error paths

3. **Output structured review**:

## Output Format

For each finding:

```
### [SEVERITY] [Category] — file:line

**Issue**: Description of the problem.

**Why it matters**: Impact if not fixed.

**Suggestion**:
\`\`\`language
// Proposed fix
\`\`\`
```

Severity levels:
- **CRITICAL** — Bugs or security issues that must be fixed before merge
- **WARNING** — Problems that should be fixed but aren't blocking
- **INFO** — Style nits, suggestions, minor improvements
- **DOCS** — Missing or inaccurate documentation that needs attention

End with a summary:

```
## Summary
- X critical, Y warnings, Z info, W docs
- Overall: APPROVE / REQUEST CHANGES / NEEDS DISCUSSION
- Documentation coverage: [assessment of doc completeness]
- Key themes: [common patterns across findings]
```

## Rules
- Be specific — reference exact line numbers and variable names.
- Provide a fix, not just a complaint. Every finding should have a suggestion.
- Don't flag things that are intentional project conventions (check `.claude/rules/`).
- Prioritize: bugs and security first, then documentation, then style.
- Flag any public function, class, or module missing documentation as a DOCS finding.
- If the code is good, say so. Not every review needs findings.
