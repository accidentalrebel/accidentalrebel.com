---
name: blog-serve
description: >
  Serve the AccidentalRebel Pelican blog locally for preview. Use when the user says
  "serve", "preview", "blog-serve", "start the site", "run the blog", or wants to
  view the blog locally before publishing.
---

# Blog Serve

Serve the Pelican blog locally with live preview.

## Command

```bash
source /workspace/venv/bin/activate && pelican /workspace/content -o /workspace/output -s /workspace/pelicanconf.py && pelican -l /workspace/content -o /workspace/output -s /workspace/pelicanconf.py -p 8000 -b 0.0.0.0
```

Build the site first, then serve. Run in the background so the conversation can continue.

## Notes

- The Makefile's `serve` target doesn't work because `pelican` isn't on PATH outside the venv. Call pelican directly after activating the venv.
- Bind to `0.0.0.0` (not `localhost`) so the site is accessible from outside the container.
- Port 8000 is the only externally accessible port.
- Use `-l` flag for Pelican's built-in live reload server.
- To also auto-regenerate on file changes, add the `-r` flag.
