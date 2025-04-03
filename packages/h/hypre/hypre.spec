#
# spec file for package hypre
#
# Copyright (c) 2025 SUSE LLC
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
Version:        2.20.0
%define somver 2_20_0
Release:        0
Summary:        Scalable algorithms for solving linear systems of equations
License:        Apache-2.0 OR MIT
Group:          Productivity/Scientific/Math
URL:            https://www.llnl.gov/casc/hypre/
Source:         https://github.com/hypre-space/hypre/archive/v%{version}.tar.gz#/hypre-%{version}.tar.gz
Patch0:         hypre_Makefile_examples.patch
Patch1:         Add-library-version.patch

# TODO : add babel
#BuildRequires:  babel-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  superlu-devel
%if 0%{?with mpi}
BuildRequires:  %{mpi_family}%{?mpi_ext}-devel
%endif
BuildRequires:  cmake
BuildRequires:  fdupes
# Default library install path

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
BuildRequires:  texlive-bibtex
BuildRequires:  texlive-latex-bin-bin
BuildRequires:  texlive-xypic

%description    doc
This package contains development documentation for Hypre.

%prep
%autosetup -p0 -n %{pname}-%{version}

cat > %{_sourcedir}/baselibs.conf  <<EOF
%{libname}
%{libname}-devel
  requires %{?_suffix}-<targettype>
  requires "%{libname}-<targettype> = <version>"
EOF

%build
%{?with_mpi: . %{my_bindir}/mpivars.sh}

export LDFLAGS="-lm"

cd src/
%cmake \
       -DHYPRE_SHARED=ON \
       %if %{without mpi}
       -DHYPRE_WITH_MPI=OFF \
       %else
       -DHYPRE_WITH_MPI=ON \
       %endif
       -DHYPRE_USING_HYPRE_BLAS=OFF \
       -DHYPRE_USING_HYPRE_LAPACK=OFF \
       -DCMAKE_SHARED_LINKER_FLAGS="-lm"

%make_jobs

%install
cd src/
install -m 644 -D docs/usr-manual/*pdf -t %{buildroot}%{_docdir}/%{package_name}/
%fdupes -s examples

%cmake_install

%fdupes -s %{buildroot}%{_prefix}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

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
