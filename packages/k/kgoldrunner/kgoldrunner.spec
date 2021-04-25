#
# spec file for package kgoldrunner
#
# Copyright (c) 2021 SUSE LLC
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kgoldrunner
Version:        21.04.0
Release:        0
Summary:        Action & Puzzle Solving Game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://apps.kde.org/kgoldrunner
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
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
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     %{name}-lang

%description
KGoldrunner is a game of action and puzzle solving

%lang_package

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/kgoldrunner/
%{_kf5_applicationsdir}/org.kde.kgoldrunner.desktop
%{_kf5_appsdir}/kgoldrunner
%{_kf5_appstreamdir}/org.kde.kgoldrunner.appdata.xml
%{_kf5_bindir}/kgoldrunner
%{_kf5_debugdir}/kgoldrunner.categories
%{_kf5_iconsdir}/hicolor/*/apps/kgoldrunner.*
%{_kf5_knsrcfilesdir}/kgoldrunner.knsrc

%if %{with lang}
%files lang -f %{name}.lang
%license LICENSES/*
%endif

%changelog
