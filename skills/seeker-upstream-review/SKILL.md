---
name: seeker-upstream-review
description: Use when comparing a local thewhiteh4t/seeker checkout with upstream, checking version drift, or assessing whether an update affects CLI, templates, dependencies, or safe-lab behavior.
---

# Seeker upstream review

Prefer read-only Git inspection first.

1. Identify the local commit, branch, and working-tree state.
2. Preserve uncommitted work.
3. Read local `metadata.json`, `seeker.py`, `template/templates.json`, and installer/dependency files.
4. When web/GitHub access is available, inspect the current upstream files or commits.
5. Summarize changes that affect:
   - CLI flags or environment variables;
   - template indexes/modules;
   - dependencies and supported platforms;
   - PHP/server behavior;
   - data collection/storage/forwarding;
   - generated artifacts;
   - safety/privacy implications.
6. Do not run the upstream update path or overwrite local files unless the user requested an update.

Report the exact refs compared and separate verified differences from inference.
