Title: #1 - Thinking of adding Lisp to my custom game engine
Date: 2020-05-03 11:19
Slug: thinking-of-adding-lisp-to-my-custom-game-engine
Tags: dev, lisp, engine, 
Category: engine
FacebookImage: https://www.accidentalrebel.com/images/thinking-of-adding-lisp-to-my-custom-game-engine-01.jpg

   I've long wondered if I should add a scripting language to [my game engine](https://github.com/accidentalrebel/Rebel-Game-Engine). I know that most game engines could do without such a feature but I just recently came across [Chibi-Scheme](https://github.com/ashinn/chibi-scheme), a library that allows the use of Scheme lisp scripting for C programs. 
   
   I like Lisp. I use it a lot when customizing my Emacs environment ([using ELisp](https://github.com/accidentalrebel?tab=repositories&q=&type=&language=emacs+lisp)). There's something about it's syntax and different way to structure programs that appeals to my programmer brain. I've toyed with other Lisp flavors but never had a strong enough reason to continue using them. With Chibi-scheme I may have found that reason.
   
![thinking-of-adding-lisp-to-my-custom-game-engine-01]({attach}/images/thinking-of-adding-lisp-to-my-custom-game-engine-01.jpg)

   I am aware that Lisp is not as widespread as Lua or Javascript. And that choosing it might limit the number of potential people to try out my game engine. But as I've been telling myself over and over, this is a self-learning project. So it's okay if no one would try it out as long as I get to learn from it.

   This morning I started implementing a simple implementation of Chibi. Thankfully, it's easy to setup. However, the more I implement it the more that I realize that I may need to change how my engine is structured to better suit Lisp's functional nature. This means less object oriented design similar to how [Raylib](https://www.raylib.com/index.html) does things. 

   I still need some time to think this through. I am open to do the changes needed if I am to include a scripting language. I just want to make sure if my engine would really need it. We'll see.
