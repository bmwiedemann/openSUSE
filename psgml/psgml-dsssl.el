;; psgml-dsssl.el --- create a skeleton DSSSL spec for an SGML document.
;; $Id: psgml-dsssl.el,v 1.2 1996/10/19 17:24:24 david Exp david $
;; Copyright (C) 1996 David Megginson.  Free redistribution permitted.
;; USE AT YOUR OWN RISK!
;;
;; Author: David Megginson (dmeggins@microstar.com)


;;; Commentary:

;; Installation:
;;
;; This file requires Gnu Emacs 19.* or XEmacs, together with Lennart
;; Staflin's PSGML mode (tested with version 1a12).
;;
;; Install this file somewhere on your load path, byte-compile it, and
;; include the following in your .emacs or site-start.el file:
;;
;;   (autoload 'sgml-dsssl-make-spec "psgml-dsssl" nil t)
;;
;; Now, whenever you are editing an SGML document with PSGML, you can
;; type
;;
;;    M-x sgml-dsssl-make-spec
;;
;; to create a skeleton DSSSL style spec in a temporary buffer
;; "**DSSSL**" (overwriting any existing spec).  You may save the
;; buffer to a file and edit it as you wish.
;;
;;
;; Operation:
;;
;; This package will generate an element construction rule for every
;; element type which could appear in the SGML document, whether it
;; actually appears or not -- it does so by starting with the element
;; type of the document's root element, then performing a depth-first
;; traversal of the DTD tree.  Any element types which are not
;; reachable from the root will be excluded.
;;
;; The first instance of each element class in the DTD tree will
;; determine its context, and thus, its default flow-object class.
;; The contexts are as follow:
;;
;; 1) The root element of the document (default: simple-page-sequence).
;; 2) The element appears in mixed content or contains PCDATA content
;;    (default: sequence).
;; 3) The element contains mixed content and appears in element content
;;    (default: paragraph).
;; 4) The element contains only element content
;;    (default: display-group).
;; 5) The element is EMPTY (default: sequence).
;;
;; These will work well with some DTDs, but the assumptions will fall
;; apart quickly for others, especially HTML (which allows mixed
;; content almost everywhere).  You can change the default flow-object
;; classes for each of these using configuration variables, as you can
;; change the default document-type declaration at the top of the
;; specification.
;;


;;; Code:

(require 'psgml-parse)
(autoload 'sgml-map-element-types "psgml-info" nil t)
(autoload 'sgml-eltype-refrenced-elements "psgml-info" nil t)

;;
;; Global configuration variables -- change as appropriate.
;;

					; Default to the style-sheet
					; DTD from the jade distribution.
(defvar sgml-dsssl-prolog
  "<!DOCTYPE style-sheet PUBLIC \"-//James Clark//DTD DSSSL Style Sheet//EN\">\n\n"
  "Prolog for generated DSSSL scripts.")

(defvar sgml-dsssl-root-foc "simple-page-sequence"
  "The default flow-object class for the root element type.")

(defvar sgml-dsssl-mixed-foc "paragraph"
  "The default flow-object class for an element type with mixed content.")

(defvar sgml-dsssl-element-foc "display-group"
  "The default flow-object class for an element type with element content.")

(defvar sgml-dsssl-data-foc "sequence"
  "The default flow-object class for an element type with data content.")

(defvar sgml-dsssl-empty-foc "sequence"
  "The default flow-object class for an element type with EMPTY content.")

;;;
;;; Generate a skeleton DSSSL spec.
;;;
(defun sgml-dsssl-make-spec ()
  "Generate a skeleton DSSSL style spec for the SGML document in a buffer.
The output will always go into a buffer named \"**DSSSL**\"."

  (interactive)
  (sgml-need-dtd)
  (let ((root (symbol-name (sgml-element-name (sgml-top-element))))
	(max-lisp-eval-depth 10000)
	(elements-seen ()))
    (with-output-to-temp-buffer "**DSSSL**"
      (princ sgml-dsssl-prolog)
      (sgml-dsssl-make-rule (sgml-lookup-eltype root)))))

(defun sgml-dsssl-make-rule (eltype &optional parent-mixed)
  "Generate an element-construction rule, then recurse to any children."

  (let ((name (sgml-eltype-name eltype))
	(foc
	 (cond ((equal elements-seen ())
		sgml-dsssl-root-foc)
	       ((or (equal (sgml-eltype-refrenced-elements eltype)
			   (list (intern "#PCDATA")))
		    parent-mixed)
		sgml-dsssl-data-foc)
;	       ((sgml-eltype-mixed eltype)
;		sgml-dsssl-mixed-foc)
	       ((equal (sgml-eltype-refrenced-elements eltype) ())
		sgml-dsssl-empty-foc)
	       (t sgml-dsssl-element-foc))))

    (push name elements-seen)
    
;    (princ ";; Contents: ")
;    (mapc (function (lambda (child) (princ child) (princ " ")))
;	  (sgml-eltype-refrenced-elements eltype))
;    (princ "\n")
    (princ (format "(element %s\n  (make %s\n    (process-children)))\n\n"
		   (upcase name) foc)))
  (mapcar (function
	   (lambda (el)
	     (if (and (not (memq (sgml-eltype-name el) elements-seen))
		      (not (string= (sgml-eltype-name el) "#PCDATA")))
		 (sgml-dsssl-make-rule el (sgml-eltype-mixed eltype)))))
	  (sgml-eltype-refrenced-elements eltype)))
