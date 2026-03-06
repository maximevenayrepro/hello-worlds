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

Multi-step workflows the AI follows on demand:

| Skill | Purpose |
|-------|---------|
| `scaffold-demo` | Generate a new demo with all required files |
| `validate-demo` | Check a demo folder against every project rule |
| `git-commit` | Analyze changes and create a conventional commit |
| `docker-run` | Build and run a demo's Docker container |

### Subagents (`.cursor/agents/`)

Specialized agents that can be delegated tasks or invoked with `/name`:

| Subagent | Mode | Purpose |
|----------|:----:|---------|
| `tester` | readonly | Run validate + tests + Docker + browser on a demo |
| `verifier` | readonly | Confirm that completed work is actually functional |
| `debugger` | read/write | Diagnose errors and propose fixes |
| `researcher` | readonly | Search online for up-to-date docs and best practices |

### Documentation

- **ADRs** (`docs/decisions/`) — Architectural decisions with context, rationale, and alternatives
- **Plans** (`.cursor/plans/`) — Implementation plans for complex tasks

## Demos

| Language | Framework | Description |
|----------|-----------|-------------|
| [Python](python/) | — | Minimal HTTP server using the standard library |
