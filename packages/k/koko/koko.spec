#
# spec file for package koko
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

%bcond_without released
Name:           koko
Version:        24.05.1
Release:        0
Summary:        Kirigami based gallery application
License:        LGPL-2.1-or-later
URL:            https://apps.kde.org/koko/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# TODO Sources change daily, download updates before each release
# https://download.geonames.org/export/dump/cities1000.zip
Source3:        cities1000.zip
# https://download.geonames.org/export/dump/admin1CodesASCII.txt
Source4:        admin1CodesASCII.txt
# https://download.geonames.org/export/dump/admin2Codes.txt
Source5:        admin2Codes.txt
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
# Both kquickimageeditor flavors provide the same CMake target name, use the devel package name instead
# BuildRequires:  cmake(KQuickImageEditor)
BuildRequires:  kquickimageeditor6-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Declarative) >= %{kf6_version}
BuildRequires:  cmake(KF6FileMetaData) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(Qt6Positioning) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(exiv2) >= 0.21
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-atom)
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kquickimageeditor6-imports
Requires:       qt6-sql-sqlite >= %{qt6_version}

%description
Koko is a simple image gallery application that is designed to view, edit and
share images.

%lang_package

%prep
%autosetup -p1

cp %{SOURCE3} %{SOURCE4} %{SOURCE5} src/

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

# Not needed
rm %{buildroot}%{_kf6_libdir}/libkokocommon.so

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/org.kde.koko.desktop
%{_kf6_appstreamdir}/org.kde.koko.appdata.xml
%{_kf6_bindir}/koko
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.koko.svg
%{_kf6_libdir}/libkokocommon.so.*
%{_kf6_notificationsdir}/koko.notifyrc
%{_kf6_qmldir}/org/kde/koko/
%{_kf6_sharedir}/koko/

%files lang -f %{name}.lang

%changelog
