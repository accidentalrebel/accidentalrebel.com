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
- Dimensions: 1080x1350 (4:5 portrait — LinkedIn recommended)
- Constraints: No photorealism, no clutter, professional, white/red palette
```

Use the blog's white-and-red color scheme for all carousels. Add variety through layout, visual weight, and selective use of the subtle gray background — not through changing the palette.

### Content-First Slide Philosophy

Core slides are **text-forward**. The primary content is readable text — headlines, short paragraphs, and icon-bulleted lists. Diagrams and illustrations are the exception, not the default.

Each core slide follows this vertical flow:
1. **Big headline** (top) — the one thing this slide communicates
2. **Supporting paragraph** — 1-2 sentences of context below the headline
3. **Icon-bulleted list** — 2-4 scannable items, each with a small inline SVG icon
4. **Concluding statement** (bottom) — a bold takeaway or transition line

This is modeled on high-performing LinkedIn carousels where every slide is readable at a glance — big text, clear hierarchy, list-like structure. Think "slide as a page of notes" not "slide as an infographic."

**When to use visuals:** Cover slides may include a simple centered icon. A single core slide per carousel may use a diagram or stat callout if the point is inherently visual (e.g., a before/after, a flow, a big number). But the default for core slides is text + list.

### Per-Slide Format

For each slide, provide:

| Field | Description |
|-------|-------------|
| **Slide N (Role)** | Number and role: Cover, Core, or Closing |
| **Headline** | Short bold statement — the one thing this slide communicates |
| **Supporting text** | 1-2 sentences of context that frames the headline |
| **List items** | 2-4 bullet points (icon + text), scannable at a glance. Omit if slide is a stat callout or diagram |
| **Concluding line** | Bold takeaway or transition at the bottom of the slide |
| **Visual note** | _(Optional)_ Only if this slide uses a diagram, stat callout, or icon instead of the standard text layout |

### Slide Text Writing Rules

The slide plan text is the **final rendered text** — it will appear on screen exactly as written. Apply all voice and content rules when writing it, not after.

**Voice (same rules as the text post):**
- Direct, practitioner-grounded. "I found X" not "It was discovered that X"
- No buzzwords: no "landscape", "leverage", "crucial", "robust", "ecosystem"
- No engagement bait: no "You won't believe..." or "Here's why you should care..."
- No fluff padding. Every sentence earns its place
- Write as a practitioner sharing findings with peers, not a marketer promoting content

**Content framing:**
- Risk language, not implementation: "Agents can exfiltrate your code" not "The agent uses subprocess.run to execute shell commands"
- Organizational risk for security leadership, not tutorial-level detail
- Each slide must stand alone — if someone screenshots one slide, it delivers value on its own

**Slide-specific text constraints:**
- **Headlines:** 3-6 words. Bold claim or topic label. No full sentences
- **Supporting text:** 1-2 sentences max. Context, not explanation. If it runs long, cut it or move detail to a list item
- **List items:** Fragments or single sentences. Concrete and specific — names, numbers, real examples. No vague generalities ("various security risks")
- **Concluding line:** One sentence. A takeaway the reader walks away with, or a transition to the next slide. Bold and direct

**Writing process:** Draft all slide text, then review the full carousel for voice consistency. Run `/arebel-voice` on the slide text the same way you would on the text post. Fix any buzzwords, passive constructions, or padding before presenting the plan.

### Slide Structure

- **Slide 1 (Cover):** Title + subtitle. Create curiosity or state a bold claim. May include a simple centered icon. Make someone start swiping.
- **Slides 2-N (Core):** One point per slide, text-forward layout. Each stands alone — someone swiping fast gets value from any single slide. Use the headline → paragraph → icon-list → concluding line structure. Prioritize: surprising findings, actionable insights, risk-relevant facts. Cut filler.
- **Final slide (Closing):** CTA. "Full breakdown at accidentalrebel.com" + "Juan Karlo Licudine / @accidentalrebel"

Refer to [references/example.md](references/example.md) for a complete example transformation showing the full carousel plan.

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

After generating all slides, screenshot each one and visually review for issues. Fix and re-screenshot until clean.

**Screenshot all slides** (Python Playwright is pre-installed via pip — no setup needed):
```python
from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 1350})
    slide_dir = f"social/<slug>/slides"
    for i in range(1, N + 1):
        path = os.path.abspath(f"{slide_dir}/slide{i}.html")
        page.goto(f"file://{path}")
        page.locator(".slide").screenshot(path=f"{slide_dir}/slide{i}.png")
    browser.close()
```

Review each PNG using the Read tool (which renders images visually). Check for:
- Text overlapping other text or visuals
- Elements clipped by the slide boundary
- Diagram components misaligned or colliding
- Unreadable text (too small, too low contrast)
- **Excessive empty space** — if the content only fills the top portion and the bottom half is blank, the slide height needs to shrink

If issues found: fix the HTML, re-screenshot that slide, re-review. Repeat until all slides pass.

### Slide Height Adjustment

The default slide height is 1350px (4:5 portrait at 1080px wide). After the first QA pass, evaluate whether the content fills the slides well. If most slides have a large blank area below the concluding line, reduce the slide height to better fit the content:

1. Estimate where the lowest content element sits across all slides (excluding the bottom-anchored subtitle and accent line)
2. Pick a new height that leaves ~150-200px of breathing room below the last content element, while keeping the subtitle and accent line anchored near the bottom
3. Update the `.slide` height, reposition `.subtitle`, `.accent-line`, and `.corner-br` to match
4. Re-screenshot and re-review

Common reduced heights: 1200px, 1080px (square), or anywhere in between. The goal is every slide feeling well-filled, not cramped.

## Content Principles

These apply to **both** the LinkedIn text post and all carousel slide text:

- **Risk language, not implementation:** "Agents can exfiltrate your code" not "The agent uses subprocess.run to execute shell commands"
- **Each slide is a screenshot candidate:** If someone shares just one slide, it should still make sense and deliver value
- **Sequential story:** The carousel tells a coherent narrative when swiped through
- **No filler slides:** If a point doesn't earn its own slide, fold it into another or cut it
- **Authentic voice:** Practitioner sharing what they found, not thought leader pontificating
- **No emojis** in any output — text post or slides
