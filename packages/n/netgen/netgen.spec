#
# spec file for package netgen
#
# Copyright (c) 2021 SUSE LLC
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


%bcond_with need_clang
%bcond_with openmpi
%bcond_without ffmpeg
%bcond_without opencascade
# pytest-check is not available
%bcond_with pytest

Name:           netgen
Version:        6.2.2101
Release:        0
Summary:        Automatic 3D tetrahedral mesh generator
License:        LGPL-2.1-only
Group:          Productivity/Graphics/CAD
URL:            https://ngsolve.org/
Source0:        netgen-%{version}.tar.xz
# PATCH-FIX-OPENSUSE
Patch0:         0001-Set-explicit-OBJECT-library-type-for-internal-togl.patch
# PATCH-FIX-OPENSUSE
Patch1:         0001-Disable-backtrace-generation.patch
# PATCH-FIX-OPENSUSE
Patch2:         0001-Throw-in-case-enum-value-is-unhandled.patch
# PATCH-FIX-OPENSUSE
Patch3:         0001-Fix-GetTimeCounter-for-Aarch64-variants.patch
# PATCH-FIX-OPENSUSE -- Allow to disable download of Catch2
Patch4:         0001-Optionally-use-system-provided-Catch2.patch
%if %{with opencascade}
BuildRequires:  occt-devel
%endif
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  libjpeg-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pybind11-devel
%if %{with pytest}
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-check
%endif
BuildRequires:  pkgconfig(catch2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(tcl)
BuildRequires:  pkgconfig(tk)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(zlib)
%if %{with openmpi}
BuildRequires:  metis-devel
BuildRequires:  openmpi-devel
%endif
%if %{with ffmpeg}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
%endif
%if %{with need_clang}
BuildRequires:  llvm
BuildRequires:  llvm-clang
%else
BuildRequires:  gcc-c++ >= 7
%endif
BuildRequires:  xz
# x86 (32bit) is no longer supported upstream. Also exclude other 32 bit archs
ExcludeArch:    %{ix86} %{arm} ppc
Recommends:     %{name}-examples

%description
NETGEN is an automatic 3D tetrahedral mesh generator. It accepts
input from constructive solid geometry (CSG) or boundary
representation (BRep) from STL file format. The connection to a
geometry kernel allows the handling of IGES and STEP files. NETGEN
contains modules for mesh optimization and hierarchical mesh
refinement.

%package -n netgen-libs
Summary:        NETGEN mesher libraries
Group:          System/Libraries
Conflicts:      %{name} < %{version}
Provides:       %{name}:%{_libdir}/netgen/libngcore.so

%description -n netgen-libs
NETGEN mesh generator shared libraries.

%package devel
Summary:        Development files for netgen
# Should not depend on the netgen binary, but the cmake config is broken
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       netgen-libs = %{version}
%if %{with opencascade}
Requires:       occt-devel
%endif

%description devel
Development files for NETGEN.

%package examples
Summary:        NETGEN examples
Group:          Productivity/Graphics/CAD
Requires:       %{name} = %{version}
Conflicts:      %{name} < %{version}
Provides:       %{name}:%{_datadir}/netgen/cube.geo
BuildArch:      noarch

%description examples
Various example geometry data for NETGEN.

%package -n python3-%{name}
Summary:        NETGEN python bindings
Group:          Productivity/Graphics/CAD
Conflicts:      %{name} < %{version}
Provides:       %{name}:%{python3_sitearch}/netgen/libngpy.so

%description  -n python3-%{name}
Python bindings for NETGEN.


%prep
%autosetup -p1

%build
%if %{with need_clang}
    OPTFLAGS="$(echo %{optflags} | sed "s:-grecord-gcc-switches::g") -flto"
%else
    OPTFLAGS="%{optflags}"
%endif

# Work around broken version detection
echo "v%{version}-0-0" > ./version.txt

# Do not error out on undefined symbols - there is a circular dependency
# between libvisual and libmesh ...
%cmake \
    -DUSE_SUPERBUILD=OFF \
    -DCMAKE_SHARED_LINKER_FLAGS="-flto=auto -Wl,--as-needed -Wl,--warn-unresolved-symbols -Wl,-z,now" \
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
    -DENABLE_UNIT_TESTS=ON \
    -DDOWNLOAD_DEPENDENCIES=OFF \
    -DUSE_NATIVE_ARCH=OFF \
    -DUSE_GUI=ON \
    -DUSE_PYTHON=ON \
    -DNG_INSTALL_DIR_PYTHON=%{python3_sitearch} \
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

%cmake_build

%install
%cmake_install
rm -Rf %{buildroot}%{_datadir}/%{name}/doc

%fdupes %{buildroot}/%{_prefix}

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}/%{name}
%ctest %{!?with_pytest: --exclude-regex pytest}

%files
%license LICENSE
%doc doc/*.pdf
%{_bindir}/*

%files examples
%{_datadir}/netgen

%files -n netgen-libs
%{_libdir}/netgen

%files -n python3-%{name}
%{python3_sitearch}/netgen
%{python3_sitearch}/pyngcore*.so

%files devel
%dir %{_prefix}/lib/cmake
%{_includedir}/netgen
%{_prefix}/lib/cmake/netgen

%changelog
