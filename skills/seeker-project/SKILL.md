---
name: seeker-project
description: Use for general work on a checkout of thewhiteh4t/seeker, including inspection, configuration, safe lab testing, troubleshooting, or deciding which Seeker-specific workflow applies.
---

# Seeker project router

This Skill targets `thewhiteh4t/seeker`, whose inspected upstream source reports version 1.3.1.

## First actions

1. Confirm the workspace is a Seeker checkout by locating `seeker.py`, `metadata.json`, `template/templates.json`, `php/`, and `js/location.js`.
2. Inspect before running or modifying anything.
3. Route to the narrowest Skill:
   - exact flags/templates/env vars -> `seeker-cli-reference`
   - startup/install/runtime failure -> `seeker-diagnostics`
   - transparent local testing -> `seeker-local-lab`
   - template mechanics -> `seeker-template-review`
   - JS/PHP/Python data path -> `seeker-dataflow-audit`
   - logs/results/KML -> `seeker-artifact-review`
   - privacy/local-only hardening -> `seeker-privacy-hardening`
   - upstream comparison -> `seeker-upstream-review`

## Authorization boundary

Seeker is designed to request browser geolocation and collect device/network information. Treat location, IP/device fingerprints, logs, exported CSV, and KML as sensitive.

Proceed with runtime collection only for transparent localhost tests, the user's own devices, synthetic fixtures, or clearly consenting participants. Do not create or deploy deceptive third-party impersonation pages, conceal the collection purpose, obtain another person's precise location/device data without informed consent, or configure covert exfiltration.

For ambiguous runtime requests, prefer a synthetic localhost fixture that proves the pipeline without collecting real location data.

## Completion

Report the exact checkout/ref inspected, commands actually executed, files changed, tests run, and any safety or environment limits that remain.
