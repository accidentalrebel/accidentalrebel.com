# LinkedIn Content for: EU AI Act Prompt Injection Defense

Source post: `content/eu-ai-act-prompt-injection-defense.md`

---

## Text Post

40% of encoded prompt injections bypass the classifiers you're probably relying on.

I tested ProtectAI's most-downloaded prompt injection classifier against encoded attacks — leetspeak, base64, ROT13, dot-separated characters, and combinations. Eight out of twenty encoded payloads sailed right through. Not because the classifier is bad. Because it was trained on natural language, and encoded text isn't natural language.

The Mindgard/Lancaster paper confirmed this at scale: emoji smuggling hit 100% bypass rates against Azure Prompt Shields, Meta PromptGuard, and Lakera Guard. All six products tested were defeated by character-level encoding tricks that any web security tester already knows.

The fix is a preprocessing normalizer — seven layers that strip encoding tricks before the text reaches the classifier. Zero-width characters, homoglyphs, leet, base64, ROT13, hex, separated characters. After adding it: 20/20 encoded attacks caught, zero false positives, under 1ms added latency. A few hundred lines of code, not a new vendor contract.

The EU AI Act requires high-risk AI systems to defend against exactly this class of attack by August 2026. Penalties run up to EUR 15M or 3% of global turnover. If your classifier isn't normalizing inputs, you have a gap that's both exploitable and non-compliant.

Full technical breakdown with test results at accidentalrebel.com

#PromptInjection #AISecurity #EUAIAct #LLMSecurity #CyberSecurity

---

## Carousel Plan

### Visual Identity

- Background: #0F1419 (dark charcoal)
- Accent color: #1DA1F2 (blue)
- Warning color: #E0245E (red)
- Highlight color: #FFAD1F (amber, for stats/numbers)
- Style: Dark tech aesthetic, flat minimal, regulatory gravity
- Typography: Clean sans-serif, bold headlines top-left, detail text bottom
- Motif: Subtle horizontal scan lines / data-stream pattern in background
- Layout: Headline top-left, visual element center, detail text bottom
- Dimensions: 1080x1080
- Constraints: No photorealism, no clutter, professional

---

### Slide 1 (Cover)

**Headline:** "40% of Encoded Prompt Injections Bypass Your Classifier"
**Key detail:** Subtitle — "The EU AI Act says that's not good enough."
**Visual suggestion:** A shield icon with a crack through it, data streams passing through the crack
**Image prompt:** "Minimal dark tech slide, 1080x1080, background #0F1419 with subtle horizontal scan-line pattern. Center: flat shield icon in blue (#1DA1F2) with a visible crack/fracture down the middle, small red (#E0245E) data stream particles passing through the crack. Top-left bold white sans-serif text: '40% of Encoded Prompt Injections Bypass Your Classifier'. Bottom-left smaller white text: 'The EU AI Act says that's not good enough.' Clean, professional, no photorealism."

---

### Slide 2 (Core)

**Headline:** "Classifiers are the standard defense"
**Key detail:** A classifier sits between user input and your LLM, catching malicious prompts before they execute. Azure Prompt Shields, Lakera Guard, ProtectAI — all take this approach.
**Visual suggestion:** Simple pipeline diagram: User -> Classifier -> LLM
**Image prompt:** "Minimal dark tech slide, 1080x1080, background #0F1419 with subtle scan lines. Center: flat horizontal pipeline — three rounded rectangles labeled 'User Input', 'Classifier', 'LLM' connected by blue (#1DA1F2) arrows left to right. The Classifier box has a small shield icon. Top-left bold white sans-serif text: 'Classifiers Are the Standard Defense.' Bottom smaller white text: 'They sit between user input and your LLM. Azure, Lakera, ProtectAI all take this approach.' Consistent with carousel series."

---

### Slide 3 (Core)

**Headline:** "Attackers encode their way around them"
**Key detail:** Same malicious words, different characters. Leetspeak, base64, ROT13, Unicode tricks — techniques borrowed straight from web application security.
**Visual suggestion:** Side-by-side showing plain text vs encoded text, both saying the same thing
**Image prompt:** "Minimal dark tech slide, 1080x1080, background #0F1419. Center: two text blocks side by side. Left block in white monospace: 'Ignore all previous instructions' with a red (#E0245E) 'BLOCKED' stamp. Right block in amber (#FFAD1F) monospace: '1gn0r3 4ll pr3v10us 1nstruct10ns' with a green checkmark and 'PASSED'. An equals sign between them. Top-left bold white text: 'Attackers Encode Their Way Around Them.' Bottom smaller white text: 'Same words, different characters. Borrowed from web security.' Consistent series style."

---

### Slide 4 (Core)

**Headline:** "Research confirms: all major products bypassed"
**Key detail:** Mindgard/Lancaster tested 12 attack methods against 6 guardrails. Emoji smuggling: 100% bypass. Unicode tags: 90%. Bidirectional text: 99%. Every product was defeated.
**Visual suggestion:** Bar chart showing bypass rates for top attack types
**Image prompt:** "Minimal dark tech slide, 1080x1080, background #0F1419. Center: horizontal bar chart with 5 bars. Labels on left in white: 'Emoji smuggling', 'Upside-down text', 'Unicode tags', 'Bidi text', 'Number substitution'. Bars filled in red (#E0245E) to varying lengths: 100%, 100%, 90%, 99%, 95%. Percentage labels in amber (#FFAD1F) at bar ends. Top-left bold white text: 'All Major Products Bypassed.' Bottom smaller white text: '12 attack methods tested against 6 guardrails. Source: Mindgard/Lancaster, 2025.' Consistent series style."

---

### Slide 5 (Core)

**Headline:** "My test: 8 of 20 encoded attacks got through"
**Key detail:** Tested DeBERTa classifier on 20 encoded injections across 7 encoding types. Leetspeak, base64, ROT13, and combinations all bypassed cleanly. The 60% that were caught was a tokenizer side effect, not a defense.
**Visual suggestion:** Grid of encoding types with pass/fail indicators
**Image prompt:** "Minimal dark tech slide, 1080x1080, background #0F1419. Center: grid layout with 7 rows, each showing an encoding name and a status icon. 'Leetspeak' with red X, 'Base64' with red X, 'ROT13' with red X, 'Dot-separated' with red X, 'Zero-width' with blue checkmark, 'Homoglyphs' with blue checkmark, 'Hex' with blue checkmark. Red (#E0245E) for bypassed, blue (#1DA1F2) for caught. Large amber (#FFAD1F) text '40% bypassed' to the right. Top-left bold white text: '8 of 20 Encoded Attacks Got Through.' Consistent series style."

---

### Slide 6 (Core)

**Headline:** "The fix: a 7-layer normalizer"
**Key detail:** Strip encoding tricks before the classifier sees them. Zero-width chars, homoglyphs, leet, base64, ROT13, hex, separated characters. Result: 20/20 caught, 0 false positives, <1ms added latency.
**Visual suggestion:** Updated pipeline with normalizer inserted before classifier
**Image prompt:** "Minimal dark tech slide, 1080x1080, background #0F1419. Center: horizontal pipeline — four rounded rectangles: 'User Input', 'Normalizer' (highlighted with amber #FFAD1F border, labeled '7 layers'), 'Classifier', 'LLM' connected by blue (#1DA1F2) arrows. Above the normalizer, small icons representing each layer in a vertical stack. Below pipeline: '20/20 caught | 0 false positives | <1ms latency' in amber text. Top-left bold white text: 'The Fix: a 7-Layer Normalizer.' Consistent series style."

---

### Slide 7 (Core)

**Headline:** "The EU AI Act makes this a compliance requirement"
**Key detail:** High-risk AI must defend against "adversarial examples" by August 2026. Penalties: up to EUR 15M or 3% global turnover. Incident reporting required within 2-15 days.
**Visual suggestion:** Timeline with key dates and penalty callout
**Image prompt:** "Minimal dark tech slide, 1080x1080, background #0F1419. Center: horizontal timeline with three date markers. 'Aug 2025' in blue (#1DA1F2) labeled 'GPAI obligations'. 'Aug 2026' in red (#E0245E) labeled 'High-risk AI deadline'. 'Dec 2027' in muted gray labeled 'Possible delay (Omnibus)'. Below timeline: penalty callout box with amber (#FFAD1F) border: 'EUR 15M or 3% global turnover'. Top-left bold white text: 'EU AI Act: This Is a Compliance Requirement.' Consistent series style."

---

### Slide 8 (Closing)

**Headline:** "Full breakdown at accidentalrebel.com"
**Key detail:** Karlo Licudine / @accidentalrebel / AI security practitioner
**Visual suggestion:** Clean close with name, URL, and blog reference
**Image prompt:** "Minimal dark tech slide, 1080x1080, background #0F1419 with subtle scan-line motif. Center: bold white sans-serif text 'Full breakdown with test results' on one line, 'accidentalrebel.com' in blue (#1DA1F2) below. Bottom: 'Karlo Licudine — @accidentalrebel' in smaller white text. Clean, professional. Consistent series style."
