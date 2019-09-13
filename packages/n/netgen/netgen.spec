#
# spec file for package netgen
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%bcond_with need_clang
%bcond_with openmpi
%bcond_without ffmpeg
%bcond_with opencascade

Name:           netgen
Version:        6.2.1810
Release:        0
Summary:        Automatic 3D tetrahedral mesh generator
License:        LGPL-2.1-only
Group:          Productivity/Graphics/CAD
URL:            https://ngsolve.org/
Source0:        netgen-%{version}.tar.xz
Patch0:         fix_build.patch
# PATCH-FIX-OPENSUSE -- do not try to include immintrin.h when SSE is not supported
Patch1:         0001-Allow-compilation-on-archs-beyond-x86.patch
# not supported by upstream
%if %{with opencascade}
BuildRequires:  occt-devel
%endif
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(tcl)
BuildRequires:  pkgconfig(tk)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  libjpeg-devel
BuildRequires:  python3-devel
%if %{with openmpi}
BuildRequires:  openmpi-devel
BuildRequires:  metis-devel
%endif
%if %{with ffmpeg}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat) 
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
%endif
%if %{with need_clang}
BuildRequires:  llvm-clang
BuildRequires:  llvm
%else
%if %{?suse_version} == 1315
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc-c++ >= 7
%endif
%endif
BuildRequires:  xz

%description
NETGEN is an automatic 3D tetrahedral mesh generator. It accepts
input from constructive solid geometry (CSG) or boundary
representation (BRep) from STL file format. The connection to a
geometry kernel allows the handling of IGES and STEP files. NETGEN
contains modules for mesh optimization and hierarchical mesh
refinement.

%package devel
Summary:        Development files for netgen
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
%if %{with opencascade}
Requires:       occt-devel
%endif

%description devel
Development files for NETGEN.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
# fix version, non-number will break FreeCAD macros
sed -i -e 's,"6.2-dev","6.2.0",' libsrc/include/mydefs.hpp

%build
%if %{?suse_version} == 1315
export CC=gcc-7
export CXX=g++-7
%endif
mkdir build
cd build
%if %{with need_clang}
    OPTFLAGS="$(echo %{optflags} | sed "s:-grecord-gcc-switches::g") -flto"
%else
    OPTFLAGS="%{optflags}"
%endif
  CFLAGS="$OPTFLAGS -fno-strict-aliasing" \
  CXXFLAGS="$OPTFLAGS -fno-strict-aliasing" \
  cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DNG_INSTALL_DIR_INCLUDE=%{_includedir}/netgen \
    -DNG_INSTALL_DIR_LIB=%{_libdir}/netgen \
    -DCMAKE_SKIP_BUILD_RPATH=ON \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
%if %{with need_clang}
    -DCMAKE_C_COMPILER=clang \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DCMAKE_AR=%{_bindir}/llvm-ar \
    -DCMAKE_RANLIB=%{_bindir}/llvm-ranlib \
    -DCMAKE_NM=%{_bindir}/llvm-nm \
    -DCMAKE_OBJDUMP=%{_bindir}/llvm-objdump \
%endif
    -DUSE_NATIVE_ARCH=OFF \
    -DUSE_GUI=ON \
    -DUSE_PYTHON=ON \
%if %{with openmpi}
    -DUSE_MPI=ON \
%else
    -DUSE_MPI=OFF \
%endif
    -DUSE_OCC=%{?with_opencascade:ON}%{!?with_opencascade:OFF} \
    -DUSE_JPEG=ON \
%if %{with ffmpeg}
    -DUSE_MPEG=ON \
%else
    -DUSE_MPEG=OFF \
%endif
    ..
  make %{?_smp_mflags}
cd ..

%install
cd build
%make_install
cd ..
%fdupes %{buildroot}/%{_prefix}

%files
%license LICENSE
%{_bindir}/*
%{_datadir}/netgen
%{_libdir}/netgen
%{python3_sitearch}/netgen

%files devel
%dir %{_prefix}/lib/cmake
%{_includedir}/netgen
%{_prefix}/lib/cmake/netgen

