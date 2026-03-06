"""Validate a demo folder against project rules."""

import sys
from pathlib import Path

ENTRYPOINTS = {
    "python": ["main.py", "app.py"],
    "typescript": ["index.ts", "main.ts"],
    "javascript": ["index.js", "main.js"],
    "rust": ["src/main.rs"],
    "go": ["main.go"],
    "java": ["Main.java"],
    "c": ["main.c"],
    "cpp": ["main.cpp"],
}

README_SECTIONS = ["prerequisites", "run"]
README_MUST_HAVE_DESCRIPTION = True


def validate(demo_path: Path) -> list[str]:
    errors = []

    name = demo_path.name
    if name != name.lower() or " " in name or "_" in name:
        errors.append(f"Folder name '{name}' is not kebab-case")

    if not (demo_path / "README.md").exists():
        errors.append("Missing README.md")
    else:
        readme = (demo_path / "README.md").read_text(encoding="utf-8")
        readme_lower = readme.lower()

        if not readme.startswith("# "):
            errors.append("README.md missing title (should start with '# ')")

        if README_MUST_HAVE_DESCRIPTION:
            lines = readme.strip().split("\n")
            has_desc = any(
                l.strip() and not l.startswith("#") for l in lines[1:5]
            )
            if not has_desc:
                errors.append("README.md missing description after title")

        for section in README_SECTIONS:
            if f"## {section}" not in readme_lower:
                errors.append(f"README.md missing '## {section.title()}' section")

    if not (demo_path / "Dockerfile").exists():
        errors.append("Missing Dockerfile")

    lang = name.split("-")[0] if "-" in name else name
    candidates = ENTRYPOINTS.get(lang, [])
    if candidates and not any((demo_path / f).exists() for f in candidates):
        errors.append(f"No entrypoint found (expected one of: {', '.join(candidates)})")

    test_patterns = ["test_*", "*_test.*", "*.test.*", "*Test*", "tests/"]
    has_test = any(
        list(demo_path.glob(p)) for p in test_patterns
    )
    if not has_test:
        errors.append("No test file found")

    root_readme = demo_path.parent / "README.md"
    if root_readme.exists():
        content = root_readme.read_text(encoding="utf-8")
        if name not in content:
            errors.append(f"Demo '{name}' not listed in root README.md")

    return errors


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate.py <demo-folder>")
        sys.exit(1)

    demo_path = Path(sys.argv[1])
    if not demo_path.is_dir():
        print(f"Error: '{demo_path}' is not a directory")
        sys.exit(1)

    errors = validate(demo_path)

    if errors:
        print(f"FAIL — {len(errors)} issue(s) found in '{demo_path.name}':")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"PASS — '{demo_path.name}' is valid")


if __name__ == "__main__":
    main()
