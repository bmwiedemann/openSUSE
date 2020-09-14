#
# spec file for package libqt5-qtwebsockets
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
%define libname libQt5WebSockets5
%define base_name libqt5
%define real_version 5.15.1
%define so_version 5.15.1
%define tar_version qtwebsockets-everywhere-src-5.15.1
Name:           libqt5-qtwebsockets
Version:        5.15.1
Release:        0
Summary:        Qt 5 WebSockets Library
License:        LGPL-3.0-only OR  (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  libQt5Core-private-headers-devel >= %{version}
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Core) >= %{version}
BuildRequires:  pkgconfig(Qt5Network) >= %{version}
BuildRequires:  pkgconfig(Qt5Qml) >= %{version}
BuildRequires:  pkgconfig(Qt5Quick) >= %{version}
BuildRequires:  pkgconfig(Qt5Sql) >= %{version}
BuildRequires:  pkgconfig(openssl)
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif

%description
The Qt WebSockets module provides C++ and QML interfaces that enable
Qt applications to act as a server that can process WebSocket
requests, or a client that can consume data received from the server,
or both.

%prep
%setup -q -n %{tar_version}

%package -n %{libname}
Summary:        Qt 5 WebSockets Library
Group:          Development/Libraries/X11
%requires_ge    libQt5Network5

%description -n %{libname}
The Qt WebSockets module provides C++ and QML interfaces that enable
Qt applications to act as a server that can process WebSocket
requests, or a client that can consume data received from the server,
or both.

%package -n %{libname}-imports
Summary:        QML imports for the Qt 5 WebSockets library
Group:          Development/Libraries/X11
%requires_ge    libQtQuick5
Supplements:    (%{libname} and libQtQuick5)
# imports splited with 5.4.1
Conflicts:      %{libname} < 5.4.1

%description -n %{libname}-imports
The Qt WebSockets module provides C++ and QML interfaces that enable
Qt applications to act as a server that can process WebSocket
requests, or a client that can consume data received from the server,
or both.

%package devel
Summary:        Development files for the Qt5 WebSockets library
Group:          Development/Libraries/X11
Requires:       %{libname} = %{version}

%description devel
You need this package if you want to compile programs with QtWebSockets.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 WebSocket library
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libQt5Core-private-headers-devel >= %{version}
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qtwebsockets that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 websockets examples
Group:          Development/Libraries/X11
License:        BSD-3-Clause
Recommends:     %{name}-devel

%description examples
Examples for the libqt5-qtwebsockets module.

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
%license *GPL*
%{_libqt5_libdir}/libQt5WebSockets.so.*

%files -n %{libname}-imports
%defattr(-,root,root,755)
%license *GPL*
%{_libqt5_archdatadir}/qml/Qt/WebSockets/
%{_libqt5_archdatadir}/qml/QtWebSockets/

%files private-headers-devel
%defattr(-,root,root,755)
%license *GPL*
%{_libqt5_includedir}/Qt*/%{so_version}

%files devel
%defattr(-,root,root,755)
%license *GPL*
%{_libqt5_includedir}/QtWebSockets
%exclude %{_libqt5_includedir}/Qt*/%{so_version}
%{_libqt5_includedir}/QtWebSockets
%{_libqt5_libdir}/cmake/Qt5*
%{_libqt5_libdir}/libQt5WebSockets.prl
%{_libqt5_libdir}/libQt5WebSockets.so
%{_libqt5_libdir}/pkgconfig/Qt5WebSockets.pc
%{_libqt5_archdatadir}/mkspecs/modules/*.pri

%files examples
%defattr(-,root,root,755)
%license *GPL*
%{_libqt5_examplesdir}/

%changelog
