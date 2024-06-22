#
# spec file for package kglobalacceld6
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

%define rname kglobalacceld
%bcond_without released
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Name:           kglobalacceld6
Version:        6.1.0
Release:        0
Summary:        Global keyboard shortcut daemon
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
%if 0%{?suse_version} == 1500
# Due to leap being leap, rpmlint rules are obsolete
Source99:       kglobalacceld6-rpmlintrc
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-xkb)
Provides:       kglobalaccel5 = %{version}
Obsoletes:      kglobalaccel5 < %{version}

%description
Daemon providing Global Keyboard Shortcut (Accelerator) functionality.

%package -n libKGlobalAccelD6-0
Summary:        KGlobalAccelD library
Recommends:     kglobalacceld6

%description -n libKGlobalAccelD6-0
KGlobalAcceld is a daemon providing Global Keyboard Shortcut (Accelerator)
functionality.
This package provides the kglobalacceld library.

%package devel
Summary:        Global keyboard shortcut daemon: Build Environment
Requires:       libKGlobalAccelD6-0 >= %{_plasma6_bugfix}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description devel
Daemon providing Global Keyboard Shortcut (Accelerator) functionality.
Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%post
%{systemd_user_post plasma-kglobalaccel.service}

%preun
%{systemd_user_preun plasma-kglobalaccel.service}

%postun
# TODO? Drop? systemd_user_postun is a stub in TW
%{systemd_user_postun plasma-kglobalaccel.service}

%ldconfig_scriptlets -n libKGlobalAccelD6-0

%files
%{_kf6_configdir}/autostart/kglobalacceld.desktop
%dir %{_kf6_plugindir}/org.kde.kglobalacceld.platforms
%{_kf6_plugindir}/org.kde.kglobalacceld.platforms/KGlobalAccelDXcb.so
%{_libexecdir}/kglobalacceld
%{_userunitdir}/plasma-kglobalaccel.service

%files -n libKGlobalAccelD6-0
%license LICENSES/*
%{_kf6_libdir}/libKGlobalAccelD.so.*

%files devel
%{_kf6_cmakedir}/KGlobalAccelD/
%{_includedir}/KGlobalAccelD/

%changelog
