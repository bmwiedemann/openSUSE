;; Used by ispell-emacs-menu.el
;; Do *not* byte-compile this file because its loaded by both emacs and xemacs

(append-ispell-dict-alist	"slovak.hash"
   '("slovak-latin2"
      "[A-Za-z\245\251\253\256\265\271\273\276\300\301\304\305\310\311\315\317\322-\324\332\335\340\341\344\345\350\351\355\357\362-\364\372\375]"
     "[^A-Za-z\245\251\253\256\265\271\273\276\300\301\304\305\310\311\315\317\322-\324\332\335\340\341\344\345\350\351\355\357\362-\364\372\375]"
     "[']" nil ("-B" "-d" "slovak") nil iso-8859-2))

