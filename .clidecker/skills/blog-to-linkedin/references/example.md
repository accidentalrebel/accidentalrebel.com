# Example Transformation

Source blog post: "The threat model that made me sandbox my AI agents" — 1500+ words covering 8 threats, tool architecture, and mitigations.

## LinkedIn Text Post

```
Most developers hand AI agents a terminal and never think about what that means.

I mapped 8 specific threats that come with giving AI coding agents shell access — data exfiltration, file system escape, lateral network movement, compromised tool supply chains, and more.

These aren't theoretical. The first real MCP supply chain attack already happened. An agent on your network is one curl away from infrastructure it has no business touching. And most setups have zero isolation between the agent and your host system.

After mapping the threats, I built a containerized sandbox — Docker wrapper with network lockdown, per-project images, and no host access. It adds friction. It's worth it.

Full threat model and tool at accidentalrebel.com

#AISecurity #ThreatModeling #AgentSecurity #CyberSecurity #LLMSecurity
```

## Carousel Plan

### Visual Identity

- Background: #ffffff (white)
- Accent color: #dc2626 (red)
- Text color: #24292f (dark gray)
- Text muted: #656d76
- Subtle background: #f6f8fa (light gray)
- Border: #d0d7de
- Style: Clean minimal, white-dominant with red accents
- Typography: Clean sans-serif, bold headlines top-left, detail text bottom
- Motif: Minimal — thin red lines, subtle geometric touches
- Layout: Headline top-left, visual element center, detail text bottom
- Dimensions: 1080x1350
- Constraints: No photorealism, no clutter, professional, white/red palette

---

### Slide 1 (Cover)

**Headline:** "8 Threats From Giving AI Agents Shell Access"
**Key detail:** Subtitle — "I mapped them. Then I built a sandbox."
**Visual suggestion:** Abstract terminal window with a red warning accent
**Image prompt:** "Clean minimal slide, 1080x1350 portrait, white (#ffffff) background. Center: a stylized terminal window icon with thin dark gray (#24292f) strokes and a red (#dc2626) warning triangle overlaid. Top-left bold dark text: '8 Threats From Giving AI Agents Shell Access'. Bottom-left smaller gray (#656d76) text: 'I mapped them. Then I built a sandbox.' Red accent line (60x3px) above subtitle. Corner brackets in faint red. No photorealism, no clutter."

---

### Slide 2 (Core)

**Headline:** "AI coding agents have a terminal."
**Key detail:** They run commands, modify files, reach your network. Most developers don't think about what this means.
**Visual suggestion:** Terminal icon connected to three risk icons — files, commands, network
**Image prompt:** "Clean minimal slide, 1080x1350 portrait, white (#ffffff) background. Center: flat terminal window icon in dark gray (#24292f) with three thin lines branching out to three icons — a file folder, a command prompt arrow, and a network globe. Lines and icons in dark gray with red (#dc2626) accent dots at connection points. Top-left bold dark text: 'AI coding agents have a terminal.' Bottom area smaller gray text: 'They run commands, modify files, and reach your network.' Matching carousel series style."

---

### Slide 3 (Core)

**Headline:** "Threat: Data exfiltration"
**Key detail:** An agent with network access can send your code anywhere. Obvious or subtle. You probably wouldn't notice.
**Visual suggestion:** Simple diagram of agent -> network -> external server
**Image prompt:** "Clean minimal slide, 1080x1350 portrait, white (#ffffff) background. Center: flat diagram showing a laptop icon with an AI agent symbol, an arrow pointing right through a network cloud to an external server icon. Arrow in dark gray (#24292f), server icon accented with red (#dc2626) border. Diagram sits on a light gray (#f6f8fa) card with subtle border. Top-left bold dark text: 'Data Exfiltration.' Bottom smaller gray text: 'An agent with network access can send your code anywhere.' Consistent style with series."

---

### Slide 4 (Core)

**Headline:** "Threat: File system escape"
**Key detail:** Agents wander outside project directories. If compromised, that wandering becomes dangerous.
**Visual suggestion:** Directory tree showing access boundary being crossed
**Image prompt:** "Clean minimal slide, 1080x1350 portrait, white (#ffffff) background. Center: flat directory tree diagram with folders in dark gray (#24292f), a dashed horizontal red (#dc2626) line representing a boundary, and one folder path crossing below the line highlighted with a red background tint. Top-left bold dark text: 'File System Escape.' Bottom smaller gray text: 'Agents wander outside project directories. If compromised, that wandering becomes dangerous.' Consistent series style."

---

### Slide 5 (Core)

**Headline:** "Threat: Compromised tools"
**Key detail:** Even if the agent is trustworthy, the MCP servers and skills it loads might not be. First real MCP supply chain attack already happened.
**Visual suggestion:** Supply chain diagram with a poisoned link
**Image prompt:** "Clean minimal slide, 1080x1350 portrait, white (#ffffff) background. Center: flat chain of three connected nodes — 'Agent', 'MCP Server', 'Action' — with the middle node highlighted red (#dc2626) border and a small warning icon. Other nodes in light gray (#f6f8fa) cards with gray (#d0d7de) borders. Connections as thin dark lines. Top-left bold dark text: 'Compromised Tools.' Bottom smaller gray text: 'The first real MCP supply chain attack already happened.' Consistent series style."

---

### Slide 6 (Core)

**Headline:** "Threat: Lateral network access"
**Key detail:** An agent on your network is one curl away from infrastructure it has no business touching.
**Visual suggestion:** Network diagram with agent reaching internal services
**Image prompt:** "Clean minimal slide, 1080x1350 portrait, white (#ffffff) background. Center: flat network diagram — laptop with AI agent icon on left, multiple internal service nodes (database, API, server) on right on light gray (#f6f8fa) cards. Dark gray connection lines reaching across. One connection highlighted red (#dc2626). Top-left bold dark text: 'Lateral Network Access.' Bottom smaller gray text: 'One curl away from infrastructure it has no business touching.' Consistent series style."

---

### Slide 7 (Core)

**Headline:** "The fix: containerized isolation"
**Key detail:** Docker wrapper. Network lockdown. Per-project images. No host access.
**Visual suggestion:** Before/after showing open access vs contained agent
**Image prompt:** "Clean minimal slide, 1080x1350 portrait, white (#ffffff) background. Split layout — left side: AI agent icon with messy red (#dc2626) lines reaching everywhere, labeled 'Before'. Right side: same agent icon inside a clean dark gray (#24292f) container box with no lines escaping, labeled 'After'. Both on light gray (#f6f8fa) card backgrounds. Top-left bold dark text: 'Containerized Isolation.' Bottom smaller gray text: 'Docker wrapper. Network lockdown. Per-project images. No host access.' Consistent series style."

---

### Slide 8 (Closing)

**Headline:** "Full threat model at accidentalrebel.com"
**Key detail:** Juan Karlo Licudine / @accidentalrebel / Follow for AI security analysis
**Visual suggestion:** Clean close with name and blog URL
**Image prompt:** "Clean minimal slide, 1080x1350 portrait, white (#ffffff) background. Center: bold dark (#24292f) sans-serif text 'Full threat model and tool' with 'accidentalrebel.com' in red (#dc2626) below. Thin gray (#d0d7de) divider line. Bottom: 'Karlo Licudine — @accidentalrebel' in smaller gray (#656d76) text. Faint red watermark at opacity 0.03 behind text. Clean, professional. Consistent series style."
