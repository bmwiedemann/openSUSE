#
# spec file for package plasma6-bigscreen
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define kf6_version 6.24.0
%define qt6_version 6.10.0

# Internal QMl import
%global __requires_exclude qt6qmlimport\\((org\\.kde\\.private\\.bigscreen|org\\.kde\\.private\\.biglauncher|org\\.kde\\.bigscreen).*

%define rname plasma-bigscreen
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           plasma6-bigscreen
Version:        6.7.2
Release:        0
Summary:        Plasma shell for TVs
License:        GPL-2.0-or-later
URL:            https://www.kde.org/
Source0:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6BluezQt) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Screen) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(LibKWorkspace) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivitiesStats) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(QCoro6Qml)
BuildRequires:  cmake(QCoro6Quick)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineCore) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineQuick) >= %{qt6_version}
BuildRequires:  pkgconfig(libcec)
BuildRequires:  pkgconfig(sdl3)
BuildRequires:  pkgconfig(wayland-client)
Requires:       systemsettings6
Requires:       qt6qmlimport(org.kde.bluezqt) >= %{kf6_version}
Requires:       qt6qmlimport(org.kde.kdeconnect)
Requires:       qt6qmlimport(org.kde.kquickcontrols) >= %{kf6_version}
ExclusiveArch:  x86_64 aarch64 riscv64

%description
Plasma Bigscreen is a Wayland desktop environment designed for devices like
HTPCs and SBCs connected to TVs and projectors.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

# Can't use this yet, see
# https://invent.kde.org/plasma/plasma-bigscreen/-/work_items?show=eyJpaWQiOiI1OSIsImZ1bGxfcGF0aCI6InBsYXNtYS9wbGFzbWEtYmlnc2NyZWVuIiwiaWQiOjUyNzM5fQ%3D%3D
# mkdir -p %{buildroot}%{_udevrulesdir}
# mv %{buildroot}%{_libdir}/udev/rules.d/40-uinput.rules %{buildroot}%{_udevrulesdir}/
rm %{buildroot}%{_libdir}/udev/rules.d/40-uinput.rules

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/kcm_mediacenter_audiodevice.desktop
%{_kf6_applicationsdir}/kcm_mediacenter_bigscreen_settings.desktop
%{_kf6_applicationsdir}/kcm_mediacenter_bluetooth.desktop
%{_kf6_applicationsdir}/kcm_mediacenter_display.desktop
%{_kf6_applicationsdir}/kcm_mediacenter_input.desktop
%{_kf6_applicationsdir}/kcm_mediacenter_kdeconnect.desktop
%{_kf6_applicationsdir}/kcm_mediacenter_wallpaper.desktop
%{_kf6_applicationsdir}/kcm_mediacenter_webapps.desktop
%{_kf6_applicationsdir}/kcm_mediacenter_wifi.desktop
%{_kf6_applicationsdir}/org.kde.plasma.bigscreen.inputhandler.desktop
%{_kf6_applicationsdir}/org.kde.plasma.bigscreen.uvcviewer.desktop
%{_kf6_applicationsdir}/plasma-bigscreen-swap-session.desktop
%{_kf6_appstreamdir}/org.kde.plasma.bigscreen.metainfo.xml
%{_kf6_bindir}/plasma-bigscreen-common-env
%{_kf6_bindir}/plasma-bigscreen-envmanager
%{_kf6_bindir}/plasma-bigscreen-inputhandler
%{_kf6_bindir}/plasma-bigscreen-settings
%{_kf6_bindir}/plasma-bigscreen-swap-session
%{_kf6_bindir}/plasma-bigscreen-uvcviewer
%{_kf6_bindir}/plasma-bigscreen-wayland
%{_kf6_bindir}/plasma-bigscreen-webapp
%{_kf6_dbusinterfacesdir}/org.kde.biglauncher.xml
%dir %{_kf6_plasmadir}/look-and-feel
%{_kf6_plasmadir}/look-and-feel/org.kde.plasma.bigscreen/
%{_kf6_plasmadir}/plasmoids/org.kde.bigscreen.homescreen/
%dir %{_kf6_plasmadir}/shells
%{_kf6_plasmadir}/shells/org.kde.plasma.bigscreen/
%{_kf6_pluginsdir}/kf6/kded/kded_plasma_bigscreen_start.so
%{_kf6_pluginsdir}/plasma/applets/org.kde.bigscreen.homescreen.so
%{_kf6_pluginsdir}/plasma/kcms/systemsettings/kcm_mediacenter_audiodevice.so
%{_kf6_pluginsdir}/plasma/kcms/systemsettings/kcm_mediacenter_bigscreen_settings.so
%{_kf6_pluginsdir}/plasma/kcms/systemsettings/kcm_mediacenter_bluetooth.so
%{_kf6_pluginsdir}/plasma/kcms/systemsettings/kcm_mediacenter_display.so
%{_kf6_pluginsdir}/plasma/kcms/systemsettings/kcm_mediacenter_input.so
%{_kf6_pluginsdir}/plasma/kcms/systemsettings/kcm_mediacenter_kdeconnect.so
%{_kf6_pluginsdir}/plasma/kcms/systemsettings/kcm_mediacenter_wallpaper.so
%{_kf6_pluginsdir}/plasma/kcms/systemsettings/kcm_mediacenter_webapps.so
%{_kf6_pluginsdir}/plasma/kcms/systemsettings/kcm_mediacenter_wifi.so
%{_kf6_qmldir}/org/kde/bigscreen/
%{_kf6_sharedir}/sounds/plasma-bigscreen/
%dir %{_kf6_sharedir}/wayland-sessions
%{_kf6_sharedir}/wayland-sessions/plasma-bigscreen-wayland.desktop
#%%{_udevrulesdir}/40-uinput.rules

%files lang -f %{name}.lang

%changelog
