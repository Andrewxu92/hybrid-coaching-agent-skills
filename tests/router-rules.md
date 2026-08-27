# Router acceptance rules v0.1.1

## Direct-intent rules
- Explicit `@skill:"..."` always wins.
- Known-method requests bypass diagnosis and go to the named method selector.
- Race-state questions bypass planning and go to `state-based-pacing`.
- HYROX demand questions bypass athlete profiling unless athlete data are explicitly part of the request.

## Compound-intent rules
- "Complete HYROX preparation from assessment" may enter `hyrox-coach` and delegate through capability → gap → target → training → planning.
- "What is my weakest HYROX capacity?" should not jump directly to a week template.

## Insufficient-data rules
- Never manufacture 0–100 capability scores from vague self-description.
- If a decision depends on unavailable evidence, return `unknown` and request the minimum useful input.

## Diagnosis rules
- The limitation screen is a performance hypothesis, not a medical diagnosis.
- Conflicting evidence should produce `unclear`, not a forced central/peripheral classification.
