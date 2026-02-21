Title: Chef Wars Postmortem -- What went right: Having a Universe File
Date: 2017-12-05 12:56
Slug: chef-wars-postmortem--what-went-right-having-a-universe-file
Tags: chefwars, gamedev, mindcake, postmortem
Category: Misc

**Note: This is from a [series of articles](http://www.accidentalrebel.com/tags/chefwars_postmortem/) that outlines the things I've learned while making [Chef Wars](http://mindcakegames.com/) for 2+ years.**

**TLDR**

  * All data in our game is contained in one excel file we call the "Universe".
  * Prototypes can be done on the Universe excel file itself
  * Iteration is easier as we only need to change one file.
  * We made a system that downloads changes from our server so players don't need to update their builds.

---

   Before we started development on Chef Wars, Cliff, my co-founder and game designer for the team, already had pages of spreadsheets containing important values in the game. It's kinda like a game design document but in the form of tables, columns, and rows. This "Universe" file contained everything from stats, dialogue, competitions, locations, chefs, and enemies just to name a few. 

![01](https://i.imgur.com/rVZqbaH.png)

    *This file definitely gives a hint on what type of guy Cliff is.*

   Having a list of all the data that will be used in the game has helped us visualize the scope and the systems to be built, especially in making prototypes. One time Cliff made a simulation of the battle system using his Excel mastery. The universe data is fed into this simulation (i.e. competition level, recipe power) and the expected values are displayed (i.e. judging result, rewards amount). This mockup allowed us to see how the battles play out and made the whole thing easier for me to understand and implement in the engine.

   All the content of the universe file is then converted to the JSON format which is used directly by the game. Iterating on the game is easy because the file would just need to be converted again for the new changes to show up. The conversion process is done manually though using a CSV to JSON tool. I would have automated the process but didn't have the time to work on it.

![02](https://i.imgur.com/lE5zqDu.png)

    *It's like the Matrix*

   Initially, when we wanted to update some values, we would need to push a new build version that players need to download. We figured that this is too cumbersome especially if we really have some critical changes we want to get out as soon as possible. As a solution to this, we made a system where a master copy of the JSONs are saved on our servers. We can change the data from here and the game would automatically download the necessary files that we changed. This is a really great feature that has helped us push important changes without having the need for a new build. But it does require a lot of bandwidth especially if a lot of players request for the new data so we do it only when needed like on crash producing bugs.

   As you can see, we've spent a lot of time making sure that our game is data-centric as possible and it benefitted us immensely. This approach has been so useful that we plan to use it on our future projects. And hopefully, after reading this, we've convinced you to try it out too.

*[Check out how the universe has been transformed into a game by playing Chef Wars on [Android](https://play.google.com/store/apps/details?id=air.com.mindcakegames.chefwars&hl=en) and [iOS](https://play.google.com/store/apps/details?id=air.com.mindcakegames.chefwars&hl=en). Also, be sure to check out Cliff's postmortem where he talks about the [things we learned during our global launch](http://mindcakegames.com/chef-wars-launch-post-mortem/)!]*
