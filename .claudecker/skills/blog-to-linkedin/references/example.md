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

- Background: #0D1117 (near-black)
- Accent color: #58A6FF (electric blue)
- Warning color: #F85149 (red)
- Style: Dark tech aesthetic, flat minimal iconography
- Typography: Clean sans-serif, bold headlines top-left, detail text bottom
- Motif: Subtle circuit-board / node-graph pattern in background
- Layout: Headline top-left, visual element center, detail text bottom
- Dimensions: 1080x1080
- Constraints: No photorealism, no clutter, professional

---

### Slide 1 (Cover)

**Headline:** "8 Threats From Giving AI Agents Shell Access"
**Key detail:** Subtitle — "I mapped them. Then I built a sandbox."
**Visual suggestion:** Abstract terminal window with a threat warning
**Image prompt:** "Minimal dark tech slide, 1080x1080, background #0D1117 with subtle circuit-board pattern. Center: a stylized terminal window icon with a glowing electric blue (#58A6FF) warning triangle overlaid. Top-left bold white sans-serif text: '8 Threats From Giving AI Agents Shell Access'. Bottom-left smaller white text: 'I mapped them. Then I built a sandbox.' Clean, professional, no photorealism. No clutter."

---

### Slide 2 (Core)

**Headline:** "AI coding agents have a terminal."
**Key detail:** They run commands, modify files, reach your network. Most developers don't think about what this means.
**Visual suggestion:** Terminal icon connected to three risk icons — files, commands, network
**Image prompt:** "Minimal dark tech slide, 1080x1080, background #0D1117 with subtle circuit pattern. Center: flat icon of a terminal window with three electric blue (#58A6FF) lines branching out to three icons — a file folder, a command prompt arrow, and a network globe. Top-left bold white sans-serif text: 'AI coding agents have a terminal.' Bottom area smaller white text: 'They run commands, modify files, and reach your network.' Clean, professional layout matching carousel series."

---

### Slide 3 (Core)

**Headline:** "Threat: Data exfiltration"
**Key detail:** An agent with network access can send your code anywhere. Obvious or subtle. You probably wouldn't notice.
**Visual suggestion:** Simple diagram of agent -> network -> external server
**Image prompt:** "Minimal dark tech slide, 1080x1080, background #0D1117. Center: flat diagram showing a laptop icon with an AI agent symbol, an arrow pointing right through a network cloud to a red-tinted external server icon. Arrow in electric blue (#58A6FF), server icon tinted warning red (#F85149). Top-left bold white sans-serif text: 'Data Exfiltration.' Bottom smaller white text: 'An agent with network access can send your code anywhere.' Consistent style with series."

---

### Slide 4 (Core)

**Headline:** "Threat: File system escape"
**Key detail:** Agents wander outside project directories. If compromised, that wandering becomes dangerous.
**Visual suggestion:** Directory tree showing access boundary being crossed
**Image prompt:** "Minimal dark tech slide, 1080x1080, background #0D1117. Center: flat directory tree diagram with folders in electric blue (#58A6FF), a dashed horizontal line representing a boundary, and one folder path crossing below the line tinted warning red (#F85149). Top-left bold white sans-serif text: 'File System Escape.' Bottom smaller white text: 'Agents wander outside project directories. If compromised, that wandering becomes dangerous.' Consistent series style."

---

### Slide 5 (Core)

**Headline:** "Threat: Compromised tools"
**Key detail:** Even if the agent is trustworthy, the MCP servers and skills it loads might not be. First real MCP supply chain attack already happened.
**Visual suggestion:** Supply chain diagram with a poisoned link
**Image prompt:** "Minimal dark tech slide, 1080x1080, background #0D1117. Center: flat chain of three connected nodes — 'Agent', 'MCP Server', 'Action' — with the middle node tinted warning red (#F85149) and a small poison/skull icon. Connections in electric blue (#58A6FF). Top-left bold white sans-serif text: 'Compromised Tools.' Bottom smaller white text: 'The first real MCP supply chain attack already happened.' Consistent series style."

---

### Slide 6 (Core)

**Headline:** "Threat: Lateral network access"
**Key detail:** An agent on your network is one curl away from infrastructure it has no business touching.
**Visual suggestion:** Network diagram with agent reaching internal services
**Image prompt:** "Minimal dark tech slide, 1080x1080, background #0D1117. Center: flat network diagram — laptop with AI agent icon on left, multiple internal service nodes (database, API, server) on right, with electric blue (#58A6FF) connection lines reaching across. One connection highlighted warning red (#F85149). Top-left bold white text: 'Lateral Network Access.' Bottom smaller white text: 'One curl away from infrastructure it has no business touching.' Consistent series style."

---

### Slide 7 (Core)

**Headline:** "The fix: containerized isolation"
**Key detail:** Docker wrapper. Network lockdown. Per-project images. No host access.
**Visual suggestion:** Before/after showing open access vs contained agent
**Image prompt:** "Minimal dark tech slide, 1080x1080, background #0D1117. Split layout — left side: AI agent icon with messy red (#F85149) lines reaching everywhere, labeled 'Before'. Right side: same agent icon inside a clean electric blue (#58A6FF) container box with no lines escaping, labeled 'After'. Top-left bold white text: 'Containerized Isolation.' Bottom smaller white text: 'Docker wrapper. Network lockdown. Per-project images. No host access.' Consistent series style."

---

### Slide 8 (Closing)

**Headline:** "Full threat model at accidentalrebel.com"
**Key detail:** Karlo Licudine / @accidentalrebel / Follow for AI security analysis
**Visual suggestion:** Clean close with name and blog URL
**Image prompt:** "Minimal dark tech slide, 1080x1080, background #0D1117. Center: bold white sans-serif text 'Full threat model and tool' with 'accidentalrebel.com' in electric blue (#58A6FF) below. Bottom: 'Karlo Licudine - @accidentalrebel' in smaller white text. Subtle circuit-board motif in background. Clean, professional. Consistent series style."
