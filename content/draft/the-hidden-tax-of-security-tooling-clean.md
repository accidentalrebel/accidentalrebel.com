Title: The hidden tax of security tooling: why your analysts are clicking instead of analyzing
Date: 2026-03-09 20:00
Slug: the-hidden-tax-of-security-tooling-clean
Tags: security, tools
Category: security
Status: draft
Image: the-hidden-tax-of-security-tooling.png
Summary: SOC analysts spend 20+ minutes per shift on repetitive UI clicks in tools like Sentinel. Here's how I measured it, what I built to fix it, and what it tells us about how we evaluate security tooling.

![The hidden tax of security tooling]({attach}/images/the-hidden-tax-of-security-tooling.png)
*Image by Gemini*

Security Operations Centers run on tickets. An alert fires, an analyst triages it, and the ticket gets assigned, investigated, documented, and closed. That cycle repeats dozens of times per shift. The tools that manage this workflow, SIEMs like Microsoft Sentinel, Splunk, or IBM QRadar, are built for complex investigations. But most tickets aren't complex. Most are routine closures where the UI gets in the way more than it helps.

I started measuring how much time my team was losing to mechanical clicking. The numbers surprised me.

## The click tax

Closing a ticket in Microsoft Sentinel is not hard. It's just slow. You click to assign, wait for the page to update, click to change status, wait again, click to open the comments field, type your note, click to save, click to confirm. Multiply that by every ticket, every shift, every analyst on the team. After hours of doing this, it gets tiring.

None of those clicks are analysis. They're ceremony. The platform needs you to navigate its UI the way it was designed, not the way the work actually flows. And because each individual click takes only a few seconds, nobody measures the cumulative cost.

I started paying attention to how much of my shift was spent on mechanical interaction versus actual investigation. The ratio was worse than I expected. If closing a ticket takes 30 seconds of clicking and waiting, and an analyst closes 40 tickets per shift, that's 20 minutes per analyst per day spent on clicks alone. Scale that across a team of five analysts and you're losing over an hour and a half of combined analyst time every day. Not on analysis. On UI navigation. At a fully loaded cost of $60/hour per analyst, that's roughly $25,000 a year spent on clicking through UI dialogs.

## Why this goes unmeasured

Security tools are typically evaluated on capability: detection coverage, integration breadth, compliance features. Procurement checklists ask "Can it do X?" not "How many clicks does X take?" That's reasonable during selection, but it means workflow efficiency rarely gets assessed after deployment.

The result is platforms that technically do everything but make the common paths friction-heavy. The 80% case (triage, assign, close with a note) gets the same number of clicks as the 5% case (complex multi-step investigation). There's no fast path for the routine work.

This is easy to miss if you're not the one doing the clicking. Analyst activity looks like productivity from the outside — if someone is working through Sentinel, they look busy. But half those clicks are navigational overhead, not investigative decisions, and you won't see that unless you measure it.

## The bookmarklets

I got tired of the repetition, so I wrote two browser bookmarklets — one to assign a ticket to me, one to close it. The assign one is trivial, so I'll share the closing script since it has more steps. It opens the status dialog, selects "Closed", prompts for a closing reason and classification, then clicks OK. Two prompts replace 30 seconds of manual navigation. The analyst clicks on an incident ticket first to open it, then clicks the bookmark:

<details>
<summary>Close ticket bookmarklet (click to expand)</summary>

```javascript
javascript:(function(){
  /* Opens the status change dialog */
  document.getElementsByClassName(
    "ext-details-header-item fxs-fxclick ext-dialog-target-caseStatus"
  )[0].click();

  setTimeout(function(){
    var mouseup_event = document.createEvent("MouseEvents");
    mouseup_event.initEvent("mouseup", true, true);
    var change_event = document.createEvent("HTMLEvents");
    change_event.initEvent("change", true, true);
    var dialog = document.getElementsByClassName("fxs-messagebox")[0];

    /* Selects "Closed" from the status list */
    dialog.getElementsByClassName("fxc-listView-itemcontent")[2].click();

    /* Prompts for closing reason and fills the textarea */
    var text_area = dialog.getElementsByClassName(
      "azc-textarea azc-formControl azc-input azc-validation-border "
      + "msportalfx-tooltip-overflow msportalfx-font-regular"
    )[0];
    var reason = prompt("Closing reason", "");
    text_area.value = reason;
    text_area.dispatchEvent(change_event);

    /* Opens the classification dropdown, defaults to False Positive */
    dialog.getElementsByClassName(
      "azc-formControl azc-input fxc-dropdown-open "
      + "msportalfx-tooltip-overflow azc-validation-border fxc-dropdown-input"
    )[0].dispatchEvent(mouseup_event);
    var classifications = dialog.getElementsByClassName(
      "fxc-dropdown-option msportalfx-tooltip-overflow fxs-portal-hover"
    );
    var pick = prompt("Classification (1-4)", "2");
    classifications[parseInt(pick) - 1].dispatchEvent(mouseup_event);

    /* Clicks OK after a delay */
    setTimeout(function(){
      dialog.getElementsByClassName(
        "fxc-base fxc-simplebutton"
      )[0].click();
    }, 1000);
  }, 1000);
})();
```

You're free to use this. Collapse it to a single line and save it as the URL of a browser bookmark. It works on the current Sentinel portal as of early 2026.

</details>

![Edit bookmark dialog showing the Close Ticket bookmarklet]({attach}/images/editbookmark.png)

It's not sophisticated. No API calls, no network access, no external dependencies. The `setTimeout` calls are ugly but necessary because the portal renders asynchronously.

 Here's the bookmarklet in action:

<iframe width="560" height="315" src="https://www.youtube.com/embed/rCi5JlfY73U?si=GaQJQVLYIXe3fYKu" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

One caveat: if Microsoft changes Sentinel's layout or element structure (which they do), the script breaks. So you want someone on the team who can fix it. Thankfully, the script is simple enough that updating a selector takes a few minutes.

A browser bookmark shouldn't be able to replace a multi-step workflow that takes 30+ seconds per ticket. But it does, which tells you the platform's UI wasn't optimized for the work analysts actually do most often.

## Where this could go

If I could, I'd skip the Sentinel UI for routine tickets entirely. The Azure CLI has a `sentinel` extension with `az sentinel incident update` and `az sentinel incident comment create` commands that can assign, change status, close with classification, and add comments from the command line. The extension is still marked experimental, but the commands work. You could build a lightweight interface on top of that, designed around the actual triage workflow instead of the general-purpose portal.

This matters more now because Microsoft is moving Sentinel management into the Defender portal, with the Azure portal redirect going mandatory in July 2026. The UI these bookmarklets target will eventually stop working. The API won't.

Looking further out, you could wire an AI agent into the same API. It reads the incident details, drafts a closing comment based on the alert context, and the analyst approves or edits before it closes the ticket. The mechanical part disappears and the analyst only shows up for the judgment call. That's either fewer analysts for the same volume, or the same team spending their time on investigations instead of ticket ceremony. We're not far from that being practical.

## What to do about it

Every analyst I've worked with feels this friction, but the small delays compound invisibly over a shift. Each click feels minor. Nobody notices the accumulation. Couple that with a queue that never empties, and nobody stops to ask whether the tool itself is part of the problem.

The fix doesn't have to be bookmarklets. It depends on where you sit.

**Measure it.** If you manage a SOC, sit behind an analyst for an hour without saying anything. Time how long it takes to close a straightforward true-positive ticket from start to finish. Then ask how much of that time was thinking versus clicking. The gap is the tax you're paying. Document the number so you have a baseline before you try to fix anything.

**Automate the worst offenders.** In my case, 40 lines of JavaScript saved each analyst roughly 20 minutes per shift. You don't need a full platform overhaul. Identify the two or three most repetitive workflows and script them. Bookmarklets, CLI wrappers, or API calls against the same backend your SIEM already uses. Start small, measure the difference.

**Bring the data to your vendor or procurement team.** "Our analysts spend 20 minutes per shift on UI navigation" is a specific, measurable complaint. "The 80% case takes the same number of clicks as the 5% case" is a design problem your vendor should hear about. If you're in a renewal cycle, workflow efficiency deserves a line on the evaluation checklist next to detection coverage and compliance.

Most teams never get past step one because the cost is spread thin enough that it never shows up in a report. But someone has to look at the workflow, notice the waste, and decide it's worth fixing. 

Next time you evaluate a security tool, ask how many clicks it takes to close a routine ticket. Nobody ever does. That's the problem.
