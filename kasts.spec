#
# spec file for package kasts
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
Name:           kasts
Version:        23.04.0
Release:        0
Summary:        Kirigami-based podcast player
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kasts
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5Syndication)
BuildRequires:  cmake(KF5ThreadWeaver)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(taglib)
Requires:       kirigami-addons
Requires:       kirigami2

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
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --all-name

%files
%license LICENSES/*
%dir %{_kf5_qmldir}/org
%dir %{_kf5_qmldir}/org/kde
%{_kf5_applicationsdir}/org.kde.kasts.desktop
%{_kf5_appstreamdir}/org.kde.kasts.appdata.xml
%{_kf5_bindir}/kasts
%{_kf5_iconsdir}/hicolor/scalable/actions/media-playback-start-cloud.svg
%{_kf5_iconsdir}/hicolor/scalable/apps/kasts-tray-*.svg
%{_kf5_iconsdir}/hicolor/scalable/apps/kasts.svg
%{_kf5_libdir}/libKMediaSession.so
%{_kf5_libdir}/libKastsSolidExtras.so
%{_kf5_qmldir}/org/kde/kasts/
%{_kf5_qmldir}/org/kde/kmediasession/

%files lang -f %{name}.lang

%changelog
