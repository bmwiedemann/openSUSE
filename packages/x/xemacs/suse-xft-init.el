;;; -*- mode: emacs-lisp -*-

;;; Fri Jul 13 20:43:53 2007   Mike FABIAN  <mfabian@suse.de>

(setq xft-debug-level 0) ;; default is 1. Set to 0 to suppress all warnings

(setq suse-xft-lang-tags
      (list "ar"
	    "en"
	    "de"
	    "he"
	    "ko"
	    "zh-TW"
	    "zh-CN"
	    "ja"
	    "th"
	    "vi"))
  
(mapcar (lambda (x) (define-specifier-tag (intern x))) suse-xft-lang-tags)
  
(defun suse-xft-find-font-for-tag (tag)
  "uses fc-match to find a suitable font for tag"
  (let* ((fc-match-result (shell-command-to-string
			   (format "fc-match monospace:lang=%s" tag)))
	 (family (nth 1 (split-string fc-match-result "\"")))
	 (style (nth 3 (split-string fc-match-result "\""))))
    (format "%s:style=%s" family style)))


(defun suse-xft-make-fonts-alist (tags)
  "returns an alist of with the tags as keys and suitable fonts as values"
  (let ((fonts-alist nil))
    (mapcar
     (lambda (x)
       (setq fonts-alist
	(cons (cons x (suse-xft-find-font-for-tag x))
	      fonts-alist)))
     tags)
    (reverse fonts-alist)))

(setq suse-xft-fonts-alist (suse-xft-make-fonts-alist suse-xft-lang-tags))

;; tune the defaults returned by fc-match according to taste:
;; For example, I prefer "DejaVu Sans Mono" as the standard
;; font even if another font is the default for "monospace"
;; because "DejaVu Sans Mono" has a lot more special symbols
;; than most other monospaced fonts.

(if (not (equal "" (shell-command-to-string "fc-list \"DejaVu Sans Mono\"")))
    (setf (cdr (assoc "en" suse-xft-fonts-alist)) "DejaVu Sans Mono"))

(defun suse-xft-set-all-faces (size)
  "tries to set reasonable fonts for all faces"
  (interactive "nnew size for all faces: ")
  (setq suse-xft-current-size size)
  (when (console-on-window-system-p)
    (mapcar 
     (lambda (face)
       (progn
	 ;; first set the English font as the standard font for all faces
	 (set-face-font face
			(format "%s:size=%d"
				(cdr (assoc "en" suse-xft-fonts-alist))
				size)
			'global
			nil
			'remove-all)
	 ;; then append the fonts for the other languages
	 (mapcar
	  (lambda (tag)
	    (set-face-font face
			   (format "%s:size=%d"
				   (cdr (assoc tag suse-xft-fonts-alist))
				   size)
			   'global
			   (list (intern tag))
			   'remove-tag-set-append))
	  suse-xft-lang-tags)
	 (if (string-match "bold-italic" (symbol-name face))
	     (make-face-bold-italic face)
	   (if (string-match "bold" (symbol-name face))
	       (make-face-bold face))
	   (if (string-match "italic" (symbol-name face))
	       (make-face-italic face)))
	 (when (fboundp 'custom-face-get-spec)
	   (if (and (eq t (plist-get (cadr (assoc t (custom-face-get-spec face))) :bold))
		    (eq t (plist-get (cadr (assoc t (custom-face-get-spec face))) :italic)))
	       (make-face-bold-italic face)
	     (if (and (eq 'bold (plist-get (cadr (assoc t (custom-face-get-spec face))) :weight))
		      (eq 'italic (plist-get (cadr (assoc t (custom-face-get-spec face))) :slant)))
		 (make-face-bold-italic face)
	       (if (eq 'bold (plist-get (cadr (assoc t (custom-face-get-spec face))) :weight))
		   (make-face-bold face))
	       (if (eq 'italic (plist-get (cadr (assoc t (custom-face-get-spec face))) :slant))
		   (make-face-italic face))
	       (if (eq t (plist-get (cadr (assoc t (custom-face-get-spec face))) :bold))
		   (make-face-bold face))
	       (if (eq t (plist-get (cadr (assoc t (custom-face-get-spec face))) :italic))
		   (make-face-italic face)))))
	 ))
     (face-list))))

(defun suse-xft-set-size (size)
  (interactive "nset all fonts to point-size: ")
  (setq suse-xft-current-size size)
  (if (> 1 suse-xft-current-size)
      (setq suse-xft-current-size 1))
  (suse-xft-set-all-faces suse-xft-current-size))

(defun suse-xft-change-size (delta)
  (interactive "nsize change in point (may be negative): ")
  (setq suse-xft-current-size (+ delta suse-xft-current-size))
  (if (> 1 suse-xft-current-size)
      (setq suse-xft-current-size 1))
  (suse-xft-set-all-faces suse-xft-current-size))

(setq suse-xft-current-size 12)

(suse-xft-set-all-faces suse-xft-current-size)



