;; /usr/share/emacs/site-lisp/suse-start-po-mode.el

(autoload 'po-mode "po-mode"
  "Major mode for translators when they edit PO files.

Special commands:
\\{po-mode-map}
Turning on PO mode calls the value of the variable 'po-mode-hook',
if that value is non-nil.  Behaviour may be adjusted through some variables,
all reachable through 'M-x customize', in group 'Emacs.Editing.I18n.Po'." t)
(setq auto-mode-alist (cons '("\\.po[tx]?\\'" . po-mode)
                            auto-mode-alist))

;; To automatically use proper fonts under Emacs 20, also add:

(unless (fboundp 'po-find-file-coding-system)
  (autoload 'po-find-file-coding-system "po-compat" "\
Return a Mule (DECODING . ENCODING) pair, according to PO file charset.
Called through file-coding-system-alist, before the file is visited for real."))
(modify-coding-system-alist 'file "\\.po[tx]?\\'"
                            'po-find-file-coding-system)

;; /usr/share/emacs/site-lisp/suse-start-po-mode.el ends here
