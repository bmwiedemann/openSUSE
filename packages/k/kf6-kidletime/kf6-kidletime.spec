#
# spec file for package kf6-kidletime
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define qt6_version 6.8.0

%define rname kidletime
# Full KF6 version (e.g. 6.21.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-kidletime
Version:        6.21.0
Release:        0
Summary:        User and system idle time reporting singleton
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  pkgconfig(wayland-protocols) >= 1.27
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)

%description
KIdleTime is a singleton reporting information on idle time. It is useful not
only for finding out about the current idle time of the PC, but also for getting
notified upon idle time events, such as custom timeouts, or user activity.

%package plugins
Summary:        User and system idle time reporting singleton

%description plugins
KIdleTime is a singleton reporting information on idle time. It is useful not
only for finding out about the current idle time of the PC, but also for getting
notified upon idle time events, such as custom timeouts, or user activity.

%package -n libKF6IdleTime6
Summary:        User and system idle time reporting singleton
Requires:       kf6-kidletime >= %{version}
Recommends:     kf6-kidletime-plugins = %{version}

%description -n libKF6IdleTime6
KIdleTime is a singleton reporting information on idle time. It is useful not
only for finding out about the current idle time of the PC, but also for getting
notified upon idle time events, such as custom timeouts, or user activity.

%package devel
Summary:        Build environment for kidletime, an idle time singleton
Requires:       libKF6IdleTime6 = %{version}

%description devel
Development files for KIdleTime, which is a singleton reporting
information on idle time. It is useful not only for finding out about
the current idle time of the PC, but also for getting notified upon
idle time events, such as custom timeouts, or user activity.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%ldconfig_scriptlets -n libKF6IdleTime6

%files
%{_kf6_debugdir}/kidletime.categories
%{_kf6_debugdir}/kidletime.renamecategories

%files plugins
%dir %{_kf6_plugindir}/kf6/org.kde.kidletime.platforms
%{_kf6_plugindir}/kf6/org.kde.kidletime.platforms/KF6IdleTimeWaylandPlugin.so
%{_kf6_plugindir}/kf6/org.kde.kidletime.platforms/KF6IdleTimeXcbPlugin0.so
%{_kf6_plugindir}/kf6/org.kde.kidletime.platforms/KF6IdleTimeXcbPlugin1.so

%files -n libKF6IdleTime6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6IdleTime.so.*

%files devel
%{_kf6_includedir}/KIdleTime/
%{_kf6_cmakedir}/KF6IdleTime/
%{_kf6_libdir}/libKF6IdleTime.so

%changelog
