# Hello Worlds

A collection of minimal, self-contained demos across various languages and frameworks.

## Goals

- **Ready-to-run references** — One folder per stack with the strict minimum to go from zero to a running app, tests and Dockerfile included.
- **Side-by-side comparison** — See how different languages and frameworks handle the same basic concepts.
- **AI-driven development** — A playground for refining AI-assisted workflows: rules, skills, automated review, and structured processes.

## Structure

Each demo lives in its own folder following a consistent layout:

```
{language-framework}/
├── README.md          # What it does, how to run it
├── Dockerfile         # Run it anywhere
├── {entrypoint}       # main.py, index.ts, main.rs…
├── {deps file}        # Only if needed
└── {test file}        # At least one test
```

## AI-Driven Development

This project uses [Cursor](https://cursor.com) as its primary development environment. The `.cursor/` directory contains the configuration that makes AI a first-class contributor.

### Rules (`.cursor/rules/`)

Short, always-on constraints injected into every conversation: naming conventions, code style, commit format, demo structure, etc. They act as guardrails so the AI stays consistent without being told twice.

### Skills (`.cursor/skills/`)

Multi-step workflows the AI follows on demand. Invoked with `/skill-name` in chat:

| Skill | Trigger | Purpose |
|-------|---------|---------|
| `scaffold-demo` | `/scaffold-demo` | Generate a new demo with all required files |
| `validate-demo` | `/validate-demo` | Check a demo folder against every project rule |
| `git-commit` | `/git-commit` | Analyze changes and create a conventional commit |
| `docker-run` | `/docker-run` | Build and run a demo's Docker container |

### Why no Commands (`.cursor/commands/`)?

Commands are the older slash-shortcut mechanism in Cursor — simple markdown prompts in `.cursor/commands/` triggered by `/`. Since Cursor 2.4+, **Skills supersede Commands**: they live in `.cursor/skills/`, support richer multi-step workflows, and are invoked with the same `/` syntax. There is no reason to maintain both, so this project uses Skills exclusively.

## Demos

| Language | Framework | Description |
|----------|-----------|-------------|
| — | — | *Coming soon* |
