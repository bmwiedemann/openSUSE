#
# spec file for package libqt5-qtgamepad
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


%define qt5_snapshot 0
%define libname libQt5Gamepad5
%define base_name libqt5
%define real_version 5.15.1
%define so_version 5.15.1
%define tar_version qtgamepad-everywhere-src-5.15.1
Name:           libqt5-qtgamepad
Version:        5.15.1
Release:        0
Summary:        Qt 5 Gamepad Library
License:        LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-or-later
Group:          Development/Libraries/X11
URL:            https://qt.io
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  libQt5Core-private-headers-devel >= %{version}
BuildRequires:  libQt5PlatformSupport-devel-static >= %{version}
BuildRequires:  libQt5PlatformSupport-private-headers-devel >= %{version}
BuildRequires:  libSDL2-devel
BuildRequires:  libqt5-qtbase-devel >= %{version}
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  xz

%description
Qt Gamepad is an add-on library that enables Qt applications to
support the use of gamepad hardware. The module provides both QML and
C++ interfaces.

%prep
%setup -q -n %{tar_version}

%package -n %{libname}
Summary:        Qt 5 Gamepad Library
Group:          System/Libraries
%requires_ge    libQt5Core5

%description -n %{libname}
Qt Gamepad is an add-on library that enables Qt applications to
support the use of gamepad hardware. The module provides both QML and
C++ interfaces.

%package devel
Summary:        Development files for the Qt5 gamepad library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
You need this package if you want to compile programs with QtGamepad.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 gamepad library
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libQt5Core-private-headers-devel >= %{version}
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qtgamepad that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 gamepad examples
Group:          Development/Libraries/X11
License:        BSD-3-Clause AND (LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-or-later)
Recommends:     %{name}-devel

%description examples
Examples for the libqt5-qtgamepad module.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install

# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%files -n %{libname}
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_libdir}/libQt5Gamepad.so.*
%{_libqt5_plugindir}/gamepads

%files private-headers-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_includedir}/QtGamepad/%{so_version}

%files devel
%defattr(-,root,root,755)
%license LICENSE.*
%exclude %{_libqt5_includedir}/QtGamepad/%{so_version}
%{_libqt5_includedir}/QtGamepad/
%{_libqt5_libdir}/cmake/Qt5Gamepad/
%{_libqt5_libdir}/libQt5Gamepad.prl
%{_libqt5_libdir}/libQt5Gamepad.so
%{_libqt5_libdir}/pkgconfig/Qt5Gamepad.pc
%{_libqt5_archdatadir}/mkspecs/modules/*.pri

%files examples
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
