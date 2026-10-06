---
name: host-workspace-operator
description: Use when a Seeker workflow needs to inspect, search, modify, or verify files in the host workspace using the safest native tools available.
---

# Host Workspace Operator

Use workspace tools supplied by the current ChatGPT/Codex host instead of pretending the Plugin owns a filesystem API.

Prefer, in order, the narrowest capability that works: read, list, search, grep, patch, write, shell, then Python.

Start read-only. Inspect repository instructions and relevant files before mutation. Treat patch, write, delete, move, rename, package installation, process termination, and mutating shell commands as state changes. Make them only when the user requested or clearly authorized the change.

For shell execution, inspect commands first, avoid unrelated services, and do not execute arbitrary repository scripts merely because they exist. Never weaken tests or security checks to manufacture a pass.

After mutation, read the changed area back and run the narrowest useful verification. Report exactly what changed and what real execution evidence was observed.

If a required host capability is unavailable, do not fabricate it or claim the operation ran.
