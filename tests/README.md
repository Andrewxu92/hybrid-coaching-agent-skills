# Tests

The tests in this directory are deterministic contract checks for the repository.

Run from the repository root:

```bash
python scripts/validate_skills.py
python tests/scripts/router-regression.py
python tests/scripts/semantic-acceptance.py
python tests/scripts/install-smoke.py
```

These checks validate routing contracts and repository structure. They are not a substitute for live evaluation with a compatible agent client.
