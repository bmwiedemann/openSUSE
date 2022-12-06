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

%define so_ver 2

%if 0%{?sle_version} >= 150200
%define DisOMPI1 ExclusiveArch:  do_not_build
%endif
%if !0%{?is_opensuse} && 0%{?sle_version:1} && 0%{?sle_version} < 150200
%define DisOMPI3 ExclusiveArch:  do_not_build
%endif

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%endif

%bcond_without openblas

%if "%flavor" == "serial"
%{bcond_with hpc}
%endif

%if "%flavor" == "openmpi1"
%{?DisOMPI1}
%define mpi_family openmpi
%define mpi_ver 1
%{bcond_with hpc}
%endif

%if "%flavor" == "openmpi2"
%{?DisOMPI2}
%define mpi_family openmpi
%define mpi_ver 2
%{bcond_with hpc}
%endif

%if "%flavor" == "openmpi3"
%{?DisOMPI3}
%define mpi_family openmpi
%define mpi_ver 3
%{bcond_with hpc}
%endif

%if "%flavor" == "openmpi4"
%define mpi_family openmpi
%define mpi_ver 4
%{bcond_with hpc}
%endif

# openmpi 1 was called just "openmpi" in Leap 15.x/SLE15
%if 0%{?suse_version} >= 1550 || "%{mpi_family}" != "openmpi"  || "%{mpi_ver}" != "1"
%define mpi_ext %{?mpi_ver}
%endif

%if 0%{?mpi_family:1}
%{bcond_without mpi}
%define pkgname   parpack-%{mpi_family}%{?mpi_ext}
%define libname() libparpack%{so_ver}-%{mpi_family}%{?mpi_ext}
%global my_prefix %{_libdir}/mpi/gcc/%{mpi_family}%{?mpi_ext}
%global my_libdir %{my_prefix}/%{_lib}
%global my_incdir %{my_prefix}/include
%else
%{bcond_with mpi}
%define pkgname   arpack-ng
%define libname() libarpack%{so_ver}
%global my_prefix %{_prefix}
%global my_libdir %{_libdir}
%global my_incdir %{_includedir}
%endif

# 3. OOM on i586 and 32-bit Arm: https://github.com/opencollab/arpack-ng/issues/289
%ifarch i586 %{arm}
%bcond_with pyarpack
%else
# 2. Boost too old for 15.2 and earlier
%if 0%{?suse_version} < 1550
%bcond_with pyarpack
%else
# 1. Build python module once: for serial flavor only
%if %{with mpi}
%bcond_with pyarpack
%else
%bcond_without pyarpack
%endif
# /1
%endif
# /2
%endif
# /3

Name:           %{pkgname}
Version:        3.8.0
Release:        0
Summary:        Fortran77 subroutines for solving large scale eigenvalue problems
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://github.com/opencollab/arpack-ng
Source0:        https://github.com/opencollab/arpack-ng/archive/%{version}.tar.gz#/arpack-ng-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE arpack-ng-python-module-installdir.patch badshah400@gmail.com -- Install python module to standard python sitearch instead of libdir
Patch0:         arpack-ng-python-module-installdir.patch
# PATCH-FIX-UPSTREAM -- Fix mixup of relative and absolute libdir in pkgconfig files
Patch1:         Use-CMAKE_INSTALL_FULL_-dir.patch
# PATCH-FIX-UPSTREAM
Patch2:         fix_tautological_compare_321.patch
%if %{with mpi}
BuildRequires:  %{mpi_family}%{?mpi_ext}-devel
%endif
BuildRequires:  blas-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
%if %{with openblas}
BuildRequires:  libopenblas_pthreads-devel
%endif
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(eigen3)
%if %{with pyarpack}
BuildRequires:  libboost_numpy3-devel
BuildRequires:  libboost_python3-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
%endif

%description
ARPACK is a collection of Fortran77 subroutines designed to solve
large scale eigenvalue problems.

Arpack-ng is the successor of the legacy Arpack. It is fully compatible
with Arpack.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
%if %{with mpi}
Requires:       %{mpi_family}%{?mpi_ext}-devel
%else
Obsoletes:      arpack-devel < %{version}
Provides:       arpack-devel = %{version}
%endif
Requires:       %{libname} = %{version}-%{release}
Requires:       blas-devel
Requires:       gcc-fortran
Requires:       lapack-devel
%if "%{name}" == "parpack-openmpi1"
Provides:       parpack-openmpi-devel = %{version}
%endif

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n %{libname}
Summary:        Files needed for developing arpack based applications
Group:          System/Libraries
%if %{with mpi}
Requires:       %{mpi_family}%{?mpi_ext}-libs
%endif

%description -n %{libname}
ARPACK is a collection of Fortran77 subroutines designed to solve
large scale eigenvalue problems. This package contains the so
library links used for building arpack based applications.

%package -n python3-%{name}
Summary:        Python bindings for ARPACK
Group:          Development/Libraries/Python

%description -n python3-%{name}
ARPACK is a collection of Fortran77 subroutines designed to solve
large scale eigenvalue problems. This package provides the python
bindings for ARPACK.

%prep
%autosetup -p1 -n arpack-ng-%{version}

# create baselibs.conf based on flavor
cat >  %{_sourcedir}/baselibs.conf <<EOF
%{libname}
%{name}-devel
    requires -%{name}-<targettype>
    requires "%{libname}-<targettype> = <version>"
EOF

%build
# Force -fPIC, otherwise linking of the test binaries fails
# on aarch64 an ppc64
export FFLAGS="%{optflags} -fPIC"
export FCFLAGS="%{optflags} -fPIC"
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"

%if %{with mpi}
source %{my_prefix}/bin/mpivars.sh
export CC=%{my_prefix}/bin/mpicc
export CXX=%{my_prefix}/bin/mpic++
export F77=%{my_prefix}/bin/mpif77
export MPIF77=%{my_prefix}/bin/mpif77
export LD_LIBRARY_PATH=%{my_prefix}/%{_lib}
%endif

%cmake \
  -DCMAKE_INSTALL_PREFIX:PATH=%{my_prefix} \
  -DCMAKE_INSTALL_LIBDIR:PATH=%{my_libdir} \
  -DCMAKE_SKIP_RPATH:BOOL=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
  -DCMAKE_CXX_COMPILER_VERSION=$(gcc -dumpfullversion) \
  -DMPI:BOOL=%{?with_mpi:ON}%{!?with_mpi:OFF} \
  -DPYTHON3:BOOL=%{?with_pyarpack:ON}%{!?with_pyarpack:OFF}

%if %{with pyarpack}
# Build pyarpack in a multiple steps, as arpackmm and
# pyarpack need a considerable amount of memory
%cmake_build arpack
%cmake_build arpackmm
%cmake_build pyarpack
%endif
# Make sure all (remaining) targets are build
%cmake_build

%install
%cmake_install
find %{buildroot} -type f -name "*.la" -delete -print

# Remove sequential version files
%if %{with mpi}
rm -Rf %{buildroot}%{my_libdir}/pkgconfig
rm %{buildroot}%{my_libdir}/libarpack.so*
%endif

ln -s EXAMPLES examples

%check
%if %{with mpi}
source %{my_prefix}/bin/mpivars.sh
%endif
%ctest

%post   -n %{libname}           -p /sbin/ldconfig
%postun -n %{libname}           -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%{my_libdir}/*.so.*

%files devel
%doc examples
%doc CHANGES README.md
%{my_libdir}/*.so
%{my_incdir}/arpack
%if %{without mpi}
%{_libdir}/pkgconfig/*.pc
%else
%dir %{my_libdir}/cmake
%endif
%{my_libdir}/cmake/arpack-ng/

%if %{with pyarpack}
%files -n python3-%{name}
%{python3_sitearch}/*.so
%endif

%changelog
