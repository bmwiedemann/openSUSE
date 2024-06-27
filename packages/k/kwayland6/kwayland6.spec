#
# spec file for package kwayland6
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname kwayland
%bcond_without released
Name:           kwayland6
Version:        6.1.1
Release:        0
Summary:        KDE Wayland library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  qt6-waylandclient-private-devel >= %{qt6_version}
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.9.0
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client) >= 1.15.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.15.0
BuildRequires:  pkgconfig(wayland-server) >= 1.15.0

%description
KWayland provides a Qt-style Client and Server library wrapper for the Wayland
libraries.

%package -n libKWaylandClient6
Summary:        KDE Wayland library
Requires:       kwayland6 >= %{version}

%description -n libKWaylandClient6
KWayland provides a Qt-style Client and Server library wrapper for the Wayland
libraries.

%package devel
Summary:        KDE Wayland library: Build Environment
Requires:       libKWaylandClient6 = %{version}

%description devel
KWayland provides a Qt-style Client and Server library wrapper for the Wayland
libraries.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets -n libKWaylandClient6

%files
%{_kf6_debugdir}/kwayland.categories
%{_kf6_debugdir}/kwayland.renamecategories

%files -n libKWaylandClient6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKWaylandClient.so.*

%files devel
%doc %{_kf6_qchdir}/KWayland.*
%{_includedir}/KWayland/
%{_kf6_cmakedir}/KWayland/
%{_kf6_libdir}/libKWaylandClient.so
%{_kf6_pkgconfigdir}/KWaylandClient.pc

%changelog
