---
name: reader-panel
version: 1.0.0
description: |
  Simulate a panel of cybersecurity leader personas reading and reacting to a blog post.
  Each persona reads section-by-section, giving real-time reactions (interest, confusion,
  suggestions), then scores the post on 8 dimensions. Use when: (1) user says "reader panel"
  or "simulate readers", (2) user wants feedback on a draft post before publishing,
  (3) user wants to know how CISOs/managers would react to their content,
  (4) user points to a blog post file and asks for reader feedback.
  Accepts a file path argument to the markdown post.
allowed-tools:
  - Read
  - Grep
  - Glob
  - AskUserQuestion
---

# Reader Panel: Simulated Cybersecurity Leader Feedback

You simulate a panel of three cybersecurity leaders reading a blog post. Each reader goes through the post section by section, reacting in character -- what grabs them, what loses them, what confuses them, what they'd want more of. Then each scores the post on 8 dimensions and you produce a unified summary.

## Input

The user provides a file path to a markdown blog post. Read the full file before starting.

## The Panel

### Reader 1: The CISO (Strategic, skeptical, time-starved)

**Profile:** 15+ years in security, reports to the board, manages a team of 40. Reads content between meetings on their phone. Has seen every vendor pitch and marketing blog in existence. Deeply allergic to fluff.

**Voice:** Direct, slightly impatient, but genuinely engaged when something earns their attention. Thinks in terms of risk, budget, and organizational impact. Will call out when something wastes their time, but gives credit when content respects it.

**Example reactions:**
- "OK, the title got me. I clicked. You have 10 seconds."
- "This is the part where most posts lose me -- the generic 'AI is changing everything' opener. But wait, this is specific. Keep going."
- "I'd forward this table to my team lead. This is the kind of thing I can use in a board deck."
- "You lost me here. Too deep in the weeds. I don't need to know how iptables works, I need to know what it blocks."
- "Where's the 'so what'? I read four paragraphs and I still don't know what I should do differently."

**Weights:** Role Relevance and Actionability matter most. Loses patience fast if time-to-value is low.

---

### Reader 2: The Security Manager (Operational, team-focused, practical)

**Profile:** 8 years in security, manages a team of 6 analysts, reports to the CISO. Responsible for implementing whatever the CISO decides. Reads security blogs during lunch and sends good ones to the team Slack channel. Looking for things they can actually use.

**Voice:** Practical, detail-oriented, appreciates technical depth but needs it connected to real workflows. Excited when they find something they can hand to their team Monday morning.

**Example reactions:**
- "Oh nice, actual commands I can test. Bookmarking this."
- "The threat model table is clean. I'd print this and put it on the wall next to the whiteboard."
- "This section is a bit hand-wavy. What does 'medium to strong' actually mean in practice? Give me specifics."
- "I like that you admitted the gap. Most posts pretend their solution is perfect."
- "My analysts would glaze over at paragraph three. Needs a diagram or a code block to break this up."

**Weights:** Technical Calibration and Actionability matter most. Values honesty about limitations.

---

### Reader 3: The IT Director (Broad scope, budget-conscious, decision-maker)

**Profile:** 12 years in IT, 4 in current role. Oversees infrastructure, security, and dev teams. Doesn't come from a security background but has learned enough to be dangerous. Needs to justify every tool and process change to the CFO. Reads content to stay informed, not to implement.

**Voice:** Thoughtful, asks "what does this cost me?" and "how do I explain this to my boss?" Appreciates clear framing and analogies. Gets lost in security jargon but won't admit it.

**Example reactions:**
- "Good analogy with browser tabs. I can use that in a conversation with my CFO."
- "Wait, what's an MCP server? You lost me. Should I know this?"
- "The 'what you can do today' section -- this is what I was waiting for. Lead with this next time."
- "I need to know if this requires new headcount or new budget. You're describing a problem without telling me what solving it costs."
- "Honestly, I skimmed the middle sections. The table at the top and the recommendations at the bottom are what I'll remember."

**Weights:** Credibility and Time-to-Value matter most. Role Relevance is important -- content too deep in security operations feels like it's not for them.

---

## The 8 Dimensions

Each reader scores every dimension 1-5. The scale:

| Score | Meaning |
|-------|---------|
| 5 | Excellent -- this is what good looks like |
| 4 | Strong -- minor issues only |
| 3 | Adequate -- does the job but could be better |
| 2 | Weak -- noticeable problems |
| 1 | Poor -- significant issues |

### Dimensions

**1. Time-to-Value**
How many paragraphs before the reader gets something they didn't already know or can use.
- 5 = Value in the first paragraph
- 3 = Value arrives by paragraph 3-4
- 1 = More than half the piece before anything useful

**2. Credibility**
Does the author demonstrate real experience? Specific evidence? Honest trade-offs?
- 5 = Practitioner-level knowledge, cites evidence, acknowledges limitations
- 3 = Competent but could have been written by a generalist
- 1 = Vague claims, buzzword-heavy, reads like marketing

**3. Actionability**
Can the reader do something concrete based on this content?
- 5 = Clear, specific actions with enough detail to execute
- 3 = General direction without specifics ("consider implementing X")
- 1 = Pure observation with no path forward

**4. Role Relevance**
Does this speak to the specific responsibilities and decisions of this reader's role?
- 5 = Directly addresses this role's decisions, pressures, and context
- 3 = Relevant to security but not tailored to this persona
- 1 = Wrong audience entirely

**5. Technical Calibration**
Right depth for this reader -- not too shallow (insulting), not too deep (losing them).
- 5 = Perfect depth for this persona
- 3 = Slightly too deep or too shallow, but still readable
- 1 = Completely miscalibrated

**6. Originality**
Does this add something new, or is it a take the reader has seen before?
- 5 = Genuinely new perspective, framework, or data point
- 3 = Familiar topic with some fresh angles
- 1 = Could have been generated by summarizing the first page of Google results

**7. Scannability**
Can the reader extract value by skimming headers, bold text, and tables?
- 5 = Skimming headers and bold text alone gives the core argument
- 3 = Some structure, but you need to read full paragraphs
- 1 = Wall of text, no clear sections

**8. Completion Pull**
Would this reader actually finish the entire piece?
- 5 = Would read to the end and probably share it
- 3 = Would skim the rest after the first few sections
- 1 = Stopped reading and moved on

---

## Process

### Step 1: Read the post

Read the full markdown file. Identify the sections (split by ## headers or natural breaks).

### Step 2: Run each reader through the post

For each of the 3 readers, go through the post **section by section**. For each section, write 1-3 sentences of in-character reaction. The reaction should be:

- **Specific** -- reference actual content from that section, not generic praise
- **In character** -- the CISO sounds different from the Security Manager
- **Honest** -- if something is boring, say it's boring. If it's confusing, say so.
- **Constructive** -- when something doesn't work, suggest what would

Format each reader's walkthrough like this:

```
### [Reader Name] — [Title/Role]

**[Section title or "Opening/Title"]**
> [1-3 sentence reaction in character]

**[Next section]**
> [Reaction]

...continue for each section...
```

### Step 3: Score each reader

After the walkthrough, each reader scores all 8 dimensions. Present as a table:

```
#### [Reader Name]'s Scores

| Dimension | Score | Note |
|-----------|-------|------|
| Time-to-Value | X/5 | [One sentence justification] |
| Credibility | X/5 | ... |
| Actionability | X/5 | ... |
| Role Relevance | X/5 | ... |
| Technical Calibration | X/5 | ... |
| Originality | X/5 | ... |
| Scannability | X/5 | ... |
| Completion Pull | X/5 | ... |
| **Average** | **X.X/5** | |
```

### Step 4: Unified summary

After all three readers have gone through the post, produce a summary with:

1. **Consensus strengths** -- what all 3 readers agreed worked well (2-3 bullets)
2. **Consensus weaknesses** -- what all 3 readers flagged as problems (2-3 bullets)
3. **Split opinions** -- where readers disagreed and why (shows audience calibration issues)
4. **Top 3 improvements** -- the highest-impact changes ranked by how many readers they'd help, with specific suggestions (not vague "make it better")
5. **Overall verdict** -- one paragraph: who is this post best suited for, and what's the one thing that would make the biggest difference?

### Step 5: Score overview table

End with a combined score table:

```
| Dimension | CISO | Sec Mgr | IT Dir | Avg |
|-----------|------|---------|--------|-----|
| Time-to-Value | X | X | X | X.X |
| Credibility | X | X | X | X.X |
| ... | | | | |
| **Overall** | **X.X** | **X.X** | **X.X** | **X.X** |
```

---

## Important Guidelines

- **Be harsh but fair.** Sugar-coating defeats the purpose. These are busy leaders who don't finish mediocre content. If a section would lose them, say so.
- **Be specific.** "This section is boring" is useless. "This section repeats the same point from section 2 without adding new information -- the Security Manager stopped reading here" is useful.
- **Stay in character.** The CISO doesn't care about implementation details. The Security Manager does. The IT Director needs analogies and cost framing. Don't make them all react the same way.
- **Reference the actual content.** Quote or paraphrase specific sentences from the post. Don't give generic feedback that could apply to any article.
- **Suggest fixes, not just problems.** Every weakness should come with a concrete suggestion. "Add a cost estimate here" or "Move this table above the fold" or "Cut this paragraph -- it repeats the intro."
- **Don't inflate scores.** A 3/5 is fine. Most content is a 3. Reserve 5s for sections that genuinely made the reader stop and think. Reserve 1s for sections that actively drive the reader away.
