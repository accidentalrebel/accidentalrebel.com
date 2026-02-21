Title: Chef Wars Postmortem -- What went wrong: Optimizing too early and too late
Date: 2017-12-06 00:02
Slug: chef-awrs-postmortem--what-went-wrong-optimizing-too-early-and-too-late
Tags: chefwars, gamedev, mindcake, postmortem
Category: Misc

**Note: This is from a [series of articles](http://www.accidentalrebel.com/tags/chefwars_postmortem/) that outlines the things I've learned while making [Chef Wars](http://mindcakegames.com/) for 2+ years.**

**TLDR**

  * There is more to the saying that "premature optimization is the root of all evil".
  * Instead of asking WHEN to optimize, it is more important to ask WHAT and HOW to optimize.

----

It is a well known adage among programmers that premature optimization is the root of all evil. If this is true then I must have been very close to the devil himself.

During the early months of development on Chef Wars I did my best to optimize my code as much as possible. We were making a big game and I wanted to have a stable foundation to build our game on. I obsessed over lots of things from the interconnection of the various systems to folder structures. I was happy with all that I've built, but sadly progress was slow.

I realized at this point that I was optimizing too prematurely. If I wanted to reach my milestones on time then I needed to change my approach. This means leaving the optimizations for later. When is later though? I figured that it makes sense to do it at the end when all the systems are in place.

All went smoothly until we reached Open Beta. The game was reported to be sluggish and almost unplayable which signaled the need to start optimizing. While I was able to optimize some parts, there were some that I could not optimize properly without undergoing a major change to the code. Sadly, rewrites were not an option as we were running out of time.

![01](https://media.giphy.com/media/26n6T9MrKZ2Qo16Vy/giphy.gif)

    The profiler has been really helpful in catching performance problems.

Looking back it is easy to pinpoint what went wrong. I was optimizing too early, later changed my approach only to find out that I was already too late to optimize certain critical parts. I, of course, want to prevent this from happening again. So the million dollar question is: How does one determine when to optimize? How does one know when is too early and too late?

## The complete version
I later learned that the famous adage actually has a longer version:

> Programmers waste enormous amounts of time thinking about, or worrying about, the speed of noncritical parts of their programs, and these attempts at efficiency actually have a strong negative impact when debugging and maintenance are considered. We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. Yet we should not pass up our opportunities in that critical 3%.

![02](https://i.imgur.com/dqPF0cK.jpg)

	From Donald Knuth's The Art of Computer Programming

Turns out there was more to the saying that completely changes the lesson to be learned. Breaking it down we can infer that the author is telling us that:

  * Too much obsession over non-critical parts wastes time.
  * Only focus on efficiencies that matter.
  * Optimize whenever possible, but not at the expense of the previously mentioned points.

So instead of asking WHEN to optimize, it is more important to ask WHAT and HOW to optimize. In other words, anytime there is a chance to evaluate if an optimization is needed, one needs to consider whether there really is something worthwhile to optimise, and if so, how to proceed in optimizing.

## Answering the WHAT and HOW
Knowing how to answer the WHAT and HOW is not easy and requires both experience and careful planning to get right. The internet is a bit divided about this as nobody really knows the best answer. In spite of this, I was able to gather some helpful nuggets of wisdom during my research that are worth considering:

  * Be critical of what optimizations to use at each stage of the project. Determine how critical it is and if it can be done later.
  * If setting aside optimizations for later, make sure to prepare the code so that it would be easy to do so when the time comes.
  * Proper planning during the design stage can determine what to build and how to optimize in advance.
  * Measuring/profiling optimizations would reveal which are the most effective to use in the future.

## Conclusion
There is a certain sense of pride in producing optimized and stable code. Sadly, this kind of perfection comes at a cost of time. The solution is to always consider at all times when, what, and how to optimize.

This may all seem overkill to worry about but after going through 2 years worth of development on Chef Wars, I know all of this is worth taking the extra effort to do right. I hope that what I've learned may also be of use to you.

*[Our game is running better now and you could play it by downloading it on on [Android](https://play.google.com/store/apps/details?id=air.com.mindcakegames.chefwars&hl=en) and [iOS](https://play.google.com/store/apps/details?id=air.com.mindcakegames.chefwars&hl=en). Also check out my [previous postmortem](http://www.accidentalrebel.com/blog/2017/12/05/chef-wars-postmortem--what-went-right-having-a-universe-file/) where I talk about something that went right.]*
