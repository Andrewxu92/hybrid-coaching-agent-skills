#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
scenarios = json.loads((ROOT / "tests/scenarios/routing.json").read_text(encoding="utf-8"))
expected = json.loads((ROOT / "tests/expected/routing-expected.json").read_text(encoding="utf-8"))["core"]
errors = []
for s in scenarios:
    e = expected.get(s["id"])
    if not e:
        errors.append(f"{s["id"]}: missing acceptance expectation")
        continue
    if e["route"] != s["primary"]:
        errors.append(f"{s["id"]}: route mismatch")
    if not s["prompt"].strip():
        errors.append(f"{s["id"]}: empty prompt")
required = [
    "Named skill request wins",
    "Missing data must remain `unknown`",
    "Known target wins over diagnosis",
    "Full-chain routing is only for compound tasks",
]
text = (ROOT / "docs/orchestration/routing-matrix.md").read_text(encoding="utf-8")
for phrase in required:
    if phrase not in text:
        errors.append("missing routing policy: " + phrase)
print(f"Acceptance fixtures: {len(scenarios)}")
if errors:
    print("FAIL")
    for e in errors: print(" -", e)
    sys.exit(1)
print("PASS")
