# spec file for kweather
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


%bcond_without  released
Name:           kweather 
Version:        23.04.0
Release:        0
License:        GPL-2.0-or-later
Summary:        Weather application for Plasma
Url:            https://apps.kde.org/kweather
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KWeatherCore) >= 0.6.0
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(Qt5Charts)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickCompiler)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Requires:       kirigami-addons
Requires:       kirigami2

%description
A convergent weather application for Plasma. Has flat and dynamic/animated
views for showing forecasts and other information.

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
%dir %{_kf5_plasmadir}/plasmoids
%dir %{_kf5_plugindir}/plasma/applets
%{_datadir}/dbus-1/services/org.kde.kweather.service
%{_kf5_applicationsdir}/org.kde.kweather.desktop
%{_kf5_appstreamdir}/org.kde.kweather.appdata.xml
%{_kf5_appstreamdir}/org.kde.plasma.kweather_1x4.appdata.xml
%{_kf5_bindir}/kweather
%{_kf5_iconsdir}/hicolor/scalable/apps/org.kde.kweather.svg
%{_kf5_plasmadir}/plasmoids/org.kde.plasma.kweather_1x4/
%{_kf5_plugindir}/plasma/applets/plasma_applet_kweather_1x4.so

%files lang -f %{name}.lang

%changelog
