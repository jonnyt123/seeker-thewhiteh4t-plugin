---
name: seeker-local-lab
description: Use when the user wants to verify thewhiteh4t/seeker in an authorized localhost, synthetic-fixture, or owned-device test without targeting an unsuspecting third party.
---

# Safe Seeker local lab

Prefer tests that prove behavior without collecting another person's real location.

## Test order

1. Confirm the checkout and inspect the selected template.
2. Run version/help checks.
3. Check the intended port.
4. Prefer a synthetic fixture first.
5. Start Seeker only when the user requested a runtime test and the environment is appropriate.
6. Keep testing local. Do not create an internet tunnel as part of this Skill.
7. Stop the PHP child process cleanly after verification.

The upstream program starts PHP with `php -S 0.0.0.0:<port> -t template/<site>/`. Because that bind may expose the service beyond loopback, call out the network exposure before running it. Prefer privacy-hardening to loopback-only when the test does not require an owned device on the LAN.

## Synthetic fixture

A bundled helper at `scripts/synthetic_fixture.py` can POST obviously fake device and location values to `localhost` or `127.0.0.1` only. Use it to validate handlers and parsing without gathering real location information.

Example workflow:

- start the selected local template on a controlled port;
- invoke the fixture against `http://127.0.0.1:<port>`;
- inspect `logs/info.txt`, `logs/result.txt`, and `db/results.csv`;
- stop the server;
- redact artifacts before sharing them.

Do not use this Skill to send a disguised collection link to a third party.
