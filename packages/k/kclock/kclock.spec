#
# spec file for package kclock
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_without  released
Name:           kclock
Version:        23.04.0
Release:        0
Summary:        Clock application for Plasma
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kclock
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Package)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickCompiler)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
Requires:       kirigami-addons
Requires:       kirigami2

%description
A clock application for Plasma.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --all-name

%files
%license LICENSES/*
%doc README.md
%dir %{_kf5_plasmadir}/plasmoids
%dir %{_kf5_plugindir}/plasma
%dir %{_kf5_plugindir}/plasma/applets
%{_datadir}/dbus-1/services/org.kde.kclockd.service
%{_kf5_applicationsdir}/org.kde.kclock.desktop
%{_kf5_appstreamdir}/org.kde.kclock.appdata.xml
%{_kf5_appstreamdir}/org.kde.plasma.kclock_1x2.appdata.xml
%{_kf5_bindir}/kclock
%{_kf5_bindir}/kclockd
%{_kf5_configdir}/autostart/org.kde.kclockd-autostart.desktop
%{_kf5_dbusinterfacesdir}/org.kde.kclockd.Alarm.xml
%{_kf5_dbusinterfacesdir}/org.kde.kclockd.AlarmModel.xml
%{_kf5_dbusinterfacesdir}/org.kde.kclockd.KClockSettings.xml
%{_kf5_dbusinterfacesdir}/org.kde.kclockd.Timer.xml
%{_kf5_dbusinterfacesdir}/org.kde.kclockd.TimerModel.xml
%{_kf5_dbusinterfacesdir}/org.kde.kclockd.Utility.xml
%{_kf5_iconsdir}/hicolor/scalable/apps/kclock_plasmoid_1x2.svg
%{_kf5_iconsdir}/hicolor/scalable/apps/org.kde.kclock.svg
%{_kf5_notifydir}/kclockd.notifyrc
%{_kf5_plasmadir}/plasmoids/org.kde.plasma.kclock_1x2/
%{_kf5_plugindir}/plasma/applets/plasma_applet_kclock_1x2.so

%files lang -f %{name}.lang

%changelog
