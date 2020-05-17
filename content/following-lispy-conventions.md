Title: #4 - Following Lispy conventions
Date: 2020-05-15 07:00
Slug: following-lispy-conventions
Tags: dev, game_engine, 
Category: game_engine

   ![following-lispy-conventions-01]({attach}/images/following-lispy-conventions-01.png)

   I was adding new Lisp functions to [my game engine](https://github.com/accidentalrebel/Rebel-Game-Engine) when I noticed that I had functions that had a naming scheme that were inconsistent with others. For example, I had ones that create objects like *sprite_create* and *shader_create* but this one function I named *make_vec3*. I proceeded to rename *make_vec3* to *vec3_create*. Not only is it consistent with other names but it made me realize that having a pattern of object_verb makes it easy to parse the function and what it does. 

   This made me wonder if there are other ways I could improve which led me to this page [about variable naming conventions](http://community.schemewiki.org/?variable-naming-convention) for Scheme. I learned that the language employs a rather effective yet simple naming convention for functions and variables. I've noticed them before but never really thought about their usefulness. 
   
   For example, adding a *?* prefix easily indicates that the function, when called, will always return a boolean value. I looked at my code and I had the function *is_key_down*. Changing it to *key_down?* looked weird at first but I liked how it made the function name shorter and the *?* prefix made it easy to spot and parse.

   Okay, cool! What's next?

   Adding a *!* indicates a function that mutates data. Most commonly used for setting a variable. I saw I had variables like *set_vec3_x*, to which I changed to *vec3_x!*.

   This went on as I continue to find improvements. Here's a list of all the naming convention changes that I've made:

   | **The change**                                 | **From**              | **To**             |
   | :--------------------------------------------: | :-------------------: | :----------------: |
   | *:* infix for namespaces.                      | vec3_create           | vec3:create        |
   | *?* postfix for boolean functions              | key_down?             | key:down?          |
   | *!* postfix for destructive functions          | set_camera_position   | camera:position!   |
   | *%* postfix for low level functions            | free                  | free%              |
   | *%* prefix and postfix for low level variables | shader-pointer        | %shader-pointer%   |
   | *\** prefix and postfix for global variables   | cube-shader           | \*cube-shader\*    |

   Again, these new changes felt weird at first but I quickly became accustomed the more of these functions I changed. The code became easier to scan as there are now key characters for my eyes to easily latch onto. Something to appreciate especially with multi-level nested expressions.

   Here's how the code now looks like with the new functions:
   
	:::scheme
	(define MOVEMENT_SPEED 0.001)

	(define *cube*)
	(define *cube-shader*)
	(define *cube-positions*)

	(define (init)
	  (set! *cube*
		(cube:create "assets/textures" "awesomeface.png"))
	  (set! *cube-shader*
		(shader:create "shaders/simple-3d.vs" "shaders/simple.fs"))
	  (set! *cube-positions*
		(list (vec3:create 0 0 0)
			  (vec3:create 1.25 0 0)
			  (vec3:create -1.25 0 0))))

	(define (update)
	  (window:clear)

	  (let* ((main-camera (camera:main))
		 (current-projection (camera:projection main-camera))
		 (camera-pos (camera:position main-camera)))

		(when (key:up? KEY_C)
		  (if (= current-projection PERSPECTIVE)
		  (camera:projection! main-camera ORTHOGRAPHIC)
		  (camera:projection! main-camera PERSPECTIVE)))

		(when (key:down? KEY_A)
		  (vec3:x! camera-pos
			  (+ (vec3:x camera-pos) MOVEMENT_SPEED)))
		(when (key:down? KEY_E)
		  (vec3:x! camera-pos
			  (- (vec3:x camera-pos) MOVEMENT_SPEED)))
		(when (key:down? KEY_COMMA)
		  (vec3:z! camera-pos
			  (+ (vec3:z camera-pos) MOVEMENT_SPEED)))
		(when (key:down? KEY_O)
		  (vec3:z! camera-pos
			  (- (vec3:z camera-pos) MOVEMENT_SPEED))))

	  (for-each
	   (lambda (position)
		 (let ((%tint% (vec3:create% 1 0 1)))
		   (cube:draw *cube* position 1 1 %tint% *cube-shader*)
		   (free% %tint%)))
	   *cube-positions*)

	  (window:swap))

   
   I also changed my C functions to reflect a *NamespaceVerb* convention. I could have used *namespace::Verb* but the [FFI that I use](http://wiki.call-cc.org/eggref/5/bind) to communicate with C cannot parse C namespaces. So instead of *Shader::Create*, I am left with *ShaderCreate*. This is unfortunate, but I'm fine with it since the lisp scripting side of the engine will be the most prominently used (Plus, [Raylib also uses this convention](https://www.raylib.com/examples.html) for their functions).

   I am happy that I was able to do these changes early. Because of this, readability of my code has increased, something I worried about when I first started implementing scripting.
