# Claude New Project Superpack

A reusable template that bootstraps Claude Code with a structured workflow: Python backend, React/TS frontend, TDD-first development, planning mode, and phased TODO tracking.

## What's Inside

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Project config loaded every Claude Code session |
| `INITIAL_PROMPT.md` | One-time bootstrap prompt for first session |
| `CLAUDE.local.md` | Personal overrides (gitignored) |
| `TODO.md` | Phased roadmap with checkboxes |
| `.gitignore-snippet` | Lines to add to your `.gitignore` |
| `settings-snippet.json` | Status line config for `~/.claude/settings.json` |
| `.claude/statusline.py` | Status line script (model, context %, tokens, cost) |
| `.claude/rules/*.md` | Auto-loading coding conventions by file type |
| `.claude/skills/*/SKILL.md` | Reusable skills: plan, TDD, TODO, code review |

## Setup

### 1. Copy to your project root

```bash
cp -r claude_new_project_superpack/* your-project/
cp -r claude_new_project_superpack/.claude your-project/
cp claude_new_project_superpack/.gitignore-snippet your-project/
```

### 2. Make the status line executable

```bash
chmod +x your-project/.claude/statusline.py
```

### 3. Merge status line settings

Add the contents of `settings-snippet.json` into your `~/.claude/settings.json`:

```bash
cat settings-snippet.json
# Manually merge the "status_line" key into ~/.claude/settings.json
```

### 4. Append to .gitignore

```bash
cat .gitignore-snippet >> your-project/.gitignore
```

### 5. Fill in CLAUDE.md placeholders

Open `CLAUDE.md` and replace all `[BRACKETED_CAPS]` placeholders with your project details.

### 6. Start your first session

Paste the contents of `INITIAL_PROMPT.md` into your first Claude Code session. This enters planning mode, scaffolds directories, and generates your TODO.md.

## Customizing for Other Stacks

- **Different backend**: Edit `.claude/rules/python-backend.md` or replace with your language's conventions. Update the `Tech Stack` section in `CLAUDE.md`.
- **Different frontend**: Edit `.claude/rules/react-frontend.md`. Change the glob pattern in the frontmatter to match your file extensions.
- **No frontend**: Delete `react-frontend.md` and remove the frontend section from `CLAUDE.md`.
- **Different test framework**: Edit `.claude/rules/testing.md` and update test commands in `CLAUDE.md`.

## Skills

Four starter skills are included in `.claude/skills/`:

- **plan-project** — Enter planning mode, analyze current state, output a structured plan
- **tdd-enforce** — Enforce test-first development: write test, see it fail, then implement
- **generate-todo** — Create or update TODO.md with phased structure
- **code-review** — Review code for bugs, style, security, and test coverage

See `.claude/skills/README.md` for how to create your own.
