;; Used by ispell-emacs-menu.el
;; Do *not* byte-compile this file because its loaded by both emacs and xemacs

(append-ispell-dict-alist	"austrian.hash"
   '("austrian-babel"
      "[a-zA-Z\"]"
     "[^a-zA-Z\"]" "[']" t ("-C" "-d" "austrian") "~tex" nil))

(append-ispell-dict-alist	"austrian.hash"
   '("austrian"
      "[[:alpha:]]"
     "[^[:alpha:]]"
     "[']" t ("-C" "-d" "austrian") "~latin1" iso-latin-1))

(append-ispell-dict-alist       "austrian.hash"
   '("austrian-utf8"
      "[[:alpha:]]"
     "[^[:alpha:]]"
     "[']" t ("-C" "-d" "austrian") "~utf8" utf-8))

