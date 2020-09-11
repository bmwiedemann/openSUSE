#
# spec file for package kspaceduel
#
# Copyright (c) 2020 SUSE LLC
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
Name:           kspaceduel
Version:        20.08.1
Release:        0
Summary:        Space Arcade game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     %{name}-lang
Obsoletes:      kspaceduel5 < %{version}
Provides:       kspaceduel5 = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
KSpaceduel is a space arcade game for two players. However, one player
can be controlled by the computer. Each player controls a satellite
that flies around the sun. While doing so both players try not to
collide with anything but shoot at the other space ship.

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file -r org.kde.kspaceduel          Game ArcadeGame

%files
%license COPYING*
%dir %{_kf5_appstreamdir}
%dir %{_kf5_configkcfgdir}
%doc %lang(en) %{_kf5_htmldir}/en/kspaceduel/
%{_kf5_applicationsdir}/org.kde.kspaceduel.desktop
%{_kf5_appsdir}/kspaceduel/
%{_kf5_appstreamdir}/org.kde.kspaceduel.appdata.xml
%{_kf5_bindir}/kspaceduel
%{_kf5_configkcfgdir}/kspaceduel.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/kspaceduel.*
%{_kf5_kxmlguidir}/kspaceduel/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
