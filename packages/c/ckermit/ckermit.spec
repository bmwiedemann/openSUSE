#
# spec file for package ckermit
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        11.0.514
Release:        0
Summary:        A Combined Serial and Network Communication Software Package
License:        BSD-3-Clause
URL:            https://www.openkermit.org/
Source0:        https://github.com/OpenKermit/ckermit/archive/refs/tags/v%{version}.tar.gz
Source1:        ckermit-tmp.conf
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
Provides:       kermit

%description
C-Kermit is a combined serial and network communication software
package offering a consistent, medium-independent, and cross-platform
approach to connection establishment, terminal sessions, file transfer,
character-set translation, and automation of communication tasks.

%package doc
Summary:        Documentation for CKermit
%if !0%{?sles_version}
BuildArch:      noarch
%endif

%description doc
This package contains the documentation and manual pages for ckermit.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -DLOCK_DIR=\\\\\\\\\\\\\\\"/run/lock/uucp\\\\\\\\\\\\\\\""
%make_build KFLAGS="$CFLAGS" linux

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 wermit %{buildroot}%{_bindir}/kermit
install -m 644 ckuker.nr %{buildroot}%{_mandir}/man1/kermit.1
cd %{buildroot}%{_mandir}/man1
ln -s kermit.1 ckermit.1
install -pD -m644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/ckermit.conf

%files
%license COPYING.TXT
%{_bindir}/kermit
%{_mandir}/man1/ckermit.1%{?ext_man}
%{_mandir}/man1/kermit.1%{?ext_man}
%{_tmpfilesdir}/ckermit.conf

%files doc
%doc android.txt doc/

%changelog
