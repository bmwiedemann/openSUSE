#
# spec file for package kidletime
#
# Copyright (c) 2023 SUSE LLC
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


%define lname   libKF5IdleTime5
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           kidletime
Version:        5.116.0
Release:        0
Summary:        User and system idle time reporting singleton
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  libQt5Gui-private-headers-devel >= %{qt5_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5WaylandClient) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5X11Extras) >= %{qt5_version}
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)

%description
KIdleTime is a singleton reporting information on idle time. It is useful not
only for finding out about the current idle time of the PC, but also for getting
notified upon idle time events, such as custom timeouts, or user activity.

%package -n %{lname}
Summary:        User and system idle time reporting singleton
%requires_ge    libQt5Core5
%requires_ge    libQt5Widgets5
%requires_ge    libQt5X11Extras5

%description -n %{lname}
KIdleTime is a singleton reporting information on idle time. It is useful not
only for finding out about the current idle time of the PC, but also for getting
notified upon idle time events, such as custom timeouts, or user activity.

%package devel
Summary:        Build environment for kidletime, an idle time singleton
Requires:       %{lname} = %{version}
Requires:       cmake(Qt5Core) >= %{qt5_version}

%description devel
Development files for KIdleTime, which is a singleton reporting
information on idle time. It is useful not only for finding out about
the current idle time of the PC, but also for getting notified upon
idle time events, such as custom timeouts, or user activity.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}
%license LICENSES/*
%doc README*
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/org.kde.kidletime.platforms
%{_kf5_debugdir}/kidletime.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5IdleTime.so.*
%{_kf5_plugindir}/kf5/org.kde.kidletime.platforms/KF5IdleTimeWaylandPlugin.so
%{_kf5_plugindir}/kf5/org.kde.kidletime.platforms/KF5IdleTimeXcbPlugin0.so
%{_kf5_plugindir}/kf5/org.kde.kidletime.platforms/KF5IdleTimeXcbPlugin1.so

%files devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5IdleTime/
%{_kf5_libdir}/libKF5IdleTime.so
%{_kf5_mkspecsdir}/qt_KIdleTime.pri

%changelog
