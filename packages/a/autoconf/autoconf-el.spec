#
# spec file for package autoconf-el
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define site_lisp %{_datadir}/emacs/site-lisp
Name:           autoconf-el
Version:        2.71
Release:        0
Summary:        Emacs mode for editing GNU Autoconf scripts
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/autoconf
Source:         https://ftp.gnu.org/gnu/autoconf/autoconf-%{version}.tar.xz
BuildRequires:  emacs-nox
BuildRequires:  m4 >= 1.4.6
Enhances:       emacs
BuildArch:      noarch

%description
Emacs mode for editing GNU Autoconf scripts

%prep
%setup -q -n autoconf-%{version}

%build
%configure
%make_build

%install
mkdir -p %{buildroot}%{site_lisp}
install -c -m 644 lib/emacs/autoconf-mode.el  %{buildroot}%{site_lisp}/autoconf-mode.el
install -c -m 644 lib/emacs/autoconf-mode.elc %{buildroot}%{site_lisp}/autoconf-mode.elc
install -c -m 644 lib/emacs/autotest-mode.el  %{buildroot}%{site_lisp}/autotest-mode.el
install -c -m 644 lib/emacs/autotest-mode.elc %{buildroot}%{site_lisp}/autotest-mode.elc
sed 's/^;//' > %{buildroot}%{site_lisp}/suse-start-%{name}.el <<\EOF
;;; %{site_lisp}/suse-start-%{name}.el
;
(autoload 'autoconf-mode "autoconf-mode"
	  "Major mode for editing autoconf files." t)
(add-to-list 'auto-mode-alist
	     '("configure\\.\\(ac\\|in\\)\\'" . autoconf-mode))
;
(autoload 'autotest-mode "autotest-mode"
	  "Major mode for editing autotest files." t)
(add-to-list 'auto-mode-alist
	     '("\\.at\\'" . autotest-mode))
;
;;; %{site_lisp}/suse-start-%{name}.el ends here
EOF

%files
%license COPYING
%{site_lisp}/*.el
%{site_lisp}/*.elc

%changelog
