Title: Converting org-journal entry to org-page post
Date: 2017-04-19 13:17
Slug: minifying-buffer-contents-in-emacs
Tags: emacs
Category: Misc
Summary: A short Emacs Lisp function to minify buffer contents by stripping all whitespace and newlines, useful for compacting JSON files.

I needed a way to minify JSON files from Emacs so I made the short function below.

	:::elisp
	(defun arebel-minify-buffer-contents()
		"Minifies the buffer contents by removing whitespaces."
		(interactive)
		(delete-whitespace-rectangle (point-min) (point-max))
		(mark-whole-buffer)
		(goto-char (point-min))
		(while (search-forward "\n" nil t) (replace-match "" nil t)))

The function is very simple. First it deletes the whitespaces for the whole current buffer then removes every newline.

This effectively turns this:

	:::json
	{
		"glossary": {
			"title": "example glossary",
			"GlossDiv": {
				"title": "S",
				"GlossList": {
					"GlossEntry": {
						"ID": "SGML",
						"SortAs": "SGML",
						"GlossTerm": "Standard Generalized Markup Language",
						"Acronym": "SGML",
						"Abbrev": "ISO 8879:1986",
	"GlossDef": {


							  "para": "A meta-markup language, used to create markup languages such as DocBook.",
							"GlossSeeAlso": ["GML", "XML"]
						},
						"GlossSee": "markup"
					}
				}
			}
		}
	}

To this:

	:::json
	{"glossary": {"title": "example glossary","GlossDiv": {"title": "S","GlossList": {"GlossEntry": {"ID": "SGML","SortAs": "SGML","GlossTerm": "Standard Generalized Markup Language","Acronym": "SGML","Abbrev": "ISO 8879:1986","GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso": ["GML", "XML"]},"GlossSee": "markup"}}}}}

It works for my current needs but have not fully tested it yet. It works for emacs lisp buffers too.
