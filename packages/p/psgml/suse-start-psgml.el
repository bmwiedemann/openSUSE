;; You can use this setup in your ~/.emacs resp. ~/.gnu-emacs file.

(eval-after-load "psgml-parse"
	'(modify-syntax-entry ?_ "_" sgml-parser-syntax))

(add-to-list 'load-path "/usr/share/emacs/site-lisp/psgml")
(autoload 'sgml-mode "psgml" "Major mode to edit SGML files." t)
(autoload 'sgml-xpointer "psgml-xpointer" nil t)

;; (autoload 'html-mode "xxml" "Major mode to edit HTML files." t)
(defvar suse-psgml-use-xxml t
  "*Use xxml for fontification of SGML/XML files.")

(autoload 'ke-docbook-mode "ke-docbook")

(add-hook 'sgml-mode-hook
          #'(lambda ()
              ;; (local-unset-key "\C-c\C-c")
              ;; (local-unset-key "\C-c\C-t")
              ;; (define-key sgml-mode-map "\C-c\C-c\C-c" 'sgml-show-context)
              ;; (define-key sgml-mode-map "\C-c\C-x" 'sgml-show-context)
              ;; (define-key sgml-mode-map "\C-c\C-c\C-t" 'sgml-list-valid-tags)
              ;; (modify-face 'highlight "turquoise4" nil nil nil nil nil)
              ;; (modify-face 'italic "grey60" nil nil nil nil nil)
              ;; (modify-face 'bold-italic nil "grey80" nil nil nil nil)
              (auto-fill-mode t)
              (make-variable-buffer-local 'adaptive-fill-regexp)
              (setq adaptive-fill-regexp nil)
              (make-variable-buffer-local 'fill-column)
              (setq fill-column 79)
              ;; (require 'psgml-jade)
              (when suse-psgml-use-xxml
                (autoload 'xxml-mode-routine "xxml")
                (xxml-mode-routine))))

(add-to-list 'auto-mode-alist '("\\.xml\\'" . xml-mode))
(autoload 'xml-mode "psgml" nil t)

;; (defvar suse-psgml-use-psgml-html nil
;;   "*Use psgml-html for editing HTML files.")
;; (when suse-psgml-use-psgml-html
;;   (add-to-list 'auto-mode-alist '("\\.s?html?\\'" . html-mode))
;;   (autoload 'html-mode "psgml-html" "HTML mode." t))

(setq sgml-xml-declaration "/usr/share/sgml/openjade/xml.dcl")
(setq sgml-xml-validate-command
      "SP_CHARSET_FIXED=YES SP_ENCODING=XML onsgmls -wxml -s %s %s"
      sgml-validate-command "onsgmls -s %s %s")

;; Lots of overlays in a buffer is bad news since they have to
;; be relocated on changes, with typically quadratic
;; behaviour.
(setq-default sgml-use-text-properties t)

(setq sgml-markup-faces
      '((start-tag . font-lock-function-name-face) ;; was 7.2: italic
        (end-tag   . font-lock-function-name-face) ;; was 7.2: italic
        (comment   . font-lock-comment-face)       ;; comment declaration
        ;; ignored      - ignored marked section
        (ms-end    . font-lock-constant-face)   ;; marked section start, if not ignored
        (ms-start  . font-lock-constant-face)   ;; marked section end, if not ignored
        (pi 	   . bold)                      ;; processing instruction
        (sgml 	   . highlight)                 ;; SGML declaration
        (doctype   . font-lock-string-face)     ;; doctype declaration
        (entity    . font-lock-reference-face)  ;; general entity reference
        (shortref  . font-lock-builtin-face)    ;; short reference; was 7.2:
                                                ;; font-lock-function-name-face
        ))

(setq sgml-set-face t)
(setq sgml-auto-activate-dtd t)

(setq sgml-system-path '("/usr/share/sgml"
                         ;; "/usr/share/sgml/TEI/dtd"
                         "/usr/share/sgml/ISO_8879:1986")
      sgml-public-map '("%S"
                        "/usr/share/sgml/%o/%c/%d_%v"
			"/usr/share/sgml/%S"
                        "/usr/share/sgml/%o/%c/%d"))

(setq sgml-catalog-files '("CATALOG"
                           "~/sgml/CATALOG"
                           "/etc/sgml/catalog"
                           "/usr/share/sgml/CATALOG")
      sgml-ecat-files '("ECAT" "~/sgml/ECAT" "/usr/share/sgml/ECAT"))

(setq sgml-display-char-list-filename
      "/usr/share/emacs/site-lisp/psgml/iso88591.map")

;; Use onsgmls from opensp/openjade for validation
;; (setq sgml-validate-command "onsgmls -s %s %s")

;; Init tdtd (copied from the tdtd package and a little bit modified
(autoload 'dtd-mode "tdtd" "Major mode for SGML and XML DTDs." t)
(autoload 'dtd-etags "tdtd"
  "Execute etags on FILESPEC and match on DTD-specific regular expressions."
  t)
(autoload 'dtd-grep "tdtd" "Grep for PATTERN in files matching FILESPEC." t)

;; Turn on font lock when in DTD mode
(add-hook 'dtd-mode-hooks 'turn-on-font-lock)

(setq auto-mode-alist
      (append
       (list
	'("\\.dcl$" . dtd-mode)
	'("\\.dec$" . dtd-mode)
	'("\\.dtd$" . dtd-mode)
	'("\\.ele$" . dtd-mode)
	'("\\.ent$" . dtd-mode)
	'("\\.mod$" . dtd-mode))
       auto-mode-alist))

;; To use resize-minibuffer-mode, uncomment this and include in your .emacs:
;;(resize-minibuffer-mode)

;; suse-start-psgml.el ends here
