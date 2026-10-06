# Seeker Lab Plugin v0.5.0

A ChatGPT/Codex skills-only plugin for authorized inspection, diagnostics, testing, privacy hardening, and auditing of `thewhiteh4t/seeker`.

## Capabilities

Seeker Lab can inspect a checkout, explain the current CLI/template configuration, diagnose Python/PHP/runtime failures, run synthetic localhost checks, audit the browser → PHP → Python → CSV/KML/outbound data flow, redact sensitive artifacts, review templates, apply privacy/local-only hardening when requested, and compare a checkout with upstream.

## Safety boundary

Seeker can collect precise browser geolocation and device/network information. Runtime collection is limited to transparent localhost tests, the user's own devices, synthetic fixtures, or clearly consenting participants. The plugin does not assist deceptive or covert collection against third parties.

## Package structure

The root `plugin.json` is the portable Agent Plugins manifest. `.codex-plugin/plugin.json` is the compatibility fallback. This is a skills-only package: it has no MCP server, app mapping, external authentication dependency, or bundled upstream Seeker source.

## Validation

Run:

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

GitHub Actions runs the same repository validator, compiles every bundled Python helper, and runs the regression suite on pushes and pull requests.

## Upstream target

The workflows were designed from inspection of `thewhiteh4t/seeker` 1.3.1-era source. The upstream project is not vendored into this repository. Use the upstream-review Skill to verify drift before relying on version-sensitive details.

## Release status

GitHub `main` is the development source of truth. A passing local/CI validation run is not the same as OpenAI Plugin Directory submission, approval, or publication.

See `QUALITY-100.md` for the v0.5.0 quality ledger and `SECURITY.md` for the authorized-use boundary.
