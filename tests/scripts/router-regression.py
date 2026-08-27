#!/usr/bin/env python3
"""Check routing fixtures against expected routes and local skill files."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UPSTREAM_ONLY = {
    "strength-method-selector",
    "endurance-method-selector",
    "speed-agility-method-selector",
    "periodization-planner",
    "session-plan-builder",
}


def local_skill_names():
    names = set(p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md"))
    names.update(
        p.parent.name
        for p in (ROOT / "integration" / "patch").glob("*/SKILL.md")
        if p.parent.name != "patch"
    )
    return names


def main():
    scenarios = json.loads((ROOT / "tests/scenarios/routing.json").read_text(encoding="utf-8"))
    expected = json.loads((ROOT / "tests/expected/routing-expected.json").read_text(encoding="utf-8"))["core"]
    fixtures = json.loads((ROOT / "tests/scenarios/router-fixtures.json").read_text(encoding="utf-8"))
    matrix = (ROOT / "docs/orchestration/routing-matrix.md").read_text(encoding="utf-8")
    local = local_skill_names()
    errors = []

    if (ROOT / "integration/patch/patch").exists():
        errors.append("stale nested overlay at integration/patch/patch/")

    fixture_by_id = dict((row["id"], row) for row in fixtures)
    if set(row["id"] for row in scenarios) != set(expected):
        errors.append("routing.json ids do not match routing-expected.json")

    for scenario in scenarios:
        sid = scenario["id"]
        primary = scenario["primary"]
        exp = expected.get(sid)
        fixture = fixture_by_id.get(sid)
        if exp is None:
            errors.append("{0}: missing acceptance expectation".format(sid))
            continue
        if exp["route"] != primary:
            errors.append(
                "{0}: expected route {1}, fixture primary {2}".format(
                    sid, exp["route"], primary
                )
            )
        if fixture is None:
            errors.append("{0}: missing router-fixtures.json entry".format(sid))
        elif fixture.get("primary") != primary:
            errors.append(
                "{0}: router-fixtures.json primary {1} != routing.json {2}".format(
                    sid, fixture.get("primary"), primary
                )
            )
        if not scenario["prompt"].strip():
            errors.append("{0}: empty prompt".format(sid))
        if primary in UPSTREAM_ONLY:
            if primary not in matrix:
                errors.append("{0}: upstream route {1} missing from routing matrix".format(sid, primary))
        elif primary not in local:
            errors.append("{0}: unknown local route {1}".format(sid, primary))

    print("Routing fixtures: {0}".format(len(scenarios)))
    if errors:
        print("FAIL")
        print("\n".join(errors))
        raise SystemExit(1)
    print("PASS")


if __name__ == "__main__":
    main()
