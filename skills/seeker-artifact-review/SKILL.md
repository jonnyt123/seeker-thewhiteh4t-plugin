---
name: seeker-artifact-review
description: Use when inspecting Seeker logs, results.csv, info/result JSON, or KML from an authorized test while minimizing exposure of precise location or identifying device/network data.
---

# Seeker artifact review

Treat Seeker artifacts as sensitive by default.

Relevant files may include `logs/php.log`, `logs/info.txt`, `logs/result.txt`, `db/results.csv`, and generated `.kml` files.

## Default handling

- summarize rather than reproduce exact sensitive values;
- redact full public IP addresses;
- redact precise latitude/longitude and KML coordinates;
- do not expose tokens, webhook URLs, or credentials;
- distinguish synthetic values from live test data;
- do not commit sensitive artifacts to source control.

Use the bundled `scripts/redact_seeker_data.py` for a safe local summary. It never performs network requests and does not modify the original files.

If the user explicitly asks to inspect their own test data, exact values may be read only as necessary for the requested troubleshooting; avoid echoing them back when a redacted explanation is sufficient.
