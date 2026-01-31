# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Pelican-based static blog for AccidentalRebel.com focusing on cybersecurity, malware analysis, reverse engineering, and programming. The repository has two main branches:

- **master**: Source content (Markdown files, configuration, images)
- **gh-pages**: Generated HTML output for GitHub Pages deployment

## Key Information

- **Domain**: www.accidentalrebel.com
- **Static Site Generator**: Pelican (Python-based)
- **Theme**: rebel-minimal-theme (custom theme with rebellious elements)
- **Author**: AccidentalRebel (Karlo - L2 SOC Analyst focusing on malware RE)

## Common Development Tasks

### Building the Site
```bash
make html          # Generate the site locally
make clean         # Remove generated files
make regenerate    # Auto-regenerate on file changes
make serve         # Serve locally at http://localhost:8000
make devserver     # Serve and regenerate together
make publish       # Generate with production settings
make github        # Publish to GitHub Pages (gh-pages branch)
```

### Writing New Posts
1. Create a new `.md` file in `content/` directory
2. Use this header format:
```markdown
Title: Your Post Title
Date: YYYY-MM-DD HH:MM
Slug: url-slug-for-post
Tags: tag1, tag2, tag3
Category: category_name
Image: featured-image.png
```
3. Images go in `content/images/`
4. Reference images with `{attach}/images/filename.png`

### Publishing Workflow
1. Write/edit content in master branch
2. Run `make publish` to generate production build
3. Run `make github` to deploy to gh-pages branch

## Site Architecture

### Source Structure (master branch)
- `/content/` - Markdown blog posts
- `/content/images/` - Image assets
- `/content/extras/` - Extra files (CNAME)
- `/pelicanconf.py` - Development configuration
- `/publishconf.py` - Production configuration
- `/Makefile` - Build commands

### Output Structure (gh-pages branch)
- Category pages (`/category/`)
- Tag pages (`/tag/`)
- Author pages with pagination
- Atom/RSS feeds (`/feeds/`)
- Custom theme (`/theme/`)

## Configuration Details

### Key Settings
- **Timezone**: Asia/Singapore
- **Default Language**: English
- **Pagination**: 10 posts per page
- **Analytics**: Google Analytics enabled
- **Comments**: Disqus integration
- **Social**: Twitter, GitHub, YouTube links

### Dependencies
Dependencies are defined in `requirements.txt`:
- pelican
- markdown
- invoke
- ghp-import

### Environment Setup
This project uses a Python virtual environment. Before running any commands:
```bash
source venv/bin/activate
```

If the venv doesn't exist or dependencies need updating:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Quick Workflow: Adding a New Blog Post
1. Activate the virtual environment: `source venv/bin/activate`
2. Create the post file in `content/` with Pelican header metadata
3. Build and preview: `make html && make serve`
4. When ready: `make publish && make github`

## Theme Features

### Rebel Minimal Theme
The custom theme includes:
- **Clean minimal design** with mobile-first responsive layout
- **Rebellious elements**: Glitch effect on title hover, animated comic strip with hidden message
- **Syntax highlighting** for Python, JavaScript, Bash, and C/C++
- **Dark mode support** (auto-detects system preference)
- **Reading progress indicator**
- **Zero dependencies** - no external libraries or fonts
- **Red accent color** theme throughout

### Applying the New Theme

**To deploy the Rebel Minimal Theme:**

1. **Copy theme to your site:**
   ```bash
   cp -r rebel-minimal-theme /path/to/your/pelican/site/themes/
   ```

2. **Update pelicanconf.py:**
   ```python
   THEME = 'themes/rebel-minimal-theme'
   ```

3. **Test locally:**
   ```bash
   make html
   make serve
   ```

4. **Deploy to production:**
   ```bash
   make publish
   make github
   ```

### Theme Customization
- Theme location: `/rebel-minimal-theme/`
- Main CSS: `/rebel-minimal-theme/static/css/main.css`
- JavaScript: `/rebel-minimal-theme/static/js/main.js`
- Templates: `/rebel-minimal-theme/templates/`

**Key customizable elements:**
- Colors: Edit CSS variables in `main.css` (`:root` section)
- Comic strip message: Modify `content` property in `.comic-strip::before`
- Glitch effect: Adjust `.site-title:hover` animation
- Syntax highlighting: Extend language support in `main.js`

## Content Topics

The blog specializes in:
- Malware analysis and reverse engineering
- x64 Assembly programming
- Anti-virus evasion techniques
- CTF writeups and challenges
- Security tool development
- Threat hunting
- Game engine development (Rebel Game Engine)
- Emacs and development tools