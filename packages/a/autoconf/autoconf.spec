#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "testsuite"
%global psuffix -testsuite
%elif "%{flavor}" == "el"
%global psuffix -el
%else
%global psuffix %{nil}
%endif
Name:           autoconf%{?psuffix}
Version:        2.71
Release:        0
Summary:        A GNU Tool for Automatically Configuring Source Code
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/autoconf
Source0:        https://ftp.gnu.org/gnu/autoconf/autoconf-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/autoconf/autoconf-%{version}.tar.xz.sig
Source9:        autoconf.keyring
Patch0:         autoreconf-ltdl.diff
Patch1:         fix-testsuite-failures-with-bash-5.2.patch
BuildRequires:  help2man
BuildRequires:  m4 >= 1.4.6
BuildArch:      noarch
%if "%{name}" == "autoconf"
Requires:       info
Requires:       m4 >= 1.4.6
Requires:       perl-base >= 5.6
%endif
%if "%{name}" == "autoconf-testsuite"
BuildRequires:  gcc-c++
%endif
%if "%{name}" == "autoconf-el"
%global site_lisp %{_datadir}/emacs/site-lisp
BuildRequires:  emacs-nox
BuildRequires:  gcc-c++
Enhances:       emacs
%endif

%description
GNU Autoconf is a tool for configuring source code and makefiles. Using
autoconf, programmers can create portable and configurable packages,
because the person building the package is allowed to specify various
configuration options.

You should install autoconf if you are developing software and would
like to create shell scripts to configure your source code packages.

Note that the autoconf package is not required for the end user who may
be configuring software with an autoconf-generated script; autoconf is
only required for the generation of the scripts, not their use.

%prep
%setup -q -n autoconf-%{version}
%patch0
%patch1 -p1

%build
%configure
%make_build

%if "%{name}" == "autoconf-testsuite"
%check
trap 'test $? -ne 0 && cat tests/testsuite.log' EXIT
%make_build check

%install
%elif "%{name}" == "autoconf-el"

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
%else

%install
%make_install
%endif

%if "%{name}" == "autoconf"
%files
%doc AUTHORS NEWS README TODO
%license COPYING
%{_bindir}/*
%{_datadir}/autoconf
%{_infodir}/*.gz
%{_mandir}/man1/*.gz
%endif

%if "%{name}" == "autoconf-el"
%files
%license COPYING
%{site_lisp}/*.el
%{site_lisp}/*.elc
%endif

%changelog
