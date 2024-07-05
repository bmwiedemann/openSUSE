#
# spec file for package plasmatube
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
Name:           plasmatube
Version:        24.05.2
Release:        0
Summary:        YouTube client
License:        GPL-3.0-or-later
URL:            https://apps.kde.org/plasmatube
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
BuildRequires:  cmake(KF6KirigamiAddons) >= 0.11
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(MpvQt)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kirigami-addons6
Requires:       yt-dlp

%description
PlasmaTube allows you to watch YouTube videos on your phone or desktop using a
elegant user interface integrated with the rest of Plasma.

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
%{_kf6_applicationsdir}/org.kde.plasmatube.desktop
%{_kf6_appstreamdir}/org.kde.plasmatube.appdata.xml
%{_kf6_bindir}/plasmatube
%{_kf6_debugdir}/plasmatube.categories
%{_kf6_iconsdir}/hicolor/scalable/actions/plasmatube-invidious.svg
%{_kf6_iconsdir}/hicolor/scalable/actions/plasmatube-peertube.svg
%{_kf6_iconsdir}/hicolor/scalable/actions/plasmatube-piped.svg
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.plasmatube.svg

%files lang -f %{name}.lang

%changelog
