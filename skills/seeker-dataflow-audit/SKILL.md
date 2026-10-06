---
name: seeker-dataflow-audit
description: Use when reviewing how thewhiteh4t/seeker collects, stores, forwards, or transforms browser, device, IP, and location data.
---

# Seeker data-flow audit

Trace the actual source instead of relying only on README claims.

Current high-level flow:

1. `js/location.js` gathers browser/device fields and requests browser geolocation.
2. `php/info.php` writes device/network information to `logs/info.txt`.
3. `php/result.php` or `php/error.php` writes geolocation/error state to `logs/result.txt`.
4. `seeker.py` parses these files, may perform public-IP reconnaissance, may forward events through configured Telegram/webhook outputs, appends a row to `db/results.csv`, and may generate KML.

Review:

- collection purpose and consent surface;
- data minimization;
- local bind/network exposure;
- trusted proxy/IP-header assumptions;
- outbound HTTP requests;
- webhook/Telegram secret handling;
- retention and cleanup behavior;
- CSV/KML precision;
- template-generated redirects;
- exception and stale-file behavior.

The bundled `scripts/static_audit.py` performs a read-only source scan and reports notable data paths/endpoints without executing Seeker.

Recommendations should favor transparent consent, local-only testing, minimized retention, disabled outbound forwarding, and synthetic fixtures.
