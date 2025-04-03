#
# spec file for package pnetcdf
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


%global flavor @BUILD_FLAVOR@%{nil}

%define pname pnetcdf
%define sonum 4
%define libname libpnetcdf

# no burst buffering
%bcond_with b_buff

ExcludeArch:    s390 s390x i586

%if "%{flavor}" == ""
%define build_doc 1
%else
%define mpi_flavor %{flavor}
%endif

%if "%{flavor}" == "openmpi5"
ExcludeArch:    %{ix86} %{arm}
%endif

%global _defaultlicensedir %{expand:%_defaultlicensedir}
%if 0%{?!build_doc:1}
%define my_suffix  -%{mpi_flavor}
%else
# for 'configure' provide an MPI flavor
%define mpi_flavor openmpi5
%endif

%define package_name %{pname}%{?my_suffix}
%define lib_name %{libname}%{sonum}%{?my_suffix}
%global mpiprefix %{_libdir}/mpi/gcc/%{mpi_flavor}
%define _prefix %{mpiprefix}
%define _bindir %{mpiprefix}/bin
%define _libdir %{mpiprefix}/%{_lib}
%define _includedir %{mpiprefix}/include
%define _mandir %{mpiprefix}/man

Name:           %package_name
Version:        1.12.3
Release:        0
Summary:        High-performance parallel I/O with the NetCDF scientific data format
License:        NetCDF
Group:          Productivity/Scientific/Other
URL:            https://parallel-netcdf.github.io/
Source0:        https://parallel-netcdf.github.io/Release/%{pname}-%{version}.tar.gz
BuildRequires:  bison
%if 0%{?build_doc}
BuildRequires:  doxygen
BuildRequires:  ghostscript
BuildRequires:  texlive-collection-latex
%endif
BuildRequires:  flex
BuildRequires:  pkg-config
Requires:       %{lib_name} = %{version}
BuildRequires:  %{mpi_flavor}-devel
%if 0%{?!build_doc:1}
Requires:       %{mpi_flavor}
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
%endif
#BuildRequires:  mpi-selector
Provides:       parallel-netcdf%{?my_suffix}

%description
NetCDF is a set of software libraries and self-describing,
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

Parallel netCDF (PnetCDF) is a library providing high-performance I/O while
still maintaining file-format compatibility with NetCDF by Unidata.

This package contains the %{mpi_flavor} version of utility functions for
working with NetCDF files.

%package -n %{lib_name}
Summary:        High-performance parallel I/O with the NetCDF scientific data format
# Unversioned provides to allow e.g. netcdf to pull in pnetcdf with the
# same flavor
Group:          System/Libraries
Provides:       %{libname}%{my_suffix}

%description -n %{lib_name}
NetCDF is a set of software libraries and data formats for array-oriented
scientific data.

Parallel netCDF (PnetCDF) maintains file-format compatibility with NetCDF.

This package contains the %{mpi_flavor} version of the PnetCDF runtime
libraries.

%package -n %{pname}-devel-data
Summary:        Development data files for %{name}
Group:          Development/Libraries/Parallel
BuildArch:      noarch
Provides:       parallel-netcdf%{?my_suffix}-devel-data

%description -n %{pname}-devel-data
NetCDF is a set of software libraries and data formats for array-oriented
scientific data.

Parallel netCDF (PnetCDF) maintains file-format compatibility with NetCDF.

This package contains generic files needed to create projects that use
any version of PnetCDF.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Parallel
Requires:       %{lib_name} = %{version}
%if 0%{?!build_doc:1}
Requires:       %{mpi_flavor}-devel
%endif
Requires:       %{pname}-devel-data
Provides:       parallel-netcdf%{?my_suffix}-devel

%description devel
NetCDF is a set of software libraries and data formats for array-oriented
scientific data.

Parallel netCDF (PnetCDF) maintains file-format compatibility with NetCDF.

This package contains all files needed to create projects that use
the %{mpi_flavor} version of PnetCDF.

%package devel-static
Summary:        Static development files for %{name}
Group:          Development/Libraries/Parallel
Requires:       %{name}-devel = %{version}
Provides:       parallel-netcdf%{?my_suffix}-devel-static

%description devel-static
NetCDF is a set of software libraries and data formats for array-oriented
scientific data.

Parallel netCDF (PnetCDF) maintains file-format compatibility with NetCDF.

This package contains the %{mpi_flavor} versions of the static libraries for
PnetCDF.

%package doc
Summary:        Documentation for %{pname}
Group:          Documentation/Other
BuildArch:      noarch

%description doc
NetCDF is a set of software libraries and data formats for array-oriented
scientific data.

Parallel netCDF (PnetCDF) maintains file-format compatibility with NetCDF.

This package contains the documentation for PnetCDF.

%prep
%setup -q -n %{pname}-%{version}

%build
%if 0%{?!build_doc:1}
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export FCFLAGS="%{optflags}"
export FFLAGS="%{optflags}"

source %{_bindir}/mpivars.sh
%configure --prefix=%{_prefix} \
           --libdir=%{_libdir} \
	   --enable-shared \
	   %{?with_b_buff:--enable-burst-buffering} \
           --with-mpi=%{_prefix}

%make_build
# Build tests without executing
%make_build check TESTS=""

mkdir shared
pushd shared
popd

%else
PATH=%_bindir:$PATH
%configure  --enable-doxygen
%make_build -C doc/pnetcdf-api
%endif

%install
%make_install %{?build_doc:-C doc/pnetcdf-api}

%if 0%{?!build_doc:1}
pushd %{buildroot}%{_libdir}
popd

find %{buildroot} -name '*.la' -delete

%if "%{flavor}" == "openmpi4"
# rpm macro for version checking
mkdir -p %{buildroot}%{_rpmmacrodir}
cat > %{buildroot}%{_rpmmacrodir}/macros.pnetcdf <<EOF
#
# RPM macros for hdf5 packaging
#
%_pnetcdf_sonum  %{sonum}
%_pnetcdf_version  %{version}
EOF
%endif
%endif

%if 0%{?!build_doc:1}
%check
source %{_bindir}/mpivars.sh
%make_build check

%post -n %{lib_name}
/sbin/ldconfig -N %{_libdir}

%postun -n %{lib_name}
/sbin/ldconfig -N %{_libdir}

%if "%{flavor}" == "openmpi4"
%files -n %{pname}-devel-data
%{_rpmmacrodir}/macros.pnetcdf
%endif

%files
%{_bindir}/*
%dir %{_mandir}
%{_mandir}/*

%files -n %{lib_name}
%license COPYRIGHT COPYING
%doc CREDITS RELEASE_NOTES AUTHORS
%doc README
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/pnetcdf.pc

%files devel-static
%{_libdir}/*.a

%else

%files doc
%doc doc/pnetcdf-api/pnetcdf-api.pdf
%doc doc/README.consistency doc/README.large_files %{?with_b_buff:doc/README.burst_buffering}

%endif

%changelog
