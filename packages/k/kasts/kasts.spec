#
# spec file for package kasts
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
Name:           kasts
Version:        24.05.2
Release:        0
Summary:        Kirigami-based podcast player
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kasts
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons) >= 0.7
BuildRequires:  cmake(KF6NetworkManagerQt) >= %{kf6_version}
BuildRequires:  cmake(KF6Syndication) >= %{kf6_version}
BuildRequires:  cmake(KF6ThreadWeaver) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(taglib)
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kirigami-addons6
Requires:       qt6-sql-sqlite >= %{qt6_version}

%description
Kasts is a convergent podcast application.
Its main features are:

- Episode management through play queue
- Sync playback positions with other clients through gpodder.net or
  gpodder-nextcloud
- Variable playback speed
- Search for podcasts
- Full system integration: e.g. inhibit system suspend while listening

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
%{_kf6_applicationsdir}/org.kde.kasts.desktop
%{_kf6_appstreamdir}/org.kde.kasts.appdata.xml
%{_kf6_bindir}/kasts
%{_kf6_iconsdir}/hicolor/scalable/actions/media-playback-cloud.svg
%{_kf6_iconsdir}/hicolor/scalable/apps/kasts-tray-*.svg
%{_kf6_iconsdir}/hicolor/scalable/apps/kasts.svg
%{_kf6_libdir}/libKMediaSession.so

%files lang -f %{name}.lang

%changelog
