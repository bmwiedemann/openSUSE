#
# spec file for package kscreen6
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


%global __requires_exclude qt6qmlimport\\(org\\.kde\\.private\\.kscreen.*

%global kf6_version 6.0.0
%define qt6_version 6.6.0

%define rname kscreen
%bcond_without released
Name:           kscreen6
Version:        6.1.1
Release:        0
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Screen management software by KDE
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6Screen) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(LayerShellQt) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaQuick) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Sensors) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xi)
Requires:       kf6-kded
Requires:       libkscreen6-plugin >= %{_plasma6_bugfix}
Requires:       xrdb
Supplements:    (libkscreen6-plugin and plasma6-workspace)
Obsoletes:      kscreen5 < %{version}
Obsoletes:      kscreen5-lang < %{version}
Obsoletes:      kscreen5-plasmoid < %{version}
Provides:       kscreen6-plasmoid < %{version}
Obsoletes:      kscreen6-plasmoid < %{version}

%description
KScreen handles screen management for both X11 and Wayland sessions, including rotation, size, refresh rate, and scaling.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%post
%{systemd_user_post plasma-kscreen-osd.service}

%preun
%{systemd_user_preun plasma-kscreen-osd.service}

%postun
%{systemd_user_postun plasma-kscreen-osd.service}

%files
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_kscreen.desktop
%{_kf6_appstreamdir}/org.kde.kscreen.appdata.xml
%{_kf6_bindir}/kscreen-console
%{_kf6_debugdir}/kscreen.categories
%{_kf6_plasmadir}/plasmoids/org.kde.kscreen/
%{_kf6_plugindir}/kf6/kded/kscreen.so
%{_kf6_plugindir}/plasma/applets/org.kde.kscreen.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_kscreen.so
%{_kf6_sharedir}/dbus-1/services/org.kde.kscreen.osdService.service
%{_kf6_sharedir}/kglobalaccel/org.kde.kscreen.desktop
%{_libexecdir}/kscreen_osd_service
%{_userunitdir}/plasma-kscreen-osd.service

%files lang -f kscreen6.lang

%changelog
