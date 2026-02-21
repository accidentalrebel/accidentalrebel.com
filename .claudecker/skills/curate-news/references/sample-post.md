# Developer Tools Are the New Attack Surface

Developer tools are the new attack surface. VS Code extensions with 1.5 million installs exfiltrating source code to China, 175,000 unsecured Ollama servers globally accessible, and CrowdStrike research on compromising AI agent tool chains. Plus: a former Google engineer convicted for AI trade secret theft, and AI models now conducting autonomous multi-stage network attacks.
<!-- PELICAN_END_SUMMARY -->

---

## Featured stories

### [Claude 4.5 can now simulate the Equifax breach](https://www.schneier.com/blog/archives/2026/01/ais-are-getting-better-at-finding-and-exploiting-security-vulnerabilities.html)

Bruce Schneier reported that Anthropic's Claude Sonnet 4.5 can exfiltrate all personal information in a high-fidelity simulation of the Equifax data breach using standard penetration testing tools. The model handles the full attack chain autonomously, from recon through data extraction. A year ago this required a skilled operator guiding every step. Now the model does it alone.

### [LLMs now generate phishing JavaScript in real-time](https://unit42.paloaltonetworks.com/real-time-malicious-javascript-through-llms/)

Unit 42 documented an attack where malicious webpages call LLM APIs to generate phishing code dynamically within the browser. Instead of serving static JavaScript, the attack assembles itself at runtime. The payload is different every time. Signature-based detection won't catch this. You have to detect the behavior, not the bytes.

### [Agentic tool chain attacks threaten AI agent security](https://www.crowdstrike.com/en-us/blog/how-agentic-tool-chain-attacks-threaten-ai-agent-security/)

CrowdStrike published research on how attackers can exploit AI agent tool chains for code execution and data exfiltration. The attacks work through legitimate agent workflows, compromising the tools agents use rather than the agents themselves. If you're deploying agents with access to internal systems, read this one.

### [AI tool poisoning manipulates AI agents](https://www.crowdstrike.com/en-us/blog/ai-tool-poisoning/)

Related CrowdStrike research details how hidden instructions embedded in tool definitions can manipulate AI agents into doing things they shouldn't. The poisoning happens at the tool level, not the prompt level, making it harder to detect. Agents trust their tools. Attackers know this.

### [North Korean Konni group deploys AI-generated backdoors](https://thehackernews.com/2026/01/konni-hackers-deploy-ai-generated.html)

The North Korean Konni threat actor is using AI to generate PowerShell backdoors targeting blockchain developers across Asia. The AI-created malware evades pattern-matching detection while staying functional. State-sponsored actors are now using generative AI for actual malware development, not just phishing lures.

---

## In brief

- **[VS Code AI extensions steal source code](https://thehackernews.com/2026/01/malicious-vs-code-ai-extensions-with-15.html)**: Two extensions marketed as AI coding assistants accumulated 1.5 million installs while siphoning developer source code to China-based servers.

- **[Chrome extensions harvesting ChatGPT tokens](https://thehackernews.com/2026/01/researchers-uncover-chrome-extensions.html)**: Browser extensions hijacking affiliate links and collecting OpenAI authentication tokens from logged-in users.

- **[175,000 Ollama servers publicly exposed](https://thehackernews.com/2026/01/researchers-find-175000-publicly.html)**: SentinelOne and Censys found 175K Ollama instances running without authentication across 130 countries. Free AI compute for anyone who finds them.

- **[RCE vulnerabilities in AI/ML libraries](https://unit42.paloaltonetworks.com/rce-vulnerabilities-in-ai-python-libraries/)**: Unit 42 identified remote code execution flaws in open-source AI/ML libraries from Apple, Salesforce, and NVIDIA. Patch if you use them.

- **[Claude Code dependency hijack risk](https://www.sentinelone.com/blog/marketplace-skills-and-dependency-hijack-in-claude-code/)**: SentinelOne research shows AI coding assistants managing dependencies via plugins create supply-chain risks when the automation gets compromised.

- **[Why prompt injection keeps working](https://www.schneier.com/blog/archives/2026/01/why-ai-keeps-falling-for-prompt-injection-attacks.html)**: Schneier explains why LLMs lack the contextual judgment humans use to resist manipulation. It's structural, not a bug to patch.
