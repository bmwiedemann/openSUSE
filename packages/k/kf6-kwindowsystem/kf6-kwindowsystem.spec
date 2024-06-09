#
# spec file for package kf6-kwindowsystem
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

%define rname kwindowsystem
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kwindowsystem
Version:        6.3.0
Release:        0
Summary:        KDE Access to window manager
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
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  qt6-waylandclient-private-devel >= %{qt6_version}
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  pkgconfig(wayland-protocols) >= 1.21.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrender)

%description
Convenience access to certain properties and features of the window manager.

KWindowSystem provides information about the state of the window manager and
allows asking the window manager to change the using a more high-level
interface than the NETWinInfo/NETRootInfo low-level classes.

%package imports
Summary:        QML Bindings for KWindowSystem

%description imports
QML Bindings for KWindowSystem.

%package -n libKF6WindowSystem6
Summary:        KDE Access to window manager
Requires:       kf6-kwindowsystem >= %{version}

%description -n libKF6WindowSystem6
Convenience access to certain properties and features of the window manager.

KWindowSystem provides information about the state of the window manager and
allows asking the window manager to change the using a more high-level
interface than the NETWinInfo/NETRootInfo low-level classes.

%package devel
Summary:        KDE Access to window manager: Build Environment
Requires:       libKF6WindowSystem6 = %{version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xcb)

%description devel
Convenience access to certain properties and features of the window manager.

KWindowSystem provides information about the state of the window manager and
allows asking the window manager to change the using a more high-level
interface than the NETWinInfo/NETRootInfo low-level classes.
Development files.

%lang_package -n libKF6WindowSystem6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kwindowsystem6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6WindowSystem6

%files
%{_kf6_debugdir}/kwindowsystem.categories
%{_kf6_debugdir}/kwindowsystem.renamecategories
%dir %{_kf6_plugindir}/kf6/kwindowsystem
%{_kf6_plugindir}/kf6/kwindowsystem/KF6WindowSystemKWaylandPlugin.so
%{_kf6_plugindir}/kf6/kwindowsystem/KF6WindowSystemX11Plugin.so

%files imports
%{_kf6_qmldir}/org/kde/kwindowsystem/

%files -n libKF6WindowSystem6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6WindowSystem.so.*

%files devel
%doc %{_kf6_qchdir}/KF6WindowSystem.*
%{_kf6_includedir}/KWindowSystem/
%{_kf6_cmakedir}/KF6WindowSystem/
%{_kf6_libdir}/libKF6WindowSystem.so
%{_kf6_pkgconfigdir}/KF6WindowSystem.pc

%files -n libKF6WindowSystem6-lang -f kwindowsystem6.lang

%changelog
