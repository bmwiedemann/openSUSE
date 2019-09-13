;;; psgml-html.el --- HTML mode in conjunction with PSGML

;; Copyright (C) 1994 Nelson Minar.
;; Copyright (C) 1995 Nelson Minar and Ulrik Dickow.
;; Copyright (C) 1996 Ben Wing.

;; This file is part of XEmacs.

;; XEmacs is free software; you can redistribute it and/or modify it
;; under the terms of the GNU General Public License as published by
;; the Free Software Foundation; either version 2, or (at your option)
;; any later version.

;; XEmacs is distributed in the hope that it will be useful, but
;; WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
;; General Public License for more details.

;; You should have received a copy of the GNU General Public License
;; along with XEmacs; see the file COPYING.  If not, write to the Free
;; Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.

;;; Synched up with: FSF 19.30.

;;; Author: Ben Wing.

;;; Commentary:

; Parts were taken from html-helper-mode and from code by Alastair Burt.

; If you'd like to use the hm--html-minor-mode together with this
; mode, you have to put the following line to your ~/.emacs:
;	(add-hook 'html-mode-hook 'hm--html-minor-mode)

;; Modified for Debian: use (string-match "XEmacs" emacs-version)
;; instead of running-xemacs
;;; Code:

(defvar html-auto-sgml-entity-conversion nil
  "*Control automatic sgml entity to ISO-8859-1 conversion")

(provide 'psgml-html)
(require 'psgml)
(require 'derived)
(when html-auto-sgml-entity-conversion
  (require 'iso-sgml))
(require 'tempo)			;essential part of html-helper-mode

(eval-when-compile
  (require 'browse-url)
  (require 'font-lock)
  (require 'imenu))

;;{{{ user variables

(defgroup html nil
  "HyperText Markup Language"
  :group 'sgml)

(defgroup psgml-html nil
  "HTML mode in conjunction with PSGML"
  :tag "Psgml Html"
  :prefix "psgml-html-"
  :group 'html
  :group 'psgml)

;;;; Modified for Debian: now accomodates Emacs as well
;; Set this to be whatever signature you want on the bottom of your pages.
(defcustom psgml-html-address-string
  (cond
   ((string-match "XEmacs" emacs-version) ; XEmacs/Lucid
    (concat "<a href=\"mailto:" (user-mail-address) "\">"
	    (user-full-name) "</a>"))
   (t
    (concat "<a href=\"mailto:" user-mail-address "\">"
	    user-full-name "</a>")))
    "*The default author string of each file."
    :type 'string
    :group 'psgml-html)

(defcustom psgml-html-htmldtd-version "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">\n"
  "*Version of HTML DTD you're using."
  :type 'string
  :group 'psgml-html)

(defcustom psgml-html-do-write-file-hooks t
  "*If not nil, then modify `local-write-file-hooks' to do timestamps."
  :type 'boolean
  :group 'psgml-html)

(defcustom psgml-html-build-new-buffer t
  "*If not nil, then insert `psgml-html-new-buffer-strings' for new buffers."
  :type 'boolean
  :group 'psgml-html)

(defcustom psgml-html-timestamp-hook 'psgml-html-default-insert-timestamp
  "*Hook called for timestamp insertion.
Override this for your own timestamp styles."
  :type 'hook
  :group 'psgml-html)

;; strings you might want to change

(defcustom psgml-html-new-buffer-template
  '(psgml-html-htmldtd-version
    "<html>\n"
    "  <head>\n"
    "    <title>" (p "Document Title: " title) "</title>\n"
    "  </head>\n"
    "\n"
    "  <body>\n"
    "    <h1>" (s title) "</h1>\n\n"
    p
    "\n\n    <hr>\n"
    "    <address>" psgml-html-address-string "</address>\n"
    (psgml-html-return-created-string)
    psgml-html-timestamp-start
    psgml-html-timestamp-end
    "\n  </body>\n</html>\n")
  "*Template for new buffers.
Inserted by `psgml-html-insert-new-buffer-strings' if
`psgml-html-build-new-buffer' is set to t"
  :type 'sexp
  :group 'psgml-html)

(defcustom psgml-html-timestamp-start "<!-- hhmts start -->\n"
  "*Start delimiter for timestamps.
Everything between `psgml-html-timestamp-start' and
`psgml-html-timestamp-end' will be deleted and replaced with the output
of the functions `psgml-html-timestamp-hook' if
`psgml-html-do-write-file-hooks' is t"
  :type 'string
  :group 'psgml-html)

(defcustom psgml-html-timestamp-end "<!-- hhmts end -->"
  "*End delimiter for timestamps.
Everything between `psgml-html-timestamp-start' and
`psgml-html-timestamp-end' will be deleted and replaced with the output
of the function `psgml-html-insert-timestamp' if
`psgml-html-do-write-file-hooks' is t"
  :type 'string
  :group 'psgml-html)

;; control over what types of tags to load. By default, we load all the
;; ones we know of.

(defcustom psgml-html-types-to-install
  '(anchor header logical phys list textel entity image head form table
	   special)
  "*List of tag types to install when psgml-html-mode is first loaded.
If you want to not install some type of tag, override this variable.
Order is significant: menus go in this order."
  :type '(repeat symbol)
  :group 'psgml-html)

(defcustom psgml-html-use-expert-menu nil
  "*If not nil, then use the full HTML menu."
  :type 'boolean
  :group 'psgml-html)

(defcustom psgml-html-user-menu nil
  "*Extra items to put in the HTML expert menu.
The value of this symbol is appended to the beginning of the expert
menu that is handed off to easymenu for definition. It should be a
list of vectors or lists which themselves are vectors (for submenus)."
  :type 'sexp
  :group 'psgml-html)

;;}}} end of user variables
;;{{{ type based keymap and menu variable and function setup

;; psgml-html-mode has a concept of "type" of tags. Each type is a
;; list of tags that all go together in one keymap and one menu.
;; Types can be added to the system after psgml-html has been loaded,
;; briefly by doing psgml-html-add-type-to-alist, then
;; psgml-html-install-type, then psgml-html-add-tag (for each tag)
;; then psgml-html-rebuild-menu. See the mode documentation for more detail.

(defconst psgml-html-type-alist nil
  "Alist: type of tag -> keymap, keybinding, menu, menu string.
Add to this with `psgml-html-add-type-to-alist'.")

;;{{{ accessor functions for psgml-html-type-alist
(tempo-define-template "html-skeleton" psgml-html-new-buffer-template
                       nil
                       "Insert a skeleton for a HTML document")

(defun psgml-html-keymap-for (type)
  "Accessor function for alist: for type, return keymap or nil"
  (nth 0 (cdr-safe (assq type psgml-html-type-alist))))

(defun psgml-html-key-for (type)
  "Accessor function for alist: for type, return keybinding or nil"
  (nth 1 (cdr-safe (assq type psgml-html-type-alist))))

(defun psgml-html-menu-for (type)
  "Accessor function for alist: for type, return menu or nil"
  (nth 2 (cdr-safe (assq type psgml-html-type-alist))))

(defun psgml-html-menu-string-for (type)
  "Accessor function for alist: for type, return menustring or nil"
  (nth 3 (cdr-safe (assq type psgml-html-type-alist))))

(defun psgml-html-normalized-menu-for (type)
  "Helper function for building menus from submenus: add on string to menu."
  (cons (psgml-html-menu-string-for type)
	(eval (psgml-html-menu-for type))))

;;}}}

(define-derived-mode html-mode sgml-mode "HTML"
  "Major mode for editing HTML documents.
This is based on PSGML mode, and has a sophisticated SGML parser in it.
It knows how to properly indent HTML/SGML documents, and it can do
  a form of document validation (use \\[sgml-next-trouble-spot] to find
  the next error in your document).
Commands beginning with C-z insert various types of HTML tags
  (prompting for the required information); to iconify or suspend,
  use C-z C-z.
To literally insert special characters such as < and &, use C-c followed
  by the character.
Use \\[sgml-insert-end-tag] to insert the proper closing tag.
Use \\[sgml-edit-attributes] to edit the attributes for a tag.
Use \\[sgml-show-context] to show the current HTML context.

More specifically:
\\{html-mode-map}
"
  (make-local-variable 'sgml-declaration)
  (make-local-variable 'sgml-default-doctype-name)
  (if (or
       (not (boundp 'sgml-custom-dtd))
       (not sgml-custom-dtd))
      (setq 
       sgml-custom-dtd
       '(
	 ( "HTML 4.01 Strict"
	   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\">" )
	 ( "HTML 4.01 Transitional"
	   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">")
	 ( "HTML 4.01 Frameset"
	   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Frameset//EN\">" )
	 )
       ))


  (setq sgml-declaration             (expand-file-name "html.decl"
						       sgml-data-directory)
	sgml-default-doctype-name    "HTML"
	sgml-always-quote-attributes t
	sgml-indent-step             2
	sgml-indent-data	     t
	sgml-inhibit-indent-tags     '("pre")
	sgml-minimize-attributes     nil
	sgml-omittag                 t
	sgml-shorttag                t)

	;; Added for Debian
	;; menus for creating new documents

  ;; font-lock setup for various emacsen: XEmacs, Emacs 19.29+, Emacs <19.29.
  ;; By Ulrik Dickow <dickow@nbi.dk>.  (Last update: 05-Sep-1995).
  (cond	((string-match "XEmacs" emacs-version) ; XEmacs/Lucid
	 (put major-mode 'font-lock-keywords-case-fold-search t))
	;; XEmacs (19.13, at least) guesses the rest correctly.
	;; If any older XEmacsen don't, then tell me.
	;;
	((string-lessp "19.28.89" emacs-version) ; Emacs 19.29 and later
	 (make-local-variable 'font-lock-defaults)
	 (setq font-lock-defaults '(html-font-lock-keywords t t)))
	;;
	(t ; Emacs 19.28 and older
	 (make-local-variable 'font-lock-keywords-case-fold-search)
	 (make-local-variable 'font-lock-keywords)
	 (make-local-variable 'font-lock-no-comments)
	 (setq font-lock-keywords-case-fold-search t)
	 (setq font-lock-keywords html-font-lock-keywords)
	 (setq font-lock-no-comments t)))

  (if psgml-html-do-write-file-hooks
      (add-hook 'local-write-file-hooks 'psgml-html-update-timestamp))

  (if (and psgml-html-build-new-buffer (zerop (buffer-size)))
      (psgml-html-insert-new-buffer-strings))

  (set (make-local-variable 'sgml-custom-markup)
       '(("<A>" "<A HREF=\"\">\r</a>")))

  ;; Set up the syntax table.
  (modify-syntax-entry ?< "(>" html-mode-syntax-table)
  (modify-syntax-entry ?> ")<" html-mode-syntax-table)
  (modify-syntax-entry ?\" ".   " html-mode-syntax-table)
  (modify-syntax-entry ?\\ ".   " html-mode-syntax-table)
  (modify-syntax-entry ?'  "w   " html-mode-syntax-table)

  (tempo-use-tag-list 'psgml-html-tempo-tags psgml-html-completion-finder)
  (setq imenu-create-index-function 'psgml-html-imenu-index)
  (setq imenu-sort-function nil) ; sorting the menu defeats the purpose

  ; sigh ...  need to call this now to get things working.
  (sgml-build-custom-menus)
  ;; (add-submenu nil sgml-html-menu "SGML")
  (setq sgml-menu-name "HTML")
  (easy-menu-add sgml-html-menu)
  (psgml-html-rebuild-menu)
  (if (string-match "XEmacs" emacs-version)
      (unless (featurep 'infodock)
	(delete-menu-item '("SGML")))))


(defvar psgml-html-imenu-regexp
  "\\s-*<h\\([1-9]\\)[^\n<>]*>\\(<[^\n<>]*>\\)*\\s-*\\([^\n<>]*\\)"
  "*A regular expression matching a head line to be added to the menu.
The first `match-string' should be a number from 1-9.
The second `match-string' matches extra tags and is ignored.
The third `match-string' will be the used in the menu.")

;; Make an index for imenu
(defun psgml-html-imenu-index ()
  "Return an table of contents for an html buffer for use with Imenu."
  (let ((space ?\ ) ; a char
	(toc-index '())
	toc-str)
    (save-excursion
      (goto-char (point-min))
      (while (re-search-forward psgml-html-imenu-regexp nil t)
	(setq toc-str
	      (concat
	       (make-string
		(* 2 (- (string-to-number (match-string 1)) 1))
		space)
	       (match-string 3)))
	(beginning-of-line)
	(setq toc-index (cons (cons toc-str (point)) toc-index))
	(end-of-line)))
    (nreverse toc-index)))

(defun psgml-html-add-type-to-alist (type)
  "Add a type specification to the alist.
The spec goes (type . (keymap-symbol keyprefix menu-symbol menu-string)).
See code for an example."
  (setq psgml-html-type-alist (cons type psgml-html-type-alist)))

;; Here are the types provided by psgml-html-mode.
(mapcar 'psgml-html-add-type-to-alist
  '((entity  . (nil nil psgml-html-entity-menu "Insert Character Entities"))
    (textel  . (nil nil psgml-html-textel-menu "Insert Text Elements"))
    (head    . (psgml-html-head-map "\C-zw" psgml-html-head-menu "Insert Structural Elements"))
    (header  . (psgml-html-base-map "\C-z" psgml-html-header-menu "Insert Headers"))
    (anchor  . (psgml-html-base-map "\C-z" psgml-html-anchor-menu "Insert Hyperlinks"))
    (logical . (psgml-html-base-map "\C-z" psgml-html-logical-menu "Insert Logical Styles"))
    (phys    . (psgml-html-base-map "\C-z" psgml-html-phys-menu "Insert Physical Styles"))
    (list    . (psgml-html-list-map "\C-zl" psgml-html-list-menu "Insert List Elements"))
    (form    . (psgml-html-form-map "\C-zf" psgml-html-form-menu "Insert Form Elements"))
    (table   . (psgml-html-table-map "\C-zt" psgml-html-table-menu "Insert Table Elements"))
    (image   . (psgml-html-image-map "\C-zm" psgml-html-image-menu "Insert Inlined Images"))
    (special . (psgml-html-base-map "\C-z" psgml-html-special-menu "Insert Specials"))))

;; Once psgml-html-mode is aware of a type, it can then install the
;; type: arrange for keybindings, menus, etc.

(defconst psgml-html-installed-types nil
  "The types that have been installed (used when building menus).
There is no support for removing a type once it has been installed.")

(defun psgml-html-install-type (type)
  "Install a new tag type: add it to the keymap, menu structures, etc.
For this to work, the type must first have been added to the list of types
with psgml-html-add-type-to-alist."
  (setq psgml-html-installed-types (cons type psgml-html-installed-types))
  (let ((keymap (psgml-html-keymap-for type))
	(key (psgml-html-key-for type))
	(menu (psgml-html-menu-for type))
	(menu-string (psgml-html-menu-string-for type)))
    (and key
	 (progn
	   (set keymap nil)
	   (define-prefix-command keymap)
	   (define-key html-mode-map key keymap)))
    (and menu
	 (progn
	   (set menu nil)))))

;; install the default types.
(mapcar 'psgml-html-install-type psgml-html-types-to-install)

;;}}}

;;{{{ psgml-html-add-tag function for building basic tags

(defvar psgml-html-tempo-tags nil
  "List of tags used in completion.")

;; this while loop is awfully Cish
;; isn't there an emacs lisp function to do this?
(defun psgml-html-string-to-symbol (input-string)
  "Given a string, downcase it and replace spaces with -.
We use this to turn menu entries into good symbols for functions.
It's not entirely successful, but fortunately emacs lisp is forgiving."
  (let* ((s (downcase input-string))
	 (l (1- (length s))))
    (while (>= l 0)
      (if (char-equal (aref s l) ?\ )
	  (aset s l ?\-))
      (setq l (1- l)))
    (concat "html-" s)))


(defun psgml-html-add-tag (l)
  "Add a new tag to psgml-html-mode.
Builds a tempo-template for the tag and puts it into the
appropriate keymap if a key is requested. Format:
`(psgml-html-add-tag '(type keybinding completion-tag menu-name template doc)'"
  (let* ((type (car l))
	 (keymap (psgml-html-keymap-for type))
	 (menu (psgml-html-menu-for type))
	 (key (nth 1 l))
	 (completer (nth 2 l))
	 (name (nth 3 l))
	 (tag (nth 4 l))
	 (doc (nth 5 l))
	 (command (tempo-define-template (psgml-html-string-to-symbol name)
					 tag completer doc
					 'psgml-html-tempo-tags)))

    (if (null (memq type psgml-html-installed-types))    ;type loaded?
	t                                                 ;no, do nothing.
      (if (stringp key)			                  ;bind key somewhere?
	  (if keymap			                  ;special keymap?
	      (define-key (eval keymap) key command)      ;t:   bind to prefix
	    (define-key html-mode-map key command))	  ;nil: bind to global
	t)
      (if menu				                  ;is there a menu?
	  (set menu			                  ;good, cons it in
	       (cons (vector name command t) (eval menu))))
      )))

;;}}}

;;{{{ most of the HTML tags

;; These tags are an attempt to be HTML 3.2 compliant
;; For reference see <URL:http://www.w3.org/TR/REC-html32.html>

;; order here is significant: within a tag type, menus and mode help
;; go in the reverse order of what you see here. Sorry about that, it's
;; not easy to fix.

(mapcar
 'psgml-html-add-tag
 '(
   ;;entities
   (entity  "\C-c#"   "&#"              "Ascii Code"     ("&#" (r "Ascii: ") ";"))
   (entity  "\C-c\""  "&quot;"          "Quotation mark" ("&quot;"))
   (entity  "\C-c$"   "&reg;"           "Registered"     ("&reg;"))
   (entity  "\C-c@"   "&copy;"          "Copyright"      ("&copy;"))
   (entity  "\C-c-"   "&shy;"           "Soft Hyphen"    ("&shy;"))
   (entity  "\C-c "   "&nbsp;"		"Nonbreaking Space" ("&nbsp;"))
   (entity  "\C-c&"   "&amp;"		"Ampersand"	 ("&amp;"))
   (entity  "\C-c>"   "&gt;"	  	"Greater Than"   ("&gt;"))
   (entity  "\C-c<"   "&lt;"		"Less Than"	 ("&lt;"))

   ;; logical styles
   (logical "v"       "<div"            "Text Division"  ("<div align=\"" (r "Alignment: ") "\">" (r "Text: ") "</div>"))
   (logical "n"       "<center>"        "Center"         ("<center>" (r "Text: ") "</center>"))
   (logical "q"       "<blockquote>"	"Blockquote"     ("<blockquote>" (r "Quote: ") "</blockquote>"))
   (logical "c"       "<code>"		"Code"           ("<code>" (r "Code: ") "</code>"))
   (logical "x"       "<samp>"		"Sample"         ("<samp>" (r "Sample code") "</samp>"))
   (logical "r"       "<cite>"		"Citation"       ("<cite>" (r "Citation: ") "</cite>"))
   (logical "k"       "<kbd>"		"Keyboard Input" ("<kbd>" (r "Keyboard: ") "</kbd>"))
   (logical "v"       "<var>"		"Variable"       ("<var>" (r "Variable: ") "</var>"))
   (logical "d"       "<dfn>"		"Definition"     ("<dfn>" (r "Definition: ") "</dfn>"))
   (logical "a"	      "<address>"	"Address"	 ("<address>" r "</address>"))
   (logical "e"       "<em>"		"Emphasized"     ("<em>" (r "Text: ") "</em>"))
   (logical "s"       "<strong>"	"Strong"         ("<strong>" (r "Text: ") "</strong>"))
   (logical "p"       "<pre>"		"Preformatted"   ("<pre>" (r "Text: ") "</pre>"))

   ;;physical styles
   (phys    "p"       "<sup>"           "Superscript"    ("<sup>" (r "Text: ") "</sup>"))
   (phys    "u"       "<sub>"           "Subscript"      ("<sub>" (r "Text: ") "</sub>"))
   (phys    "s"       "<small>"         "Small"          ("<small>" (r "Text: ") "</small>"))
   (phys    "g"       "<big>"           "Big"            ("<big>" (r "Text: ") "</big>"))
   (phys    "-"       "<strike>"	"Strikethru"     ("<strike>" (r "Text: ") "</strike>"))
   (phys    "u"       "<u>"		"Underline"      ("<u>" (r "Text: ") "</u>"))
   (phys    "o"       "<i>"		"Italic"         ("<i>" (r "Text: ") "</i>"))
   (phys    "b"	      "<b>"    		"Bold"           ("<b>" (r "Text: ") "</b>"))
   (phys    "t"       "<tt>"		"Fixed"          ("<tt>" (r "Text: ") "</tt>"))

   ;;headers
   (header  "6"       "<h6>"		"Header 6"       ("<h6>" (r "Header: ") "</h6>"))
   (header  "5"       "<h5>"		"Header 5"       ("<h5>" (r "Header: ") "</h5>"))
   (header  "4"       "<h4>"		"Header 4"       ("<h4>" (r "Header: ") "</h4>"))
   (header  "3"       "<h3>"		"Header 3"       ("<h3>" (r "Header: ") "</h3>"))
   (header  "2"       "<h2>"		"Header 2"       ("<h2>" (r "Header: ") "</h2>"))
   (header  "1"	      "<h1>"     	"Header 1"       ("<h1>" (r "Header: ") "</h1>"))

   ;; forms
   (form    "o"       "<option>"        "Option"         (& "<option>" > ))
   (form    "v"       "<option value"   "Option with Value"  (& "<option value=\"" (r "Value: ") "\">" >))
   (form    "s"       "<select"		"Selections"	 ("<select name=\"" (p "Name: ") "\">\n<option>" > "\n</select>")"<select")
   (form    "z"	      "<input"		"Reset Form"     ("<input type=\"RESET\" value=\"" (p "Reset button text: ") "\">"))
   (form    "b"	      "<input"		"Submit Form"    ("<input type=\"SUBMIT\" value=\"" (p "Submit button text: ") "\">"))
   (form    "i"	      "<input"		"Image Field"    ("<input type=\"IMAGE\" name=\"" (p "Name: ") "\" src=\"" (p "Image URL: ") "\">"))
   (form    "h"       "<input"          "Hidden Field"   ("<input type=\"HIDDEN\" name=\"" (p "Name: ") "\" value=\"" (p "Value: ") "\">"))
   (form    "p"	      "<textarea"	"Text Area"	 ("<textarea name=\"" (p "Name: ") "\" rows=\"" (p "Rows: ") "\" cols=\"" (p "Columns: ") "\">" r "</textarea>"))
   (form    "c"	      "<input"		"Checkbox"   	 ("<input type=\"CHECKBOX\" name=\"" (p "Name: ") "\">"))
   (form    "r"	      "<input"		"Radiobutton"    ("<input type=\"RADIO\" name=\"" (p "Name: ") "\">"))
   (form    "t"	      "<input"		"Text Field"	 ("<input type=\"TEXT\" name=\"" (p "Name: ") "\" size=\"" (p "Size: ") "\">"))
   (form    "f"	      "<form"           "Form"		 ("<form action=\"" (p "Action: ") "\" method=\"" (p "Method: ") "\">\n</form>\n"))

   ;;tables
   (table   "d"       "<td>"            "Data cell"      ("<td>"))
   (table   "h"       "<th>"            "Header"         ("<th>"))
   (table   "r"       "<tr>"            "Row"            ("<tr>"))
   (table   "t"       "<table>"         "Table"          ("<table>\n<tr>\n</table>\n"))

   ;;lists
   (list    "t"       "<dt>"            "Definition Item" (& "<dt>" > (p "Term: ") "\n<dd>" > (r "Definition: ")))
   (list    "l"       "<li>"            "List Item"      (& "<li>" > (r "Item: ")))
   (list    "r"	      "<dir>"		"DirectoryList"  (& "<dir>" > "\n<li>" > (r "Item: ") "\n</dir>" >))
   (list    "m"	      "<menu>"		"Menu List"	 (& "<menu>" > "\n<li>" > (r "Item: ") "\n</menu>" >))
   (list    "o"	      "<ol>"		"Ordered List"   (& "<ol>" > "\n<li>" > (r "Item: ") "\n</ol>" >))
   (list    "d"	      "<dl>"		"Definition List" (& "<dl>" > "\n<dt>" > (p "Term: ") "\n<dd>" > (r "Definition: ") "\n</dl>" >))
   (list    "u"	      "<ul>"		"Unordered List" (& "<ul>" > "\n<li>" > (r "Item: ") "\n</ul>" >))

   ;;anchors
   (anchor  "n"	      "<a name="	"Link Target"	 ("<a name=\"" (p "Anchor name: ") "\">" (r "Anchor text: ") "</a>"))
   (anchor  "h"	      "<a href="        "Hyperlink"      ("<a href=\"" (p "URL: ") "\">" (r "Anchor text: ") "</a>"))

   ;;graphics
   (image   "m"       "<map name="      "Image map"      ("<map name=\"" (r "Map name: ") "\">"))
   (image   "a"       nil               "Aligned Image"	 ("<img align=\"" (r "Alignment: ") "\" src=\"" (r "Image URL: ") "\">"))
   (image   "i"       "<img src="	"Image"		 ("<img src=\"" (r "Image URL: ") "\">"))
   (image   "e"       "<img align="     "Aligned Image With Alt. Text"	("<img align=\"" (r "Alignment: ") "\" src=\"" (r "Image URL: ") "\" alt=\"" (r "Text URL: ") "\">"))
   (image   "t"       "<img alt="	"Image With Alternate Text"	("<img alt=\"" (r "Text URL: ") "\" src=\"" (r "Image URL: ") "\">"))

   ;;specials
   (special "a"       "<applet code="   "Applet"         ("<applet code=\"" (r "Applet class: ") "\" width=" (r "Applet width: ") " height=" (r "Applet height: ") ">"))
   (special "b"       "<basefont size=" "Base font size" ("<basefont size=" (r "Font size: ") ">"))
   (special "c"       "<font color="    "Font color"     ("<font color=\"" (r "Color: ") "\">" (r "Text: ") "</font>"))
   (special "s"       "<font size="     "Font size"      ("<font size=" (r "Font size: ") ">" (r "Text: ") "</font>"))

   ;;text elements
   (textel  "\C-c="   nil		"Horizontal Line" (& "<hr>\n"))
   (textel  "\C-c\C-m" nil		"Line Break"	 ("<br>\n"))
   (textel  "\e\C-m"  nil		"Paragraph"	 ("<p>" (progn (sgml-indent-line) nil) "\n"))

   ;;head elements
   (head    "H"       "<head>"          "Head"           ("<head>\n" "</head>\n"))
   (head    "B"       "<body>"          "Body"           ("<body>\n" "</body>\n"))
   (head    "i"	      "<isindex>"	"Isindex"        ("<isindex>\n"))
   (head    "n"	      "<nextid>"	"Nextid"         ("<nextid>\n"))
   (head    "h"       "<meta http-equiv=" "HTTP Equivalent" ("<meta http-equiv=\"" (p "Equivalent: ") "\" content=\"" (r "Content: ") "\">\n"))
   (head    "m"       "<meta name="     "Meta Name"      ("<meta name=\"" (p "Name: ") "\" content=\"" (r "Content: ") "\">\n"))
   (head    "l"	      "<link"		"Link"           ("<link href=\"" p "\">"))
   (head    "s"       "<script>"        "Script"         ("<script>"))
   (head    "y"       "<style>"         "Style"          ("<style>"))
   (head    "b"       "<base"		"Base"           ("<base href=\"" r "\">"))
   (head    "t"	      "<title>"		"Title"          ("<title>" (r "Document title: ") "</title>"))
   ))

;;}}}
;;{{{ psgml-html-smart-insert-item

;; there are two different kinds of items in HTML - those in regular
;; lists <li> and those in dictionaries <dt>..<dd>
;; This command will insert the appropriate one depending on context.

(defun psgml-html-smart-insert-item (&optional arg)
  "Insert a new item, either in a regular list or a dictionary."
  (interactive "*P")
  (let ((case-fold-search t))
    (if
        (save-excursion
          (re-search-backward "<li>\\|<dt>\\|<ul>\\|<ol>\\|<dd>\\|<menu>\\|<dir>\\|<dl>" nil t)
          (looking-at "<dt>\\|<dl>\\|<dd>"))
        (tempo-template-html-definition-item arg)
      (tempo-template-html-list-item arg))))

;; special keybindings in the prefix maps (not in the list of tags)
(and (boundp 'psgml-html-base-map)
     (define-key psgml-html-base-map "i" 'psgml-html-smart-insert-item))

(if (eq window-system 'x)
    (define-key html-mode-map "\C-z\C-z" 'iconify-or-deiconify-frame)
  (define-key html-mode-map "\C-z\C-z" 'suspend-emacs))

;;(define-key html-mode-map "\C-zg" 'html-insert-mailto-reference-from-click)

;; and, special menu bindings
(and (boundp 'psgml-html-list-menu)
     (setq psgml-html-list-menu
	   (cons '["List Item" psgml-html-smart-insert-item t] psgml-html-list-menu)))

;;}}}

;;{{{ menu support

;; menus are built for easymenu. psgml-html-add-tag builds
;; submenus based on tag type, the expert menu code lumps them
;; together into one list and calls easy-menu-define

(defun psgml-html-rebuild-menu nil
  "Rebuild and install the HTML menu (using `easy-menu-define').
If `psgml-html-use-expert-menu' is nil, then just use a novice menu."
  (let ((menu (psgml-html-expert-menu)))
    (easy-menu-remove menu)
    (easy-menu-add menu html-mode-map)))

(defun psgml-html-toggle-expert-menu (&optional arg)
  "Toggle full HTML menus. Optional arg acts like minor-mode args."
  (interactive "P")
  (setq psgml-html-use-expert-menu
	(if (null arg) (not psgml-html-use-expert-menu)
	  (> (prefix-numeric-value arg) 0)))
  (psgml-html-rebuild-menu))

;; Expert menus: consed up out of psgml-html-installed-types
(defun psgml-html-expert-menu ()
  "This menu is based on the current value of `psgml-html-installed-types'.
This function can be called again, it redoes the entire menu."
  ;; Start with the user-provided menu stuff
  (let ((psgml-html-mode-menu psgml-html-user-menu))
    ;; Now cons in the browse-url functions
    (if (fboundp 'browse-url-of-file)
	(setq psgml-html-mode-menu
	      (cons '["Load this Buffer in Browser" browse-url-of-file t]
		    psgml-html-mode-menu)))
    (if (and (boundp 'browse-url-browser-function)
	     (fboundp 'browse-url-browser-function))
	(setq psgml-html-mode-menu
	      (cons (vector "Browse URL at point"
			    browse-url-browser-function t)
		    psgml-html-mode-menu)))

    ;; cons in the timestamp delimiters
    (setq psgml-html-mode-menu
	  (cons '["Insert Timestamp Delimiter"
		  psgml-html-insert-timestamp-delimiter-at-point t]
		psgml-html-mode-menu))

    ;; now cons up the main menu out of the submenus
    (mapcar
     (function (lambda (type)
		 (setq psgml-html-mode-menu
		       (cons (psgml-html-normalized-menu-for type)
			     psgml-html-mode-menu))))
     psgml-html-installed-types)

    ;; now tack on our name
    (setq psgml-html-mode-menu (cons "Insert" psgml-html-mode-menu))

    ;; special mode keys
    (define-key html-mode-map (kbd "<M-iso-left-tab>") 'tempo-complete-tag)
    ;;("\M-\C-f" tempo-forward-mark)
    ;;("\M-\C-b" tempo-backward-mark)

    psgml-html-mode-menu))

;;}}}

;;{{{ patterns for font-lock

; Old patterns from html-mode.el
;(defvar html-font-lock-keywords
;  (list
;   '("\\(<[^>]*>\\)+" . font-lock-comment-face)
;   '("[Hh][Rr][Ee][Ff]=\"\\([^\"]*\\)\"" 1 font-lock-string-face t)
;   '("[Ss][Rr][Cc]=\"\\([^\"]*\\)\"" 1 font-lock-string-face t))
;  "Patterns to highlight in HTML buffers.")

;; By Ulrik Dickow <dickow@nbi.dk>.
;;
;; Originally aimed at Emacs 19.29.  Later on disabled syntactic fontification
;; and reordered regexps completely, to be compatible with XEmacs (it doesn't
;; understand OVERRIDE=`keep').
;;
;; We make an effort on handling nested tags intelligently.

;; font-lock compatibility with XEmacs/Lucid and older Emacsen (<19.29).
;;
(if (string-match "XEmacs" emacs-version)
    ;; XEmacs/Lucid
    ;; Make needed faces if the user hasn't already done so.
    ;; Respect X resources (`make-face' uses them when they exist).
    (let ((change-it
	   (function (lambda (face)
		       (or (if (fboundp 'facep)
			       (facep face)
			     (memq face (face-list)))
			   (make-face face))
		       (not (face-differs-from-default-p face))))))
      (if (funcall change-it 'psgml-html-bold-face)
	  (copy-face 'bold 'psgml-html-bold-face))
      (if (funcall change-it 'psgml-html-italic-face)
	  (copy-face 'italic 'psgml-html-italic-face))
      (if (funcall change-it 'psgml-html-underline-face)
	  (set-face-underline-p 'psgml-html-underline-face t))
;;       (if (funcall change-it 'font-lock-variable-name-face)
;; 	  (set-face-foreground 'font-lock-variable-name-face "salmon"))
;;       (if (funcall change-it 'font-lock-reference-face)
;; 	  (set-face-foreground 'font-lock-reference-face "violet"))
      )
  ;; Emacs (any version)
  ;;
  ;; Note that Emacs evaluates the face entries in `font-lock-keywords',
  ;; while XEmacs doesn't.  So XEmacs doesn't use the following *variables*,
  ;; but instead the faces with the same names as the variables.
  (defvar psgml-html-bold-face 'bold
    "Face used as bold.  Typically `bold'.")
  (defvar psgml-html-italic-face 'italic
    "Face used as italic.  Typically `italic'.")
  (defvar psgml-html-underline-face 'underline
    "Face used as underline.  Typically `underline'.")
  ;;
  (if (string-lessp "19.28.89" emacs-version)
      () ; Emacs 19.29 and later
    ;; Emacs 19.28 and older
    ;; Define face variables that don't exist until Emacs 19.29.
    (defvar font-lock-variable-name-face 'font-lock-doc-string-face
      "Face to use for variable names -- and some HTML keywords.")
    (defvar font-lock-reference-face 'underline ; Ugly at line breaks
      "Face to use for references -- including HTML hyperlink texts.")))

(defvar html-font-lock-keywords
  (let (;; Titles and H1's, like function defs.
	;;   We allow for HTML 3.0 attributes, like `<h1 align=center>'.
	(tword "\\(h1\\|title\\)\\([ \t\n]+[^>]+\\)?")
	;; Names of tags to boldify.
	(bword "\\(b\\|h[2-4]\\|strong\\)\\([ \t\n]+[^>]+\\)?")
	;; Names of tags to italify.
	(iword "\\(address\\|cite\\|em\\|i\\|var\\)\\([ \t\n]+[^>]+\\)?")
	;; Regexp to match shortest sequence that surely isn't a bold end.
	;; We simplify a bit by extending "</strong>" to "</str.*".
	;; Do similarly for non-italic and non-title ends.
	(not-bend (concat "\\([^<]\\|<\\([^/]\\|/\\([^bhs]\\|"
			  "b[^>]\\|"
			  "h\\([^2-4]\\|[2-4][^>]\\)\\|"
			  "s\\([^t]\\|t[^r]\\)\\)\\)\\)"))
	(not-iend (concat "\\([^<]\\|<\\([^/]\\|/\\([^aceiv]\\|"
			  "a\\([^d]\\|d[^d]\\)\\|"
			  "c\\([^i]\\|i[^t]\\)\\|"
			  "e\\([^m]\\|m[^>]\\)\\|"
			  "i[^>]\\|"
			  "v\\([^a]\\|a[^r]\\)\\)\\)\\)"))
	(not-tend (concat "\\([^<]\\|<\\([^/]\\|/\\([^ht]\\|"
			  "h[^1]\\|t\\([^i]\\|i[^t]\\)\\)\\)\\)")))
    (list ; Avoid use of `keep', since XEmacs will treat it the same as `t'.
     ;; First fontify the text of a HREF anchor.  It may be overridden later.
     ;; Anchors in headings will be made bold, for instance.
     '("<a\\s-+href[^>]*>\\([^>]+\\)</a>"
       1 font-lock-reference-face t)
     ;; Tag pairs like <b>...</b> etc.
     ;; Cunning repeated fontification to handle common cases of overlap.
     ;; Bold complex --- possibly with arbitrary other non-bold stuff inside.
     (list (concat "<" bword ">\\(" not-bend "*\\)</\\1>")
	   3 'psgml-html-bold-face t)
     ;; Italic complex --- possibly with arbitrary non-italic kept inside.
     (list (concat "<" iword ">\\(" not-iend "*\\)</\\1>")
	   3 'psgml-html-italic-face t)
     ;; Bold simple --- first fontify bold regions with no tags inside.
     (list (concat "<" bword ">\\("  "[^<]"  "*\\)</\\1>")
	   3 'psgml-html-bold-face t)
     ;; Any tag, general rule, just after bold/italic stuff.
     '("\\(<[^>]*>\\)" 1 font-lock-type-face t)
     ;; Titles and level 1 headings (anchors do sometimes appear in h1's)
     (list (concat "<" tword ">\\(" not-tend "*\\)</\\1>")
	   3 'font-lock-function-name-face t)
     ;; Underline is rarely used. Only handle it when no tags inside.
     '("<u>\\([^<]*\\)</u>" 1 psgml-html-underline-face t)
     ;; Forms, anchors & images (also fontify strings inside)
     '("\\(<\\(form\\|i\\(mg\\|nput\\)\\)\\>[^>]*>\\)"
       1 font-lock-variable-name-face t)
     '("</a>" 0 font-lock-keyword-face t)
     '("\\(<a\\b[^>]*>\\)" 1 font-lock-keyword-face t)
     '("=[ \t\n]*\\(\"[^\"]+\"\\)" 1 font-lock-string-face t)
     ;; Large-scale structure keywords (like "program" in Fortran).
     ;;   "<html>" "</html>" "<body>" "</body>" "<head>" "</head>" "</form>"
     '("</?\\(body\\|form\\|h\\(ead\\|tml\\)\\)>"
       0 font-lock-variable-name-face t)
     ;; HTML special characters
     '("&[^;\n]*;" 0 font-lock-string-face t)
     ;; SGML things like <!DOCTYPE ...> with possible <!ENTITY...> inside.
     '("\\(<![a-z]+\\>[^<>]*\\(<[^>]*>[^<>]*\\)*>\\)"
       1 font-lock-comment-face t)
     ;; Comments: <!-- ... -->. They traditionally override anything else.
     ;; It's complicated 'cause we won't allow "-->" inside a comment, and
     ;; font-lock colours the *longest* possible match of the regexp.
     '("\\(<!--\\([^-]\\|-[^-]\\|--[^>]\\)*-->\\)"
       1 font-lock-comment-face t)))
    "Additional expressions to highlight in HTML mode.")

(put 'html-mode 'font-lock-defaults '(html-font-lock-keywords nil t))

;;}}}

;;{{{ patterns for hilit19

;; Define some useful highlighting patterns for the hilit19 package.
;; These will activate only if hilit19 has already been loaded.
;; Thanks to <dickow@nbi.dk> for some pattern suggestions

(if (featurep 'hilit19)
    (hilit-set-mode-patterns
     'psgml-html-mode
     '(("<!--" "-->" comment)
       ("<![a-z]+\\>[^<>]*\\(<[^>]*>[^<>]*\\)*>" nil comment) ;<!DOCTYPE ...>
       ("<title>" "</title>" defun)
       ("<h[1-6]>" "</h[1-6]>" bold) ;only colour inside tag
       ("<a\\b" ">" define)
       ("</a>" nil define)
       ("<img\\b" ">" include)
       ("<option\\|</?select\\|<input\\|</?form\\|</?textarea" ">" include)
       ;; First <i> highlighting just handles unnested tags, then do nesting
       ("<i>[^<]*</i>" nil italic)
       ("<b>" "</b>" bold)
       ("<i>" "</i>" italic)
       ("<u>" "</u>" underline)
       ("&[^;\n]*;" nil string)
       ("<" ">" keyword))
     nil 'case-insensitive)
  nil)

;;}}}

;;{{{ completion finder for tempo

;; The regexp finds everything between the last < or & and point,
;; which is good enough to match the tags HTML might complete.
(defvar psgml-html-completion-finder "\\(\\(<\\|&\\).*\\)\\="
  "Passed to tempo-use-tag-list, used to find tags to complete.")

;;}}}

;;{{{ timestamps

(defun psgml-html-update-timestamp ()
  "Basic function for updating timestamps.
It finds the timestamp in the buffer by looking for
`psgml-html-timestamp-start', deletes all text up to
`psgml-html-timestamp-end', and runs `psgml-html-timestamp-hook' which
will should insert an appropriate timestamp in the buffer."
  (save-excursion
    (goto-char (point-max))
    (if (not (search-backward psgml-html-timestamp-start nil t))
	(message "timestamp delimiter start was not found")
      (let ((ts-start (+ (point) (length psgml-html-timestamp-start)))
	    (ts-end (if (search-forward psgml-html-timestamp-end nil t)
			(- (point) (length psgml-html-timestamp-end))
		      nil)))
	(if (not ts-end)
	    (message "timestamp delimiter end was not found. Type C-c C-t to insert one.")
	  (delete-region ts-start ts-end)
	  (goto-char ts-start)
	  (run-hooks 'psgml-html-timestamp-hook)))))
  nil)

(defun psgml-html-return-created-string ()
  "Return a \"Created:\" string."
  (let ((time (current-time-string)))
    (concat "<!-- Created: "
	    (substring time 0 20)
	    (nth 1 (current-time-zone))
	    " "
	    (substring time -4)
	    " -->\n")))

(defun psgml-html-default-insert-timestamp ()
  "Default timestamp insertion function."
  (let ((time (current-time-string)))
    (insert "Last modified: "
	    (substring time 0 20)
	    (nth 1 (current-time-zone))
	    " "
	    (substring time -4)
	    "\n")))

(defun psgml-html-insert-timestamp-delimiter-at-point ()
  "Simple function that inserts timestamp delimiters at point.
Useful for adding timestamps to existing buffers."
  (interactive)
  (insert psgml-html-timestamp-start)
  (insert psgml-html-timestamp-end))

;;}}}

(defun mail-address-at-point (pos &optional buffer)
  "Return a list (NAME ADDRESS) of the address at POS in BUFFER."
  (or buffer (setq buffer (current-buffer)))
  (let (beg end)
    (save-excursion
      (set-buffer buffer)
      (save-excursion
	(goto-char pos)
	(or (re-search-forward "[\n,]" nil t)
	    (error "Can't find address at position"))
	(backward-char)
	(setq end (point))
	(or (re-search-backward "[\n,:]" nil t)
	    (error "Can't find address at position"))
	(forward-char)
	(re-search-forward "[ \t]*" nil t)
	(setq beg (point))
	(mail-extract-address-components (buffer-substring beg end))))))

(defun html-insert-mailto-reference-from-click ()
  "Insert a mailto: reference for the clicked-on e-mail address."
  (interactive)
  (let (event)
    (message "Click on a mail address:")
    (save-excursion
      (setq event (next-command-event))
      (or (mouse-event-p event)
	  (error "Aborted.")))
    (let ((lis (mail-address-at-point (event-closest-point event)
				      (event-buffer event))))
      (insert "<a href=\"mailto:" (car (cdr lis)) "\">"
	      (or (car lis) (car (cdr lis))) "</a>"))))

;;;###autoload
(defun html-quote-region (begin end)
  "\"Quote\" any characters in the region that have special HTML meanings.
This converts <'s, >'s, and &'s into the HTML commands necessary to
get those characters to appear literally in the output."
  (interactive "r")
  (save-excursion
    (goto-char begin)
    (while (search-forward "&" end t)
      (forward-char -1)
      (delete-char 1)
      (insert "&amp;")
      (setq end (+ 4 end)))
    (goto-char begin)
    (while (search-forward "<" end t)
      (forward-char -1)
      (delete-char 1)
      (insert "&lt;")
      (setq end (+ 3 end)))
    (goto-char begin)
    (while (search-forward ">" end t)
      (forward-char -1)
      (delete-char 1)
      (insert "&gt;")
      (setq end (+ 3 end)))))

;;{{{ psgml-html-insert-new-buffer-strings

(tempo-define-template "html-skeleton" psgml-html-new-buffer-template
		       nil
		       "Insert a skeleton for a HTML document")

(defun psgml-html-insert-new-buffer-strings ()
  "Insert `psgml-html-new-buffer-strings'."
  (set-mark (point-min))
  (tempo-template-html-skeleton nil))

;;}}}

;;;###autoload
(autoload 'html-mode "psgml-html" "HTML mode." t)

(defvar sgml-html-menu
  (cons "HTML"
	(append '(["View in Browser" browse-url-of-buffer
		   (buffer-file-name
		    (current-buffer))]
		  ["View in W3" w3-preview-this-buffer t]
		  "---"
		  ["HTML-Quote Region" html-quote-region t]
		  "---")
		(cdr sgml-main-menu))))

(defun sgml-html-netscape-file ()
  "Preview the file for the current buffer in Netscape."
  (interactive)
  (highlight-headers-follow-url-netscape
   (concat "file:" (buffer-file-name (current-buffer)))))

(defun sgml-html-kfm-file ()
  "Preview the file for the current buffer in kfm."
  (interactive)
  (highlight-headers-follow-url-kfm
   (concat "file:" (buffer-file-name (current-buffer)))))

;;; end of psgml-html.el
