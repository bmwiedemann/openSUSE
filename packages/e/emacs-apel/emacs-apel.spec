#
# spec file for package emacs-apel
#
# Copyright (c) 2020 SUSE LLC
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


Name:           emacs-apel
Version:        10.8
Release:        0
Summary:        A Portable Emacs Library
License:        GPL-2.0-or-later
Group:          Productivity/Editors/Emacs
URL:            http://git.chise.org/elisp/apel
Source:         http://git.chise.org/elisp/dist/apel/apel-%{version}.tar.gz
Source1:        suse-start-apel.el
Patch0:         prevent-fontset-error.patch
# PATCH-FIX-UPSTREAM
Patch1:         apel-10.8-040_make-temp-file-for-Emacs-24.3.50.patch
Patch2:         apel-emacs-escape-fix.patch
#PATCH-FIX-UPSTREAM use new style backquotes
Patch3:         https://src.fedoraproject.org/rpms/emacs-apel/raw/master/f/emacs-apel-fix-old-backquote.patch
BuildRequires:  emacs-nox
Requires:       emacs
Requires:       emacs_program
Provides:       apel = %{version}
Obsoletes:      apel < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A Portable Emacs Library

%prep
%setup -q -n apel-%{version}
%patch0 -p1
%if 0%{?suse_version} > 1310
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
cp -p %{SOURCE1} .
iconv -fiso2022jp -tutf-8 README.ja > README.ja.new
mv README.ja.new README.ja

%build
make "CFLAGS=%{optflags}" LDFLAGS=-s EMACS=emacs PREFIX=%{_prefix} %{?_smp_mflags}

%install
make install EMACS=emacs PREFIX=%{buildroot}%{_prefix}
install -m 644 suse-start-apel.el %{buildroot}%{_datadir}/emacs/site-lisp/
# make install.man

%files
%defattr(-,root,root)
%doc README.en README.ja ChangeLog
%{_datadir}/emacs/site-lisp/suse-start-apel.el
%{_datadir}/emacs/site-lisp/emu
%{_datadir}/emacs/site-lisp/apel

%changelog
