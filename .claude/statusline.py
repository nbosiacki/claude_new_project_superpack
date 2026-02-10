#!/usr/bin/env python3
"""Claude Code status line: model, project, context usage, tokens, cost."""

import json
import os
import sys


def format_tokens(n: int) -> str:
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.0f}k"
    return str(n)


def context_bar(pct: float) -> str:
    remaining = 100 - pct
    if remaining > 50:
        color = "\033[32m"  # green
    elif remaining > 20:
        color = "\033[33m"  # yellow
    else:
        color = "\033[31m"  # red
    reset = "\033[0m"
    filled = round(pct / 10)
    empty = 10 - filled
    return f"{color}[{'█' * filled}{'░' * empty}]{reset} {pct:.0f}%"


def main() -> None:
    raw = sys.stdin.read()
    if not raw.strip():
        return

    data = json.loads(raw)

    model = data.get("model", "unknown")
    cwd = os.path.basename(data.get("cwd", ""))
    project = os.path.basename(data.get("projectDir", ""))

    context_pct = 0.0
    total_tokens = data.get("totalTokens", 0)
    max_tokens = data.get("maxTokens", 0)
    if max_tokens > 0:
        context_pct = (total_tokens / max_tokens) * 100

    remaining = max_tokens - total_tokens
    cost = data.get("totalCost", 0.0)

    parts = [
        model,
        f"📁 {project or cwd}",
        context_bar(context_pct),
        f"{format_tokens(remaining)} left",
        f"${cost:.2f}",
    ]
    print(" | ".join(parts))


if __name__ == "__main__":
    main()
