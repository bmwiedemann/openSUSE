#
# spec file for package plasma6-integration
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


%global kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released

# Compatibility with plasma5
%bcond_without plasma5
%if %{with plasma5}
%define kf5_version 5.102.0
%define qt5_version 5.15.2
%endif
%define rname plasma-integration
Name:           plasma6-integration
Version:        6.1.2
Release:        0
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(Breeze) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KWayland) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
%if %{with plasma5}
BuildRequires:  kf5-filesystem
BuildRequires:  libqt5-qtbase-private-headers-devel >= %{qt5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5Wayland) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlGui) >= %{kf5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5QuickControls2) >= %{qt5_version}
BuildRequires:  cmake(Qt5ThemeSupport) >= %{qt5_version}
BuildRequires:  cmake(Qt5WaylandClient) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5X11Extras) >= %{qt5_version}
%endif
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcursor)

%description
Plasma Integration is a set of plugins responsible for better integration of Qt
applications when running on a KDE Plasma workspace.

Applications do not need to link to this directly.

%package plugin
Summary:        Plugins responsible for better integration of Qt applications in KDE Workspace
Requires:       hack-fonts
Requires:       noto-sans
Requires:       xdg-desktop-portal-kde6
# Forced on all QGuiApplications
Requires:       qqc2-breeze-style6
%requires_eq    libQt6Gui6
Provides:       plasma5-integration-plugin < %{version}
Obsoletes:      plasma5-integration-plugin < %{version}
Obsoletes:      plasma5-integration-plugin-lang < %{version}

%description plugin
Plasma Integration is a set of plugins responsible for better integration of Qt
applications when running on a KDE Plasma workspace.

Applications do not need to link to this directly.

%lang_package -n plasma6-integration-plugin

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 \
  -DBUILD_QT6:BOOL=TRUE \
%if %{with plasma5}
  -DBUILD_QT5:BOOL=TRUE
%else
  -DBUILD_QT5:BOOL=FALSE
%endif

%kf6_build

%install
%kf6_install

%find_lang plasmaintegration5

%files plugin
%license LICENSES/*
%if %{with plasma5}
%{_kf5_plugindir}/platformthemes
%{_kf5_plugindir}/platformthemes/KDEPlasmaPlatformTheme5.so
%endif
%dir %{_kf6_plugindir}/platformthemes
%{_kf6_plugindir}/platformthemes/KDEPlasmaPlatformTheme6.so

%files -n plasma6-integration-plugin-lang -f plasmaintegration5.lang

%changelog
