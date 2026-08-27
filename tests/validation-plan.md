# Validation Plan v0.3

## 目标
验证新 6 个 Skills 不会把 Agent 路由回旧的 generic planner，也不会把不确定推断包装成确定结论。

## Suite A — Discovery / routing

1. 核心能力画像
2. HYROX 需求差距
3. 表现限制初筛
4. 训练适应目标
5. Hybrid 判定
6. 比赛现场动态配速
7. HYROX 周课表
8. HYROX 计划审计

## Suite B — Boundary

- 不把 medical diagnosis 当作 limitation screen 输出。
- 不在缺失数据时制造分数。
- 不把 Adaptation Target Selector 变成完整训练计划生成器。
- 不让 state-based-pacing 代替周课表规划。

## Suite C — Regression

旧 repo 的核心路由仍应满足其原有边界：
- `hyrox-week-template` 用于排周课表/前瞻安排。
- `hyrox-plan-audit` 用于已成文计划审查。
- `hyrox-needs-profile` 用于 HYROX 需求画像。
- `hyrox-coach` 用于复合/模糊 HYROX 请求。

## Pass criteria

- 正确主 Skill
- 正确 handoff
- 无越权诊断
- 无数据幻觉
- 输出保持单一主要决策
