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
**Supporting text:** I mapped them. Then I built a sandbox.
**Visual note:** Simple centered terminal icon with red warning accent — this is the one slide that uses a visual element.

---

### Slide 2 (Core)

**Headline:** "AI Agents Have a Terminal"
**Supporting text:** Most developers hand agents shell access and never think about what that means. Here's what they can reach:
**List items:**
- Run arbitrary shell commands
- Read and modify any file on the host
- Make network requests to internal infrastructure
**Concluding line:** And most setups have zero isolation.

---

### Slide 3 (Core)

**Headline:** "Data Exfiltration"
**Supporting text:** An agent with network access can send your code anywhere. Obvious or subtle — you probably wouldn't notice.
**List items:**
- Source code, credentials, API keys — all reachable
- One curl to an external endpoint is all it takes
- Prompt injection can trigger this without user intent
**Concluding line:** If an agent can read files and reach the network, exfiltration is trivial.

---

### Slide 4 (Core)

**Headline:** "File System Escape"
**Supporting text:** Agents wander outside project directories. If compromised, that wandering becomes dangerous.
**List items:**
- SSH keys, cloud credentials, browser data
- Other projects on the same machine
- System configuration files
**Concluding line:** No boundary between "project scope" and "everything else."

---

### Slide 5 (Core)

**Headline:** "Compromised Tools"
**Supporting text:** Even if the agent is trustworthy, the MCP servers and skills it loads might not be.
**List items:**
- The first real MCP supply chain attack already happened
- Skills run with the agent's full permissions
- No signature verification, no sandboxing by default
**Concluding line:** Your agent is only as secure as its least-trusted plugin.

---

### Slide 6 (Core)

**Headline:** "Lateral Network Access"
**Supporting text:** An agent on your network is one curl away from infrastructure it has no business touching.
**List items:**
- Internal APIs, databases, admin panels
- Cloud metadata endpoints (169.254.169.254)
- Other machines on the same subnet
**Concluding line:** Network access without segmentation is an open door.

---

### Slide 7 (Core)

**Headline:** "The Fix: Containerized Isolation"
**Supporting text:** After mapping the threats, I built a sandbox. It adds friction. It's worth it.
**List items:**
- Docker wrapper with no host filesystem access
- Network lockdown — allowlist only
- Per-project images — no cross-contamination
- Disposable environments — rebuild, don't patch
**Concluding line:** Contain the agent. Assume it will be compromised.

---

### Slide 8 (Closing)

**Headline:** "Full threat model at accidentalrebel.com"
**Supporting text:** Juan Karlo Licudine / @accidentalrebel
**Visual note:** Clean close — centered text, red URL, author name. No list.
