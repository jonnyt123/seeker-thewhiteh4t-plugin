# Contributing

Keep changes narrowly scoped and preserve the plugin's authorized-lab safety boundary.

Before proposing a change:

1. Inspect the current Skill that owns the workflow.
2. Avoid duplicate or overly broad Skills.
3. Keep runtime collection limited to transparent, authorized testing.
4. Do not add secrets, generated Seeker runtime data, or upstream Seeker source.
5. Run `python3 scripts/validate_repo.py`.
