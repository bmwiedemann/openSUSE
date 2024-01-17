#
# spec file
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

%global pname netcdf-cxx4
%global ver 4.3.1
%global _ver 4_3_1
%define sover 1
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

ExcludeArch:    s390 s390x

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%endif

%if "%flavor" == "standard"
%undefine compiler_family
%bcond_with hpc
%endif

%if "%flavor" == "gnu-hpc"
%global compiler_family gnu
%bcond_without hpc
%endif

%if "%flavor" == "gnu7-hpc"
%global compiler_family gnu
%bcond_without hpc
%define c_f_ver 7
%endif

%if "%flavor" == "gnu8-hpc"
%global compiler_family gnu
%bcond_without hpc
%define c_f_ver 8
%endif

%if "%flavor" == "gnu9-hpc"
%global compiler_family gnu
%bcond_without hpc
%define c_f_ver 9
%endif

%if "%flavor" == "gnu10-hpc"
%global compiler_family gnu
%bcond_without hpc
%define c_f_ver 10
%endif

%if !0%{?is_opensuse} && !0%{?with_hpc:1}
ExclusiveArch:  do_not_build
%endif

%define hpc_upcase_trans_hyph() %(echo %{**} | tr [a-z] [A-Z] | tr '-' '_')

%if %{with hpc}
%{hpc_init -c %{compiler_family} %{?c_f_ver:-v %{c_f_ver}}}
%define package_name %{hpc_package_name %_ver}
%define libname(s:l:)   lib%{pname}%{hpc_package_name_tail %{?-l:%{-l*}}}
%define p_bindir %hpc_bindir
%define p_libdir %hpc_libdir
%define p_includedir %hpc_includedir
%else
%define package_name %pname
%define libname(s:l:)   libnetcdf_c++4%{?-s:-%{-s*}}
%define p_bindir %_bindir
%define p_libdir %_libdir
%define p_includedir %_includedir
%endif

Name:           %{package_name}
Version:        %ver
Release:        0
Summary:        C++ library for the Unidata network Common Data Form version 4
License:        NetCDF
Group:          Productivity/Scientific/Other
URL:            http://www.unidata.ucar.edu/software/netcdf/
Source0:        http://www.unidata.ucar.edu/downloads/netcdf/ftp/netcdf-cxx4-%{version}.tar.gz
Patch0:         netcdf-cxx4-testsuite_bigendian.patch
%if %{without hpc}
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(netcdf)
%else
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  lua-lmod
BuildRequires:  netcdf-%{compiler_family}%{?c_f_ver}-hpc-devel
# Install libnetcdf-<compiler_family>-hpc explicitly for %%requires_eq
BuildRequires:  libnetcdf-%{compiler_family}%{?c_f_ver}-hpc
BuildRequires:  suse-hpc
%endif

%description
NetCDF4 (network Common Data Form) is a set of software libraries and
machine-independent data formats that support the creation, access, and sharing
of array-oriented scientific data.

This package provides the C++ API.

%package -n %{libname -s %{sover} -l %_ver}
Summary:        C++ library for the Unidata network Common Data Form version 4
Group:          System/Libraries
%if %{without hpc}
Provides:       libnetcdf%{sover}:%{p_libdir}/libnetcdf_c++.so.%{sover}
%else
%hpc_requires
%{requires_eq libnetcdf-%{compiler_family}%{?c_f_ver}-hpc}
%endif

%description -n %{libname -s %{sover} -l %_ver}
NetCDF4 (network Common Data Form) is a set of software libraries and
machine-independent data formats that support the creation, access, and sharing
of array-oriented scientific data.

This package provides the C++ API.

%{?with_hpc:%{hpc_master_package -n %{libname} -L -l}}

%package -n %{libname -l %_ver}-devel
Summary:        Development files for netcdf_c++
Group:          Development/Libraries/C and C++
%if %{without hpc}
Provides:       libnetcdf-devel:%{_libdir}/libnetcdf_c++.so
%else
%{requires_eq netcdf-%{compiler_family}%{?c_f_ver}-hpc-devel}
%endif
Requires:       %{libname -s %{sover} -l %_ver} = %{version}
%{?with_hpc:%hpc_requires_devel}
Obsoletes:      %{name}-tools <= %{version}
Provides:       %{name}-tools = %{version}

%description -n %{libname -l %_ver}-devel
This package contains the netcdf_c++4 header files and shared devel libs.

%{?with_hpc:%{hpc_master_package -l devel -O netcdf-cxx4%{hpc_package_name_tail}-tools}}

%package -n %{libname -l %_ver}-devel-static
Summary:        Static development files for netcdf_c++
Group:          Development/Libraries/C and C++
Requires:       %{libname -l %_ver}-devel = %{version}

%description -n %{libname -l %_ver}-devel-static
Libraries to build statically linked applications with NetCDF.

%prep
%setup -q -n %{pname}-%{version}
%ifarch ppc ppc64 s390 s390x
%patch0 -p1
%endif

%build
%{?with_hpc:%hpc_setup}
%if %{without hpc}
%configure \
     --disable-static
%else
module load netcdf
export CFLAGS="-I $NETCDF_INC -L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"
export CPPFLAGS=$CFLAGS
export LDFLAGS="-L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"
%hpc_configure \
    --enable-shared \
    --enable-netcdf-4 \
    --enable-dap \
    --enable-ncgen4 \
    --with-pic \
    --disable-doxygen \
    --enable-static
%endif
make %{?_smp_mflags}

%install
%if %{with hpc}
%{hpc_setup}
module load netcdf
export CFLAGS="-I $NETCDF_INC -L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"
export CPPFLAGS=$CFLAGS
export LDFLAGS="-L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"
%endif
%make_install
rm %{buildroot}%{p_libdir}/libnetcdf_c++4.la

%if %{with hpc}
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the NetCDF C++ API built with the %{compiler_family} compiler toolchain."
puts stderr " "
puts stderr "Note that this build of NetCDF leverages the HDF I/O library and requires linkage"
puts stderr "against hdf5 and the native C NetCDF library. Consequently, phdf5 and the standard C"
puts stderr "version of NetCDF are loaded automatically via this module. A typical compilation"
puts stderr "example for C++ applications requiring NetCDF is as follows:"
puts stderr " "
puts stderr "\\\$CXX -I\\\$NETCDF_CXX_INC app.cpp -L\\\$NETCDF_CXX_LIB -lnetcdf_c++4 -L\\\$NETCDF_LIB -lnetcdf -L\\\$HDF5_LIB -lhdf5"

puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{hpc_upcase %pname} built with %{compiler_family} toolchain"
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
if ([file isdirectory  %{hpc_bindir}]) {
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

%endif

%check
%{?hpc_setup}
%if %{with hpc}
module load netcdf
export CFLAGS="-I $NETCDF_INC -L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"
export CPPFLAGS=$CFLAGS
export LDFLAGS="-L$NETCDF_LIB -lnetcdf -L$HDF5_LIB -lhdf5"
%endif
make check || {
	cat cxx4/test-suite.log
	exit 1
}

%post -n %{libname -s %{sover} -l %_ver} -p /sbin/ldconfig

%postun -n %{libname -s %{sover} -l %_ver}
/sbin/ldconfig
%{?with_hpc:%hpc_module_delete_if_default}

%files -n %{libname -s %{sover} -l %_ver}
%license COPYRIGHT
%doc README.md RELEASE_NOTES.md
%{?with_hpc:%hpc_dirs}
%{?with_hpc:%hpc_modules_files}
%{p_libdir}/libnetcdf_c++4.so.%{sover}
%{p_libdir}/libnetcdf_c++4.so.%{sover}.*

%files -n %{libname -l %_ver}-devel
%license COPYRIGHT
%doc README.md RELEASE_NOTES.md
%{?with_hpc:%dir %{p_includedir}}
%{p_includedir}/nc*.h
%{p_includedir}/netcdf
%{?with_hpc:%dir %{hpc_pkgconfigdir}}
%{?with_hpc:%dir %{p_bindir}}
%{p_bindir}/ncxx4-config
%{p_libdir}/pkgconfig/netcdf-cxx4.pc
%{p_libdir}/libnetcdf_c++4.so
# Do not add plugins for now
%exclude %{p_libdir}/libh5bzip2.*

%if %{with hpc}
%files -n %{libname -l %_ver}-devel-static
%{p_libdir}/*.a
%endif

%changelog
