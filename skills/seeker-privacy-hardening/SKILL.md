---
name: seeker-privacy-hardening
description: Use when the user wants to make a Seeker checkout safer for local demonstrations by reducing network exposure, outbound forwarding, data retention, or precision.
---

# Seeker privacy hardening

This Skill modifies an authorized local checkout only when the user asks for hardening.

Useful defensive changes include:

- bind PHP to `127.0.0.1` for localhost-only demos;
- disable or remove Telegram/webhook forwarding;
- disable automatic public-IP reconnaissance;
- replace real geolocation with synthetic fixtures for demonstrations;
- minimize or disable persistent CSV/KML retention;
- clear sensitive temporary files on shutdown;
- add explicit consent/disclosure copy to neutral lab templates;
- add `.gitignore` coverage for logs, results, KML, and generated template output where appropriate.

Inspect the exact source before patching. Make focused changes, preserve upstream behavior outside the requested safety profile, and verify the resulting local test.

Do not use hardening as a pretext to conceal data collection or make the tool stealthier.
