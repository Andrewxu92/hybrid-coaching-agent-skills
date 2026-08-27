#!/usr/bin/env python3
from pathlib import Path
import re
import sys

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: python -m pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted(p.parent for p in (ROOT / "skills").glob("*/SKILL.md"))
PATCHES = sorted(p.parent for p in (ROOT / "integration" / "patch").glob("*/SKILL.md"))
errors = []
checked = []

name_re = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*$")

for skill_dir in SKILLS + PATCHES:
    path = skill_dir / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{path}: missing YAML frontmatter")
        continue
    end = text.find("\n---\n", 4)
    if end == -1:
        errors.append(f"{path}: invalid frontmatter terminator")
        continue
    try:
        frontmatter = yaml.safe_load(text[4:end]) or {}
    except Exception as exc:
        errors.append(f"{path}: YAML parse error: {exc}")
        continue

    name = frontmatter.get("name")
    desc = frontmatter.get("description")
    if not isinstance(name, str):
        errors.append(f"{path}: name must be a string")
    elif not (1 <= len(name) <= 64):
        errors.append(f"{path}: name length must be 1-64")
    elif not name_re.fullmatch(name) or "--" in name:
        errors.append(f"{path}: invalid name {name!r}")
    elif name != skill_dir.name:
        errors.append(f"{path}: name {name!r} does not match directory {skill_dir.name!r}")

    if not isinstance(desc, str) or not desc.strip():
        errors.append(f"{path}: description must be a non-empty string")
    elif len(desc) > 1024:
        errors.append(f"{path}: description exceeds 1024 characters")

    if len(text.splitlines()) > 500:
        errors.append(f"{path}: SKILL.md exceeds recommended 500-line limit")

    for ref in re.findall(r"\]\((references/[^)]+)\)", text):
        target = skill_dir / ref
        if not target.exists():
            errors.append(f"{path}: missing referenced file {ref}")

    checked.append((name or "<missing>", len(desc) if isinstance(desc, str) else 0))

names = [name for name, _ in checked]
if len(names) != len(set(names)):
    errors.append("duplicate skill names")

print(f"Skills checked: {len(SKILLS)} canonical + {len(PATCHES)} integration patches")
for name, n in checked:
    print(f"  OK  {name} (description {n} chars)")
if errors:
    print("\nERRORS")
    for err in errors:
        print(f"- {err}")
    raise SystemExit(1)
print("\nPASS")
