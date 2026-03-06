---
name: scaffold-demo
description: Scaffold a new hello-world demo with standard structure. Use when creating a new demo, adding a new language or framework, or when the user says "new demo" or "add a demo".
---

# Scaffold Demo

## Workflow

1. **Determine the demo name** following `naming-conventions` rule: `{language}-{framework}` in kebab-case
2. **Create the folder** inside `demos/` at the project root
3. **Generate all required files** per `demo-structure` rule:
   - `README.md` following `readme-standards` rule
   - Standard entrypoint for the language (`main.py`, `index.ts`, `main.rs`...)
   - Dependency file only if needed
   - `Dockerfile` that builds and runs the demo
   - At least one minimal test
4. **Update the root `README.md`** — add a row to the Demos table with language, framework, and description
5. **Run the `validate-demo` skill** to verify everything is correct

## Code principles

- Strict minimum code — the simplest possible working example
- Follow the idiomatic style of the language/framework
- Comments in English, only when non-obvious

## Templates

See [templates/](templates/) for reference examples. Adapt to the target language — do not copy blindly.
