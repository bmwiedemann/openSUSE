(defvar xe-list-file-name "xe-list")

(defun xe-list-find-el (&optional buffer)
  (interactive)
  (let ((el-with-elc)
	(el-without-elc))
    (save-excursion
      (if buffer
	  (set-buffer buffer))
      (goto-char (point-min))
      (while (re-search-forward "^\\(.*\\.el\\)$" nil t)
	(let ((el (match-string 1)))
	  (save-excursion
	    (goto-char (point-min))
	    (if (re-search-forward (concat "^" (regexp-quote el) "c$") nil t)
		(setq el-with-elc (cons el el-with-elc))
	      (setq el-without-elc (cons el el-without-elc)))))))
   (list (nreverse el-with-elc) (nreverse el-without-elc))))

(defun xe-list-find-elc (&optional buffer)
  (interactive)
  (let ((elc-with-el)
	(elc-without-el))
    (save-excursion
      (if buffer
	  (set-buffer buffer))
      (goto-char (point-min))
      (while (re-search-forward "^\\(.*\\.elc\\)$" nil t)
	(let ((elc (match-string 1))
	      (el (replace-in-string (match-string 1) "\\.elc$" ".el")))
	  (save-excursion
	    (goto-char (point-min))
	    (if (re-search-forward (concat "^" (regexp-quote el) "$") nil t)
		(setq elc-with-el (cons elc elc-with-el))
	      (setq elc-without-el (cons elc elc-without-el)))))))
   (list (nreverse elc-with-el) (nreverse elc-without-el))))

(defun xe-list-write-list-to-file (list file)
  (interactive)
  (with-temp-buffer
    (mapcar (lambda (x) (insert x) (insert "\n"))
	    list)
    (write-file file)))

(defun xe-list-generate-list-files ()
  (interactive)
  (let ((el-lists)
	(elc-lists))
    (find-file xe-list-file-name)
    (setq el-lists (xe-list-find-el xe-list-file-name))
    (setq elc-lists (xe-list-find-elc xe-list-file-name))
    (xe-list-write-list-to-file (car el-lists)
				(concat xe-list-file-name "-el-with-elc"))
    (xe-list-write-list-to-file (car (cdr el-lists))
				(concat xe-list-file-name "-el-without-elc"))
    (xe-list-write-list-to-file (car elc-lists)
				(concat xe-list-file-name "-elc-with-el"))
    (xe-list-write-list-to-file (car (cdr elc-lists))
				(concat xe-list-file-name "-elc-without-el"))))

