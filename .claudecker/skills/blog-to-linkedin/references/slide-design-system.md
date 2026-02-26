# Slide HTML Design System

Every slide must follow this exact structure and design system for visual consistency.

All sizes are optimized for 1080x1080 slides viewed on mobile phones. Prefer larger text over fitting more content.

## Base HTML Structure

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: #000; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
  .slide {
    width: 1080px; height: 1080px;
    background: #0F1419;
    position: relative; overflow: hidden;
    font-family: -apple-system, 'Segoe UI', 'Inter', 'Helvetica Neue', Arial, sans-serif;
  }
  .scanlines {
    position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background: repeating-linear-gradient(0deg, transparent, transparent 3px, rgba(255,255,255,0.015) 3px, rgba(255,255,255,0.015) 4px);
    pointer-events: none; z-index: 10;
  }
  .corner-tl { position: absolute; top: 48px; left: 48px; width: 24px; height: 24px; border-top: 2px solid rgba(29,161,242,0.3); border-left: 2px solid rgba(29,161,242,0.3); z-index: 5; }
  .corner-br { position: absolute; bottom: 48px; right: 48px; width: 24px; height: 24px; border-bottom: 2px solid rgba(29,161,242,0.3); border-right: 2px solid rgba(29,161,242,0.3); z-index: 5; }
  .series-marker { position: absolute; top: 56px; right: 72px; font-size: 13px; font-weight: 600; color: rgba(255,255,255,0.25); letter-spacing: 2px; text-transform: uppercase; z-index: 5; }
  .headline {
    position: absolute; left: 72px; right: 72px;
    font-size: 52px; font-weight: 800; color: #FFFFFF; line-height: 1.15; letter-spacing: -0.5px; z-index: 5;
  }
  .subtitle {
    position: absolute; bottom: 80px; left: 72px; right: 72px;
    font-size: 26px; font-weight: 400; color: rgba(255,255,255,0.5); line-height: 1.5; z-index: 5;
  }
  .accent-line { position: absolute; bottom: 100px; left: 72px; width: 60px; height: 3px; background: #1DA1F2; z-index: 5; }
</style>
</head>
<body>
<div class="slide">
  <div class="scanlines"></div>
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
2. **Scanlines overlay**: separate div, `pointer-events:none`, `z-index:10`
3. **Corner brackets**: top-left AND bottom-right, 24x24px, `rgba(29,161,242,0.3)`
4. **Series marker**: `"NN / NN"` format, top-right at `top:56px; right:72px`
5. **Accent line**: 60x3px blue bar at `bottom:100px; left:72px`

## Layout Rules

- **Margins**: 72px on all sides — all content stays within this boundary
- **Headline placement**: Cover slides use `bottom:200px`, all other slides use `top:72px`
- **Subtitle**: Always at `bottom:80px`
- **Visual content zone**: Between headline and subtitle (roughly 240px-800px vertical)
- **Center visuals**: Use `position:absolute; top:50%; left:50%; transform:translate(-50%, -N%)` for centered elements

## Typography

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| Headline | 52-54px | 800 | `#FFFFFF` |
| Subtitle | 26px | 400 | `rgba(255,255,255,0.5)` |
| Body/feature text | 22-24px | 500-600 | varies |
| Code/mono (main) | 22-26px | - | use `'SF Mono', 'Fira Code', 'Consolas', monospace` |
| Code/mono (output) | 18-19px | - | use `'SF Mono', 'Fira Code', 'Consolas', monospace` |
| Item names (threats, tools) | 24px | 700 | varies |
| Item descriptions | 18px | 400 | varies |
| Labels (step/time badges) | 15-16px | 600-700 | varies |
| Container/section labels | 16px | 700 | varies |
| Series marker | 13px | 600 | `rgba(255,255,255,0.25)` |

## Color System

Adapt colors to topic, but follow these opacity patterns:

| Use | Pattern |
|-----|---------|
| Subtle backgrounds | `rgba(color, 0.04-0.08)` |
| Borders | `rgba(color, 0.1-0.25)` |
| Muted text | `rgba(255,255,255, 0.3-0.5)` |
| Glow/shadow | `box-shadow: 0 0 12px rgba(color, 0.4)` or `0 0 24px rgba(color, 0.12)` |
| Highlight box | `background: rgba(color, 0.08); border: 2px solid color; box-shadow: 0 0 24px rgba(color, 0.12)` |

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
.pipe-box.default { background: rgba(255,255,255,0.04-0.06); border: 1.5-2px solid rgba(255,255,255,0.12-0.15); }
.pipe-box.highlight { background: rgba(accent,0.08-0.1); border: 2px solid accent; box-shadow: 0 0 24px rgba(accent,0.12); }
.arrow-connector { width: 40-60px; height: 2px; background: accent; }
.arrow-connector::after { /* triangle arrowhead via border trick */ }
```

### Bar chart
```css
.bar-row { display: flex; align-items: center; margin-bottom: 24px; }
.bar-label { width: 220px; text-align: right; padding-right: 24px; }
.bar-track { flex: 1; height: 40px; background: rgba(255,255,255,0.04); border-radius: 6px; overflow: hidden; }
.bar-fill { height: 100%; background: linear-gradient(90deg, color1, color2); border-radius: 6px; }
.bar-value { position: absolute; right: -56px; /* outside the bar */ }
```

### Grid rows (pass/fail lists)
```css
.grid-row { display: flex; align-items: center; gap: 16px; padding: 14px 20px; border-radius: 10px; }
.grid-row.fail { background: rgba(red,0.06); border: 1.5px solid rgba(red,0.25); }
.grid-row.pass { background: rgba(blue,0.06); border: 1.5px solid rgba(blue,0.2); }
```
Use proper SVG icons for status (circled X for fail, circled checkmark for pass).

### Stat callouts
```css
.big-number { font-size: 96px; font-weight: 900; color: highlight; line-height: 1; }
.big-label { font-size: 26px; font-weight: 600; color: rgba(highlight, 0.6); }
```

### Stat row (multiple stats side by side)
```css
.stats { display: flex; gap: 40px; }
.stat-value { font-size: 28px; font-weight: 800; color: highlight; }
.stat-label { font-size: 16px; font-weight: 500; color: rgba(highlight, 0.5); }
.stat-divider { width: 1px; background: rgba(255,255,255,0.08); }
```

### Pill tags
```css
.tag { padding: 8px 18px; border-radius: 20px; font-size: 17px; font-weight: 600; color: rgba(255,255,255,0.5); border: 1px solid rgba(255,255,255,0.12); }
```

### Timeline
```css
.timeline-line { height: 2px; background: rgba(255,255,255,0.1); }
.marker-dot { width: 14px; height: 14px; border-radius: 50%; }
.marker-dot.active { box-shadow: 0 0 12px rgba(color, 0.4); }
```

### Penalty/callout box
```css
.callout-box { border: 2px solid highlight; border-radius: 12px; padding: 24px 48px; text-align: center; background: rgba(highlight, 0.04); }
```

## SVG Icons

Use inline SVG with `stroke` outlines (not filled). Typical size: 22-28px viewBox.

```html
<!-- Shield -->
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1DA1F2" stroke-width="1.5">
  <path d="M12 3L4 7v5c0 5 3.5 9.7 8 11 4.5-1.3 8-6 8-11V7l-8-4z"/>
</svg>

<!-- User -->
<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.5)" stroke-width="1.5">
  <circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/>
</svg>

<!-- Document/LLM -->
<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.5)" stroke-width="1.5">
  <rect x="4" y="4" width="16" height="16" rx="3"/><path d="M9 9h6M9 12h6M9 15h3"/>
</svg>

<!-- Circled X (fail) -->
<svg width="22" height="22" viewBox="0 0 22 22">
  <circle cx="11" cy="11" r="10" fill="none" stroke="#E0245E" stroke-width="1.5"/>
  <path d="M7 7l8 8M15 7l-8 8" stroke="#E0245E" stroke-width="1.5" stroke-linecap="round"/>
</svg>

<!-- Circled check (pass) -->
<svg width="22" height="22" viewBox="0 0 22 22">
  <circle cx="11" cy="11" r="10" fill="none" stroke="#1DA1F2" stroke-width="1.5"/>
  <path d="M6 11l4 4 6-7" stroke="#1DA1F2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>
```

For cover slides, use larger SVGs (240x280+) with:
- SVG `<defs>` filters for glow effects (`feGaussianBlur` + `feMerge`)
- Secondary detail lines at low opacity for depth
- Background radial gradient glow behind the main visual

## Closing Slide Pattern

Center all content vertically. Add a faint SVG watermark at `opacity: 0.03` behind the text. Include: CTA text, URL in accent color, divider, author name, handle.
