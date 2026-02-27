#
# spec file for package flatpak-kcm6
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define kf6_version 6.18.0
%define qt6_version 6.9.0

%define rname flatpak-kcm

%bcond_without released
Name:           flatpak-kcm6
Version:        6.6.1
Release:        0
Summary:        Flatpak Permissions Management KCM
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/plasma/flatpak-kcm
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  pkgconfig(flatpak) >= 0.11.8
# Used by the .desktop file
Requires:       systemsettings6
Supplements:    (flatpak and plasma6-workspace)
Provides:       kcm_flatpak = %{version}
Obsoletes:      kcm_flatpak < %{version}
Obsoletes:      kcm_flatpak-lang < %{version}

%description
The KCM allows changing what permissions have been granted to installed Flatpak applications.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang kcm_app-permissions %{name}.lang

%files
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_app-permissions.desktop
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_app-permissions.so

%files lang -f %{name}.lang

%changelog
