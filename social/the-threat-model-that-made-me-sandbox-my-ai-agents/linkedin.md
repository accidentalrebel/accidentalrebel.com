# LinkedIn Content

Source: `content/the-threat-model-that-made-me-sandbox-my-ai-agents.md`

---

## Text Post

I gave an AI coding agent shell access to my machine, then sat down and mapped everything that could go wrong.

Eight specific threats. Not theoretical — based on incidents already happening in the wild. Data exfiltration, credential theft, lateral movement, supply chain injection through compromised MCP servers.

The first real MCP supply chain attack already happened. Compromised npm publish token, poisoned package downloaded 4,000 times in 8 hours, autonomous AI agent installed on each machine. An agent on your network is one curl away from infrastructure it has no business touching. Most setups have zero isolation between the agent and your host system.

After mapping the threats, I built a containerized sandbox. Docker wrapper with network lockdown, ephemeral sessions, no host filesystem access. The agent gets full capability inside a container where the blast radius is limited to the project directory.

You don't need my tool to act on this. Audit your settings.local.json for broad permissions you forgot you approved. Enable the built-in sandbox. Run your agent in a container. Review every MCP server and skill your agent loads.

Full threat model and mitigation matrix at accidentalrebel.com

#AISecurity #ThreatModeling #AgentSecurity #CyberSecurity #LLMSecurity

---

## Carousel Plan (3 slides — test run)

### Visual Identity

- Background: #ffffff (white)
- Accent color: #dc2626 (red)
- Text color: #24292f (dark gray)
- Text muted: #656d76
- Subtle background: #f6f8fa (light gray)
- Border: #d0d7de
- Style: Clean minimal, white-dominant with red accents
- Typography: Clean sans-serif, bold headlines top-left
- Motif: Minimal — thin red lines, subtle geometric touches
- Dimensions: 1080x1350
- Constraints: No photorealism, no clutter, professional, white/red palette

---

### Slide 1 (Cover)

**Headline:** "8 Threats From Giving AI Agents Shell Access"
**Key detail:** "I mapped them. Then I built a sandbox."
**Visual suggestion:** Large stylized terminal icon with a red warning triangle overlay. Clean, bold, high-contrast.
**Image prompt:** "Clean minimal slide, 1080x1350 portrait, white (#ffffff) background. Center: large stylized terminal window (240px) with thin dark gray (#24292f) strokes, a red (#dc2626) warning triangle overlaid on the terminal. Faint radial gradient glow behind terminal: rgba(220,38,38,0.06). Bottom-left at 280px from bottom: bold 52px dark (#24292f) text 'Eight threats from giving AI agents shell access'. Below that: 28px gray (#656d76) text 'I mapped them. Then I built a sandbox.' Red accent line 60x3px above subtitle. Corner brackets faint red rgba(220,38,38,0.25). Series marker top-right '01 / 03'. No photorealism, no clutter."

---

### Slide 2 (Core)

**Headline:** "One curl away from your infrastructure"
**Key detail:** AI agents have shell access, network access, and your credentials. The first MCP supply chain attack already happened — 4,000 installs in 8 hours.
**Visual suggestion:** Three threat cards stacked vertically: data exfiltration, credential theft, lateral movement. Each with a small icon and one-line description.
**Image prompt:** "Clean minimal slide, 1080x1350 portrait, white (#ffffff) background. Top-left: bold 52px dark (#24292f) headline 'One curl away from your infrastructure'. Below headline, vertically stacked, three content cards on light gray (#f6f8fa) backgrounds with #d0d7de borders, rounded 12px. Each card: left-side small SVG icon (stroke #dc2626), right-side 24px dark text name + 18px gray description. Card 1: outbound arrow icon, 'Data exfiltration' / 'Agent sends your code to any endpoint'. Card 2: key icon, 'Credential theft' / 'SSH keys, API tokens, cloud creds — all readable'. Card 3: network icon, 'Lateral movement' / 'One curl to internal services'. Below cards: red-bordered callout box with '4,000 installs in 8 hours' in 28px bold red, 'First real MCP supply chain attack' in 18px gray below. Subtitle bottom: '3 of 8 mapped threats'. Series marker '02 / 03'. Corner brackets, accent line. No photorealism."

---

### Slide 3 (Closing)

**Headline:** "Full threat model at accidentalrebel.com"
**Key detail:** Karlo Licudine / @accidentalrebel
**Visual suggestion:** Centered text, clean close. Faint shield watermark behind.
**Image prompt:** "Clean minimal slide, 1080x1350 portrait, white (#ffffff) background. Center vertically: bold 44px dark (#24292f) text 'Full threat model' on first line, 'and mitigation matrix' on second line. Below: 'accidentalrebel.com' in 36px red (#dc2626). Thin gray (#d0d7de) horizontal divider 120px wide. Below divider: 'Karlo Licudine' in 24px dark text, '@accidentalrebel' in 20px gray (#656d76). Faint shield SVG watermark centered behind all text at opacity 0.03, 300px tall, stroke #dc2626. Corner brackets, accent line, series marker '03 / 03'. No photorealism, no clutter."
