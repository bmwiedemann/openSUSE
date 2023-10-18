#
# spec file for package xwaylandvideobridge
#
# Copyright (c) 2021 SUSE LLC
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


Name:           xwaylandvideobridge
Version:        0.2+git6
Release:        0
Summary:        XWayland Video Bridge
License:        GPL-2.0-only or GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
# No release yet, missing kdereview
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.83.0
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KPipeWire) >= 5.27.5
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-xfixes)
%if 0%{?suse_version} < 1600
# Needs C++20
BuildRequires:  gcc12-c++
BuildRequires:  gcc12-PIE
%endif

%description
By design, X11 applications can't access window or screen contents for wayland clients.
This is fine in principle, but it breaks screen sharing in tools like Discord, MS Teams, Skype, etc and more.
This tool allows us to share specific windows to X11 clients, but within the control of the user at all times.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600
export CC=gcc-12
export CXX=g++-12
%endif
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_bindir}/xwaylandvideobridge
%{_kf5_applicationsdir}/org.kde.xwaylandvideobridge.desktop
%{_kf5_iconsdir}/hicolor/scalable/apps/xwaylandvideobridge.svg
%{_kf5_debugdir}/xwaylandvideobridge.categories
%{_kf5_appstreamdir}/org.kde.xwaylandvideobridge.appdata.xml

%changelog
