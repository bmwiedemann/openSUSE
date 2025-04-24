#
# spec file for package glew
#
# Copyright (c) 2025 SUSE LLC
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
%global pname glew
# If you change so_ver, then you have to update baselibs.conf as well.
%define so_ver 2_2

%if "%{flavor}" == ""
%bcond_with egl
%endif

%if "%{flavor}" == "egl"
%bcond_without egl
%define pkg_suffix _EGL
%endif

%define shlib libGLEW%{?pkg_suffix}%{so_ver}

Name:           %{pname}%{?pkg_suffix}
Version:        2.2.0
Release:        0
Summary:        OpenGL Extension Wrangler Library
# was http://glew.sourceforge.net/
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/nigels-com/glew
Source0:        https://downloads.sourceforge.net/%{pname}/%{pname}-%{version}.tgz
Source1:        baselibs.conf
Patch0:         glew-2.2.0-mesa-24.patch
# PATCH-FIX-UPSTREAM See (cherry picked from) line in the patch file from
# https://github.com/nigels-com/glew/commits/master/
Patch1:         glew-2.2.0-fix-cmake.patch
# PATCH-FEATURE-OPENSUSE glew-rename-EGL-library.patch badshah400@gmail.com -- Append suffix to shared library built with EGL support to allow parallel installation with the GLX compatible flavor
Patch2:         glew-rename-EGL-library.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gl)
%if %{with egl}
BuildRequires:  pkgconfig(egl)
Conflicts:      %{pname}
%else
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcb)
%endif

%description
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform
open-source C/C++ extension loading library. GLEW provides efficient
run-time mechanisms for determining which OpenGL extensions are
supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file.

%package -n %{shlib}
Summary:        OpenGL Extension Wrangler Library
Group:          System/Libraries

%description -n %{shlib}
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform
open-source C/C++ extension loading library. GLEW provides efficient
run-time mechanisms for determining which OpenGL extensions are
supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file.

%package devel
Summary:        Development files for glew
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}
Requires:       pkgconfig(glu)
%if %{with egl}
Requires:       pkgconfig(egl)
Conflicts:      %{pname}-devel
%else
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xau)
Requires:       pkgconfig(xcb)
%endif

%description devel
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform
open-source C/C++ extension loading library. GLEW provides efficient
run-time mechanisms for determining which OpenGL extensions are
supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file.

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
# Allow apps requesting both GLX and EGL symbols to get both shlibs
echo 'G_%flavor { global: *; };' > x.sym
%define build_ldflags -Wl,--version-script=`readlink -f ../x.sym`

%define __sourcedir build/cmake
%cmake \
    -DGLEW_EGL=%{?with_egl:ON}%{!?with_egl:OFF} \
    -DBUILD_UTILS=ON \
    %{nil}

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %{shlib}

%files
%license LICENSE.txt
%doc doc/*
%{_bindir}/glewinfo
%{_bindir}/visualinfo

%files -n %{shlib}
%{_libdir}/libGLEW*.so.*

%files devel
%{_includedir}/GL/
%{_libdir}/libGLEW*.so
%{_libdir}/pkgconfig/glew.pc
%{_libdir}/cmake/glew/

%changelog
