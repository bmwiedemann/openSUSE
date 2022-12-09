#
# spec file for package kshisen
#
# Copyright (c) 2022 SUSE LLC
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kshisen
Version:        22.12.0
Release:        0
Summary:        Shisen-Sho Mahjongg-like game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kshisen
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-OPENSUSE cpp14.patch fabian@ritter-vogt.de Use only c++11 features
Patch1:         cpp14.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5KDEGames)
BuildRequires:  cmake(KF5KMahjongglib)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Shisen-Sho (KShishen) is a game similar to Mahjongg. The object of the
game is to remove all tiles from the field. This is done by removing
two tiles with of the same type until no tile is left.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file -r org.kde.kshisen Game BoardGame

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/kshisen/
%{_kf5_applicationsdir}/org.kde.kshisen.desktop
%{_kf5_appstreamdir}/org.kde.kshisen.appdata.xml
%{_kf5_bindir}/kshisen
%{_kf5_configkcfgdir}/
%{_kf5_debugdir}/kshisen.categories
%{_kf5_iconsdir}/hicolor/*/apps/kshisen.*
%{_kf5_sharedir}/sounds/kshisen/

%files lang -f %{name}.lang

%changelog
