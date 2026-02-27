---
name: send-newsletter
description: |
  Send a newsletter email to Buttondown subscribers. Use when the user says
  "send newsletter", "email subscribers", "publish newsletter", or after
  finishing a /curate-news draft that's ready to send.
---

# Send Newsletter

Send the latest Cybersecurity x AI News Roundup post as a Buttondown newsletter.

## Prerequisites

- `BUTTONDOWN_API_KEY` environment variable must be set
- `requests` Python package installed (`pip install requests`)

## Workflow

1. **Find the latest post** — grep `content/` for `Category: Cybersecurity x AI News Roundup`,
   sort by `Date:` header, pick the most recent. Show the user the title and date.
2. **Confirm** — ask the user if this is the post they want to send.
   If the user specifies a different file, use that instead.
3. **Extract subject** — use the `Title:` from the Pelican front matter.
4. **Dry run** — run `scripts/send.py --strip-headers --dry-run` to preview.
5. **Confirm send** — ask "Send this to all subscribers?"
6. **Send** — run `scripts/send.py --strip-headers --subject "<subject>" --body-file <path>`

## Send Script

```
python3 scripts/send.py --subject "Subject" --body-file post.md --strip-headers
python3 scripts/send.py --subject "Subject" --body-file post.md --strip-headers --dry-run
```

`--strip-headers` removes Pelican front matter (everything before the first blank line).

## Error Handling

- Missing `BUTTONDOWN_API_KEY` → tell user: `export BUTTONDOWN_API_KEY=your-token`
- Empty body file → warn and abort
- API error → show status code and response body
