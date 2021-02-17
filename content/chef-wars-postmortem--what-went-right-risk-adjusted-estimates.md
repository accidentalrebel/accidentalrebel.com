Title: Chef Wars Postmortem -- What Went Right: Risk Adjusted Technical Estimates
Date: 2017-12-10 23:33
Slug: chef-wars-postmortem--what-went-right-risk-adjusted-estimates
Tags: chefwars, gamedev, mindcake, postmortem
Category: postmortem

**Note: This is from a [series of articles](http://www.accidentalrebel.com/tags/chefwars_postmortem/) that outlines the things I've learned while making [Chef Wars](http://mindcakegames.com/) for 2+ years.**

**TL;DR**

  * We used a risk adjusted estimation system that produces near accurate estimates we can confidently rely on.

----

I usually dreaded being asked how long a programming task will take. I always seem to have the knack to overshoot no matter how hard I try. This is an all too common scenario that programmers face and is something that is considered to be a difficult, if not impossible, problem to solve.

![01](https://i.imgur.com/KqCZUHl.jpg)

This all changed when I was introduced to a helpful system that helps in producing estimates that are "accurate enough". I don't think it has a name yet but my colleagues who introduced me to it says that they got it from a [Gamasutra article](https://www.gamasutra.com/view/feature/181992/waterfall_game_development_done_.php) by Eric Preisz of Garage Games. Since then I've used this system in all my game development related projects and has helped us immensely in the development of our recent game, [Chef Wars](http://mindcakegames.com/).

I'm sharing this in the hopes that it would help others too.

## Risk Adjusted Estimates

The basic idea of this system is that for each task, an estimated time would be given along with a "confidence level". The lower the confidence the more padding is added automatically to the estimate for that task.

It's a very simple system and is illustrated clearly in the image below:

| Task   | Estimate | Confidence | Risk-Adjusted |
|--------|:--------:|:----------:|--------------:|
| Task A |        5 |          2 |          9.44 |
| Task B |        8 |          6 |         11.56 |
| Task C |       10 |          8 |         12.22 |
| Task D |       10 |         10 |         10.00 |

A legend (shown below) is used to help programmers determine what confidence level to specify based on their current situation.

|     Level | Description                                                                                                                                    |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------:|
|         1 | 	No clue -- don't make decisions on this. We need to talk more.                                                                         |
| 2	 | Hardly a clue -- don't make decisions on this. We need to talk more.                                                                           |
|         3 | 	Someone else has done this and I read about it; job not well defined -- don't make decisions on this. We need to talk more.            |
| 4	 | Someone else has done this and I think I understand this; job might not be well-defined -- don't make decisions on this. We need to talk more. |
|         5 | 	Done something similar to this before and this relates to that work -- this estimate has a variance of +/- 50 percent of estimate.     |
| 6	 | I think I understand this fairly well and I understand the goal.                                                                               |
|         7 | 	The average case for programming when the requirements are understood.                                                                 |
|         8 | 	A confident case for programming. It's rare that something unexpected would happen.                                                    |
|         9 | 	I've done this before and it's very similar. If something unexpected comes up, I know how to tackle it.                                |
|        10 | 	No matter what, I'm only going to work on this for the specified period of time                                                        |

The formula for calculating the risk-adjusted time is also very straightforward:

> (estimated time * (10 - confidence level) / 9) + estimated time

From hereon you can easily compute for the total time and make a comparison between the estimated time and the risk adjusted time.

To see how all of this works you can check out our [Technical Estimate Template Sheet](https://docs.google.com/spreadsheets/d/1KNTq88bw5qO6Ejbm71z31X-jraJDjB-9WET-2BZR2-s/edit?usp=sharing) at our Google Drive. Or if you are into Emacs, I also have a [template for that as well](https://gist.github.com/accidentalrebel/0df9f9e024c7e3d433ef8a4f9fada2a9) using OrgMode.

## How effective is it?

The following is taken from the technical estimate I made for a recent module in Chef Wars. I've logged the actual time it took me to finish the task so the results can be compared.

**Note:** _Each estimate is in hours._

| Task                                                       | Estimate | Confidence | Risk Adjusted | Actual time | Difference |
|:----------------------------------------------------------:|:--------:|:----------:|:-------------:|:-----------:|:----------:|
| [Backend] Create PVP Player Collections                    |        2 |          8 |     2.4444444 |           1 |       1.44 |
| [Backend] Set Player PVP Collections                       |        8 |          8 |     9.7777778 |           7 |       2.78 |
| [Leaderboard] Fetch City Leaderboards                      |       16 |          7 |     21.333333 |          18 |       3.33 |
| [Leaderboard] Monthly Leaderboard Resetting                |        2 |          7 |     2.6666667 |           4 |      -1.33 |
| [Logic] PVP Competition Setup                              |        8 |          7 |     10.666667 |           9 |       1.67 |
| [UI] Add the City Ranking button in Global/Friend Rankings |        1 |         10 |             1 |           1 |          0 |
| [UI] City Master Chefs UI                                  |        2 |          8 |     2.4444444 |           6 |      -3.56 |
| [UI] City Arena UI                                         |        2 |          8 |     2.4444444 |           4 |      -1.56 |
| [UI] Top Chef Awarding Pop Up                              |        1 |          8 |     1.2222222 |           2 |      -0.78 |
| Totals                                                     |          |            |         53.99 |          51 |       2.99 |

As you can see that the actual times are very close to the risk adjusted times. I overshot quite a bit during the UI related tasks but the time lost was offseted by the other tasks as seen in the totals. 

Take note that this is just a small sample and results will vary. There are times where totals still overshoot but mostly it is just in terms of a few hours, or at worst a full day. Regardless, our overall experience has been great as it has proven to be accurate enough that we could confidently commit to certain dates and schedules.

## Tips on using this system

* This system works great if you know the tasks beforehand. You really need to sit down and think what the steps are and try not to miss anything and to avoid adjustments.
* The more granular the tasks, the easier it is to assign a time and confidence level to them.
* Being honest with the confidence levels helps produce more accurate estimates. It also brings to light any low-confidence tasks that are in need of reconsideration.
* Make the scope smaller and easier to digest by dividing your project into smaller parts (It can be by milestone or by module) and then make an estimate for each.
* Do this long enough and you'll get better with judging estimates and confidence levels.
* It helps to review and compare how long a task took against your estimates. It will give you insight why you overshot (In the example above, I learned that I am still bad at properly estimating UI related tasks. I should adjust my confidence levels for next time).

## Conclusion
This simple system has helped us a lot and we plan to use it on all our future projects. It's not 100% accurate but it is accurate enough that we can schedule confidently with it. I would be the first to admit that it may not work for everyone but if you are always overshooting your estimates then this system might be worth a try.

**[Check out our game which was released relatively on time over at [Android](https://play.google.com/store/apps/details?id=air.com.mindcakegames.chefwars&hl=en) and [iOS](https://itunes.apple.com/us/app/chef-wars/id1254831133?mt=8)]**
