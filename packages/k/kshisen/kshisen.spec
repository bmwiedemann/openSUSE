#
# spec file for package kshisen
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
Name:           kshisen
Version:        24.05.2
Release:        0
Summary:        Shisen-Sho Mahjongg-like game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kshisen
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KDEGames6) 
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KMahjongglib6) >= 5.1.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
Obsoletes:      kshisen5 < %{version}
Provides:       kshisen5 = %{version}

%description
Shisen-Sho (KShishen) is a game similar to Mahjongg. The object of the
game is to remove all tiles from the field. This is done by removing
two tiles with of the same type until no tile is left.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/kshisen/
%{_kf6_applicationsdir}/org.kde.kshisen.desktop
%{_kf6_appstreamdir}/org.kde.kshisen.appdata.xml
%{_kf6_bindir}/kshisen
%{_kf6_configkcfgdir}/kshisen.kcfg
%{_kf6_debugdir}/kshisen.categories
%{_kf6_iconsdir}/hicolor/*/apps/kshisen.*
%{_kf6_sharedir}/sounds/kshisen/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kshisen/

%changelog
