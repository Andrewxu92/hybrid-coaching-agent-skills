# Routing Matrix v0.1.0

| User intent | Primary skill | Do not route to | Typical handoff |
|---|---|---|---|
| 当前力量/速度/耐力如何 | `athlete-capability-profile` | planning skills | `capability-gap-analysis` if demand exists |
| HYROX 我最缺什么 | `capability-gap-analysis` | `hyrox-week-template` first | `adaptation-target-selector` |
| 为什么 HR 高但跑不动 | `performance-limitation-screen` | immediate plan generation | `adaptation-target-selector` |
| 下一步提高什么 | `adaptation-target-selector` | method selector as diagnosis | existing method skill |
| 这个训练算 Hybrid 吗 | `hybrid-transfer-selector` | generic exercise classifier | none / planning |
| 比赛现在 HR 很高怎么办 | `state-based-pacing` | weekly planning | none |
| HYROX 需要什么 | `hyrox-needs-profile` | athlete diagnosis | `capability-gap-analysis` when athlete data exist |
| 给我排一周 HYROX | `hyrox-week-template` | gap diagnosis unless needed | `periodization-planner` if phase context is needed |
| 审计已有计划 | `hyrox-plan-audit` | replacement plan generation | none |
| 完整 HYROX 备赛 | `hyrox-coach` | direct execution by router | capability → gap → target → existing engine → HYROX |
| 已明确最大力量，怎么练 | `strength-method-selector` | diagnostic screen | `session-plan-builder` if requested |
| 已明确耐力方法，怎么安排 | `endurance-method-selector` | adaptation selector | `session-plan-builder` if requested |
| 完整 Hybrid 训练系统 | `hybrid-coach` | narrow skill first | capability → gap → target → engine → transfer |

## Hard guardrails

- Named skill request wins.
- Known target wins over diagnosis.
- Assessment beats planning when current-state information is explicitly requested.
- Full-chain routing is only for compound tasks.
- Missing data must remain `unknown`; never manufacture 0–100 scores.
