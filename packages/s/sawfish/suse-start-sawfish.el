;; this tells emacs to automatically activate the sawfish-mode whenever open
;; file with "sawfishrc" or "jl" (John Lisp) suffix

(setq auto-mode-alist (cons '("\\.sawfishrc$"  . sawfish-mode) auto-mode-alist)
      auto-mode-alist (cons '("\\.jl$"         . sawfish-mode) auto-mode-alist)
      auto-mode-alist (cons '("\\.sawfish/rc$" . sawfish-mode) auto-mode-alist))

;; (add-to-list 'auto-mode-alist '(".*sawfishrc\\'" . sawfish-mode ))
;; (add-to-list 'auto-mode-alist '(".*\\.jl\\'" . sawfish-mode )))
;; if you're using ECB, tells to use the compilation buffer to show long
;; sawfish messages
;; (add-to-list 'ecb-compilation-buffer-names '("*sawfish*"))
(add-hook 'sawfish-mode-hook
          (lambda ()
            (set (make-local-variable
                  'open-paren-in-column-0-is-defun-start) nil)
            ))
