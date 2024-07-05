#
# spec file for package kclock
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0
%define plasma6_version 5.27.80

%bcond_without  released
Name:           kclock
Version:        24.05.2
Release:        0
Summary:        Clock application for Plasma
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kclock
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{plasma6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
Requires:       kirigami-addons6
Requires:       kf6-kirigami-imports >= %{kf6_version}

%description
A clock application for Plasma.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%files
%license LICENSES/*
%doc README.md
%{_datadir}/dbus-1/services/org.kde.kclockd.service
%{_kf6_applicationsdir}/org.kde.kclock.desktop
%{_kf6_appstreamdir}/org.kde.kclock.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.kclock_1x2.appdata.xml
%{_kf6_bindir}/kclock
%{_kf6_bindir}/kclockd
%{_kf6_configdir}/autostart/org.kde.kclockd-autostart.desktop
%{_kf6_dbusinterfacesdir}/org.kde.kclockd.Alarm.xml
%{_kf6_dbusinterfacesdir}/org.kde.kclockd.AlarmModel.xml
%{_kf6_dbusinterfacesdir}/org.kde.kclockd.KClockSettings.xml
%{_kf6_dbusinterfacesdir}/org.kde.kclockd.Timer.xml
%{_kf6_dbusinterfacesdir}/org.kde.kclockd.TimerModel.xml
%{_kf6_dbusinterfacesdir}/org.kde.kclockd.Utility.xml
%{_kf6_iconsdir}/hicolor/scalable/apps/kclock_plasmoid_1x2.svg
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.kclock.svg
%{_kf6_notificationsdir}/kclockd.notifyrc
%dir %{_kf6_plasmadir}/plasmoids
%{_kf6_plasmadir}/plasmoids/org.kde.plasma.kclock_1x2/
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.kclock_1x2.so

%files lang -f %{name}.lang

%changelog
