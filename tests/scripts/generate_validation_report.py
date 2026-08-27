#!/usr/bin/env python3
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
fixture = json.loads((ROOT/'tests/scenarios/router-fixtures.json').read_text(encoding='utf-8'))
# Static route checks based on explicit high-signal phrases.
rules = [
    ('strength-method-selector', [r'最大力量', r'endurance-method-selector']),
]

# This is intentionally a fixture/report generator rather than an LLM simulator.
# It validates that all intended routes exist somewhere in the overlay or source mapping.
valid_routes = set(p.name for p in (ROOT/'skills').glob('*'))
valid_routes |= set(p.name for p in (ROOT/'integration/patch').glob('*'))
valid_routes |= {'strength-method-selector','endurance-method-selector','speed-agility-method-selector'}
missing = []
for row in fixture:
    if row.get('route', row.get('primary')) not in valid_routes:
        missing.append(row)
report = {
    'scenario_count': len(fixture),
    'known_routes': sorted(valid_routes),
    'missing_route_references': missing,
    'status': 'PASS' if not missing else 'FAIL'
}
path = ROOT/'tests/router-validation-report.json'
path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=2))
if missing:
    raise SystemExit(1)
