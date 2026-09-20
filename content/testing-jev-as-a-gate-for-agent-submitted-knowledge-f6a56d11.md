Title: Testing Jev as a gate for agent-submitted knowledge
Date: 2026-09-20
Status: published
Slug: testing-jev-as-a-gate-for-agent-submitted-knowledge-f6a56d11

I got access to [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) and have been brainstorming cybersecurity projects to try it on. But I wanted to try it on something simple first, so I integrated it into a personal project: my existing knowledge vault for agents. In this integration, Jev evaluates proposed notes against review questions and returns probabilities that the application uses to decide what goes in.

The vault uses Obsidian as a backend and Khoj for retrieval. It stores information that agents can use in future tasks, including project facts, shared capabilities, decisions and their reasons, and verified lessons.

The tricky part is deciding what deserves to go in. Something that failed on one machine might be useful to remember, but that doesn't mean it should become a rule saying it always fails. An agent finding that note later needs to know the difference.

I've used calls to Claude or Codex to help determine what goes in. That has worked fine, but when I learned about Jev, it seemed like a good fit for my problem. I had to give it a try.

It's not exactly the best application for Jev (especially when you see the other crazy things people are doing with it), but this is the need that I currently have, and so I made it.

## What makes a note worth keeping?

![93dd4b6a 4465 4197 a5d2 a704d004890f fit]({attach}/images/dashboard/f6a56d11-2363-40a2-838c-6a844d86f653/b95411a4-2044-4c78-bf2f-ac5ce3ea70dc-93dd4b6a-4465-4197-a5d2-a704d004890f-fit.png)

The vault isn't meant to hold everything an agent did. Routine task summaries, generic advice, and paraphrases of existing entries don't belong there. Neither do unverified claims or secrets. Repositories still hold the authoritative code, commands, configuration, and current status. A note can point to those and explain a lasting constraint without copying the runbook into another place.

I wanted something like Wikipedia for my agents.

The integration breaks the review into four questions. These are paraphrases, rather than the exact prompts:

| Dimension               | What we're asking                                   |
| ----------------------- | --------------------------------------------------- |
| `factual_support`       | Does the evidence support what the note says?       |
| `durability`            | Will this remain useful beyond the current task?    |
| `reference_value`       | Would a future agent have a reason to consult it?   |
| `sensitive_information` | Would disclosing this expose sensitive information? |

All four go into one request with the proposed note and its evidence. For each question, Jev returns probabilities over five rubric levels, numbered 0 through 4. The application uses those probabilities to decide what happens next.

For factual support, for example, approval requires both `P(4) ≥ 0.25` and `P(3-4) ≥ 0.85`. That second expression means adding the probabilities for levels 3 and 4. The application checks those values directly instead of turning the distribution into an average score.

One submission described transcription output exceeding a media worker's log buffer. According to the implementation agent's account, it came with supporting documentation, cleared all four checks, and was published. Quick and easy.

But there was another note that landed just below the factual-support cutoff: 0.840 against a required 0.85. The implementation agent reran the same packet five times, and every rerun cleared that check. So the same note could pass or fail that check without its contents changing.

## So what about speed and cost?

According to the measurements, Jev answered all four review questions in roughly 1.1–1.2 seconds. One request used 2,944 input tokens and returned 63 output tokens.

The agent also reported 17 seconds for the editorial LLM to review and draft one candidate, and around 42 seconds for two. Those timings cover broader work than Jev's four judgments, so they aren't a direct speed comparison. In the workflow the agent described, the editorial LLM still runs, and Jev takes over the manual approval step.

![jev 2026 09 20 11 06]({attach}/images/dashboard/f6a56d11-2363-40a2-838c-6a844d86f653/b6affa18-788e-45db-9f98-fe7704607120-jev-2026-09-20_11-06.png)

As for cost, I've used 598K tokens over two days of running this, with reported spend of around $0.0243. Very cheap! I don't yet have a comparable cost breakdown for the previous workflow, though, so this isn't a measured savings figure.

## What comes next

My small experiment with Jev has given me useful data, and I'm now thinking of other areas to apply it to. I'm thinking along the lines of SOC work, log analysis, and possibly malware analysis. Something that puts its speed and cost to the test.

I'm excited to see where this goes.

You can see the implementation of Jev here: [Knowledge Vault Public](https://github.com/accidentalrebel/knowledge-vault-public).
