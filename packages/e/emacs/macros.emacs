# -*- rpm-spec -*-
%_emacs_sitelispdir %{_datadir}/emacs/site-lisp
%_emacs_etcdir %{_datadir}/emacs/etc
%_emacs_sitestartdir %{_emacs_sitelispdir}/site-start.d
%_emacs_archsitelispdir %{_libdir}/emacs/site-lisp

%emacs_addto_load_path() \
    cat <<EOF > %{buildroot}/%{_emacs_sitestartdir}/%1.el \
    ;; -*- lexical-binding: t -*- \
    ;; Add package %1 to load-path \
    (add-to-list 'load-path %2) \
    EOF
