;; Used by ispell-emacs-menu.el
;; Do *not* byte-compile this file because its loaded by both emacs and xemacs

(append-ispell-dict-alist	"swiss.hash"
   '("swiss-babel"
      "[a-zA-Z\"]"
     "[^a-zA-Z\"]" "[']" t ("-C" "-d" "swiss") "~tex" nil))

(append-ispell-dict-alist	"swiss.hash"
   '("swiss"
      "[[:alpha:]]"
     "[^[:alpha:]]"
     "[']" t ("-C" "-d" "swiss") "~latin1" iso-latin-1))

(append-ispell-dict-alist	"swiss.hash"
   '("swiss-utf8"
      "[[:alpha:]]"
     "[^[:alpha:]]"
     "[']" t ("-C" "-d" "swiss") "~utf8" utf-8))

