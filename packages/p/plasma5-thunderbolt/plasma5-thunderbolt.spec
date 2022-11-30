#
# spec file for package plasma5-thunderbolt
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


# Internal QML import
%global __requires_exclude qmlimport\\(org\\.kde\\.bolt.*

%define kf5_version 5.98.0
%define qt5_version 5.15.0
%bcond_without released
Name:           plasma5-thunderbolt
Version:        5.26.4
Release:        0
Summary:        Plasma frontend for Thunderbolt 3 security levels
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/plasma-thunderbolt-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-thunderbolt-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
Requires:       bolt
Requires:       kded >= %{kf5_version}
# QML imports
Requires:       kdeclarative-components >= %{kf5_version}
Requires:       kirigami2 >= %{kf5_version}
Requires:       libqt5-qtquickcontrols2 >= %{qt5_version}

%description
This is a frontend for configuring security levels of Thunderbolt 3 devices.

%lang_package

%prep
%autosetup -n plasma-thunderbolt-%{version}

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%check
export CTEST_OUTPUT_ON_FAILURE=1
export QT_QPA_PLATFORM=offscreen
dbus-run-session make %{?_smp_mflags} -C build VERBOSE=1 test

%install
%make_install -C build
%if %{with released}
  %find_lang kcm_bolt %{name}.lang
  %find_lang kded_bolt %{name}.lang
%endif

%files
%license LICENSES/*
%{_libdir}/libkbolt.so
%dir %{_kf5_plugindir}/plasma
%dir %{_kf5_plugindir}/plasma/kcms
%dir %{_kf5_plugindir}/plasma/kcms/systemsettings
%{_kf5_plugindir}/plasma/kcms/systemsettings/kcm_bolt.so
%dir %{_kf5_plugindir}/kf5/kded
%{_kf5_plugindir}/kf5/kded/kded_bolt.so
%{_kf5_notifydir}/kded_bolt.notifyrc
%dir %{_kf5_sharedir}/kpackage
%dir %{_kf5_sharedir}/kpackage/kcms
%{_kf5_sharedir}/kpackage/kcms/kcm_bolt
%{_kf5_applicationsdir}/kcm_bolt.desktop

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
