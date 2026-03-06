---
name: git-commit
description: Analyze changes and create a git commit with a conventional commit message. Use when the user asks to commit, save progress, or says "commit".
---

# Git Commit

## Workflow

1. **Run `git status` and `git diff`** to understand all changes
2. **Propose what to stage** — list the files and ask for confirmation before running `git add`
3. **Draft a commit message** following `git-conventions` rule:
   - Conventional Commits format (`feat:`, `fix:`, `docs:`, `chore:`...)
   - Add a scope when the commit targets a specific demo (e.g. `feat(python-fastapi): add demo`)
   - No scope for cross-cutting changes (e.g. `chore: add .gitignore`)
4. **Present the message** and wait for user approval
5. **Commit** only after explicit confirmation

## Message guidelines

- One short line (max ~72 chars), lowercase, no period
- Focus on the "why" or "what", not the "how"
- If multiple logical changes exist, suggest splitting into separate commits
