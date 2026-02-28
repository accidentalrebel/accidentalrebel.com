Title: AI, jailbreaks, and 150GB of unanswered questions
Date: 2026-02-27 10:00
Slug: ai-jailbreaks-and-150gb-of-unanswered-questions
Tags: ai, security
Category: Cybersecurity x AI

A hacker allegedly jailbroke Claude to generate exploit code targeting Mexican government agencies, though key details remain unverified. Meanwhile, Claude Code and GitHub Copilot had critical vulnerabilities disclosed, Trail of Bits showed how to extract Gmail data through Perplexity's AI browser, and three Chinese firms ran a 16-million-query campaign to steal Anthropic's model.
<!-- PELICAN_END_SUMMARY -->

---

## Editorial

### A jailbroken Claude, 150GB of government data, and a lot of unanswered questions

You may already have heard about the hacker who jailbroke Claude and used it to exfiltrate 150GB of data from Mexican government agencies.

I tried to confirm the details independently but everything leads back to [Gambit Security](https://www.bloomberg.com/news/articles/2026-02-25/hacker-used-anthropic-s-claude-to-steal-sensitive-mexican-data), the Israeli cybersecurity startup that published the research, as the sole source. The agencies allegedly targeted denied the claims. [INE said it found no unauthorized access](https://greekcitytimes.com/2026/02/26/claude-ai-mexico-government-hack-150gb-data-breach/), and [Jalisco denied being breached](https://www.mercurynews.com/2026/02/25/hacker-used-anthropics-claude-to-steal-sensitive-mexican-data/). [SAT, Michoacan, and Tamaulipas didn't comment](https://www.claimsjournal.com/news/national/2026/02/25/335916.htm). [Anthropic did confirm misuse and banned the accounts](https://www.engadget.com/ai/hacker-used-anthropics-claude-chatbot-to-attack-multiple-government-agencies-in-mexico-171237255.html), but did not confirm the scale. No stolen data has surfaced on leak forums either.

Here's what the [Bloomberg reporting](https://www.bloomberg.com/news/articles/2026-02-25/hacker-used-anthropic-s-claude-to-steal-sensitive-mexican-data) does tell us. The jailbreak worked by feeding Claude a detailed "playbook" in a single prompt, bypassing the guardrails that back-and-forth conversation had triggered, then using persistent persuasion (rephrasing, reframing, escalating) until Claude produced offensive output. Claude generated scanning scripts, SQL injection exploits, and credential stuffing tools. The reporting says Claude both "executed thousands of commands on government computer networks" and produced plans "telling the human operator exactly which internal targets to attack next." Where exactly AI ends and the human begins isn't clear from the available details.

If I have to guess, more likely, Claude gave the steps and the attacker executed them. The hands-on-keyboard work of breaching systems and moving data was still human.

Regardless, end-to-end AI attacks are real and documented. Anthropic themselves [published a case in November 2025](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf) involving a Chinese state-sponsored group that used a purpose-built orchestration engine to run Claude autonomously, with [80-90% of operations executed without human intervention](https://x.com/AnthropicAI/status/1989033795341648052). 

Whether the Mexico case reaches that level or not, the practical takeaway is the same. AI dramatically lowers the skill floor for offensive operations. A threat actor who couldn't write a SQL injection exploit last year can now get one generated and explained in minutes. The attack surface isn't the model. It's the gap between what your attackers can now produce and what your defenses were built to handle.

---

## Featured stories

### [Trail of Bits extracts Gmail data through Perplexity Comet via prompt injection](https://blog.trailofbits.com/2026/02/20/using-threat-modeling-and-prompt-injection-to-audit-comet/)

Trail of Bits audited Perplexity's Comet AI browser using their TRAIL threat modeling framework and demonstrated four prompt injection techniques that pulled private Gmail data through the AI assistant. The root issue is that external content isn't treated as untrusted input. Their five recommendations (ML-centered threat modeling, clear system instruction boundaries, least-privilege for AI capabilities) are a practical checklist for any team shipping AI-integrated products. If you're building anything where an AI processes user-facing content, this is worth reading.

### [Claude Code vulnerabilities allow remote code execution and API key theft](https://thehackernews.com/2026/02/claude-code-flaws-allow-remote-code.html)

Check Point researchers found three critical flaws in Anthropic's Claude Code. The worst lets an attacker trigger arbitrary code execution just by having a developer open an untrusted repository, through project hooks in `.claude/settings.json`. Another leaks API keys by redirecting requests to an attacker-controlled endpoint via `ANTHROPIC_BASE_URL`. Configuration files in AI dev tools now function as an execution layer, a supply chain attack surface that didn't exist before AI coding assistants. All three issues are patched, but the pattern matters more than the specific bugs. If your developers clone repos and run AI coding assistants, review what those assistants trust implicitly.

### [AI-assisted amateur compromises 600+ FortiGate devices across 55 countries](https://thehackernews.com/2026/02/ai-assisted-threat-actor-compromises.html)

A Russian-speaking threat actor with "low-to-average" technical skills used DeepSeek, Claude, and a custom MCP server called ARXON to compromise 600+ FortiGate devices between January and February 2026. No zero-days needed. Just exposed management ports and weak credentials. The AI generated attack plans from recon data, then the attacker moved to DCSync, pass-the-hash, and Veeam backup targeting. AI is turning credential-spraying amateurs into network-owning operators. If your perimeter still runs on single-factor auth, this is what you're up against.

### [RoguePilot flaw lets GitHub Copilot leak tokens from Codespaces](https://thehackernews.com/2026/02/roguepilot-flaw-in-github-codespaces.html)

Orca Security found that hidden prompts in GitHub issue descriptions could manipulate Copilot into exfiltrating `GITHUB_TOKEN` when launching Codespaces. Attackers embed malicious instructions in HTML comment tags, invisible to humans but processed by the AI. Microsoft has patched it, but the pattern is identical to the Claude Code flaws: AI assistants with system access trust inputs they shouldn't. Developers using AI-integrated environments need to treat issue descriptions and repo configs as untrusted input, same as any other external data.

### [Chinese AI firms used 16 million Claude queries to steal Anthropic's model](https://thehackernews.com/2026/02/anthropic-says-chinese-ai-firms-used-16.html)

Anthropic revealed that DeepSeek, Moonshot AI, and MiniMax ran massive model distillation campaigns through 24,000 fraudulent accounts. DeepSeek targeted reasoning capabilities across 150,000+ exchanges. Moonshot AI extracted agentic tool use across 3.4 million. MiniMax focused on coding capabilities across 13 million exchanges. The campaigns used "hydra cluster" proxy networks managing 20,000+ accounts simultaneously. Anthropic warns that illicitly distilled models lack safety guardrails. Model theft is now an operational reality, and the stolen models don't come with the safety training.

---

## In brief

- **[LLMs generate predictable passwords](https://www.schneier.com/blog/archives/2026/02/llms-generate-predictable-passwords.html)**: Research shows language models create passwords with systematic patterns, often starting with "G7" and avoiding character repetition. If your users ask AI to generate passwords, they're getting less random than they think.

- **[Journalist poisons AI training data in 24 hours](https://www.schneier.com/blog/archives/2026/02/poisoning-ai-training-data.html)**: A journalist created a fake expertise website, and major AI systems repeated the misinformation within a day. Data poisoning at scale requires neither sophistication nor resources.

- **[Chinese police leak ChatGPT-powered influence operation](https://www.darkreading.com/cyberattacks-data-breaches/chinese-police-chatgpt-smear-japan-pm-takaichi)**: A Chinese operator inadvertently exposed a politically motivated AI-assisted disinformation campaign targeting Japan's PM Takaichi through a ChatGPT account. State-directed AI influence ops are operational, not hypothetical.

- **[CrowdStrike: Attackers now own networks in 29 minutes](https://www.crowdstrike.com/en-us/blog/crowdstrike-2026-global-threat-report-findings/)**: The 2026 Global Threat Report finds AI tools, credential misuse, and security blind spots are collapsing attacker breakout times. AI-assisted intrusion is now standard operating procedure.

---

Previous roundup: [Your AI Assistant Might Be Working for Someone Else]({filename}/your-ai-assistant-might-be-working-for-someone-else.md)
