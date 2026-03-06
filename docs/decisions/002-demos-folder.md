# 002 — Move demos into `demos/` folder

**Date:** 2026-03-07

## Context

With 8 demos planned on the roadmap, having each demo folder at the project root would clutter it alongside `.cursor/`, `docs/`, and `README.md`. With only 2 demos completed, this was the cheapest time to restructure.

## Decisions

- All demo folders now live under `demos/` (e.g. `demos/python/`, `demos/javascript-node/`)
- Root README links updated to point to `demos/{name}/`
- `validate.py` updated to find the root README regardless of demo depth
- `scaffold-demo` skill updated to create folders inside `demos/`
- ADR 001 statement "self-contained folder at the project root" is superseded by this decision

## Alternatives considered

- Keep demos at root → rejected because it does not scale to 8+ folders
- Use a `src/` folder → rejected because `demos/` better conveys intent
