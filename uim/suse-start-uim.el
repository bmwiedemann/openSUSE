;; /usr/share/emacs/site-lisp/suse-start-uim.el

(add-to-list 'load-path "/usr/share/emacs/site-lisp/uim-el")

;; candidate display style of this buffer
(defvar uim-candidate-display-inline t
  "If non-nil, a candidate list is displayed below the
preedit string in vertical direction.  Otherwise, it is
displayed at the echo area.")

;; don't load uim-leim immediately, see 
;; http://bugzilla.novell.com/show_bug.cgi?id=436245
(add-hook 'emacs-startup-hook '(lambda () (load "uim-el/uim-leim" nil t)))

;; /usr/share/emacs/site-lisp/suse-start-uim-el.el ends here
