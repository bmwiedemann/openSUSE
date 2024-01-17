;; Used by ispell-emacs-menu.el
;; Do *not* byte-compile this file because its loaded by both emacs and xemacs

(append-ispell-dict-alist	"magyar.hash"
   '("magyar-latin2"
      "[A-Za-z\301\311\315\323\326\325\332\334\333\341\351\355\363\366\365\372\374\373]"
     "[^A-Za-z\301\311\315\323\326\325\332\334\333\341\351\355\363\366\365\372\374\373]"
     "[']" nil ("-d" "magyar") nil iso-8859-2))

