#
# spec file for package kscreenlocker6
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

%define rname kscreenlocker
%bcond_without released
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Name:           kscreenlocker6
Version:        6.1.1
Release:        0
Summary:        Library and components for secure lock screen architecture
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
Source3:        kde
Source4:        kde-fingerprint
Source5:        kde-smartcard
BuildRequires:  cmake >= 3.16
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Screen) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KWayland) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LayerShellQt) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaQuick) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
Requires:       pam-config
Provides:       kscreenlocker = %{version}
Provides:       qt6qmlimport(org.kde.kscreenlocker.1) = 0
Obsoletes:      kscreenlocker < %{version}
Obsoletes:      kscreenlocker-lang < %{version}

%description
Library and components for secure lock screen architecture.

%package -n libKScreenLocker6
Summary:        Library and components for secure lock screen architecture

%description -n libKScreenLocker6
Library and components for secure lock screen architecture.

%package devel
Summary:        Library and components for secure lock screen architecture - development files
Requires:       libKScreenLocker6 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Conflicts:      kscreenlocker-devel

%description devel
Development files for Library and components for secure lock screen architecture.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

# Ship our own files to not depend on a display manager being installed (boo#1108329)
install -D -m0644 %{SOURCE3} %{buildroot}%{_pam_vendordir}/kde
install -D -m0644 %{SOURCE4} %{buildroot}%{_pam_vendordir}/kde-fingerprint
install -D -m0644 %{SOURCE5} %{buildroot}%{_pam_vendordir}/kde-smartcard

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKScreenLocker6

%files
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_screenlocker.desktop
%{_kf6_debugdir}/kscreenlocker.categories
%{_kf6_notificationsdir}/ksmserver.notifyrc
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_screenlocker.so
%{_kf6_sharedir}/ksmserver/
%{_libexecdir}/kscreenlocker_greet
%{_pam_vendordir}/kde
%{_pam_vendordir}/kde-fingerprint
%{_pam_vendordir}/kde-smartcard

%files -n libKScreenLocker6
%{_kf6_libdir}/libKScreenLocker.so.*

%files devel
%{_includedir}/KScreenLocker/
%{_kf6_cmakedir}/KScreenLocker/
%{_kf6_cmakedir}/ScreenSaverDBusInterface/
%{_kf6_libdir}/libKScreenLocker.so
%{_kf6_sharedir}/dbus-1/interfaces/kf6_org.freedesktop.ScreenSaver.xml
%{_kf6_sharedir}/dbus-1/interfaces/org.kde.screensaver.xml

%files lang -f %{name}.lang

%changelog
