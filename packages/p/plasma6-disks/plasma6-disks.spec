#
# spec file for package plasma6-disks
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

%define rname plasma-disks
%bcond_without released
Name:           plasma6-disks
Version:        6.1.2
Release:        0
Summary:        Plasma service for monitoring disk health
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
Requires:       /usr/sbin/smartctl
Provides:       plasma5-disks = %{version}
Obsoletes:      plasma5-disks < %{version}
Obsoletes:      plasma5-disks-lang < %{version}

%description
Monitors S.M.A.R.T. capable devices for imminent failure and informs the user.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_TESTING:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%check
export QT_QPA_PLATFORM=offscreen
%ctest

%files
%license LICENSES/*
%{_datadir}/dbus-1/system-services/org.kde.kded.smart.service
%{_datadir}/polkit-1/actions/org.kde.kded.smart.policy
%{_kf6_appstreamdir}/org.kde.plasma.disks.metainfo.xml
%{_kf6_applicationsdir}/kcm_disks.desktop
%{_kf6_dbuspolicydir}/org.kde.kded.smart.conf
%{_kf6_notificationsdir}/org.kde.kded.smart.notifyrc
%{_kf6_plugindir}/kf6/kded/smart.so
%dir %{_kf6_plugindir}/plasma/kcms/kinfocenter/
%{_kf6_plugindir}/plasma/kcms/kinfocenter/kcm_disks.so
%{_kf6_libexecdir}/kauth/kded-smart-helper

%files lang -f %{name}.lang

%changelog
