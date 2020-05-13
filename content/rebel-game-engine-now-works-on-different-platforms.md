Title: Rebel Game Engine now works on different platforms
Date: 2020-05-10 07:08
Slug: rebel-game-engine-now-works-on-different-platforms
Tags: dev, game_engine, 
Category: dev

   After finishing the integration of Chicken-scheme scripting for [my custom game engine](https://github.com/accidentalrebel/Rebel-Game-Engine) I decided I wanted to tackle another hard problem, and that is making it cross-platform. At the very least, my engine should be able to deploy to Linux, Windows, and MacOSX.
   
   ![rebel-game-engine-now-works-on-different-platforms-01]({attach}/images/rebel-game-engine-now-works-on-different-platforms-01.jpg)

   It might seem silly to be working on this while the engine is still in its early stages, but I think it is better to get this out of the way before the codebase becomes huge. With a small codebase I was able to easily identify the causes of the problems as I was porting them.

   It still wasn't a walk in the park, however. Being inexperienced with developing C programs on other platforms (I've only done it mostly in Linux) I had to do research and do a lot of trial and error. I learned so much about cross-compilers, portable makefiles, and the quirks of different package managers.

   After a week of this I was finally able to get the engine working on all three platforms. To make sure others can be able to do the same, I also documented the steps which can now be read on [the project's wiki](https://github.com/accidentalrebel/rebel-game-engine/wiki). 

   I was surprised that the hardest one to get working was for Windows. Because I didn't want to create a separate build system that uses Visual Studio solution files, I had to find a simple way to make it work and that involved the use of an excellent building platform for Windows called [Msys2](https://www.msys2.org/). 

   I am quite happy that I was able to structure the whole system so that you only need one Makefile for all three platforms. I'm not sure if this wil change in the future, but I'll do my best for it to stay like this as long as it's possible.

   If you are interested to try it out here's the project's [Github page](https://github.com/accidentalrebel/rebel-game-engine), depending on your platform here are the instructions on how to build for each one: [Linux](https://github.com/accidentalrebel/rebel-game-engine/wiki/Building-and-running-the-engine-for-Arch-Linux), [MacOSX](https://github.com/accidentalrebel/rebel-game-engine/wiki/Building-and-running-the-engine-for-MacOSX) and [Windows](https://github.com/accidentalrebel/rebel-game-engine/wiki/Building-and-running-the-engine-for-Windows-(using-Msys2)).
