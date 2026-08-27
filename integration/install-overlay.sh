#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./install-overlay.sh /path/to/skill-for-hirox
#
# Installs the v0.1.0 intelligence overlay and patches the four HYROX boundary skills.
# Existing training/nutrition skills are preserved.

ROOT="${1:-}"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PACKAGE_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"

if [[ -z "$ROOT" || ! -d "$ROOT" ]]; then
  echo "Usage: $0 /path/to/skill-for-hirox" >&2
  exit 2
fi

CORE_SRC="$PACKAGE_ROOT/skills"
PATCH_SRC="$PACKAGE_ROOT/integration/patch"
DEST="$ROOT/hybrid-core-skills"
mkdir -p "$DEST"
cp -R "$CORE_SRC/." "$DEST/"

for name in hyrox-coach hyrox-needs-profile hyrox-week-template hyrox-plan-audit; do
  target="$ROOT/hyrox-skills/$name/SKILL.md"
  src="$PATCH_SRC/$name/SKILL.md"
  if [[ -f "$target" && ! -f "$target.pre-v0.1.0.bak" ]]; then
    cp "$target" "$target.pre-v0.1.0.bak"
  fi
  mkdir -p "$(dirname "$target")"
  cp "$src" "$target"
done

echo "Installed v0.1.0 Hybrid Coaching overlay into: $ROOT"
