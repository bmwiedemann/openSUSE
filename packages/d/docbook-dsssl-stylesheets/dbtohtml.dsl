<!doctype style-sheet PUBLIC "-//James Clark//DTD DSSSL Style Sheet//EN">
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
; dbtohtml.dsl - DSSSL style sheet for DocBook to HTML conversion (jadeware)
;
; Author          : Mark Burton (markb@ordern.com)
; Created On      : Fri Jun 13 18:21:14 1997
; Last Modified By: Mark Burton
; Last Modified On: Sat Nov 21 22:04:53 1998
;
; $Id: dbtohtml.dsl,v 1.23 1998/11/21 22:11:14 markb Exp $
;
; Usage:
;
; jade -d dbtohtml.dsl -t sgml yourdoc.sgm
;
; Additional command line options:
;
; -V %no-split-output%  sends all the output to one file
; -V %no-make-index%    disables index creation
; -V %no-make-toc%      disables TOC creation
; -V %no-shade-screen%  disables grey background to SCREEN regions
; -V %show-comments%    includes contents of COMMENT regions
;
; See below for more variables that can be set.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Contributors

; Mark Eichin   (eichin@cygnus.com)
; Jason Molenda (crash@cygnus.co.jp)
; Tony Graham   (tgraham@mulberrytech.com)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Parameterisation

; This style sheet can easily be parameterised by the use of a driver.
; Here is a simple example that sets the output file basename and directory.
; If the driver is foo.dsl, use: jade -d foo.dsl -t sgml yourdoc.sgm

<!--

<!doctype style-sheet PUBLIC "-//James Clark//DTD DSSSL Style Sheet//EN" [
<!ENTITY dbtohtml.dsl SYSTEM "dbtohtml.dsl" CDATA DSSSL >
]>

<style-specification id="foodbtohtml" use="dbtohtml">

(define %output-basename% "foo")
(define %output-directory% "foodir")

</style-specification>

<external-specification id="dbtohtml" document="dbtohtml.dsl">

-->

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; declare non-standard functions

(declare-flow-object-class element
  "UNREGISTERED::James Clark//Flow Object Class::element")
(declare-flow-object-class empty-element
  "UNREGISTERED::James Clark//Flow Object Class::empty-element")
(declare-flow-object-class document-type
  "UNREGISTERED::James Clark//Flow Object Class::document-type")
(declare-flow-object-class processing-instruction
  "UNREGISTERED::James Clark//Flow Object Class::processing-instruction")
(declare-flow-object-class entity
  "UNREGISTERED::James Clark//Flow Object Class::entity")
(declare-flow-object-class entity-ref
  "UNREGISTERED::James Clark//Flow Object Class::entity-ref")
(declare-flow-object-class formatting-instruction
  "UNREGISTERED::James Clark//Flow Object Class::formatting-instruction")

(declare-characteristic preserve-sdata?
  "UNREGISTERED::James Clark//Characteristic::preserve-sdata?" #f)

(define all-element-number
  (external-procedure "UNREGISTERED::James Clark//Procedure::all-element-number"))

(define debug
  (external-procedure "UNREGISTERED::James Clark//Procedure::debug"))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; variables

(define %no-split-output% #f)		; if #t puts all output in one file
(define %no-split-refentries% #f)	; if #t don't put refentries
					; in separate files
(define %no-make-toc% #f)		; if #t disables TOC creation
(define %no-make-index% #f)		; if #t disables index creation
(define %no-shade-screen% #f)		; if #t disables grey
					; background to SCREEN regions
(define %show-comments% #f)		; if #t includes contents of
					; COMMENT regions
(define %shade-width% "100%")		; width string or #f
(define %email-element% "TT")		; font changing element or #f

(define %lineannotation-color% "green")	; colour or #f (ignored if
					; %stylesheet-name% is not #f)

(define %warning-color% "red")		; colour or #f
(define %important-color% #f)		; colour or #f
(define %caution-color% #f)		; colour or #f
(define %tip-color% #f)			; colour or #f
(define %note-color% #f)		; colour or #f
(define %example-color% #f)		; colour or #f

(define %display-dpi% 100)		; for converting lengths into pixels

(define %centre-figures% #t)		; whether figures should be centred

(define %default-graphic-format% "gif")
(define %graphic-directory% #f)		; name of directory containing
					; graphics or #f

(define %html-public-id% "-//W3C//DTD HTML 4.0//EN")

(define %stylesheet-name% #f)		; name of css style-sheet to
					; be used or #f
(define %have-javascript% #f)		; true if browser groks JavaScript
(define %make-nav-links% #f)		; true if pages should have
					; navigation links at their
					; top and bottom
(define %body-bgcolor% "white")		; document background colour
					; (ignored if %stylesheet-name% is
					; not #f
(define %output-directory% ".")		; where to write generated HTML
(define %output-basename% "DBTOHTML")	; generated filenames are
					; based on this
(define %output-suffix% ".html")	; generated filename suffix
(define %newline% "\U-000D")		; there must be an easier way
					; to specify \n

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; top-level sections

(element BOOK
  (if %no-split-output%			; everything goes in one file
      (make-file (string-append %output-basename% %output-suffix%)
		 (make sequence
		   (process-children)
		   (cond ((not %no-make-index%)
			  (make sequence
			    (make-fat-rule)
			    (make-index)))
			 (#t (empty-sosofo))))
		 (current-node)
		 (node-list)
		 (node-list))
      (make sequence			; split output into separate files
	(let* ((content (make sequence
			  (process-first-descendant "TITLE")
			  (process-first-descendant "BOOKINFO")))
	       (children (children (current-node)))
	       (linkable-children (node-list (select-elements children "PREFACE")
					     (select-elements children "ARTICLE")
					     (select-elements children "CHAPTER")
					     (select-elements children "APPENDIX"))))
	  (make-file (string-append %output-basename% %output-suffix%)
		     (if %stylesheet-name%
			 (make element
			   gi: "DIV"
			      attributes: '(("class" "book"))
			      content)
			 content)
		     (current-node)
		     (node-list-last linkable-children)
		     (node-list-first linkable-children)))
	(process-matching-children "PREFACE"
				   "ARTICLE"
				   "CHAPTER"
				   "APPENDIX"
				   "BIBLIOGRAPHY"
				   "GLOSSARY"
				   "ARTHEADER")
	(if %no-make-index%
	    (empty-sosofo)
	    (make-file (index-file-name)
		       (make sequence
			 (make-nav-links (current-node))
			 (make-index)
			 (make-nav-links (current-node)))
		       (current-node)
		       (node-list)
		       (node-list))))))

(define (make-file file-name content top-node preceding-node following-node)
  (make entity
    system-id: (string-append %output-directory% "/" file-name)
    (make sequence
      (make document-type
	name: "HTML"
	public-id: %html-public-id%)
      (make element
	gi: "HTML" 
	(make sequence
	  (make element
	    gi: "HEAD"
	    (make sequence
	      (make element
		gi: "TITLE"
		(with-mode extract-title-text
		  (process-first-descendant "TITLE")))
	      (if %stylesheet-name%
		  (make empty-element
		    gi: "LINK"
		    attributes: (list (list "rel" "stylesheet")
				      (list "type" "text/css")
				      (list "href" %stylesheet-name%)))
		  (empty-sosofo))
	      (if %have-javascript%
		  (make element
		    gi: "SCRIPT"
		    attributes: '(("type" "text/javascript"))
		    (make sequence
		      (make formatting-instruction
			data: (string-append %newline% "<" "!--" %newline%))
		      (literal "var toppage='"
			       (link-file-name top-node)
			       "';" %newline%
			       "var nextpage='"
			       (if (node-list-empty? following-node)
				   (link-file-name top-node)
				   (link-file-name following-node))
			       "';" %newline%
			       "var prevpage='"
			       (if (node-list-empty? preceding-node)
				   (link-file-name top-node)
				   (link-file-name preceding-node))
			       "';" %newline%
			       (if %no-make-index%
				   ""
				   (string-append "var indexpage='"
						  (index-file-name)
						  "';" %newline%))
			       )
		      (make formatting-instruction
			data: (string-append "// -->" %newline%))))
		  (empty-sosofo))))
	  (make element
	    gi: "BODY"
	    attributes: (if %stylesheet-name%
			    (list)
			    (list (list "bgcolor" %body-bgcolor%)))
	    (make sequence
	      (if %stylesheet-name%
		  (make element
		    gi: "DIV"
		    (make-anchor))
		  (make-anchor))
	      content
	      (make-footer))))))))
			 
(define (make-footer)
  (let ((copyright (select-elements (descendants (book-node))
				    '("BOOKINFO" "COPYRIGHT"))))
    (cond ((node-list-empty? copyright) (empty-sosofo))
	  (#t (make sequence
		(make-fat-rule)
		(process-node-list copyright))))))

(define (node-list-last nl)
  (node-list-ref nl (- (node-list-length nl) 1)))

(define (filtered-preceding-node)
  (let* ((preceding-node (node-list-last (preced (current-node))))
	 (acceptable-neighbours '("CHAPTER" "APPENDIX" "GLOSSARY" "REFENTRY")))
    (if (member (gi preceding-node) acceptable-neighbours)
	preceding-node
	(node-list))))

(define (filtered-following-node)
  (let* ((following-node (node-list-first (follow (current-node))))
	 (acceptable-neighbours '("CHAPTER" "APPENDIX" "GLOSSARY" "REFENTRY")))
    (if (member (gi following-node) acceptable-neighbours)
	following-node
	(node-list))))

(define (make-nav-links up-node)
  (if %make-nav-links%
      (let ((gubbins
	     (let ((filtered-preceding-node (filtered-preceding-node))
		   (filtered-following-node (filtered-following-node)))
	       (make sequence
		 (make empty-element
		   gi: "P")
		 (make element
		   gi: "A"
		   attributes: (list (list "href" (link-file-name up-node)))
		   (literal "Up"))
		 (literal " ")
		 (if (node-list-empty? filtered-following-node)
		     (empty-sosofo)
		     (make element
		       gi: "A"
		       attributes: (list (list "href"
					       (link-file-name filtered-following-node)))
		       (literal "Forward")))
		 (literal " ")
		 (if (node-list-empty? filtered-preceding-node)
		     (empty-sosofo)
		     (make element
		       gi: "A"
		       attributes: (list (list "href"
					       (link-file-name filtered-preceding-node)))
		       (literal "Back")))
		 (make empty-element
		   gi: "P")))))
	(if %stylesheet-name%
	    (make element
	      gi: "DIV"
	      attributes: '(("class" "navlinks"))
	      gubbins)
	    gubbins))
      (empty-sosofo)))

(define (make-major-div)
  (cond (%no-split-output%
	 (make sequence
	   (make-anchor)
	   (make-fat-rule)
	   (process-children)))
	(#t
	 (make-file (link-file-name (current-node))
		    (make sequence
		      (make-nav-links (book-node))
		      (if %stylesheet-name%
			  (make element
			    gi: "DIV"
			    attributes: '(("class" "chapter"))
			    (process-children))
			  (process-children))
		      (make-nav-links (book-node)))
		    (book-node)
		    (filtered-preceding-node)
		    (filtered-following-node)))))

(element ARTICLE (make-major-div))

(element PREFACE (make-major-div))

(element CHAPTER (make-major-div))

(element APPENDIX (make-major-div))

(element BEGINPAGE (make-thin-rule))

(element BIBLIOGRAPHY (make-major-div))

(element BOOKBIBLIO (process-children))

(element BIBLIODIV (process-children))

(element GLOSSARY (make-major-div))

; (element GLOSSDIV (make-major-div))

(element ARTHEADER (process-children))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; sections

(element SECT1
  (make sequence
    (make empty-element
      gi: "P")
    (make-anchor)
    (process-children)))

(element SECT2
  (make sequence
    (make-anchor)
    (process-children)))

(element SECT3
  (make sequence
    (make-anchor)
    (process-children)))

(element SECT4
  (make sequence
    (make-anchor)
    (process-children)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; reference pages

(element REFENTRY 
  (if (or %no-split-output% %no-split-refentries%)
      (make sequence
	(make-anchor)
	(make-fat-rule)
	(process-children))
      (let ((filename (link-file-name (current-node)))
	    (title-text (with-mode make-toc-links (process-first-descendant "REFMETA"))))
	(make sequence
	  (make-file filename
		     (make sequence
		       (make-nav-links (parent (current-node)))
		       (if %stylesheet-name%
			   (make element
			     gi: "DIV"
			     attributes: '(("class" "refentry"))
			     (process-children))
			   (process-children))
		       (make-nav-links (parent (current-node))))
		     (parent (current-node))
		     (filtered-preceding-node)
		     (filtered-following-node))
	  (make empty-element
	    gi: "P")
	  (make element
	    gi: "A"
	    attributes: (list (list "href" filename))
	    title-text)))))

(define (refmeta) 
  (make sequence
    (process-matching-children "REFENTRYTITLE")
    (literal "(")
    (process-matching-children "MANVOLNUM")
    (literal ")")))

(define (refentrytitle)
  (process-children-trim))
(define (manvolnum)
  (process-children-trim))

(mode make-toc-links
  (element REFMETA (refmeta))
  (element REFENTRYTITLE (refentrytitle))
  (element MANVOLNUM (manvolnum)))

(element REFMETA
  (if %stylesheet-name%
      (make element
	gi: "DIV"
	attributes: '(("style" "text-align: right"))
	(refmeta))
      (refmeta)))

(element REFENTRYTITLE (refentrytitle))
(element MANVOLNUM (manvolnum))

(element REFNAMEDIV
  (make sequence
    (make element
      gi: "H2"
      (literal "NAME"))
    (process-matching-children "REFNAME")
    (literal " - ")
    (process-matching-children "REFPURPOSE")))

(element REFNAME (process-children-trim))
(element REFPURPOSE (process-children-trim))

(element REFSYNOPSISDIV (process-children))
(element REFSECT1 (process-children))
(element REFSECT2 (process-children))
(element REFSECT3 (process-children))
(element REFSECT4 (process-children))

(element CMDSYNOPSIS
  (make element
    gi: "TT"))

(element ARG
  (let ((optional (equal? (attribute-string "CHOICE") "OPT"))
	(repeat (equal? (attribute-string "REP") "REPEAT"))
	(content (process-children-trim)))
    (if optional
	(make sequence
	  (literal " [ ")
	  content
	  (if repeat
	      (literal " ... ")
	      (empty-sosofo))
	  (literal " ] "))
	(make sequence
	  (literal " ")
	  content
	  (if repeat
	      (literal " ... ")
	      (empty-sosofo))
	  (literal " ")))))

(element FUNCSYNOPSIS
  (let ((gubbins (make sequence
		   (process-matching-children "FUNCSYNOPSISINFO")
		   (process-matching-children "FUNCDEF" "PARAMDEF"))))
    (if %stylesheet-name%
	gubbins
	(make element
	  gi: "TT"
	  gubbins))))

(element FUNCSYNOPSISINFO
  (make element
    gi: "PRE"
    attributes: '(("class" "funcsynopsisinfo"))))

(element FUNCDEF
  (make sequence
    (make empty-element
      gi: "TABLE")
    (make empty-element
      gi: "TR"
      attributes: (list '("valign" "top")))
    (make empty-element
      gi: "TD")
    (make empty-element
      gi: "PRE"
      attributes: '(("class" "plain")))
    (make empty-element
      gi: "TT")
    (process-children-trim)))

(element PARAMDEF
  (let ((head (if (equal? (gi (node-list-last (preced (current-node))))
			  "PARAMDEF")
		  (literal ", ")
		  (make sequence
		    (literal "(")
		    (make empty-element
		      gi: "/TT")
		    (make empty-element
		      gi: "/PRE")
		    (make empty-element
		      gi: "TD")
		    (make empty-element
		      gi: "TT"))))
	(tail (if (equal? (gi (node-list-first (follow (current-node))))
			      "PARAMDEF")
		  (empty-sosofo)
		  (make sequence
		    (literal " );")
		    (make empty-element
		      gi: "/TT")
		    (make empty-element
		      gi: "/TABLE")))))
    (make sequence
      head
      (process-children-trim)
      tail)))

(element CITEREFENTRY
  (make sequence
    (process-matching-children "REFENTRYTITLE")
    (literal "(")
    (process-matching-children "MANVOLNUM")
    (literal ")")))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; titles

(mode extract-title-text
  (element (TITLE)
    (process-children)))

(element (BOOK TITLE)
  (let ((content (make element
		   gi: "H1"
		   attributes: '(("class" "book"))
		   (process-children-trim))))
    (if %stylesheet-name%
	content
	(make element
	  gi: "CENTER"
	  content))))

(element (CHAPTER TITLE)
  (make element
    gi: "H1"
    attributes: '(("class" "chapter"))
    (make sequence
      (literal (chap-app-head-label "Chapter"))
      (process-children-trim))))

(element (APPENDIX TITLE)
  (make element
    gi: "H1"
    attributes: '(("class" "appendix"))
    (make sequence
      (literal (chap-app-head-label "Appendix"))
      (process-children-trim))))

(element (BIBLIOGRAPHY TITLE)
  (make element
    gi: "H1"
    attributes: '(("class" "bibliography"))
    (make sequence
      (literal (chap-app-head-label "Bibliography"))
      (process-children-trim))))

(element (BOOKBIBLIO TITLE)
  (make element
    gi: "H2"
    attributes: '(("class" "bookbiblio"))
    (make sequence
;;;      (literal (chap-app-head-label "Bibliography"))
      (process-children-trim))))

(element (BIBLIODIV TITLE)
  (make element
    gi: "H2"
    attributes: '(("class" "bibliodiv"))
    (make sequence
      (process-children-trim))))

(element (GLOSSARY TITLE)
  (make element
    gi: "H1"
    attributes: '(("class" "glossary"))
    (make sequence
      (literal "Glossary")
;      (process-children-trim)
      )))

(element (GLOSSDIV TITLE)
  (make element
    gi: "H2"
    attributes: '(("class" "glossdiv"))
    (process-children-trim)))

(element (ARTHEADER TITLE)
  (let ((content (make element
		   gi: "H1"
		   attributes: '(("class" "artheader"))
		   (process-children-trim))))
    (if %stylesheet-name%
	content
	(make element
	  gi: "CENTER"
	  content))))
 
(element (SECT1 TITLE)
  (make element
    gi: "H2"
    attributes: '(("class" "sect1"))))

(element (SECT2 TITLE)
  (make element
    gi: "H3"
    attributes: '(("class" "sect2"))))

(element (SECT3 TITLE)
  (make element
    gi: "H4"
    attributes: '(("class" "sect3"))))

(element (SECT4 TITLE)
  (make element
    gi: "H5"
    attributes: '(("class" "sect1"))))

(element (FORMALPARA TITLE)
  (make element
    gi: "H4"
    attributes: '(("class" "formalpara"))))

(element (SIDEBAR TITLE)
  (make element
    gi: "H2"
    attributes: '(("class" "sidebar"))))

(element (REFSYNOPSISDIV TITLE)
  (make element
    gi: "H2"
    attributes: '(("class" "refsynopsisdiv"))))

(element (REFSECT1 TITLE)
  (make element
    gi: "H2"
    attributes: '(("class" "refsect1"))))

(element (REFSECT2 TITLE)
  (make element
    gi: "H3"
    attributes: '(("class" "refsect2"))))

(element (REFSECT3 TITLE)
  (make element
    gi: "H4"
    attributes: '(("class" "refsect1"))))

(element (REFSECT4 TITLE)
  (make element
    gi: "H5"
    attributes: '(("class" "sect4"))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; font changers

(element LINEANNOTATION
  (cond (%stylesheet-name%
	 (make element
	   gi: "SPAN"
	   attributes: '(("class" "lineannotation"))
	   (process-children-trim)))
	(%lineannotation-color%
	 (make element
	   gi: "FONT"
	   attributes: (list (list "color" %lineannotation-color%))
	   (process-children-trim)))
	(#t (process-children-trim))))


(element EMPHASIS
  (make element gi: "I"))

(element TYPE
  (make element gi: "B" 
	(make element gi: "TT")))

(element REPLACEABLE
  (make element gi: "I"
	(make element gi: "B" 
	      (make element gi: "TT"))))

(element TOKEN 
  (if %stylesheet-name%
      (make element
	gi: "SPAN"
	attributes: '(("class" "token"))
	(process-children-trim))
      (process-children-trim)))

(element PARAMETER (make element gi: "I"))

(element FIRSTTERM (make element gi: "I"))

(element APPLICATION (make element gi: "TT"))

(element SYSTEMITEM (make element gi: "TT"))

(element FILENAME (make element gi: "TT"))

(element LITERAL (make element gi: "TT"))

(element ENVAR (make element gi: "TT"))

(element SUBSCRIPT (make element gi: "SUB"))

(element SUPERSCRIPT (make element gi: "SUP"))

(element CITETITLE (make element gi: "I"))

(element GUIBUTTON   (make element gi: "I"))
(element GUIMENU     (make element gi: "I"))
(element GUIMENUITEM (make element gi: "I"))
(element GUILABEL    (make element gi: "I"))

(element STRUCTNAME  (make element gi: "TT"))
(element STRUCTFIELD (make element gi: "TT"))

(element COMMAND (make element gi: "TT"))

(element OPTION (make element gi: "TT"))

(element USERINPUT (make element gi: "TT"))

(element COMPUTEROUTPUT (make element gi: "TT"))

(element PROMPT (make element gi: "TT"))

(element PRODUCTNAME (make element gi: "I"))

(element SGMLTAG (make element gi: "TT"))

(element (FUNCDEF FUNCTION)
  (make element
    gi: "B"
    (make element
      gi: "TT")))
(element FUNCTION (make element gi: "TT"))

(element SYMBOL (make element gi: "TT"))
(element LITERALLAYOUT
  (make element
    gi: "PRE"
    attributes: '(("class" "literallayout"))))

(element FOREIGNPHRASE (make element gi: "I"))

(element ABBREV (process-children-trim))

(element EMAIL
  (if %email-element%
      (make element
	gi: %email-element%
	(process-children-trim))
      (process-children-trim)))

(element QUOTE
  (make sequence
    (make entity-ref
      name: "quot")
    (process-children-trim)
    (make entity-ref
      name: "quot")))

(element ADDRESS
  (make element
    gi: "ADDRESS"
    (process-children-trim)))

(element (ADDRESS CITY)
  (make sequence
    (make empty-element 
      gi: "BR")
    (process-children-trim)))

(element (ADDRESS COUNTRY)
  (make sequence
    (make empty-element 
      gi: "BR")
    (process-children-trim)))

(element (ADDRESS EMAIL)
  (make sequence
    (make empty-element
      gi: "BR")
    (if %email-element%
	(make element
	  gi: %email-element%
	  (process-children-trim))
	(process-children-trim))))

(element (ADDRESS FAX)
  (make sequence
    (make empty-element 
      gi: "BR")
    (process-children-trim)))

(element (ADDRESS OTHERADDR)
  (make sequence
    (make empty-element 
      gi: "BR")
    (process-children-trim)))

(element (ADDRESS POB)
  (make sequence
    (make empty-element 
      gi: "BR")
    (process-children-trim)))

(element (ADDRESS PHONE)
  (make sequence
    (make empty-element 
      gi: "BR")
    (process-children-trim)))

(element (ADDRESS POSTCODE)
  (process-children-trim))

(element (ADDRESS STATE)
  (process-children-trim))

(element (ADDRESS STREET)
  (make sequence
    (make empty-element 
      gi: "BR")
    (process-children-trim)))

(element PROGRAMLISTING
  (make element
    gi: "PRE"
    attributes: '(("class" "programlisting"))))

(element SECT2INFO
  (empty-sosofo))

(element SYNOPSIS
  (make element
    gi: "PRE"
    attributes: '(("class" "synopsis"))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; paragraph like things

(element CAUTION
  (if %caution-color%
      (make-color-para %caution-color%)
      (make-special-para)))

(element IMPORTANT
  (if %important-color%
      (make-color-para %important-color%)
      (make-special-para)))

(element WARNING 
  (if %warning-color%
      (make-color-para %warning-color%)
      (make-special-para)))

(element NOTE
  (if %note-color%
      (make-color-para %note-color%)
      (make-special-para)))

(element TIP
  (if %tip-color%
      (make-color-para %tip-color%)
      (make-special-para)))

(element EXAMPLE
  (if %example-color%
      (make-color-para %example-color%)
      (make-special-para)))

(element COMMENT
  (if %show-comments%
      (make-color-para "red")
      (empty-sosofo)))

(element PARA
  (make sequence
    (make empty-element
      gi: "P")
    (make-anchor)
    (with-mode footnote-ref
      (process-children))
    (with-mode footnote-def
      (process-matching-children "FOOTNOTE"))))

(element BLOCKQUOTE (make element gi: "BLOCKQUOTE"))

(element SCREEN
  (let ((gubbins (make element
		   gi: "PRE"
		   attributes: '(("class" "screen"))
		   (process-children))))
    (make sequence
      (make empty-element
	gi: "P")
      (if (or %stylesheet-name% %no-shade-screen%)
	  gubbins
	  (make element
	    gi: "TABLE"
	    attributes: (append (list '("border" "0")
				      '("bgcolor" "#E0E0E0"))
				(if %shade-width%
				    (list (list "width" %shade-width%))
				    '()))
	    (make element
	      gi: "TR"
	      (make element
		gi: "TD"
		gubbins)))))))

(element FORMALPARA (process-children))

(element PHRASE (maybe-bold-children))

(mode footnote-ref
  (element FOOTNOTE
    (let ((num (format-number (element-number (current-node)) "1")))
      (make element
	gi: "SUP"
	attributes: '(("class" "footnoteref"))
	(make element
	  gi: "A"
	  attributes: (list (list "href" (string-append "#footnote-" num)))
	  (literal num))))))

(mode footnote-def
  (element FOOTNOTE
    (let ((num (format-number (element-number (current-node)) "1")))
      (make element
	gi: "BLOCKQUOTE"
	attributes: '(("class" "footnote"))
	(make sequence
	  (make empty-element
	    gi: "P")
	  (make element
	    gi: "A"
	    attributes: (list (list "name" (string-append "footnote-" num)))
	    (make element
	      gi: "SUP"
	      attributes: '(("class" "footnote"))
	      (literal num)))
	  (process-children))))))

(element (CAUTION TITLE)
  (make element
      gi: "H5"))

(element (IMPORTANT TITLE)
  (make element
      gi: "H5"))

(element (WARNING TITLE)
  (make element
      gi: "H5"))

(element (NOTE TITLE)
  (make element
      gi: "H5"))

(element (TIP TITLE)
  (make element
      gi: "H5"))

(element (EXAMPLE TITLE)
  (make element
      gi: "H5"))

(element (BIBLIOENTRY TITLE)
  (make element
      gi: "H3"))

(element (SIDEBAR)
  (make sequence
    (make empty-element
      gi: "P")
    (make element
      gi: "TABLE"
      attributes: '(("border" "1")
		    ("bgcolor" "#f0f0f0")
		    ("width" "100%"))
      (make element
	gi: "TR"
	(make element
	  gi: "TD"
	  (process-children))))))
  
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; lists

(element ITEMIZEDLIST
  (make sequence
    (make empty-element
      gi: "P")
    (make-anchor)
    (make element
      gi: "UL")))

(element ORDEREDLIST
  (make sequence
    (make empty-element
      gi: "P")
    (make-anchor)
    (make element
      gi: "OL")))

(element (ITEMIZEDLIST LISTITEM)
  (make sequence
    (make empty-element
      gi: "LI")
    (process-children)
    (make empty-element
      gi: "P")))

(element (ORDEREDLIST LISTITEM)
  (make sequence
    (make empty-element
      gi: "LI")
    (process-children)
    (make empty-element
      gi: "P")))

(element VARIABLELIST
  (make sequence
    (make empty-element
      gi: "P")
    (make-anchor)
    (make element
      gi: "DL")))

(element VARLISTENTRY (process-children))

(element (VARLISTENTRY LISTITEM)
  (make sequence
    (make empty-element
      gi: "DD")
    (process-children)
    (make empty-element
      gi: "P")))


(element (VARLISTENTRY TERM)
  (let ((content (make sequence
		   (make-anchor)
		   (maybe-bold-children))))
    (make sequence
      (make empty-element
	gi: "DT")
      (cond ((equal? (inherited-element-attribute-string
		      "VARIABLELIST" "role") "bold")
	     (make element
	       gi: "B"
	       content))
	    ((equal? (inherited-element-attribute-string
		      "VARIABLELIST" "role") "fixed")
	     (make element
	       gi: "TT"
	       content))
	    (#t content)))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; glossary

(element GLOSSTERM (process-children))

(element GLOSSDIV
  (make sequence
    (make empty-element
      gi: "P")
    (process-children)))

(element (GLOSSENTRY GLOSSSEE)
  (make sequence
    (make empty-element
      gi: "DD")
    (literal "See ")
    (make element
      gi: "A" 
      attributes: (list (list "href" 
			      (string-append "#"
					     (if
					      (string?
					       (attribute-string "otherterm"))
					      (attribute-string "otherterm")
					      (gloss-entry-name
					       (current-node))))))
      (if (string? (attribute-string "otherterm"))
	  (with-mode glosssee
	    (process-element-with-id
	     (attribute-string "OTHERTERM")))
	  (process-children-trim)))
    (make empty-element
      gi: "P")))

(define (gloss-entry-name glossterm)
  (string-append "gloss-" (data glossterm)))

(element (GLOSSENTRY GLOSSTERM)
  (make sequence
    (make empty-element
      gi: "DT")
    (make element
      gi: "A" 
      attributes: (list (list "name"
			      (if (string? (inherited-attribute-string "ID"))
				  (inherited-attribute-string "ID")
				  (gloss-entry-name (current-node)))))
      (empty-sosofo))
    (process-children)))

(element GLOSSENTRY
  (make element
    gi: "DL"
    (process-children)))

(element (GLOSSENTRY GLOSSDEF)
  (make sequence
    (make empty-element
      gi: "DD")
    (process-children)
    (make empty-element
      gi: "P")))

(element GLOSSSEEALSO
  (make sequence
    (if (first-sibling?)
	(make sequence
	  (make empty-element
	    gi: "P")
	  (make element
	    gi: "EM"
	    (literal "See also ")))
	(make sequence
	  (make element
	    gi: "EM"
	    (literal ", "))))
    (make element
      gi: "a"
      attributes: (list (list "href"
			      (string-append
			       "#"
			       (attribute-string
				"OTHERTERM"))))
      (with-mode glosssee
	(process-element-with-id
	 (attribute-string "OTHERTERM"))))))

;; This is referenced within the GLOSSSEE and GLOSSSEEALSO element
;; construction expressions.  The OTHERTERM attributes on GLOSSSEE and
;; GLOSSSEEALSO (should) refer to GLOSSENTRY elements but we're only
;; interested in the text within the GLOSSTERM.  Discard the revision
;; history and the definition from the referenced term.
(mode glosssee
  (element GLOSSTERM
    (process-children))
  (element REVHISTORY
    (empty-sosofo))
  (element GLOSSDEF
    (empty-sosofo)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; index

(define (index-entry-name indexterm)
  (string-append "index." (format-number (element-number indexterm) "1")))

(element INDEXTERM
  (make sequence
    (make-anchor)
    (make element
      gi: "A"
      attributes: (list (list "name" (index-entry-name (current-node))))
      (literal ""))
    (empty-sosofo)))

; DIY string-ci>?

(define (string-ci>? s1 s2)
  (let ((len1 (string-length s1))
	(len2 (string-length s2)))
    (let loop ((i 0))
      (cond ((= i len1) #f)
	    ((= i len2) #t)
	    (#t (let ((c1 (index-char-val (string-ref s1 i)))
		      (c2 (index-char-val (string-ref s2 i))))
		  (cond
		   ((= c1 c2) (loop (+ i 1)))
		   (#t (> c1 c2)))))))))

(define (equal-ci? s1 s2)
  (let ((len1 (string-length s1))
	(len2 (string-length s2)))
    (if (= len1 len2) 
	(let loop ((i 0))
	  (if (= i len1)
	      #t
	      (let ((c1 (index-char-val (string-ref s1 i)))
		    (c2 (index-char-val (string-ref s2 i))))
		(if (= c1 c2)
		    (loop (+ i 1))
		    #f))))
	#f)))

(define (index-char-val ch)
  (case ch
    ((#\A #\a) 65)
    ((#\B #\b) 66)
    ((#\C #\c) 67)
    ((#\D #\d) 68)
    ((#\E #\e) 69)
    ((#\F #\f) 70)
    ((#\G #\g) 71)
    ((#\H #\h) 72)
    ((#\I #\i) 73)
    ((#\J #\j) 74)
    ((#\K #\k) 75)
    ((#\L #\l) 76)
    ((#\M #\m) 77)
    ((#\N #\n) 78)
    ((#\O #\o) 79)
    ((#\P #\p) 80)
    ((#\Q #\q) 81)
    ((#\R #\r) 82)
    ((#\S #\s) 83)
    ((#\T #\t) 84)
    ((#\U #\u) 85)
    ((#\V #\v) 86)
    ((#\W #\w) 87)
    ((#\X #\x) 88)
    ((#\Y #\y) 89)
    ((#\Z #\z) 90)

    ((#\ ) 32)

    ((#\0) 48)
    ((#\1) 49)
    ((#\2) 50)
    ((#\3) 51)
    ((#\4) 52)
    ((#\5) 53)
    ((#\6) 54)
    ((#\7) 55)
    ((#\8) 56)
    ((#\9) 57)

    ; laziness precludes me from filling this out further
    (else 0)))

(define (string->number-list s)
  (let loop ((i (- (string-length s) 1))
	     (l '()))
    (if (< i 0)
	l
	(loop (- i 1) (cons (index-char-val (string-ref s i)) l)))))

(define (number-list>? l1 l2)
  (cond ((null? l1) #f)
	((null? l2) #t)
	((= (car l1) (car l2))
	 (number-list>? (cdr l1) (cdr l2)))
	(#t (> (car l1) (car l2)))))

; return the string data for a given index entry

(define (get-index-entry-data entry)
  (let ((primary (select-elements (children entry) "PRIMARY"))
	(secondary (select-elements (children entry) "SECONDARY")))
    (if (node-list-empty? secondary)
	(data primary)
	(string-append (data primary) " - " (data secondary)))))

(define (make-index-entry entry)
  (let ((text (get-index-entry-data entry)))
    (cons text
	  (make sequence
	    (make empty-element
	      gi: "LI")
	    (make element
	      gi: "A"
	      attributes: (list (list "href"
				      (string-append (link-file-name
						      entry)
						     "#"
						     (index-entry-name
						      entry))))
	      (literal text))))))

(define (build-index nl)
  (let loop ((result '())
	     (nl nl))
    (if (node-list-empty? nl)
	result
	(loop (cons (make-index-entry (node-list-first nl)) result)
	      (node-list-rest nl)))))

(define (sort-index il)
  (letrec ((list-head (lambda (l n)
			(if (> n 0)
			    (cons (car l) (list-head (cdr l) (- n 1)))
			    '())))
	   (merge (lambda (il1 il2)
		    (cond ((null? il1) il2)
			  ((null? il2) il1)
			  ((string-ci>? (car (car il1)) (car (car il2)))
			   (cons (car il2) (merge il1 (cdr il2))))
			  (#t
			   (cons (car il1) (merge (cdr il1) il2)))))))
    (let* ((ll (length il))
	   (ldiv2 (quotient ll 2)))
      (if (> 2 ll)
	  il
	  (merge (sort-index (list-head il ldiv2))
		 (sort-index (list-tail il ldiv2)))))))

(define (output-index il)
  (let extract-and-append ((il il)
			   (result (empty-sosofo)))
    (if (null? il)
	result
	(extract-and-append (cdr il) (sosofo-append result (cdr (car il)))))))

(define (make-index)
  (make sequence
    (make element
      gi: "H1"
      (make element
	gi: "A"
	attributes: (list (list "name" "INDEXTOP"))
	(literal "Index")))
    (make element
      gi: "UL"
      (output-index
       (sort-index
	(build-index (select-elements (descendants (current-node))
				      "INDEXTERM")))))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; links & cross-references

(define (link-file-name target)
  (if %no-split-output%
      ""
      (string-append
       %output-basename%
       (cond ((equal? (gi target) "BOOK") "")
	     
	     ((equal? (gi target) "APPENDIX")
	      (string-append
	       "-APP-"
	       (format-number (child-number target) "A")))

	     ((or (equal? (gi target) "CHAPTER")
		  (equal? (gi target) "ARTICLE")
		  (equal? (gi target) "GLOSSARY"))
	      (string-append
	       "-"
	       (substring (gi target) 0 3)
	       "-"
	       (format-number (child-number target) "1")))

	     ((equal? (gi target) "REFENTRY")
	      (string-append
	       "-REF-"
	       (number->string (all-element-number target))))

	     ((ancestor-child-number "APPENDIX" target)
	      (string-append
	       "-APP-"
	       (format-number (ancestor-child-number "APPENDIX" target) "A")))
	     ((ancestor-child-number "CHAPTER" target)
	      (string-append
	       "-CHA-"
	       (format-number (ancestor-child-number "CHAPTER" target) "1")))

	     ((ancestor-child-number "ARTICLE" target)
	      (string-append
	       "-ART-"
	       (format-number (ancestor-child-number "ARTICLE" target) "1")))
	     
	     ((ancestor-child-number "GLOSSARY" target)
	      (string-append
	       "-GLO-"
	       (format-number (ancestor-child-number "GLOSSARY" target) "1")))

	     (#t 
	      (string-append
	       "-XXX-"
	       (number->string (all-element-number target)))))
       %output-suffix%)))

(element LINK
  (let* ((target (element-with-id (attribute-string "linkend")
				  (book-node)))
	 (target-file-name (link-file-name target)))
    (make element
      gi: "A"
      attributes: (list
		   (list "href" 
			 (string-append 
			  target-file-name
			  "#"
			  (attribute-string "linkend")))))))
(element ULINK
  (make element 
    gi: "A"
    attributes: (list
		 (list "href" (attribute-string "url")))))

(element XREF
  (let* ((linkend (attribute-string "linkend"))
	 (target (element-with-id linkend (book-node)))
	 (target-gi (gi target)))
    (make element
      gi: "A"
      attributes: (append
		   (list (list "href" (string-append (link-file-name target) 
						     "#"
						     linkend)))
		   (if (equal? target-gi "CO")
		       ;;; XREF must be in same file as CO for
		       ;;; backlink to work correctly
		       (list (list "name" (string-append "backlink-" linkend)))
		       '()))
      (if (equal? target-gi "CO")
	  (literal (or (attribute-string "label" target)
		       "Unlabeled CO"))
	  (with-mode extract-xref-text
	    (process-node-list target))))))

(mode extract-xref-text
  (default
    (let ((titles (select-elements (children (current-node)) "TITLE")))
      (if (node-list-empty? titles)
	  (literal (string-append "Reference to " (id)))
	  (with-mode extract-title-text
	    (process-node-list (node-list-first titles)))))))

(element CO
  (if (id)
      (make element
	gi: "A"
	attributes: (list (list "name" (id))
			  (list "href" (string-append "#backlink-" (id))))
	(make element
	  gi: "SPAN"
	  attributes: '(("class" "co"))
	  (literal (or (attribute-string "label")
		       "Unlabeled CO"))))
      (empty-sosofo)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; figures

(element FIGURE
  (let ((gubbins (make sequence
		   (make empty-element
		     gi: "P")
		   (make-anchor)
		   (process-children)
		   (make empty-element
		     gi: "P"))))
    (cond (%stylesheet-name%
	   (make element
	     gi: "DIV"
	     attributes: '(("class" "figure"))
	     gubbins))
	  (%centre-figures%
	   (make element
	     gi: "CENTER"
	     gubbins))
	  (#t gubbins))))

(element (FIGURE TITLE)
  (make sequence
    (make element
      gi: "H5"
      attributes: '(("class" "figure"))
      (make sequence
	(literal "Figure: ")
	(process-children-trim)))
    (make empty-element
      gi: "P")))

(element GRAPHIC
  (let ((img
	 (make sequence
	   (make empty-element
	     gi: "P")
	   (make empty-element
	     gi: "IMG"
	     attributes: (let ((filename (string-append
					  (or (and %graphic-directory%
						   (string-append %graphic-directory%
								  "/"))
					      "")
					  (attribute-string "fileref")
					  "."
					  (or (attribute-string "format")
					      %default-graphic-format%))))
			   (list (list "src" filename)
				 (list "alt" filename)))))))
    (if (equal?
	 (attribute-string "align")
	 "CENTER")
	(if %stylesheet-name%
	    (make element
	      gi: "DIV"
	      attributes: '(("class" "center"))
	      img)
	    (make element
	      gi: "CENTER"
	      img))
	img)))
  
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; tables

(define (make-table-attributes)
  (append (if (equal? (attribute-string "frame") "ALL")
	      '(("border" "1") ("cellpadding" "2"))
	      '(("border" "0")))
;	  (let ((wantcolsep (equal? (attribute-string "colsep") "1"))
;		(wantrowsep (equal? (attribute-string "rowsep") "1")))
;	    (list
;	     (cond ((and wantrowsep wantcolsep) '("rules" "all"))
;		   (wantcolsep '("rules" "cols"))
;		   (wantrowsep '("rules" "rows"))
;		   (#t '("rules" "none")))))
	  ))

(element TABLE
  (let ((table (make sequence
		 (make-anchor)
		 (let ((tab (make sequence
			      (make element
				gi: "TABLE"
				attributes: (make-table-attributes)
				(make sequence
				  (make element
				    gi: "CAPTION"
				    (make sequence
				      (literal "Table: ")
				      (with-mode extract-title-text
					(process-first-descendant "TITLE"))))
				  (with-mode footnote-ref
				    (process-children))))
			      (with-mode footnote-def
				(process-node-list (select-elements (descendants (current-node)) "FOOTNOTE")))))
		       (roleattr (or (attribute-string "role") "")))
		   (if (or
			(equal-ci? roleattr
				   "centre")
			(equal-ci? roleattr
				   "center"))
		       (if %stylesheet-name%
			   (make element
			     gi: "DIV"
			     attributes: '(("class" "center"))
			     tab)
			   (make element
			     gi: "CENTER"
			     tab))
		       tab)))))
    (if %stylesheet-name%
	(make element
	  gi: "DIV"
	  attributes: '(("class" "table"))
	  table)
	(make sequence
	  (make empty-element gi: "P")
	  table
	  (make empty-element gi: "P")))))

(element (TABLE TITLE) (empty-sosofo))

(element INFORMALTABLE
  (make sequence
    (make empty-element
      gi: "P")
    (let ((tab (make element
		 gi: "TABLE"
		 attributes: (make-table-attributes)
		 (process-children)))
	  (roleattr (or (attribute-string "role")
			"")))
      (if (or
	   (equal-ci? roleattr
		      "centre")
	   (equal-ci? roleattr
		      "center"))
	  (if %stylesheet-name%
	      (make element
		gi: "DIV"
		attributes: '(("class" "center"))
		tab)
	      (make element
		gi: "CENTER"
		tab))
	  tab))
    (make empty-element
      gi: "P")))

(element ENTRY
  (process-children-trim))

; routine to convert a string consisting of a number followed by a
; unit (mm, cm, etc.) into a string consisting of just a number (in
; pixel units)

(define (to-pixels lenstring)
  (let ((num (or (string->number lenstring) 0)))
    (number->string
     (truncate (* %display-dpi%
		  0.01388888
		  (if (quantity? num)
		      (let ((qstr (quantity->string num)))
			;; this assumes the unit string is "pt1"
			(string->number (substring qstr 0 (- (string-length qstr) 3))))
		      num))))))

;; hairy stuff to get table entries to understand various attributes

(define (process-table-entry entry entrycolnum span entrygi colspecs cols)
  (make sequence
    ;; loop through COLSPECs looking for one that has the right
    ;; column number
    (let loop ((specs colspecs)
	       (nextspeccolnum 1))
      (if (node-list-empty? specs)
	  ;; we didn't find a COLSPEC for this column
	  (let ((alignattr (or (inherited-attribute-string "align" entry)
			       "left")))
	    (make empty-element
	      gi: entrygi
	      attributes: (append (list (list "align" alignattr))
				  (if (> span 1)
				      (list (list "colspan" (number->string span)))
				      '()))))
	  ;; look at next COLSPEC and see if it is for this column the
	  ;; column number can be explicitly given with a 'colnum'
	  ;; attribute or implicitly one more than the last column
	  ;; number
	  (let* ((spec (node-list-first specs))
		 (colnumattr (attribute-string "colnum" spec))
		 (speccolnum (or (and colnumattr (string->number colnumattr))
				 nextspeccolnum)))
	    (if (equal? speccolnum entrycolnum)
		;; we matched column numbers so extract the align
		;; attribute and do the right thing
		(let ((alignattr (or (attribute-string "align" entry)
				     (attribute-string "align" spec)
				     (inherited-attribute-string "align" entry)
				     "left"))
		      (widthattr (attribute-string "colwidth" spec)))
		  (make empty-element
		    gi: entrygi
		    attributes: (append (if alignattr
					    (list (list "align" alignattr))
					    '())
					(if (and widthattr (= span 1))
					    (list (if %stylesheet-name%
						      (list "style" (string-append "width: " (to-pixels widthattr)))
						      (list "width" (to-pixels widthattr))))
					    '())
					(if (> span 1)
					    (list (list "colspan" (number->string span)))
					    '()))))
		;; didn't match column number so look at next in list
		(loop (node-list-rest specs)
		      (+ speccolnum 1))))))
    (process-node-list entry)))

;; determine the column number (1, 2, ...) that corresponds to the
;; supplied column name from the supplied COLSPECs. If none of the
;; COLSPECs has a matching name and the supplied column name is
;; actually a number, we return that number.

(define (find-column-number colspecs colname)
  ;; loop searches for a COLSPEC whose name matches the supplied
  ;; column name
  (let loop ((specs colspecs)
	     (colnum 1))
    (if (node-list-empty? specs)
	;; if the column name is actually a number use that,
	;; otherwise, just return 1
	(or (string->number colname) 1)
	(let* ((spec (node-list-first specs))
	       (nameattr (attribute-string "colname" spec))
	       (colnumattr (attribute-string "colnum" spec))
	       (speccolnum (if colnumattr (string->number colnumattr) colnum)))
	  (if (equal? colname nameattr)
	      speccolnum
	      (loop (node-list-rest colspecs)
		    (+ speccolnum 1)))))))

;; determine the number of columns spanned by the given table entry
(define (columns-spanned entry)
  (let* ((colspecs (select-elements (ancestor "TGROUP" entry) "COLSPEC"))
	 (namest (attribute-string "namest" entry))
	 (nameend (attribute-string "nameend" entry)))
    (if (and namest nameend)
	(+ (- (find-column-number colspecs nameend)
	      (find-column-number colspecs namest))
	   1)
	1)))

(define (process-table-row sofar row entrygi entryprocessor)
  (sosofo-append sofar
		 (make empty-element gi: "TR")
		 (let loop ((entries (children row))
			    (result (empty-sosofo))
			    (colnum 1))
		   (if (node-list-empty? entries)
		       result
		       (let* ((entry (node-list-first entries))
			      (span (columns-spanned entry)))
			 (loop (node-list-rest entries)
			       (sosofo-append result
					      (entryprocessor entry
							      colnum
							      span
							      entrygi))
			       (+ colnum span)))))))

(define (process-table-group sofar group entrygi rowreducer)
  (sosofo-append sofar 
		 (node-list-reduce (select-elements (children group) "ROW")
				   (lambda (sofar new)
				     (rowreducer sofar new entrygi))
				   (empty-sosofo))))

(define (process-tgroup)
  (let* ((colspecs (select-elements (children (current-node)) "COLSPEC"))
	 (cols (string->number (attribute-string "cols")))
	 (entryprocessor (lambda (new colnum span entrygi)
			   (process-table-entry new colnum span entrygi colspecs cols)))
	 (rowreducer (lambda (sofar new entrygi)
		       (process-table-row sofar new entrygi entryprocessor)))
	 (groupreducer (lambda (sofar new entrygi)
			 (process-table-group sofar new entrygi rowreducer))))
    (make sequence
      (node-list-reduce (select-elements (children (current-node)) "THEAD")
			(lambda (sofar new)
			  (groupreducer sofar new "TH"))
			(empty-sosofo))
      (node-list-reduce (select-elements (children (current-node)) "TBODY")
			(lambda (sofar new)
			  (groupreducer sofar new "TD"))
			(empty-sosofo))
      (node-list-reduce (select-elements (children (current-node)) "TFOOT")
			(lambda (sofar new)
			  (groupreducer sofar new "TH"))
			(empty-sosofo)))))

(element TGROUP
  (process-tgroup))

(element ENTRYTBL
  (make element
    gi: "TABLE"
    attributes: (make-table-attributes)
    (process-tgroup)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; book info

(element BOOKINFO
  (make sequence
    (if %stylesheet-name%
	(make element
	  gi: "DIV"
	  attributes: '(("class" "bookinfo"))
	  (process-children))
	(make element
	  gi: "CENTER"
	  (process-children)))
    (cond ((not %no-make-toc%)
	   (make sequence
	     (make-fat-rule)
	     (make element
	       gi: "H2"
	       (literal "Contents"))
	     (make element
	       gi: "ul"
	       (with-mode make-toc-links
		 (process-node-list (book-node))))))
	  (#t (empty-sosofo)))))


(element AUTHORGROUP
  (let ((reducer (lambda (sofar new)
		   (sosofo-append sofar (make element
					  gi: "H2"
					  attributes: '(("class" "bookinfo"))
					  (process-node-list new))))))
    (make sequence
      (node-list-reduce (select-elements (children (current-node)) "AUTHOR")
			reducer
			(empty-sosofo))
      (node-list-reduce (select-elements (children (current-node)) "EDITOR")
			reducer
			(empty-sosofo))
      (node-list-reduce (select-elements (children (current-node)) "CORPAUTHOR")
			reducer
			(empty-sosofo)))))

(element (BIBLIOENTRY AUTHORGROUP)
  (let ((reducer (lambda (sofar new)
		   (sosofo-append sofar (make element
					  gi: "H3"
					  (process-node-list new))))))
    (make sequence
      (node-list-reduce (select-elements (children (current-node)) "AUTHOR")
			reducer
			(empty-sosofo))
      (node-list-reduce (select-elements (children (current-node)) "EDITOR")
			reducer
			(empty-sosofo))
      (node-list-reduce (select-elements (children (current-node)) "CORPAUTHOR")
			reducer
			(empty-sosofo)))))

(element (BOOKINFO DATE)
  (process-children-trim))

(element (BOOKINFO EDITION)
  (make sequence
    (literal "Edition ")
    (process-children-trim)))

(element COPYRIGHT
  (make element
    gi: "H4"
    (make sequence
      (make entity-ref
	name: "copy")
      (process-matching-children "HOLDER")
      (process-matching-children "YEAR"))))

(element HOLDER
  (make sequence
    (literal " ")
    (process-children-trim)))

(element YEAR
  (make sequence
    (literal " ")
    (process-children-trim)))

(element CORPAUTHOR
  (process-children-trim))

(element AUTHOR
  (process-children-trim))

(element EDITOR
  (process-children-trim))

(element CONFGROUP
  (process-children-trim))

(element CONFTITLE
  (make sequence
    (make empty-element
      gi: "BR")
    (make element gi: "I" (process-children))))

(element CONFDATES
  (make sequence
    (make empty-element
      gi: "BR")
    (process-children)))

(element HONORIFIC
  (make sequence
    (process-children-trim)
    (literal " ")))

(element FIRSTNAME
  (make sequence
    (process-children-trim)
    (literal " ")))

(element OTHERNAME
  (make sequence
    (process-children-trim)
    (literal " ")))

(element SURNAME
  (make sequence
    (process-children-trim)
    (literal " ")))

(element LINEAGE
  (make sequence
    (process-children-trim)
    (literal " ")))

(element TRADEMARK (process-children))

(element PUBLISHERNAME (process-children))

(element BIBLIOENTRY (process-children))

(element ACRONYM (process-children))

(element RELEASEINFO
  (make sequence
    (make empty-element
      gi: "BR")
    (make element gi: "B")))

(element AFFILIATION
  (make sequence
    (make element
      gi: "I")))

(element ORGNAME
  (make sequence
    (make empty-element
      gi: "BR")
    (process-children)))

(element JOBTITLE
  (make sequence
    (make empty-element
      gi: "BR")
    (process-children)))

(element ORGDIV
  (make sequence
    (make empty-element
      gi: "BR")
    (process-children)))

(element PUBLISHER
  (make sequence
    (make empty-element
      gi: "BR")
    (process-children)))

(element ISBN
  (make sequence
    (make empty-element
      gi: "BR")
    (process-children)))

(element PUBDATE
  (make sequence
    (make empty-element
      gi: "BR")
    (process-children)))

(element REVHISTORY
  (empty-sosofo))

(element LEGALNOTICE
  (make sequence
    (if %stylesheet-name%
	(make element
	  gi: "DIV"
	  attributes: '(("align" "left")))
	(process-children))))

(element KEYWORDSET
  (empty-sosofo))

(element SUBJECTSET
  (empty-sosofo))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; TOC

(element LOF (empty-sosofo))

(element LOT (empty-sosofo))

(element TOC (empty-sosofo))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; DIY TOC

(mode make-toc-links
  (element (BOOK)
    (sosofo-append
     (process-children)
     (cond ((not %no-make-index%)
	    (make sequence
	      (make empty-element
		gi: "LI")
	      (make element
		gi: "A"
		attributes: (list (list "href"
					(cond (%no-split-output% "#INDEXTOP")
					      (#t
					       (string-append (index-file-name)
							      "#INDEXTOP")))))
		(literal "Index"))))
	   (#t (empty-sosofo)))))
  (element (ARTICLE)
    (process-matching-children "SECT1"))
  (element (CHAPTER)
    (make-major-div-toc-links))
  (element (APPENDIX)
    (make-major-div-toc-links))
  (element (GLOSSARY)
    (make-major-div-toc-links))
  (element (SECT1)
    (make sequence
      (make empty-element
	gi: "LI")
      (let ((title-text (with-mode extract-title-text
			  (process-first-descendant "TITLE"))))
	(make element
	  gi: "A"
	  attributes: (list (list "href" (string-append (link-file-name (current-node))
							"#"
							(gi)
							(number->string (all-element-number (current-node))))))
	  title-text))
      (let ((refentries (select-elements (children (current-node)) "REFENTRY")))
	(if (node-list-empty? refentries)
	    (empty-sosofo)
	    (make element
	      gi: "ul"
	      (with-mode make-toc-links (process-node-list refentries)))))))
  (element (REFENTRY)
    (make sequence
      (make empty-element
	gi: "LI")
      (let ((title-text (process-first-descendant "REFMETA")))
	(make element
	  gi: "A"
	  attributes: (list (list "href" (string-append (link-file-name (current-node))
							"#"
							(gi)
							(number->string (all-element-number (current-node))))))
	  title-text))))

  (default
    (empty-sosofo)))

(define (make-major-div-toc-links)
  (make sequence
    (make empty-element
      gi: "LI")
    (let ((title-text
	   (cond ((equal? (gi) "CHAPTER")
		  (make sequence
		    (literal (string-append "Chapter "
					    (format-number
					     (element-number (current-node))
					     "1")
					    " - "))
		    (with-mode extract-title-text
		      (process-first-descendant "TITLE"))))

		 ((equal? (gi) "APPENDIX")
		  (make sequence
		    (literal
		     (string-append "Appendix "
				    (format-number
				     (element-number (current-node))
				     "A")
				    " - "))
		    (with-mode extract-title-text
		      (process-first-descendant "TITLE"))))

		 ((equal? (gi) "GLOSSARY") (literal "Glossary"))
		     
		 (#t
		  (with-mode extract-title-text
		    (process-first-descendant "TITLE"))))))
      (make element
	gi: "A"
	attributes: (list (list "href" (string-append (link-file-name (current-node))
						      "#"
						      (gi)
						      (number->string (all-element-number (current-node))))))
	title-text))
    (let ((wanted (node-list-reduce (children (current-node))
				    (lambda (sofar new)
				      (if (or (equal? (gi new) "SECT1")
					      (equal? (gi new) "REFENTRY"))
					  (node-list sofar new)
					  sofar))
				    (node-list))))
      (if (node-list-empty? wanted)
	(empty-sosofo)
	(make element
	    gi: "UL"
	    (with-mode make-toc-links (process-node-list wanted)))))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; make the unimplemented bits stand out

(default
  (make element
    gi: "FONT"
    attributes: '(("color" "red"))
    (make sequence
      (literal (string-append "<" (gi) ">"))
      (process-children)
      (literal (string-append "</" (gi) ">")))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; standard subroutines

(define (node-list-reduce nl combine init)
  (if (node-list-empty? nl)
      init
      (node-list-reduce (node-list-rest nl)
                        combine
                        (combine init (node-list-first nl)))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; various homebrew subroutines

(define (book-node)
  (cond ((equal? (gi) "BOOK") (current-node))
	(#t (ancestor "BOOK"))))

(define (make-fat-rule)
  (make empty-element
    gi: "HR"
    attributes: (if %stylesheet-name%
		    '(("class" "fat"))
		    '(("size" "5")))))

(define (make-thin-rule)
  (make empty-element
    gi: "HR"
    attributes: (if %stylesheet-name%
		    '(("class" "thin"))
		    '(("size" "2")))))

(define (index-file-name)
  (string-append %output-basename%
		 "-IND"
		 %output-suffix%))

(define (chap-app-head-label chap-or-app)
  (let ((label
	 (attribute-string "label" (ancestor chap-or-app))))
    (string-append 
     chap-or-app
     " "
     (if label
	 (if (equal? label "auto")
	     (format-number
	      (element-number (ancestor chap-or-app))
	      (if (equal? chap-or-app "Chapter") "1" "A"))
	   label)
       (format-number
	(element-number (ancestor chap-or-app))
	(if (equal? chap-or-app "Chapter") "1" "A")))
     ". ")))

(define (make-anchor)
  (make sequence
    (make element
      gi: "A"
      attributes: (list (list "name" (string-append (gi)
						    (number->string (all-element-number (current-node))))))
      (literal ""))
    (if (id)
	(make element
	  gi: "A"
	  attributes: (list (list "name" (id)))
	  (literal ""))
	(empty-sosofo))))

(define (make-color-para color)
  (if %stylesheet-name%
      (make element
	gi: "DIV" 
	attributes: (list (list "class" (string-append "{color: " color "}")))
	(make-special-para))
      (make element
	gi: "FONT"
	attributes: (list (list "color" color))
	(make-special-para))))

(define (make-special-para)
  (make sequence
    (make empty-element
      gi: "P")
    (make element
      gi: "B"
      (literal (string-append (gi) ":")))
    (make element
      gi: "BLOCKQUOTE"
      (process-children))))

(define (maybe-bold-children)
  (cond ((equal? (attribute-string "role")
		 "bold")
	 (make element
	   gi: "B"
	   (process-children-trim)))
	(#t (process-children-trim))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; the end

