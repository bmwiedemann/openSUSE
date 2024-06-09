#
# spec file for package kf6-networkmanager-qt
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

%define rname networkmanager-qt
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-networkmanager-qt
Version:        6.3.0
Release:        0
Summary:        A Qt wrapper for NetworkManager DBus API
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
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libnm) >= 1.4.0

%description
NetworkManagerQt provides access to all NetworkManager features
exposed on DBus. It allows you to manage your connections and control
your network devices and also provides a library for parsing connection
settings which are used in DBus communication.

%package imports
Summary:        QML components for networkmanager-qt

%description imports
This package provides QML bindings for networkmanager-qt.

%package -n libKF6NetworkManagerQt6
Summary:        A Qt wrapper for NetworkManager DBus API
Requires:       kf6-networkmanager-qt >= %{version}

%description -n libKF6NetworkManagerQt6
NetworkManagerQt provides access to all NetworkManager features
exposed on DBus. It allows you to manage your connections and control
your network devices and also provides a library for parsing connection
settings which are used in DBus communication.

%package devel
Summary:        A Qt wrapper for NetworkManager DBus API
Requires:       libKF6NetworkManagerQt6 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       pkgconfig(gio-2.0)
Requires:       pkgconfig(libnm) >= 1.4.0

%description devel
NetworkManagerQt provides access to all NetworkManager features
exposed on DBus. It allows you to manage your connections and control
your network devices and also provides a library for parsing connection
settings which are used in DBus communication. Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets -n libKF6NetworkManagerQt6

%files
%{_kf6_debugdir}/networkmanagerqt.categories
%{_kf6_debugdir}/networkmanagerqt.renamecategories

%files imports
%{_kf6_qmldir}/org/kde/networkmanager/

%files -n libKF6NetworkManagerQt6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6NetworkManagerQt.so.*

%files devel
%doc %{_kf6_qchdir}/KF6NetworkManagerQt.*
%{_kf6_cmakedir}/KF6NetworkManagerQt/
%{_kf6_includedir}/NetworkManagerQt/
%{_kf6_libdir}/libKF6NetworkManagerQt.so

%changelog
