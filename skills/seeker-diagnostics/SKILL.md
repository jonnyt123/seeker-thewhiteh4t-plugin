---
name: seeker-diagnostics
description: Use when thewhiteh4t/seeker fails to install, start, load a template, bind its port, launch PHP, process a local test, or exits with a Python/PHP/runtime error.
---

# Seeker diagnostics

Diagnose the first actionable failure rather than applying broad fixes.

## Read-only preflight

Check:

1. `python3 --version`
2. `php --version`
3. `python3 seeker.py -v`
4. `python3 seeker.py -h`
5. imported Python modules used by `seeker.py` and the selected template
6. whether the requested port is already occupied
7. `pid` ownership before terminating any process
8. `logs/php.log` after a PHP launch failure

Known direct Python dependencies include `requests`, `packaging`, and `psutil`; the source also relies on PHP for the local web handlers.

## Common failures

- `FileNotFoundError` for `php`: PHP is not available on PATH.
- template parse failure: current `-t/--template` expects a numeric index.
- occupied port: identify the owning process; never kill an unrelated service.
- stale `pid`: verify process identity before removing or terminating.
- missing module: repair in an isolated environment when possible.
- missing template artifact: inspect the corresponding `template/mod_*.py` source and referenced files.
- malformed environment variable: validate type/format before retrying.

Do not blindly execute `install.sh`; inspect it first. It may use privileged package managers. Never default to `sudo pip`.

After a fix, rerun the narrowest failing check and report exact evidence.
