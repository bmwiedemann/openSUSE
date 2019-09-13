;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; File name: ` ~/.gnu-emacs '
;;; ---------------------
;;;
;;; Note: This file is for GNU-Emacs only ...
;;;       GNU-Emacs is incompatible to X-Emacs. Therefore your
;;;       personal ~/.emacs should load this file if your runnning
;;;       the good old GNU-emacs.
;;;
;;; If you need your own personal ~/.gnu-emacs
;;; please make a copy of this file
;;; an placein your changes and/or extension.
;;;
;;; For emacs commands have a look onto the
;;; `emacs-revcard' in the directory /usr/doc/packages/emacs/
;;;
;;; Copyright 1993-2001 Werner Fink
;;; Copyright (c) 1996-2001 SuSE Gmbh Nuernberg, Germany.
;;; All rights reserved.
;;;
;;; Author: Werner Fink, <werner@suse.de> 1993-2001
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;
;; No splash screen at all
;; -----------------------
(if (and (file-exists-p "~/.inhibit-splash-screen")
	 (boundp 'inhibit-splash-screen))
  (setq-default inhibit-splash-screen t))
;;
;; Debuging only
;; -------------
;  (open-dribble-file "~/.dribble")
;  (open-termscript "~/.termscript")
;;
;; Emacs makes backup by moving original files, to
;; avoid trouble with hardlinked files we may use:
;; -----------------------------------------------
;  (defconst backup-by-copying-when-linked t)
;;
;; Rmail: We will place all Mail's an Mail-folders into ~/Mail
;; -----------------------------------------------------------
(if (file-accessible-directory-p "~/Mail/")
    (setq rmail-secondary-file-directory "~/Mail/"))
;;
;; Prefix for mail-mode
;; ---------------------
  (setq mail-yank-prefix "> ")
; (setq mail-archive-file-name "~/Mail/.CarbonCopy")
  (setq mail-self-blind nil)
  (setq mail-default-headers nil)
  (setq mail-signature nil)
;;
;; Settings for message-mode
;; -------------------------
  (setq message-from-style "angles")
(if (null mail-host-address)
  (let ((tmph (getenv "HOSTNAME"))
	(tmpf (getenv "FROM_HEADER")))
     (if (or (null tmph) (not (string-match "\\." tmph)))
	 (setq tmph (system-name)))
     (if (not (string-match "\\." tmph))
	 (setq mail-host-address "our.domain.is.not.set")
	(string-match "\\." tmph)
	(setq mail-host-address (substring tmph (match-end 0))))
     (if (stringp tmpf)
	 (setq mail-host-address tmpf)))
     (setq tmpf nil tmph nil))
;;
;; RMAILGEN: Folder im Rmail-Mode :-)
;; ----------------------------------
;;
;; 1. I want to define a mail directory that isn't `~/'
(if (file-accessible-directory-p "~/Mail/")
    (setq rmailgen-default-directory "~/Mail/")) ; must end in slash
;;;
;; 2. I want 78 column
(add-hook 'mail-mode-hook (function (lambda () (setq fill-column 78))))
(if (file-exists-p "~/.abbrev_defs")
    (progn (read-abbrev-file "~/.abbrev_defs")
           (add-hook 'mail-setup-hook 'mail-abbrevs-setup)))
;;;
;; 3. By default, if mail-archive-file-name is non-nil then
;; archive file names will be generated automatically based on
;; the message to which a reply is being constructed.  If I
;; wanted to turn this off I would put in a statement like
(setq rmailgen-archive-file-name nil)
;;;
;; 4. By default, rmailgen.el downcases generated filenames
;; If I wanted uppercase I would put in a statement like here.
(setq rmailgen-downcase "dummy")
;;;
;; 5. By default, rmailgen.el does not append `.gz' to generated
;; filenames.  If I wanted such an extension I would put in a statement
;; like
;;(setq rmailgen-gzip-file-name t)
;;;
;; 6. By default, rmailgen.el will use generated FCC filenames even
;; if the file does not exist.  If I wanted to FCC only if the file
;; already exists I would put in a statement like
;; (setq rmailgen-archive-only-if-exists t)
;;;
;; 7. Add my own personal output list for specific friends
;; and special subjects.
;;;
;; First define rmail-output-file-alist, just in case this
;; is not already defined.  That is, may be
;; ../lisp/rmailout.el has not been loaded yet.
(if (not (boundp 'rmail-output-file-alist))
    (defvar rmail-output-file-alist nil))
;;;
(setq rmail-output-file-alist
      (append
	(list

;	  ;; For my friends (some have strange account names).
;	  '("^From:[ \t]*.*jones.*" . "jmjones")
;	  '("^From:[ \t]*.*Joe[ \t]*Smith.*" . "joe")
;
;	  ;; Special subject lines.
;	  '("^Subject:[ \t]*.*crypt.*" . "crypt++")
;	  '("^Subject:[ \t]*.*rmailgen.*" . "genrmail")
;	  '("^Subject:[ \t]*.*dired-x.*" . "dired-x")
;	  '("^Subject:[ \t]*.*GNU Emacs 19 RMAIL Poll.*" . "rmail")
;
;	  ;; Add more entries here...
	)
;;;
	;; In case rmail-output-file-alist has been defined
	;; already elsewhere.
	rmail-output-file-alist))
;;;
;; 8. Load package [REQUIRED].
(if (file-exists-p "/usr/share/emacs/site-lisp/rmailgen.el")
    (require 'rmailgen))
;;
;; Base text mode
;; ----------------------
  (setq default-major-mode 'text-mode)
  (line-number-mode 1)
  (global-set-key "\e\?" 'goto-line)
  (column-number-mode 1)
;;
;; User can cutomize that: Just show e.g. DOS files with CR/NL
;; ----------------------
; (setq-default inhibit-eol-conversion t)
  (setq-default require-final-newline "ask")
;;
;; Specials for X Window System
;; -------------------------
(if (not window-system)
      ;; ispell
      ;; ----------------------
      ;; (A few changes on ispell)
      (setq ispell-highlight-face 'underline);)
  ;;
  ;; Some fonts
  ;; -----------------------
  (if (> emacs-major-version 20) (require 'xfonts))
  ;;
  ;; New in Emacs 21: tool bar menu, you may switch it of
  ;; ----------------------------------------------------
; (if (fboundp 'tool-bar-mode) (tool-bar-mode 0))
  ;;
  ;; mouse as arrow
  ;; --------------
  (setq x-pointer-shape x-pointer-left-ptr)
  (if (x-display-color-p)
      (set-mouse-color "RoyalBlue")
    (set-mouse-color (cdr (assq 'mouse-color (frame-parameters)))))
  ;;
  ;;   Automatically replacing of fore- and background.
  (if (not (x-display-color-p))
    (progn
      (set-face-background 'region
	       (cdr (assq 'foreground-color (frame-parameters ))))
      (set-face-foreground 'region
	       (cdr (assq 'background-color (frame-parameters ))))
      ;; ispell
      ;; ----------------------
      ;; (A few changes on ispell)
      (setq ispell-highlight-face 'underline)))
  ;;
  ;; Highlighting of special emacs modes
  ;; -----------------------------------
  ;; We use font lock mode

  ;; Darken greyed strings in font lock mode
  (custom-declare-face 'font-lock-string-face
    '((((class grayscale) (background light)) (:foreground "gray37"    :italic t))
      (((class grayscale) (background dark))  (:foreground "LightGray" :italic t))
      (((class color) (background light)) (:foreground "gray37"))
      (((class color) (background dark))  (:foreground "LightGray"))
      (t (:italic t)))
    "Font Lock mode face used to highlight strings."
    :group 'font-lock-highlighting-faces)

  ;; Enable font lock support
  (require 'font-lock)
  (cond ((and (boundp 'jit-lock-mode) (symbol-value 'jit-lock-mode))
         (setq font-lock-support-mode '((latex-mode . fast-lock-mode) (t . jit-lock-mode))))
        ((and (boundp 'lazy-lock-mode) (symbol-value 'lazy-lock-mode))
         (setq font-lock-support-mode '((latex-mode . fast-lock-mode) (t . lazy-lock-mode)))))
  (add-hook 'after-init-hook '(lambda () (global-font-lock-mode 1)))

  ;;
  ;; Some dialog
  ;; ------------------
  (setq use-dialog-box t)
  ;;
  ;; less dialog
  ;; -----------
  ;(menu-prompting nil)
  ;; 
  ;; Set X synchrone
  ;; ---------------
  ;; Speed up
   (setq mouse-scroll-delay 0)
   (setq x-selection-timeout 0)
  ;;
  ;; We use a wrapper script for netscape
  ;;
  (if (file-executable-p "/usr/X11R6/bin/Netscape")
      (setq browse-url-netscape-program "/usr/X11R6/bin/Netscape"))
)
;;
;; emacsclient: automatical popup under X11
;; ------------------------------------------
;(defun server-make-window-visible ()
;  "Try to make this window even more visible."
;(if window-system
;  (progn
;     (let ((foo (selected-frame)))
;	   (sit-for 0)
;	   (make-frame-visible foo))
;       (accept-process-output))))
;(add-hook 'server-switch-hook '(lambda () (server-make-window-visible)))
;(add-hook 'server-visit-hook  '(lambda () (server-make-window-visible)))
;; Start it for popup
;(server-start)
;;
;; Emacs experts like this
;; -----------------------
(put 'eval-expression 'disabled nil)
;;
;; Working on parts of text
;; ------------------------
;; NB: `C-x n n' is narrow-to-region
;;     `C-x n p' is narrow-to-page
;;     `C-x n w' is widen
;(put 'narrow-to-region 'disabled nil)
;(put 'narrow-to-page   'disabled nil)
;;
;; GNUS
;; ----
;; Sorting
(if (or (and (= emacs-major-version 19) (> emacs-minor-version 29))
	(> emacs-major-version 19))
     (add-hook 'gnus-select-group-hook
	'(lambda ()
	  (setq-default gnus-auto-select-first nil)
	  (setq-default gnus-auto-center-summary nil)
	  (setq gnus-thread-sort-functions
	   '(gnus-thread-sort-by-number
	     gnus-thread-sort-by-subject
	     gnus-thread-sort-by-date
	     gnus-thread-sort-by-score))))
   (add-hook 'gnus-select-group-hook
	'(lambda ()
	  (setq-default gnus-auto-select-first nil)
	  (setq-default gnus-auto-center-summary nil)
	  ;; First of all, sort by date.
	  (gnus-keysort-headers
	   (function string-lessp)
	   (function
	    (lambda (a)
	      (gnus-sortable-date (gnus-header-date a)))))
	  ;; Then sort by subject string ignoring `Re:'.
	  ;; If case-fold-search is non-nil, case of letters is ignored.
	  (gnus-keysort-headers
	   (function string-lessp)
	   (function
	    (lambda (a)
	      (if case-fold-search
		  (downcase (gnus-simplify-subject (gnus-header-subject a) t))
		(gnus-simplify-subject (gnus-header-subject a) t)))))
	 ))
)
;; highlighting, menus, and subscribing in GNUS
(add-hook 'gnus-startup-hook
     '(lambda ()
	(setq gnus-subscribe-newsgroup-method
	'(lambda (newsgroup)
	   (gnus-subscribe-newsgroup newsgroup)
	   (gnus-kill-newsgroup newsgroup)))
	(setq gnus-use-generic-from t)
	;; highlighting and menu in GNUS
	(if (or (and (= emacs-major-version 19) (> emacs-minor-version 29))
		(> emacs-major-version 19))
	  (progn
	    (setq gnus-visual '(highlight menu))
	    (setq gnus-group-highlight
		'(;; News.
		  ((and (> unread 100) (not mailp)) . gnus-summary-high-ticked-face)
		  ((and (> unread 0) (not mailp))   . gnus-summary-high-read-face)
		  ((and (= unread 0) (not mailp))   . gnus-summary-high-ancient-face) 
		  ((not mailp)			    . gnus-summary-normal-ancient-face) 
		  ;; Mail.
		  ((and (= unread 0) (eq level 1))  . gnus-group-mail-1-empty-face)
		  ((eq level 1)			    . gnus-group-mail-1-face)
		  ((and (= unread 0) (eq level 2))  . gnus-group-mail-2-empty-face)
		  ((eq level 2)			    . gnus-group-mail-2-face)
		  ((and (= unread 0) (eq level 3))  . gnus-group-mail-3-empty-face)
		  ((eq level 3)			    . gnus-group-mail-3-face)
		  ((= unread 0)			    . gnus-group-mail-low-empty-face)
		  (t				    . gnus-group-mail-low-face)))
      )))
)
;;
;; Common to all C modes
;; ---------------------
;(add-hook 'c-mode-common-hook
;   '(lambda () (c-set-style "linux")
;	(c-set-offset 'case-label 4)
;	(setq c-basic-offset 4)))

;;
;; Auto fill mode
;; --------------
(add-hook 'text-mode-hook 'turn-on-auto-fill)
;;
;; Fill-column
;; -----------
;;    Fill-column ist hier auf 78 Charakter gesetzt, nach Wunsch "andern!
(setq-default fill-column 78)
(add-hook 'TeX-mode-hook '(lambda () (setq fill-column 78)))
;;
;; AUC-TeX
;; ----------------------------
(if (boundp 'AUCTeX-version)
 (progn
  (let* ((version (split-string AUCTeX-version "\\."))
	 (major (string-to-number (car version)))
	 (minor (string-to-number (car (cdr version)))))
    (if (or (> major 11) (and (eq major 11) (>= minor 86)))
	(custom-set-default 'TeX-master nil)
      (setq-default TeX-master nil)))
; ; Users private libaries 
; (if (boundp 'AUCTeX-version)
;   (progn
;     (setq TeX-macro-private '("~/lib/tex-lib/"))
;     (setq TeX-style-private   "~/lib/site-lisp/auctex/style/")   ; AUC-TeX-Macros
;     (setq TeX-auto-private    "~/lib/site-lisp/auctex/auto/")))  ; Autom. Auc-TeX-Macros
  (if (and window-system (featurep 'font-lock))
      (progn
	(add-hook 'latex-mode-hook 'turn-on-font-lock)
	(if (boundp 'AUCTeX-version)
	  (progn
	    (add-hook 'LaTeX-mode-hook 'turn-on-font-lock)
	    (add-hook 'LaTeX-mode-hook 'LaTeX-math-mode)
	    (add-hook 'after-init-hook '(lambda () (load "auctex/font-latex" nil t)))))))
))

;;
;; Brace macros
;; ------------
(defun TeX-Inserting (sta stb stc)
    (if (= (preceding-char) sta )
	(insert stb)
      (progn (insert stc) (backward-char 1))))
(defun TeX-schweif () (interactive "*") (TeX-Inserting ?\\ "{"  "{}"))
(defun TeX-rundekl () (interactive "*") (TeX-Inserting ?\\ "("  "()"))
(defun TeX-eckigek () (interactive "*") (TeX-Inserting ?\\ "["  "[]"))
(defun TeX-exponen () (interactive "*") (TeX-Inserting ?\\ "^" "^{}"))
(defun TeX-subscri () (interactive "*") (TeX-Inserting ?\\ "_" "_{}"))
(defun TeX-dollarm () (interactive "*") (TeX-Inserting ?\\ "$"  "$$"))
(defun TeX-REVbbox () (interactive "*") (TeX-Inserting ?\\ "bbox{"  "\\bbox{}"))
(add-hook 'LaTeX-mode-hook
      '(lambda ()
	 ;; Uncomment this for automatic bracket closing
	 ;; Begin bracket closing
;	 (local-set-key  "{" 'TeX-schweif)
;	 (local-set-key  "(" 'TeX-rundekl)
;	 (local-set-key  "[" 'TeX-eckigek)
;	 (local-set-key  "^" 'TeX-exponen)
;	 (local-set-key  "_" 'TeX-subscri)
;	 (local-set-key  "$" 'TeX-dollarm)
;	 (local-set-key  "\C-b" 'TeX-REVbbox)
	 ;;
	 ;; It's german:
	 ;; Deutsche Tastatur im LaTeX-German-Style/Babel-Class
	 ;; ---------------------------------------------------
	 ;;    Aktivierung mit `M-x german-mode' -> man dr"ucke
	 ;;    *nacheinander* <ComposeCharacter>, <">, <a> und staune!
	 ;;    ACHTUNG: Bei grossen Files sehr LANGSAM beim Abspeichern
	 ;;    das ist vom Prinzip her bedingt! Hier gibt's keinen Support!
;	 (require 'ger-keys)
	 ;; End bracket closing
	 ;; For ISO Latin standard: Macro out of `ger-keys'
	 ;; ger-keys should be loaded
;	 (german-mode)
	 ;; For german style usage:
;	 (modify-syntax-entry ?" "w")
;	 (local-set-key  "\"" 'self-insert-command)
	 ;; Deutsche Belegung amerikanischer Tastaturen: aus `ger-keys'
;	 (german-keyboard)
))
;;
;; Provide some usefull function keys
;; ----------------------------------
;; Have a look on /usr/share/emacs/site-lisp/function-keys.el
;; Extensions or changes of the keymap
;; original definitions will found in loaddefs.el.
;;(global-set-key [escape] [?\e]) ; Escape
;;
  (global-set-key [M-left]  'backward-word)
  (global-set-key [M-right] 'forward-word)
  (global-set-key [M-up]    'beginning-of-line)
  (global-set-key [M-down]  'end-of-line)
;;
; (global-set-key [C-left]  'backward-char)
; (global-set-key [C-right] 'forward-char)
; (global-set-key [C-up]    'previous-line)
; (global-set-key [C-down]  'next-line)
;;
; (global-set-key [S-left]  'backward-char)
; (global-set-key [S-right] 'forward-char)
; (global-set-key [S-up]    'previous-line)
; (global-set-key [S-down]  'next-line)
;;
  (global-set-key [find]   'isearch-forward) ; Search
  (global-set-key [select] 'set-mark-command) ; Mark
;;
  (global-set-key [S-next]   'end-of-buffer)
  (global-set-key [S-prior]  'beginning-of-buffer)
  (global-set-key [S-find]   'find-file)
  (global-set-key [S-select] 'switch-to-buffer)
  (global-set-key [S-insert] 'insert-file)
;;
  (if (and (= emacs-major-version 19) (= emacs-minor-version 29))
    (define-key key-translation-map [f1] nil)) ; 19.29+
  (global-set-key [S-f1]  'find-file)
  (global-set-key [M-f1]  'find-file)
  (global-set-key [f1]    'help-for-help)    ; `Help'
  (global-set-key [pause] 'toggle-read-only) ; `HoldScreen'
;;
  (if (global-key-binding [f2])
    (progn
      (global-set-key [S-f2]  'split-window)
      (global-set-key [M-f2]  'split-window))
    (global-set-key [f2]  'split-window))
  (if (global-key-binding [f2])
    (progn
      (global-set-key [S-f2]  'split-window)
      (global-set-key [M-f2]  'split-window))
    (global-set-key [f2]  'split-window))
  (if (global-key-binding [f3])
    (progn
      (global-set-key [S-f3]  'isearch-forward)
      (global-set-key [M-f3]  'isearch-forward))
    (global-set-key [f3]  'isearch-forward))
  (if (global-key-binding [f4])
    (progn
      (global-set-key [S-f4]  'query-replace-regexp)
      (global-set-key [M-f4]  'query-replace-regexp))
    (global-set-key [f4]  'query-replace-regexp))
  (if (global-key-binding [f5])
    (progn
      (global-set-key [S-f5]  'save-buffer)
      (global-set-key [M-f5]  'save-buffer))
    (global-set-key [f5]  'save-buffer))
  (if (global-key-binding [f6])
    (progn
      (global-set-key [S-f6]  'find-file)
      (global-set-key [M-f6]  'find-file))
    (global-set-key [f6]  'find-file))
  (if (global-key-binding [f7])
    (progn
      (global-set-key [S-f7]  'buffer-menu)
      (global-set-key [M-f7]  'buffer-menu))
    (global-set-key [f7]  'buffer-menu))
  (if (global-key-binding [f8])
    (progn
      (global-set-key [S-f8]  'repeat-complex-command)
      (global-set-key [M-f8]  'repeat-complex-command))
    (global-set-key [f8]  'repeat-complex-command))
  (if (global-key-binding [f9])
    (progn
      (global-set-key [S-f9]  'execute-extended-command)
      (global-set-key [M-f9]  'execute-extended-command))
    (global-set-key [f9]  'execute-extended-command))
  (if (global-key-binding [f10])
    (progn
      (global-set-key [S-f10] 'eval-expression)
      (global-set-key [M-f10] 'eval-expression))
    (global-set-key [f10] 'eval-expression))
;;
;;(global-set-key [f11] [?\e]) ; Escape
  (global-set-key [f11] esc-map) ; Escape
;;
  (global-set-key [f12]       'backward-delete-char-untabify) ; Backspace
;;
;; DEC keyboard: f13 up to f20
  (global-set-key [f13]      'newline) ; Linefeed
  (global-set-key [linefeed] 'newline) ; Linefeed
;;
  (global-set-key [f14] 'switch-to-buffer)
;;
;; Emacs original key binding
;;
; (global-set-key [home]   'beginning-of-buffer) ;
; (global-set-key [end]    'end-of-buffer) ;
;;
  (global-set-key [help]   'info) ; Help
  (global-set-key [M-help] 'repeat-complex-command) ; Redo
  (global-set-key [menu]   'execute-extended-command) ; Do
  (global-set-key [M-menu] 'eval-expression) ; eval
;;
  (global-set-key [f17] 'beginning-of-buffer)
  (global-set-key [f18] 'end-of-buffer)
  (global-set-key [f19] 'save-buffer)
  (global-set-key [f20] 'find-file)
;;
;; Translate `C-h' to DEL.
; (keyboard-translate ?\C-h ?\C-?)
;;
;; Translate DEL to `C-h'.
; (keyboard-translate ?\C-? ?\C-h)
;;;;;;;;;;
;; the end
