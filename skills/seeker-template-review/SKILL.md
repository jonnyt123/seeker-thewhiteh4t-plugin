---
name: seeker-template-review
description: Use when inspecting, explaining, repairing, or making a transparent test-only template for thewhiteh4t/seeker.
---

# Seeker template review

Use `template/templates.json` as the authoritative template registry and inspect the selected `template/mod_*.py` module plus its HTML/JS assets.

A template module may read environment variables, copy an image, substitute text/URLs into a template, create `index.html`, and receive copied handler/location files during startup.

When editing templates:

- preserve the registry/module/directory relationship;
- keep placeholders deterministic and validate missing values;
- keep test branding neutral and explicit that it is a location-permission demonstration;
- avoid copying real service branding or UI in a way intended to trick a person;
- use local or user-owned test assets;
- do not add hidden data collection beyond what the user can see and consent to;
- verify generated `index.html` and asset paths.

For a new lab template, prefer a neutral name such as `Consent Demo` and clear on-page disclosure rather than impersonating Google Drive, WhatsApp, Telegram, Zoom, or another third-party service.
