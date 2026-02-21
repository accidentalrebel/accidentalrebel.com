---
name: curate-news
description: |
  Curates AI + cybersecurity news from RSS feeds for the AccidentalRebel blog.
  Fetches feeds, filters for AI+security intersection, then presents each
  candidate article one-by-one for the user to approve, reclassify, or skip.
  Generates a draft blog post from user-approved selections only.
  Use when the user wants to create a news roundup post or curate AI security news.
allowed-tools:
  - WebFetch
  - Read
  - Write
  - Skill
  - Glob
  - mcp__pal__consensus
---

# Cybersecurity x AI News Roundup

Generate a weekly news roundup blog post covering the intersection of AI and cybersecurity.

## Workflow

1. Fetch RSS feeds using WebFetch — **batch 5 at a time** to avoid parallel fetch errors (see "Fetching" below)
2. Fetch web sources (no RSS) using WebFetch and extract recent items
3. Filter articles (must match BOTH security AND AI keywords)
4. **Filter by age: discard any article older than 7 days from today's date**
5. Deduplicate by URL, then **trace to primary sources** (see "Source Tracing" below)
6. **PAL consensus** — use consensus to rank and suggest classifications (see "Article Selection" below)
7. **Interactive article review** — present each candidate one-by-one with consensus suggestions for user final approval
8. Generate draft from user-approved articles only, in **plain voice** (focus on accuracy)
9. Apply **/humanizer** to remove AI patterns
10. Apply **/accidentalrebel-voice** to add the final personality
11. Save draft to working directory (see "Output" below)
12. Tell the user to run `/new-post <draft-file>` to convert to Pelican format

---

## RSS Sources

Fetch ALL feeds and extract title, link, description, pubDate:

| Source | URL |
|--------|-----|
| Krebs on Security | `https://krebsonsecurity.com/feed/` |
| The Hacker News | `https://feeds.feedburner.com/TheHackersNews` |
| Bleeping Computer | `https://www.bleepingcomputer.com/feed/` |
| Schneier on Security | `https://www.schneier.com/feed/atom/` |
| Superhuman.ai | `https://www.superhuman.ai/feed` |
| HN AI+Security | `https://hnrss.org/newest?q=AI+security&points=50` |
| SentinelOne | `https://www.sentinelone.com/feed/` |
| Unit 42 | `http://feeds.feedburner.com/Unit42` |
| CrowdStrike | `https://www.crowdstrike.com/blog/feed/` |
| NIST Cybersecurity | `https://www.nist.gov/blogs/cybersecurity-insights/rss.xml` |
| Simon Willison | `https://simonwillison.net/atom/everything/` |
| LangChain Blog | `https://blog.langchain.com/rss` |
| HN MCP/Agents | `https://hnrss.org/newest?q=MCP+OR+%22model+context+protocol%22&points=30` |
| Lilian Weng | `https://lilianweng.github.io/index.xml` |
| AI Brews | `https://aibrews.substack.com/feed` |
| Dark Reading | `https://www.darkreading.com/rss.xml` |
| Trail of Bits | `https://blog.trailofbits.com/feed/` |
| Daniel Miessler | `https://danielmiessler.com/feed` |
| Wiz | `https://www.wiz.io/blog/rss` |
| Google Security Blog | `http://feeds.feedburner.com/GoogleOnlineSecurityBlog` |
| Epoch AI | `https://epochai.substack.com/feed` |
| Cyber Security News (AI) | `https://cybersecuritynews.com/category/cyber-ai/feed/` |

---

## Web Sources (No RSS)

Some sources don't have RSS feeds. Fetch these pages directly and extract recent items:

| Source | URL | What to extract |
|--------|-----|-----------------|
| MCP Servers Directory | `https://mcpservers.org/` | New MCP server listings, recently added tools |
| MCP Skills Library | `https://mcpservers.org/claude-skills` | New Claude skills, recently added skills |

For web sources: use WebFetch to get the page, extract item names/descriptions/links, then apply the same keyword filtering as RSS items.

---

## Fetching

**Batch feeds in groups of 5 parallel WebFetch calls.** Too many simultaneous fetches cause "sibling tool call errored" failures. Wait for each batch to complete before starting the next.

Example with 20 RSS sources:
- Batch 1: feeds 1-5 (parallel)
- Batch 2: feeds 6-10 (parallel)
- Batch 3: feeds 11-15 (parallel)
- Batch 4: feeds 16-20 (parallel)
- Batch 5: web sources (parallel)

If a feed fails, note it and move on — don't retry during the same batch.

---

## Keyword Filtering

Articles must match at least ONE from EACH list:

**Security:** vulnerability, exploit, malware, cve, breach, attack, threat, ransomware, phishing, zero-day, hacker, cyber, security, apt, backdoor, botnet, credential, encryption, intrusion, patch, payload, pentesting, rootkit, spyware, trojan

**AI:** ai, artificial intelligence, machine learning, llm, gpt, neural, deep learning, model, chatgpt, claude, copilot, gemini, openai, anthropic, transformer, generative, prompt, embedding, inference, training, agent, automation, nlp, mcp, model context protocol, langchain, agentic, tool use, function calling

---

## Age Filtering

**IMPORTANT: Only include articles published within the last 7 days.**

Before presenting candidates for review:
1. Check the `pubDate` field from each RSS item
2. Calculate the article's age relative to today's date
3. **Discard any article older than 7 days**

This ensures the post covers current news, not stale content that readers may have already seen.

---

## Source Tracing

Many feeds (Schneier, The Hacker News, Dark Reading, Bleeping Computer) are **aggregators** — they report on research published elsewhere. Before presenting candidates, trace each article back to its **primary source**.

**How to trace:**
1. Check if the article's description or title references another organization's research (e.g., "CrowdStrike found...", "Unit 42 researchers discovered...", "according to a report by Wiz...")
2. If it does, use WebFetch on the aggregator article to find the link to the original source
3. Replace the aggregator link with the primary source link
4. Credit the primary source, not the aggregator

**When to keep the aggregator:**
- The aggregator *is* the primary source (Schneier's own analysis/opinion, not reporting on someone else)
- The original source is behind a paywall or login wall
- The original source can't be found

**Deduplication after tracing:** Multiple aggregators often cover the same original research. After tracing, deduplicate by primary source URL — keep only one entry per underlying story.

---

## Classification

| Type | Criteria | Output |
|------|----------|--------|
| **EDITORIAL** (1 max) | Story worth exploring in depth — implications, context, opinion, what it means for the field | 3-5 paragraph long-form write-up |
| **FEATURE** (4-5 max) | Major CVE with AI component, significant breach, new AI attack technique, defensive AI breakthrough | 2-3 sentence summary |
| **MENTION** (5-7 max) | Tool updates, minor vulns, conference talks, industry news | One-liner |
| **SKIP** | No AI+security intersection, duplicates, marketing, >7 days old | Ignore |

**Be selective.** With many sources, you'll have more candidates than slots. Quality over quantity.

**Editorial vs Feature:** A feature summarizes *what happened*. An editorial explores *what it means* — adds context, connects dots, takes a position. Not every issue needs one; only select editorial when a story genuinely warrants deeper analysis.

---

## Article Selection

### Step 1: PAL Consensus

After filtering and deduplication, use `mcp__pal__consensus` to rank the candidates.

**Models to use:**
- `google/gemini-2.5-flash`
- `x-ai/grok-4.1-fast`
- `openai/gpt-5-mini`

**Consensus prompt:**
> Given these candidate articles for an AI + cybersecurity news roundup blog post, classify each as:
> - EDITORIAL (at most 1 — a story worth exploring in depth with context, implications, and opinion)
> - FEATURE (most significant, novel, or impactful — aim for 4-5)
> - BRIEF (noteworthy but less critical — aim for 5-7)
> - SKIP (not worth including)
>
> For each article, provide a one-line reason for the classification.
>
> Criteria for EDITORIAL: A story that warrants deeper analysis — broader implications, connects to trends, or deserves a position/opinion. Not every issue needs one.
> Criteria for FEATURE: Major security implications, novel AI attack/defense technique, significant breach, or important research.
> Criteria for BRIEF: Useful updates, minor vulnerabilities, interesting but not groundbreaking.
> Criteria for SKIP: Weak AI+security intersection, marketing fluff, or redundant coverage.
>
> **All candidates have already been filtered to the last 7 days.** Be ruthless. Readers have limited time.

### Step 2: Interactive Review

Present each candidate to the user one-by-one, using the consensus classification as the **suggested** pick. Do NOT generate any draft content until the user has reviewed every candidate.

**For each candidate, present:**

```
### [N/total] Title
Source: <source name> | Published: <date>
Summary: <1-2 sentence description from the feed>
Link: <url>

Consensus says: FEATURE / BRIEF / SKIP
Reason: <consensus reasoning>
```

**Then ask the user to choose using AskUserQuestion:**
- **Editorial** — Deep-dive write-up with context and opinion (max 1 per issue)
- **Feature** — Include as a featured story (full write-up)
- **Brief** — Include in "In brief" section (one-liner)
- **Skip** — Leave it out

The default option should match the consensus suggestion. The user may also provide free-text notes (e.g., "feature this but focus on the supply chain angle", "combine with the next one", "I saw a better source for this").

**After all candidates are reviewed, show a summary:**

```
EDITORIAL (0-1):
1. Title — [user notes if any]

FEATURES (N):
1. Title — [user notes if any]
2. ...

IN BRIEF (N):
1. Title — [user notes if any]
2. ...

SKIPPED (N):
1. Title
2. ...
```

Then ask using AskUserQuestion: "This is your final lineup. Want to swap any classifications, or good to go?"
- **Swap some** — User specifies which articles to reclassify (e.g., "move #3 to editorial, demote #1 to brief")
- **Good to go** — Proceed to draft generation

If the user wants swaps, apply the changes, show the updated summary, and ask again. Repeat until confirmed.

**Guardrails:**
- If user selects >1 editorial, ask which one to keep (max 1 per issue)
- If user approves >5 features, note the limit and ask which to demote to brief
- If user approves <2 features, note it's a slow news week (still proceed)
- Respect user notes during draft generation — if they said "focus on X", do that

---

## Voice Pipeline

After generating the draft content:

### Step 1: /humanizer
Removes AI writing patterns (filler phrases, promotional language, em-dash overuse, etc.)

### Step 2: /accidentalrebel-voice
Applies the final personality:
- Direct and practical tone
- Shows the "why it matters"
- Specific numbers (CVEs, versions, percentages)
- Honest about limitations

---

## Blog Post Structure

The draft follows the established pattern for "Cybersecurity x AI News Roundup" posts on AccidentalRebel.com:

1. **Title** (H1) — catchy headline summarizing the week's theme (NOT "WaitAISec")
2. **Introduction** — 2-3 sentences summarizing what's in this issue, followed by `<!-- PELICAN_END_SUMMARY -->`
3. **Horizontal rule** (`---`)
4. **Editorial** (`## Editorial`, optional) — Long-form deep-dive on one story (3-5 paragraphs). Omit entirely if no EDITORIAL selected.
5. **Horizontal rule** (`---`) (only if editorial exists)
6. **Featured stories** (`## Featured stories`) — 4-5 major stories with full summaries
7. **Horizontal rule** (`---`)
8. **In brief** (`## In brief`) — 5-7 one-liner mentions

---

## Markdown Formatting

### Article links
- Every article title in FEATURE sections must link to the original article
- Every item in "In Brief" must include a source link
- Use inline Markdown links: `[Title](URL)`

### Example output

```markdown
# AI Agents Under Attack

AI agents are under attack this week—and AI is doing the attacking. Claude Opus 4.6 found 500+ vulnerabilities in major libraries. Language models can now run complete network breaches autonomously.
<!-- PELICAN_END_SUMMARY -->

---

## Editorial

### The real problem with autonomous vulnerability discovery

Anthropic's Claude Opus 4.6 found 500+ vulnerabilities in major open-source projects. That's impressive. It's also terrifying — because attackers have access to the same models.

We're entering an arms race where both sides use AI to find bugs. The difference: defenders need to patch all of them, attackers only need one. The economics favor offense, and the gap will only widen as models improve.

The practical takeaway? If you maintain open-source code, assume AI is already auditing it. Automated scanning isn't optional anymore — it's table stakes.

---

## Featured stories

### [AI models execute autonomous network attacks](https://example.com/article2)

Language models can now independently conduct multi-stage network penetration testing, handling reconnaissance through data extraction while adapting to defensive measures.

---

## In brief

- **[175,000 Ollama servers publicly exposed](https://example.com/article3)**: SentinelOne and Censys found 175K Ollama instances running without authentication across 130 countries.

- **[Ghidra MCP server](https://example.com/article4)**: A developer released 110 tools integrating Ghidra with AI assistants via Model Context Protocol.
```

---

## Output

Save the draft to the working directory:

1. Build filename: `YYYY-MM-DD-waitaisec-draft.md` using current date
2. Use Glob to check if file exists: `**/YYYY-MM-DD-waitaisec-draft*.md`
3. If exists, append `_N` (start at 1, increment until unique)
4. Write the Markdown file to the current working directory

After saving, tell the user: "Draft saved to `<filename>`. Run `/new-post <filename>` to convert to a Pelican blog post, then `/send-newsletter` to email it to subscribers."

---

## Reference Files

- [references/sample-post.md](references/sample-post.md) - Example output matching existing blog posts

---

## Notes

- If <2 FEATURE articles, note it's a slow news week
- If no dual-keyword matches, relax to "security OR AI with clear relevance"
- The `/new-post` skill handles Pelican metadata (Category, Tags, Slug, Date), featured image reminder, and placement in `content/`
