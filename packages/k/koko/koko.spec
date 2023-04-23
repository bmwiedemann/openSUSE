#
# spec file for package koko
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
Name:           koko
Version:        23.04.0
Release:        0
Summary:        Kirigami based gallery application
License:        LGPL-2.1-or-later
URL:            https://apps.kde.org/koko/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# Sources change daily, download updates before each release
# https://download.geonames.org/export/dump/cities1000.zip
Source3:        cities1000.zip
# https://download.geonames.org/export/dump/admin1CodesASCII.txt
Source4:        admin1CodesASCII.txt
# https://download.geonames.org/export/dump/admin2Codes.txt
Source5:        admin2Codes.txt
BuildRequires:  extra-cmake-modules
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KQuickImageEditor)
BuildRequires:  cmake(Qt5Positioning)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(exiv2) >= 0.21
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-atom)
Requires:       kirigami2

%description
Koko is a simple image gallery application that is designed to view, edit and
share images.

%lang_package

%prep
%autosetup -p1

cp %{SOURCE3} %{SOURCE4} %{SOURCE5} src/

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

# Not needed
rm %{buildroot}%{_kf5_libdir}/libkokocommon.so

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc README.md
%{_kf5_applicationsdir}/org.kde.koko.desktop
%{_kf5_appstreamdir}/org.kde.koko.appdata.xml
%{_kf5_bindir}/koko
%{_kf5_iconsdir}/hicolor/128x128/apps/koko.png
%{_kf5_libdir}/libkokocommon.so.*
%{_kf5_notifydir}/koko.notifyrc
%{_kf5_qmldir}/org/kde/koko/
%{_kf5_sharedir}/koko/

%files lang -f %{name}.lang

%changelog
