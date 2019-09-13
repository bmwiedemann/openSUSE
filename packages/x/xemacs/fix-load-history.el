;;; -*- mode: emacs-lisp -*-

;;; fix up the load-history to make it possible to use find-function
;;; on functions which are in dumped lisp files, even if XEmacs was not
;;; dumped at the place where it is finally running. 
;;; 
;;; Suggested by Jeff Mincy <jeff@delphioutpost.com>, see:
;;; 
;;; http://list-archive.xemacs.org/xemacs-design/200204/msg00365.html
;;;
;;; Test whether this works by evaluating (find-function 'next-line)
;;; 

(defvar suse-build-directory
  (let ((dumped-file (symbol-file 'next-line)))
    (and lisp-directory
	 (file-directory-p lisp-directory)
	 dumped-file
         (not (file-exists-p dumped-file))
	 (string-match "^\\(.*[/\\]lisp[/\\]\\)" dumped-file)
         (substring dumped-file (match-beginning 1) (match-end 1))))
  "The directory that is stored in load-history for dumped files")

(when suse-build-directory
  (eval-after-load 'find-func
    (dolist (entry load-history)
      (when (string-match (regexp-quote suse-build-directory) (car entry))
	(setcar entry (replace-match lisp-directory t t (car entry)))))))

