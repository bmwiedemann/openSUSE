#
# spec file for package plasma6-thunderbolt
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname plasma-thunderbolt

%bcond_without released
Name:           plasma6-thunderbolt
Version:        6.1.2
Release:        0
Summary:        Plasma frontend for Thunderbolt 3 security levels
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
Requires:       bolt
Requires:       kf6-kded >= %{kf6_version}
# QML imports
Requires:       kf6-kdeclarative-imports >= %{kf6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       qt6-declarative-imports >= %{qt6_version}
Provides:       plasma5-thunderbolt = %{version}
Obsoletes:      plasma5-thunderbolt < %{version}
Obsoletes:      plasma5-thunderbolt-lang < %{version}

%description
This is a frontend for configuring security levels of Thunderbolt 3 devices.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_TESTING=ON

%kf6_build

%install
%kf6_install

%find_lang kcm_bolt %{name}.lang
%find_lang kded_bolt %{name}.lang

%check
export CTEST_OUTPUT_ON_FAILURE=1
export QT_QPA_PLATFORM=offscreen
# ctest can't be used or it would reset the dbus session
dbus-run-session cmake --build %{__kf6_builddir} -t test

%files
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_bolt.desktop
%{_kf6_libdir}/libkbolt.so
%{_kf6_notificationsdir}/kded_bolt.notifyrc
%{_kf6_plugindir}/kf6/kded/kded_bolt.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_bolt.so

%files lang -f %{name}.lang

%changelog
