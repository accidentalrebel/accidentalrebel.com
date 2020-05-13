Title: Implemented basic Scheme scripting for Rebel Game Engine
Date: 2020-05-07 21:35
Slug: implemented-basic-scheme-scripting-for-rebel-game-engine
Tags: lisp, game_engine, dev, 
Category: lisp

   When I first learned about [Chibi](http://synthcode.com/wiki/chibi-scheme), an embeddable scheme that allows scripting on C programs, I immediately tried it out on my game engine. I was able to make it work with my existing APIs but I kept on running against segfaults and memory issues. The community was helpful in answering my questions as I tried to track down the cause of the bug, but I eventually gave up out of frustration.

   I then learned about [Chicken Scheme](http://wiki.call-cc.org/eggref/5/bind), a somewhat competitor to Chibi that does the same thing but with a larger community and more documentation. I checked it out and liked it so I went ahead and implemented it.
   
   ![implemented-basic-scheme-scripting-for-rebel-game-engine-01]({attach}/images/implemented-basic-scheme-scripting-for-rebel-game-engine-01.png)

   Thankfully I have not experienced any segfaults anymore. It's not because Chicken is better (I don't know well enough of the two to make a good comparison) but because I've come to better understand how to properly structure my code after two implementations.

   And my code did change a lot. The biggest change is switching from an object oriented approach to functional style so that it would suit Lisp scripting. I also paid special attention in making sure that whatever change I made would make sense when the game engine is used without scripting. My guiding principle is that implementing a game on both C and Scheme should be structurally identical, aside from the difference in syntaxes, of course.
   
   Here's a simple program wher you could move a colored box using the keyboard:

	:::scheme
	(define box-sprite)
	(define box-pos)

	(define (init)
	  (set! box-sprite (sprite_create assets/textures tile.png))
	  (set! box-pos (make_vec3 400 300 0))
	  #t)

	(define (update)
	  (window_clear)

	  (when (is_key_down KEY_COMMA)
		(set_vec3_y box-pos (+ (get_vec3_y box-pos) 1)))
	  (when (is_key_down KEY_O)
		(set_vec3_y box-pos (- (get_vec3_y box-pos) 1)))
	  (when (is_key_down KEY_E)
		(set_vec3_x box-pos (+ (get_vec3_x box-pos) 1)))
	  (when (is_key_down KEY_A)
		(set_vec3_x box-pos (- (get_vec3_x box-pos) 1)))

	  (let ((tint (make_vec3 1 0 1)))
		(sprite_draw box-sprite box-pos 50 50 tint #f))

	  (window_swap)
	  #t)

   Implementing Lisp, and coding with it has been very fun too. I've had the most fun when [I implemented the FFI](http://wiki.call-cc.org/eggref/5/bind). Every time I go through the wiki I find a better way of doing things so I'd go and re-implement them again. Each iteration I learn something new and it's such a joy exploring.
   
   Playing with the garbage collector has also made me think about memory management more. This resulted in having two ways to call certain API functions: one will return a pointer that will automatically get tracked by the GC. The other you'd have to free manually. I figured this is a good approach for situations when having control over memory and references is crucial.

   I've already spent a lot of time on this project and it was mostly spent on the scripting side of the engine. There are still more to do for it to be considered useful but I'm happy I was able to learn a lot.

   If you are curious about the engine you could check it out [here](https://github.com/accidentalrebel/Rebel-Game-Engine).
