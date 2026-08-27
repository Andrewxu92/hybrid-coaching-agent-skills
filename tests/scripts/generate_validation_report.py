#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
fixture = json.loads((ROOT / "tests/scenarios/router-fixtures.json").read_text(encoding="utf-8"))
valid_routes = set(p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md"))
valid_routes.update(
    p.parent.name
    for p in (ROOT / "integration" / "patch").glob("*/SKILL.md")
    if p.parent.name != "patch"
)
valid_routes.update(
    {
        "strength-method-selector",
        "endurance-method-selector",
        "speed-agility-method-selector",
    }
)
missing = []
for row in fixture:
    route = row.get("route", row.get("primary"))
    if route not in valid_routes:
        missing.append(row)
report = {
    "scenario_count": len(fixture),
    "known_routes": sorted(valid_routes),
    "missing_route_references": missing,
    "status": "PASS" if not missing else "FAIL",
}
print(json.dumps(report, ensure_ascii=False, indent=2))
if missing:
    raise SystemExit(1)
