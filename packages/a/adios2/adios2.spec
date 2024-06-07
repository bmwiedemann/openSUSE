#
# spec file for package adios2
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


%define flavor @BUILD_FLAVOR@%{nil}
%define major_ver 2
%define minor_ver 10
%define patch_ver 1
# Name the suffix of the pkg
%if "%{flavor}" != "%{nil}"
  %define pkg_suffix -%{flavor}
%endif
%if "%{flavor}" == "mpich"
%global mpi_flavor mpich
%global mpi_family mpich
%endif
%if "%{flavor}" == "mvapich2"
%global mpi_flavor mvapich2
%global mpi_family mvapich2
%endif
%if "%{flavor}" == "openmpi4"
%global mpi_flavor openmpi4
%global mpi_family openmpi
%global mpi_ver 4
%endif
%if "%{flavor}" == "openmpi5"
%global mpi_flavor openmpi5
%global mpi_family openmpi
%global mpi_ver 5
%endif

# Paths  ----------------------------------------------------------------------
%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}
%{?with_mpi:%{!?mpi_flavor:%global mpi_flavor openmpi}}
%{?with_mpi:%global pkg_suffix -%{mpi_flavor}}
%{?with_mpi:%define pkg_prefix %{_libdir}/mpi/gcc/%{mpi_flavor}}
%{!?with_mpi:%define pkg_prefix %{_prefix}}
%define pkg_bindir  %{pkg_prefix}/bin
%define pkg_libdir  %{pkg_prefix}/%{_lib}/
%define pkg_incdir  %{pkg_prefix}/include/
%define pkg_datadir %{pkg_prefix}/share/
%define shlib       libadios2%{?pkg_suffix}-%{major_ver}_%{minor_ver}
# Header ----------------------------------------------------------------------
Name:           adios2%{?pkg_suffix}
Version:        %{major_ver}.%{minor_ver}.%{patch_ver}
Release:        0
Summary:        The Adaptable IO System (ADIOS2)
License:        Apache-2.0
Group:          Productivity/Scientific/Other
URL:            https://adios2.readthedocs.io/en/
Source0:        https://github.com/ornladios/ADIOS2/archive/refs/tags/v%{version}.tar.gz#/ADIOS2-%{version}.tar.gz
Source1:        adios2-rpmlintrc
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  libbz2-devel
BuildRequires:  libffi-devel
BuildRequires:  liblz4-devel
BuildRequires:  ninja
BuildRequires:  zlib-devel
ExcludeArch:    %{ix86}
# mpi4py pkg (Not MPI-4)
%if %{with mpi}
BuildRequires:  %{mpi_flavor}-devel
%endif

%description
ADIOS2: The Adaptable Input Output (I/O) System version 2  is an open-source
framework that addresses scientific data management challenges, e.g. scalable
parallel I/O, as we approach the exascale era in high-performance computing
(HPC). ADIOS 2 bindings are available in C++, C, Fortran, Python and can be
used on supercomputers, personal computers, and cloud systems running on Linux,
macOS and Windows. ADIOS 2 has out-of-the-box support for MPI and serial
environments.

This package contains all files needed to run projects that depends on the
%{?mpi_flavor}%{!?mpi_flavor:serial} version of ADIOS2.

%package -n %{shlib}
Summary:        The Adaptable IO System (ADIOS2) run-time libraries
Group:          System/Libraries
Provides:       %{name} = %{version}
%{?mpi_flavor:Requires:       %{mpi_flavor}}

%description -n %{shlib}
ADIOS2: The Adaptable Input Output (I/O) System version 2  is an open-source
framework that addresses scientific data management challenges.

This package provides the shared libraries for ADIOS2.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Parallel
Requires:       %{shlib} = %{version}
Conflicts:      adios%{?pkg_suffix}
%if 0%{?with_hdf5}
BuildRequires:  hdf5%{?mpi_flavor:-%{mpi_flavor}}-devel
Requires:       hdf5%{?mpi_flavor:-%{mpi_flavor}}-devel
%endif

%description devel
ADIOS2: The Adaptable Input Output (I/O) System version 2  is an open-source
framework that addresses scientific data management challenges.

This package contains all files needed to create projects that use the
%{?mpi_flavor}%{!?mpi_flavor:serial} version of ADIOS2.

%prep
%autosetup -p1 -n ADIOS2-%{version}
bindir=%{_bindir} sed -i "1c #!${bindir}/python3" \
      source/utils/bp4dbg/bp4dbg.py \
      source/utils/bp5dbg/bp5dbg.py \
      source/utils/adios2_json_pp.py

%build
%global __builder ninja
export CC=gcc
export CXX=g++
export FC=gfortran
%if %{with mpi}
source %{pkg_prefix}/bin/mpivars.sh
%endif
%cmake \
    -DADIOS2_BUILD_EXAMPLES=OFF \
    -DADIOS2_INSTALL_GENERATE_CONFIG=OFF \
    -DADIOS2_USE_BP5=ON \
    -DADIOS2_USE_BZip2=ON \
    -DADIOS2_USE_Fortran=ON \
    -DADIOS2_USE_HDF5=%{?with_hdf5:ON}%{!?with_hdf5:OFF} \
    -DADIOS2_USE_MGARD=OFF \
    -DADIOS2_USE_MPI=%{?with_mpi:ON}%{!?with_mpi:OFF} \
    -DADIOS2_USE_Profiling=OFF \
    -DADIOS2_USE_Python=OFF \
    -DBUILD_TESTING=OFF \
    -DCMAKE_BUILD_TYPE=RELWITHDEBINFO \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_POSITION_INDEPENDENT_CODE=ON
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%license Copyright.txt
%{pkg_libdir}/*.so.*
%{pkg_libdir}/adios2-evpath-modules-%{major_ver}_%{minor_ver}

%files devel
%doc Contributing.md ReadMe.md
%{pkg_bindir}/*
%{pkg_incdir}/*
%{pkg_libdir}/*.so
%{pkg_libdir}/cmake/adios2

# When using MPI whe own these dirs
%if %{with mpi}
%dir %{pkg_libdir}/cmake
%{pkg_datadir}/iotest-config
%endif

%changelog
