Title: Temp Solution For When Text Copying Does Not Work in Emacs Under Windows Subsytem for Linux
Date: 2017-09-23 13:08
Slug: temp-solution-for-when-copying-does-not-work-in-emacs-under-windows-subsystem-for-linux
Tags: emacs windows linux
Category: Misc

One of the problems I was having with my Emacs environment under WSL _(Windows Subsystem for Linux, aka. Bash On Windows)_ is that I could not copy text from WSL Emacs to other Windows applications. Copy and pasting from Windows to Emacs works without any problems so it's weird it does not work the other way around.

I tried a lot of solutions from Google but none of them seem to work. There was an emacs package called [simpleclip](https://github.com/rolandwalker/simpleclip) that worked but the results were not consistent.

I then realized that a temporary solution would be to make use of Windows' clip.exe command line utility which can bme seen below.

	:::elisp
	(defun arebel-set-clipboard-data (str-val)
	  "Puts text in Windows clipboard. Copying to Windows from WSL does 
	not work on my end so this one is a temporary solution.

	This function is called from within the simpleclip package when copy 
	or bgcopy command is issued."
	  (start-process "cmd" nil "cmd.exe" "/C" (concat "echo " (replace-regexp-in-string "\n" "\r" str-val) " | clip.exe")))

It works quite nicely especially after integrating it with simpleclip. This would do for now until I find a better solution.

> **EDIT (2017-10-01):** Turns out the original code could not copy a region with multiple lines due to the difference in carriage return characters. This is now fixed with `(replace-regexp-in-string "\n" "\r" str-val)`.
