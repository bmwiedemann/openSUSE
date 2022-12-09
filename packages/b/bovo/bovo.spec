#
# spec file for package bovo
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
Name:           bovo
Version:        22.12.0
Release:        0
Summary:        Five-in-a-row Board Game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/bovo
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  xz
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5KDEGames)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Bovo is a Gomoku (Connect Five, Five in a row, X and O, etc) game by KDE.

%lang_package

%prep
%autosetup -p1 -n bovo-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%files
%license COPYING*
%doc %lang(en) %{_kf5_htmldir}/en/bovo/
%{_kf5_applicationsdir}/org.kde.bovo.desktop
%{_kf5_appstreamdir}/org.kde.bovo.appdata.xml
%{_kf5_bindir}/bovo
%{_kf5_iconsdir}/hicolor/*/apps/bovo.*
%{_kf5_sharedir}/bovo/

%files lang -f %{name}.lang

%changelog
