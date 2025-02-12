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


%bcond egl 0

# If you change so_ver, then you have to update baselibs.conf as well.
%define so_ver 2_2
Name:           glew
Version:        2.2.0
Release:        0
Summary:        OpenGL Extension Wrangler Library
# was http://glew.sourceforge.net/
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/nigels-com/glew
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
Source1:        baselibs.conf
Source2:        %{name}.rpmlintrc
Patch0:         glew-2.2.0-mesa-24.patch
# PATCH-FIX-UPSTREAM See (cherry picked from) line in the patch file from
# https://github.com/nigels-com/glew/commits/master/
Patch1:         glew-2.2.0-fix-cmake.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig
%if %{with egl}
BuildRequires:  pkgconfig(egl)
%endif
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)

%description
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform
open-source C/C++ extension loading library. GLEW provides efficient
run-time mechanisms for determining which OpenGL extensions are
supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file.

%package -n libGLEW%{so_ver}
Summary:        OpenGL Extension Wrangler Library
Group:          System/Libraries

%description -n libGLEW%{so_ver}
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform
open-source C/C++ extension loading library. GLEW provides efficient
run-time mechanisms for determining which OpenGL extensions are
supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file.

%package devel
Summary:        Development files for glew
Group:          Development/Libraries/C and C++
Requires:       libGLEW%{so_ver} = %{version}
%if %{with egl}
Requires:       pkgconfig(egl)
%endif
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xproto)
# Don't require GLU, because there is GLEW_NO_GLU option
Recommends:     pkgconfig(glu)

%description devel
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform
open-source C/C++ extension loading library. GLEW provides efficient
run-time mechanisms for determining which OpenGL extensions are
supported on the target platform. OpenGL core and extension
functionality is exposed in a single header file.

%prep
%autosetup -p1

%build
%define __sourcedir build/cmake
%cmake \
%if %{with egl}
    -DGLEW_EGL=ON \
%endif
    -DBUILD_UTILS=ON

%cmake_build

%install
%cmake_install

%post -n libGLEW%{so_ver} -p /sbin/ldconfig
%postun -n libGLEW%{so_ver} -p /sbin/ldconfig

%files
%license LICENSE.txt
%doc doc/*
%{_bindir}/glewinfo
%{_bindir}/visualinfo

%files -n libGLEW%{so_ver}
%{_libdir}/libGLEW.so.*

%files devel
%{_includedir}/GL/
%{_libdir}/libGLEW.so
%{_libdir}/pkgconfig/glew.pc
%{_libdir}/cmake/glew/

%changelog
