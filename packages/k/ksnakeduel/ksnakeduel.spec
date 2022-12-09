#
# spec file for package ksnakeduel
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
Name:           ksnakeduel
Version:        22.12.0
Release:        0
Summary:        Simple snake duel game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/ksnakeduel
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KDEGames)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      ksnakeduel5 < %{version}
Provides:       ksnakeduel5 = %{version}

%description
KSnakeDuel is a simple snake duel game

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
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/*
%doc %lang(en) %{_kf5_htmldir}/en/ksnakeduel/
%{_kf5_applicationsdir}/org.kde.ksnakeduel.desktop
%{_kf5_appsdir}/ksnakeduel/
%{_kf5_appstreamdir}/org.kde.ksnakeduel.appdata.xml
%{_kf5_bindir}/ksnakeduel
%{_kf5_configkcfgdir}/ksnakeduel.kcfg
%{_kf5_debugdir}/ksnakeduel.categories
%{_kf5_iconsdir}/hicolor/*/*/ksnakeduel.*
%{_kf5_knsrcfilesdir}/ksnakeduel.knsrc

%files lang -f %{name}.lang

%changelog
