#
# spec file for package xwaylandvideobridge
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


%global flavor @BUILD_FLAVOR@%{nil}

%if 0%{?suse_version} > 1500 || "%{_repository}" == "KDE_Applications_openSUSE_Leap_15.5" || "%{_repository}" == "KDE_Applications_openSUSE_Leap_15.6"
%define kf6 1
%define _version 6
%define kf_version 5.240.0
%define qt_version 6.4.0
%else
%define kf6 0
%define _version 5
%define kf_version 5.83.0
%define qt_version 5.15.0
%endif

Name:           xwaylandvideobridge
Version:        0.4.0+git12
Release:        0
Summary:        XWayland Video Bridge
License:        GPL-2.0-only OR GPL-3.0-or-later
URL:            https://www.kde.org
# No release yet, missing kdereview
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM:
Patch0:         0001-Remove-duplicate-StartupNotify-entry.patch
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF%{_version}CoreAddons) >= %{kf_version}
BuildRequires:  cmake(KF%{_version}I18n) >= %{kf_version}
BuildRequires:  cmake(KF%{_version}Notifications) >= %{kf_version}
BuildRequires:  cmake(KF%{_version}WindowSystem) >= %{kf_version}
BuildRequires:  cmake(Qt%{_version}DBus) >= %{qt_version}
BuildRequires:  cmake(Qt%{_version}Quick) >= %{qt_version}
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-xfixes)
%if %{kf6}
BuildRequires:  kf6-extra-cmake-modules >= %{kf_version}
BuildRequires:  qt6-gui-private-devel >= %{qt_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf_version}
BuildRequires:  cmake(KPipeWire) >= 6.0.0
%else
# Still useful for some repos in the devel project
BuildRequires:  extra-cmake-modules >= %{kf_version}
# Needs C++20
BuildRequires:  gcc13-PIE
BuildRequires:  gcc13-c++
BuildRequires:  cmake(Qt5X11Extras) >= %{qt_version}
BuildRequires:  (cmake(KPipeWire) >= 5.27 with cmake(KPipeWire) < 6)
%endif

%description
By design, X11 applications can't access window or screen contents for wayland clients.
This is fine in principle, but it breaks screen sharing in tools like Discord, MS Teams, Skype, etc and more.
This tool allows us to share specific windows to X11 clients, but within the control of the user at all times.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%if !%{kf6}
export CC=gcc-13
export CXX=g++-13
%endif

%if %{kf6}
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE
%kf6_build
%else
%cmake_kf5 -d build
%cmake_build
%endif

%install
%if %{kf6}
%kf6_install
%else
%kf5_makeinstall -C build
%endif

%find_lang %{name} --all-name

%files -f %{name}.lang
%license LICENSES/*
%if %{kf6}
%{_kf6_applicationsdir}/org.kde.xwaylandvideobridge.desktop
%{_kf6_appstreamdir}/org.kde.xwaylandvideobridge.appdata.xml
%{_kf6_bindir}/xwaylandvideobridge
%{_kf6_configdir}/autostart/org.kde.xwaylandvideobridge.desktop
%{_kf6_debugdir}/xwaylandvideobridge.categories
%{_kf6_iconsdir}/hicolor/scalable/apps/xwaylandvideobridge.svg
%else
%{_kf5_applicationsdir}/org.kde.xwaylandvideobridge.desktop
%{_kf5_appstreamdir}/org.kde.xwaylandvideobridge.appdata.xml
%{_kf5_bindir}/xwaylandvideobridge
%{_kf5_configdir}/autostart/org.kde.xwaylandvideobridge.desktop
%{_kf5_debugdir}/xwaylandvideobridge.categories
%{_kf5_iconsdir}/hicolor/scalable/apps/xwaylandvideobridge.svg
%endif

%changelog
