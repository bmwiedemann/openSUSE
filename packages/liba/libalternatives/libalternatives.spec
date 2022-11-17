#
# spec file for package libalternatives
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


%define sover 1

Name:           libalternatives
Version:        1.2+3.b848aad
Release:        0
Summary:        Helper for executing preferred application based on user preferences
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://github.com/openSUSE/libalternatives
Source0:        libalternatives-v%{version}.tar.zst
BuildRequires:  cmake > 3.8
BuildRequires:  cunit-devel
BuildRequires:  gcc
BuildRequires:  zstd

%description
libalternatives is a helper that executes an application based on
preferences of a user, system admin or package maintainer, in this
order of preference. This is accomplished with only the help of
config files and without the need to maintain system symlinks states.

%package -n alts
Summary:        Helper for executing preferred application based on user preferences
License:        GPL-3.0-or-later

%description -n alts
This package contains a default helper and configuration application utility
for libalternatives. libalternatives is a helper that executes an application
based on preferences of a user, system admin or package maintainer, in this
order of preference. This is accomplished with only the help of config files
and without the need to maintain system symlinks states.

%package devel
Summary:        Development headers for libalternatives
License:        LGPL-3.0-or-later
Requires:       libalternatives%sover = %version

%description devel
This package contains development headers and library for libalternatives.

%package -n libalternatives%sover
Summary:        Runtime for libalternatives
License:        LGPL-3.0-or-later

%description -n libalternatives%sover
This package contains the core logic and the runtime library for
libalternatives. libalternatives is a helper that executes an application based
on preferences of a user, system admin or package maintainer, in this order of
preference. This is accomplished with only the help of config files and
without the need to maintain system symlinks states.

%package unit-test-helper
Summary:        Verification helper for libalternatives
License:        LGPL-3.0-or-later

%description unit-test-helper
This is a testing-only installation that may be used to verify that successful
integration with manual pages.

%prep
%autosetup -n libalternatives-v%version

%build
%cmake
%cmake_build

%install
%cmake_install

mkdir -p -m 0755 %buildroot/%_datadir/libalternatives

mkdir -p -m 0755 %buildroot/%_datadir/libalternatives/libalternatives-unit-test-helper
cat > %buildroot/%_datadir/libalternatives/libalternatives-unit-test-helper/10.conf <<EOF
binary=/usr/bin/true
man=true.1
EOF

cat > %buildroot/%_bindir/libalternatives-unit-test-helper.sh <<EOF
#!/bin/bash

(diff <(man libalternatives-unit-test-helper 2> /dev/null) <(man true) >> /dev/null && echo "Everything seems OK && exit")
echo "It seems `man` doesn't display the proper manpage for libalternatives system."
echo "You should see the manpage for true(1) when running"
echo "   man libalternatives-unit-test-helper"
exit 1
EOF
chmod 755 %buildroot/%_bindir/libalternatives-unit-test-helper.sh

%check
%ctest

%post -n libalternatives%sover -p /sbin/ldconfig
%postun -n libalternatives%sover -p /sbin/ldconfig

%files -n alts
%license COPYING
%doc README.md
%_bindir/alts
%_mandir/man1/alts.1.*

%files devel
%_includedir/libalternatives.h
%_libdir/libalternatives.so

%files -n libalternatives%sover
%license COPYING.LIB
%dir %_datadir/libalternatives
%_libdir/libalternatives.so.%sover

%files unit-test-helper
%dir %_datadir/libalternatives
%dir %_datadir/libalternatives/libalternatives-unit-test-helper
%_datadir/libalternatives/libalternatives-unit-test-helper/10.conf
%_bindir/libalternatives-unit-test-helper.sh

%changelog
