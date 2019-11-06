#
# spec file for package parallel-netcdf
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define pname parallel-netcdf
%define sonum 1
%define libname libpnetcdf

%if "%{flavor}" == ""
ExclusiveArch: do_not_build
%endif

%if "%{flavor}" == "openmpi1" && 0%{?suse_version} < 1550
%define mpi_flavor  openmpi
%else
%define mpi_flavor  %{flavor}
%endif

%if "%{?mpi_flavor}" != ""
%define my_suffix  -%{mpi_flavor}
%define mpiprefix %{_libdir}/mpi/gcc/%{mpi_flavor}
%define my_prefix %{mpiprefix}
%define my_bindir %{mpiprefix}/bin
%define my_libdir %{mpiprefix}/%{_lib}
%define my_includedir %{mpiprefix}/include
%endif

Name:           %{pname}%{?my_suffix}
Version:        1.7.0
Release:        0
Summary:        High-performance parallel I/O with the NetCDF scientific data format
License:        NetCDF
Group:          Productivity/Scientific/Other
Url:            http://cucis.ece.northwestern.edu/projects/PnetCDF/index.html
Source0:        http://cucis.ece.northwestern.edu/projects/PnetCDF/Release/%{pname}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE parallel-netcdf-1.6.1-destdir.patch Fix install directories
Patch0:         parallel-netcdf-1.6.1-destdir.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  pkg-config
BuildRequires:  %{mpi_flavor}-devel
Requires:       %{mpi_flavor}
Requires:       %{libname}%{sonum}%{?my_suffix} = %{version}

%description
NetCDF is a set of software libraries and self-describing, 
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

Parallel netCDF (PnetCDF) is a library providing high-performance I/O while
still maintaining file-format compatibility with Unidata's NetCDF.

This package contains the %{mpi_flavor} version of utility functions for
working with NetCDF files.

%package -n %{libname}%{sonum}%{my_suffix}
Summary:        High-performance parallel I/O with the NetCDF scientific data format
Group:          System/Libraries

%description -n %{libname}%{sonum}%{my_suffix}
NetCDF is a set of software libraries and data formats for array-oriented
scientific data.

Parallel netCDF (PnetCDF) maintains file-format compatibility with NetCDF.

This package contains the %{mpi_flavor} version of the PnetCDF runtime
libraries.

%package -n %{pname}-devel-data
Summary:        Development data files for %{name}
Group:          Development/Libraries/Parallel
BuildArch:      noarch

%description -n %{pname}-devel-data
NetCDF is a set of software libraries and data formats for array-oriented
scientific data.

Parallel netCDF (PnetCDF) maintains file-format compatibility with NetCDF.

This package contains generic files needed to create projects that use
any version of PnetCDF.

%package devel
Summary:        Development files for %{name}%{?my_suffix}
Group:          Development/Libraries/Parallel
Requires:       %{libname}%{sonum}%{?my_suffix} = %{version}
Requires:       %{mpi_flavor}-devel
Requires:       %{pname}-devel-data

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

%description devel-static
NetCDF is a set of software libraries and data formats for array-oriented
scientific data.

Parallel netCDF (PnetCDF) maintains file-format compatibility with NetCDF.

This package contains the %{mpi_flavor} versions of the static libraries 
for PnetCDF.

%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1


%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%configure --prefix=%{my_prefix} \
           --libdir=%{my_libdir} \
           --with-mpi=%{my_prefix}
make

mkdir shared
pushd shared
%{my_bindir}/mpif77 -shared -Wl,-soname=%{libname}.so.%{sonum} -o ../%{libname}.so.%{version}
popd


%install
%make_install

%if %{_lib} != lib
mv %{buildroot}%{my_prefix}/lib %{buildroot}%{my_libdir}
%endif

install -m 755 %{libname}.so.%{version} %{buildroot}%{my_libdir}
pushd %{buildroot}%{my_libdir}
ln -s %{libname}.so.%{version} %{libname}.so.%{sonum}
ln -s %{libname}.so.%{version} %{libname}.so
popd

find %{buildroot} -name '*.la' -delete

%if "%{flavor}" == "openmpi1"
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

%post -n %{libname}%{sonum}%{?my_suffix} -p /sbin/ldconfig
%postun -n %{libname}%{sonum}%{?my_suffix} -p /sbin/ldconfig

%if "%{flavor}" == "openmpi1"
%files -n %{pname}-devel-data
%defattr(-,root,root)
%{_rpmmacrodir}/macros.pnetcdf
%endif

%files
%defattr(-,root,root)
%{my_bindir}/*
%dir %{my_prefix}/man/
%{my_prefix}/man/*

%files -n %{libname}%{sonum}%{?my_suffix}
%defattr(-,root,root)
%license COPYRIGHT
%doc CREDITS RELEASE_NOTES
%doc README README.LINUX README.large_files 
%{my_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{my_includedir}/*
%{my_libdir}/*.so
%{my_libdir}/pkgconfig/pnetcdf.pc

%files devel-static
%defattr(-,root,root)
%{my_libdir}/*.a

%changelog
