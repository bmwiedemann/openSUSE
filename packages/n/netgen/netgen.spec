#
# spec file for package netgen
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


%bcond_with openmpi
%bcond_without ffmpeg
%bcond_without opencascade
%if 0%{?suse_version} > 1500
%bcond_without pytest
%else
# pytest-check is not available
%bcond_with    pytest
%endif

Name:           netgen
Version:        6.2.2404
Release:        0
Summary:        Automatic 3D tetrahedral mesh generator
License:        LGPL-2.1-only
Group:          Productivity/Graphics/CAD
URL:            https://ngsolve.org/
Source0:        https://github.com/NGSolve/netgen/archive/refs/tags/v%{version}.tar.gz#/netgen-%{version}.tar.gz
# PATCH-FIX-OPENSUSE
Patch1:         0001-Disable-backtrace-generation.patch
# PATCH-FIX-OPENSUSE -- Allow to disable download of Catch2
Patch4:         0001-Optionally-use-system-provided-Catch2.patch
# PATCH-FIX-UPSTREAM
Patch6:         0001-Link-nggui-to-FFMPEG-und-JPEG-libraries-when-needed.patch
# PATCH-FIX-UPSTREAM
Patch7:         0001-Avoid-installation-of-Togl-static-library.patch
# PATCH-FIX-OPENSUSE
Patch9:         0001-Include-filesystem-from-experimental-for-GCC-7.patch
# PATCH-FIX-UPSTREAM
Patch10:        0001-Fix-netgen-executable-and-library-RUNPATHs.patch
# PATCH-FIX-OPENSUSE
Patch11:        0001-Fix-ODR-violation-for-struct-class-Line.patch
# PATCH-FIX-OPENSUSE
Patch12:        0002-Add-missing-includes-for-std-string-std-cerr-fix-nam.patch
# PATCH-FIX-UPSTREAM -- https://github.com/NGSolve/netgen/issues/200
Patch13:        0001-Do-not-EXPORT-python-modules-as-CMake-targets.patch
# PATCH-FIX-UPSTREAM -- https://github.com/NGSolve/netgen/issues/201
Patch14:        0001-Fix-static-initialization-order-for-UserFormatRegist.patch
# PATCH-FIX-UPSTREAM -- https://github.com/NGSolve/netgen/issues/203
Patch15:        0001-Fix-invalid-string-access-in-BoundaryLayerTool.patch
%if %{with opencascade}
BuildRequires:  occt-devel
BuildRequires:  (pkgconfig(catch2) >= 2.13.4 with pkgconfig(catch2) < 3)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(xi)
%endif
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 7
BuildRequires:  git-core
BuildRequires:  libjpeg-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pybind11-devel >= 2.7.0
BuildRequires:  python3-pybind11-stubgen
%if %{with pytest}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-check
%endif
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

%package -n netgen-gui-libs
Summary:        NETGEN mesher library - GUI part
Group:          System/Libraries
Conflicts:      netgen-libs < 6.2.2204
Provides:       %{name}:%{_libdir}/netgen/libnggui.so

%description -n netgen-gui-libs
GUI support for NETGEN mesh generator shared libraries.

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
%global optflags %{optflags} -DPYBIND11_HAS_FILESYSTEM_IS_OPTIONAL=1

# Work around broken version detection
echo "v%{version}-0-0" > ./version.txt

# Do not error out on undefined symbols - there is a circular dependency
# between libvisual and libmesh ...
%cmake \
    -DOpenGL_GL_PREFERENCE=GLVND \
    -DUSE_SUPERBUILD=OFF \
    -DCMAKE_SHARED_LINKER_FLAGS="-flto=auto -Wl,--as-needed -Wl,--warn-unresolved-symbols -Wl,-z,now" \
    -DNG_INSTALL_DIR_INCLUDE=%{_includedir}/netgen \
    -DNG_INSTALL_DIR_LIB=%{_libdir}/netgen \
    -DCMAKE_SKIP_RPATH:BOOL=OFF \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
    -DCMAKE_SKIP_BUILD_RPATH=ON \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
    -DCMAKE_INSTALL_RPATH_USE_LINK_PATH:BOOL=ON \
    -DENABLE_UNIT_TESTS=ON \
    -DDOWNLOAD_DEPENDENCIES=OFF \
    -DUSE_NATIVE_ARCH=OFF \
    -DUSE_GUI=ON \
    -DUSE_PYTHON=ON \
    -DPREFER_SYSTEM_PYBIND11=ON \
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
# Stubgen imports the just created netgen bindings -- https://github.com/NGSolve/netgen/issues/132
export PYTHONPATH=%{buildroot}%{python3_sitearch}
# Avoid creating invalid bytecode fails via stubgen
export PYTHONDONTWRITEBYTECODE=1
%cmake_install
rm -Rf %{buildroot}%{_datadir}/%{name}/doc
# https://github.com/NGSolve/netgen/issues/126
find %{buildroot}%{_libdir}/ -iname \*.a -print -delete
# Remove private attributes from stubs
find %{buildroot}%{python3_sitearch} -iname \*.pyi -exec sed -i -e '/^_[^_].*=/ d' '{}' \;

%fdupes %{buildroot}/%{_prefix}

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}/%{name}
# Test if the binary actually works
%{buildroot}/%{_bindir}/netgen -batchmode || true
%ctest --exclude-regex pytest

%if %{with pytest}
# run manually, to see progress/failures
# tolerance failures on aarch64 and ppc64le, see https://github.com/NGSolve/netgen/issues/167
%ifarch %{arm64} %{ppc64}
export PYTEST_ADDOPTS='-k "not (boxcyl.geo-mp11-5 or cylsphere.geo-mp58-4 or hinge.stl-mp93-5 or part1.stl-mp123-1 or part1.stl-mp126-4 or sculpture.geo-mp143-4 or sphereincube.geo-mp162-5 or twobricks.geo-mp195-2 or twocubes.geo-mp201-2)"'
%endif
export COLUMNS=120
(cd tests/pytest; %{python3_pytest_arch})
%endif

%files
%license LICENSE
%doc doc/*.pdf
%{_bindir}/*

%files examples
%{_datadir}/netgen

%files -n netgen-libs
%dir %{_libdir}/netgen
%{_libdir}/netgen/libngcore.so
%{_libdir}/netgen/libnglib.so

%files -n netgen-gui-libs
%{_libdir}/netgen/libnggui.so

%files -n python3-%{name}
%{python3_sitearch}/netgen
%{python3_sitearch}/pyngcore
%{python3_sitearch}/netgen_mesher-*.egg-info

%files devel
%dir %{_prefix}/lib/cmake
%{_includedir}/netgen
%{_prefix}/lib/cmake/netgen

%changelog
