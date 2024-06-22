#
# spec file for package layer-shell-qt6
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2021 Fabian Vogt
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%define rname layer-shell-qt
%bcond_without released
Name:           layer-shell-qt6
Version:        6.1.0
Release:        0
Summary:        wlr-layer-shell integration for Qt
License:        LGPL-3.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-wayland-private-devel >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  pkgconfig(wayland-client) >= 1.3.0
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server) >= 1.3.0
BuildRequires:  pkgconfig(xkbcommon)

%description
This allows integration of Qt applications with wlr-layer-shell.

%package -n libLayerShellQtInterface6
Summary:        wlr-layer-shell integration for Qt 6 - library
Requires:       layer-shell-qt6 = %{version}

%description -n libLayerShellQtInterface6
This allows integration of Qt applications with wlr-layer-shell.

%package imports
Summary:        wlr-layer-shell integration for Qt 6 - QtQuick support
Requires:       layer-shell-qt6 = %{version}
Requires:       libLayerShellQtInterface6 = %{version}

%description imports
This package provides a QML plugin and QtQuick components for
layer-shell-qt6, a library for integration of Qt applications with
wlr-layer-shell.

%package -n layer-shell-qt6-devel
Summary:        wlr-layer-shell integration for Qt 6 - development files
Requires:       libLayerShellQtInterface6 = %{version}
Conflicts:      layer-shell-qt5-devel

%description -n layer-shell-qt6-devel
This allows integration of Qt applications with wlr-layer-shell.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets -n libLayerShellQtInterface6

%files
%{_kf6_plugindir}/wayland-shell-integration/liblayer-shell.so

%files -n libLayerShellQtInterface6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libLayerShellQtInterface.so.6
%{_kf6_libdir}/libLayerShellQtInterface.so.*

%files imports
%{_kf6_qmldir}/org/kde/layershell/

%files -n layer-shell-qt6-devel
%{_includedir}/LayerShellQt/
%{_kf6_cmakedir}/LayerShellQt/
%{_kf6_libdir}/libLayerShellQtInterface.so

%changelog
