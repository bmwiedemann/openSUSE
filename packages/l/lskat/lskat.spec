#
# spec file for package lskat
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
Name:           lskat
Version:        24.05.1
Release:        0
Summary:        German Skat game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/lskat
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KDEGames6) 
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
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
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --with-html --all-name

%files
%license LICENSES/*
%doc README
%doc %lang(en) %{_kf6_htmldir}/en/lskat/
%{_kf6_applicationsdir}/org.kde.lskat.desktop
%{_kf6_appstreamdir}/org.kde.lskat.appdata.xml
%{_kf6_bindir}/lskat
%{_kf6_debugdir}/lskat.categories
%{_kf6_iconsdir}/hicolor/*/apps/lskat.*
%{_kf6_sharedir}/lskat/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/lskat/

%changelog
