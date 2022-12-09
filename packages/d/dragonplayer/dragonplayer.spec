#
# spec file for package dragonplayer
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


%define rname dragon
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           dragonplayer
Version:        22.12.0
Release:        0
Summary:        Multimedia Player
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/dragonplayer
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Phonon4Qt5)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Dragon Player is a simple video player.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file org.kde.dragonplayer Video

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/dragonplayer/
%doc %{_kf5_mandir}/man1/dragon.1*
%doc README
%config %{_kf5_configdir}/dragonplayerrc
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/parts
%dir %{_kf5_servicesdir}/ServiceMenus
%dir %{_kf5_sharedir}/solid
%dir %{_kf5_sharedir}/solid/actions
%{_kf5_applicationsdir}/org.kde.dragonplayer.desktop
%{_kf5_appstreamdir}/org.kde.dragonplayer.appdata.xml
%{_kf5_bindir}/dragon
%{_kf5_iconsdir}/hicolor/*/apps/dragonplayer.*
%{_kf5_iconsdir}/oxygen/*/actions/player-volume-muted.*
%{_kf5_plugindir}/kf5/parts/dragonpart.so
%{_kf5_servicesdir}/ServiceMenus/dragonplayer_play_dvd.desktop
%{_kf5_servicesdir}/dragonplayer_part.desktop
%{_kf5_sharedir}/solid/actions/dragonplayer-openaudiocd.desktop
%{_kf5_sharedir}/solid/actions/dragonplayer-opendvd.desktop

%files lang -f %{name}.lang

%changelog
