#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./install-overlay.sh /path/to/skill-for-hirox
#
# Installs the v0.1.1 intelligence overlay and patches the four HYROX boundary skills.
# Existing training/nutrition skills are preserved.
#
# Expected upstream layout (skill-for-hirox):
#   hyrox-skills/hyrox-coach/SKILL.md
#   hyrox-skills/hyrox-needs-profile/SKILL.md
#   hyrox-skills/hyrox-week-template/SKILL.md
#   hyrox-skills/hyrox-plan-audit/SKILL.md

ROOT="${1:-}"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PACKAGE_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"
PATCH_NAMES=(hyrox-coach hyrox-needs-profile hyrox-week-template hyrox-plan-audit)

if [[ -z "$ROOT" || ! -d "$ROOT" ]]; then
  echo "Usage: $0 /path/to/skill-for-hirox" >&2
  exit 2
fi

if [[ ! -d "$ROOT/hyrox-skills" ]]; then
  echo "Expected upstream directory missing: $ROOT/hyrox-skills" >&2
  echo "This overlay targets https://github.com/Andrewxu92/skill-for-hirox" >&2
  exit 2
fi

CORE_SRC="$PACKAGE_ROOT/skills"
PATCH_SRC="$PACKAGE_ROOT/integration/patch"

if [[ -d "$PATCH_SRC/patch" ]]; then
  echo "Stale nested overlay found at $PATCH_SRC/patch; remove it before installing." >&2
  exit 2
fi

for name in "${PATCH_NAMES[@]}"; do
  src="$PATCH_SRC/$name/SKILL.md"
  target_dir="$ROOT/hyrox-skills/$name"
  if [[ ! -f "$src" ]]; then
    echo "Missing overlay patch: $src" >&2
    exit 2
  fi
  if [[ ! -d "$target_dir" ]]; then
    echo "Missing upstream skill directory: $target_dir" >&2
    exit 2
  fi
done

DEST="$ROOT/hybrid-core-skills"
mkdir -p "$DEST"
cp -R "$CORE_SRC/." "$DEST/"

for name in "${PATCH_NAMES[@]}"; do
  target="$ROOT/hyrox-skills/$name/SKILL.md"
  src="$PATCH_SRC/$name/SKILL.md"
  if [[ -f "$target" && ! -f "$target.pre-v0.1.1.bak" ]]; then
    cp "$target" "$target.pre-v0.1.1.bak"
  fi
  cp "$src" "$target"
done

echo "Installed v0.1.1 Hybrid Coaching overlay into: $ROOT"
