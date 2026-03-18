#
# spec file for package hypre
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


%global flavor @BUILD_FLAVOR@%{?nil}
%define somver %{_ver}
%define sover %{ver}

# Base package name
%define pname hypre
%define PNAME %(echo %{pname} | tr [a-z] [A-Z])

%if 0%{?sle_version} >= 150200
%define DisOMPI1 ExclusiveArch:  do_not_build
%endif
%if !0%{?is_opensuse} && 0%{?sle_version:1} && 0%{?sle_version} < 150200
%define DisOMPI3 ExclusiveArch:  do_not_build
%endif
%if 0%{?sle_version:1} && 0%{?sle_version} < 150300
%define DisOMPI4 ExclusiveArch:  do_not_build
%endif

%if "%flavor" == ""
%define package_name %{pname}
ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == "serial"
%undefine mpi_family
%endif

%if "%{flavor}" == "openmpi4"
%global mpi_family  openmpi
%define mpi_vers 4
%{?DisOMPI4}
%endif

%if "%{flavor}" == "openmpi5"
%global mpi_family  openmpi
%define mpi_vers 5
%{?DisOMPI5}
ExcludeArch:    i586 %arm s390
%endif

%if "%{flavor}" == "mvapich2"
%global mpi_family  mvapich2
%endif

%if "%{flavor}" == "mpich"
%global mpi_family  mpich
%endif

%{?mpi_family:%{bcond_without mpi}}%{!?mpi_family:%{bcond_with mpi}}

# For compatibility package names
%if "%{mpi_family}" != "openmpi" || "%{mpi_vers}" != "1" || 0%{?suse_version} > 1500
%define mpi_ext %{?mpi_vers}
%endif

%if %{without mpi}
 %global my_bindir %_bindir
 %global _incdir %{_prefix}/include/
%else
 %global _bindir %_bindir
 %global _defaultlicensedir %_defaultlicensedir
 %global _prefix %{_libdir}/mpi/gcc/%{mpi_family}%{?mpi_ext}
 %global _suffix -%{?mpi_family}%{?mpi_ext}
 %global my_bindir %{_prefix}/bin
 %global _libdir %{_prefix}/%{_lib}/
 %global _incdir %{_prefix}/include/
%endif
%if 0%{!?package_name:1}
  %define package_name   %pname%{?_suffix}
%endif
%define libname  lib%{PNAME}%{somver}%{?_suffix}

Name:           %package_name
Version:        3.1.0
%define somver 301
Release:        0
Summary:        Scalable algorithms for solving linear systems of equations
License:        Apache-2.0 OR MIT
Group:          Productivity/Scientific/Math
URL:            https://www.llnl.gov/casc/hypre/
Source0:        https://github.com/hypre-space/hypre/archive/v%{version}.tar.gz#/hypre-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  superlu-devel
%if 0%{?with mpi}
BuildRequires:  %{mpi_family}%{?mpi_ext}-devel
%endif
BuildRequires:  cmake
BuildRequires:  fdupes

%description
Hypre is a library of preconditioners that feature parallel multigrid
methods for both structured and unstructured grid problems arising in
the simulation codes being developed at LLNL to study physical
phenomena in the defense, environmental, energy, and biological
sciences.

%package     -n %{libname}
Summary:        Scalable algorithms for solving linear systems of equations
Group:          System/Libraries

%description -n %{libname}
Hypre is a library of preconditioners that feature parallel multigrid
methods for both structured and unstructured grid problems arising in
the simulation codes being developed at LLNL to study physical
phenomena in the defense, environmental, energy, and biological
sciences.

This package contains %{?mpi_family}%{?mpi_vers}%{!?mpi_family:serial} shared libraries of Hypre.

%package devel
Summary:        Headers and library links for %{libname}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %version
Requires:       lapack-devel
Requires:       superlu-devel

%description devel
%{PNAME} headers and libraries files needed for development
This package contains development files of the %{?mpi_family}%{?mpi_vers}%{!?mpi_family:serial} version of Hypre.

%package        examples
Summary:        Examples for Hypre
Group:          Documentation/Other
BuildArch:      noarch

%description    examples
This package contains examples for Hypre.

%package        doc
Summary:        Development documentation for Hypre
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
This package contains development documentation for Hypre.

%prep
%autosetup -n %{pname}-%{version}

%build
%{?with_mpi: . %{my_bindir}/mpivars.sh}

cd src/
%cmake \
       -DCMAKE_SHARED_LINKER_FLAGS="-lm" \
       -DCMAKE_INSTALL_INCLUDEDIR="include/hypre" \
       -DHYPRE_ENABLE_FORTRAN=ON \
       -DHYPRE_ENABLE_LTO=ON \
       %if %{without mpi}
       -DHYPRE_ENABLE_OPENMP=ON \
       -DHYPRE_ENABLE_MPI=OFF \
       %else
       -DHYPRE_ENABLE_OPENMP=OFF \
       -DHYPRE_ENABLE_MPI=ON \
       %endif
       -DHYPRE_ENABLE_HYPRE_BLAS=OFF \
       -DHYPRE_ENABLE_HYPRE_LAPACK=OFF \
       -DHYPRE_ENABLE_SUPERLU=ON \
%{nil}

%cmake_build

%install
cd src/
install -m 644 -D docs/usr-manual/*pdf -t %{buildroot}%{_docdir}/%{package_name}/
%fdupes -s examples

%cmake_install

%fdupes -s %{buildroot}%{_prefix}

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%{_libdir}/*.so.*

%files devel
%{_libdir}/cmake
%license COPYRIGHT LICENSE-APACHE LICENSE-MIT NOTICE
%doc CHANGELOG README.md INSTALL.md
%{_incdir}/%{pname}
%{_libdir}/*.so

%files doc
%{_docdir}/%{package_name}

%files examples
%doc src/examples

%changelog
