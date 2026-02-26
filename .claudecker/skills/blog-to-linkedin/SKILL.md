---
name: blog-to-linkedin
description: Convert a blog post into LinkedIn-ready content — a text post and a carousel slide
  plan with image generation prompts. Use when the user says "LinkedIn", "convert to LinkedIn",
  "carousel", "promote this post", or provides a blog post and wants social media content.
  Also use when the user points to a blog post file and asks for LinkedIn or social content.
---

# Blog to LinkedIn

Convert a completed blog post into three outputs:
1. A ready-to-paste **LinkedIn text post**
2. A **carousel slide plan** with image generation prompts
3. **Rendered HTML slides** — one self-contained HTML file per slide

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

**Voice rules:**
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
- Background: [color hex]
- Accent color: [color hex]
- Warning/danger color: [color hex]
- Style: [e.g. flat minimal, dark tech, clean corporate]
- Typography direction: [e.g. clean sans-serif, bold headlines top-left]
- Recurring motif: [e.g. circuit-board pattern, node graph, grid lines]
- Layout grid: [e.g. headline top-left, visual center, detail text bottom]
- Dimensions: 1080x1080
- Constraints: no photorealism, no clutter, professional
```

Choose colors and style that fit the blog post's subject matter. Dark tech aesthetic works for security topics. Adjust for other domains.

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
- **Final slide (Closing):** CTA. "Full breakdown at accidentalrebel.com" + "Karlo Licudine / @accidentalrebel"

### Image Prompt Requirements

Each prompt must specify:
- Dimensions (1080x1080)
- Background color (from visual identity)
- Accent colors used in this slide
- What visual elements appear and where
- What text overlays to render and their position
- Style consistency note ("Consistent with series" or "Matching carousel style")
- Exclusions (no photorealism, no clutter)

Refer to [references/example.md](references/example.md) for a complete example transformation showing the full carousel plan with image prompts.

## Output 3: Rendered HTML Slides

After finalizing the carousel plan, render each slide as a self-contained HTML file. Save to `social/<slug>/slides/slide1.html`, `slide2.html`, etc.

### HTML Slide Requirements

- **Dimensions**: Single `div` at 1080x1080px, centered on page
- **Background**: Solid color from visual identity + CSS `repeating-linear-gradient` for scan-line/texture effects
- **Icons/diagrams/charts**: Inline SVG (`<path>`, `<rect>`, `<circle>`, `<text>`) — no external images or libraries
- **Text**: `position: absolute` with pixel coordinates. System font stack (`-apple-system, 'Segoe UI', Arial`)
- **Colors**: Reuse the 4-5 colors defined in the visual identity block across all slides
- **No dependencies**: Everything inline — no CDN links, no external fonts, no JS libraries
- **Static by default**: No animations unless requested

The user opens each HTML file in a browser and screenshots at 1080x1080.

## Content Principles

- **Risk language, not implementation:** "Agents can exfiltrate your code" not "The agent uses subprocess.run to execute shell commands"
- **Each slide is a screenshot candidate:** If someone shares just one slide, it should still make sense and deliver value
- **Sequential story:** The carousel tells a coherent narrative when swiped through
- **No filler slides:** If a point doesn't earn its own slide, fold it into another or cut it
- **Authentic voice:** Practitioner sharing what they found, not thought leader pontificating
