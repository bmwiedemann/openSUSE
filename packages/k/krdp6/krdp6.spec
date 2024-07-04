#
# spec file for package krdp6
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Fabian Vogt
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

%define rname krdp
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           krdp6
Version:        6.1.2
Release:        0
Summary:        RDP Server for Plasma
License:        LGPL-2.1-or-later
URL:            https://invent.kde.org/plasma/krdp
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  qt6-gui-private-devel
BuildRequires:  cmake(FreeRDP) >= 2.10
BuildRequires:  cmake(FreeRDP-Server)
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KPipeWire) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(WinPR)

%description
RDP Server with settings Module for Plasma.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_EXAMPLES=OFF
%kf6_build

%install
%kf6_install

# No external users (yet?)
rm %{buildroot}%{_kf6_libdir}/libKRdp.so
rm -r %{buildroot}%{_kf6_cmakedir}

%find_lang kcm_krdpserver --all-name

%pre
# No systemd_user_ in *un, broken by design (boo#1221405)
%{systemd_user_pre plasma-krdp_server.service}

%post
%ldconfig
%{systemd_user_post plasma-krdp_server.service}

%postun
%ldconfig

%files
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/krdpserver
%{_kf6_libdir}/libKRdp.so.6
%{_kf6_libdir}/libKRdp.so.*
%{_kf6_applicationsdir}/kcm_krdpserver.desktop
%{_kf6_applicationsdir}/org.kde.krdp.desktop
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_krdpserver.so
%{_kf6_debugdir}/kcm_krdpserver.categories
%{_kf6_debugdir}/krdp.categories
%{_userunitdir}/plasma-krdp_server.service

%files lang -f kcm_krdpserver.lang

%changelog
