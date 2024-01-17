#
# spec file for package futuresql
#
# Copyright (c) 2023 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%endif
%if "%{flavor}" == "qt5"
  %define qt5 1
  %define pkgname_suffix -qt5
  %define library_suffix 5
%endif
%if "%{flavor}" == "qt6"
  %define qt6 1
  %define pkgname_suffix -qt6
  %define library_suffix 6
%endif
%define rname futuresql
%bcond_without released
Name:           futuresql%{?pkgname_suffix}
Version:        0.1.1
Release:        0
Summary:        Library for accessing SQLite
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/futuresql/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/futuresql/%{rname}-%{version}.tar.xz.sig
Source2:        futuresql.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.93
%if 0%{?qt5}
# C++-20 required for tests, Qt6 already requires a recent compiler
%if 0%{?suse_version} == 1500
BuildRequires:  gcc10-c++
BuildRequires:  gcc10-PIE
%endif
BuildRequires:  cmake(QCoro5Core)
BuildRequires:  cmake(Qt5Core) >= 5.15.2
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
# For running tests
BuildRequires:  libQt5Sql5-sqlite
%endif
%if 0%{?qt6}
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
# For running tests
BuildRequires:  qt6-sql-sqlite
%endif

%description
A library for accessing SQLite (and other databases) in Qt projects without
blocking.

It also features a migration system and automatic result deserialization.

%package -n libfuturesql%{library_suffix}-0
Summary:        Library for accessing SQLite
%if 0%{?qt5}
Recommends:     libQt5Sql5-sqlite
%endif
%if 0%{?qt6}
Recommends:     qt6-sql-sqlite
%endif

%description -n libfuturesql%{library_suffix}-0
A library for accessing SQLite (and other databases) in Qt projects without
blocking.

It also features a migration system and automatic result deserialization.

%package devel
Summary:        Development files for futuresql
Requires:       libfuturesql%{library_suffix}-0 = %{version}

%description devel
This package contains development files needed to use futuresql.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%if 0%{?qt5}
%if 0%{?suse_version} == 1500
export CXX=g++-10 CC=gcc-10
%endif
%cmake -DQT_MAJOR_VERSION:STRING=5
%cmake_build
%endif
%if 0%{?qt6}
%cmake_qt6 -DQT_MAJOR_VERSION:STRING=6 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
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
%ctest

%ldconfig_scriptlets -n libfuturesql%{library_suffix}-0

%files -n libfuturesql%{library_suffix}-0
%license LICENSES/*
%{_libdir}/libfuturesql%{library_suffix}.so.0

%files devel
%doc README.md
%{_includedir}/FutureSQL%{library_suffix}/
%{_libdir}/cmake/FutureSQL%{library_suffix}/
%{_libdir}/libfuturesql%{library_suffix}.so

%changelog
