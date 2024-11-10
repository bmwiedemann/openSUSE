#
# spec file for package kf6-bluez-qt
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


%define qt6_version 6.7.0

%define rname bluez-qt
# Full KF6 version (e.g. 6.8.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-bluez-qt
Version:        6.8.0
Release:        0
Summary:        Async Bluez wrapper library
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
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
Async Bluez wrapper library.

%package -n libKF6BluezQt6
Summary:        Async Bluez wrapper library
Requires:       kf6-bluez-qt >= %{version}

%description -n libKF6BluezQt6
Async Bluez wrapper library.

%package imports
Summary:        Async Bluez wrapper library
Supplements:    (libKF6BluezQt6 and libQt6Qml6)

%description imports
Async Bluez wrapper library.
QML imports.

%package devel
Summary:        Async Bluez wrapper library - development files
Requires:       libKF6BluezQt6 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description devel
Development files for QBluez Async Bluez wrapper library.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%ldconfig_scriptlets -n libKF6BluezQt6

%files
%{_kf6_debugdir}/bluezqt.categories
%{_kf6_debugdir}/bluezqt.renamecategories

%files -n libKF6BluezQt6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6BluezQt.so.*

%files imports
%{_kf6_qmldir}/org/kde/bluezqt/

%files devel
%doc %{_kf6_qchdir}/KF6BluezQt.*
%{_kf6_cmakedir}/KF6BluezQt/
%{_kf6_includedir}/BluezQt/
%{_kf6_libdir}/libKF6BluezQt.so
%{_kf6_pkgconfigdir}/KF6BluezQt.pc

%changelog
