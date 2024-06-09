#
# spec file for package kf6-attica
#
# Copyright (c) 2024 SUSE LLC
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


%define qt6_version 6.6.0

%define rname attica
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-attica
Version:        6.3.0
Release:        0
Summary:        Open Collaboration Service client library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
Attica is a library to access Open Collaboration Service servers.

%package -n libKF6Attica6
Summary:        Open Collaboration Service client library
Requires:       kf6-attica >= %{version}
%requires_ge    libQt6Core6
%requires_ge    libQt6Network6

%description -n libKF6Attica6
Attica is a library to access Open Collaboration Service servers.

%package devel
Summary:        Open Collaboration Service client library - development files
Requires:       libKF6Attica6 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Network) >= %{qt6_version}

%description devel
Development files for attica, a library to access Open Collaboration Service servers.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%ldconfig_scriptlets -n libKF6Attica6

%files
%doc README.md
%{_kf6_debugdir}/attica.categories
%{_kf6_debugdir}/attica.renamecategories

%files -n libKF6Attica6
%license LICENSES/*
%{_kf6_libdir}/libKF6Attica.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Attica.*
%{_kf6_cmakedir}/KF6Attica/
%{_kf6_includedir}/Attica/
%{_kf6_libdir}/libKF6Attica.so
%{_kf6_pkgconfigdir}/KF6Attica.pc

%changelog
