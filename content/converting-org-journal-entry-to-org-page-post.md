Title: Converting org-journal entry to org-page post
Date: 2017-04-19 13:17
Slug: converting-org-journal-entry-to-org-page-post
Tags: emacs org-mode
Category: Misc

Since my recent switch from Wordpress to [org-page](https://github.com/kelvinh/org-page) I wanted a way to convert my org-journal entries to org-page posts. Instead of copying each entry by hand and pasting to an org-page new page buffer I decided to make an elisp code that would do it automatically which can be seen below:

	:::elisp
	(defun arebel-org-journal-entry-to-org-page-post ()
	  "Copy the org-journal entry at point and then convert it to a org-page new post buffer."
	  (interactive)
	  (if (eq 'org-journal-mode major-mode)
		  (let ((headline-text (nth 4 (org-heading-components)))
			(entry-text (org-get-entry)))
		(funcall-interactively 'op/new-post "blog" (concat (buffer-name) "-" headline-text))
		(goto-char (point-max))
		(insert entry-text))
		(message "This function can only be called inside org-journal-mode.")) )

The function is simple and uses functions from org-mode and org-page.

  * First, it checks if the current buffer is in org-journal-mode
  * Then it gets the headline text and entry texts
  * It then calls op/new-post. It does it interactively so that it will trigger the prompts needed to populate the template. (Also notice that it takes the org-journal buffer name plus time as the blog post's org file name. This way I don't have to specify it.)
  * It then inserts the entry-text at the end of the buffer.

From here I am free to edit, commit, then publish.

It's working great. As proof this post you are reading right now has been made with the code above.
