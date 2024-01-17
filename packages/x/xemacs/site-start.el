;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; File name: ` /usr/share/xemacs/site-lisp/site-start.el '
;;; System wide start file for xemacs.
;;; Copyright 1999  (c) S.u.S.E. Gmbh Fuerth, Germany. All rights reserved.
;;; Author: Werner Fink <werner@suse.de>, 1999
;;;         Mike Fabian <mfabian@suse.de>, 2004, 2005
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(setq load-path (delete (concat lisp-directory
				"site-packages/lisp/term/")
			load-path))

;;
;; Preload dynamic (i)Spell menu
;; --------------
(load "/usr/lib/ispell/ispell-emacs-menu.el" t t)
(load "fix-load-history.el" t t)

;;
;; Enable mouse wheel support
;;

(when window-system
  (mwheel-install))

;; Let gnus save articles in mbox format
(defvar gnus-default-article-saver 'gnus-summary-save-in-file)

;; This system use terminfo
(defvar system-uses-terminfo t)

;; Syntax highlighting
(when (fboundp 'turn-on-lazy-lock)
  (require 'font-lock)
  ;; use lazy-lock by default if lazy-shot is not enabled
  (remove-hook 'font-lock-mode-hook 'turn-on-lazy-lock)
  (add-hook 'font-lock-mode-hook
	    (function
	     (lambda ()
		(unless (and (boundp 'lazy-shot-mode) lazy-shot-mode)
		  (turn-on-lazy-lock))))
	    t))

;;
;; i18n setup (encoding, language-environment, ...)
;; -------------------------------------------------

(if (locate-library "latin-unity") (require 'latin-unity))
(if (locate-library "latin-euro-input") (require 'latin-euro-input))
(if (and (<= emacs-major-version 21)
	 (<= emacs-minor-version 4)
	 (locate-library "un-define"))
    (require 'un-define)
  (provide 'un-define))

;; Setting the language-environment
;;
;; fix unicode-precedence-list if setting the language environment
;; screws it up.
;; 
;; Unfortunately 'set-language-environment' also changes the locale.
;; For example (set-language-environment "Japanese") sets the locale
;; to ja_JP.eucJP. That is nonsense and should not be done.
;; Therefore we remember the original value of LANG and restore the
;; locale after 'set-language-environment'.

;; create missing UTF-8 language environments:
(mapcar
 (lambda (x)
   (let ((langenv (car x)))
     (if (not (string-match "UTF-8" langenv))
	 (create-variant-language-environment langenv 'utf-8))))
 language-info-alist)

(set-language-unicode-precedence-list
 (get-language-info current-language-environment 'charset))

;; (when (emacs-version>= 21 5 6)
;;   (let ((old-lang (getenv "LANG"))
;; 	(case-fold-search nil))
;;     (when (getenv "LANG")
;;       (cond ((string-match "af" (getenv "LANG"))
;; 	     (set-language-environment "Afrikaans"))
;; 	    ((string-match "sq" (getenv "LANG"))
;; 	     (set-language-environment "Albanian"))
;; 	    ((string-match "ca" (getenv "LANG"))
;; 	     (set-language-environment "Catalan"))
;; 	    ((string-match "zh_TW" (getenv "LANG"))
;; 	     (set-language-environment "Chinese-BIG5")
;; 	     (set-language-unicode-precedence-list
;; 	      '(ascii
;; 		latin-iso8859-1
;; 		latin-iso8859-2
;; 		latin-iso8859-3
;; 		latin-iso8859-4
;; 		latin-iso8859-13
;; 		latin-iso8859-15
;; 		latin-iso8859-16
;; 		cyrillic-iso8859-5
;; 		greek-iso8859-7
;; 		chinese-big5-1
;; 		chinese-big5-2
;; 		chinese-gb2312
;; 		chinese-sisheng
;; 		korean-ksc5601
;; 		japanese-jisx0208
;; 		japanese-jisx0208-1978
;; 		japanese-jisx0212
;; 		latin-jisx0201
;; 		katakana-jisx0201)))
;; 	    ((string-match "zh_HK" (getenv "LANG"))
;; 	     (set-language-environment "Chinese-BIG5")
;; 	     (set-language-unicode-precedence-list
;; 	      '(ascii
;; 		latin-iso8859-1
;; 		latin-iso8859-2
;; 		latin-iso8859-3
;; 		latin-iso8859-4
;; 		latin-iso8859-13
;; 		latin-iso8859-15
;; 		latin-iso8859-16
;; 		cyrillic-iso8859-5
;; 		greek-iso8859-7
;; 		chinese-big5-1
;; 		chinese-big5-2
;; 		chinese-gb2312
;; 		chinese-sisheng
;; 		korean-ksc5601
;; 		japanese-jisx0208
;; 		japanese-jisx0208-1978
;; 		japanese-jisx0212
;; 		latin-jisx0201
;; 		katakana-jisx0201)))
;; 	    ((string-match "zh_CN" (getenv "LANG"))
;; 	     (set-language-environment "Chinese-GB")
;; 	     (set-language-unicode-precedence-list
;; 	      '(ascii
;; 		latin-iso8859-1
;; 		latin-iso8859-2
;; 		latin-iso8859-3
;; 		latin-iso8859-4
;; 		latin-iso8859-13
;; 		latin-iso8859-15
;; 		latin-iso8859-16
;; 		cyrillic-iso8859-5
;; 		greek-iso8859-7
;; 		chinese-gb2312
;; 		chinese-sisheng
;; 		chinese-big5-1
;; 		chinese-big5-2
;; 		korean-ksc5601
;; 		japanese-jisx0208
;; 		japanese-jisx0208-1978
;; 		japanese-jisx0212
;; 		latin-jisx0201
;; 		katakana-jisx0201)))
;; 	    ((string-match "zh_SG" (getenv "LANG"))
;; 	     (set-language-environment "Chinese-GB")
;; 	     (set-language-unicode-precedence-list
;; 	      '(ascii
;; 		latin-iso8859-1
;; 		latin-iso8859-2
;; 		latin-iso8859-3
;; 		latin-iso8859-4
;; 		latin-iso8859-13
;; 		latin-iso8859-15
;; 		latin-iso8859-16
;; 		cyrillic-iso8859-5
;; 		greek-iso8859-7
;; 		chinese-gb2312
;; 		chinese-sisheng
;; 		chinese-big5-1
;; 		chinese-big5-2
;; 		korean-ksc5601
;; 		japanese-jisx0208
;; 		japanese-jisx0208-1978
;; 		japanese-jisx0212
;; 		latin-jisx0201
;; 		katakana-jisx0201)))
;; 	    ((string-match "hr" (getenv "LANG"))
;; 	     (set-language-environment "Croatian"))
;; 	    ((string-match "ru" (getenv "LANG"))
;; 	     (set-language-environment "Cyrillic-KOI8"))
;; 	    ((string-match "cs" (getenv "LANG"))
;; 	     (set-language-environment "Czech"))
;; 	    ((string-match "da" (getenv "LANG"))
;; 	     (set-language-environment "Danish"))
;; 	    ((string-match "nl" (getenv "LANG"))
;; 	     (set-language-environment "Dutch"))
;; 	    ((string-match "et" (getenv "LANG"))
;; 	     (set-language-environment "Estonian"))
;; 	    ((string-match "fi" (getenv "LANG"))
;; 	     (set-language-environment "Finnish"))
;; 	    ((string-match "fr" (getenv "LANG"))
;; 	     (set-language-environment "French"))
;; 	    ((string-match "gl" (getenv "LANG"))
;; 	     (set-language-environment "Galician"))
;; 	    ((string-match "de" (getenv "LANG"))
;; 	     (set-language-environment "German"))
;; 	    ((string-match "el" (getenv "LANG"))
;; 	     (set-language-environment "Greek"))
;; 	    ((string-match "kl" (getenv "LANG"))
;; 	     (set-language-environment "Greenlandic"))
;; 	    ((string-match "he" (getenv "LANG"))
;; 	     (set-language-environment "Hebrew"))
;; 	    ((string-match "iw" (getenv "LANG"))
;; 	     (set-language-environment "Hebrew"))
;; 	    ((string-match "hu" (getenv "LANG"))
;; 	     (set-language-environment "Hungarian"))
;; 	    ((string-match "ga" (getenv "LANG"))
;; 	     (set-language-environment "Irish"))
;; 	    ((string-match "it" (getenv "LANG"))
;; 	     (set-language-environment "Italian"))
;; 	    ((string-match "ja" (getenv "LANG"))
;; 	     (set-language-environment "Japanese")
;; 	     (set-language-unicode-precedence-list
;; 	      '(ascii
;; 		latin-iso8859-1
;; 		latin-iso8859-2
;; 		latin-iso8859-3
;; 		latin-iso8859-4
;; 		latin-iso8859-13
;; 		latin-iso8859-15
;; 		latin-iso8859-16
;; 		cyrillic-iso8859-5
;; 		greek-iso8859-7
;; 		japanese-jisx0208
;; 		japanese-jisx0208-1978
;; 		japanese-jisx0212
;; 		latin-jisx0201
;; 		katakana-jisx0201
;; 		korean-ksc5601
;; 		chinese-big5-1
;; 		chinese-big5-2
;; 		chinese-gb2312
;; 		chinese-sisheng)))
;; 	    ((string-match "ko" (getenv "LANG"))
;; 	     (set-language-environment "Korean")
;; 	     (set-language-unicode-precedence-list
;; 	      '(ascii
;; 		latin-iso8859-1
;; 		latin-iso8859-2
;; 		latin-iso8859-3
;; 		latin-iso8859-4
;; 		latin-iso8859-13
;; 		latin-iso8859-15
;; 		latin-iso8859-16
;; 		cyrillic-iso8859-5
;; 		greek-iso8859-7
;; 		korean-ksc5601
;; 		japanese-jisx0208
;; 		japanese-jisx0208-1978
;; 		japanese-jisx0212
;; 		latin-jisx0201
;; 		katakana-jisx0201
;; 		chinese-big5-1
;; 		chinese-big5-2
;; 		chinese-gb2312
;; 		chinese-sisheng)))
;; 	    ((string-match "lt" (getenv "LANG"))
;; 	     (set-language-environment "Lithuanian"))
;; 	    ((string-match "mt" (getenv "LANG"))
;; 	     (set-language-environment "Maltese"))
;; 	    ((string-match "nb" (getenv "LANG"))
;; 	     (set-language-environment "Norwegian"))
;; 	    ((string-match "nn" (getenv "LANG"))
;; 	     (set-language-environment "Norwegian"))
;; 	    ((string-match "no" (getenv "LANG"))
;; 	     (set-language-environment "Norwegian"))
;; 	    ((string-match "pl" (getenv "LANG"))
;; 	     (set-language-environment "Polish"))
;; 	    ((string-match "pt" (getenv "LANG"))
;; 	     (set-language-environment "Portuguese"))
;; 	    ((string-match "ro" (getenv "LANG"))
;; 	     (set-language-environment "Romanian"))
;; 	    ((string-match "sk" (getenv "LANG"))
;; 	     (set-language-environment "Slovak"))
;; 	    ((string-match "sl" (getenv "LANG"))
;; 	     (set-language-environment "Slovenian"))
;; 	    ((string-match "es" (getenv "LANG"))
;; 	     (set-language-environment "Spanish"))
;; 	    ((string-match "sv" (getenv "LANG"))
;; 	     (set-language-environment "Swedish"))
;; 	    ((string-match "th" (getenv "LANG"))
;; 	     (set-language-environment "Thai-XTIS"))
;; 	    ((string-match "tr" (getenv "LANG"))
;; 	     (set-language-environment "Turkish"))
;; 	    ((string-match "vi" (getenv "LANG"))
;; 	     (set-language-environment "Vietnamese"))
;; 	    (t
;; 	     (set-language-environment "English")))
;;       (setenv "LANG" old-lang)
;;       (set-current-locale old-lang))))

(defun suse-set-coding-systems ()
  (let* ((tmp (shell-command-to-string "locale charmap"))
	 (tmp (substring tmp 0 (string-match "\[ \t\n\]" tmp)))
	 (tmp (downcase tmp)))
    (when (find-coding-system (intern tmp))
      ;; set the coding system priorities:
      ;; (this is also important to make XIM in utf-8 work
      ;; because XEmacs has no variable/function to set the
      ;; coding-system for XIM, it is just autodetected which
      ;; will work correctly only when the coding-system priorities
      ;; are OK.)
      (if (coding-system-category (intern tmp))
	  ;; if coding-system-category is nil the coding-system is
	  ;; no-conversion or undecided and prefer-coding system would
	  ;; fail.
	  (progn (prefer-coding-system (intern tmp))
		 (if (fboundp 'latin-unity-install) (latin-unity-install))))
      (if (emacs-version>= 21 5 6)
	  ;; XEmacs 21.5 apparently renamed this function:
	  (set-default-output-coding-systems (intern tmp))
	(set-default-coding-systems (intern tmp)))
      (set-keyboard-coding-system (intern tmp))
      (set-terminal-coding-system (intern tmp))
      ;; XEmacs 21.5.16 needs this to be able to use non-ASCII file names:
      ;; (according to Aidan, file-name-coding-system is ignored for
      ;; XEmacs >= 21.5.26. One may use
      ;;     (define-coding-system-alias 'file-name 'utf-8)
      ;; instead but even this should not be necessary if
      ;; LC_CTYPE is already an UTF-8 locale).
      (if (and (string-match "XEmacs" emacs-version)
	       (emacs-version>= 21 5 6))
	  (setq file-name-coding-system (intern tmp)))
      ;; without the following line, shell buffers are not by default
      ;; in UTF-8 when running in an UTF-8 locale in XEmacs 21.5.16:
      (setq process-coding-system-alist (cons (cons ".*" (intern tmp)) '()))
      ;; these two lines appearently make no difference, if they
      ;; are used instead of the above process-coding-system-alist,
      ;; shell buffers still have the wrong encoding:
      ;;    (setq default-process-coding-system-read (intern tmp))
      ;;    (setq default-process-coding-system-write (intern tmp))
      ;; and this doesn't seem to work either:
      ;;    (setq default-process-coding-system '(utf-8 . utf-8))
      ;; 
      ;; the following is necessary to enable XEmacs to pass
      ;; command line arguments to external processes in the correct
      ;; encoding. For example this is needed to make
      ;; 'M-x grep' work when searching for UTF-8 strings
      ;; while running in an UTF-8 locale.
      ;; 
      (if (and (string-match "XEmacs" emacs-version)
	       (emacs-version>= 21 5 6))
	  (define-coding-system-alias 'native (intern tmp))))))

(if load-user-init-file-p
  (suse-set-coding-systems))

;; Set input mode
(let ((value (current-input-mode)))
  (set-input-mode (nth 0 value)
		  (nth 1 value)
		  (terminal-coding-system)
		  ;; This quit value is optional
		  (nth 3 value)))

;; Hack to support some important Unicode keysyms which are not yet
;; natively supported in XEmacs:

(defun insert-unicode-keysym ()
  "Assuming the last typed key has an associated keysym of the form
UXXXX, where XXXX is the hexadecimal code point of a Unicode
character, insert that Unicode character at point.  "
  (interactive)
  (let* ((unicode-codepoint
	  (string-to-int 
	   (substring (format "%s" (event-key last-command-event)) 1) 16))
	 (mule-char (unicode-to-char unicode-codepoint)))
    (if mule-char
	(insert mule-char)
      (error 'text-conversion-error 
	     (format "Could not convert U+%X to a Mule character, sorry"
		     unicode-codepoint)))))

(defun suse-global-map-default-binding ()
  "Workaround to make X11 keysyms of the form UXXXX work.
This is a stopgap until proper translation of these keysyms is
integrated into XEmacs"
  
  (interactive)
  (let* ((keysym
	   (format "%s" (event-key last-command-event)))
	 (case-fold-search nil))
    (when (string-match "U[0-9A-F][0-9A-F][0-9A-F][0-9A-F]" keysym)
	  (insert-unicode-keysym)
	  (define-key global-map (intern keysym) 'insert-unicode-keysym))))

;;; (when (equal (console-type) 'x)
;;;   (set-keymap-default-binding global-map 'suse-global-map-default-binding))

;; Hack to support some extra Unicode characters which are not in any
;; legacy charset. This hack is not enough to display the characters
;; correctly (should work with the Xft build of XEmacs) but at least
;; it prevents data loss if files containing these characters are read
;; and saved again.

;; This hack is not needed anymore, something similar has been
;; implemented upstream.
;; Keeping this hack enabled causes problems, for example it often
;; causes error messages when trying to attach .pdf files in Gnus.
;; Therefore I comment it out.
;; Mon Feb 23 12:20:01 2009    <mike.fabian@gmx.de>

;; (make-charset 'suse-private    
;; 	      "Private character set for SUSE"                            
;; 	      '(dimension 2
;; 		chars 96              
;; 		columns 1             
;; 		final ?R ;; Change this--see docs for make-charset        
;; 		long-name "Private charset for some Unicode char support."
;; 		short-name            
;; 		"Suse-Private"))
;; 
;; (defun suse-list-unsupported-codepoints-range (range)
;;   (interactive)
;;   (let ((unsupported nil)
;; 	(i (car range))
;; 	(j (cadr range)))
;;     (while (<= i j)
;;       (if (not (unicode-to-char i))
;; 	  (push i unsupported))
;;       (setq i (1+ i)))
;;     unsupported))
;; 
;; (defun suse-fill-charset (charset codepoint-list)
;;   (interactive)
;;   (let ((n 0))
;;     (dolist (codepoint codepoint-list)
;;       (let ((i (mod n 96))
;; 	    (j (/ n 96)))
;; 	(if (< j 95)
;; 	    (set-unicode-conversion (make-char charset (+ i #x20) (+ j #x20)) codepoint)
;; 	  (message "charset %s is full" charset))
;; 	(setq n (1+ n))))))
;; 
;; (suse-fill-charset
;;  'suse-private
;;  (nconc
;;   (suse-list-unsupported-codepoints-range '(#x0100 #x06FF))
;;   (suse-list-unsupported-codepoints-range '(#x0900 #x11FF))
;;   (suse-list-unsupported-codepoints-range '(#x1E00 #x27FF))
;;   (suse-list-unsupported-codepoints-range '(#x3000 #x33FF))
;;   (suse-list-unsupported-codepoints-range '(#xE800 #xE8FF))
;;   (suse-list-unsupported-codepoints-range '(#xF000 #xF0FF))
;;   (suse-list-unsupported-codepoints-range '(#xFB00 #xFFFF))
;;   ))

(if (and (boundp 'xft-version) (eq window-system 'x))
 (load "suse-xft-init.el" t t))

;;;;;;;;;;
;; the end
