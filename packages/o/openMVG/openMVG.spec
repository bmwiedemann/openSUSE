#
# spec file for package openMVG
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2018-2019 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


%define major   1
%define minor   6
%define libname libopenMVG%{major}
Name:           openMVG
Version:        %{major}.%{minor}
Release:        0
Summary:        Library for Multiple-View-Geometry and Structure-From-Motion
License:        MPL-2.0
URL:            https://github.com/openMVG/openMVG
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM Enable_NEW_mode_of_CMP0100.patch andythe_great@pm.me -- Fix cmake do not run automoc on .hh files, generating linker errors for the ui tools.
# https://github.com/openMVG/openMVG/pull/1760
Patch0:         Enable_NEW_mode_of_CMP0100.patch
# PATCH-FIX-OPENSUSE use_gnuinstalldirs.patch andythe_great@pm.me gh#openMVG/openMVG#1852 -- Fix some files went into lib instead of lib64.
Patch1:         use_gnuinstalldirs.patch
BuildRequires:  blas-devel
BuildRequires:  cereal-devel
BuildRequires:  clang
BuildRequires:  flann-devel
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  git
BuildRequires:  glpk-devel
BuildRequires:  graphviz
BuildRequires:  lapack-devel
BuildRequires:  pkgconfig
BuildRequires:  wget
BuildRequires:  pkgconfig(Coin)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xxf86vm)
Recommends:     graphviz
Recommends:     openMVS

%description
Library for computer-vision scientists and especially targeted to the Multiple
View Geometry community. It is designed to provide an easy access to the
classical problem solvers in Multiple View Geometry and solve them accurately.

%package -n %{libname}
Summary:        Multiple View Geometry library

%description -n %{libname}
Library for computer-vision scientists and especially targeted to the Multiple
View Geometry community. It is designed to provide an easy access to the
classical problem solvers in Multiple View Geometry and solve them accurately.

%package devel
Summary:        Files for developing with Multiple View Geometry library
Requires:       %{name} = %{version}-%{release}

%description devel
Header files and definitions for developing with %{name}.

%prep
%autosetup -p1

%build
%cmake -DTARGET_ARCHITECTURE=generic \
       -DOpenMVG_BUILD_DOC:BOOL=OFF \
       -DOpenMVG_BUILD_EXAMPLES:BOOL=ON \
       -DOpenMVG_BUILD_SOFTWARES:BOOL=ON \
       -DOpenMVG_BUILD_GUI_SOFTWARES:BOOL=ON \
       -DOpenMVG_BUILD_SHARED:BOOL=ON \
       -DOpenMVG_BUILD_TESTS:BOOL=ON \
       -DOpenMVG_BUILD_OPENGL_EXAMPLES:BOOL=ON \
       -DOpenMVG_USE_OPENCV:BOOL=OFF \
       -DOpenMVG_USE_OCVSIFT:BOOL=OFF \
       -DFLANN_INCLUDE_DIR_HINTS:PATH=%{_includedir} \
       . ../src/

%cmake_build

%install
%cmake_install

%fdupes %{buildroot}

# Remove static libs
find %{buildroot} -type f -name "*.a" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%check
# Test fail in Leap but not TW when enable build share libs flag, no clue why.
%ctest

%files
%{_bindir}/openMVG_main_*
%{_bindir}/ui_openMVG_*

%files -n %{libname}
%doc AUTHORS CONTRIBUTING.md
%license LICENSE
%{_libdir}/libopenMVG*.so.%{version}

%files devel
%{_datadir}/%{name}
%{_includedir}/%{name}_dependencies
%{_includedir}/%{name}
%{_libdir}/lib%{name}*.so
%{_libdir}/lib%{name}*.so.%{major}
%{_libdir}/%{name}-targets*.cmake

%changelog
