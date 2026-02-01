Title: Building a session retrospective skill for Claude Code
Date: 2026-02-01 12:00
Slug: building-a-session-retrospective-skill-for-claude-code
Tags: claude-code, tools, ai, programming
Category: programming

I've been using Claude Code for a while now, and I noticed a pattern: at the end of a productive session, I'd have this vague sense of "we figured out some useful stuff" but no concrete record of what those lessons actually were.

Recently, I learned of a skill called [continuous-learning](https://github.com/affaan-m/everything-claude-code/tree/main/skills/continuous-learning). It automatically extracts reusable patterns and saves them as skills. But I wanted something different. Not automated pattern extraction, but a human-readable summary I could actually share. Something I could look back on, or turn into a blog post.

So I built the [session-retrospective](https://github.com/accidentalrebel/claude-skill-session-retrospective) skill.

## What it does

The skill analyzes the current Claude session and generates a markdown summary covering:
- What we set out to do
- Problems encountered and how they were solved
- Mistakes made and corrections
- Techniques discovered worth remembering
- Key takeaways

The output goes straight to console for copy/paste. No files created, no cleanup needed.

## How it works

Claude Code stores session history as JSONL files in `~/.claude/projects/<project-dir>/<session-id>.jsonl`. Each line is JSON with message type, content, timestamps, and metadata. A simple bash file locates and outputs the session JSONL:

```bash
SESSION_FILE=$(find "$PROJECTS_DIR" -name "${SESSION_ID}.jsonl" -type f | head -1)
cat "$SESSION_FILE"
```
Once the history is fetched, the actual analysis is left to Claude with structured guidance. I provided a template for the output format and a table of what to look for (problems, decisions, techniques, mistakes). There's a lot of freedom, since synthesizing lessons requires judgment.

## What's next

The skill works for my current needs. I haven't tested it extensively on very long sessions (the JSONL can get large and might need chunking). For now, it handles my typical single-session bursts fine.

Also, the output format might need iteration based on actual use. The template includes sections for "mistakes made" and "techniques worth remembering" but maybe other categories would be more useful. I'll adjust as I use it more.

The code is [here](https://github.com/accidentalrebel/claude-skill-session-retrospective) if you want to try it.
