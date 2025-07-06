#
# spec file for package killbots
#
# Copyright (c) 2025 SUSE LLC
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


%define kf6_version 6.6.0
%define qt6_version 6.6.0

%bcond_without released
Name:           killbots
Version:        25.04.3
Release:        0
Summary:        Robots-like game by KDE
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/killbots
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KDEGames6) 
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      killbots5 < %{version}
Provides:       killbots5 = %{version}

%description
Killbots is a turn-based game of evading "killer" robots on a board.
Robots home in on the player, but can crash into other robots or
debris, rendering them inert. The player has to strategically move
and can optionally use teleportation to a random location.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --with-html --all-name

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/killbots/
%{_kf6_applicationsdir}/org.kde.killbots.desktop
%{_kf6_appstreamdir}/org.kde.killbots.appdata.xml
%{_kf6_bindir}/killbots
%{_kf6_configkcfgdir}/killbots.kcfg
%{_kf6_debugdir}/killbots.categories
%{_kf6_debugdir}/killbots.renamecategories
%{_kf6_iconsdir}/hicolor/*/apps/killbots.*
%{_kf6_sharedir}/killbots/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/killbots/

%changelog
