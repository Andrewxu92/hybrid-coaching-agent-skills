#!/usr/bin/env python3
import json
from pathlib import Path
import re
import sys

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: python3 -m pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted(p.parent for p in (ROOT / "skills").glob("*/SKILL.md"))
PATCHES = sorted(
    p.parent
    for p in (ROOT / "integration" / "patch").glob("*/SKILL.md")
    if p.parent.name != "patch"
)
errors = []
checked = []

nested_patch = ROOT / "integration" / "patch" / "patch"
if nested_patch.exists():
    errors.append("stale nested overlay directory: integration/patch/patch/")

manifest_path = ROOT / "repository-manifest.json"
static_path = ROOT / "tests" / "expected" / "static-validation.json"
version_path = ROOT / "VERSION"
if manifest_path.exists():
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("canonical_skill_count") != len(SKILLS):
        errors.append(
            "repository-manifest canonical_skill_count does not match skills/"
        )
    if manifest.get("integration_patch_count") != len(PATCHES):
        errors.append(
            "repository-manifest integration_patch_count does not match integration/patch/"
        )
    if version_path.exists() and version_path.read_text(encoding="utf-8").strip() != manifest.get("version"):
        errors.append("VERSION does not match repository-manifest.json version")
if static_path.exists():
    static = json.loads(static_path.read_text(encoding="utf-8"))
    actual_skills = ["skills/{0}/SKILL.md".format(p.name) for p in SKILLS]
    actual_patches = ["integration/patch/{0}/SKILL.md".format(p.name) for p in PATCHES]
    if static.get("canonical_skills") != actual_skills:
        errors.append("tests/expected/static-validation.json canonical_skills mismatch")
    if static.get("integration_patches") != actual_patches:
        errors.append("tests/expected/static-validation.json integration_patches mismatch")

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
