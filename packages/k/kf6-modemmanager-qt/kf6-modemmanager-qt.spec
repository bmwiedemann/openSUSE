#
# spec file for package kf6-modemmanager-qt
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

%define rname modemmanager-qt
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-modemmanager-qt
Version:        6.3.0
Release:        0
Summary:        Qt wrapper for ModemManager DBus API
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(ModemManager) >= 1.0.0

%description
Qt wrapper for ModemManager DBus API.

%package devel
Summary:        Development package for the libmm-qt library
Requires:       libKF6ModemManagerQt6 = %{version}
Requires:       pkgconfig(ModemManager) >= 1.0.0

%description devel
Qt wrapper for ModemManager DBus API. Development files.

%package -n libKF6ModemManagerQt6
Summary:        Qt wrapper around the ModemManager libraries
Requires:       kf6-modemmanager-qt >= %{version}

%description -n libKF6ModemManagerQt6
Qt wrapper for ModemManager DBus API.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets -n libKF6ModemManagerQt6

%files
%{_kf6_debugdir}/modemmanagerqt.categories
%{_kf6_debugdir}/modemmanagerqt.renamecategories

%files -n libKF6ModemManagerQt6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6ModemManagerQt.so.*

%files devel
%doc %{_kf6_qchdir}/KF6ModemManagerQt.*
%{_kf6_cmakedir}/KF6ModemManagerQt/
%{_kf6_includedir}/ModemManagerQt/
%{_kf6_libdir}/libKF6ModemManagerQt.so

%changelog
