#
# spec file for package libksysguard5
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


%bcond_without released
%global systemstatssover 1
Name:           libksysguard5
Version:        5.26.4
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Task management and system monitoring library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/libksysguard-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/libksysguard-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
Source3:        %{name}-rpmlintrc
BuildRequires:  extra-cmake-modules >= 5.98.0
BuildRequires:  kf5-filesystem
BuildRequires:  xz
%if 0%{?suse_version} <= 1500
# It does not build with the default compiler (GCC 7) on Leap 15.x
BuildRequires:  gcc10-PIE
BuildRequires:  gcc10-c++
%endif
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Network)
%ifnarch ppc ppc64 ppc64le s390 s390x riscv64
BuildRequires:  cmake(Qt5WebChannel)
BuildRequires:  cmake(Qt5WebEngineWidgets)
%endif
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
# Has no effect, we use set_permissions
#BuildRequires:  libcap-progs
# No pkgconfig(pcap) in Leap <= 15.3 yet
BuildRequires:  libpcap-devel
# TODO: This breaks on Leap s390x
BuildRequires:  libsensors4-devel
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(zlib)
Recommends:     %{name}-imports
Recommends:     %{name}-lang
Recommends:     %{name}-plugins

%description
Task management and system monitoring library.

%package -n libKSysGuardSystemStats%{systemstatssover}
Summary:        Library for system monitoring plugins for KSystemStats
Group:          System/Libraries
Requires:       ksysguardsystemstats-data >= %{version}

%description -n libKSysGuardSystemStats%{systemstatssover}
This library is used by plugins for KSystemStats, a system monitoring daemon.

%package -n ksysguardsystemstats-data
Summary:        Data needed by libKSysGuardSystemStats
Group:          System/Libraries

%description -n ksysguardsystemstats-data
Contains the unversioned D-Bus interface definition for KSystemStats plugins.

%package devel
Summary:        Task management and system monitoring library -- devel files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libKSysGuardSystemStats%{systemstatssover} = %{version}
Requires:       cmake(KF5Config)
Requires:       cmake(KF5I18n)
Requires:       cmake(KF5IconThemes)
Requires:       cmake(Qt5Core) >= 5.15.0
Requires:       cmake(Qt5DBus)
Requires:       cmake(Qt5Network)
Requires:       cmake(Qt5Widgets)
Conflicts:      kdebase4-workspace-devel

%description devel
Task management and system monitoring library. This package contains development
files.

%package plugins
Summary:        Task management and system monitoring library -- plugins
Group:          Development/Libraries/C and C++
Conflicts:      kdebase4-workspace < 5.3.0
Requires:       %{name} = %{version}
Provides:       %{name}-helper = %{version}
Obsoletes:      %{name}-helper <= %{version}
Conflicts:      ksysguard5 < 5.21.80
# For post and verifyscript
Requires(post): permissions
Requires(verify):permissions

%description plugins
Task management and system monitoring library. This package contains plugins.

%package imports
Summary:        Task management and system monitoring library -- QML bindings
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description imports
This package provides QtQuick bindings for libksysguard, allowing its use in
QML applications.

%lang_package

%prep
%autosetup -p1 -n libksysguard-%{version}

%build
%if 0%{?suse_version} <= 1500
    export CC=gcc-10 CXX=g++-10
%endif
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with released}
  %kf5_find_lang
%endif

%post plugins
%if %{pkg_vcmp kf5-filesystem >= 20220307}
%set_permissions %{_libexecdir}/ksysguard/ksgrd_network_helper
%else
%set_permissions %{_kf5_libdir}/libexec/ksysguard/ksgrd_network_helper
%endif

%verifyscript plugins
%if %{pkg_vcmp kf5-filesystem >= 20220307}
%verify_permissions -e %{_libexecdir}/ksysguard/ksgrd_network_helper
%else
%verify_permissions -e %{_kf5_libdir}/libexec/ksysguard/ksgrd_network_helper
%endif

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post -n libKSysGuardSystemStats%{systemstatssover} -p /sbin/ldconfig
%postun -n libKSysGuardSystemStats%{systemstatssover} -p /sbin/ldconfig

%files
%license LICENSES/*
%{_kf5_debugdir}/*.categories
%{_kf5_libdir}/libKSysGuardFormatter.so.*
%{_kf5_libdir}/libKSysGuardSensorFaces.so.*
%{_kf5_libdir}/libKSysGuardSensors.so.*
%{_kf5_libdir}/libksgrd.so.*
%{_kf5_libdir}/libksignalplotter.so.*
%{_kf5_libdir}/liblsofui.so.*
%{_kf5_libdir}/libprocesscore.so.*
%{_kf5_libdir}/libprocessui.so.*
%{_kf5_knsrcfilesdir}/systemmonitor-faces.knsrc
%{_kf5_knsrcfilesdir}/systemmonitor-presets.knsrc
%dir %{_kf5_plugindir}/kpackage/
%dir %{_kf5_plugindir}/kpackage/packagestructure/
%{_kf5_plugindir}/kpackage/packagestructure/sensorface_packagestructure.so
%{_kf5_sharedir}/ksysguard/

%files -n libKSysGuardSystemStats%{systemstatssover}
%license LICENSES/*
%{_kf5_libdir}/libKSysGuardSystemStats.so.%{systemstatssover}
%{_kf5_libdir}/libKSysGuardSystemStats.so.%{_plasma5_bugfix}

%files -n ksysguardsystemstats-data
%license LICENSES/*
%{_kf5_sharedir}/dbus-1/interfaces/org.kde.ksystemstats.xml

%files plugins
%license LICENSES/*
%dir %{_kf5_plugindir}/ksysguard/
%dir %{_kf5_plugindir}/ksysguard/process
%{_kf5_plugindir}/ksysguard/process/ksysguard_plugin_network.so
%{_kf5_plugindir}/ksysguard/process/ksysguard_plugin_nvidia.so
%{_kf5_sharedir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
%{_kf5_sharedir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy
%{_kf5_dbuspolicydir}/org.kde.ksysguard.processlisthelper.conf
%if %{pkg_vcmp kf5-filesystem >= 20220307}
%dir %{_libexecdir}/kauth/
%{_libexecdir}/kauth/ksysguardprocesslist_helper
%dir %{_libexecdir}/ksysguard/
%{_libexecdir}/ksysguard/ksgrd_network_helper
%else
%dir %{_kf5_libdir}/libexec/
%dir %{_kf5_libdir}/libexec/kauth/
%{_kf5_libdir}/libexec/kauth/ksysguardprocesslist_helper
%dir %{_kf5_libdir}/libexec/ksysguard/
%{_kf5_libdir}/libexec/ksysguard/ksgrd_network_helper
%endif

%files imports
%license LICENSES/*
%dir %{_kf5_qmldir}/org/kde/ksysguard
%{_kf5_qmldir}/org/kde/ksysguard/faces
%{_kf5_qmldir}/org/kde/ksysguard/formatter
%{_kf5_qmldir}/org/kde/ksysguard/process
%{_kf5_qmldir}/org/kde/ksysguard/sensors

%files devel
%license LICENSES/*
%{_includedir}/ksysguard/
%{_kf5_libdir}/cmake/KF5SysGuard/
%{_kf5_libdir}/cmake/KSysGuard/
%dir %{_kf5_plugindir}/designer/
%{_kf5_plugindir}/designer/ksignalplotter5widgets.so
%{_kf5_plugindir}/designer/ksysguard5widgets.so
%{_kf5_plugindir}/designer/ksysguardlsof5widgets.so
%{_kf5_libdir}/libKSysGuardSystemStats.so
%{_kf5_libdir}/libKSysGuardFormatter.so
%{_kf5_libdir}/libKSysGuardSensorFaces.so
%{_kf5_libdir}/libKSysGuardSensors.so
%{_kf5_libdir}/libksgrd.so
%{_kf5_libdir}/libksignalplotter.so
%{_kf5_libdir}/liblsofui.so
%{_kf5_libdir}/libprocesscore.so
%{_kf5_libdir}/libprocessui.so

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
