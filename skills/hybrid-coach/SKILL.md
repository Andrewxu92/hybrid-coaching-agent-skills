---
name: hybrid-coach
description: >-
  Route broad Hybrid/HYROX coaching requests across athlete capability, demand, gaps, limitation screening, training targets, transfer, planning, and race-state execution. Use for compound requests or underspecified coaching requests. Explicit skill names and known single-method targets should bypass this router. For generic requests such as “怎么训练才能变强”, open a clarification gate rather than starting the full chain.
metadata:
  version: "0.1.0"
  role: "compound-router"
---
# Hybrid Coach

## Purpose
Provide the smallest useful entry path for compound or underspecified Hybrid coaching requests.

## Dispatch priority
1. Explicit named skill → that skill.
2. Known single training target/method → existing method selector.
3. Explicit complete HYROX preparation → `hyrox-coach`.
4. Immediate race-state question → `state-based-pacing`.
5. Sport-demand question → `hyrox-needs-profile`.
6. Athlete-vs-demand question → `capability-gap-analysis`.
7. Capability-profile question → `athlete-capability-profile`.
8. Limitation question → `performance-limitation-screen`.
9. Adaptation question → `adaptation-target-selector`.
10. Hybrid classification/transfer question → `hybrid-transfer-selector`.
11. Broad planning (non-HYROX) / complete preparation → compound flow.
12. Ambiguous “be stronger/fitter” request with no sport, target, or baseline → clarification gate only.

## Clarification gate
For an underspecified request, ask for the smallest missing context needed to route correctly, such as:
- sport/event;
- primary outcome;
- current baseline or known scores;
- time horizon.
Do not generate a full plan from the generic request alone.

## Compound flow
`Profile → Demand → Gap → Limitation (only if decision-relevant) → Adaptation Target → Existing Training Engine → Transfer → HYROX Execution/Pacing → Monitoring`

## Boundaries
- This router does not duplicate method-selection or periodization logic.
- It does not force every request through the complete chain.
- It must preserve upstream outputs when delegating.
- It may return a clarification request instead of a skill handoff when the intent is too underspecified.
