#
# spec file for package libksysguard6
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

%define rname libksysguard

%bcond_without released

# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF6, but 5.8.95 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Name:           libksysguard6
Version:        6.1.2
Release:        0
Summary:        Task management and system monitoring library
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
Source3:        libksysguard6-rpmlintrc
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libsensors4-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(zlib)
# Has no effect, we use set_permissions
# BuildRequires:  libcap-progs
Recommends:     libksysguard6-imports
Recommends:     libksysguard6-plugins
Provides:       libksysguard5 = %{version}
Obsoletes:      libksysguard5 < %{version}
Obsoletes:      libksysguard5-lang < %{version}

%description
Task management and system monitoring library.

%package -n libKSysGuardSystemStats2
Summary:        Library for system monitoring plugins for KSystemStats
Requires:       ksysguardsystemstats6-data >= %{version}

%description -n libKSysGuardSystemStats2
This library is used by plugins for KSystemStats, a system monitoring daemon.

%package -n ksysguardsystemstats6-data
Summary:        Data needed by libKSysGuardSystemStats
Provides:       ksysguardsystemstats-data = %{version}
Obsoletes:      ksysguardsystemstats-data < %{version}

%description -n ksysguardsystemstats6-data
Contains the unversioned D-Bus interface definition for KSystemStats plugins.

%package plugins
Summary:        Task management and system monitoring library -- plugins
Requires:       libksysguard6 = %{version}
# For post and verifyscript
Requires(post): permissions
Requires(verify): permissions
Conflicts:      kdebase4-workspace < 5.3.0
Conflicts:      ksysguard5 < 5.21.80
Provides:       libksysguard5-plugins = %{version}
Obsoletes:      libksysguard5-plugins < %{version}
Provides:       libksysguard5-helper = %{version}
Obsoletes:      libksysguard5-helper < %{version}

%description plugins
Task management and system monitoring library. This package contains plugins.

%package imports
Summary:        Task management and system monitoring library -- QML bindings
Requires:       libksysguard6 = %{version}
Obsoletes:      libksysguard5-imports < %{version}

%description imports
This package provides QtQuick bindings for libksysguard, allowing its use in
QML applications.

%package devel
Summary:        Task management and system monitoring library -- devel files
Requires:       libKSysGuardSystemStats2 >= %{version}
Requires:       libksysguard6 >= %{version}
Requires:       cmake(KF6Config) >= %{kf6_version}
Requires:       cmake(KF6I18n) >= %{kf6_version}
Requires:       cmake(KF6IconThemes) >= %{kf6_version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Network) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
Provides:       libksysguard5-devel = %{version}
Obsoletes:      libksysguard5-devel < %{version}

%description devel
Task management and system monitoring library. This package contains development
files.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%post plugins
%set_permissions %{_libexecdir}/ksysguard/ksgrd_network_helper

%verifyscript plugins
%verify_permissions -e %{_libexecdir}/ksysguard/ksgrd_network_helper

%ldconfig_scriptlets
%ldconfig_scriptlets -n libKSysGuardSystemStats2

%files
# TODO? split libraries and drop the -rpmlintrc file
%license LICENSES/*
%{_kf6_debugdir}/libksysguard.categories
%{_kf6_knsrcfilesdir}/systemmonitor-faces.knsrc
%{_kf6_knsrcfilesdir}/systemmonitor-presets.knsrc
%{_kf6_libdir}/libKSysGuardFormatter.so.*
%{_kf6_libdir}/libKSysGuardSensorFaces.so.*
%{_kf6_libdir}/libKSysGuardSensors.so.*
%{_kf6_libdir}/libprocesscore.so.*
%dir %{_kf6_plugindir}/kf6/packagestructure/
%{_kf6_plugindir}/kf6/packagestructure/ksysguard_sensorface.so
%{_kf6_sharedir}/ksysguard/

%files -n libKSysGuardSystemStats2
%license LICENSES/*
%{_kf6_libdir}/libKSysGuardSystemStats.so.*

%files -n ksysguardsystemstats6-data
%{_kf6_sharedir}/dbus-1/interfaces/org.kde.ksystemstats1.xml

%files plugins
%{_kf6_dbuspolicydir}/org.kde.ksysguard.processlisthelper.conf
%dir %{_kf6_plugindir}/ksysguard/
%dir %{_kf6_plugindir}/ksysguard/process
%{_kf6_plugindir}/ksysguard/process/ksysguard_plugin_network.so
%{_kf6_plugindir}/ksysguard/process/ksysguard_plugin_nvidia.so
%{_kf6_sharedir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
%{_kf6_sharedir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy
%{_kf6_libexecdir}/kauth/ksysguardprocesslist_helper
%dir %{_libexecdir}/ksysguard/
%{_libexecdir}/ksysguard/ksgrd_network_helper

%files imports
%dir %{_kf6_qmldir}/org/kde/ksysguard
%{_kf6_qmldir}/org/kde/ksysguard/faces/
%{_kf6_qmldir}/org/kde/ksysguard/formatter/
%{_kf6_qmldir}/org/kde/ksysguard/process/
%{_kf6_qmldir}/org/kde/ksysguard/sensors/

%files devel
%{_includedir}/ksysguard/
%{_kf6_cmakedir}/KSysGuard/
%{_kf6_libdir}/libKSysGuardFormatter.so
%{_kf6_libdir}/libKSysGuardSensorFaces.so
%{_kf6_libdir}/libKSysGuardSensors.so
%{_kf6_libdir}/libKSysGuardSystemStats.so
%{_kf6_libdir}/libprocesscore.so

%files lang -f %{name}.lang

%changelog
