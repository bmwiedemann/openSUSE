#
# spec file for package autoconf-el
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           autoconf-el
BuildRequires:  emacs-nox
BuildRequires:  m4 >= 1.4.6
BuildRequires:  xz
Version:        2.69
Release:        0
Summary:        Emacs mode for editing GNU Autoconf scripts
License:        GPL-3.0-or-later
Url:            http://www.gnu.org/software/autoconf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         http://ftp.gnu.org/gnu/autoconf/autoconf-%{version}.tar.gz
BuildArch:      noarch
Enhances:       emacs
%define site_lisp %{_prefix}/share/emacs/site-lisp

%description
Emacs mode for editing GNU Autoconf scripts

%prep
%setup -q -n autoconf-%{version}

%build
./configure --prefix=%{_prefix} --infodir=%{_infodir} --mandir=%{_mandir}
make -C lib/emacs %{?_smp_mflags}

%install
make -C lib/emacs install DESTDIR=$RPM_BUILD_ROOT
sed 's/^;//' > $RPM_BUILD_ROOT%{site_lisp}/suse-start-%{name}.el <<\EOF
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
%defattr(-,root,root)
%{site_lisp}/*.el
%{site_lisp}/*.elc

%changelog
