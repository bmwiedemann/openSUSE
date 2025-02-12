#
# spec file for package libtsm
#
# Copyright (c) 2025 SUSE LLC
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
Version:        4.0.2+git24
Release:        0
Summary:        DEC-VT terminal emulator state machine
License:        LGPL-2.1-or-later AND MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/Aetf/libtsm
%define rev 69922bde02c7af83b4d48a414cc6036af7388626
Source:         https://github.com/Aetf/libtsm/archive/%rev.tar.gz
BuildRequires:  cmake
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(xkbcommon)

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
%autosetup -p1 -n libtsm-%rev

%build
%cmake
%make_build

%install
%cmake_install

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}
%license COPYING LICENSE_htable
%{_libdir}/libtsm.so.%{sover}*

%files devel
%doc README
%{_includedir}/libtsm.h
%{_libdir}/libtsm.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/

%changelog
