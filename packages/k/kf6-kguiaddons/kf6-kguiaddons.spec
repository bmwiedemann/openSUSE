#
# spec file for package kf6-kguiaddons
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

%define rname kguiaddons
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kguiaddons
Version:        6.3.0
Release:        0
Summary:        Utilities for graphical user interfaces
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
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  pkgconfig(wayland-client) >= 1.9
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
Requires:       libKF6GuiAddons6 = %{version}
# https://community.kde.org/Plasma/Plasma_6#Coinstallability
Provides:       kguiaddons = %{version}
Obsoletes:      kguiaddons < %{version}

%description
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input.

%package -n libKF6GuiAddons6
Summary:        Utilities for graphical user interfaces
Requires:       kf6-kguiaddons >= %{version}

%description -n libKF6GuiAddons6
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input.

%package devel
Summary:        Utilities for graphical user interfaces: Build Environment
Requires:       libKF6GuiAddons6 = %{version}

%description devel
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input. Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%ldconfig_scriptlets -n libKF6GuiAddons6

%files
%{_kf6_applicationsdir}/google-maps-geo-handler.desktop
%{_kf6_applicationsdir}/openstreetmap-geo-handler.desktop
%{_kf6_applicationsdir}/qwant-maps-geo-handler.desktop
%{_kf6_applicationsdir}/wheelmap-geo-handler.desktop
%{_kf6_bindir}/kde-geo-uri-handler
%{_kf6_debugdir}/kguiaddons.categories

%files -n libKF6GuiAddons6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6GuiAddons.so.*

%files devel
%doc %{_kf6_qchdir}/KF6GuiAddons.*
%{_kf6_cmakedir}/KF6GuiAddons/
%{_kf6_includedir}/KGuiAddons/
%{_kf6_libdir}/libKF6GuiAddons.so
%{_kf6_pkgconfigdir}/KF6GuiAddons.pc

%changelog
