# Validation

Validation is split into three levels.

## 1. Static Skill validation

Checks:

- every skill has `SKILL.md`;
- frontmatter is valid YAML;
- `name` matches its directory;
- names are lowercase kebab-case;
- description length is within the Agent Skills limit;
- references are resolvable.

## 2. Deterministic routing tests

The scenario suite verifies expected primary routes for capability, gap, diagnosis, adaptation, Hybrid classification, pacing, HYROX demand, planning, audit, explicit skill requests, and ambiguous requests.

## 3. Real-agent behavior evaluation

Static tests do not prove LLM routing quality. Run the skill collection inside the target Skills-compatible agent and record:

- selected skill;
- unnecessary skill activations;
- skipped handoffs;
- invented precision;
- incorrect Hybrid classification;
- failure to preserve uncertainty.

The real-agent test set should be treated as an evaluation artifact and expanded when a failure pattern is observed.
