#
# spec file for package plasma5-disks
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
%global __requires_exclude qmlimport\\(SMART.*

%define kf5_version 5.98.0
%bcond_without released

Name:           plasma5-disks
Version:        5.26.4
Release:        0
Summary:        Plasma service for monitoring disk health
License:        GPL-2.0-only OR GPL-3.0-only
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/plasma-disks-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-disks-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  cmake(KF5Auth) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5Service) >= %{kf5_version}
BuildRequires:  cmake(KF5Solid) >= %{kf5_version}
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)
# Old temporary name, only in K:F5
Provides:       plasma-disks = %{version}
Obsoletes:      plasma-disks < %{version}
Requires:       /usr/sbin/smartctl

%description
Monitors S.M.A.R.T. capable devices for imminent failure and informs the user.

%lang_package

%prep
%autosetup -p1 -n plasma-disks-%{version}

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%check
export CTEST_OUTPUT_ON_FAILURE=1
export QT_QPA_PLATFORM=offscreen
make %{?_smp_mflags} -C build VERBOSE=1 test

%install
%make_install -C build
%if %{with released}
  %find_lang %{name} --with-man --all-name
%endif

%files
%license LICENSES/*
%dir %{_kf5_plugindir}/plasma
%dir %{_kf5_plugindir}/plasma/kcms
%dir %{_kf5_plugindir}/plasma/kcms/kinfocenter/
%{_kf5_plugindir}/plasma/kcms/kinfocenter/smart.so
%dir %{_kf5_plugindir}/kf5/kded/
%{_kf5_plugindir}/kf5/kded/smart.so
%{_kf5_notifydir}/org.kde.kded.smart.notifyrc
%dir %{_datadir}/kpackage/
%dir %{_datadir}/kpackage/kcms/
%{_datadir}/kpackage/kcms/plasma_disks/
%{_kf5_appstreamdir}/org.kde.plasma.disks.metainfo.xml
%{_datadir}/dbus-1/system-services/org.kde.kded.smart.service
%{_kf5_dbuspolicydir}/org.kde.kded.smart.conf
%{_datadir}/polkit-1/actions/org.kde.kded.smart.policy
%{_libexecdir}/kauth/kded-smart-helper

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
