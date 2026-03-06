# 001 — Project Setup

**Date:** 2026-03-06

## Context

New repository for simple demos in various languages and frameworks. Goal: learn useful technologies with AI-driven development best practices using Cursor.

## Decisions

### Demo structure
- Each demo is a self-contained folder at the project root
- Folder naming: `{language}-{framework}` in kebab-case, variants with descriptive suffix
- Every demo must include: README.md, Dockerfile, at least one test, standard entrypoint
- Dependency files only when needed

### Documentation
- All READMEs and code comments in English
- Demo READMEs follow a fixed format: Title, Description, Prerequisites, Installation, Run
- Root README contains a table of all demos

### Code philosophy
- Strict minimum — simplest possible working example
- Idiomatic style per language/framework

### Git workflow
- Conventional Commits format
- Scope only when targeting a specific demo
- Flexible commit granularity

### Cursor configuration
- 8 rules in `.cursor/rules/`: naming, structure, readme, code-style, git, workflow, scope, shell
- 4 skills in `.cursor/skills/`: scaffold-demo, validate-demo, docker-run, git-commit
- Shell rule enforces PowerShell-compatible syntax (Windows environment)
- Workflow rule: ask before (if ambiguous), always review after, re-review after corrections
- Scope rule: do only what is explicitly asked

## Alternatives considered

- Single monolithic project rule → rejected in favor of one rule per concern
- Personal skills (~/.cursor/skills/) → chose project-level for shareability
- Bash syntax → incompatible with Windows/PowerShell environment
