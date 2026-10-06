# Seeker Lab Plugin v0.4.0

A ChatGPT/Codex skills-only plugin specialized for `thewhiteh4t/seeker`.

## What it can do

- inspect a Seeker checkout and current CLI/template configuration;
- diagnose Python, PHP, dependency, port, PID, and template failures;
- run transparent localhost/owned-device lab checks;
- validate the handler pipeline with synthetic localhost-only fixture data;
- audit browser → PHP → Python → CSV/KML/outbound data flow;
- inspect/redact sensitive artifacts;
- review templates;
- apply privacy/local-only hardening when explicitly requested;
- compare a checkout with upstream.

## Safety boundary

Seeker can collect precise browser geolocation and device/network information. Runtime collection is limited to transparent localhost tests, the user's own devices, synthetic fixtures, or clearly consenting participants. The plugin does not assist deceptive or covert collection against third parties.

## Package structure

The root `plugin.json` is the portable Agent Plugins manifest. `.codex-plugin/plugin.json` is included as a compatibility fallback. This plugin has no MCP server and no external authentication dependency.

## Upstream target

The plugin was built from inspection of `thewhiteh4t/seeker` version 1.3.1 source and its current `template/templates.json`, `js/location.js`, PHP handlers, and installer.

## Source of truth

This repository is the canonical source for the plugin. Build release artifacts from committed repository contents; do not edit generated ZIPs directly.
