<!DOCTYPE style-sheet PUBLIC "-//James Clark//DTD DSSSL Style Sheet//EN" >

<style-sheet>
<style-specification id="params">
<style-specification-body>
;;
;; linuxdoc to docbook transformation stylesheet
;;
;; Charles Bozeman
;;
;; $Id: ld2db.dsl,v 1.2 1998/10/05 18:40:46 cg Exp $
;;
;; This transformation stylesheet attempts to "pretty print" the
;; resulting sgml document.
;;
;; Several of the procedure are copied from other sources such as
;; Norm Walsh's docbook stylesheets, Paul Prescod's transform.dsl,
;; and Mulberry Technologies DSSSL pages.
;;
;; Invocation example:
;; jade -t sgml -d ld2db.dsl#db in.sgm >out.sgm

;; ============================ PARAMETERS ==============================

(define %transform-element-BF% "Emphasis")
(define %transform-element-SL% "Emphasis")
(define %transform-element-TT% "Literal")
(define %ids-repl-list% `("0" "i-0" "1" "i-1" "2" "i-2" "3" "i-3"
                          "4" "i-4" "5" "i-5" "6" "i-6" "7" "i-7"
                          "8" "i-8" "9" "i-9"))

</style-specification-body>
</style-specification>

<style-specification id="library" >
<style-specification-body>

(define debug
  (external-procedure "UNREGISTERED::James Clark//Procedure::debug"))

;(declare-characteristic preserve-sdata?
;  "UNREGISTERED::James Clark//Characteristic::preserve-sdata?"
;  #f)


;; ====================== Library Functions     ========================

(define (node-list-first-element nodelist)
  ;; REFENTRY lib-node-list-first-element
  ;; PURP Return the first element node in a node list
  ;; DESC
  ;; This function returns the first node in a node list which is
  ;; an element (as opposed to a PI or anything else that might appear
  ;; in a node list).
  ;; /DESC
  ;; /REFENTRY
  (let loop ((nl nodelist))
    (if (node-list-empty? nl)
        (empty-node-list)
        (if (gi (node-list-first nl))
            (node-list-first nl)
            (loop (node-list-rest nl))))))
 
(define (ipreced nl)
  ;; REFENTRY lib-ipreced
  ;; PURP Implements ipreced as per ISO/IEC 10179:1996
  ;; DESC
  ;; Implements 'ipreced' as per ISO/IEC 10179:1996
  ;; /DESC
  ;; AUTHOR From ISO/IEC 10179:1996
  ;; /REFENTRY
  (node-list-map (lambda (snl)
                 (let loop ((prev (empty-node-list))
                            (rest (siblings snl)))
                   (cond ((node-list-empty? rest)
                          (empty-node-list))
                         ((node-list=? (node-list-first rest) snl)
                          prev)
                         (else
                          (loop (node-list-first rest)
                                (node-list-rest rest))))))
                 nl))
 

(define (ifollow nl)
  ;; REFENTRY
  ;; PURP Implements ifollow as per ISO/IEC 10179:1996
  ;; DESC
  ;; Implements 'ifollow' as per ISO/IEC 10179:1996
  ;; /DESC
  ;; AUTHOR From ISO/IEC 10179:1996
  ;; /REFENTRY
  (node-list-map (lambda (snl)
                   (let loop ((rest (siblings snl)))
                     (cond ((node-list-empty? rest)
                            (empty-node-list))
                           ((node-list=? (node-list-first rest) snl)
                            (node-list-first (node-list-rest rest)))
                           (else
                            (loop (node-list-rest rest))))))
                 nl))
 
(define (siblings snl)
  ;; REFENTRY
  ;; PURP Implements siblings as per ISO/IEC 10179:1996
  ;; DESC
  ;; Implements 'siblings' as per ISO/IEC 10179:1996
  ;; /DESC
  ;; AUTHOR From ISO/IEC 10179:1996
  ;; /REFENTRY
  (children (parent snl)))
 
;; ======================================================================
 
(define (sgml-root-element)
  ;; REFENTRY
  ;; PURP Returns the node that is the root element of the current document
  ;; DESC
  ;; Return the root element of the document by walking up from
  ;; wherever we are.  (Isn't this built-in to DSSSL somehow???)
  ;; /DESC
  ;; /REFENTRY
  (let loop ((root (current-node)))
    (if (node-list-empty? (parent root))
        root
        (loop (parent root)))))
 
;; ======================================================================
 
(define (repl-substring? string target pos)
  ;; REFENTRY lib-repl-substring-p
  ;; PURP Returns true if the specified substring can be replaced
  ;; DESC
  ;; Returns '#t' if 'target' occurs at 'pos' in 'string'.
  ;; /DESC
  ;; /REFENTRY
  (let* ((could-match (<= (+ pos (string-length target))
                         (string-length string)))
         (match (if could-match
                    (substring string pos (+ pos (string-length target))) "")))
    (and could-match (string=? match target))))
 
(define (repl-substring string target repl pos)
  ;; REFENTRY lib-repl-substring
  ;; PURP Replace substring in a string
  ;; DESC
  ;; Replaces 'target' with 'repl' in 'string' at 'pos'.
  ;; /DESC
  ;; /REFENTRY
  (let ((matches (repl-substring? string target pos)))
    (if matches
        (string-append
         (substring string 0 pos)
         repl
         (substring string
                    (+ pos (string-length target))
                    (string-length string)))
        string)))
 
(define (repl-substring-list? string replace-list pos)
  ;; REFENTRY lib-repl-substring-list-p
  ;; PURP Perform repl-substring? with a list of target/replacement pairs
  ;; DESC
  ;; Returns '#t' if any target in 'replace-list' occurs at 'pos' in 'string'.
  ;; ARGS
  ;; ARG 'string'
  ;; The string in which replacement should be tested.
  ;; /ARG
  ;; ARG 'replace-list'
  ;; A list of target/replacement pairs.  This list is just a list of
  ;; strings, treated as pairs.  For example, '("was" "x" "is" "y")'.
  ;; In this example, 'was' may be replaced by 'x' and 'is' may be
  ;; replaced by 'y'.
  ;; /ARG
  ;; ARG 'pos'
  ;; The location within 'string' where the test will occur.
  ;; /ARG
  ;; /ARGS
  ;; /DESC
  ;; EXAMPLE
  ;; '(repl-substring-list? "this is it" ("was" "x" "is" "y") 2)'
  ;; returns '#t': "is" could be replaced by "y".
  ;; /EXAMPLE
  ;; /REFENTRY
  (let loop ((list replace-list))
    (let ((target (car list))
          (repl   (car (cdr list)))
          (rest   (cdr (cdr list))))
      (if (repl-substring? string target pos)
          #t
          (if (null? rest)
              #f
              (loop rest))))))
 
(define (repl-substring-list-target string replace-list pos)
  ;; REFENTRY lib-repl-substring-list-target
  ;; PURP Return the target that matches in a string
  ;; DESC
  ;; Returns the target in 'replace-list' that matches in 'string' at 'pos'
  ;; See also 'repl-substring-list?'.
  ;; /DESC
  ;; /REFENTRY
  (let loop ((list replace-list))
    (let ((target (car list))
          (repl   (car (cdr list)))
          (rest   (cdr (cdr list))))
      (if (repl-substring? string target pos)
          target
          (if (null? rest)
              #f
              (loop rest))))))
 
(define (repl-substring-list-repl string replace-list pos)
  ;; REFENTRY lib-repl-substring-list-repl
  ;; PURP Return the replacement that would be used in the string
  ;; DESC
  ;; Returns the replacement in 'replace-list' that would be used for the
  ;; target that matches in 'string' at 'pos'
  ;; See also 'repl-substring-list?'.
  ;; /DESC
  ;; /REFENTRY
  (let loop ((list replace-list))
    (let ((target (car list))
          (repl   (car (cdr list)))
          (rest   (cdr (cdr list))))
      (if (repl-substring? string target pos)
          repl
          (if (null? rest)
              #f
              (loop rest))))))
 
(define (repl-substring-list string replace-list pos)
  ;; REFENTRY lib-repl-substring-list
  ;; PURP Replace the first target in the replacement list that matches
  ;; DESC
  ;; Replaces the first target in 'replace-list' that matches in 'string'
  ;; at 'pos' with its replacement.
  ;; See also 'repl-substring-list?'.
  ;; /DESC
  ;; /REFENTRY
  (if (repl-substring-list? string replace-list pos)
      (let ((target (repl-substring-list-target string replace-list pos))
            (repl   (repl-substring-list-repl string replace-list pos)))
        (repl-substring string target repl pos))
      string))
 
(define (string-replace string target repl)
  ;; REFENTRY lib-string-replace
  ;; PURP Replace all occurances of a target substring in a string
  ;; DESC
  ;; Replaces all occurances of 'target' in 'string' with 'repl'.
  ;; /DESC
  ;; /REFENTRY
  (let loop ((str string) (pos 0))
    (if (>= pos (string-length str))
        str
        (loop (repl-substring str target repl pos)
              (if (repl-substring? str target pos)
                  (+ (string-length repl) pos)
                  (+ 1 pos))))))
 
(define (node-list-first-element-after-match nodelist match-el)
  ;; REFENTRY lib-node-list-first-element
  ;; PURP Return the first element node in a node list after given element
  ;; DESC
  ;; This function returns the first node in a node list which appears
  ;; after the given match element n element (as opposed to a PI or
  ;; aanything else that might appear n a node list).
  ;; /DESC
  ;; /REFENTRY
  (let loop ((nl nodelist))
    (if (node-list-empty? nl)
        (empty-node-list)
        (if (equal? (gi (node-list-first nl)) match-el)
            (let loop-2 ((nl (node-list-rest nl)))
              (if (node-list-empty? nl)
                  (empty-node-list)
                  (if (gi (node-list-first nl))
                      (node-list-first nl)
                      (loop-2 (node-list-rest nl)))))
            (loop (node-list-rest nl))))))

</style-specification-body>
</style-specification>

<style-specification id="common" >
<style-specification-body>

;; ============================ TOP LEVEL ==============================

(declare-flow-object-class formatting-instruction
  "UNREGISTERED::James Clark//Flow Object Class::formatting-instruction")
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

(declare-characteristic preserve-sdata?
  "UNREGISTERED::James Clark//Characteristic::preserve-sdata?" #t)


(define (start-tag str)
  (string-append "<" str ">" ))

(define (end-tag str)
  (string-append "</" str ">"))

(define (comment-tag str)
  (string-append "<" "--" str "--" ">"))

; newline
;(define %RE% "\U-000D")
(define %RE% "&#RE;")

(define (write-string str)
  (make formatting-instruction
        data: str))

(define (write-string-RE str)
  (make formatting-instruction
        data: (string-append str %RE%)))

(define (RE-write-string str)
  (make formatting-instruction
        data: (string-append %RE% str)))

(define (RE-write-string-RE str)
  (make formatting-instruction
        data: (string-append %RE% str %RE%)))

; procedure for enclosing inline data between pre and aft text
(define ($make-inline$ pre aft)
  (sosofo-append
    (write-string pre)
    (process-children)
    (write-string aft)))

; procedure for enclosing a block of data between pre and aft text
; Note: always terminates with a newline
(define ($make-block$ pre aft)
  (sosofo-append
    (write-string pre)
    (process-children)
    (write-string-RE aft)))

(define ($remap-attr$ el)
  (cons (list "REMAP" el) `()))

(define (attr-name lis)
  (car (car lis)))

(define (attr-value lis)
  (car (cdr (car lis))))

; given a list of attribute pairs, output them
(define ($out-attributes$ attlist)
  (let loop ((rest attlist))
    (if (equal? rest `())
        (write-string ">")
        (make sequence
          (write-string (string-append " " 
                                       (attr-name rest) 
                                       "=\"" 			; open quote
                                       (attr-value rest)
                                       "\""))			; close quote
          (loop (cdr rest))))))


(define (make-block-element #!optional #!key gind attributes
                            (sosofo (process-children)))
  (let ((gi-nd (if gind gind (gi (current-node)))))
    (sosofo-append
      (RE-write-string (string-append "<" gi-nd))
      (if attributes
          ($out-attributes$ attributes)
          (write-string-RE ">"))
      sosofo
      (RE-write-string-RE (end-tag gi-nd)))))

(define (make-comment-element #!optional #!key gind attributes
                            (sosofo (process-children)))
  (let ((gi-nd (if gind gind (gi (current-node)))))
    (sosofo-append
      (RE-write-string (string-append "<" "!--" gi-nd "--" ">"))
      (if attributes
          ($out-attributes$ attributes)
          (write-string-RE ">"))
      sosofo
      (RE-write-string-RE (string-append "<" "!--" "/" gi-nd "--" ">")))))

(define (make-inline-element #!optional #!key gind attributes
                            (sosofo (process-children)))
  (let ((gi-nd (if gind gind (gi (current-node)))))
    (sosofo-append
      (write-string (string-append "<" gi-nd))
      (if attributes
          ($out-attributes$ attributes)
          (write-string ">"))
      sosofo
      (write-string (end-tag gi-nd)))))

(define (make-empty-inline-element #!optional #!key gind attributes
                            (sosofo (process-children)))
  (let ((gi-nd (if gind gind (gi (current-node)))))
    (sosofo-append
      (write-string (string-append "<" gi-nd))
      (if attributes
          ($out-attributes$ attributes)
          (write-string ">"))
      sosofo)))

(define (make-line-element #!optional #!key gind attributes
                            (sosofo (process-children)))
  (let ((gi-nd (if gind gind (gi (current-node)))))
    (sosofo-append
      (RE-write-string (string-append "<" gi-nd))
      (if attributes
          ($out-attributes$ attributes)
          (write-string ">"))
      sosofo
      (write-string-RE (end-tag gi-nd)))))

(define (make-empty-line-element #!optional #!key gind attributes
                            (sosofo (process-children)))
  (let ((gi-nd (if gind gind (gi (current-node)))))
    (sosofo-append
      (RE-write-string (string-append "<" gi-nd))
      (if attributes
          ($out-attributes$ attributes)
          (write-string ">"))
      sosofo)))

</style-specification-body>
</style-specification>

<style-specification id="db" use="common library params">
<style-specification-body>

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; From the DSSSL Cookbook
;; http://www.mulberrytech.com/dsssl/dsssldoc/cookbook/cookbook.html
;; Default rule

(default (output-element))

(define (output-element #!optional (node (current-node)))
  (if (node-property "must-omit-end-tag?" node)
      (make empty-element
            attributes: (copy-attributes))
      (make element
            attributes: (copy-attributes))))

(define (copy-attributes #!optional (nd (current-node)))
  (let loop ((atts (named-node-list-names (attributes nd))))
    (if (null? atts)
        '()
        (let* ((name (car atts))
               (value (attribute-string name nd)))
          (if value
              (cons (list name value)
                    (loop (cdr atts)))
              (loop (cdr atts)))))))


(element LINUXDOC (process-children))

(element ARTICLE 
  (make sequence
    (make document-type name: "Article"
                        public-id: "-//Davenport//DTD DocBook V3.0//EN")
    (make-block-element gind: "Article")))

(element BOOK
  (make sequence
    (make document-type name: "Book" 
                        public-id: "-//Davenport//DTD DocBook V3.0//EN" )
    (make-block-element gind: "Book")))

(element REPORT
  (make sequence
    (make document-type name: "Book" 
                        public-id: "-//Davenport//DTD DocBook V3.0//EN" )
    (make-block-element gind: "Book" attributes: `(("remap" "report")))))

(element TITLEPAG
  (if (equal? (gi (parent (current-node))) "ARTICLE")
      (make-block-element gind: "ArtHeader")
      (make-block-element
        gind: "BookInfo"
        sosofo: (make-block-element
                  gind: "BookBiblio"))))

(element DATE (make-line-element gind: "PubDate"))

; this may need to be fixed-up manually
(element NAME
  (let ((htmlurl-nl (select-elements (children (current-node)) "HTMLURL")))
    (make sequence
      (make-line-element gind: "FirstName")
      (if (node-list-empty? htmlurl-nl)
          (empty-sosofo)
          (make-block-element gind: "AuthorBlurb"
            sosofo: (make-line-element gind: "Para"
                      sosofo: (with-mode name-htmlurl
                                (process-node-list htmlurl-nl))))))))

;; does'nt work well, correct by hand
;(element INST (make element gi: "OrgName"))
(element INST (empty-sosofo))

(element ABSTRACT
  (make-block-element
    gind: "Abstract"
    sosofo: (make-block-element gind: "Para")))

;; Norm's stylesheets build this stuff
(element TOC (empty-sosofo))
(element LOT (empty-sosofo))
(element LOF (empty-sosofo))

(element TITLE (make-line-element gind: "Title"))

;; ========================== BLOCK ELEMENTS ============================

(element P
  (let ((para-empty (if (and (equal? 0 (string-length (data (current-node))))
                             (node-list-empty? (children (current-node))))
                        #t #f)))
    (if para-empty
        (empty-sosofo)		; don't leave empty paragraphs lying around!
        (make-block-element gind: "Para" ))))

(element APPENDIX
  (let* ((follow-nd (ifollow (current-node)))
         (chapt-next (if (equal? (gi follow-nd) "CHAPT") #t #f)))
    (if chapt-next
        (empty-sosofo)
        (make-empty-line-element
          sosofo: (make-line-element
                    gind: "Title"
                    sosofo: (literal "Appendix"))))))

(element CHAPT
  (let* ((preced-nd (ipreced (current-node)))
         (apdx-prev (if (equal? (gi preced-nd) "APPENDIX") #t #f)))
    (if apdx-prev
        ($make-sect$ "Appendix")
        ($make-sect$ "Chapter"))))

(element SECT ($make-sect$ "Sect1"))
(element SECT1 ($make-sect$ "Sect2"))
(element SECT2 ($make-sect$ "Sect3"))
(element SECT3 ($make-sect$ "Sect4"))
(element SECT4 ($make-sect$ "Sect5"))

;; build a section (or chapter)
(define ($make-sect$ gi-name)
  (let ((attrs ($get-sect-id$ (current-node))))
    (make-block-element gind: gi-name attributes: attrs)))


;; look for a label element in a heading element then put the 'id' in
;; the section (or chapter) attribute
(define ($get-sect-id$ nd)
  (let* ((heading (node-list-first
                    (select-elements (children nd) "HEADING")))
         (label (select-elements (children heading) "LABEL"))
         (label-id (if (node-list-empty? label)
                       #f
                       ($fix-ids$ 
                         (attribute-string "id" (node-list-first label)))))
         (attrs (if label-id
                    (cons (list "id" ($fix-ids$ label-id)) (copy-attributes))
                    (copy-attributes))))
    attrs))

;; look for a label element in a child elements
(define ($get-child-id$ nd)
  (let* ((label (select-elements (children nd) "LABEL")))
    (if (node-list-empty? label)
        #f
        ($fix-ids$ (attribute-string "id" (node-list-first label))))))

(element HEADING (make-line-element gind: "Title" ))

(element HEADER (empty-sosofo))
(element LHEAD (empty-sosofo))
(element RHEAD (empty-sosofo))

;; ============================== LISTS =================================

(element ITEM
  (let ((para-nl (select-elements (children (current-node)) "P"))
        (item-empty (if (equal? 0 (string-length (data (current-node))))
                        #t #f)))
    (make sequence
      (write-string-RE (start-tag "ListItem"))
      (if (node-list-empty? para-nl)
          (make-block-element gind: "Para")
          (if item-empty
              (process-children)
              (make sequence
                (write-string-RE (start-tag "Para"))
                (process-children))))
      (write-string-RE (end-tag "ListItem")))))

(element ENUM (make-block-element gind: "OrderedList" ))
(element ITEMIZE (make-block-element gind: "ItemizedList" ))

(element DESCRIP 
  (make sequence
    (write-string-RE (start-tag "VariableList"))
    (process-children)
    (write-string-RE (end-tag "VarListEntry"))
    (write-string (end-tag "VariableList"))))

(element TAG 
  (let ((END-ENTRY (cond ((> (child-number) 1)
                          (end-tag "VarListEntry"))
                          (else ""))))
  (make sequence
    (write-string END-ENTRY)
    (RE-write-string (start-tag "VarListEntry"))
    (make-line-element gind: "Term")
    (write-string (start-tag "ListItem")))))

;; =========================== FONT CHANGES =============================

(element EM
  (if (equal? (gi (parent)) "TT")
      (process-children)
      (make-inline-element gind: "Emphasis")))

(element TT
  (make-inline-element gind: %transform-element-TT%
                       attributes: `(("remap" "tt"))))

(element BF
  (if (equal? (gi (parent)) "TT")
      (process-children)
      (make-inline-element gind: %transform-element-BF%
                           attributes: `(("remap" "bf")))))

(element IT
  (if (equal? (gi (parent)) "TT")
      (process-children)
      (make-inline-element gind: "Emphasis"
                           attributes: `(("remap" "it")))))

(element SL
  (make-inline-element gind: %transform-element-SL%
                       attributes: `(("remap" "sl"))))

(element CODE (make-block-element gind: "ProgramListing"))

(element TSCREEN (make-block-element gind: "Screen"))
(element VERB (process-children))

;============================  Linking ==================================

;; ID and IDREF cannot begin with a number and cannot have embedded spaces
;; or under bars.
(define ($fix-ids$ string)
  (let* ((nw-str (string-replace string " " "-"))
         (ub-str (string-replace nw-str "_" "-")))
    (repl-substring-list ub-str %ids-repl-list% 0)))


(element REF
  (make-empty-inline-element 
        gind: "XRef"
        attributes: `(("LinkEnd" ,($fix-ids$ (attribute-string "id"))))))

(element HTMLURL
  (if (equal? (gi (parent (current-node))) "NAME")
    (empty-sosofo)
    (make element gi: "ULink"
          attributes: `(("URL" ,(attribute-string "URL")))
          (if (attribute-string "NAME")
              (literal (attribute-string "NAME"))
              (literal (attribute-string "URL")) ))))
 
(element URL
    (make element gi: "ULink"
          attributes: `(("URL" ,(attribute-string "URL")))
          (if (attribute-string "NAME")
              (literal (attribute-string "NAME"))
              (literal (attribute-string "URL")) )))
              ; FIXME: Name attribute
 
(element LABEL
  (if (equal? (gi (parent (current-node))) "P")
      (make-empty-inline-element
        gind: "Anchor"
        attributes: `(("id" ,($fix-ids$ (attribute-string "id")))))
      (empty-sosofo)))

;; for when htmlurl is a child of name
(mode name-htmlurl
  (element HTMLURL
    (make-block-element
      gind: "ULink"
      attributes: `(("URL" ,(attribute-string "URL")))
      sosofo: (if (attribute-string "NAME")
                  (literal (attribute-string "NAME"))
                  (literal (attribute-string "URL")) ))))

;; ======================== FIGURES and TABLES ==========================

(define (make-graphic-el fileref)
  (make-line-element gind: "Graphic" attributes: `(("FileRef" ,fileref))))

(element FIGURE
  (let* ((caption-nl (select-elements (descendants (current-node)) "CAPTION"))
         (label-id ($get-child-id$ caption-nl))
         (eps (select-elements (children (current-node)) "EPS"))
         (file (attribute-string "file" (node-list-first eps))))
     (make-block-element
       gind: "Figure"
       attributes: (if label-id `(("id" ,($fix-ids$ label-id))) `())
       sosofo: (if (not (node-list-empty? caption-nl))
                   (make sequence
                     (with-mode caption-to-title
                       (process-node-list caption-nl))
                     (make-graphic-el (if file file "dummy")))
                   (make-graphic-el (if file file "dummy"))))))

(element EPS (empty-sosofo))
(element PH (empty-sosofo))

(element CAPTION (empty-sosofo))

(mode caption-to-title
  (element CAPTION
      (make-line-element gind: "Title")))

;; currently the frame attribute must be set manually
(element TABLE
  (let* ((caption-nl (select-elements (descendants (current-node)) "CAPTION"))
         (label-id ($get-child-id$ caption-nl)))
    (if (node-list-empty? caption-nl)
        (make-block-element gind: "InformalTable")
        (make-block-element gind: "Table" 
                            attributes: (if label-id
                                            `(("id" ,($fix-ids$ label-id)))
                                            `())
                            sosofo: (make sequence
                                      (with-mode caption-to-title
                                        (process-node-list caption-nl))
                                      (process-children))))))

(define ($count-cols$ ca-str)
   (let loop ((cnt 0) (str ca-str))
     (if (equal? (string-length str) 0)
         cnt
         (if (equal? (substring str 0 1) "|")
             (loop cnt (substring str 1 (string-length str)))
             (loop (+ 1 cnt) (substring str 1 (string-length str)))))))

(define ($make-colspecs$ ca-str)
  (if (equal? (string-length ca-str) 0)
      (empty-sosofo)
      (if (equal? (substring ca-str 0 1) "|")
          ($make-colspecs$ (substring ca-str 1 (string-length ca-str)))
          (let loop ((str ca-str))
            (if (equal? (string-length str) 0)
                (empty-sosofo)
                (let* ((col-sep (if (> (string-length str) 1)
                                    (if (equal? (substring str 1 2) "|")
                                        #t
                                        #f)
                                    #f))
                       (pos (if col-sep 2 1)))
                  (make sequence
                    ($build-colspec$ (substring str 0 1) col-sep)
                    (loop (substring str pos (string-length str))))))))))

(define ($build-colspec$ cell-align col-sep)
  (let* ((cellalign (case cell-align
                          (("l") "Left")
                          (("c") "Center")
                          (("r") "Right")
                          (else  "Left")))
         (attrs (cons (list "Align" cellalign) (cons
           (if col-sep
               (list "Colsep" "1")
               (list "Colsep" "0"))
           `()))))
    (make-empty-line-element
      gind: "ColSpec"
      attributes: attrs
      sosofo: (empty-sosofo))))

(element TABULAR
  (let* ((col-attr (attribute-string "CA"))
         (colcnt ($count-cols$ col-attr)))
    (make-block-element
      gind: "TGroup"
      attributes: `(("Cols" ,(number->string colcnt)))
      sosofo: (make sequence
                ($make-colspecs$ col-attr)
                (RE-write-string-RE (start-tag "TBody"))
                (row-check-border (node-list-first (children (current-node))))
                (write-string    (start-tag "Entry"))
                (process-children)
                (write-string-RE (end-tag "Entry"))
                (write-string-RE (end-tag "Row"))
                (write-string-RE (end-tag "TBody"))))))

(element COLSEP
  (make sequence
    (write-string (end-tag "Entry"))
    (RE-write-string (start-tag "Entry"))))

;; find the next "rowsep" then check if a "hline" immediatly follows
(define (row-check-border nd)
  (let* ((follow-nl (follow nd))
         (af-nl (node-list-first-element-after-match follow-nl "ROWSEP"))
         (hline-next (if (equal? (gi af-nl) "HLINE") #t #f)))
      (if hline-next
          (make sequence
            (write-string (string-append "<" "Row"))
            (if attributes
                (make sequence
                  ($out-attributes$ `(("RowSep" "1")))
                  (write-string %RE%))
                (write-string-RE ">")))
          (write-string-RE (start-tag "Row")))))

(element ROWSEP
    (make sequence
      (write-string-RE (end-tag "Entry"))
      (write-string-RE (end-tag "Row"))
      (row-check-border (current-node))
      (write-string-RE (start-tag "Entry"))))

; for now
(element HLINE (empty-sosofo))

; don't do any math
(element DM (empty-sosofo))

(element FOOTNOTE
  (make-block-element
    sosofo: (make-block-element gind: "Para")))

(element NEWLINE
  (write-string %RE%))

</style-specification-body>
</style-specification>
</style-sheet>
