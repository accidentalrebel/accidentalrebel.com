# Slide HTML Design System

Every slide must follow this exact structure and design system for visual consistency.

All sizes are optimized for 1080x1350 portrait slides (4:5 ratio) viewed on mobile phones. Prefer larger text over fitting more content. The extra vertical space compared to square slides gives room to breathe — use it for spacing, not cramming.

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
- **Visual content zone**: Between headline and subtitle (roughly 240px–1050px vertical) — the portrait format gives significantly more room here than square
- **Center visuals**: Use `position:absolute; top:50%; left:50%; transform:translate(-50%, -N%)` for centered elements

## Typography

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| Headline | 52-54px | 800 | `#24292f` |
| Subtitle | 28px | 400 | `#656d76` |
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

### Pipeline (flow diagrams)
```css
.pipeline { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -30%); display: flex; align-items: center; gap: 0; z-index: 5; }
.pipe-box { width: 160-200px; height: 80-100px; border-radius: 14-16px; display: flex; flex-direction: column; align-items: center; justify-content: center; }
.pipe-box.default { background: #f6f8fa; border: 1.5-2px solid #d0d7de; }
.pipe-box.highlight { background: rgba(220,38,38,0.05); border: 2px solid #dc2626; box-shadow: 0 0 24px rgba(220,38,38,0.08); }
.arrow-connector { width: 40-60px; height: 2px; background: #dc2626; }
.arrow-connector::after { /* triangle arrowhead via border trick */ }
```

### Bar chart
```css
.bar-row { display: flex; align-items: center; margin-bottom: 24px; }
.bar-label { width: 220px; text-align: right; padding-right: 24px; color: #24292f; }
.bar-track { flex: 1; height: 40px; background: #f6f8fa; border-radius: 6px; overflow: hidden; }
.bar-fill { height: 100%; background: linear-gradient(90deg, #dc2626, #ef4444); border-radius: 6px; }
.bar-value { position: absolute; right: -56px; /* outside the bar */ }
```

### Grid rows (pass/fail lists)
```css
.grid-row { display: flex; align-items: center; gap: 16px; padding: 14px 20px; border-radius: 10px; }
.grid-row.fail { background: rgba(220,38,38,0.04); border: 1.5px solid rgba(220,38,38,0.25); }
.grid-row.pass { background: #f6f8fa; border: 1.5px solid #d0d7de; }
```
Use proper SVG icons for status (circled X for fail, circled checkmark for pass).

### Stat callouts
```css
.big-number { font-size: 96px; font-weight: 900; color: #dc2626; line-height: 1; }
.big-label { font-size: 26px; font-weight: 600; color: #656d76; }
```

### Stat row (multiple stats side by side)
```css
.stats { display: flex; gap: 40px; }
.stat-value { font-size: 28px; font-weight: 800; color: #dc2626; }
.stat-label { font-size: 16px; font-weight: 500; color: #656d76; }
.stat-divider { width: 1px; background: #d0d7de; }
```

### Pill tags
```css
.tag { padding: 8px 18px; border-radius: 20px; font-size: 17px; font-weight: 600; color: #656d76; border: 1px solid #d0d7de; }
```

### Timeline
```css
.timeline-line { height: 2px; background: #d0d7de; }
.marker-dot { width: 14px; height: 14px; border-radius: 50%; }
.marker-dot.active { background: #dc2626; box-shadow: 0 0 12px rgba(220,38,38,0.3); }
.marker-dot.inactive { background: #d0d7de; }
```

### Penalty/callout box
```css
.callout-box { border: 2px solid #dc2626; border-radius: 12px; padding: 24px 48px; text-align: center; background: rgba(220,38,38, 0.03); }
```

### Content card (use the extra portrait height)
```css
.content-card { background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 12px; padding: 32px; }
```

## SVG Icons

Use inline SVG with `stroke` outlines (not filled). Typical size: 22-28px viewBox.

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
