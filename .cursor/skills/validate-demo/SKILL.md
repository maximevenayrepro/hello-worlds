---
name: validate-demo
description: Validate that a demo folder respects all project rules. Use when verifying a demo, after scaffolding, or when the user asks to check or validate a demo.
---

# Validate Demo

## Workflow

1. **Identify the demo folder** to validate (ask if ambiguous)
2. **Run the validation script**: `python .cursor/skills/validate-demo/scripts/validate.py {demo-folder}`
3. **Review the output** — the script checks all project rules
4. **Report findings** to the user with pass/fail for each check
5. **If failures exist**, propose fixes and ask for confirmation

## What is checked

- Folder name matches `naming-conventions` (kebab-case, `{lang}-{framework}` pattern)
- `README.md` exists and has required sections (Title, Description, Prerequisites, Installation, Run)
- Standard entrypoint file exists
- `Dockerfile` exists
- At least one test file exists
- Demo is listed in the root `README.md` table
