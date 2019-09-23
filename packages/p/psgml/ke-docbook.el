;; <!-- Keep this comment at the end of the file
;; Local variables:
;; mode: ke-docbook
;; sgml-omittag:nil
;; sgml-shorttag:t
;; sgml-namecase-general:t
;; sgml-general-insert-case:lower
;; sgml-minimize-attributes:nil
;; sgml-always-quote-attributes:nil
;; sgml-indent-step:1
;; sgml-indent-data:nil
;; sgml-parent-document:nil
;; sgml-default-dtd-file:"main.ced"
;; sgml-exposed-tags:nil
;; sgml-local-catalogs:nil
;; sgml-local-ecat-files:nil
;; End:
;; -->

(load "xxml")
(require 'tempo)

(add-hook 'ke-docbook-mode-hook
          '(lambda ()
             (setq xxml-highlight-tag-alist
                   '(("chapter" . ke-docbook-chapter-face)
                     ("section" . ke-docbook-section-face)
                     ("sect1" . ke-docbook-section-face)
                     ("sect2" . ke-docbook-sect2-face))
		   xxml-highlight-recursive-alist
		   '(("title" . xxml-header-1-face)
		     ("subtitle" . xxml-header-3-face))
		   xxml-highlight-initial-alist
		   '(("firstterm" . xxml-emph-1-face)
                     ("emphasis" . italic)
                     ("keycap" . bold)
                     ;; ("filename" . font-lock-constant-face)
                     ("ulink" . xxml-interaction-face)
                     ("link" . xxml-interaction-face)))))

(define-skeleton ke-dbk-varlistentry-skel
  "Insert <varlistentry>."
  nil
>
"<varlistentry>" \n >
" <term>" _ "</term>" \n >
" <listitem>" \n >
"  <para>" \n >
@ "</para>" \n >
" </listitem>" \n >
"</varlistentry>")

(tempo-define-template "varlistentry"
                       '(& > "\
<varlistentry>" n>
"<term>" r "</term>" n>
"<listitem>" n>
"<para>" n
r n
"</para>" n>
"</listitem>" n>
"</varlistentry>" % >))

(require 'tempo)
(global-set-key [C-tab] 'tempo-forward-mark)
(global-set-key [S-C-tab] 'tempo-backward-mark)
;; for now, these are needed:
(global-set-key [S-iso-lefttab] 'tempo-backward-mark)
(global-set-key [C-S-iso-lefttab] 'tempo-backward-mark)

(tempo-define-template "emphasis"
		       '("<emphasis>" r "</emphasis>" p))
(tempo-define-template "filename"
		       '("<filename>" r "</filename>" p))
(tempo-define-template "function"
		       '((if (y-or-n-p "Emacs Lisp? ")
                             "<function role=\"elisp\">"
                           "<function>") r "</function>"
                             p))
(tempo-define-template "wordasword"
		       '("<wordasword>" r "</wordasword>" p))

(tempo-define-template "para"
		       '(& "<para>" > n r n "</para>" > p))

(tempo-define-template "programlisting"
		       '(& "\
<programlisting format=\"linespecific\">
<![ CDATA [" n p n
"]]>
</programlisting>" n))

(tempo-define-template "step"
      '(& "<step>" > n "<para>" > r "</para>" > n "</step>" > p))

(define-derived-mode ke-docbook-mode sgml-mode "DocBk"
  "Major mode for editing DocBook files.
Run `ke-docbook-mode-hook'.\n
\\{ke-spec-mode-map}"
;;   (set (make-local-variable 'font-lock-defaults)
;;       '(ke-spec-font-lock-keywords nil nil))
;;   (set (make-local-variable 'ke-spec-pkg)
;;        (ke-spec-pkg-name))
;;   (set (make-local-variable 'sh-shell-file)
;;        "/bin/sh")             ; rpm default
;;   (easy-menu-add ke-spec-menu)
;;   (if ke-spec-build-new-buffer
;;       (ke-spec-insert-new-buffer-strings))
  (run-hooks 'ke-docbook-mode-hook))

(define-key ke-docbook-mode-map "\C-cp" 'tempo-template-para)
(define-key ke-docbook-mode-map "\C-c\C-ce" 'tempo-template-emphasis)
(define-key ke-docbook-mode-map "\C-c\C-cf" 'tempo-template-filename)
(define-key ke-docbook-mode-map "\C-c\C-cp" 'tempo-template-programlisting)
(define-key ke-docbook-mode-map "\C-c\C-cs" 'tempo-template-step)

(easy-menu-define ke-docbook-menu ke-docbook-mode-map "DocBook Menu"
                  '("DocBk"
                    ["Emphasis" tempo-template-emphasis t]
                    ["Filename" tempo-template-filename t]
                    ["Function" tempo-template-function t]
                    ["WordAsWord" tempo-template-wordasword t]
                    "---"
                    ["Para" tempo-template-para t]
                    ["ProgramListing" tempo-template-programlisting t]
                    ["Step" tempo-template-step t]
                    ))

(defvar ke-docbook-chapter-face nil
  "Face used for chapter tag.")
(copy-face 'xxml-rug-face 'ke-docbook-chapter-face)

(defvar ke-docbook-section-face nil
  "Face used for section and sect1 tag.")
(copy-face 'xxml-sparkle-face 'ke-docbook-section-face)

(defvar ke-docbook-sect2-face nil
  "Face used for sect2 tag.")
(copy-face 'xxml-sparkle-face 'ke-docbook-sect2-face)
(set-face-background 'ke-docbook-sect2-face "orange")

(provide 'ke-docbook)

;; eof
