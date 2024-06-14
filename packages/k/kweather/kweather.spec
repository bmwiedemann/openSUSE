#
# spec file for package kweather
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

%bcond_without released
Name:           kweather
Version:        24.05.1
Release:        0
License:        GPL-2.0-or-later
Summary:        Weather application for Plasma
URL:            https://apps.kde.org/kweather
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KWeatherCore) >= 0.8
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons) >= 0.11
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{plasma6_version}
BuildRequires:  cmake(Qt6Charts) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6OpenGL) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kf6-kholidays-imports >= %{kf6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kirigami-addons6
Requires:       qt6-charts-imports >= %{qt6_version}

%description
A convergent weather application for Plasma. Has flat and dynamic/animated
views for showing forecasts and other information.

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
%{_datadir}/dbus-1/services/org.kde.kweather.service
%{_kf6_applicationsdir}/org.kde.kweather.desktop
%{_kf6_appstreamdir}/org.kde.kweather.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.kweather_1x4.appdata.xml
%{_kf6_bindir}/kweather
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.kweather.svg
%dir %{_kf6_plasmadir}/plasmoids
%{_kf6_plasmadir}/plasmoids/org.kde.plasma.kweather_1x4/
%{_kf6_plugindir}/plasma/applets/plasma_applet_kweather_1x4.so

%files lang -f %{name}.lang

%changelog
