#
# spec file for package dwayland
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

%define  sover  5

Name:           dwayland
Version:        5.24.3
Release:        0
Summary:        Deepin Wayland library
License:        LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxdeepin/dwayland
Source0:        https://github.com/linuxdeepin/dwayland/archive/refs/tags/%{version}-deepin.1.4.tar.gz
BuildRequires:  wayland-devel
BuildRequires:  libqt5-qtwayland
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  cmake(DeepinWaylandProtocols) 
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(wayland-protocols)

%description
DWayland is a Qt-style API to interact with the wayland-client and
wayland-server API.

%package -n libDWaylandClient%{sover}
Summary:        DWayland Client Library
Group:          System/Libraries

%description -n libDWaylandClient%{sover}
DWayland is a Qt-style API to interact with the wayland-client API.

%package -n libDWaylandServer%{sover}
Summary:        DWayland Client Library
Group:          System/Libraries

%description -n libDWaylandServer%{sover}
DWayland is a Qt-style API to interact with the wayland-server API.

%package devel
Summary:        Development tools for dwayland
Group:          Development/Languages/C and C++
Requires:       libDWaylandClient%{sover} = %{version}
Requires:       libDWaylandServer%{sover} = %{version}

%description devel
The dwayland-devel package contains the header files and developer docs for
dwayland.

%prep
%autosetup -p1 -n %{name}-%{version}-deepin.1.4

%build
%cmake_kf5 -d build
%cmake_build

%install
%cmake_install

%post -n libDWaylandClient%{sover} -p /sbin/ldconfig
%postun -n libDWaylandClient%{sover} -p /sbin/ldconfig

%post -n libDWaylandServer%{sover} -p /sbin/ldconfig
%postun -n libDWaylandServer%{sover} -p /sbin/ldconfig

%files -n libDWaylandClient%{sover}
%{_libdir}/libDWaylandClient.so.*

%files -n libDWaylandServer%{sover}
%{_libdir}/libDWaylandServer.so.*

%files devel
%doc DESIGN.md README.md
%license debian/copyright
%{_libdir}/libDWaylandClient.so
%{_libdir}/libDWaylandServer.so
%{_libdir}/cmake/DWayland
%{_libdir}/qt5/mkspecs/modules/qt_DWaylandClient.pri
%{_includedir}/DWayland
%{_includedir}/dwayland_version.h
%{_datadir}/qlogging-categories5/dwayland.*

%changelog

