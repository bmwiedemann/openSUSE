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

%define _do_check 1

%define ver 4.9.0
%define _ver 4_9_0
%define pname netcdf
%define sonum   19

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

%bcond_with valgrind_checks
# Keep disabled until properly set up on HDF5 library side
%bcond_with plugins

%if "%flavor" == ""
%define package_name %{pname}
ExclusiveArch:  do_not_build
%endif

ExcludeArch:    s390

%if "%{flavor}" == "serial"
%bcond_with hpc
%endif

%if "%{flavor}" == "gnu-hpc"
%global compiler_family gnu
%undefine c_f_ver
%undefine mpi_flavor
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%undefine c_f_ver
%define mpi_flavor openmpi
%define mpi_ver 1
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

%if "%{flavor}" == "gnu-openmpi2-hpc"
%{?DisOMPI2}
%global compiler_family gnu
%undefine c_f_ver
%define mpi_flavor openmpi
%define mpi_ver 2
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
#
%if "%{flavor}" == "gnu11-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%define c_f_ver 11
%define mpi_flavor openmpi
%define mpi_ver 1
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu11-openmpi2-hpc"
%{?DisOMPI2}
%global compiler_family gnu
%define c_f_ver 11
%define mpi_flavor openmpi
%define mpi_ver 2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu11-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%define c_f_ver 11
%define mpi_flavor openmpi
%define mpi_ver 3
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu11-openmpi4-hpc"
%{?DisOMPI4}
%global compiler_family gnu
%define c_f_ver 11
%define mpi_flavor openmpi
%define mpi_ver 4
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu11-mvapich2-hpc"
%global compiler_family gnu
%define c_f_ver 11
%define mpi_flavor mvapich2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu11-mpich-hpc"
%global compiler_family gnu
%define c_f_ver 11
%define mpi_flavor mpich
%bcond_without hpc
%endif

%if "%{flavor}" == "mvapich2"
%define mpi_flavor mvapich2
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

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}
%{?with_hpc:%{!?compiler_family:%global compiler_family gnu}}
%{?with_mpi:%{!?mpi_flavor:error "No MPI family specified!"}}

# openmpi 1 was called just "openmpi" in Leap 15.x/SLE15
%if 0%{?suse_version} >= 1550 || "%{mpi_flavor}" != "openmpi"  || "%{mpi_ver}" != "1"
%define mpi_ext %{?mpi_ver}
%endif

%if %{with hpc}
%{hpc_init -c %compiler_family %{?c_f_ver:-v %{c_f_ver}} %{?with_mpi:-m {%mpi_flavor}} %{?mpi_ver:-V %{mpi_ver}} %{?ext:-e %{ext}}}
%define package_name %{hpc_package_name %_ver}
%define libname(s:)   lib%{pname}%{hpc_package_name_tail %_ver}
%define p_prefix %hpc_prefix
%define p_bindir %hpc_bindir
%define p_libdir %hpc_libdir
%define p_mandir %hpc_mandir
%define p_includedir %hpc_includedir
%else
%define package_name %{pname}%{p_suffix}
%define libname(s:)   lib%{pname}%{-s*}%{?p_suffix}
 %if %{without mpi}
%define p_prefix %_prefix
%define p_bindir %_bindir
%define p_libdir %_libdir
%define p_mandir %_mandir
%define p_includedir %_includedir
 %else
%define p_prefix /usr/%{_lib}/mpi/gcc/%{mpi_flavor}%{?mpi_ext}
%define p_bindir %{p_prefix}/bin
%define p_libdir %{p_prefix}/%{_lib}
%define p_mandir %{p_prefix}/share/man
%define p_includedir %{p_prefix}/include
 %endif
%endif
%define p_suffix %{?with_mpi:-%{mpi_flavor}%{?mpi_ext}}
%define hdf5_module_file %{?with_mpi:p}hdf5

%define purpose_compiler %{?nil:%{!?with_hpc:.}
%{?with_hpc:built for the %{compiler_family} compiler%{?c_f_ver: version %c_f_ver}.}
}

%define purpose() This package contains %{?with_mpi:the %{mpi_flavor}%{?mpi_ver} version of }%{**}%{purpose_compiler}

%if %{with valgrind_checks}
%ifnarch %ix86 x86_64 ppc ppc64 s390x armv7l aarch64
%{error: Vagrind not support on this platform!}
%else
%define valgrind_checks 1
%endif
%endif

Name:           %{package_name}
Summary:        Command-line programs for the NetCDF scientific data format
License:        NetCDF
Group:          Productivity/Scientific/Other
Version:        %ver
Release:        0
URL:            https://www.unidata.ucar.edu/software/netcdf/
Source:         https://downloads.unidata.ucar.edu/netcdf-c/%{version}/%{pname}-c-%{version}.tar.gz
Source1:        nc-config.1.gz
Patch6:         parseServers-Fix-uninitialized-variable-simplify-error-path.patch
Patch8:         val_NC_check_voff-Fix-uninitialized-variable-warning.patch
Patch9:         pr_att-Fix-uninitialized-variable.patch
Patch10:        NCD4_dumpbytes-Add-missing-initialization-of-float-types.patch
Patch11:        NCZ_def_var_chunking-make-sure-cs-is-set-before-used.patch
Patch12:        Fix-spurious-uninitialized-variable-warning.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gawk
BuildRequires:  libcurl-devel >= 7.18.0
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  unzip
BuildRequires:  zlib-devel >= 1.2.5
BuildRequires:  pkgconfig(libxml-2.0)
%if 0%{?valgrind_checks}
BuildRequires:  valgrind
%endif
%if %{without hpc}
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  hdf5%{p_suffix}-devel
BuildRequires:  libhdf5_hl%{p_suffix}
 %if %{with mpi}
BuildRequires:  %{mpi_flavor}%{?mpi_ext}-devel
 %endif
%else
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  hdf5-%{compiler_family}%{?c_f_ver}%{?with_mpi:-%{mpi_flavor}%{?mpi_ver}}-hpc-devel
# Install libhdf5*-<compiler_family>-hpc explicitly for %%requires_eq:
BuildRequires:  libhdf5-%{compiler_family}%{?c_f_ver}%{?with_mpi:-%{mpi_flavor}%{?mpi_ver}}-hpc
BuildRequires:  libhdf5_hl-%{compiler_family}%{?c_f_ver}%{?with_mpi:-%{mpi_flavor}%{?mpi_ver}}-hpc
BuildRequires:  lua-lmod
BuildRequires:  suse-hpc
 %if %{with mpi}
BuildRequires:  %{mpi_flavor}%{?mpi_ver}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
 %endif
%endif
Requires:       %{libname -s %{sonum}} = %{version}

%description
NetCDF is a set of software libraries and self-describing,
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

%{purpose utility functions for working with NetCDF files}

%{?with_hpc:%{hpc_master_package}}

%package -n     %{libname -s %{sonum}}
Summary:        Shared libraries for the NetCDF scientific data format
Group:          Productivity/Scientific/Other
%if %{without hpc}
# To avoid unresolvable errors due to multiple providers of the library
%{requires_eq libhdf5%{p_suffix}}
%{requires_eq libhdf5_hl%{p_suffix}}
%else
%{hpc_requires}
%{requires_eq libhdf5%{hpc_package_name_tail}}
%{requires_eq libhdf5_hl%{hpc_package_name_tail}}
%endif

%description -n %{libname -s %{sonum}}
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

%{purpose the NetCDF runtime libraries}

%{?with_hpc:%{hpc_master_package -L -l}}

%package   devel-data
Summary:        Development data files for %{name}
Group:          Development/Libraries/C and C++
Provides:       %{pname}-rpm-macros = %version
Conflicts:      otherproviders(%{pname}-rpm-macros)

%description devel-data
NetCDF is a set of software libraries and self-describing,
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

This package contains generic files needed to create projects that use
any version of NetCDF.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname -s %{sonum}} = %{version}
%{!?with_hpc:Requires:       %{pname}-devel-data = %{version}}
Requires:       libcurl-devel >= 7.18.0
Requires:       pkgconfig
Requires:       zlib-devel >= 1.2.5
%if %{without hpc}
%{requires_eq hdf5%{p_suffix}-devel}
%{?with_mpi:Requires:       %{mpi_flavor}%{?mpi_ext}-devel}
%else
%{hpc_requires_devel}
%{requires_eq hdf5%{hpc_package_name_tail}-devel}
%endif

%description devel
NetCDF is a set of software libraries and self-describing,
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

%{purpose all files needed to create projects that use NetCDF}

%{?with_hpc:%{hpc_master_package devel}}

%package devel-static
Summary:        Static development files for %{name}
Group:          Development/Libraries/C and C++
%if %{without hpc}
%{requires_eq hdf5%{p_suffix}-devel}
%else
Requires:       %{name}-devel = %{version}
%endif
Requires:       libcurl-devel >= 7.18.0
Requires:       zlib-devel >= 1.2.5

%description devel-static
NetCDF is a set of software libraries and self-describing,
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

%{purpose the static libraries for NetCDF}

%prep
%{?with_hpc:%hpc_debug}
%setup -q -n %{pname}-c-%{version}
%autopatch -p1

# Create baselib.conf dynamically (non-HPC build only).
%if %{without hpc}
cat > %{_sourcedir}/baselibs.conf  <<EOF
%{libname -s %{sonum}}
EOF
%endif

# Fix spurious-executable-perm RPMLINT warning
chmod a-x RELEASE_NOTES.md

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%{?with_hpc:%{hpc_setup}}
%{?with_hpc:module load %{hdf5_module_file}}

%if %{without mpi}
export CC=gcc CXX=g++ FC=gfortran
%else
export CC=%{!?with_hpc:/usr/%_lib/mpi/gcc/%{mpi_flavor}%{?mpi_ext}/bin/}mpicc
export FC=%{!?with_hpc:/usr/%_lib/mpi/gcc/%{mpi_flavor}%{?mpi_ext}/bin/}mpif90
export CXX=%{!?with_hpc:/usr/%_lib/mpi/gcc/%{mpi_flavor}%{?mpi_ext}/bin/}mpic++
%endif
autoreconf -fv
export CFLAGS="%{optflags} %{?with_hpc:-L$HDF5_LIB -I$HDF5_INC}"
export CXXFLAGS="%{optflags} %{?with_hpc:-L$HDF5_LIB -I$HDF5_INC}"
export FCFLAGS="%{optflags} %{?with_hpc:-L$HDF5_LIB -I$HDF5_INC}"
%{?with_hpc:export LDFLAGS="-L$HDF5_LIB"}
%if %{without hpc}
%configure \
     --prefix=%{p_prefix} \
     --bindir=%{p_bindir} \
     --libdir=%{p_libdir} \
     --includedir=%{p_includedir} \
     --mandir=%{p_mandir} \
%else
%hpc_configure \
%endif
    --enable-shared \
    --enable-netcdf-4 \
    --enable-dap \
    --enable-extra-example-tests \
    --disable-dap-remote-tests \
    --with-pic \
    --disable-doxygen \
    --enable-static \
%if %{with plugins}
    --enable-plugins \
    --with-plugin-dir=%{p_libdir}/hdf5/plugin/
%else
    --disable-plugins \
%endif
#    --enable-logging \

%make_build
# Build tests without executing
%make_build check TESTS=""

%install
%{?with_hpc:%{hpc_setup}}
%{?with_hpc:module load %{hdf5_module_file}}

%{?with_hpc:export CFLAGS="-L$HDF5_LIB -I$HDF5_INC"}
make install DESTDIR="%{buildroot}"

mkdir -p %{buildroot}%{_mandir}/man1
install -m644 %{S:1} %{buildroot}%{p_mandir}/man1
rm -f %{buildroot}%{p_libdir}/*.la

# install netcdf_par.h which is skipped when mpicc in not detected
install -m644 include/netcdf_par.h %{buildroot}%{p_includedir}/netcdf_par.h

%if %{without mpi} && %{without hpc}
# rpm macro for version checking
mkdir -p %{buildroot}%{_rpmmacrodir}
cat > %{buildroot}%{_rpmmacrodir}/macros.netcdf <<EOF
#
# RPM macros for hdf5 packaging
#
%_netcdf_sonum  %{sonum}
%_netcdf_version  %{version}
EOF
%endif

%if %{without hpc}
 %if %{with mpi}
# Module files
mkdir -p %{buildroot}%{_datadir}/modules/%{pname}-%{mpi_flavor}%{?mpi_ext}
cat << EOF > %{buildroot}%{_datadir}/modules/%{pname}-%{mpi_flavor}%{?mpi_ext}/%version
#%%Module
proc ModulesHelp { } {
        global dotversion
        puts stderr "\tLoads the %{pname}-%{mpi_flavor} %version Environment"
}

module-whatis  "Loads the %{pname}-%{mpi_flavor} %version Environment."
prepend-path    PATH                %{p_bindir}
prepend-path    MANPATH             %{p_mandir}
prepend-path    LD_LIBRARY_PATH     %{p_libdir}
prepend-path    LIBRARY_PATH        %{p_libdir}
prepend-path    CPATH               %{p_includedir}
prepend-path    C_INCLUDE_PATH      %{p_includedir}
prepend-path    CPLUS_INCLUDE_PATH  %{p_includedir}
EOF

 %endif
%else
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the NetCDF C API built with the %{compiler_family} compiler"
puts stderr "toolchain and the %{mpi_flavor}%{?mpi_ver} MPI stack."
puts stderr " "
puts stderr "Note that this build of NetCDF leverages the HDF I/O library and requires linkage"
puts stderr "against hdf5. Consequently, the phdf5 package is loaded automatically with this module."
puts stderr "A typical compilation step for C applications requiring NetCDF is as follows:"
puts stderr " "
puts stderr "\\\$CC -I\\\$NETCDF_INC app.c -L\\\$NETCDF_LIB -lnetcdf -L\\\$HDF5_LIB -lhdf5"

puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{hpc_upcase %pname} built with %{compiler_family} toolchain"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{SUMMARY:0}"
module-whatis "%{url}"

set             version             %{version}

# Require phdf5

if [ expr [ module-info mode load ] || [module-info mode display ] ] {
    if {  ![is-loaded %{hdf5_module_file}]  } {
        module load %{hdf5_module_file}
    }
}

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
prepend-path    INCLUDE                         %{hpc_includedir}
%hpc_modulefile_add_pkgconfig_path

setenv          %{hpc_upcase %pname}_LIB        %{hpc_libdir}
setenv          %{hpc_upcase %pname}_INC        %{hpc_includedir}
}
EOF

%endif

%if 0%{?_do_check}
%check
%if %{with hpc}
%{hpc_setup}
module load %{hdf5_module_file}
%else
 %if %{with mpi}
 . /usr/%_lib/mpi/gcc/%{mpi_flavor}%{?mpi_ext}/bin/mpivars.sh
 %endif
%endif
%ifarch ppc64 s390x %ix86
# tst_netcdf4_4 fails on ix86 - https://github.com/Unidata/netcdf-c/issues/2433
    make check || { echo -e "WARNING: ignore check error for ppc64/s390x/ix86"; }
%else
    make check
%endif
%if 0%{?valgrind_checks}
    make check-valgrind
%endif
%endif

%if %{with hpc} || %{with mpi}
%define ldconfig_args -N %p_libdir
%endif

%post -n %{libname -s %{sonum}}
/sbin/ldconfig %{?ldconfig_args}

%postun -n %{libname -s %{sonum}}
/sbin/ldconfig %{?ldconfig_args}
%{?with_hpc:%hpc_module_delete_if_default}

%files
%license COPYRIGHT
%doc README.md RELEASE_NOTES.md
%{?with_hpc:%dir %hpc_datadir}
%{?with_hpc:%dir %p_mandir}
%{p_bindir}%{!?with_hpc:/*}
%exclude %{p_bindir}/nc-config
%if "%{flavor}" != "serial"
%dir %{p_mandir}/man1
%endif
%{p_mandir}/man1/*

%files -n %{libname -s %{sonum}}
%if %{with hpc}
%hpc_dirs
%hpc_modules_files
%else
 %if %{with mpi}
%dir %{_datadir}/modules
%{_datadir}/modules/%{pname}-%{mpi_flavor}%{?mpi_ext}
 %endif
%endif
%{p_libdir}/libnetcdf.so.%{sonum}*

%if %{without mpi} && %{without hpc}
%files devel-data
%{_rpmmacrodir}/macros.netcdf
%endif

%files devel
%{p_bindir}/nc-config
%{p_includedir}%{!?with_hpc:/*}
%{p_libdir}/*.so
%{?with_hpc:%hpc_pkgconfig_file}
%{p_libdir}/pkgconfig/netcdf.pc
%if "%{flavor}" != "serial"
%dir %{p_mandir}/man3
%endif
%{p_mandir}/man3/*
%{p_libdir}/libnetcdf.settings

%files devel-static
%{p_libdir}/libnetcdf.a

%changelog
