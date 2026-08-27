#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if command -v python3 >/dev/null 2>&1; then
  PYTHON=python3
elif command -v python >/dev/null 2>&1; then
  PYTHON=python
else
  echo "python3 or python is required" >&2
  exit 1
fi

"$PYTHON" scripts/validate_skills.py
"$PYTHON" tests/scripts/router-regression.py
"$PYTHON" tests/scripts/semantic-acceptance.py
"$PYTHON" tests/scripts/install-smoke.py
echo "All deterministic checks passed."
