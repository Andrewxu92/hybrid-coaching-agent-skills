# Skill Handoff Contract v0.1.0

The goal is not a complex data model. Each skill passes only the fields the next skill actually needs.

## 1. Profile → Gap
Input: `strength`, `speed`, `endurance`, optional evidence/confidence.

## 2. Demand → Gap
Input: sport/HYROX demand values for the same three dimensions.

## 3. Gap → Limitation (optional)
Input: meaningful gap + HR/pace/breathing/RPE/fatigue/task-response evidence when available.

## 4. Gap/Limitation → Adaptation Target
Input: ranked gap + current limitation hypothesis (if useful).

## 5. Adaptation Target → Existing Engine
Input: one primary target, optional secondary target, and method domain (`strength|endurance|speed|planning`).

## 6. Target → Transfer
Input: intended adaptation + task constraints + recovery/state carry-over.

## 7. Race state → Pacing
Input: current HR/pace/breathing/fatigue + current/next station + target pace.

## Missing-data rule
If a required field is missing and materially changes the decision, return `unknown` and ask for the minimum useful input. Do not fabricate precision.
