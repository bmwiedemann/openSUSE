#
# spec file for package xdg-desktop-portal-kde6
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


# Internal QML import
%global __requires_exclude qt6qmlimport\\(org\\.kde\\.xdgdesktopportal.*

%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname xdg-desktop-portal-kde

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           xdg-desktop-portal-kde6
Version:        6.1.0
Release:        0
Summary:        QT/KF6 backend for xdg-desktop-portal
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  qt6-printsupport-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KWayland) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.7.0
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(wayland-client) >= 1.15
BuildRequires:  pkgconfig(wayland-protocols) >= 1.25
BuildRequires:  pkgconfig(xkbcommon)
Requires:       kf6-kiconthemes-imports >= %{kf6_version}
Requires:       kpipewire6-imports >= %{_plasma6_bugfix}
# For org.kde.plasma.workspace.dialogs.1 import
Requires:       plasma6-workspace >= %{_plasma6_bugfix}
Requires:       xdg-desktop-portal
Supplements:    (xdg-desktop-portal and plasma6-desktop)
Provides:       xdg-desktop-portal-kde = %{version}
Obsoletes:      xdg-desktop-portal-kde < %{version}
Obsoletes:      xdg-desktop-portal-kde-lang < %{version}

%description
A Qt/KF backend implementation for xdg-desktop-portal

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang xdg-desktop-portal-kde --with-man --all-name

%post
%{systemd_user_post plasma-xdg-desktop-portal-kde.service}

%preun
%{systemd_user_preun plasma-xdg-desktop-portal-kde.service}

%postun
%{systemd_user_postun plasma-xdg-desktop-portal-kde.service}

%files
%license LICENSES/*
%{_kf6_applicationsdir}/org.freedesktop.impl.portal.desktop.kde.desktop
%{_kf6_debugdir}/xdp-kde.categories
%{_kf6_notificationsdir}/xdg-desktop-portal-kde.notifyrc
%{_kf6_sharedir}/dbus-1/services/org.freedesktop.impl.portal.desktop.kde.service
%dir %{_kf6_sharedir}/xdg-desktop-portal
%{_kf6_sharedir}/xdg-desktop-portal/kde-portals.conf
%dir %{_kf6_sharedir}/xdg-desktop-portal/portals
%{_kf6_sharedir}/xdg-desktop-portal/portals/kde.portal
%{_libexecdir}/xdg-desktop-portal-kde
%{_userunitdir}/plasma-xdg-desktop-portal-kde.service

%files lang -f xdg-desktop-portal-kde.lang

%changelog
