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
Version:        10.8+80+g6947dc4
Release:        0
Summary:        A Portable Emacs Library
License:        GPL-2.0-or-later
Group:          Productivity/Editors/Emacs
URL:            https://github.com/wanderlust/apel
Source:         apel-%{version}.tar.gz
Source1:        suse-start-apel.el
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
cp -p %{SOURCE1} .

%build
make "CFLAGS=%{optflags}" LDFLAGS=-s EMACS=emacs PREFIX=%{_prefix} %{?_smp_mflags}

%install
make install EMACS=emacs PREFIX=%{buildroot}%{_prefix}
install -m 644 suse-start-apel.el %{buildroot}%{_datadir}/emacs/site-lisp/
# make install.man

%files
%defattr(-,root,root)
%doc README.en README.ja
%{_datadir}/emacs/site-lisp/suse-start-apel.el
%{_datadir}/emacs/site-lisp/emu
%{_datadir}/emacs/site-lisp/apel

%changelog
