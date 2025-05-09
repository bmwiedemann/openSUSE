#
# spec file for package kwayland
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


# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           kwayland
Version:        5.116.0
Release:        0
Summary:        KDE Wayland library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         kwayland-5.116.0-no-server.patch
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  libQt5Gui-private-headers-devel >= %{qt5_version}
BuildRequires:  libqt5-qtwayland-private-headers-devel >= %{qt5_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.2.1
BuildRequires:  cmake(Qt5Concurrent) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5WaylandClient) >= %{qt5_version}
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client) >= 1.15.0
BuildRequires:  pkgconfig(wayland-protocols)
%requires_eq    libQt5Gui5
Provides:       libKF5WaylandClient5 = %{version}
Obsoletes:      libKF5WaylandClient5 <= %{version}
Provides:       libKF5WaylandServer5 = %{version}
Obsoletes:      libKF5WaylandServer5 <= %{version}

%description
KWayland provides a Qt-style Client and Server library wrapper for the Wayland libraries.

%package devel
Summary:        KDE Wayland library: Build Environment
Requires:       %{name} = %{version}
Requires:       cmake(Qt5Gui) >= %{qt5_version}

%description devel
KWayland provides a Qt-style Client and Server library wrapper for the Wayland libraries.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DEXCLUDE_DEPRECATED_BEFORE_AND_AT:STRING=5.74.0

%cmake_build

%install
%kf5_makeinstall -C build

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5WaylandClient.so.*

%files devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5Wayland/
%{_kf5_libdir}/libKF5WaylandClient.so
%{_kf5_libdir}/pkgconfig/KF5WaylandClient.pc
%{_kf5_mkspecsdir}/qt_KWaylandClient.pri

%changelog
