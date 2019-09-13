#
# spec file for package netcdf
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

%define _do_check 1

%global pname netcdf-fortran
%global ver 4.4.5
%global _ver 4_4_5

%if 0%{?is_opensuse} || 0%{?is_backports}
%undefine DisOMPI3
%else
%define DisOMPI3 ExclusiveArch:  do_not_build
%endif

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%define package_name %pname
%endif

ExcludeArch:    s390 s390x

%if "%flavor" == "gnu-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 1
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 3
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu-openmpi2-hpc"
%{?DisOMPI2}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 2
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

%if "%flavor" == "gnu7-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 1
%global c_f_ver 7
%{bcond_without mpi}
%endif

%if "%flavor" == "gnu7-openmpi3-hpc"
%{?DisOMPI2}
%global compiler_family gnu
%global mpi_flavor openmpi
%global mpi_ver 3
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

%define hpc_upcase_trans_hyph() %(echo %{**} | tr [a-z] [A-Z] | tr '-' '_')

%{?hpc_init:%{hpc_init -c %compiler_family %{?c_f_ver:-v %{c_f_ver}} %{?with_mpi:-m %mpi_flavor %{?mpi_ver:-V %mpi_ver}}}}

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
%define sonum   6
URL:            https://www.unidata.ucar.edu/software/netcdf/
Source:         https://github.com/Unidata/netcdf-fortran/archive/v%{version}.tar.gz#/%{pname}-%{version}.tar.gz
Patch0:         netcdf4-Return-status-for-non-void-function-always.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  %{compiler_family}-compilers-hpc
BuildRequires:  gawk
BuildRequires:  libcurl-devel >= 7.18.0
BuildRequires:  lua-lmod
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

%if 0%{!?mpi_flavor:1}
This package contains utility functions for working with NetCDF files.
%else
This package contains the openmpi version of utility functions for
working with NetCDF files.
%endif

%{hpc_master_package}

%package -n     %{libname}%{hpc_package_name_tail %_ver}
Summary:        Shared libraries for the NetCDF scientific data format
Group:          System/Libraries
%hpc_requires
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
%hpc_requires_devel
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
%patch0 -p1

# Fix spurious-executable-perm RPMLINT warning
chmod a-x RELEASE_NOTES.md

%build
%{hpc_setup}
module load pnetcdf
export CFLAGS="-I $NETCDF_INC -L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"
export CPPFLAGS=$CFLAGS
export LDFLAGS="-L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"

%if 0%{?mpi_flavor:1}
export CC="mpicc"
export FC="mpif90"
export F77="mpif77"
%endif
%hpc_configure \
    --enable-shared \
    --enable-netcdf-4 \
    --enable-dap \
    --enable-ncgen4 \
    --with-pic \
    --disable-doxygen \
    --enable-static

make %{?_smp_mflags}

%install
%{hpc_setup}
module load pnetcdf
export CFLAGS="-I $NETCDF_INC -L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"
export CPPFLAGS=$CFLAGS
export LDFLAGS="-L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"
%if 0%{?mpi_flavor:1}
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
        module load pnetcdf
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
    module load pnetcdf
export CFLAGS="-I $NETCDF_INC -L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"
export CPPFLAGS=$CFLAGS
export LDFLAGS="-L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"
%if 0%{?mpi_flavor:1}
export CC="mpicc"
export FC="mpif90"
export F77="mpif77"
%endif
    make check
%endif

%post -n %{libname}%{hpc_package_name_tail %_ver} -p /sbin/ldconfig
%postun -n %{libname}%{hpc_package_name_tail %_ver} 
/sbin/ldconfig
%hpc_module_delete_if_default

%files
%defattr(-,root,root,-)
%doc COPYRIGHT README.md RELEASE_NOTES.md
%{hpc_bindir}/

%files -n %{libname}%{hpc_package_name_tail %_ver}
%defattr(-,root,root,-)
%{hpc_dirs}
%{hpc_modules_files}
%{hpc_libdir}/libnetcdff.so.*

%files devel
%defattr(-,root,root,-)
%{hpc_includedir}/
%dir %{hpc_pkgconfigdir}
%{hpc_libdir}/pkgconfig/netcdf-fortran.pc
%{hpc_libdir}/*.so
%dir %{hpc_datadir}
%dir %{hpc_mandir}
%{hpc_mandir}/man3/

%files devel-static
%defattr(-,root,root,-)
%{hpc_libdir}/libnetcdff.a

%changelog
