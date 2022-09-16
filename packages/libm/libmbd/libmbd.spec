#
# spec file for package libmbd
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
%global srcname libmbd

# SECTION MPI DEFINITIONS
%if "%{flavor}" == "mvapich2"
%global mpi_flavor mvapich2
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

Name:           %{srcname}%{?my_suffix}
Version:        0.12.6
Release:        0
Summary:        Many-body dispersion library
License:        MPL-2.0
URL:            https://github.com/libmbd/libmbd
Source:         %{url}/releases/download/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
%if %{with mpi}
BuildRequires:  %{mpi_flavor}%{?mpi_vers}-devel
BuildRequires:  scalapack%{?my_suffix}-devel
%if 0%{?suse_version} >= 1550 && "%{flavor}" != "mvapich2"
BuildRequires:  %{mpi_flavor}%{?mpi_vers}-config
%endif
%endif

%description
Libmbd implements the many-body dispersion (MBD) method in several programming
languages and frameworks. This is the reference implementation in Fortran and
C.

%package devel
Summary:        Many-body dispersion library -- headers and sources
Requires:       %{name} = %{version}
%if %{with mpi}
Requires:       scalapack%{?my_suffix}-devel
%endif

%description devel
Libmbd implements the many-body dispersion (MBD) method in several programming
languages and frameworks. This is the reference implementation in Fortran and
C.

This package provides the files needed for developing against %{name}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%if %{with mpi}
source %{my_bindir}/mpivars.sh
%endif

%cmake -DCMAKE_INSTALL_PREFIX:PATH=%{my_prefix}                     \
       -DCMAKE_PREFIX_PATH:PATH=%{my_prefix}                        \
       -DCMAKE_INSTALL_LIBDIR:PATH=%{my_libdir}                     \
       -DENABLE_SCALAPACK_MPI:BOOL=%{?with_mpi:ON}%{!?with_mpi:OFF} \
       -DSCALAPACK_LIBRARY:PATH=%{my_libdir}/libscalapack.so        \
       %{nil}
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{my_libdir}/libmbd.so

%files devel
%license LICENSE
%doc README.md
%{my_incdir}/mbd
%if %{with mpi}
%dir %{my_libdir}/cmake
%endif
%{my_libdir}/cmake/mbd/

%changelog
