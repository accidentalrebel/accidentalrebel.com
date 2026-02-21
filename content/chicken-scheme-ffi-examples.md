Title: Chicken-Scheme FFI Examples
Date: 2020-06-16 05:58
Slug: chicken-scheme-ffi-examples
Tags: programming, dev, research, code
Category: Misc
Summary: Practical Chicken Scheme FFI examples covering foreign-lambda, struct accessors, inline C code, memory management, and enum bindings for C interop.

   I'm currently working on refactoring the FFI implementation for [the Rebel Game Engine](https://github.com/accidentalrebel/rebel-game-engine). It was previously written using the [Bind chicken egg](http://wiki.call-cc.org/eggref/5/bind) but I wanted to have more control over the implementation by using the low level foreign functions. 
   
   To help me better understand I made some examples that has the basic FFI implementations that I'll be needing for my project.
   
-------------------------------------------------------------------------------

## foreign-lambda example

   Let's say we have a structure `Vec3` and a function `Vec3Create` that we want to access from chicken-scheme.

	:::c
	typedef struct Vec3 {
		float x;
		float y;
		float z;
	} Vec3;
	
    Vec3* Vec3Create(float x, float y, float z)
	{
		Vec3* v = (Vec3*)malloc(sizeof(Vec3));
		v->x = x;
		v->y = y;
		v->z = z;
		return v;
	}

   We could use [`foreign-lambda`](https://wiki.call-cc.org/man/5/Module%20(chicken%20foreign)#foreign-lambda) to bind to the function:
   
    :::scheme
	(define vec3_create
	  (foreign-lambda
	    (c-pointer (struct "Vec3"))   ; Return type, a pointer to a struct object of Vec3
		"Vec3Create"                  ; Name fo the function
		float float float))           ; The three parameters (x,y,z) to pass to the function
		
   This would allow us to call the `vec3_create` function like so:
   
    :::scheme
	(vec3_create 1.1 2.2 3.3)
	
-------------------------------------------------------------------------------

## foreign-lambda* example

   Let's bind another C function `Vec3Print`.
   
	:::c
	void Vec3Print(Vec3 v)
	{
		printf("Vec3 to print: (%f, %f, %f)\n", v.x, v.y, v.z);
	}
	
   We could also use [`foreign-lambda*`](https://wiki.call-cc.org/man/5/Module%20(chicken%20foreign)#foreign-lambda) (Notice the asterisk). This is similar to `foreign-lambda` but accepts C code as a string.
   
    :::scheme
	(define vec3_print
	  (foreign-lambda*
	    void                          ; The return type
		(((c-pointer (struct "Vec3")) a0)) ; The parameter to pass, a pointer to a Vec3 object
		"Vec3Print(*a0);"))           ; The C code in string from
		                              ; Vec3Print accepts a non pointer, we dereference it
									  
	(vec3_print (vec3_create 1.1 2.2 3.3))   ; Creates a vec3 and prints it
	
-------------------------------------------------------------------------------

## Inline C code in foreign-lambda*

   Here's another example using `foreign-lambda*`. This time there is no predefined C function, but instead we define the code inside the lisp function's body.
   
    :::scheme
	(define vec3_zero
	  (foreign-lambda*
	    (c-pointer (struct "Vec3"))
		()                            ; Empty variables
		"Vec3* v = (Vec3*)Vec3Create(0.0f, 0.0f, 0.0f); 
		C_return(v);"))               ; Instead of "return", we use "C_return".
		
	(vec3_print (vec3_zero))          ; Calls vec3_zero and prints the returned Vec3
		
   Note that due to obscure technical reasons `C_return` must be used instead of `return` when returning a value. More info about this [here](https://wiki.call-cc.org/man/5/Module%20(chicken%20foreign)#foreign-lambda).
   
-------------------------------------------------------------------------------

## Free-ing Vec3 pointers

   Since `Vec3Create` allocates memory for a Vec3 struct using `malloc`, it's a good idea to free this when we are done using it. To do this we could bind a function to `free`.
   
	:::scheme
	(define free (foreign-lambda void "free" c-pointer))
	
	(let ((v (vec3_zero)))
	  (vec3_print v)
	  (free v))
	  
-------------------------------------------------------------------------------

## Setting up getters and setters

   If we want to have access to variables of a struct object. We could do something like this:
   
    :::scheme
	(define vec3_x
	  (foreign-lambda*
	    float
		(((c-pointer (struct "Vec3")) a0))
		"C_return(a0->x);"))

	(display (vec3_x (vec3_create 8.8 8.8 8.8)))
	
   Now this is fine but it'll be a pain to specify an accessor for every variable. A better solution is to use the [`foreigners`](http://wiki.call-cc.org/eggref/5/foreigners#define-foreign-enum-type) egg which allows the use of macros that will make our lives easier.
   
    :::scheme
	(import (chicken foreign))
	(import foreigners)

	;; Set up the accessors for Vec3 struct
	(define-foreign-record-type (vec3 Vec3)
	  (float x vec3_x vec3_x!)   ; vec3_x is a getter, vec3_x! is a setter
	  (float y vec3_y vec3_y!)
	  (float z vec3_z vec3_z!))

	(let ((v (vec3_create 4.4 5.5 6.6)))
	  (display (vec3_x v)) ; Display value of x
	  (newline)

	  (vec3_x! v 7.7)      ; Set x to 7.7
	  (display (vec3_x v)) ; Display value of x
	  (newline)
	  
	  (free v))

-------------------------------------------------------------------------------

## Binding enums

   The [`foreigners`](http://wiki.call-cc.org/eggref/5/foreigners#define-foreign-enum-type) egg also allows for the binding of enums using [`define-foreign-enum-type`](http://wiki.call-cc.org/eggref/5/foreigners#define-foreign-enum-type). Say we have an enum declaration `Keys`.
   
    :::c
	enum Keys {
	  UP = 0,
	  RIGHT = 1,
	  DOWN = 2,
	  LEFT = 3
	};
	
	:::scheme
	(define-foreign-enum-type (keys int)
	  (keys->int int->keys)
	  ((up keys/up) UP)
	  ((right keys/right) RIGHT)
	  ((down keys/down) DOWN)
	  ((left keys/left) LEFT))

	(display keys/right)
	(display keys/down)

-------------------------------------------------------------------------------

These are the basic FFI implementations that I have explored. It should be enough for most uses. The example project with working code can be found [on Github](https://github.com/accidentalrebel/chicken-scheme-ffi-example).

Also, check out [the chicken-bind egg](http://wiki.call-cc.org/eggref/5/bind), it already has all of the code above conveniently in one package. If you don't need full control and just want a simple FFI solution then this is what you need.
	  

   
