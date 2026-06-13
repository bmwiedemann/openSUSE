#
# spec file for package xwaylandvideobridge
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define kf6_version 5.240.0
%define qt6_version 6.4.0

%bcond_without released
Name:           xwaylandvideobridge
Version:        0.5.0
Release:        0
Summary:        XWayland Video Bridge
License:        GPL-2.0-only OR GPL-3.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/xwaylandvideobridge/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/xwaylandvideobridge/src/%{name}-%{version}.tar.xz.sig
# https://invent.kde.org/sysadmin/release-keyring/-/blob/master/keys/silverhadch@key1.asc?ref_type=heads
Source2:        xwaylandvideobridge.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KPipeWire) >= 6.0.0
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-xfixes)

%description
By design, X11 applications can't access window or screen contents for wayland clients.
This is fine in principle, but it breaks screen sharing in tools like Discord, MS Teams, Skype, etc and more.
This tool allows us to share specific windows to X11 clients, but within the control of the user at all times.

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.xwaylandvideobridge.desktop
%{_kf6_appstreamdir}/org.kde.xwaylandvideobridge.appdata.xml
%{_kf6_bindir}/xwaylandvideobridge
%{_kf6_configdir}/autostart/org.kde.xwaylandvideobridge.desktop
%{_kf6_debugdir}/xwaylandvideobridge.categories
%{_kf6_iconsdir}/hicolor/scalable/apps/xwaylandvideobridge.svg

%changelog
