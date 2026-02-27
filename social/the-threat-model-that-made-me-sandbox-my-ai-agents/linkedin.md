# LinkedIn: The threat model that made me sandbox my AI agents

> Source: `content/the-threat-model-that-made-me-sandbox-my-ai-agents.md`

## Text Post

```
I gave an AI coding agent a terminal and then mapped what could go wrong.

8 threats. Not theoretical — based on real incidents and patterns I see running these tools daily. Data exfiltration, credential theft, lateral network movement, supply chain attacks through compromised MCP servers, cross-project contamination.

The part that surprised me: most of the risk isn't from the AI being malicious. It's from the environment being wide open. Your agent can read your SSH keys, reach internal APIs, and install packages autonomously. One compromised dependency executes with your permissions. One prompt injection and your source code is one curl away from an attacker's server.

After mapping the threats, I built a containerized sandbox — Docker wrapper with network lockdown, per-project isolation, and ephemeral sessions. It adds friction. It's worth it.

But you don't need my tool. Four things you can do today: audit your agent's permission settings, enable the built-in sandbox, run agents in containers, and review what MCP servers and skills you've installed. None require building anything.

Full threat model at accidentalrebel.com

#AISecurity #ThreatModeling #AgentSecurity #DevSecOps #LLMSecurity
```

## Carousel Plan

### Visual Identity

```
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
```

---

### Slide 1 (Cover)

**Headline:** 8 Threats From AI Agents With Shell Access
**Supporting text:** I mapped them. Then I built a sandbox.
**Visual note:** Simple centered terminal icon with red warning triangle — cover slide visual.

---

### Slide 2 (Core)

**Headline:** Your Agent Has a Terminal
**Supporting text:** Most developers hand agents shell access and never think about what that means.
**List items:**
- Runs arbitrary shell commands on your machine
- Reads and modifies any file your user account can reach
- Makes network requests to internal infrastructure
**Concluding line:** Most setups have zero isolation between the agent and your host.

---

### Slide 3 (Core)

**Headline:** What Can Go Wrong
**Supporting text:** Four threats from giving an agent access to your files and network.
**List items:**
- Host filesystem escape — reads SSH keys, cloud creds, other projects
- Data exfiltration — one curl sends your source code to an external endpoint
- Supply chain injection — compromised packages execute with your permissions
- Credential theft — infostealers already target AI agent config files and tokens
**Concluding line:** Stolen cloud credentials are how $50K AWS bills happen overnight.

---

### Slide 4 (Core)

**Headline:** It Gets Worse
**Supporting text:** Four more threats from the environment around the agent.
**List items:**
- Lateral movement — one curl to internal APIs, databases, admin panels
- Settings persistence — compromised session alters agent config permanently
- Privilege escalation — one careless sudo approval and the agent has root
- Cross-project contamination — client secrets leak into personal sessions
**Concluding line:** Most of these happen without the agent being malicious.

---

### Slide 5 (Core)

**Headline:** The Fix: Container Isolation
**Supporting text:** After mapping the threats, I built a sandbox. It adds friction. It's worth it.
**List items:**
- Docker wrapper — only the project directory is mounted
- Network lockdown — domain allowlist, everything else dropped
- Ephemeral sessions — destroyed on exit, rebuilt on launch
- Per-project profiles — no cross-contamination
**Concluding line:** Contain the agent. Assume it will be compromised.

---

### Slide 6 (Core)

**Headline:** What You Can Do Today
**Supporting text:** You don't need my tool. Four things you can act on right now.
**List items:**
- Audit your settings.local.json — check what you've approved
- Enable the built-in sandbox (/sandbox in Claude Code)
- Run agents in Docker containers
- Review installed MCP servers and skills
**Concluding line:** None of these require building anything. They're just decisions.

---

### Slide 7 (Closing)

**Headline:** Full threat model at accidentalrebel.com
**Supporting text:** Juan Karlo Licudine / @accidentalrebel
**Visual note:** Clean close — centered text, red URL, author name. No list.
