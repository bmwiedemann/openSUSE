#
# spec file for package ckermit
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


Name:           ckermit
Version:        9.0.302
Release:        0
Summary:        A Combined Serial and Network Communication Software Package
License:        BSD-3-Clause
Group:          Hardware/Modem
Url:            http://www.kermitproject.org/
Source0:        ftp://ftp.kermitproject.org/kermit/archives/cku302.tar.gz
Patch0:         decl-definition-conflict.patch
# PATCH-FIX-UPSTREAM time_and_file_failure.patch
Patch1:         time_and_file_failure.patch
BuildRequires:  ncurses-devel
Provides:       kermit
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?fedora_version} || 0%{?rhel_version}
BuildRequires:  zsh
%else
BuildRequires:  termcap
%endif
%if 0%{?suse_version} >= 1130 || 0%{?fedora_version} || 0%{?mandriva_version}
BuildRequires:  lockdev-devel
%endif

%description
C-Kermit is a combined serial and network communication software
package offering a consistent, medium-independent, and cross-platform
approach to connection establishment, terminal sessions, file transfer,
character-set translation, and automation of communication tasks.

%package doc
Summary:        Documentation for CKermit
Group:          Documentation/Howto
%if !0%{?sles_version}
BuildArch:      noarch
%endif

%description doc
This package contains the documentation and manual pages for ckermit

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"
make %{?_smp_mflags} linux

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 wermit %{buildroot}%{_bindir}/kermit
install -m 644 ckuker.nr %{buildroot}%{_mandir}/man1/kermit.1
cd %{buildroot}%{_mandir}/man1
ln -s kermit.1 ckermit.1

%files
%defattr(-,root,root)
%doc COPYING.TXT
%{_mandir}/man1/*
%{_bindir}/*

%files doc
%defattr(-,root,root)
%doc *.txt

%changelog
