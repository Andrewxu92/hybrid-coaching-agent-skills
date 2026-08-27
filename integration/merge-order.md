# Merge Order

1. Copy `skills/*` into the destination agent skill discovery root, or use the provided installer for `skill-for-hirox`.
2. Apply the four HYROX boundary patches under `integration/patch/` to the upstream `hyrox-skills/` paths.
3. Keep the upstream training, periodization, load, planning, and nutrition skills unchanged.
4. Run the repository validators before committing the integration.
5. Run real-agent scenario evaluation before treating routing behavior as production-ready.
