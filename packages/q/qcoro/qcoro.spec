#
# spec file for package qcoro
#
# Copyright (c) 2021 SUSE LLC
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
Name:           qcoro
Version:        0.3.0
Release:        0
Summary:        Coroutines for Qt
License:        MIT
URL:            https://github.com/danvratil/qcoro
Source:         https://github.com/danvratil/qcoro/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.19.0
%if 0%{?suse_version} > 1500
BuildRequires:  dbus-1
%endif
BuildRequires:  cmake(Qt5Concurrent) >= 5.12.0
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5DBus) >= 5.12.0
BuildRequires:  cmake(Qt5Network) >= 5.12.0
BuildRequires:  cmake(Qt5Test) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0

%description
The QCoro library provides set of tools to make use of the C++20
coroutines in connection with certain asynchronous Qt actions.

%package -n libQCoroCore%{sonum}
Summary:        Core library of qcoro, a library providing coroutines for Qt

%description -n libQCoroCore%{sonum}
The QCoro library provides set of tools to make use of the C++20
coroutines in connection with certain asynchronous Qt actions. This package
provides the core library.

%package -n libQCoroDBus%{sonum}
Summary:        DBus support library for qcoro, a library providing coroutines for Qt

%description -n libQCoroDBus%{sonum}
The QCoro library provides set of tools to make use of the C++20
coroutines in connection with certain asynchronous Qt actions. This package
provides a library for D-Bus support.

%package -n libQCoroNetwork%{sonum}
Summary:        Network support library for qcoro, a library providing coroutines for Qt

%description -n libQCoroNetwork%{sonum}
The QCoro library provides set of tools to make use of the C++20
coroutines in connection with certain asynchronous Qt actions. This package
provides a library for network operations support.

%package devel
Summary:        Development files for qcoro
Requires:       libQCoroCore%{sonum} = %{version}
Requires:       libQCoroDBus%{sonum} = %{version}
Requires:       libQCoroNetwork%{sonum} = %{version}

%description devel
The QCoro library provides set of tools to make use of the C++20 coroutines
in connection with certain asynchronous Qt actions.
This package provides development headers to use QCoro in Qt based
applications.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%post -n libQCoroCore%{sonum}  -p /sbin/ldconfig
%postun -n libQCoroCore%{sonum}  -p /sbin/ldconfig
%post -n libQCoroDBus%{sonum}  -p /sbin/ldconfig
%postun -n libQCoroDBus%{sonum}  -p /sbin/ldconfig
%post -n libQCoroNetwork%{sonum}  -p /sbin/ldconfig
%postun -n libQCoroNetwork%{sonum}  -p /sbin/ldconfig

%files -n libQCoroCore%{sonum}
%license LICENSES/*
%doc README.md
%{_libdir}/libQCoroCore.so.%{sonum}
%{_libdir}/libQCoroCore.so.%{sonum}.*

%files -n libQCoroNetwork%{sonum}
%{_libdir}/libQCoroNetwork.so.%{sonum}
%{_libdir}/libQCoroNetwork.so.%{sonum}.*

%files -n libQCoroDBus%{sonum}
%{_libdir}/libQCoroDBus.so.%{sonum}
%{_libdir}/libQCoroDBus.so.%{sonum}.*

%files devel
%{_libdir}/libQCoroCore.so
%{_libdir}/libQCoroNetwork.so
%{_libdir}/libQCoroDBus.so
%{_includedir}/qcoro
%{_includedir}/QCoro
%{_libdir}/cmake/QCoro

%changelog
