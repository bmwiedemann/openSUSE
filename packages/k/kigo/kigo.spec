#
# spec file for package kigo
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
Name:           kigo
Version:        22.12.0
Release:        0
Summary:        Traditional Chinese Boardgame by KDE
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kigo
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KDEGames)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     gnugo
Obsoletes:      kigo5 < %{version}
Provides:       kigo5 = %{version}

%description
Traditional Chinese Boardgame.

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

%files
%license LICENSES/*
%{_kf5_bindir}/kigo
%doc %lang(en) %{_kf5_htmldir}/en/kigo/
%{_kf5_applicationsdir}/org.kde.kigo.desktop
%{_kf5_appsdir}/kigo/
%{_kf5_appstreamdir}/org.kde.kigo.appdata.xml
%{_kf5_configkcfgdir}/kigo.kcfg
%{_kf5_debugdir}/kigo.categories
%{_kf5_iconsdir}/hicolor/*/apps/kigo.*
%{_kf5_knsrcfilesdir}/kigo*.knsrc

%files lang -f %{name}.lang

%changelog
