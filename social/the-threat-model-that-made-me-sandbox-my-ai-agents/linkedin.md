# LinkedIn Content: The Threat Model That Made Me Sandbox My AI Agents

Source: `content/the-threat-model-that-made-me-sandbox-my-ai-agents.md`

---

## Text Post

I mapped 8 threats that come with giving AI coding agents shell access. Then I built a sandbox to contain them.

When you launch Claude Code or Codex CLI, you're giving an LLM a terminal. It can run commands, modify files, and reach your network. Both tools have permission prompts -- but be honest, how often do you actually read the command before clicking "allow"?

I mapped the realistic attack surface: data exfiltration (an agent can curl your .env to any endpoint), credential theft (your ~/.ssh and ~/.aws are readable), supply chain injection (agents install packages autonomously), lateral movement (one curl to your internal API), and four more. These aren't theoretical. A supply chain attack on Cline CLI already compromised 4,000 installs through prompt injection against the tool's own AI triage.

After mapping the threats, I built a containerized sandbox -- Docker wrapper with iptables firewall, ephemeral sessions, SSH agent forwarding (keys never touch the container), and per-project volume isolation. But you don't need my tool. Four things you can do right now: audit your settings.local.json for broad permissions you forgot you approved, enable Claude Code's built-in /sandbox, run your agent in a basic Docker container, and review what MCP servers and skills your agent loads.

Full threat model with mitigations at accidentalrebel.com

#AISecurity #ThreatModeling #AgentSecurity #LLMSecurity #DevSecOps

---

## Carousel Plan

### Visual Identity

- Background: #0D1117 (near-black)
- Accent color: #58A6FF (electric blue)
- Warning color: #F85149 (red)
- Action color: #3FB950 (green, for the actionable steps)
- Style: Dark tech aesthetic, flat minimal iconography
- Typography: Clean sans-serif, bold headlines top-left, detail text bottom
- Motif: Terminal/shield motif
- Layout: Headline top-left, visual element center, detail text bottom
- Dimensions: 1080x1080
- Constraints: No photorealism, no clutter, professional

---

### Slide 1 (Cover)

**Headline:** "4 Things You Can Do Today to Secure Your AI Agent"
**Key detail:** Subtitle -- "No custom tooling required."
**Visual suggestion:** Shield icon with a checklist overlay

---

### Slide 2 (Core — Threats 1-4)

**Headline:** "8 Threats From Shell Access"
**Key detail:** T1 Host filesystem access — reads files outside project. T2 Data exfiltration — sends code/secrets to external endpoints. T3 Supply chain injection — compromised package executes on host. T4 Credential theft — reads SSH keys, API tokens, cloud creds.
**Visual suggestion:** Grid of 4 threat rows with threat IDs and short descriptions

---

### Slide 3 (Core — Threats 5-8)

**Headline:** "8 Threats (continued)"
**Key detail:** T5 Lateral movement — reaches internal network services. T6 Settings persistence — compromised session alters config permanently. T7 Privilege escalation — gains root or elevated capabilities. T8 Cross-project contamination — secrets from one project leak to another.
**Visual suggestion:** Grid of 4 threat rows continuing the pattern

---

### Slide 4 (Core — Action 1)

**Headline:** "Audit Your Permissions"
**Key detail:** Open .claude/settings.local.json. Look for Bash(sudo:*) or other broad patterns you approved and forgot about. Takes 5 minutes.
**Visual suggestion:** Code snippet showing settings file with a danger highlight on a broad pattern

---

### Slide 5 (Core — Action 2)

**Headline:** "Enable the Built-in Sandbox"
**Key detail:** Run /sandbox in a Claude Code session. It restricts file writes to the working directory and routes network through a domain-approving proxy. One command.
**Visual suggestion:** Terminal prompt showing the /sandbox command with a green checkmark

---

### Slide 6 (Core — Action 3)

**Headline:** "Run Your Agent in a Container"
**Key detail:** A basic Docker container with your project directory mounted gives you filesystem isolation, credential separation, and a throwaway environment. Covers 3 of 8 threats immediately.
**Visual suggestion:** Before/after -- open access vs contained agent in a Docker box

---

### Slide 7 (Core — Action 4)

**Headline:** "Review Your MCP Servers and Skills"
**Key detail:** Each one is third-party code running with agent permissions. Check what's installed, where it came from, and whether you still need it. If you rely on one, fork it.
**Visual suggestion:** List of loaded tools with a magnifying glass / audit icon

---

### Slide 8 (Closing)

**Headline:** "Full threat model at accidentalrebel.com"
**Key detail:** Karlo Licudine / @accidentalrebel
**Visual suggestion:** Clean close with URL and author
