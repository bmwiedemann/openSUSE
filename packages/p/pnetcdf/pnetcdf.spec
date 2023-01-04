#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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
%define ver 1.12.3
%define _ver 1_12_3
%define sonum 4
%define libname libpnetcdf
# no burst buffering
%bcond_with b_buff

ExcludeArch:    s390 s390x i586

%if !0%{?is_opensuse} && 0%{?sle_version:1}
 %if 0%{?sle_version} < 150100
  %define DisOMPI3 ExclusiveArch:  do_not_build
 %endif
 %if 0%{?sle_version} < 150200
  %define DisOMPI4 ExclusiveArch:  do_not_build
 %endif
%endif

%if "%{flavor}" == ""
%define build_doc 1
%endif

%if "%{flavor}" == "mvapich2"
%define mpi_flavor mvapich2
%bcond_with hpc
%endif

%if "%{flavor}" == "mpich"
%define mpi_flavor mpich
%bcond_with hpc
%endif

%if "%{flavor}" == "openmpi1"
%{?DisOMPI1}
%define mpi_flavor openmpi
%define mpi_ver 1
%bcond_with hpc
%endif

%if "%{flavor}" == "openmpi2"
%{?DisOMPI2}
%define mpi_flavor openmpi
%define mpi_ver 2
%bcond_with hpc
%endif

%if "%{flavor}" == "openmpi3"
%{?DisOMPI3}
%define mpi_flavor openmpi
%define mpi_ver 3
%bcond_with hpc
%endif

%if "%{flavor}" == "openmpi4"
%{?DisOMPI4}
%define mpi_flavor openmpi
%define mpi_ver 4
%bcond_with hpc
%endif

%if "%{flavor}" == "doc-hpc"
%bcond_without hpc
%define build_doc 1
%endif

%if "%{flavor}" == "gnu-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%undefine c_f_ver
%define mpi_flavor openmpi
%define mpi_ver 1
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu-openmpi2-hpc"
%{?DisOMPI2}
%global compiler_family gnu
%undefine c_f_ver
%define mpi_flavor openmpi
%define mpi_ver 2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%undefine c_f_ver
%define mpi_flavor openmpi
%define mpi_ver 3
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu-openmpi4-hpc"
%{?DisOMPI4}
%global compiler_family gnu
%undefine c_f_ver
%define mpi_flavor openmpi
%define mpi_ver 4
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu-mvapich2-hpc"
%global compiler_family gnu
%undefine c_f_ver
%define mpi_flavor mvapich2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu-mpich-hpc"
%global compiler_family gnu
%undefine c_f_ver
%define mpi_flavor mpich
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-hpc"
%global compiler_family gnu
%define c_f_ver 7
%undefine mpi_flavor
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%define c_f_ver 7
%define mpi_flavor openmpi
%define mpi_ver 1
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-openmpi2-hpc"
%{?DisOMPI2}
%global compiler_family gnu
%define c_f_ver 7
%define mpi_flavor openmpi
%define mpi_ver 2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%define c_f_ver 7
%define mpi_flavor openmpi
%define mpi_ver 3
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-openmpi4-hpc"
%{?DisOMPI4}
%global compiler_family gnu
%define c_f_ver 7
%define mpi_flavor openmpi
%define mpi_ver 4
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-mvapich2-hpc"
%global compiler_family gnu
%define c_f_ver 7
%define mpi_flavor mvapich2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-mpich-hpc"
%global compiler_family gnu
%define c_f_ver 7
%define mpi_flavor mpich
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu8-hpc"
%global compiler_family gnu
%define c_f_ver 8
%undefine mpi_flavor
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu8-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%define c_f_ver 8
%define mpi_flavor openmpi
%define mpi_ver 1
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu8-openmpi2-hpc"
%{?DisOMPI2}
%global compiler_family gnu
%define c_f_ver 8
%define mpi_flavor openmpi
%define mpi_ver 2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu8-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%define c_f_ver 8
%define mpi_flavor openmpi
%define mpi_ver 3
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu8-openmpi4-hpc"
%{?DisOMPI4}
%global compiler_family gnu
%define c_f_ver 8
%define mpi_flavor openmpi
%define mpi_ver 4
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu8-mvapich2-hpc"
%global compiler_family gnu
%define c_f_ver 8
%define mpi_flavor mvapich2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu8-mpich-hpc"
%global compiler_family gnu
%define c_f_ver 8
%define mpi_flavor mpich
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu9-hpc"
%global compiler_family gnu
%define c_f_ver 9
%undefine mpi_flavor
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu9-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%define c_f_ver 9
%define mpi_flavor openmpi
%define mpi_ver 1
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu9-openmpi2-hpc"
%{?DisOMPI2}
%global compiler_family gnu
%define c_f_ver 9
%define mpi_flavor openmpi
%define mpi_ver 2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu9-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%define c_f_ver 9
%define mpi_flavor openmpi
%define mpi_ver 3
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu9-openmpi4-hpc"
%{?DisOMPI4}
%global compiler_family gnu
%define c_f_ver 9
%define mpi_flavor openmpi
%define mpi_ver 4
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu9-mvapich2-hpc"
%global compiler_family gnu
%define c_f_ver 9
%define mpi_flavor mvapich2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu9-mpich-hpc"
%global compiler_family gnu
%define c_f_ver 9
%define mpi_flavor mpich
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu10-hpc"
%global compiler_family gnu
%define c_f_ver 10
%undefine mpi_flavor
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu10-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%define c_f_ver 10
%define mpi_flavor openmpi
%define mpi_ver 1
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu10-openmpi2-hpc"
%{?DisOMPI2}
%global compiler_family gnu
%define c_f_ver 10
%define mpi_flavor openmpi
%define mpi_ver 2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu10-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%define c_f_ver 10
%define mpi_flavor openmpi
%define mpi_ver 3
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu10-openmpi4-hpc"
%{?DisOMPI4}
%global compiler_family gnu
%define c_f_ver 10
%define mpi_flavor openmpi
%define mpi_ver 4
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu10-mvapich2-hpc"
%global compiler_family gnu
%define c_f_ver 10
%define mpi_flavor mvapich2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu10-mpich-hpc"
%global compiler_family gnu
%define c_f_ver 10
%define mpi_flavor mpich
%bcond_without hpc
%endif

%if "%{mpi_flavor}" != "openmpi" || "%{mpi_ver}" != "1" || 0%{?suse_version} >= 1550
%define mpi_ext %{?mpi_ver}
%endif

%if 0%{?!build_doc:1} && (0%{?!mpi_flavor:1}||(0%{?with_hpc:1} && 0%{?!compiler_family:1}))
%{error: Unknown build flavor!}
ExclusiveArch:  do_not_build
%endif

%global _defaultlicensedir %{expand:%_defaultlicensedir}
%if %{without hpc}
%if 0%{?!build_doc:1}
%define my_suffix  -%{mpi_flavor}%{?mpi_ext}
%else
# for 'configure' provide an MPI flavor
%define mpi_flavor mvapich2
%endif
%define package_name %{pname}%{?my_suffix}
%define lib_name %{libname}%{sonum}%{?my_suffix}
%global mpiprefix %{_libdir}/mpi/gcc/%{mpi_flavor}%{?mpi_ext}
%define _prefix %{mpiprefix}
%define _bindir %{mpiprefix}/bin
%define _libdir %{mpiprefix}/%{_lib}
%define _includedir %{mpiprefix}/include
%define _mandir %{mpiprefix}/man
%else
%{hpc_init %{?!build_doc:-c %compiler_family %{?c_f_ver:-v %{c_f_ver}} -m {%mpi_flavor} %{?mpi_ver:-V %{mpi_ver}} %{?ext:-e %{ext}}}}
%define package_name %{hpc_package_name %_ver}
%define lib_name lib%{pname}%{hpc_package_name_tail %_ver}
# fix hpc_base - remove after fixing in macros.hpc?
%global hpc_base %{expand:%hpc_base}
%if 0%{?!build_doc:1}
%define _prefix %hpc_prefix
%define _bindir %hpc_bindir
%define _libdir %hpc_libdir
%define _includedir %hpc_includedir
%define _mandir %hpc_mandir
%else
%define mpi_flavor mvapich2
%global mpiprefix %{_libdir}/mpi/gcc/%{mpi_flavor}%{?mpi_ext}
%define _prefix %{mpiprefix}
%endif
%endif

Name:           %package_name
Version:        %ver
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
%if %{without hpc}
BuildRequires:  %{mpi_flavor}%{?mpi_ext}-devel
%if 0%{?!build_doc:1}
Requires:       %{mpi_flavor}%{?mpi_ext}
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
%endif
#BuildRequires:  mpi-selector
Provides:       parallel-netcdf%{?my_suffix}
%else
%if 0%{?!build_doc:1}
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  %{mpi_flavor}%{?mpi_ver}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
BuildRequires:  lua-lmod
%else
BuildRequires:  %{mpi_flavor}%{?mpi_ext}-devel
%endif
BuildRequires:  suse-hpc
%endif

%description
NetCDF is a set of software libraries and self-describing,
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

Parallel netCDF (PnetCDF) is a library providing high-performance I/O while
still maintaining file-format compatibility with NetCDF by Unidata.

This package contains the %{mpi_flavor} version of utility functions for
working with NetCDF files.

%{?!build_doc:%{?with_hpc:%{hpc_master_package}}}

%package -n %{lib_name}
Summary:        High-performance parallel I/O with the NetCDF scientific data format
# Unversioned provides to allow e.g. netcdf to pull in pnetcdf with the
# same flavor
Group:          System/Libraries
%if %{without hpc}
Provides:       %{libname}%{my_suffix}
%else
%{hpc_requires}
%endif

%description -n %{lib_name}
NetCDF is a set of software libraries and data formats for array-oriented
scientific data.

Parallel netCDF (PnetCDF) maintains file-format compatibility with NetCDF.

This package contains the %{mpi_flavor} version of the PnetCDF runtime
libraries.

%{?!build_doc:%{?with_hpc:%{hpc_master_package -L -l}}}

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
%if %{without hpc}
%if 0%{?!build_doc:1}
Requires:       %{mpi_flavor}%{?mpi_ext}-devel
%endif
Requires:       %{pname}-devel-data
Provides:       parallel-netcdf%{?my_suffix}-devel
%else
%{hpc_requires_devel}
%endif

%description devel
NetCDF is a set of software libraries and data formats for array-oriented
scientific data.

Parallel netCDF (PnetCDF) maintains file-format compatibility with NetCDF.

This package contains all files needed to create projects that use
the %{mpi_flavor} version of PnetCDF.

%{?!build_doc:%{?with_hpc:%{hpc_master_package devel}}}

%package devel-static
Summary:        Static development files for %{name}
Group:          Development/Libraries/Parallel
Requires:       %{name}-devel = %{version}
%{?!with_hpc:Provides: parallel-netcdf%{?my_suffix}-devel-static}

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

%{?build_doc:%{?with_hpc:%{hpc_master_package doc}}}

%prep
%setup -q -n %{pname}-%{version}

%build
%if 0%{?!build_doc:1}
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export FCFLAGS="%{optflags}"
export FFLAGS="%{optflags}"

%if %{without hpc}
source %{_bindir}/mpivars.sh
%configure --prefix=%{_prefix} \
           --libdir=%{_libdir} \
	   --enable-shared \
	   %{?with_b_buff:--enable-burst-buffering} \
           --with-mpi=%{_prefix}
%else
%{hpc_setup}
# if these environment variables confuse the build
unset CC CXX F77 F90 FC
#sed -ie "s@#! /bin/sh@#! /bin/sh -x@" ./configure
%hpc_configure --with-mpi=$MPI_DIR --enable-shared \
	       %{?with_b_buff:--enable-burst-buffering}
%endif

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
 %if %{with hpc}
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{hpc_upcase %pname} library built with the %{compiler_flavor}"
puts stderr "toolchain and the %{mpi_flavor}%{?mpi_ver} MPI stack."
puts stderr " "
puts stderr "A typical compilation step for C applications requiring NetCDF is as follows:"
puts stderr " "
puts stderr "\\\$CC -I\\\$PNETCDF_INC app.c -L\\\$PNETCDF_LIB -lpnetcdf"

puts stderr "\nVersion %{version}\n"

module-whatis "Name: %{hpc_upcase %pname} built with %{compiler_family} toolchain compiler and %{mpi_flavor} MPI"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{SUMMARY:0}"
module-whatis "%{url}"

set             version             %{version}

prepend-path    PATH                %{hpc_bindir}
prepend-path    MANPATH             %{hpc_mandir}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}

setenv          %{hpc_upcase %pname}_DIR        %{hpc_prefix}
setenv          %{hpc_upcase %pname}_BIN        %{hpc_bindir}

if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    LIBRARY_PATH        %{hpc_libdir}
prepend-path    CPATH               %{hpc_includedir}
prepend-path    C_INCLUDE_PATH      %{hpc_includedir}
prepend-path    CPLUS_INCLUDE_PATH  %{hpc_includedir}
prepend-path    INCLUDE             %{hpc_includedir}
%hpc_modulefile_add_pkgconfig_path

setenv          %{hpc_upcase %pname}_LIB        %{hpc_libdir}
setenv          %{hpc_upcase %pname}_INC        %{hpc_includedir}

   }
}
EOF
 %endif
%endif

%if 0%{?!build_doc:1}
%check
%if %{without hpc}
source %{_bindir}/mpivars.sh
%else
%{hpc_setup}
%endif
%make_build check

%post -n %{lib_name}
/sbin/ldconfig -N %{_libdir}

%postun -n %{lib_name}
/sbin/ldconfig -N %{_libdir}
%{?with_hpc:%hpc_module_delete_if_default}

%if "%{flavor}" == "openmpi1"
%files -n %{pname}-devel-data
%{_rpmmacrodir}/macros.pnetcdf
%endif

%files
%{_bindir}%{?!with_hpc:/*}
%{?with_hpc:%dir %hpc_datadir}
%dir %{_mandir}
%{_mandir}/*

%files -n %{lib_name}
%license COPYRIGHT COPYING
%if %{with hpc}
%hpc_dirs
%hpc_modules_files
%endif
%doc CREDITS RELEASE_NOTES AUTHORS
%doc README
%{_libdir}/*.so.*

%files devel
%{_includedir}%{?!with_hpc:/*}
%{_libdir}/*.so
%{?with_hpc:%hpc_pkgconfig_file -n pnetcdf}
%{_libdir}/pkgconfig/pnetcdf.pc

%files devel-static
%{_libdir}/*.a

%else

%files doc
%doc doc/pnetcdf-api/pnetcdf-api.pdf
%doc doc/README.consistency doc/README.large_files %{?with_b_buff:doc/README.burst_buffering}

%endif

%changelog
