#
# spec file for package libqt5-qtwebview
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
%define libname libQt5WebView5
%define base_name libqt5
%define real_version 5.15.1
%define so_version 5.15.1
%define tar_version qtwebview-everywhere-src-5.15.1
Name:           libqt5-qtwebview
Version:        5.15.1
Release:        0
Summary:        Qt 5 WebView Library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
BuildRequires:  libQt5Core-private-headers-devel >= %{version}
BuildRequires:  libqt5-qtwebengine-private-headers-devel >= %{version}
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

# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
Qt WebView provides a way to display web content in a QML application
without necessarily including a full web browser stack by using
native APIs where it makes sense.

%prep
%setup -q -n %{tar_version}

%package -n %{libname}
Summary:        Qt 5 WebView Library
Group:          Development/Libraries/X11
%requires_ge    libQt5Network5

%description -n %{libname}
Qt WebView provides a way to display web content in a QML application
without necessarily including a full web browser stack by using
native APIs where it makes sense.

%package -n %{libname}-imports
Summary:        Qt 5 WebView Library - QML imports
Group:          Development/Libraries/X11
%requires_ge    libQtQuick5
Supplements:    (%{libname} and libQtQuick5)
# imports splited with 5.4.1
Conflicts:      %{libname} < 5.4.1

%description -n %{libname}-imports
Qt WebView provides a way to display web content in a QML application
without necessarily including a full web browser stack by using
native APIs where it makes sense.

%package devel
Summary:        Development files for the Qt5's Webview library
Group:          Development/Libraries/X11
Requires:       %{libname} = %{version}

%description devel
You need this package if you want to compile programs with QtWebView.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for Qt5's Webview library
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libQt5Core-private-headers-devel >= %{version}
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qtwebview that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 webview examples
Group:          Development/Libraries/X11
License:        BSD-3-Clause
Recommends:     %{name}-devel

%description examples
Examples for libqt5-qtwebview module.

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
%{_libqt5_libdir}/libQt5WebView.so.*
%{_libqt5_archdatadir}/plugins/webview

%files -n %{libname}-imports
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_archdatadir}/qml/QtWebView/

%files private-headers-devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_includedir}/Qt*/%{so_version}

%files devel
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_includedir}/QtWebView
%exclude %{_libqt5_includedir}/Qt*/%{so_version}
%{_libqt5_libdir}/cmake/Qt5*
%{_libqt5_libdir}/libQt5WebView.prl
%{_libqt5_libdir}/libQt5WebView.so
%{_libqt5_libdir}/pkgconfig/Qt5WebView.pc
%{_libqt5_archdatadir}/mkspecs/modules/*.pri

%files examples
%defattr(-,root,root,755)
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
