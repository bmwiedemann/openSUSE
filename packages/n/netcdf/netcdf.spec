#
# spec file for package netcdf
#
# Copyright (c) 2025 SUSE LLC and contributors
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

%define pname netcdf
%define sonum   22

%bcond_with valgrind_checks
# Keep disabled until properly set up on HDF5 library side
%bcond_with plugins

%if "%flavor" == ""
%define package_name %{pname}
ExclusiveArch:  do_not_build
%endif

ExcludeArch:    s390 s390x i586 %arm

%if "%{flavor}" == "serial"
%endif

%if "%{flavor}" == "mvapich2"
%define mpi_flavor mvapich2
%endif

%if "%{flavor}" == "openmpi4"
%define mpi_flavor openmpi4
%endif

%if "%{flavor}" == "openmpi5"
%define mpi_flavor openmpi5
ExcludeArch:    %{ix86} %{arm}
%endif

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}

%define package_name %{pname}%{p_suffix}
%define libname(s:)   lib%{pname}%{-s*}%{?p_suffix}

%if %{without mpi}
%define p_prefix %_prefix
%define p_bindir %_bindir
%define p_libdir %_libdir
%define p_mandir %_mandir
%define p_includedir %_includedir
%else
%define p_prefix /usr/%{_lib}/mpi/gcc/%{mpi_flavor}
%define p_bindir %{p_prefix}/bin
%define p_libdir %{p_prefix}/%{_lib}
%define p_mandir %{p_prefix}/share/man
%define p_includedir %{p_prefix}/include
%endif
%define p_suffix %{?with_mpi:-%{mpi_flavor}}
%define hdf5_module_file %{?with_mpi:p}hdf5

%define purpose() This package contains %{?with_mpi:the %{mpi_flavor} version of }%{**}.

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
Version:        4.9.3
Release:        0
URL:            https://www.unidata.ucar.edu/software/netcdf/
Source:         https://downloads.unidata.ucar.edu/netcdf-c/%{version}/%{pname}-c-%{version}.tar.gz
Source1:        nc-config.1.gz
Patch8:         val_NC_check_voff-Fix-uninitialized-variable-warning.patch
Patch9:         pr_att-Fix-uninitialized-variable.patch
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
BuildRequires:  pkgconfig(libzstd)
%if 0%{?valgrind_checks}
BuildRequires:  valgrind
%endif
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  hdf5%{p_suffix}-devel
BuildRequires:  libhdf5_hl%{p_suffix}
 %if %{with mpi}
BuildRequires:  %{mpi_flavor}-devel
 %endif
Requires:       %{libname -s %{sonum}} = %{version}

%description
NetCDF is a set of software libraries and self-describing,
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

%{purpose utility functions for working with NetCDF files}

%package -n     %{libname -s %{sonum}}
Summary:        Shared libraries for the NetCDF scientific data format
Group:          Productivity/Scientific/Other
# To avoid unresolvable errors due to multiple providers of the library
%{requires_eq \--whatprovides libhdf5%{p_suffix}}
%{requires_eq \--whatprovides libhdf5_hl%{p_suffix}}

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
Requires:       %{pname}-devel-data = %{version}
Requires:       libcurl-devel >= 7.18.0
Requires:       pkgconfig
Requires:       zlib-devel >= 1.2.5
%{requires_eq hdf5%{p_suffix}-devel}
%{?with_mpi:Requires:       %{mpi_flavor}-devel}

%description devel
NetCDF is a set of software libraries and self-describing,
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

%{purpose all files needed to create projects that use NetCDF}

%package devel-static
Summary:        Static development files for %{name}
Group:          Development/Libraries/C and C++
%{requires_eq hdf5%{p_suffix}-devel}
Requires:       libcurl-devel >= 7.18.0
Requires:       zlib-devel >= 1.2.5

%description devel-static
NetCDF is a set of software libraries and self-describing,
machine-independent data formats that support the creation, access,
and sharing of array-oriented scientific data.

%{purpose the static libraries for NetCDF}

%prep
%setup -q -n %{pname}-c-%{version}
%autopatch -p1

# Create baselib.conf dynamically
cat > %{_sourcedir}/baselibs.conf  <<EOF
%{libname -s %{sonum}}
EOF

# Fix spurious-executable-perm RPMLINT warning
chmod a-x RELEASE_NOTES.md

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

%if %{without mpi}
export CC=gcc CXX=g++ FC=gfortran
%else
source %{p_bindir}/mpivars.sh
export CC=mpicc
export FC=mpif90
export CXX=mpic++
%endif
autoreconf -fv
export CFLAGS="%{optflags} %{?with_hpc:-L$HDF5_LIB -I$HDF5_INC}"
export CXXFLAGS="%{optflags} %{?with_hpc:-L$HDF5_LIB -I$HDF5_INC}"
export FCFLAGS="%{optflags} %{?with_hpc:-L$HDF5_LIB -I$HDF5_INC}"
%configure \
     --prefix=%{p_prefix} \
     --bindir=%{p_bindir} \
     --libdir=%{p_libdir} \
     --includedir=%{p_includedir} \
     --mandir=%{p_mandir} \
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
%if %{with mpi}
source %{p_bindir}/mpivars.sh
%endif
make install DESTDIR="%{buildroot}"

mkdir -p %{buildroot}%{_mandir}/man1
install -m644 %{S:1} %{buildroot}%{p_mandir}/man1
rm -f %{buildroot}%{p_libdir}/*.la

# install netcdf_par.h which is skipped when mpicc in not detected
install -m644 include/netcdf_par.h %{buildroot}%{p_includedir}/netcdf_par.h

%if %{without mpi}
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

%if %{with mpi}
# Module files
mkdir -p %{buildroot}%{_datadir}/modules/%{pname}-%{mpi_flavor}
cat << EOF > %{buildroot}%{_datadir}/modules/%{pname}-%{mpi_flavor}/%version
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

%if 0%{?_do_check}
%check
%if %{with mpi}
 . %{p_bindir}/mpivars.sh
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

%if %{with mpi}
%define ldconfig_args -N %p_libdir
%endif

%post -n %{libname -s %{sonum}}
/sbin/ldconfig %{?ldconfig_args}

%postun -n %{libname -s %{sonum}}
/sbin/ldconfig %{?ldconfig_args}

%files
%license COPYRIGHT
%doc README.md RELEASE_NOTES.md
%{p_bindir}/*
%exclude %{p_bindir}/nc-config
%if "%{flavor}" != "serial"
%dir %{p_mandir}/man1
%endif
%{p_mandir}/man1/*

%files -n %{libname -s %{sonum}}
%if %{with mpi}
%dir %{_datadir}/modules
%{_datadir}/modules/%{pname}-%{mpi_flavor}
%endif
%{p_libdir}/libnetcdf.so.%{sonum}*

%if %{without mpi}
%files devel-data
%{_rpmmacrodir}/macros.netcdf
%endif

%files devel
%{p_bindir}/nc-config
%{p_includedir}/*
%{p_libdir}/*.so
%{p_libdir}/pkgconfig/netcdf.pc
%if "%{flavor}" != "serial"
%dir %{p_mandir}/man3
%endif
%{p_mandir}/man3/*
%{p_libdir}/libnetcdf.settings

%files devel-static
%{p_libdir}/libnetcdf.a

%changelog
