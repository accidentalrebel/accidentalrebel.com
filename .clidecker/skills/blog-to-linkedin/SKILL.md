---
name: blog-to-linkedin
description: Convert a blog post into LinkedIn-ready content — a text post and a carousel slide
  plan with image generation prompts. Use when the user says "LinkedIn", "convert to LinkedIn",
  "carousel", "promote this post", or provides a blog post and wants social media content.
  Also use when the user points to a blog post file and asks for LinkedIn or social content.
---

# Blog to LinkedIn

Convert a completed blog post into three outputs, with a review checkpoint between planning and rendering:

1. A ready-to-paste **LinkedIn text post**
2. A **carousel slide plan** with image generation prompts
3. **STOP — display outputs 1 and 2 to the user and wait for approval before continuing**
4. **Rendered HTML slides** — one self-contained HTML file per slide

## Input

Accept a blog post as a file path (read the markdown) or full text pasted into the conversation.

## Saving Output

Derive `<slug>` from the post's `Slug:` metadata field, or from the source filename (minus `.md`) if no slug is set. Save all output to `social/<slug>/`:

- `linkedin.md` — text post + carousel plan (header linking back to source post)
- `slides/slide1.html`, `slides/slide2.html`, etc. — rendered HTML slides

Show the full text post and carousel plan in the conversation as well.

## Output 1: LinkedIn Text Post

**Constraints:** Under 3,000 characters. No emojis. 3-5 hashtags at end.

**Structure:**

```
[Hook — 2 lines max. Must work ABOVE the "see more" fold.]
[Blank line]
[Core insight — 2-4 short paragraphs. Standalone value, not a teaser.]
[Blank line]
[Close — natural mention of full post. Plain text URL, no link card.]
[Blank line]
[#Hashtag1 #Hashtag2 #Hashtag3]
```

**Hook:** The most important part. A punchy statement or question that creates urgency. First-person where natural. Not clickbait — a real insight compressed into two lines.

**Core insight:** Reframe the blog's findings for security leadership (CISOs, directors). Organizational risk, not implementation details. Should deliver value even if the reader never clicks through.

**Close:** "Full technical breakdown at accidentalrebel.com" or similar. Plain URL only.

**Writing process (two passes):**

1. **Position with `/wwcd`**: Before drafting, run `/wwcd` on the blog post's topic to get positioning guidance. Use it to identify: what consulting capital this content builds, how to frame it for the target audience (security leadership, practitioners with budget), and what angle makes this post worth promoting. Feed this into the hook and core insight.

2. **Draft the text post** using the positioning from step 1 and the structural constraints above.

3. **Edit with `/arebel-voice`**: Run the draft through `/arebel-voice` for voice consistency. Key voice markers:
   - Direct, practitioner-grounded. "I found X" not "It was discovered that X"
   - No buzzwords: no "landscape", "leverage", "crucial", "robust", "ecosystem"
   - No engagement bait: no "You won't believe..." or "Here's why you should care..."
   - No fluff padding. Every sentence earns its place
   - Write as a practitioner sharing findings with peers, not a marketer promoting content

## Output 2: Carousel Slide Plan

Produce a slide-by-slide plan. Typically 6-10 slides — prefer fewer strong slides over padded decks.

### Visual Identity Block

Define this ONCE at the top of the carousel plan. Every slide prompt inherits these defaults:

```
Visual Identity:
- Background: #ffffff (white)
- Accent color: #dc2626 (red — the blog's signature color)
- Text color: #24292f (dark gray)
- Text muted: #656d76
- Subtle background: #f6f8fa (light gray, for cards/boxes)
- Border: #d0d7de
- Style: Clean, minimal, white-dominant with red accents
- Typography direction: Clean sans-serif, bold headlines top-left
- Recurring motif: Minimal — thin red lines, subtle geometric touches
- Layout grid: Headline top-left, visual center, detail text bottom
- Dimensions: 1080x1350 (4:5 portrait — LinkedIn recommended)
- Constraints: No photorealism, no clutter, professional, white/red palette
```

Use the blog's white-and-red color scheme for all carousels. Add variety through layout, visual weight, and selective use of the subtle gray background — not through changing the palette.

### Per-Slide Format

For each slide, provide:

| Field | Description |
|-------|-------------|
| **Slide N (Role)** | Number and role: Cover, Core, or Closing |
| **Headline** | Short bold statement — the one thing this slide communicates |
| **Key detail** | 1-3 sentences or bullets. Heavily distilled from blog |
| **Visual suggestion** | Brief note on visual type: diagram, icon, stat callout |
| **Image prompt** | Full prompt for image generation LLM (see below) |

### Slide Structure

- **Slide 1 (Cover):** Title + subtitle. Create curiosity or state a bold claim. Make someone start swiping.
- **Slides 2-N (Core):** One point per slide. Each stands alone — someone swiping fast gets value from any single slide. Prioritize: surprising findings, actionable insights, risk-relevant facts. Cut filler.
- **Final slide (Closing):** CTA. "Full breakdown at accidentalrebel.com" + "Juan Karlo Licudine / @accidentalrebel"

### Image Prompt Requirements

Each prompt must specify:
- Dimensions (1080x1350)
- Background color (from visual identity)
- Accent colors used in this slide
- What visual elements appear and where
- What text overlays to render and their position
- Style consistency note ("Consistent with series" or "Matching carousel style")
- Exclusions (no photorealism, no clutter)

Refer to [references/example.md](references/example.md) for a complete example transformation showing the full carousel plan with image prompts.

## Review Checkpoint

After generating the text post and carousel plan:

1. Save `linkedin.md` to `social/<slug>/`
2. Display the full text post and carousel plan in the conversation
3. **STOP and ask the user to review.** Do not generate any HTML slides until the user approves or requests changes.

If the user requests changes, revise the plan and re-display. Only proceed to Output 3 after explicit approval (e.g., "looks good", "go ahead", "make the slides").

## Output 3: Rendered HTML Slides

After user approval, render each slide as a self-contained HTML file. Save to `social/<slug>/slides/slide1.html`, `slide2.html`, etc.

**IMPORTANT**: Read [references/slide-design-system.md](references/slide-design-system.md) before generating any slides. It contains the exact base structure, component patterns, and design tokens that every slide must follow.

### Key rules (details in reference)

- Use a `<style>` block with CSS classes — NOT inline styles
- Every slide gets: corner brackets (TL+BR), series marker (`"01 / 08"`), accent line
- 72px margins on all sides, 52px headline, 28px subtitle at bottom
- Inline SVG with stroke outlines for icons — no external images or libraries
- No CDN links, no external fonts, no JS libraries
- Flexbox for layouts (pipelines, grids, stat rows)
- Subtle backgrounds at `rgba(color, 0.04-0.08)`, borders at `rgba(color, 0.1-0.25)`

### Visual QA Loop

After generating all slides, screenshot each one and visually review for issues (overlapping elements, text overflow, clipped content). Fix and re-screenshot until clean.

**Setup** (run once per session — system libs are pre-installed via `.claudecker/requirements.txt`, but npm packages are not):
```bash
npm install playwright && npx playwright install chromium
```

**Screenshot all slides:**
```javascript
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1080, height: 1350 });
  const dir = 'social/<slug>/slides';
  for (let i = 1; i <= N; i++) {
    await page.goto(`file://${process.cwd()}/${dir}/slide${i}.html`);
    await page.locator('.slide').screenshot({ path: `${dir}/slide${i}.png` });
  }
  await browser.close();
})();
```

Review each PNG using the Read tool (which renders images visually). Check for:
- Text overlapping other text or visuals
- Elements clipped by the 1080x1350 boundary
- Diagram components misaligned or colliding
- Unreadable text (too small, too low contrast)

If issues found: fix the HTML, re-screenshot that slide, re-review. Repeat until all slides pass.

**Fallback**: If Playwright/Chromium is unavailable (missing system libs), ask the user to screenshot manually and paste back for review.

## Content Principles

- **Risk language, not implementation:** "Agents can exfiltrate your code" not "The agent uses subprocess.run to execute shell commands"
- **Each slide is a screenshot candidate:** If someone shares just one slide, it should still make sense and deliver value
- **Sequential story:** The carousel tells a coherent narrative when swiped through
- **No filler slides:** If a point doesn't earn its own slide, fold it into another or cut it
- **Authentic voice:** Practitioner sharing what they found, not thought leader pontificating
