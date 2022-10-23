#
# spec file for package vtk-m
#
# Copyright (c) 2022 SUSE LLC
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


%define flavor @BUILD_FLAVOR@%{nil}
%define major_ver 1
%define minor_ver 9
%define patch_ver 0
%define short_ver %{major_ver}.%{minor_ver}

%if "%flavor" != "%nil"
  %define pkg_suffix -%{flavor}
  %bcond_without mpi
%else
  %bcond_with mpi
%endif

%if 0%{?fedora} && %{with mpi}
ExclusiveArch:  do_not_build
%endif

# Let the user build the rpm with cuda if wanted
%bcond_with cuda

%if %{with mpi}
%define pkg_prefix     %{_libdir}/mpi/gcc/%{flavor}
%define pkg_libdir     %{pkg_prefix}/%{_lib}
%define pkg_includedir %{pkg_prefix}/include
%define pkg_datadir    %{pkg_prefix}/share
%define pkg_docdir     %{pkg_prefix}/share/doc/packages/%{name}
%else
%define pkg_prefix     %{_prefix}
%define pkg_libdir     %{_libdir}
%define pkg_includedir %{_includedir}
%define pkg_datadir    %{_datadir}
%define pkg_docdir     %{_docdir}/%{name}
%endif

%{?suse_version:%define is_suse 1}%{?!suse_version:%define is_suse 0}

%define shlib        libvtk-m-%{major_ver}_%{minor_ver}%{?pkg_suffix}

# Header ----------------------------------------------------------------------
Name:           vtk-m%{?pkg_suffix}
Version:        %{major_ver}.%{minor_ver}.%{patch_ver}
Release:        0
Summary:        Visualization ToolKit for Many-cores (vtk-m)
License:        BSD-3-Clause
Group:          Productivity/Scientific/Other
URL:            https://m.vtk.org/
Source0:        vtk-m-v%{version}.tar.gz
Source1:        vtk-m-rpmlintrc
# PATCH-FIX-UPSTREAM
Patch0:         https://gitlab.kitware.com/vtk/vtk-m/-/commit/7ceec1ddac79e6e7e3dc8b6c8f02fb01e2cbdc46.patch#/0001-fix-soname-lib.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
%if %{?is_suse}
BuildRequires:  memory-constraints
BuildRequires:  ninja
%endif
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
%if %{with mpi}
BuildRequires:  %{flavor}-devel
%endif

%description
VTK-m is a toolkit of scientific visualization algorithms for emerging
processor architectures. VTK-m supports the fine-grained concurrency for
data analysis and visualization algorithms required to drive extreme scale
computing by providing abstract models for data and execution that can be
applied to a variety of algorithms across many different processor
architectures.

This build includes the following backends:
  - OpenMP
%if %{with cuda}
  - CUDA
%endif

%package -n %{shlib}
Summary:        Visualization ToolKit for Many-cores (vtk-m) run-time libraries
Group:          System/Libraries
%if %{with mpi}
Requires:       %{flavor}
%endif

%description -n %{shlib}
VTK-m is a toolkit of scientific visualization algorithms for emerging
processor architectures.

This package provides the shared libraries for VTK-m.

%package devel
Summary:        Visualization ToolKit for Many-cores (vtk-m) development libraries
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}
Requires:       cmake
%if %{with mpi}
Requires:       %{flavor}-devel
%endif

%description devel
VTK-m is a toolkit of scientific visualization algorithms for emerging
processor architectures.

This provides development libraries and header files required to compile C++
programs that use VTK-m to do 3D visualization.

%prep
%setup  -q -n vtk-m-v%{version}
%patch0 -p1

%build
# vtk-m requires massive amounts of memory to build:
# - In SUSE we can directly set the min per thread
# - In Fedora just have no choice but to hardcode the num of threads.
%if %{?is_suse}
%global __builder ninja
%limit_build -m 2000
%else
%global _smp_mflags -j4
%endif
# INSTALL_CONFIG_DIR must be specified as relative path, https://gitlab.kitware.com/vtk/vtk-m/-/issues/741
%cmake \
%if %{with cuda}
    -DVTKm_ENABLE_CUDA=ON \
    -DVTKm_CUDA_Architecture=all \
%endif
%if %{with mpi}
    -DVTKm_ENABLE_MPI=ON \
%endif
    -DVTKm_ENABLE_OPENMP=ON \
    -DVTKm_ENABLE_RENDERING=ON \
    -DVTKm_ENABLE_GL_CONTEXT=ON \
    -DVTKm_ENABLE_TESTING=OFF \
    -DVTKm_ENABLE_TESTING_LIBRARY=ON \
    -DVTKm_ENABLE_EXAMPLES=ON \
    -DVTKm_NO_INSTALL_README_LICENSE=ON \
    -DVTKm_INSTALL_CONFIG_DIR=%{_lib}/cmake/vtkm-%{short_ver} \
    -DVTKm_INSTALL_LIB_DIR=%{pkg_libdir} \
    -DVTKm_CUSTOM_LIBRARY_SUFFIX="" \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_INSTALL_DOCDIR=%{pkg_docdir} \
    -DCMAKE_SKIP_RPATH:BOOL=OFF \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    %{nil}
%cmake_build

%install
%cmake_install
# VTKm_INSTALL_EXAMPLES=OFF has no effect, https://gitlab.kitware.com/vtk/vtk-m/-/issues/742
rm -Rf %{buildroot}/%{pkg_docdir}/examples

%post   -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files  -n %{shlib}
%{pkg_libdir}/lib*.so.*

%files  devel
%license LICENSE.txt
%doc CONTRIBUTING.md README.md
%{pkg_libdir}/cmake/vtkm-%{short_ver}
%{pkg_libdir}/lib*.so
%{pkg_includedir}/vtkm-%{short_ver}
%{pkg_datadir}/vtkm-%{short_ver}
%if %{with mpi}
%dir %{pkg_libdir}/cmake
%endif

%changelog
