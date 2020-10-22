#
# spec file for package kwayland-server
#
# Copyright (c) 2020 SUSE LLC
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


# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
%define lname libKWaylandServer5

%bcond_without lang
Name:           kwayland-server
Version:        5.20.1
Release:        0
Summary:        KDE Wayland server library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
URL:            https://www.kde.org
Source:         kwayland-server-%{version}.tar.xz
%if %{with lang}
Source1:        kwayland-server-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 3.5
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Wayland) >= 5.70.0
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.0
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Gui) >= 5.15.0
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client) >= 1.15.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.18
BuildRequires:  pkgconfig(wayland-server) >= 1.15.0

# For kwayland-testQtSurfaceExtension
BuildRequires:  Mesa-dri

%description
kwayland-server provides a Qt-style server library wrapper for the Wayland libraries.

%package -n %lname
Summary:        KDE Wayland server library
Group:          Development/Libraries/KDE

%description -n %lname
kwayland-server provides a Qt-style server library wrapper for the Wayland libraries.

%package devel
Summary:        KDE Wayland library: Build Environment
Group:          Development/Libraries/KDE
Requires:       %lname = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Gui) >= 5.15.0

%description devel
kwayland-server provides a Qt-style server library wrapper for the Wayland libraries.

%prep
%setup -q
# Needs private API. Not used here, just skip it.
echo > tests/CMakeLists.txt

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%check
export XDG_RUNTIME_DIR=$(mktemp -d)
export CTEST_OUTPUT_ON_FAILURE=1
export QT_QPA_PLATFORM=offscreen
# For some reasons some tests fail randomly with wayland protocol errors
make %{?_smp_mflags} -C build VERBOSE=1 test || :
rm -r $XDG_RUNTIME_DIR

%install
%kf5_makeinstall -C build

%post -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING* LICENSES/*.txt
%{_kf5_debugdir}/kwaylandserver.categories
%{_kf5_libdir}/libKWaylandServer.so.5
%{_kf5_libdir}/libKWaylandServer.so.%{_plasma5_bugfix}

%files devel
%license COPYING* LICENSES/*.txt
%{_kf5_libdir}/libKWaylandServer.so
%{_kf5_libdir}/cmake/KWaylandServer/
%{_includedir}/KWaylandServer/
%{_includedir}/kwaylandserver_version.h

%changelog
