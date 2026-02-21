---
name: send-newsletter
description: |
  Send a newsletter email to Buttondown subscribers. Use when the user says
  "send newsletter", "email subscribers", "publish newsletter", or after
  finishing a /curate-news draft that's ready to send.
---

# Send Newsletter

Send a markdown email to all Buttondown subscribers via the API.

## Prerequisites

- `BUTTONDOWN_API_KEY` environment variable must be set
- `requests` Python package must be installed

## Workflow

1. **Get the content** — ask the user for the markdown file path (or use the file they provide)
2. **Read the file** and display a preview (first 20 lines + total length)
3. **Confirm subject line** — suggest one from the file's H1 heading if present, let user edit
4. **Dry run first** — run `scripts/send.py --dry-run` to show the payload
5. **Confirm send** — ask "Send this to all subscribers?" before actually sending
6. **Send** — run `scripts/send.py --subject "<subject>" --body-file <path>`

## Send Script

Use `scripts/send.py` in this skill's directory:

```
python3 scripts/send.py --subject "Subject" --body-file content.md
python3 scripts/send.py --subject "Subject" --body-file content.md --dry-run
```

## Extracting Subject from Content

If the markdown starts with `# Title`, use that as the suggested subject (strip the `#`).
Otherwise ask the user to provide one.

## Error Handling

- Missing `BUTTONDOWN_API_KEY` → tell user to set it: `export BUTTONDOWN_API_KEY=your-token`
- Empty body file → warn and abort
- API error → show the status code and response body
