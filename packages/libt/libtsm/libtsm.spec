#
# spec file for package libtsm
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


%global sover   4
%global lname   libtsm%{sover}
Name:           libtsm
Version:        4.4.1
Release:        0
Summary:        DEC-VT terminal emulator state machine
License:        LGPL-2.1-or-later AND MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/kmscon/libtsm
Source:         https://github.com/kmscon/libtsm/archive/refs/tags/v%version.tar.gz
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0

%description
TSM is a state machine for DEC VT100-VT520 compatible terminal
emulators. It can be used to implement terminal emulators, or other
applications that need to interpret terminal escape sequences.

%package -n %{lname}
Summary:        DEC-VT terminal emulator state machine
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{lname}
TSM is a state machine for DEC VT100-VT520 compatible terminal
emulators. It can be used to implement terminal emulators, or other
applications that need to interpret terminal escape sequences. The
library does no rendering or window management of its own, and does
not depend on a graphics stack, unlike the similar GNOME libvte.

%package devel
Summary:        Development files for the DEC-VT terminal state machine library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}-%{release}

%description devel
TSM is a state machine for DEC VT100-VT520 compatible terminal
emulators. It can be used to implement terminal emulators, or other
applications that need to interpret terminal escape sequences. The
library does no rendering or window management of its own, and does
not depend on a graphics stack, unlike the similar GNOME libvte.

This package contains the development headers for the library found
in %{lname}.

%prep
%autosetup -p1

%build
%meson -Dtests=false
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}
%license COPYING LICENSE_htable
%{_libdir}/libtsm.so.%{sover}*

%files devel
%doc README.md
%{_includedir}/libtsm.h
%{_libdir}/libtsm.so
%{_libdir}/pkgconfig/*.pc

%changelog
