#
# spec file for package kguiaddons
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


%define lname   libKF5GuiAddons5
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           kguiaddons
Version:        5.116.0
Release:        0
Summary:        Utilities for graphical user interfaces
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  libQt5Gui-private-headers-devel >= %{qt5_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5WaylandClient) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5X11Extras) >= %{qt5_version}
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
Requires:       %{lname} = %{version}

%description
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input.

%package -n %{lname}
Summary:        Utilities for graphical user interfaces
Recommends:     %{name}
%requires_ge    libQt5Gui5

%description -n %{lname}
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input.

%package devel
Summary:        Utilities for graphical user interfaces: Build Environment
Requires:       %{lname} = %{version}
Requires:       cmake(Qt5Gui) >= %{qt5_version}

%description devel
The KDE GUI addons provide utilities for graphical user interfaces in the areas
of colors, fonts, text, images, keyboard input. Development files.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%ldconfig_scriptlets -n %{lname}

%files
%license LICENSES/*
%{_kf5_bindir}/kde-geo-uri-handler
%{_kf5_applicationsdir}/openstreetmap-geo-handler.desktop
%{_kf5_applicationsdir}/wheelmap-geo-handler.desktop
%{_kf5_applicationsdir}/google-maps-geo-handler.desktop
%{_kf5_applicationsdir}/qwant-maps-geo-handler.desktop

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5GuiAddons.so.*
%{_kf5_debugdir}/kguiaddons.categories

%files devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5GuiAddons/
%{_kf5_libdir}/libKF5GuiAddons.so
%{_kf5_mkspecsdir}/qt_KGuiAddons.pri

%changelog
