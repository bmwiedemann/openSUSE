#
# spec file for package wannier90
#
# Copyright (c) 2026 SUSE LLC and contributors
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

%define pname wannier90

# SECTION MPI DEFINITIONS
%if "%{flavor}" == ""
%define package_name %{pname}
%endif

%if "%{flavor}" == "openmpi4"
%global mpi_flavor openmpi
%define mpi_vers 4
%endif

%if "%{flavor}" == "openmpi5"
%if 0%{?suse_version} < 1550
ExclusiveArch:  do_not_build
%endif
%global mpi_flavor openmpi
%define mpi_vers 5
%endif

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}
%{?with_mpi:%{!?mpi_flavor:error "No MPI family specified!"}}

%global _gcc_ver %(gcc -dumpversion)

%if %{with mpi}
%define my_prefix  %{_libdir}/mpi/gcc/%{mpi_flavor}%{?mpi_vers}
%define my_bindir  %{my_prefix}/bin
%define my_libdir  %{my_prefix}/%{_lib}
%define my_fmoddir %{my_libdir}/finclude
%define my_incdir  %{my_prefix}/include
%define my_datadir %{my_prefix}/share
%define my_suffix  -%{mpi_flavor}%{?mpi_vers}
%else
%define my_prefix  %{_prefix}
%define my_bindir  %{_bindir}
%define my_libdir  %{_libdir}
%define my_fmoddir %{my_libdir}/gcc/%{_host}/%{_gcc_ver}/finclude
%define my_incdir  %{_includedir}
%define my_datadir %{_datadir}
%endif
# /SECTION MPI DEFINITIONS

%define libname lib%{pname}_4%{?with_mpi:_mpi%{my_suffix}}
Name:           %{pname}%{?my_suffix}
Version:        4.0.2
Release:        0
Summary:        A library for generating maximally-localized Wannier functions
License:        LGPL-2.1-or-later
URL:            http://www.wannier.org/
Source:         https://github.com/wannier-developers/wannier90/archive/refs/tags/v%{version}.tar.gz#/%{pname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM wannier90-pkgconfig-paths.patch badshah400@gmail.com -- Fix paths in pkgconfig variables
Patch0:         wannier90-pkgconfig-paths.patch
# PATCH-FIX-UPSTREAM wannier90-disable-failing-test.patch badshah400@gmail.com -- Disable a failing test that causes build failures specific to rpmbuild env
Patch1:         wannier90-disable-failing-test.patch
# PATCH-FIX-UPSTREAM gh#wannier-developers/wannier90#371 badshah400@gmail.com -- Ignore rank mismatch issues when building openmpi flavours with gfortran, as recommended in upstream bug report
Patch2:         wannier90-fix-parallel-compilation.patch
# PATCH-FIX-UPSTREAM wannier90-arm64-disable-failing-test.patch gh#wannier-developers/wannier90#678 badshah400@gmail.com -- Disable a test that fails due to minor tolerance issues on arm64
Patch3:         wannier90-arm64-disable-failing-test.patch
BuildRequires:  blas-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  memory-constraints
%if %{with mpi}
BuildRequires:  %{mpi_flavor}%{?mpi_vers}-devel
%if 0%{?suse_version} >= 1550 && "%{mpi_flavor}" == "openmpi"
# hackish workaround for multiple openmpiX-config all providing openmpi-runtime-config
BuildRequires:  %{mpi_flavor}%{?mpi_vers}-config
%endif
%endif

%description
Wannier90 is a library for generating maximally-localized Wannier functions and
using them to compute advanced electronic properties of materials with high
efficiency and accuracy.

%package -n %{libname}
Summary:        Library for generating maximally-localized Wannier functions - shared library

%description -n %{libname}
Wannier90 is a library for generating maximally-localized Wannier functions and
using them to compute advanced electronic properties of materials with high
efficiency and accuracy.

This package provides the shared library for wannier90.

%package devel
Summary:        Library for generating Wannier functions - headers and development files

%description devel
Wannier90 is a library for generating maximally-localized Wannier functions and
using them to compute advanced electronic properties of materials with high
efficiency and accuracy.

This package provides files needed for developing against wannier90.

%prep
%autosetup -N -n %{pname}-%{version}
%autopatch -p1 -M 2
%ifarch %arm64
%patch -P 3 -p1
%endif

%build
%if %{with mpi}
source %{my_bindir}/mpivars.sh
%endif
%cmake \
  -DCMAKE_INSTALL_BINDIR=%{my_bindir} \
  -DCMAKE_INSTALL_INCLUDEDIR=%{my_incdir} \
  -DCMAKE_INSTALL_LIBDIR=%{my_libdir} \
  -DCMAKE_INSTALL_MODULEDIR=%{my_fmoddir} \
  -DWANNIER90_WITH_C=ON \
  -DWANNIER90_MPI=%{?with_mpi:ON}%{!?with_mpi:OFF} \
%{nil}
%cmake_build

%install
%cmake_install

# Tests are wrecked on i586; don't even bother
%ifnarch %ix86
# Tests deadlock on openmpi5
%if 0%{?mpi_vers} != 5
%check
%if %{with mpi}
source %{my_bindir}/mpivars.sh
%endif
# Some tests are very memory intensive
%limit_build -m 6000
%ctest
%endif
%endif
#

%ldconfig_scriptlets -n %{libname}

%files
%license LICENSE
%doc CHANGELOG.md README.rst
%{my_bindir}/*

%files -n %{libname}
%{my_libdir}/lib*.so.*

%files devel
%{my_fmoddir}/Wannier90/
%{my_incdir}/*.h
%{my_libdir}/pkgconfig/*.pc
%{my_libdir}/lib*.so
%{my_libdir}/cmake/Wannier90/
%if %{with mpi}
%dir %{my_libdir}/cmake
%dir %{my_libdir}/finclude
%endif

%changelog
