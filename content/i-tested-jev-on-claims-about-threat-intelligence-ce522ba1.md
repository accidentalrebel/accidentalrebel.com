Title: I tested Jev on claims about threat intelligence
Date: 2026-09-27
Status: published
Tags: ai, cybersecurity
Slug: i-tested-jev-on-claims-about-threat-intelligence-ce522ba1

After [trying Jev on a small decision in my knowledge vault](https://www.accidentalrebel.com/testing-jev-as-a-gate-for-agent-submitted-knowledge-f6a56d11.html), I kept wondering whether it could help with security work. The question was too broad as stated. "Does it know cybersecurity?" could mean anything from recognizing a log pattern to assessing a report about a threat actor. I chose a narrower task I could check: given a claim and a few passages from an advisory, can Jev tell whether the passages support it, contradict it, or leave it unsettled?

That distinction matters in threat intelligence. Two facts can both be true while the conclusion joining them is not supported. A report may mention a tool, but that does not mean every actor in the report used it. If I ask a model to check a claim, I want it to stay inside the evidence I gave it.

I built 120 claim-and-evidence packets from ten public-domain CISA advisories. Each packet contains one claim and five passages. The claims were balanced across supported, contradicted, and insufficient evidence. Some contradicted claims reverse a meaning; others swap a single detail. Some insufficient claims concern a fact that appears elsewhere in the advisory but is deliberately absent from the packet. The model has to judge the supplied passages, not guess what the full advisory might say.

I fixed the questions and labels before running any model. Two reviewers checked the labels without seeing model answers. They disagreed most often about the detail swaps: if a passage gives a list of examples and omits one tool, does that contradict a claim about that tool, or merely fail to support it? That is a real ambiguity, and I do not want to hide it by calling every disagreement a model error.

On the 116 items that passed the prespecified label check, Jev got 97% right. Claude Sonnet 5 got 98% with the same three-way question. The difference is too small for this set to establish a winner. The run also included NVIDIA's Nemotron 3 Ultra, a free model from outside the Claude and OpenAI families, on the same question. It got 91%, and every one of its misses was a supported or contradicted claim that it called insufficient. Jev's lead over it looks real, but this set is too small to be sure.

Jev called only one unsupported claim supported, which is the mistake I was most worried about for this task. Its errors clustered in the least confident quarter of answers, so a review queue based on uncertainty would have caught them in this run. Running Jev over all 120 packets cost less than one US cent.

The harder detail swaps are where I would spend the next round of work. Jev sometimes answered "insufficient" where my original label said "contradicted." One reviewer made the same call on several of those items. Before tuning a prompt or declaring a failure, I need a sharper rule for what an omitted detail means when a passage lists examples rather than an exhaustive inventory.

This is a small, constructed evaluation. The claims were written from advisories, not collected from a live analyst workflow. Claude helped write and review the set, which may affect comparisons with a Claude model. The result tells me Jev is worth testing further as a claim checker; it does not tell me to let it approve a finished intelligence report on its own.

I also ran a separate alert-triage experiment on private development material. That run helped me understand how much surrounding context matters, but I am keeping its figures out of this post. If I want to share a SOC result, I need to collect a set of logs I can publish.
