#
# spec file for package knavalbattle
#
# Copyright (c) 2024 SUSE LLC
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           knavalbattle
Version:        24.05.1
Release:        0
Summary:        Battleship game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/knavalbattle
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KDEGames6) 
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DNSSD) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Provides:       knavalbattle5 = %{version}
Obsoletes:      knavalbattle5 < %{version}

%description
KBatteship is a KDE implementation of the popular game "Battleship" where
you have to try to sink the opponents ships. The game can also be
played with friends online via the internet.

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
%doc %lang(en) %{_kf6_htmldir}/en/knavalbattle/
%{_kf6_applicationsdir}/org.kde.knavalbattle.desktop
%{_kf6_appstreamdir}/org.kde.knavalbattle.appdata.xml
%{_kf6_bindir}/knavalbattle
%{_kf6_debugdir}/knavalbattle.categories
%{_kf6_iconsdir}/hicolor/*/apps/knavalbattle.*
%{_kf6_sharedir}/knavalbattle/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/knavalbattle/

%changelog
