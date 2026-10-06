---
name: seeker-cli-reference
description: Use when the user asks how to invoke thewhiteh4t/seeker, which template index or environment variable to use, or what files the current CLI writes.
---

# Seeker 1.3.1 CLI reference

Recognized flags from the inspected `seeker.py`:

- `-h`, `--help`
- `-k`, `--kml <filename>`
- `-p`, `--port <integer>`; default 8080
- `-u`, `--update`
- `-v`, `--version`
- `-t`, `--template <integer>`
- `-d`, `--debugHTTP`
- `-tg`, `--telegram <token:chatId>`
- `-wh`, `--webhook <URL>`

Recognized environment variables include `DEBUG_HTTP`, `PORT`, `TEMPLATE`, `TITLE`, `REDIRECT`, `IMAGE`, `DESC`, `SITENAME`, `DISPLAY_URL`, `MEM_NUM`, `ONLINE_NUM`, `TELEGRAM`, and `WEBHOOK`.

Current template indexes from `template/templates.json`:

0. NearYou
1. Google Drive
2. WhatsApp
3. WhatsApp Redirect
4. Telegram
5. Zoom
6. Google ReCaptcha
7. Custom Link Preview

The current parser expects `--template` to be an integer. Do not use obsolete examples such as `-t manual`.

Potential generated state includes:

- `logs/php.log`
- `logs/info.txt`
- `logs/result.txt`
- `db/results.csv`
- `pid`
- optional `<name>.kml`

Never print Telegram tokens, webhook credentials, or other secrets. Runtime commands that would collect sensitive data must follow the authorization boundary in `seeker-project`.
