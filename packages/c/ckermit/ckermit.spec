#
# spec file for package ckermit
#
# Copyright (c) 2024 SUSE LLC
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


Name:           ckermit
Version:        9.0.302
Release:        0
Summary:        A Combined Serial and Network Communication Software Package
License:        BSD-3-Clause
Group:          Hardware/Modem
URL:            https://www.kermitproject.org/
Source0:        ftp://ftp.kermitproject.org/kermit/archives/cku302.tar.gz
Patch0:         decl-definition-conflict.patch
# PATCH-FIX-UPSTREAM time_and_file_failure.patch
Patch1:         time_and_file_failure.patch
Patch2:         gcc14.patch
BuildRequires:  ncurses-devel
Provides:       kermit

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
This package contains the documentation and manual pages for ckermit.

%prep
%autosetup -p1 -c

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"
%make_build linux

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 wermit %{buildroot}%{_bindir}/kermit
install -m 644 ckuker.nr %{buildroot}%{_mandir}/man1/kermit.1
cd %{buildroot}%{_mandir}/man1
ln -s kermit.1 ckermit.1

%files
%license COPYING.TXT
%{_bindir}/kermit
%{_mandir}/man1/ckermit.1%{?ext_man}
%{_mandir}/man1/kermit.1%{?ext_man}

%files doc
%doc *.txt

%changelog
