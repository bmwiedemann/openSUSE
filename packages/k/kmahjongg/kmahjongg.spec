#
# spec file for package kmahjongg
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
Name:           kmahjongg
Version:        24.05.1
Release:        0
Summary:        Mahjongg game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kmahjongg
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KDEGames6) 
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KMahjongglib6) >= 5.1.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
Obsoletes:      kmahjongg5 < %{version}
Provides:       kmahjongg5 = %{version}

%description
KMahjongg is a clone of the well known tile based patience game of the
same name. In the game you have to empty a game board filled with piece
by removing pieces of the same type.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/kmahjongg/
%{_kf6_applicationsdir}/org.kde.kmahjongg.desktop
%{_kf6_appstreamdir}/org.kde.kmahjongg.appdata.xml
%{_kf6_bindir}/kmahjongg
%{_kf6_configkcfgdir}/kmahjongg.kcfg
%{_kf6_debugdir}/kmahjongg.categories
%{_kf6_iconsdir}/hicolor/*/apps/kmahjongg.*
%{_kf6_sharedir}/kmahjongg/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kmahjongg/

%changelog
