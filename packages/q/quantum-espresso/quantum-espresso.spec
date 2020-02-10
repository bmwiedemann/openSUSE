#
# spec file for package quantum-espresso
#
# Copyright (c) 2020 SUSE LLC
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

%define pname quantum-espresso

%if 0%{?sle_version} >= 150200
%define DisOMPI1 ExclusiveArch:  do_not_build
%endif
%if !0%{?is_opensuse} && 0%{?sle_version:1} && 0%{?sle_version} < 150200
%define DisOMPI3 ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == ""
%define package_name %{pname}
ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" != "" && !0%{?DisOMPI1:1} && !0%{?DisOMPI2:1} && !0%{?DisOMPI3:1}
ExclusiveArch:  x86_64
%endif

%if "%{flavor}" == "mvapich2"
%global mpi_flavor mvapich2
%endif

%if "%{flavor}" == "openmpi1"
%global mpi_flavor openmpi
%define mpi_vers 1
%{?DisOMPI1}
%endif

%if "%{flavor}" == "openmpi2"
%global mpi_flavor openmpi
%define mpi_vers 2
%{?DisOMPI2}
%endif

%if "%{flavor}" == "openmpi3"
%global mpi_flavor openmpi
%define mpi_vers 3
%{?DisOMPI3}
%endif

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}
%{?with_mpi:%{!?mpi_flavor:error "No MPI family specified!"}}

# For compatibility package names
%if "%{flavor}" == "openmpi1" && 0%{?suse_version} <= 1500
%define mpi_ext %{nil}
%else
%define mpi_ext %{?mpi_vers}
%endif

%if %{without mpi}
 %define my_prefix %_prefix
 %define my_bindir %_bindir
 %define my_libdir %_libdir
 %define my_incdir %_includedir
%else
 %define my_prefix %{_libdir}/mpi/gcc/%{mpi_flavor}%{?mpi_ext}
 %define my_bindir %{my_prefix}/bin
 %define my_suffix -%{mpi_flavor}%{?mpi_ext}
%endif

%if 0%{!?package_name:1}
 %define package_name   %pname%{?my_suffix}
%endif

Name:           %{package_name}
Version:        6.4.1
Release:        0
Summary:        A suite for electronic-structure calculations and materials modeling
License:        GPL-2.0-only
Group:          Productivity/Scientific/Physics
URL:            http://www.quantum-espresso.org
Source0:        https://gitlab.com/QEF/q-e/-/archive/qe-%{version}/q-e-qe-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM backports-6.4.1.git-diff badshah400@gmail.com -- Backported fixes for version 6.4.1 from upstream
Patch0:         https://gitlab.com/QEF/q-e/wikis/uploads/3e4b6d3844989c02d0ebb03a935e1976/backports-6.4.1.git-diff
BuildRequires:  fdupes
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
%if %{with mpi}
BuildRequires:  %{mpi_flavor}%{?mpi_ext}-devel
BuildRequires:  fftw3-mpi-devel
%if 0%{?suse_version} >= 1550 && %{mpi_flavor} == "openmpi"
# hackish workaround for multiple openmpiX-config all providing openmpi-runtime-config
BuildRequires:  %{mpi_flavor}%{?mpi_ext}-config
%endif
%if "%{flavor}" == "openmpi1" && 0%{?suse_version} <= 1550
Provides:       %{pname}-openmpi = %{version}-%{release}
Obsoletes:      %{pname}-openmpi < %{version}-%{release}
%endif
%else
BuildRequires:  fftw3-devel
%endif

%description
Quantum ESPRESSO is an integrated suite of Open-Source computer codes for
electronic-structure calculations and materials modeling at the nanoscale.
It is based on density-functional theory, plane waves, and pseudopotentials.

%package doc
Summary:        Documentation files for Quantum Espresso
Group:          Documentation/Other

%description doc
This package contains the documentation files for Quantum Espresso.

Quantum ESPRESSO is an integrated suite of Open-Source computer codes for
electronic-structure calculations and materials modeling at the nanoscale.
It is based on density-functional theory, plane waves, and pseudopotentials.

%prep
%autosetup -p1 -n q-e-qe-%{version}

%build
%if %{with mpi}
export CC="%{my_bindir}/mpicc"
export FC="%{my_bindir}/mpif90"
%configure --enable-parallel
%else
export CC=gcc
export FC=gfortran
%configure --disable-parallel
%endif
make %{?_smp_mflags} all

%install
mkdir -p %{buildroot}%{my_bindir}
pushd bin
for bin in *.x; do
    install -m 755 $bin %{buildroot}%{my_bindir}/qe_$bin
done
popd

%fdupes -s Doc/

%files
%defattr(-,root,root)
%doc README.md
%license License
%{my_bindir}/*.x

%if %{without mpi}
%files doc
%defattr(-,root,root)
%doc Doc/*
%endif

%changelog
