#
# spec file for package wannier90
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

%define pname wannier90

# SECTION MPI DEFINITIONS
%if "%{flavor}" == ""
%define package_name %{pname}
%endif

%if "%{flavor}" == "openmpi1"
%global mpi_flavor openmpi
%define mpi_vers 1
%endif

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

%if "%{flavor}" == "openmpi5"
%if 0%{?suse_version} < 1550
ExclusiveArch:  do_not_build
%endif
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

Name:           %{pname}%{?my_suffix}
Version:        3.1.0
Release:        0
Summary:        A library for generating maximally-localized Wannier functions
License:        GPL-2.0-only
URL:            http://www.wannier.org/
Source:         https://github.com/wannier-developers/wannier90/archive/refs/tags/v%{version}.tar.gz#/%{pname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM wannier90-install-pkgconfig.patch badshah400@gmail.com -- Update Makefile to install a package config file
Patch0:         wannier90-install-pkgconfig.patch
# PATCH-FIX-UPSTREAM gh#wannier-developers/wannier90#373 badshah400@gmail.com -- Allocate arrays on non-root nodes to avoid SIGSEG
Patch1:         https://github.com/wannier-developers/wannier90/commit/a75344b646227c9d7f12d90af4a35a902e940dca.patch
# PATCH-FIX-UPSTREAM gh#wannier-developers/wannier90#371 badshah400@gmail.com -- Ignore rank mismatch issues when building openmpi flavours with gfortran, as recommended in upstream bug report
Patch2:         wannier90-fix-parallel-compilation.patch
BuildRequires:  blas-devel
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
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

%package devel
Summary:        Devel files for %{name}

%description devel
This package provides files needed for developing against wannier90.

%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1
%patch1 -p1
%if 0%{?suse_version} >= 1550
%patch2 -p1
%endif

%build
# No configure script
cp ./config/make.inc.gfort.dynlib make.inc

%if %{with mpi}
source %{my_bindir}/mpivars.sh
sed -i "s/^#COMMS\s*=\s*mpi/COMMS = mpi/" make.inc
sed -i "s/^#MPIF90\s*=\s*mpgfortran #mpif90/MPIF90 = mpif90/" make.inc
cat make.inc
%endif

%make_build all dynlib

%install
%make_install PREFIX=%{my_prefix} pkgconfig

rm %{buildroot}%{my_prefix}/lib/*.a
mkdir -p %{buildroot}%{my_libdir}/pkgconfig
find ./ -name "*.so" -print -exec install {} %{buildroot}%{my_libdir}/ \;
if [ "%{_lib}" != "lib" ]
then
  mv %{buildroot}%{my_prefix}/lib/pkgconfig/*.pc %{buildroot}%{my_libdir}/pkgconfig/
fi
sed -i "s|%{buildroot}||g" %{buildroot}%{my_libdir}/pkgconfig/*.pc

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc CHANGELOG.md README.rst
%{my_bindir}/*

%files devel
%{my_libdir}/*.so
%{my_libdir}/pkgconfig/*.pc

%changelog
