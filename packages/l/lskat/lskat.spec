#
# spec file for package lskat
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
Name:           lskat
Version:        22.12.0
Release:        0
Summary:        German Skat game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/lskat
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KDEGames)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
Requires:       kdegames-carddecks-default
Obsoletes:      lskat5 < %{version}
Provides:       lskat5 = %{version}

%description
Lieutenant Skat is a nice two player card game which follows the rules
for the German game (Offiziers)-Skat. The program includes many
different carddecks to choose. A computer opponent can play for any of
the players.

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

%suse_update_desktop_file -r org.kde.lskat Game CardGame

%files
%license LICENSES/*
%doc README
%doc %lang(en) %{_kf5_htmldir}/en/lskat/
%{_kf5_applicationsdir}/org.kde.lskat.desktop
%{_kf5_appsdir}/lskat/
%{_kf5_appstreamdir}/org.kde.lskat.appdata.xml
%{_kf5_bindir}/lskat
%{_kf5_debugdir}/lskat.categories
%{_kf5_iconsdir}/hicolor/*/apps/lskat.*

%files lang -f %{name}.lang

%changelog
