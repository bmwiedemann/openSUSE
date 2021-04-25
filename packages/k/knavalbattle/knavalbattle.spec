#
# spec file for package knavalbattle
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
Name:           knavalbattle
Version:        21.04.0
Release:        0
Summary:        Battleship game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Other
URL:            https://apps.kde.org/knavalbattle
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
BuildRequires:  cmake(KF5DNSSD)
BuildRequires:  cmake(KF5Declarative)
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
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Provides:       knavalbattle5 = %{version}
Obsoletes:      knavalbattle5 < %{version}
Recommends:     %{name}-lang

%description
KBatteship is a KDE implentation of the popular game "Battleship" where
you have to try to sink the opponents ships. The game can also be
played with friends online via the internet.

%lang_package

%prep
%autosetup -p1 -n knavalbattle-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file -r org.kde.knavalbattle    Game BoardGame

%files
%license COPYING COPYING.DOC
%doc %lang(en) %{_kf5_htmldir}/en/knavalbattle/

%{_kf5_applicationsdir}/org.kde.knavalbattle.desktop
%dir %{_kf5_appsdir}/kconf_update
%{_kf5_appsdir}/kconf_update/knavalbattle.upd
%{_kf5_appsdir}/knavalbattle/
%{_kf5_appstreamdir}/org.kde.knavalbattle.appdata.xml
%{_kf5_bindir}/knavalbattle
%{_kf5_debugdir}/knavalbattle.categories
%{_kf5_iconsdir}/hicolor/*/apps/knavalbattle.*
%{_kf5_kxmlguidir}/knavalbattle/
%{_kf5_servicesdir}/knavalbattle.protocol

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
