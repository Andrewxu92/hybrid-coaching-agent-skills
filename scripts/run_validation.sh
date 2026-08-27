#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
python scripts/validate_skills.py
python tests/scripts/router-regression.py
python tests/scripts/semantic-acceptance.py
python tests/scripts/install-smoke.py
echo "All deterministic checks passed."
