import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
scenarios = json.loads((ROOT / "tests/scenarios/routing.json").read_text(encoding="utf-8"))

def expected_route(s):
    p = s["prompt"]
    if "直接调用" in p or "@skill" in p:
        if "endurance-method-selector" in p: return "endurance-method-selector"
    if "完整HYROX" in p or "完整备赛体系" in p or "我要HYROX完整备赛" in p: return "hyrox-coach"
    if "比赛现在" in p or ("下一站" in p and "HR" in p): return "state-based-pacing"
    if "HYROX到底需要" in p: return "hyrox-needs-profile"
    if "审计" in p or ("计划" in p and "Endurance" in p): return "hyrox-plan-audit"
    if "排下周HYROX" in p: return "hyrox-week-template"
    if "力量、速度、耐力分别怎么样" in p or "没有任何测试数据" in p: return "athlete-capability-profile"
    if "最短板" in p or "Demand" in p: return "capability-gap-analysis"
    if "为什么我HR很高" in p or "HR高但RPE低" in p: return "performance-limitation-screen"
    if "下一步应该提升什么" in p: return "adaptation-target-selector"
    if "算Hybrid吗" in p: return "hybrid-transfer-selector"
    if "已经决定练最大力量" in p: return "strength-method-selector"
    if "怎么训练才能变强" in p: return "hybrid-coach"
    return None

errors = []
for s in scenarios:
    got = expected_route(s)
    if got != s["primary"]:
        errors.append(f"{s["id"]}: expected {s["primary"]}, got {got}")
print(f"Routing fixtures: {len(scenarios)}")
if errors:
    print("FAIL")
    print("\n".join(errors))
    raise SystemExit(1)
print("PASS")
