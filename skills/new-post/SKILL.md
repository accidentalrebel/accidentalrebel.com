---
name: new-post
description: Process a draft markdown file into a Pelican blog post with proper metadata
disable-model-invocation: true
argument-hint: [file.md]
---

# New Blog Post Skill

Process a draft markdown file into a properly formatted Pelican blog post for AccidentalRebel.com.

## Usage

```
/new-post path/to/draft.md
```

## What This Skill Does

1. **Read the draft file** - The file should contain the post content (title as H1 is optional)

2. **Add Pelican metadata header** with these fields:
   ```
   Title: <extracted from first H1 or filename>
   Date: <current date in YYYY-MM-DD HH:MM format>
   Slug: <kebab-case derived from title>
   Tags: <suggest relevant tags based on content>
   Category: <one of: programming, security, gamedev, tools>
   ```

3. **Move to content directory** - Save as `/workspace/content/<slug>.md`

4. **Delete the original draft file**

5. **Verify the build** - Run `source venv/bin/activate && make html` to confirm it compiles

6. **Report the result** - Show the new file path and confirm it built successfully

## Common Tags

Use tags from this list when relevant:
- programming, python, tools, docker, ai, claude-code
- security, malware-analysis, reverse-engineering, ctf, threat-hunting
- gamedev, rebel-game-engine, emacs

## Categories

- `programming` - General programming, tools, AI/automation
- `security` - Malware analysis, RE, CTF, threat hunting
- `gamedev` - Game engine development
- `tools` - Development tools, Emacs, workflow

## Image References

If the post references images, remind the user to:
- Place images in `content/images/`
- Use `{attach}/images/filename.png` syntax

## Environment

Always activate the virtual environment before building:
```bash
source venv/bin/activate
```
