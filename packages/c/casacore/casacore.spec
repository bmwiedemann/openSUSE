#
# spec file
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


# ninja too old on openSUSE Leap 15.1
%if 0%{?suse_version} == 1500 && 0%{?sle_version} == 150100
%bcond_with ninja
%else
%global __builder ninja
%bcond_without ninja
%endif

%global flavor @BUILD_FLAVOR@%{nil}

%define sover 7
%global shlib lib%{name}%{sover}
%define srcname casacore

# SECTION MPI DEFINITIONS
%if "%{flavor}" == "openmpi4"
%global mpi_flavor openmpi
%define mpi_vers 4
%endif

%if "%{flavor}" == "openmpi5"
%global mpi_flavor openmpi
%define mpi_vers 5
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
%define shlib lib%{srcname}%{sover}%{?my_suffix}
# /SECTION

Name:           %{pname}
Version:        3.5.0
Release:        0
Summary:        A suite of C++ libraries for radio astronomy data processing
License:        LGPL-2.0-or-later
URL:            https://github.com/casacore/casacore
Source:         https://github.com/casacore/casacore/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Source99:       casacore-rpmlintrc
# PATCH-FIX-UPSTREAM casacore-fitsio-header.patch badshah400@gmail.com -- Fix location of cfitsio headers used in sources
Patch1:         casacore-fitsio-header.patch
# PATCH-FIX-UPSTREAM casacore-mirlib-gcc14-compat.patch gh#casacore/casacore#1344 badshah400@gmail.com -- Fix builds against GCC 14; patch taken from upstream commit
Patch2:         https://github.com/casacore/casacore/commit/a4516a86f935dea17502727c34f91955b73209ef.patch#/casacore-mirlib-gcc14-compat.patch
BuildRequires:  bison
BuildRequires:  blas-devel
BuildRequires:  cmake
BuildRequires:  fftw3-threads-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  hdf5%{?my_suffix}-devel
BuildRequires:  lapack-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_python3-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(wcslib)
BuildRequires:  pkgconfig(zlib)
%if %{with mpi}
BuildRequires:  %{mpi_flavor}%{?mpi_vers}-config
BuildRequires:  %{mpi_flavor}%{?mpi_vers}-devel
BuildRequires:  fftw3-openmp-devel
%endif
%if %{with ninja}
BuildRequires:  ninja
%endif

%description
Casacore provides a suite of C++ libraries for radio astronomy data processing.

%package -n %{shlib}
Summary:        Shared libraries for casacore, a suite of radio astronomy data

%description -n %{shlib}
Casacore provides a suite of C++ libraries for radio astronomy data processing.

This package provides the shared libraries for casacore.

%package devel
Summary:        Headers and sources for developing with casacore
Requires:       %{shlib} = %{version}
Requires:       gsl-devel
Requires:       hdf5-devel
Requires:       lapack-devel
Requires:       libboost_python3-devel
Requires:       readline-devel
Requires:       pkgconfig(cfitsio)
Requires:       pkgconfig(fftw3)
Requires:       pkgconfig(ncurses)
Requires:       pkgconfig(wcslib)

%description devel
Casacore provides a suite of C++ libraries for radio astronomy data processing.

This package provides the headers and sources for developing software with casacore.

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
%cmake \
  -DCMAKE_INSTALL_PREFIX:PATH=%{my_prefix} \
  -DUSE_FFTW3:BOOL=ON \
  -DDATA_DIR:PATH=%{my_datadir}/casacore/data \
  -DPORTABLE:BOOL=ON \
  -DUSE_OPENMP:BOOL=ON \
  -DUSE_MPI:BOOL=%{?with_mpi:ON}%{!?with_mpi:OFF} \
  -DUSE_HDF5:BOOL=ON \
  -DBUILD_PYTHON:BOOL=OFF \
  -DBUILD_PYTHON3:BOOL=ON \
  -DENABLE_SHARED:BOOL=ON \
  -DENABLE_RPATH:BOOL=OFF \
  -DUSE_THREADS:BOOL=ON

%cmake_build

%install
%cmake_install

# Move pkgconfig file to arch-specific libdir
if [ "%{_lib}" != "lib" ]
then
mkdir -p %{buildroot}%{my_libdir}/pkgconfig/
mv %{buildroot}%{my_prefix}/lib/pkgconfig/*.pc %{buildroot}%{my_libdir}/pkgconfig/
fi

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files
%{my_bindir}/*

%files -n %{shlib}
%{my_libdir}/*.so.%{sover}

%files devel
%license COPYING
%doc CHANGES.md README.md
%{my_libdir}/*.so
%{my_libdir}/pkgconfig/*.pc
%{my_incdir}/casacore/

%changelog
