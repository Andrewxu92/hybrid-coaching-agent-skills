# Skill Schema v0.1.0

Skills follow the Agent Skills format: a directory with `SKILL.md`; `name` and `description` are required frontmatter. Keep instructions concise and put detailed material into `references/` where useful.

## Required behavior

1. State the narrow purpose.
2. State when the skill should and should not trigger.
3. Prefer validated inputs; never invent precision.
4. Produce structured output first, then explanation if needed.
5. Preserve uncertainty (`unknown`, `unclear`) rather than forcing a conclusion.
6. Hand off to existing skills instead of duplicating their logic.
7. Distinguish source-derived rules from implementation inference.
8. Include enough provenance in outputs to reconstruct why the skill made the recommendation.

## Preferred output envelope

```yaml
result: {}
confidence: low|medium|high
provenance:
  source: user-methodology|external-research|inference|composition
  rules_used: []
handoff: []
unknowns: []
```

The envelope is conceptual: an implementation may use equivalent JSON, Markdown, or native tool output.
