# Security Policy

## Reporting a vulnerability

If you discover a security vulnerability in LiveRecorder, **please do not open a public issue**. Report it privately:

- Open a private vulnerability report under **GitHub → Security → Report a vulnerability** (recommended), or
- Email the maintainer via the email address shown on the GitHub profile.

We will acknowledge reports within 7 days and work toward a fix. Please allow time for the fix to be released before disclosing the issue publicly.

## Security notes

- `config/config.ini` contains personal settings. **Never commit it** — it is git-ignored; always keep secrets (Douyin cookies, notification tokens, passwords) out of any committed file.
- Log files under `logs/` may contain stream URLs. They are git-ignored; do not force-add them to the repository.
- The string `wx74767bf0b684f7d3` in `src/spider.py` is a **public WeChat App ID** used as a referer for Huya app-stream recording. It originates from the upstream project and is **not a secret** (the real secret, an AppSecret, is never present in this repository). GitHub Secret Scanning may flag it — that is a false positive; please mark it as such rather than modifying the code.
