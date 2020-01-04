#
# spec file for package arpack-ng
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

Name:           %{pkgname}
Version:        3.7.0
Release:        0
Summary:        Fortran77 subroutines for solving large scale eigenvalue problems
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://github.com/opencollab/arpack-ng
Source0:        https://github.com/opencollab/arpack-ng/archive/%{version}.tar.gz
%if %{with mpi}
BuildRequires:  %{mpi_family}%{?mpi_ext}-devel
%endif
BuildRequires:  autoconf
BuildRequires:  blas-devel
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  libtool
BuildRequires:  pkg-config

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

%prep
%setup -q -n arpack-ng-%{version}

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
export F77=%{my_prefix}/bin/mpif77
export MPIF77=%{my_prefix}/bin/mpif77
export LD_LIBRARY_PATH=%{my_prefix}/%{_lib}
%endif

%global orig_prefix %{_prefix}
%define _prefix %{my_prefix}
sh bootstrap
%configure --disable-static \
	   %{?with_mpi: --enable-mpi} \
	   %{nil}
%define _prefix %{orig_prefix}
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

# Remove sequential version files
%if %{with mpi}
rm -Rf %{buildroot}%{my_libdir}/pkgconfig
rm %{buildroot}%{my_libdir}/libarpack.so*
%endif

ln -s EXAMPLES examples

%check
%if %{with mpi}
export PATH="%{my_prefix}/bin/:$PATH"
%endif
%make_build check

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
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*.pc
%endif

%changelog
