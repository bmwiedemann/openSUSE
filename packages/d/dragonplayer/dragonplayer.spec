#
# spec file for package dragonplayer
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define kf6_version 6.14.0
%define qt6_version 6.8.0

%define rname dragon
%bcond_without released
Name:           dragonplayer
Version:        25.08.3
Release:        0
Summary:        Multimedia Player
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/dragonplayer
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libavcodec)
Requires:       kf6-kconfig-imports >= %{kf6_version}
Requires:       kf6-kcoreaddons-imports >= %{kf6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       qt6-multimedia-imports >= %{qt6_version}

%description
Dragon Player is a simple video player.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --with-html --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.dragonplayer.desktop
%{_kf6_appstreamdir}/org.kde.dragonplayer.appdata.xml
%{_kf6_bindir}/dragon
%{_kf6_qmldir}/org/kde/dragon/
%{_kf6_iconsdir}/hicolor/*/apps/dragonplayer.*

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/dragonplayer/

%changelog
