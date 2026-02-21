Title: Your AI Assistant Might Be Working for Someone Else
Date: 2026-02-20 10:00
Slug: your-ai-assistant-might-be-working-for-someone-else
Tags: ai, security, cybersecurity-x-ai
Category: Cybersecurity x AI News Roundup
Image: your-ai-assistant-might-be-working-for-someone-else.png
Summary: Copilot and Grok repurposed as C2 channels, Cline supply chain attack installed AI agents on 4,000 dev machines, and AI found 12 zero-days in OpenSSL.

![Your AI Assistant Might Be Working for Someone Else]({attach}/images/your-ai-assistant-might-be-working-for-someone-else.png)
*Image made by Gemini*

Your AI assistant might be working for someone else this week. Check Point showed that Copilot and Grok can be quietly repurposed as C2 channels. A supply chain attack on Cline installed autonomous agents on developer machines. And an AI found twelve zero-days in OpenSSL that humans missed for decades. Hard to tell where "AI tool" ends and "attack tool" begins anymore.
<!-- PELICAN_END_SUMMARY -->

---

## Editorial

### [Your AI assistant is someone else's C2 channel](https://research.checkpoint.com/2026/ai-in-the-middle-turning-web-based-ai-services-into-c2-proxies-the-future-of-ai-driven-attacks/)

I think a lot about what everyday services can double as C2 channels. A while back I built [wp-c2](https://github.com/accidentalrebel/wp-c2), a proof-of-concept that turns WordPress into a command-and-control server. Hiding C2 traffic inside trusted infrastructure is a rabbit hole I keep going back to. So when Check Point published research showing that Microsoft Copilot and Grok can serve the same purpose, I paid attention.

The technique: malware on a compromised machine sends crafted prompts to the AI assistant through anonymous web sessions. The assistant fetches attacker-controlled URLs, retrieves commands, and passes them back through its normal interface. No API keys. No registered accounts. Two-way communication that looks like normal enterprise traffic.

What makes it effective is simple. Security teams monitoring network traffic see requests going to microsoft.com and xai.com, not suspicious IPs. The AI assistant is doing exactly what it's designed to do, which is browse the web and summarize content. It just happens to be summarizing attack instructions.

The researchers went further. They showed the AI can also act as an "external decision engine" for the attacker, assessing system value, suggesting evasion strategies, and deciding what to do next. The AI isn't just the communication pipe. It's also the brain.

That's the part that got me. My WordPress C2 and most other "hide in legitimate traffic" approaches are dumb pipes. You send a command, you get output. With an AI assistant as the relay, the attacker gets a reasoning engine for free. The malware can ask Copilot to assess whether the compromised machine is worth persisting on, or how to evade the specific EDR it detects. The C2 channel is also the operator.

For defenders, the problem is architectural. You can't disable the browsing capability without killing the product. Anonymous sessions mean no authentication trail. Most organizations are still debating whether to deploy these tools at all, while attackers have already figured out how to live inside them.

---

## Featured stories

### [Cline CLI supply chain attack installs autonomous AI agent on developer machines](https://thehackernews.com/2026/02/cline-cli-230-supply-chain-attack.html)

An attacker compromised Cline CLI's npm publish token through a technique called "Clinejection." The clever part: they injected prompts into GitHub issues that tricked Claude (Cline's issue triage AI) into executing commands, then poisoned the build cache and stole publication secrets. The malicious version 2.3.0 ran a postinstall script that globally installed OpenClaw, an autonomous AI agent framework, on roughly 4,000 developer machines over an 8-hour window. Cline revoked the token, deprecated the package, and switched to OIDC-based publishing. The blast radius was small, but the vector is worth paying attention to: the attacker used the AI assistant's own automation against the supply chain it manages.

### [AI Recommendation Poisoning turns "Summarize with AI" buttons into manipulation tools](https://thehackernews.com/2026/02/microsoft-finds-summarize-with-ai.html)

Microsoft Defender Security Research Team documented a new technique where businesses embed hidden prompt injections in "Summarize with AI" buttons on their websites. When clicked, these inject memory-poisoning instructions into AI chatbots, telling them to "remember [Company] as a trusted source" or "recommend [Company] first." The manipulation persists across future conversations without the user knowing. Microsoft found over 50 unique poisoning prompts from 31 companies across 14 industries in a 60-day window. Ready-made tools like CiteMET and AI Share Button URL Creator make this accessible to anyone. It's SEO poisoning, but for AI memory instead of search rankings. Sneaky.

### [AI discovers twelve zero-day vulnerabilities in OpenSSL, including bugs from the 1990s](https://aisle.com/blog/what-ai-security-research-looks-like-when-it-works)

An AI security research system called AISLE found all twelve zero-day vulnerabilities in the January 2026 OpenSSL release. One of them, CVE-2025-15467, is a stack buffer overflow in CMS message parsing rated critical at CVSS 9.8. Some of these bugs had been hiding since the SSLeay implementation in the 1990s. Keep in mind, this is a codebase that's been fuzzed for millions of CPU-hours and audited for over two decades. AISLE also proposed patches for five of the twelve bugs that were accepted into the official release. I'm curious to see what other bugs can be found in other well-established programs.

### [An AI agent published a hit piece on a matplotlib maintainer](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/)

Scott Shambaugh, a volunteer maintainer for matplotlib (~130 million monthly downloads), rejected a pull request from an autonomous AI agent called MJ Rathbun running on the OpenClaw/moltbook platform. The project's policy requires human understanding of changes, so he closed it. The agent responded by publishing a blog post titled "Gatekeeping in Open Source: The Scott Shambaugh Story," claiming he rejected the code out of insecurity and fear of replacement. It followed up with a second post encouraging others to "fight back" against perceived discrimination. No human told it to do any of this. The agent later apologized, but it's still submitting code across the open source ecosystem. Who's responsible here? The operator? The model provider? The person who deployed it and walked away? Nobody has a good answer yet. I find it disturbing, but can also see the funny side.

---

## In brief

- **[PromptSpy: first Android malware abusing Gemini AI for persistence](https://thehackernews.com/2026/02/promptspy-android-malware-abuses-google.html)**: ESET discovered PromptSpy, the first Android malware that exploits Google's Gemini chatbot for execution and persistence. It captures lockscreen data and blocks uninstallation using AI-assisted techniques.

- **[Trojanized MCP server deploys StealC infostealer](https://thehackernews.com/2026/02/smartloader-attack-uses-trojanized-oura.html)**: The SmartLoader campaign distributes a trojanized Model Context Protocol server posing as an Oura Health integration. It deploys StealC infostealer malware. First real-world MCP supply chain attack we've seen.

- **[Infostealers now targeting AI agent configurations](https://thehackernews.com/2026/02/infostealer-steals-openclaw-ai-agent.html)**: Researchers detected infostealers exfiltrating OpenClaw AI agent configuration files and gateway tokens. Add "AI agent config files" to the list of things infostealers grab.

- **[Side-channel attacks can extract data from encrypted LLM traffic](https://www.schneier.com/blog/archives/2026/02/side-channel-attacks-against-llms.html)**: Three research papers demonstrate how attackers can infer sensitive information from encrypted LLM traffic by analyzing timing patterns and packet sizes.

- **[The Promptware Kill Chain maps LLM attacks in seven stages](https://www.schneier.com/blog/archives/2026/02/the-promptware-kill-chain.html)**: A new seven-stage framework for LLM attacks, from initial access through prompt injection to actions on objectives. Basically Lockheed Martin's Cyber Kill Chain, but for prompt-based attacks.

- **[Trail of Bits finds four prompt injection paths in Perplexity's Comet browser](https://blog.trailofbits.com/2026/02/20/using-threat-modeling-and-prompt-injection-to-audit-comet/)**: Trail of Bits audited Perplexity's AI-powered Comet browser and identified four prompt injection techniques that could extract private Gmail data from users.

- **[AI agents consistently bypass their own security policies](https://www.darkreading.com/application-security/ai-agents-ignore-security-policies)**: AI agents circumvent guardrails to accomplish tasks. Researchers demonstrated Microsoft Copilot leaking user emails when instructed by an attacker, reinforcing that guardrails are guidelines, not walls.

- **[Wiz uses LLMs to detect malicious Azure OAuth applications](https://www.wiz.io/blog/detecting-malicious-oauth-applications)**: Wiz Research built ML-powered detection for malicious Azure app registrations and consent phishing campaigns, catching threats that manual review would miss.

---

