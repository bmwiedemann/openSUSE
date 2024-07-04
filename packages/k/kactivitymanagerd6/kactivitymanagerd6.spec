#
# spec file for package kactivitymanagerd6
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


%global kf6_version 6.0.0
%define qt6_version 6.6.0

%define rname kactivitymanagerd
%bcond_without released
Name:           kactivitymanagerd6
Version:        6.1.2
Release:        0
Summary:        KDE Plasma Activities support
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/plasma/kactivitymanagerd
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libboost_headers-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# for kactivitymanagerd_plugin_sqlite.so
Requires:       qt6-sql-sqlite >= %{qt6_version}
Provides:       kactivitymanagerd = %{version}
Obsoletes:      kactivitymanagerd < %{version}
Obsoletes:      kactivitymanagerd-lang < %{version}

%description
Kactivities provides an API for using and interacting with the Plasma Activities Manager.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kactivities6

%post
%ldconfig
%{systemd_user_post plasma-kactivitymanagerd.service}

%preun
%{systemd_user_preun plasma-kactivitymanagerd.service}

%postun
%ldconfig
%{systemd_user_postun plasma-kactivitymanagerd.service}

%files
%license LICENSES/*
%{_kf6_debugdir}/kactivitymanagerd.categories
%{_kf6_libdir}/libkactivitymanagerd_plugin.so
%{_kf6_plugindir}/kactivitymanagerd1/
%{_kf6_sharedir}/dbus-1/services/org.kde.ActivityManager.service
%{_kf6_sharedir}/krunner/dbusplugins/plasma-runnners-activities.desktop
%{_libexecdir}/kactivitymanagerd
%{_userunitdir}/plasma-kactivitymanagerd.service

%files lang -f kactivities6.lang

%changelog
