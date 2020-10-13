#
# spec file for package libksysguard5
#
# Copyright (c) 2020 SUSE LLC
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


%bcond_without lang
Name:           libksysguard5
Version:        5.20.0
Release:        0
Summary:        Task management and system monitoring library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.kde.org
Source:         libksysguard-%{version}.tar.xz
%if %{with lang}
Source1:        libksysguard-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
Source3:        baselibs.conf
BuildRequires:  extra-cmake-modules >= 1.2.0
BuildRequires:  kf5-filesystem
BuildRequires:  xz
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
BuildRequires:  cmake(Qt5DBus) >= 5.4.0
BuildRequires:  cmake(Qt5Network) >= 5.4.0
%ifnarch ppc ppc64 ppc64le s390 s390x riscv64
BuildRequires:  cmake(Qt5WebChannel) >= 5.4.0
BuildRequires:  cmake(Qt5WebEngineWidgets) >= 5.4.0
%endif
BuildRequires:  cmake(Qt5UiPlugin) >= 5.14.0
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.4.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(zlib)
Recommends:     %{name}-lang
Recommends:     %{name}-imports

%description
Task management and system monitoring library.

%package devel
Summary:        Task management and system monitoring library -- devel files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       cmake(KF5Config)
Requires:       cmake(KF5I18n)
Requires:       cmake(KF5IconThemes)
Requires:       cmake(Qt5Core) >= 5.4.0
Requires:       cmake(Qt5Network) >= 5.4.0
Requires:       cmake(Qt5Widgets) >= 5.4.0
Conflicts:      kdebase4-workspace-devel

%description devel
Task management and system monitoring library. This package contains development
files.

%package helper
Summary:        Task management and system monitoring library -- helper files
Group:          Development/Libraries/C and C++
Conflicts:      kdebase4-workspace < 5.3.0

%description helper
Task management and system monitoring library. This package contains helper files
for actions that require elevated privileges.

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
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %kf5_find_lang
%endif

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING*
%dir %{_kf5_plugindir}/kpackage/
%dir %{_kf5_plugindir}/kpackage/packagestructure/
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
%{_kf5_plugindir}/kpackage/packagestructure/sensorface_packagestructure.so
%{_kf5_sharedir}/ksysguard/

%files helper
%license COPYING*
%{_kf5_dbuspolicydir}/org.kde.ksysguard.processlisthelper.conf
%{_kf5_libdir}/libexec/
%{_kf5_sharedir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
%{_kf5_sharedir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy

%files imports
%license COPYING*
%dir %{_kf5_qmldir}/org/kde/ksysguard
%dir %{_kf5_qmldir}/org/kde/ksysguard/faces
%dir %{_kf5_qmldir}/org/kde/ksysguard/formatter
%dir %{_kf5_qmldir}/org/kde/ksysguard/process
%dir %{_kf5_qmldir}/org/kde/ksysguard/sensors
%{_kf5_qmldir}/org/kde/ksysguard/faces/ExtendedLegend.qml
%{_kf5_qmldir}/org/kde/ksysguard/faces/SensorFace.qml
%{_kf5_qmldir}/org/kde/ksysguard/faces/libFacesPlugin.so
%{_kf5_qmldir}/org/kde/ksysguard/faces/qmldir
%{_kf5_qmldir}/org/kde/ksysguard/formatter/libFormatterPlugin.so
%{_kf5_qmldir}/org/kde/ksysguard/formatter/qmldir
%{_kf5_qmldir}/org/kde/ksysguard/process/libProcessPlugin.so
%{_kf5_qmldir}/org/kde/ksysguard/process/qmldir
%{_kf5_qmldir}/org/kde/ksysguard/sensors/libSensorsPlugin.so
%{_kf5_qmldir}/org/kde/ksysguard/sensors/qmldir

%files devel
%license COPYING*
%{_includedir}/ksysguard/
%{_kf5_libdir}/cmake/KF5SysGuard/
%{_kf5_libdir}/cmake/KSysGuard/
%dir %{_kf5_plugindir}/designer/
%{_kf5_plugindir}/designer/ksignalplotter5widgets.so
%{_kf5_plugindir}/designer/ksysguard5widgets.so
%{_kf5_plugindir}/designer/ksysguardlsof5widgets.so
%{_kf5_libdir}/libKSysGuardFormatter.so
%{_kf5_libdir}/libKSysGuardSensorFaces.so
%{_kf5_libdir}/libKSysGuardSensors.so
%{_kf5_libdir}/libksgrd.so
%{_kf5_libdir}/libksignalplotter.so
%{_kf5_libdir}/liblsofui.so
%{_kf5_libdir}/libprocesscore.so
%{_kf5_libdir}/libprocessui.so

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
