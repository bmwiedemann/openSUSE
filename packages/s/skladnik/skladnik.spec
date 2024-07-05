#
# spec file for package skladnik
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
Name:           skladnik
Version:        24.05.2
Release:        0
Summary:        Sokoban-like game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/skladnik
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  povray
BuildRequires:  cmake(KDEGames6) >= 6.0
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
Skladnik is an implementation of the Japanese warehouse keeper game “sokoban”.

The idea is that you are a warehouse keeper trying to push crates to their proper
locations in a warehouse. The problem is that you cannot pull the crates or step
over them. If you are not careful, some of the crates can get stuck in wrong
places and/or block your way.

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
%doc %lang(en) %{_kf6_htmldir}/en/skladnik/
%{_kf6_applicationsdir}/org.kde.skladnik.desktop
%{_kf6_appstreamdir}/org.kde.skladnik.metainfo.xml
%{_kf6_bindir}/skladnik
%{_kf6_iconsdir}/hicolor/*/apps/skladnik.*
%{_kf6_mandir}/man6/skladnik.6%{?ext_man}
%{_kf6_sharedir}/skladnik/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/skladnik/

%changelog
