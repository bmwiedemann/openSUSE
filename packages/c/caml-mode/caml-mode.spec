#
# spec file for package caml-mode
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           caml-mode
Version:        4.08.0+git20190413.38ebde1
Release:        0
Summary:        Emacs mode for OCaml
License:        GPL-2.0-or-later
Group:          Development/Languages/OCaml
Url:            http://www.ocaml.org
Source:         caml-mode-%{version}.tar.xz
Patch0:         ocaml-3.00-camldebug_el.patch
Patch1:         ocaml-3.04-ocamltags--no-site-start.patch
Patch2:         ocaml-3.09-emacs_localcompile.patch
BuildRequires:  emacs-nox
Requires:       emacs
Requires:       ocaml
# caml-mode was previously part of the ocaml sources and named ocaml-emacs
Provides:       ocaml-emacs = 4.08.0
Obsoletes:      ocaml-emacs < 4.08.0
BuildArch:      noarch

%description
This package provides Emacs mode for OCaml.

%prep
%autosetup -p2

%build
# nothing to do

%install
EMACS_SITE_LISP=%{_datadir}/emacs/site-lisp
# INSTALL_DATA is not defined in the Makefile, https://github.com/ocaml/caml-mode/issues/8
make install DESTDIR=%{buildroot} EMACSDIR=%{buildroot}${EMACS_SITE_LISP} INSTALL_DATA="install -m 644 "
make install-ocamltags SCRIPTDIR=%{buildroot}${EMACS_SITE_LISP} INSTALL_DATA="install -m 644 "

# fix bnc#411232
echo '(load "ocaml.el" nil t t)' >%{buildroot}${EMACS_SITE_LISP}/suse-start-ocaml.el
tee %{buildroot}${EMACS_SITE_LISP}/%{name}.el <<EOF
(autoload 'caml-mode "caml" "Caml editing mode" t)
(add-hook 'caml-mode-hook 'font-lock-mode)
(add-to-list 'auto-mode-alist '("\\\\.mli?$" . caml-mode))
EOF
#' # restore highlighting context in vim


%files
%doc README.md
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/site-lisp/*

%changelog

