---
name: sandbox-python-executor
description: Use when a Seeker workflow needs deterministic parsing, local file inspection, redaction, archive checks, hashing, or other host-native Python verification.
---

# Sandbox Python Executor

Use the host's Python execution capability when deterministic evidence materially improves the result.

Good uses include parsing JSON/CSV, checking file trees, redacting sensitive test artifacts, computing hashes, validating manifests, inspecting archives, and running the bundled safe helper scripts.

Do not use Python as a substitute for a narrower file/search tool. Treat target-repository code as untrusted input: inspect it before executing it. Do not assume network access. Never expose secrets or unrelated user files.

Execution claims require real tool evidence. If Python is unavailable, state which checks remain unverified.
