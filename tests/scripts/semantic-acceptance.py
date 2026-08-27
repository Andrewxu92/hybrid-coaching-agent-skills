#!/usr/bin/env python3
"""Check scenario contracts against skill text and routing policy."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
UPSTREAM_ONLY = {
    "strength-method-selector",
    "endurance-method-selector",
    "speed-agility-method-selector",
    "periodization-planner",
    "session-plan-builder",
}

# Required phrases that must appear in the owning skill or routing docs.
CONTRACTS = {
    "return_three_core_scores_or_unknown": ["unknown", "0–100"],
    "compare_athlete_with_demand": ["gap = demand - athlete"],
    "avoid_medical_diagnosis": ["not a medical diagnosis"],
    "choose_one_primary_target": ["primary_target"],
    "use_state_carryover": ["carry"],
    "return_one_immediate_action": ["action:"],
    "describe_sport_demand_only": ["does not calculate athlete gaps"],
    "preserve_selected_priority": ["preserve the selected training priority"],
    "audit_not_replace": ["do not generate a replacement plan"],
    "delegate_compound_flow": ["delegate"],
    "bypass_diagnosis": ["known target wins over diagnosis"],
    "allow_unclear_conflict": ["unclear"],
    "gap_90_minus_60_equals_30": ["gap = demand - athlete"],
    "use_unknown_not_fabrication": ["do not infer precise scores"],
    "not_call_hybrid_if_state_reset_is_sufficient": ["carry-over"],
    "recognize_meaningful_carryover": ["carry"],
    "check_gap_alignment": ["athlete-gap alignment"],
    "explicit_skill_request_wins": ["named skill request wins"],
    "start_with_assessment_then_delegate": ["delegate"],
    "open_clarification_gate_without_full_chain": ["clarification gate"],
}


def skill_text(name):
    for base in (ROOT / "skills" / name, ROOT / "integration" / "patch" / name):
        path = base / "SKILL.md"
        if path.exists():
            return path.read_text(encoding="utf-8")
    return None


def owner_text(route):
    texts = [
        (ROOT / "docs/orchestration/routing-matrix.md").read_text(encoding="utf-8"),
        (ROOT / "skills/hybrid-coach/SKILL.md").read_text(encoding="utf-8"),
    ]
    local = skill_text(route)
    if local:
        texts.insert(0, local)
    return "\n".join(texts).lower()


def main():
    scenarios = json.loads((ROOT / "tests/scenarios/routing.json").read_text(encoding="utf-8"))
    expected = json.loads((ROOT / "tests/expected/routing-expected.json").read_text(encoding="utf-8"))["core"]
    errors = []
    required_policy = [
        "Named skill request wins",
        "Missing data must remain `unknown`",
        "Known target wins over diagnosis",
        "Full-chain routing is only for compound tasks",
    ]
    matrix = (ROOT / "docs/orchestration/routing-matrix.md").read_text(encoding="utf-8")
    for phrase in required_policy:
        if phrase not in matrix:
            errors.append("missing routing policy: " + phrase)

    for scenario in scenarios:
        sid = scenario["id"]
        exp = expected.get(sid)
        if not exp:
            errors.append("{0}: missing acceptance expectation".format(sid))
            continue
        if exp["route"] != scenario["primary"]:
            errors.append("{0}: route mismatch".format(sid))
        if not scenario["prompt"].strip():
            errors.append("{0}: empty prompt".format(sid))
        markers = CONTRACTS.get(exp["must"], [])
        haystack = owner_text(exp["route"])
        for marker in markers:
            if marker.lower() not in haystack:
                errors.append(
                    "{0}: contract {1} missing phrase {2!r}".format(
                        sid, exp["must"], marker
                    )
                )
        if exp["route"] in UPSTREAM_ONLY and exp["route"] not in matrix:
            errors.append("{0}: upstream route missing from routing matrix".format(sid))

    print("Acceptance fixtures: {0}".format(len(scenarios)))
    if errors:
        print("FAIL")
        for err in errors:
            print(" -", err)
        sys.exit(1)
    print("PASS")


if __name__ == "__main__":
    main()
