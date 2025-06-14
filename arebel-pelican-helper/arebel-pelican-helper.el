;;; arebel-pelican-helper.el --- Helper functions for Pelican blog management

;;; Commentary:
;; This package provides Emacs functions to interact with Pelican blog posts
;; through Python helper scripts.

;;; Code:

(defvar arebel-pelican-helper-path
  (expand-file-name "~/development/arebel/blog/arebel-pelican-helper/")
  "Path to the arebel-pelican-helper directory.")

(defvar arebel-pelican-blog-path
  (expand-file-name "~/development/arebel/blog/")
  "Path to the Pelican blog directory.")

(defun arebel-create-blog-post ()
  "Create a new Pelican blog post."
  (interactive)
  (let* ((title (read-string "Title: "))
         (tags (read-string "Tags (comma-separated): "))
         (category (completing-read "Category: " 
                                   '("cybersecurity" "malware-analysis" "reverse-engineering" 
                                     "programming" "ctf" "tools" "misc")
                                   nil nil))
         (image (read-string "Featured image (optional): "))
         (default-directory arebel-pelican-blog-path)
         (output (shell-command-to-string
                 (format "python3 %screate-post.py %s %s %s %s"
                         arebel-pelican-helper-path
                         (shell-quote-argument title)
                         (shell-quote-argument tags)
                         (shell-quote-argument category)
                         (shell-quote-argument image)))))
    (if (string-match "^ERROR:" output)
        (message "%s" output)
      (find-file (string-trim output)))))

(defun arebel-rename-blog-post ()
  "Rename the current blog post."
  (interactive)
  (let* ((current-file (buffer-file-name))
         (new-title (read-string "New title: "))
         (default-directory arebel-pelican-blog-path)
         (output (shell-command-to-string
                 (format "python3 %srename-post.py %s %s"
                         arebel-pelican-helper-path
                         (shell-quote-argument current-file)
                         (shell-quote-argument new-title)))))
    (if (string-match "^ERROR:" output)
        (message "%s" output)
      (let ((new-file (string-trim output)))
        (kill-buffer (current-buffer))
        (find-file new-file)))))

(defun arebel-insert-image ()
  "Insert an image into the current blog post."
  (interactive)
  (let* ((image-path (read-file-name "Select image: "))
         (name-suffix (read-string "Image name suffix (optional, leave empty for auto-numbering): "))
         (current-buffer (buffer-name))
         (default-directory arebel-pelican-blog-path)
         (output (shell-command-to-string
                 (format "python3 %sinsert-image.py %s %s %s"
                         arebel-pelican-helper-path
                         (shell-quote-argument current-buffer)
                         (shell-quote-argument image-path)
                         (shell-quote-argument name-suffix)))))
    (if (string-match "^ERROR:" output)
        (message "%s" output)
      (insert (string-trim output)))))

(provide 'arebel-pelican-helper)

;;; arebel-pelican-helper.el ends here
