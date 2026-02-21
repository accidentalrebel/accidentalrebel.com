Title: AI Agents Under Attack
Date: 2026-02-07 10:00
Slug: ai-agents-under-attack
Tags: ai, security, cybersecurity-x-ai
Category: Cybersecurity x AI News Roundup
Image: ai-agents-under-attack.webp
Summary: AI security roundup: Claude finds 500+ vulns in open-source libs, LLMs conduct autonomous network breaches, and AI agent attack surfaces keep expanding.

![AI Agents Under Attack]({attach}/images/ai-agents-under-attack.webp)
*Image made by Gemini*

AI agents are under attack this week—and AI is doing the attacking. Claude Opus 4.6 found 500+ vulnerabilities in major libraries. Language models can now run complete network breaches autonomously.
<!-- PELICAN_END_SUMMARY -->

---

## Featured stories

### [Claude Opus 4.6 discovers hundreds of security flaws](https://thehackernews.com/2026/02/claude-opus-discovers-security-flaws.html)

Anthropic's latest model identified more than 500 previously unknown high-severity vulnerabilities in major open-source projects like Ghostscript through automated security analysis. The model achieved 65.4% on Terminal-Bench 2.0 (highest ever recorded) and outperforms GPT-5.2 by ~144 ELO points on enterprise knowledge work tasks. Organizations relying on these libraries should monitor for patches.

### [AI models execute autonomous network attacks](https://www.schneier.com/blog/archives/2026/02/ai-models-execute-autonomous-network-attacks.html)

Language models can now independently conduct multi-stage network penetration testing, handling reconnaissance through data extraction while adapting to defensive measures. Bruce Schneier documented this capability shift, noting that sophisticated attacks previously demanded skilled human oversight—now they require only model access.

### [OpenClaw AI agent security risks](https://www.crowdstrike.com/en-us/blog/openclaw-ai-agent-security-risks/)

CrowdStrike analyzed OpenClaw's attack surface, examining autonomous agent deployments with tool access and persistent execution. The analysis covers architecture vulnerabilities, plugin security, and compromise vectors.

### [Agentic tool chain compromise threats](https://www.crowdstrike.com/en-us/blog/how-agentic-tool-chain-attacks-threaten-ai-agent-security/)

Research reveals how attackers exploit AI agent tool chains for code execution and data theft through legitimate workflows. The core insight: agents implicitly trust their tools, creating an exploitable attack surface.

---

## In brief

- **Malicious OpenClaw plugins**: A supply-chain attack delivered credential stealers disguised as functional plugins, exploiting ecosystem trust.

- **Ghidra MCP server**: A developer released 110 tools integrating Ghidra with AI assistants via Model Context Protocol, enabling AI-assisted binary analysis.
