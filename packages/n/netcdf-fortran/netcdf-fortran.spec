#
# spec file for package netcdf-fortran
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

%define _do_check 1

%global pname netcdf-fortran
%global ver 4.5.2
%global _ver 4_5_2

%if 0%{?sle_version} >= 150200
%define DisOMPI1 ExclusiveArch:  do_not_build
%endif
%if !0%{?is_opensuse} && 0%{?sle_version:1}
 %if 0%{?sle_version} < 150200
  %define DisOMPI3 ExclusiveArch:  do_not_build
 %endif
 %if 0%{?sle_version} < 150300
  %define DisOMPI4 ExclusiveArch:  do_not_build
 %endif
%endif

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%define package_name %pname
%define compiler_family gnu
%endif

ExcludeArch:    s390 s390x

%{bcond_with staticlibs}

%if "%flavor" == "gnu-hpc"
%global compiler_family gnu
%{bcond_with mpi}
%endif

%if "%flavor" == "gnu-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 1
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu-openmpi2-hpc"
%{?DisOMPI2}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 2
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 3
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu-openmpi4-hpc"
%{?DisOMPI4}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 4
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu-mvapich2-hpc"
%global compiler_family gnu
%global mpi_flavor mvapich2
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu-mpich-hpc"
%global compiler_family gnu
%global mpi_flavor mpich
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu7-hpc"
%global compiler_family gnu
%{bcond_with mpi}
%global c_f_ver 7
%endif

%if "%flavor" == "gnu7-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 1
%global c_f_ver 7
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu7-openmpi2-hpc"
%{?DisOMPI2}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 2
%global c_f_ver 7
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu7-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 3
%global c_f_ver 7
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu7-openmpi4-hpc"
%{?DisOMPI4}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 4
%global c_f_ver 7
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu7-mvapich2-hpc"
%global compiler_family gnu
%global mpi_flavor mvapich2
%global c_f_ver 7
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu7-mpich-hpc"
%global compiler_family gnu
%global mpi_flavor mpich
%global c_f_ver 7
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu8-hpc"
%global compiler_family gnu
%{bcond_with mpi}
%global c_f_ver 8
%endif

%if "%flavor" == "gnu8-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 1
%global c_f_ver 8
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu8-openmpi2-hpc"
%{?DisOMPI2}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 2
%global c_f_ver 8
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu8-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 3
%global c_f_ver 8
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu8-openmpi4-hpc"
%{?DisOMPI4}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 4
%global c_f_ver 8
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu8-mvapich2-hpc"
%global compiler_family gnu
%global mpi_flavor mvapich2
%global c_f_ver 8
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu8-mpich-hpc"
%global compiler_family gnu
%global mpi_flavor mpich
%global c_f_ver 8
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu9-hpc"
%global compiler_family gnu
%{bcond_with mpi}
%global c_f_ver 9
%endif

%if "%flavor" == "gnu9-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 1
%global c_f_ver 9
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu9-openmpi2-hpc"
%{?DisOMPI2}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 2
%global c_f_ver 9
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu9-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 3
%global c_f_ver 9
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu9-openmpi4-hpc"
%{?DisOMPI4}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 4
%global c_f_ver 9
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu9-mvapich2-hpc"
%global compiler_family gnu
%global mpi_flavor mvapich2
%global c_f_ver 9
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu9-mpich-hpc"
%global compiler_family gnu
%global mpi_flavor mpich
%global c_f_ver 9
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu10-hpc"
%global compiler_family gnu
%{bcond_with mpi}
%global c_f_ver 10
%endif

%if "%flavor" == "gnu10-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 1
%global c_f_ver 10
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu10-openmpi2-hpc"
%{?DisOMPI2}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 2
%global c_f_ver 10
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu10-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 3
%global c_f_ver 10
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu10-openmpi4-hpc"
%{?DisOMPI4}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 4
%global c_f_ver 10
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu10-mvapich2-hpc"
%global compiler_family gnu
%global mpi_flavor mvapich2
%global c_f_ver 10
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu10-mpich-hpc"
%global compiler_family gnu
%global mpi_flavor mpich
%global c_f_ver 10
%{bcond_without mpi}
%endif

%define limit_cores(c:) %{?_smp_mflags: %(a=1;
              b=$(sed -se "s/.*-j[[:space:]]*\\([[:digit:]]\\+\\).*/\\1/" <<< %_smp_mflags);
              [ $b -le $a ] || b=$a ;
              sed -se "s/\\(.*-j[[:space:]]*\\)[[:digit:]]\\+\\(.*\\)/\\1$b/" <<< %_smp_mflags )}

%define hpc_upcase_trans_hyph() %(echo %{**} | tr [a-z] [A-Z] | tr '-' '_')

%{?hpc_init:%{hpc_init -c %compiler_family %{?c_f_ver:-v %{c_f_ver}} %{?with_mpi:-m %mpi_flavor %{?mpi_ver:-V %mpi_ver}}}}
%{!?hpc_package_name_tail:%define hpc_package_name_tail %{nil}}

%if 0%{!?package_name:1}
%define package_name %{hpc_package_name %_ver}
%endif

Name:           %package_name
%define libname libnetcdf-fortran
Summary:        Command-line programs for the NetCDF scientific data format
License:        NetCDF
Group:          Productivity/Scientific/Other
Version:        %ver
Release:        0
%define sonum   7
URL:            https://www.unidata.ucar.edu/software/netcdf/
Source:         https://github.com/Unidata/netcdf-fortran/archive/v%{version}.tar.gz#/%{pname}-%{version}.tar.gz
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  %{compiler_family}-compilers-hpc
BuildRequires:  gawk
BuildRequires:  libcurl-devel >= 7.18.0
BuildRequires:  lua-lmod
BuildRequires:  m4
BuildRequires:  pkg-config
BuildRequires:  suse-hpc
BuildRequires:  zlib-devel >= 1.2.5
%if %{with mpi}
BuildRequires:  %{mpi_flavor}%{?mpi_ver}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
%endif
BuildRequires:  hdf5-%{compiler_family}%{?c_f_ver}%{?with_mpi:-%{mpi_flavor}%{?mpi_ver}}-hpc-devel
BuildRequires:  netcdf-%{compiler_family}%{?c_f_ver}%{?with_mpi:-%{mpi_flavor}%{?mpi_ver}}-hpc-devel >= 4.6.2
Requires:       %{libname}%{hpc_package_name_tail %_ver} = %{version}

%description
NetCDF is a set of software libraries and self-describing, 
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

%if %{without mpi}
This package contains utility functions for working with NetCDF files.
%else
This package contains the %{mpi_flavor} version of utility functions for
working with NetCDF files.
%endif

%{hpc_master_package}

%package -n     %{libname}%{hpc_package_name_tail %_ver}
Summary:        Shared libraries for the NetCDF scientific data format
Group:          System/Libraries
%{?hpc_requires}
Requires:       libnetcdf-%{compiler_family}%{?c_f_ver}%{?with_mpi:-%{mpi_flavor}%{?mpi_ver}}-hpc

%description -n %{libname}%{hpc_package_name_tail %_ver}
NetCDF is a set of software libraries and self-describing, 
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

NetCDF (network Common Data Form) is an interface for array-oriented
data access and a collection of software libraries
for C, Fortran, C++, and Perl that provides an implementation of the
interface. The NetCDF library also defines a machine-independent
format for representing scientific data. Together, the interface,
library, and format support the creation, access, and sharing of
scientific data.

NetCDF data is:
   - Self-Describing: A NetCDF file includes information about the
     data it contains.
   - Network-transparent:  A NetCDF file is represented in a form that
     can be accessed by computers with different ways of storing
     integers, characters, and floating-point numbers.
   - Direct-access:  A small subset of a large dataset may be accessed
     efficiently, without first reading through all the preceding
     data.
   - Appendable:  Data can be appended to a NetCDF dataset along one
     dimension without copying the dataset or redefining its
     structure. The structure of a NetCDF dataset can be changed,
     though this sometimes causes the dataset to be copied.
   - Sharable:  One writer and multiple readers may simultaneously
     access the same NetCDF file.

This package contains all files needed to create projects that use
%{?mpi_flavor:the %mpi_flavor version of} NetCDF.

%{hpc_master_package -l -L -n %{libname}%{hpc_package_name_tail}}

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Parallel
Requires:       %{libname}%{hpc_package_name_tail %_ver} = %{version}
Requires:       libcurl-devel >= 7.18.0
Requires:       pkgconfig
Requires:       zlib-devel >= 1.2.5
%{?hpc_requires_devel}
Requires:       netcdf-%{compiler_family}%{?c_f_ver}%{?with_mpi:-%{mpi_flavor}%{?mpi_ver}}-hpc-devel

%description devel
NetCDF is a set of software libraries and self-describing, 
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

This package contains all files needed to create projects that use
%{?mpi_flavor:the %mpi_flavor version of} NetCDF.

%{hpc_master_package devel}

%package devel-static
Summary:        Static development files for %{name}
Group:          Development/Libraries/Parallel
Requires:       %{name}-devel = %{version}
#Requires:       hdf-devel
Requires:       hdf5-%{compiler_family}%{?c_f_ver}%{?with_mpi:-%{mpi_flavor}%{?mpi_ver}}-hpc-devel >= 1.8.8
Requires:       libcurl-devel >= 7.18.0
Requires:       zlib-devel >= 1.2.5

%description devel-static
NetCDF is a set of software libraries and self-describing, 
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

This package contains the static libraries for 
%{?mpi_flavor:the %mpi_flavor version of} NetCDF.

%prep
%setup -q -n %{pname}-%{version}

# Fix spurious-executable-perm RPMLINT warning
chmod a-x RELEASE_NOTES.md

%build
%{?_lto_cflags: %global _lto_cflags %{?_lto_cflags} -ffat-lto-objects}
%{?with_staticlibs:%{?_smp_mflags:%global _smp_mflags %{limit_cores -c 8}}}
%{hpc_setup}
module load netcdf
export CFLAGS="%{optflags} -I $NETCDF_INC -L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"
export FCFLAGS="%{optflags} -std=legacy"
export FFLAGS=$FCFLAGS
export CPPFLAGS=$CFLAGS
export LDFLAGS="-L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"

%if %{with mpi}
export CC="mpicc"
export FC="mpif90"
export F77="mpif77"
%endif
%hpc_configure \
    --enable-shared \
    --with-pic \
    --disable-doxygen \
%if %{with staticlibs}
    --enable-static
%else
    --disable-static
%endif

make %{?_smp_mflags}

%install
%{hpc_setup}
module load netcdf
export CFLAGS="%{optflags} -I $NETCDF_INC -L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"
export FCFLAGS="%{optflags}"
export CPPFLAGS=$CFLAGS
export LDFLAGS="-L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"
%if %{with mpi}
export CC="mpicc"
export FC="mpif90"
export F77="mpif77"
%endif

make install DESTDIR="%{buildroot}"

rm -f %{buildroot}%{hpc_libdir}/*.la

mv %{buildroot}%{hpc_bindir}/nf-config %{buildroot}%{hpc_bindir}/nf-fortran-config

%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the NetCDF Fortran API built with the %{compiler_family} compiler toolchain."
puts stderr " "
puts stderr "Note that this build of NetCDF leverages the HDF I/O library and requires linkage"
puts stderr "against hdf5 and the native C NetCDF library. Consequently, phdf5 and the standard C"
puts stderr "version of NetCDF are loaded automatically via this module. A typical compilation"
puts stderr "example for Fortran applications requiring NetCDF is as follows:"
puts stderr " "
puts stderr "\\\$FC  -I\\\$NETCDF_FORTRAN_INC app.f90 -L\\\$NETCDF_FORTRAN_LIB -lnetcdff -L\\\$NETCDF_LIB -lnetcdf -L\\\$HDF5_LIB -lhdf5"

puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{hpc_upcase %pname} built with %{compiler_family} toolchain %{mpi_flavor: and %{mpi_flavor}}"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{SUMMARY:0}"
module-whatis "%{url}"

# Require generic netcdf

if [ expr [ module-info mode load ] || [module-info mode display ] ] {
    if {  ![is-loaded netcdf]  } {
        module load netcdf
    }
}

set             version             %{version}

prepend-path    PATH                %{hpc_bindir}
prepend-path    MANPATH             %{hpc_mandir}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}

setenv          %{hpc_upcase_trans_hyph %pname}_DIR        %{hpc_prefix}
if {[file isdirectory  %{hpc_bindir}]} {
setenv          %{hpc_upcase_trans_hyph %pname}_BIN        %{hpc_bindir}
}
if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    LIBRARY_PATH        %{hpc_libdir}
prepend-path    CPATH               %{hpc_includedir}
prepend-path    C_INCLUDE_PATH      %{hpc_includedir}
prepend-path    CPLUS_INCLUDE_PATH  %{hpc_includedir}
prepend-path    INCLUDE                         %{hpc_includedir}
%hpc_modulefile_add_pkgconfig_path

setenv          %{hpc_upcase_trans_hyph %pname}_LIB        %{hpc_libdir}
setenv          %{hpc_upcase_trans_hyph %pname}_INC        %{hpc_includedir}
}
EOF

%if %_do_check
%check
%{hpc_setup}
    module load netcdf
export CFLAGS="-I $NETCDF_INC -L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"
export CPPFLAGS=$CFLAGS
export LDFLAGS="-L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"
%if 0%{with mpi}
export CC="mpicc"
export FC="mpif90"
export F77="mpif77"
%endif
    make check
%endif

%post -n %{libname}%{hpc_package_name_tail %_ver}
/sbin/ldconfig -N %{hpc_libdir}

%postun -n %{libname}%{hpc_package_name_tail %_ver} 
/sbin/ldconfig -N %{hpc_libdir}
%hpc_module_delete_if_default

%files
%doc COPYRIGHT README.md RELEASE_NOTES.md
%{hpc_bindir}/

%files -n %{libname}%{hpc_package_name_tail %_ver}
%{hpc_dirs}
%{hpc_modules_files}
%{hpc_libdir}/libnetcdff.so.*

%files devel
%{hpc_includedir}/
%dir %{hpc_pkgconfigdir}
%{hpc_libdir}/pkgconfig/netcdf-fortran.pc
%{hpc_libdir}/*.so
%dir %{hpc_datadir}
%dir %{hpc_mandir}
%{hpc_mandir}/man3/

%if %{with staticlibs}
%files devel-static
%{hpc_libdir}/libnetcdff.a
%endif

%changelog
