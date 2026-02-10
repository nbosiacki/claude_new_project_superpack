# Claude Code Skills

Skills are reusable prompts that extend Claude Code's capabilities. They live in `.claude/skills/` and are defined in `SKILL.md` files.

## Directory Structure

```
.claude/skills/
├── README.md              # This file
├── skill-name/
│   └── SKILL.md          # Skill definition
└── another-skill/
    └── SKILL.md
```

## SKILL.md Format

Each `SKILL.md` contains:
- **Frontmatter**: metadata (name, description, invocation type)
- **Body**: the prompt instructions Claude follows when the skill is invoked

```markdown
---
name: skill-name
description: One-line description (this is how Claude decides when to use it)
user_invocable: true
---

# Skill Title

Instructions for Claude when this skill is invoked...
```

## Invocation Types

- **User-invoked** (`user_invocable: true`): User triggers with `/skill-name`. Use for explicit workflows like `/plan-project` or `/code-review`.
- **Model-invoked** (`user_invocable: false`): Claude triggers automatically when the description matches the current task. Use for conventions and guardrails.

## Design Principles

1. **Keep under 500 lines** — long skills get truncated or ignored.
2. **Description is the trigger** — for model-invoked skills, write the description as if answering "when should this activate?"
3. **Progressive disclosure** — start with the common case, add detail for edge cases.
4. **Specify tools** — tell Claude which tools to use (or avoid) for the task.
5. **Include examples** — show expected output format when the skill produces structured output.
