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


%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without released
Name:           kwayland
Version:        5.101.0
Release:        0
Summary:        KDE Wayland library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libQt5Gui-private-headers-devel >= 5.15.0
BuildRequires:  libqt5-qtwayland-private-headers-devel >= 5.15.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.2.1
BuildRequires:  cmake(Qt5Concurrent) >= 5.15.0
BuildRequires:  cmake(Qt5Gui) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5WaylandClient) >= 5.15.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client) >= 1.15.0
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server) >= 1.15.0
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
Requires:       extra-cmake-modules >= %{_kf5_bugfix_version}
Requires:       cmake(Qt5Gui) >= 5.15.0

%description devel
KWayland provides a Qt-style Client and Server library wrapper for the Wayland libraries.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5WaylandClient.so.*
%{_kf5_libdir}/libKF5WaylandServer.so.*

%files devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5Wayland/
%{_kf5_libdir}/libKF5WaylandClient.so
%{_kf5_libdir}/libKF5WaylandServer.so
%{_kf5_libdir}/pkgconfig/KF5WaylandClient.pc
%{_kf5_mkspecsdir}/qt_KWaylandClient.pri
%{_kf5_mkspecsdir}/qt_KWaylandServer.pri
%{_libexecdir}/org-kde-kf5-kwayland-testserver

%changelog
