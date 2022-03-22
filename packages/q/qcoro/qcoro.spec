#
# spec file for package qcoro
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


%define sonum 0
#
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%else
%define _pkg_name_suffix -%{?flavor}
%endif
%if "%{flavor}" == "qt5"
%define qt5 1
%define qt_min_version 5.12.0
%define _qt_suffix 5
%endif
%if "%{flavor}" == "qt6"
%define qt6 1
%define qt_min_version 6.1.2
%define _qt_suffix 6
%endif
#
Name:           qcoro%{?_pkg_name_suffix}
Version:        0.4.0
Release:        0
Summary:        Coroutines for Qt
License:        MIT
URL:            https://github.com/danvratil/qcoro
Source:         https://github.com/danvratil/qcoro/archive/refs/tags/v%{version}.tar.gz#/qcoro-%{version}.tar.gz
BuildRequires:  cmake >= 3.19.0
BuildRequires:  dbus-1
BuildRequires:  cmake(Qt%{_qt_suffix}Concurrent) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{_qt_suffix}Core) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{_qt_suffix}DBus) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{_qt_suffix}Network) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{_qt_suffix}Test) >= %{qt_min_version}
BuildRequires:  cmake(Qt%{_qt_suffix}Widgets) >= %{qt_min_version}
# C++-20 support is needed. Qt6 already requires gcc10
%if 0%{?qt5} && 0%{?suse_version} == 1500
BuildRequires:  gcc10-c++
%endif

%description
The QCoro library provides set of tools to make use of the C++20
coroutines in connection with certain asynchronous Qt actions.

%package -n libQCoro%{_qt_suffix}Core%{sonum}
Summary:        Core library of qcoro, a library providing coroutines for Qt

%description -n libQCoro%{_qt_suffix}Core%{sonum}
The QCoro library provides set of tools to make use of the C++20
coroutines in connection with certain asynchronous Qt actions. This package
provides the core library.

%package -n libQCoro%{_qt_suffix}DBus%{sonum}
Summary:        DBus support library for qcoro, a library providing coroutines for Qt

%description -n libQCoro%{_qt_suffix}DBus%{sonum}
The QCoro library provides set of tools to make use of the C++20
coroutines in connection with certain asynchronous Qt actions. This package
provides a library for D-Bus support.

%package -n libQCoro%{_qt_suffix}Network%{sonum}
Summary:        Network support library for qcoro, a library providing coroutines for Qt

%description -n libQCoro%{_qt_suffix}Network%{sonum}
The QCoro library provides set of tools to make use of the C++20
coroutines in connection with certain asynchronous Qt actions. This package
provides a library for network operations support.

%package -n %{name}-devel
Summary:        Development files for qcoro
Requires:       libQCoro%{_qt_suffix}Core%{sonum} = %{version}
Requires:       libQCoro%{_qt_suffix}DBus%{sonum} = %{version}
Requires:       libQCoro%{_qt_suffix}Network%{sonum} = %{version}

%description -n %{name}-devel
The QCoro library provides set of tools to make use of the C++20 coroutines
in connection with certain asynchronous Qt actions.
This package provides development headers to use QCoro in Qt based
applications.

%prep
%autosetup -p1 -n qcoro-%{version}

# Causes build failure in FindEGL.cmake on ARM (https://github.com/danvratil/qcoro/issues/49)
sed -i '/-Wall -Wextra -Werror -pedantic/d' CMakeLists.txt

%build
%if 0%{?qt5}
%cmake -DBUILD_SHARED_LIBS:BOOL=ON \
  -DUSE_QT_VERSION:STRING=%{_qt_suffix} \
%if 0%{?qt5} && 0%{?suse_version} == 1500
  -DCMAKE_CXX_COMPILER:STRING=g++-10
%endif

%cmake_build
%endif

%if 0%{?qt6}
%cmake_qt6 \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DUSE_QT_VERSION:STRING=%{_qt_suffix}

%qt6_build
%endif

%install
%if 0%{?qt5}
%cmake_install
%endif
%if 0%{?qt6}
%qt6_install
%endif

%check
# Exclude tests that timeout randomly (https://github.com/danvratil/qcoro/issues/41)
%{ctest --exclude-regex 'test-(qcoroabstractsocket|qcorolocalsocket)'}

%post -n libQCoro%{_qt_suffix}Core%{sonum}  -p /sbin/ldconfig
%post -n libQCoro%{_qt_suffix}DBus%{sonum}  -p /sbin/ldconfig
%post -n libQCoro%{_qt_suffix}Network%{sonum}  -p /sbin/ldconfig
%postun -n libQCoro%{_qt_suffix}Core%{sonum}  -p /sbin/ldconfig
%postun -n libQCoro%{_qt_suffix}DBus%{sonum}  -p /sbin/ldconfig
%postun -n libQCoro%{_qt_suffix}Network%{sonum}  -p /sbin/ldconfig

%files -n libQCoro%{_qt_suffix}Core%{sonum}
%license LICENSES/*
%doc README.md
%{_libdir}/libQCoro%{_qt_suffix}Core.so.%{sonum}
%{_libdir}/libQCoro%{_qt_suffix}Core.so.%{sonum}.*

%files -n libQCoro%{_qt_suffix}DBus%{sonum}
%{_libdir}/libQCoro%{_qt_suffix}DBus.so.%{sonum}
%{_libdir}/libQCoro%{_qt_suffix}DBus.so.%{sonum}.*

%files -n libQCoro%{_qt_suffix}Network%{sonum}
%{_libdir}/libQCoro%{_qt_suffix}Network.so.%{sonum}
%{_libdir}/libQCoro%{_qt_suffix}Network.so.%{sonum}.*

%files devel
%{_libdir}/libQCoro%{_qt_suffix}Core.so
%{_libdir}/libQCoro%{_qt_suffix}Network.so
%{_libdir}/libQCoro%{_qt_suffix}DBus.so
%{_includedir}/qcoro%{_qt_suffix}/
%{_libdir}/cmake/QCoro%{_qt_suffix}/
%{_libdir}/cmake/QCoro%{_qt_suffix}Coro/
%{_libdir}/cmake/QCoro%{_qt_suffix}Core/
%{_libdir}/cmake/QCoro%{_qt_suffix}DBus/
%{_libdir}/cmake/QCoro%{_qt_suffix}Network/

%changelog
