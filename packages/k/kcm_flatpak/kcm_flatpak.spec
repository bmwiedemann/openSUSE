#
# spec file for package kcm_flatpak
#
# Copyright (c) 2023 SUSE LLC
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


%global __requires_exclude qmlimport\\(org\\.kde\\.plasma\\.kcm\\.flatpakpermissions

%bcond_without released
Name:           kcm_flatpak
Version:        5.27.3
Release:        0
Summary:        Flatpak Permissions Management KCM
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://invent.kde.org/plasma/flatpak-kcm
Source:         https://download.kde.org/stable/plasma/%{version}/flatpak-kcm-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/flatpak-kcm-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-UPSTREAM
BuildRequires:  extra-cmake-modules >= 5.98.0
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  pkgconfig(flatpak) >= 0.11.8
# Used by the .desktop file
Requires:       systemsettings5
Supplements:    (flatpak and plasma5-workspace)

%description
The KCM allows changing what permissions have been granted to installed Flatpak applications.

%lang_package

%prep
%autosetup -p1 -n flatpak-kcm-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%find_lang %{name} %{name}.lang

%files lang -f %{name}.lang

%files
%license LICENSES/*
%dir %{_kf5_sharedir}/kpackage/
%dir %{_kf5_sharedir}/kpackage/kcms/
%{_kf5_sharedir}/kpackage/kcms/kcm_flatpak/
%dir %{_kf5_plugindir}/plasma/
%dir %{_kf5_plugindir}/plasma/kcms/
%dir %{_kf5_plugindir}/plasma/kcms/systemsettings/
%{_kf5_plugindir}/plasma/kcms/systemsettings/kcm_flatpak.so
%{_kf5_applicationsdir}/kcm_flatpak.desktop

%changelog
