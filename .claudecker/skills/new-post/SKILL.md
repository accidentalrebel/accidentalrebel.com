---
name: new-post
description: |
  Convert draft markdown into a Pelican blog post for AccidentalRebel.com.
  Use when: (1) user provides a draft .md file to publish, (2) user says "new post"
  or "publish this", (3) user wants to convert notes/drafts into a blog post.
  Accepts a file path argument.
---

# New Blog Post

Convert draft markdown to a published Pelican blog post.

## Workflow

1. Read the draft file (argument or ask user)
2. Extract title from first H1 or filename
3. Generate metadata header:
   ```
   Title: <title>
   Date: <YYYY-MM-DD HH:MM>
   Slug: <kebab-case-title>
   Tags: <from content, see tags below>
   Category: <programming|security|gamedev|tools>
   ```
4. Write to `/workspace/content/<slug>.md`
5. Delete original draft
6. Build: `source venv/bin/activate && make html`
7. Report result

## Tags

Choose from: `programming`, `python`, `tools`, `docker`, `ai`, `claude-code`, `security`, `malware-analysis`, `reverse-engineering`, `ctf`, `threat-hunting`, `gamedev`, `rebel-game-engine`, `emacs`

## Categories

- `programming` - code, tools, AI/automation
- `security` - malware, RE, CTF, threat hunting
- `gamedev` - game engine development
- `tools` - dev tools, Emacs, workflow

## Images

If post has images, remind user:
- Place in `content/images/`
- Reference as `{attach}/images/filename.png`

## Template

See [assets/template.md](assets/template.md) for header format.
