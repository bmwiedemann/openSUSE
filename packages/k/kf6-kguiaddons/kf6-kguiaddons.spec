#
# spec file for package kf6-kguiaddons
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define qt6_version 6.8.0

%define rname kguiaddons

%bcond_without kde_python_bindings
%if %{with kde_python_bindings}
%if 0%{suse_version} > 1500
%define pythons %{primary_python}
%else
%{?sle15_python_module_pythons}
%endif
%define mypython %pythons
%define __mypython %{expand:%%__%{mypython}}
%define mypython_sitearch %{expand:%%%{mypython}_sitearch}
%endif

# Full KF6 version (e.g. 6.20.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-kguiaddons
Version:        6.20.0
Release:        0
Summary:        Utilities for graphical user interfaces
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  pkgconfig(wayland-client) >= 1.15
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(wayland-protocols)
# SECTION bindings
%if %{with kde_python_bindings}
BuildRequires:  %{mypython}-build
BuildRequires:  %{mypython}-devel >= 3.9
BuildRequires:  %{mypython}-setuptools
BuildRequires:  %{mypython}-wheel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)
%endif
# /SECTION
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

%package imports
Summary:        QtQuick bindings for utilities for graphical user interfaces
Requires:       libKF6GuiAddons6 = %{version}

%description imports
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input. This package provides QtQuick
bindings to use these GUI addons with QML and QtQuick applications.

%package devel
Summary:        Utilities for graphical user interfaces: Build Environment
Requires:       libKF6GuiAddons6 = %{version}

%description devel
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input. Development files.

%if %{with kde_python_bindings}
%package -n python3-kf6-kguiaddons
Summary:        Python bindings for kf6-kguiaddons

%description -n python3-kf6-kguiaddons
This package provides Python bindings for kf6-kguiaddons.
%endif

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 \
%if %{with kde_python_bindings}
  -DPython_EXECUTABLE:STRING=%{__mypython}
%endif
%{nil}

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%ldconfig_scriptlets -n libKF6GuiAddons6

%files
%{_kf6_applicationsdir}/google-maps-geo-handler.desktop
%{_kf6_applicationsdir}/openstreetmap-geo-handler.desktop
%{_kf6_applicationsdir}/wheelmap-geo-handler.desktop
%{_kf6_bindir}/kde-geo-uri-handler
%{_kf6_debugdir}/kguiaddons.categories

%files -n libKF6GuiAddons6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6GuiAddons.so.*

%files imports
%{_kf6_qmldir}/org/kde/guiaddons/

%files devel
%{_kf6_cmakedir}/KF6GuiAddons/
%{_kf6_includedir}/KGuiAddons/
%{_kf6_libdir}/libKF6GuiAddons.so
%{_kf6_pkgconfigdir}/KF6GuiAddons.pc

%if %{with kde_python_bindings}
%files -n python3-kf6-kguiaddons
%{mypython_sitearch}/*.so
%endif

%changelog
