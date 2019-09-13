;; Used by ispell-emacs-menu.el
;; Do *not* byte-compile this file because its loaded by both emacs and xemacs

(append-ispell-dict-alist	"german.hash"
   '("german-babel"
      "[a-zA-Z\"]"
     "[^a-zA-Z\"]" "[']" t ("-C" "-d" "german") "~tex" nil))

(append-ispell-dict-alist	"german.hash"
   '("german"
      "[[:alpha:]]"
     "[^[:alpha:]]"
     "[']" t ("-C" "-d" "german") "~latin1" iso-latin-1))

(append-ispell-dict-alist       "german.hash"
   '("german-utf8"
      "[[:alpha:]]"
     "[^[:alpha:]]"
     "[']" t ("-C" "-d" "german") "~utf8" utf-8))

