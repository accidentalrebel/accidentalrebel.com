# Slide HTML Design System

Every slide must follow this exact structure and design system for visual consistency.

Default dimensions: 1080x1350 portrait (4:5 ratio). The height may be reduced after QA if content doesn't fill the slides (see "Slide Height Adjustment" in SKILL.md). Width is always 1080px. When reducing height, reposition bottom-anchored elements (`.subtitle`, `.accent-line`, `.corner-br`) proportionally.

## Base HTML Structure

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: #f6f8fa; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
  .slide {
    width: 1080px; height: 1350px;
    background: #ffffff;
    position: relative; overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  }
  .dot-texture {
    position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle, rgba(105,105,105,0.18) 4px, transparent 4px);
    background-size: 56px 56px;
    -webkit-mask-image: radial-gradient(ellipse at center, rgba(0,0,0,0.25) 0%, rgba(0,0,0,0.25) 30%, rgba(0,0,0,0.75) 100%);
    mask-image: radial-gradient(ellipse at center, rgba(0,0,0,0.25) 0%, rgba(0,0,0,0.25) 30%, rgba(0,0,0,0.75) 100%);
    pointer-events: none; z-index: 2;
  }
  .corner-tl { position: absolute; top: 48px; left: 48px; width: 48px; height: 48px; border-top: 4px solid rgba(220,38,38,0.4); border-left: 4px solid rgba(220,38,38,0.4); z-index: 5; }
  .corner-br { position: absolute; bottom: 48px; right: 48px; width: 48px; height: 48px; border-bottom: 4px solid rgba(220,38,38,0.4); border-right: 4px solid rgba(220,38,38,0.4); z-index: 5; }
  .series-marker { position: absolute; top: 56px; right: 72px; font-size: 20px; font-weight: 600; color: rgba(36,41,47,0.3); letter-spacing: 3px; text-transform: uppercase; z-index: 5; }
  .headline {
    position: absolute; left: 72px; right: 72px;
    font-size: 52px; font-weight: 800; color: #24292f; line-height: 1.15; letter-spacing: -0.5px; z-index: 5;
  }
  .subtitle {
    position: absolute; bottom: 80px; left: 72px; right: 72px;
    font-size: 28px; font-weight: 400; color: #656d76; line-height: 1.5; z-index: 5;
  }
  .accent-line { position: absolute; bottom: 110px; left: 72px; width: 60px; height: 3px; background: #dc2626; z-index: 5; }
</style>
</head>
<body>
<div class="slide">
  <div class="dot-texture"></div>
  <div class="corner-tl"></div>
  <div class="corner-br"></div>
  <div class="series-marker">01 / 08</div>

  <div class="headline" style="top:72px">...</div>
  <!-- Slide-specific content here -->
  <div class="subtitle">...</div>
  <div class="accent-line"></div>
</div>
</body>
</html>
```

## Mandatory Elements on Every Slide

1. **CSS reset**: `* { margin:0; padding:0; box-sizing:border-box }`
2. **Dot texture**: Gray dot grid (`56px` spacing, `4px` radius, `rgba(105,105,105,0.18)`), masked with radial gradient — 25% visible at center, 75% at edges. `pointer-events:none`, `z-index:2`
3. **Corner brackets**: top-left AND bottom-right, 48x48px, 4px stroke, `rgba(220,38,38,0.4)`
4. **Series marker**: `"NN / NN"` format, 20px, top-right at `top:56px; right:72px`
5. **Accent line**: 60x3px red bar at `bottom:110px; left:72px`

## Layout Rules

- **Margins**: 72px on all sides — all content stays within this boundary
- **Headline placement**: Cover slides use `bottom:280px`, all other slides use `top:72px`
- **Subtitle**: Always at `bottom:80px`
- **Content zone**: Between headline and subtitle (roughly 180px–1050px vertical)
- **Default layout is text-forward**: headline → supporting paragraph → icon-bulleted list → concluding statement. Use the `.content` container starting at `top:180px` to flow these elements naturally
- **Center visuals sparingly**: Use `position:absolute; top:50%; left:50%; transform:translate(-50%, -N%)` only for the rare diagram or stat callout slide

## Typography

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| Headline | 52-54px | 800 | `#24292f` |
| Supporting text | 28px | 500 | `#24292f` |
| Icon-list item text | 26px | 400 | `#24292f` |
| Concluding statement | 28px | 700 | `#24292f` |
| Subtitle (bottom) | 28px | 400 | `#656d76` |
| Body/feature text | 22-24px | 500-600 | varies |
| Code/mono (main) | 22-26px | - | use `'SF Mono', 'Fira Code', 'Consolas', monospace` |
| Code/mono (output) | 18-19px | - | use `'SF Mono', 'Fira Code', 'Consolas', monospace` |
| Item names (threats, tools) | 24px | 700 | varies |
| Item descriptions | 18px | 400 | varies |
| Labels (step/time badges) | 15-16px | 600-700 | varies |
| Container/section labels | 16px | 700 | varies |
| Series marker | 20px | 600 | `rgba(36,41,47,0.3)` |

## Color System

The palette is white-dominant with red (`#dc2626`) as the primary accent. Keep it clean — variety comes from layout, not color.

### Core Palette

| Token | Value | Usage |
|-------|-------|-------|
| Background | `#ffffff` | Slide background |
| Text | `#24292f` | Headlines, body text |
| Text muted | `#656d76` | Subtitles, secondary text |
| Accent | `#dc2626` | Accent lines, highlights, key callouts |
| Subtle bg | `#f6f8fa` | Card/box backgrounds, content panels |
| Border | `#d0d7de` | Dividers, container borders |

### Opacity Patterns

| Use | Pattern |
|-----|---------|
| Subtle backgrounds | `rgba(220,38,38, 0.04-0.08)` or `#f6f8fa` |
| Borders | `#d0d7de` or `rgba(220,38,38, 0.15-0.25)` for accent borders |
| Muted text | `#656d76` |
| Glow/shadow | `box-shadow: 0 2px 8px rgba(0,0,0,0.06)` or `0 0 24px rgba(220,38,38,0.08)` |
| Highlight box | `background: rgba(220,38,38, 0.04); border: 2px solid #dc2626; box-shadow: 0 0 24px rgba(220,38,38,0.08)` |
| Danger/warning | `#dc2626` (same red, used contextually) |

## CSS Approach

- Use a `<style>` block with classes — NOT inline styles
- Define shared classes (`.pipe-box`, `.bar-row`, `.grid-row`) for repeated patterns
- Use flexbox for layouts (pipelines, grids, stat rows)
- Use `position: absolute` for fixed elements (headline, subtitle, corner brackets)

## Component Patterns

### Primary: Text-forward layout (default for core slides)

The default core slide layout. Most slides should use this structure — text is the visual.

```css
/* Content container — flows top to bottom within margins */
.content { position: absolute; top: 180px; left: 72px; right: 72px; z-index: 5; }

/* Supporting paragraph below headline */
.supporting-text { font-size: 28px; font-weight: 500; color: #24292f; line-height: 1.55; margin-bottom: 48px; }

/* Icon-bulleted list */
.icon-list { display: flex; flex-direction: column; gap: 28px; margin-bottom: 48px; }
.icon-list-item { display: flex; align-items: flex-start; gap: 20px; }
.icon-list-item svg { flex-shrink: 0; margin-top: 4px; }
.icon-list-item .item-text { font-size: 26px; font-weight: 400; color: #24292f; line-height: 1.45; }

/* Concluding statement — bold takeaway at the bottom */
.concluding { font-size: 28px; font-weight: 700; color: #24292f; line-height: 1.4; }
```

**Vertical flow:** headline (top:72px) → `.content` container starting at ~180px → supporting-text → icon-list → concluding statement. The subtitle and accent-line remain anchored at the bottom.

Icon-list icons: use small inline SVGs (20-24px) in accent red (`#dc2626`) or muted gray (`#656d76`). Keep icons simple — chevrons, checkmarks, arrows, shields. The icon is a visual bullet, not a feature illustration.

### Secondary: Visual patterns (use sparingly)

These patterns are available for the occasional slide that benefits from a visual element. Limit to 1-2 visual slides per carousel — most slides should use the text-forward layout above.

#### Stat callout
```css
.big-number { font-size: 96px; font-weight: 900; color: #dc2626; line-height: 1; }
.big-label { font-size: 26px; font-weight: 600; color: #656d76; }
```

#### Stat row (multiple stats side by side)
```css
.stats { display: flex; gap: 40px; }
.stat-value { font-size: 28px; font-weight: 800; color: #dc2626; }
.stat-label { font-size: 16px; font-weight: 500; color: #656d76; }
.stat-divider { width: 1px; background: #d0d7de; }
```

#### Pipeline (flow diagrams)
```css
.pipeline { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -30%); display: flex; align-items: center; gap: 0; z-index: 5; }
.pipe-box { width: 160-200px; height: 80-100px; border-radius: 14-16px; display: flex; flex-direction: column; align-items: center; justify-content: center; }
.pipe-box.default { background: #f6f8fa; border: 1.5-2px solid #d0d7de; }
.pipe-box.highlight { background: rgba(220,38,38,0.05); border: 2px solid #dc2626; box-shadow: 0 0 24px rgba(220,38,38,0.08); }
.arrow-connector { width: 40-60px; height: 2px; background: #dc2626; }
.arrow-connector::after { /* triangle arrowhead via border trick */ }
```

#### Grid rows (pass/fail lists)
```css
.grid-row { display: flex; align-items: center; gap: 16px; padding: 14px 20px; border-radius: 10px; }
.grid-row.fail { background: rgba(220,38,38,0.04); border: 1.5px solid rgba(220,38,38,0.25); }
.grid-row.pass { background: #f6f8fa; border: 1.5px solid #d0d7de; }
```
Use proper SVG icons for status (circled X for fail, circled checkmark for pass).

#### Pill tags
```css
.tag { padding: 8px 18px; border-radius: 20px; font-size: 17px; font-weight: 600; color: #656d76; border: 1px solid #d0d7de; }
```

#### Callout box
```css
.callout-box { border: 2px solid #dc2626; border-radius: 12px; padding: 24px 48px; text-align: center; background: rgba(220,38,38, 0.03); }
```

#### Content card
```css
.content-card { background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 12px; padding: 32px; }
```

## SVG Icons

Use inline SVG with `stroke` outlines (not filled). Typical size: 22-28px viewBox.

### Icon-list bullet icons (20-24px, used in text-forward layouts)

Use these as visual bullets in icon-lists. Pick icons that relate to the list item's meaning. Keep them simple — they're bullets, not illustrations.

```html
<!-- Chevron-right (generic bullet) -->
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2" stroke-linecap="round">
  <path d="M9 6l6 6-6 6"/>
</svg>

<!-- Checkmark (positive/included) -->
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M5 12l5 5L19 7"/>
</svg>

<!-- Warning triangle (risk/threat) -->
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M12 3L2 21h20L12 3zM12 9v5M12 17h.01"/>
</svg>

<!-- Arrow-right (flow/consequence) -->
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2" stroke-linecap="round">
  <path d="M5 12h14M13 6l6 6-6 6"/>
</svg>
```

### Larger icons (for diagrams, cover slides, feature callouts)

```html
<!-- Shield -->
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="1.5">
  <path d="M12 3L4 7v5c0 5 3.5 9.7 8 11 4.5-1.3 8-6 8-11V7l-8-4z"/>
</svg>

<!-- User -->
<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#656d76" stroke-width="1.5">
  <circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/>
</svg>

<!-- Document/LLM -->
<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#656d76" stroke-width="1.5">
  <rect x="4" y="4" width="16" height="16" rx="3"/><path d="M9 9h6M9 12h6M9 15h3"/>
</svg>

<!-- Circled X (fail) -->
<svg width="22" height="22" viewBox="0 0 22 22">
  <circle cx="11" cy="11" r="10" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <path d="M7 7l8 8M15 7l-8 8" stroke="#dc2626" stroke-width="1.5" stroke-linecap="round"/>
</svg>

<!-- Circled check (pass) -->
<svg width="22" height="22" viewBox="0 0 22 22">
  <circle cx="11" cy="11" r="10" fill="none" stroke="#24292f" stroke-width="1.5"/>
  <path d="M6 11l4 4 6-7" stroke="#24292f" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>
```

For cover slides, use larger SVGs (240x300+) with:
- Light drop shadow (`filter: drop-shadow(0 4px 12px rgba(0,0,0,0.08))`)
- Red accent strokes for key elements
- Background radial gradient glow behind the main visual: `radial-gradient(circle, rgba(220,38,38,0.06) 0%, transparent 70%)`

## Closing Slide Pattern

Center all content vertically. Add a faint SVG watermark at `opacity: 0.03` behind the text. Include: CTA text, URL in red accent, divider, author name, handle.
