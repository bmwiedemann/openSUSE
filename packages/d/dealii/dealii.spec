#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}

%define __builder ninja
%define sover 9.4.1
%define shlibver %(echo %{sover} | tr "." "_")
%define srcname dealii

# PYTHON BINDINGS CAN"T BE BUILT [https://github.com/dealii/dealii/issues/10423]
%bcond_with python

%if 0%{?suse_version} == 1500 && 0%{?sle_version} == 150100
%bcond_with doc
%else
%bcond_without doc
%endif

# SECTION MPI DEFINITIONS
%if "%{flavor}" == "openmpi2"
%global mpi_flavor openmpi
%define mpi_vers 2
%endif

%if "%{flavor}" == "openmpi3"
%global mpi_flavor openmpi
%define mpi_vers 3
%endif

%if "%{flavor}" == "openmpi4"
%global mpi_flavor openmpi
%define mpi_vers 4
%endif

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}
%{?with_mpi:%{!?mpi_flavor:error "No MPI family specified!"}}

%if %{with mpi}
%define my_prefix  %{_libdir}/mpi/gcc/%{mpi_flavor}%{?mpi_vers}
%define my_bindir  %{my_prefix}/bin
%define my_libdir  %{my_prefix}/%{_lib}
%define my_incdir  %{my_prefix}/include
%define my_datadir %{my_prefix}/share
%define my_suffix  -%{mpi_flavor}%{?mpi_vers}
%else
%define my_prefix  %{_prefix}
%define my_bindir  %{_bindir}
%define my_libdir  %{_libdir}
%define my_incdir  %{_includedir}
%define my_datadir %{_datadir}
%endif
# /SECTION MPI DEFINITIONS

# SECTION PKG NAMING DEFINITIONS
%define pname %{srcname}%{?my_suffix}
%define shlib libdeal_II%{shlibver}%{?my_suffix}
%define shlib_debug libdeal_II_g%{shlibver}%{?my_suffix}
# /SECTION

%define memlim 2500
# LTO CAUSES aarch64 BUILDS TO TIME OUT; IT ALSO REQUIRES ~4GB PER THREAD
%ifarch aarch64
%define _lto_cflags %{nil}
%define memlim 4000
%endif
%ifarch ppc64
%define memlim 3000
%endif

Name:           %{pname}
Version:        9.4.1
Release:        0
Summary:        A Finite Element Differential Equations Analysis Library
License:        LGPL-2.1-or-later
URL:            https://www.dealii.org/
Source0:        https://github.com/dealii/dealii/releases/download/v%{version}/%{srcname}-%{version}.tar.gz
Source1:        %{srcname}-rpmlintrc
# NOTE: serial arpack-ng even if parpack is available (see gh#dealii/dealii#10197)
BuildRequires:  arpack-ng-devel
BuildRequires:  blas-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gmsh
BuildRequires:  gmsh-devel
BuildRequires:  hdf5%{?my_suffix}-devel
BuildRequires:  lapack-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libnetcdf_c++-devel
BuildRequires:  memory-constraints
BuildRequires:  metis-devel
BuildRequires:  netcdf-devel
BuildRequires:  ninja
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  suitesparse-devel
BuildRequires:  tbb-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(muparser)
BuildRequires:  pkgconfig(zlib)
%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  fdupes
%endif
%if %{with mpi}
BuildRequires:  %{mpi_flavor}%{?mpi_vers}-config
BuildRequires:  %{mpi_flavor}%{?mpi_vers}-devel
BuildRequires:  parpack%{my_suffix}-devel
BuildRequires:  scalapack%{my_suffix}-devel
%endif
%if %{with python}
BuildRequires:  libboost_python3-devel
BuildRequires:  python3-devel
%endif
# Builds fail for i586 due to linking taking too long and being mistaken by OBS workers for "Job stuck"
ExcludeArch:    i586

%description
deal.II is a C++ program library targeted at the computational solution of
partial differential equations using adaptive finite elements.

%package -n %{shlib}
Summary:        A generic C++ finite element library

%description -n %{shlib}
deal.II is a C++ program library targeted at the computational solution of
partial differential equations using adaptive finite elements.

This package provides the shared library for deal.II.

%package -n deal_II%{?my_suffix}-devel
Summary:        Development files for %{name}
Requires:       %{shlib} = %{version}
Provides:       %{name}%{?my_suffix}-devel = %{version}

%description -n  deal_II%{?my_suffix}-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n python3-PyDealII
Summary:        Python bindings for %{name}

%description -n python3-PyDealII
This package provides the python3 bindings for dealii.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%if %{with mpi}
source %{my_bindir}/mpivars.sh
export CC=mpicc
export CXX=mpicxx
%else
export CC=gcc
export CXX=g++
%endif

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"

%limit_build -m %{memlim}

# BUILD ONLY SUPPORTS "Release", "Debug", OR "DebugRelease" FOR CMAKE_BUILD_TYPE
# BUT THE "-g" FLAG TO ENABLE DEBUGINFO IS AUTOMATICALLY ADDED BY %%{optflags};
# SO SIMPLY USE CMAKE_BUILD_TYPE="Release"
%cmake -DCMAKE_INSTALL_PREFIX:PATH=%{my_prefix} \
       -DCMAKE_PREFIX_PATH:PATH=%{my_prefix} \
       -DCMAKE_BUILD_TYPE:STRING="Release" \
       -DCMAKE_INSTALL_RPATH_USE_LINK_PATH:BOOL=OFF \
       -DDEAL_II_COMPONENT_DOCUMENTATION:BOOL=%{?with_doc:ON}%{!?with_doc:OFF} \
       -DDEAL_II_WITH_THREADS:BOOL=ON \
       -DDEAL_II_WITH_MPI:BOOL=%{?with_mpi:ON}%{!?with_mpi:OFF} \
       -DDEAL_II_COMPONENT_PYTHON_BINDINGS:BOOL=%{?with_python:ON}%{!?with_python:OFF} \
       -DDEAL_II_DOCHTML_RELDIR:PATH=%{_docdir}/%{name} \
       -DDEAL_II_EXAMPLES_RELDIR:PATH=%{_docdir}/%{name} \
       -DDEAL_II_COMPILE_EXAMPLES:BOOL=OFF \
       -DDEAL_II_ALLOW_BUNDLED:BOOL=OFF

%cmake_build

%install
%cmake_install

# REMOVE UNNECESSARY FILES
rm %{buildroot}%{my_prefix}/*.md \
   %{buildroot}%{my_prefix}/detailed.log \
   %{buildroot}%{my_prefix}/summary.log

# CLEAR UP UNNECESSARY HASHBANGS
sed -i "1{/\/bin\/sh/d}" %{buildroot}%{my_datadir}/deal.II/scripts/get_*_tag.sh
sed -i "1{/\/usr\/bin\/env/d}" %{buildroot}%{my_datadir}/deal.II/scripts/indent.py

%if %{with doc}
%fdupes %{buildroot}%{_docdir}/%{name}/
%endif

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%{my_libdir}/libdeal_II.so.%{sover}

%files -n deal_II%{?my_suffix}-devel
%license LICENSE.md
%doc AUTHORS.md README.md CONTRIBUTING.md
%doc %{_docdir}/%{name}
%{my_incdir}/deal.II/
%{my_libdir}/*.so
%{my_datadir}/deal.II/
%{my_libdir}/cmake/
%{my_libdir}/pkgconfig/*.pc

%if %{with python}
%files -n python3-PyDealII
%license LICENSE.md
%{python3_sitelib}/PyDealII/
%endif

%changelog
