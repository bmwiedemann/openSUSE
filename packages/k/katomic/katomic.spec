#
# spec file for package katomic
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
Name:           katomic
Version:        22.12.0
Release:        0
Summary:        Sokoban-like logic game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/katomic
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KDEGames)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
KAtomic is a thinking game where you have to form chemical molecules
out of atoms. This is done with a nice graphical interface where you
can move each atom in a labyrinth.

%lang_package

%prep
%autosetup -p1 -n katomic-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file -r org.kde.katomic Game LogicGame

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/katomic/
%{_kf5_applicationsdir}/org.kde.katomic.desktop
%{_kf5_appsdir}/katomic/
%{_kf5_appsdir}/kconf_update/katomic-levelset*
%{_kf5_appstreamdir}/org.kde.katomic.appdata.xml
%{_kf5_bindir}/katomic
%{_kf5_debugdir}/katomic.categories
%{_kf5_iconsdir}/hicolor/*/apps/katomic.*
%{_kf5_knsrcfilesdir}/katomic.knsrc

%files lang -f %{name}.lang

%changelog
