#
# spec file for package openblas
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

%define _vers 0_3_11
%define vers 0.3.11
%define pname openblas

%bcond_with ringdisabled

%if "%flavor" == ""
%define package_name %{pname}
ExclusiveArch:  do_not_build
%endif

%global build_flags USE_THREAD=1 USE_OPENMP=1

%if "%flavor" == "serial"
%define build_flags USE_THREAD=0 USE_OPENMP=0
%define openblas_so_prio 20
# we build devel packages only from one flavor
%define build_devel 1
%{bcond_with hpc}
%endif 

%if "%flavor" == "pthreads"
%define build_flags USE_THREAD=1 USE_OPENMP=0 
 %ifarch %ix86 x86_64
 %define openblas_so_prio 50
 %else
 %define openblas_so_prio 20
 %endif
%{bcond_with hpc}
%endif

%if "%flavor" == "openmp"
 %ifarch %ix86 x86_64
 %define openblas_so_prio 20
 %else
 %define openblas_so_prio 50
 %endif
%{bcond_with hpc}
%endif 

%if "%flavor" == "gnu-hpc"
%define compiler_family gnu
%undefine c_f_ver
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu-hpc-pthreads"
%define compiler_family gnu
%undefine c_f_ver
%define ext pthreads
%define build_flags USE_THREAD=1 USE_OPENMP=0
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu7-hpc"
%define compiler_family gnu
%define c_f_ver 7
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu7-hpc-pthreads"
%define compiler_family gnu
%define c_f_ver 7
%define ext pthreads
%define build_flags USE_THREAD=1 USE_OPENMP=0
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu8-hpc"
%define compiler_family gnu
%define c_f_ver 8
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu8-hpc-pthreads"
%define compiler_family gnu
%define c_f_ver 8
%define ext pthreads
%define build_flags USE_THREAD=1 USE_OPENMP=0
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu9-hpc"
%define compiler_family gnu
%define c_f_ver 9
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu9-hpc-pthreads"
%define compiler_family gnu
%define c_f_ver 9
%define ext pthreads
%define build_flags USE_THREAD=1 USE_OPENMP=0
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu10-hpc"
%define compiler_family gnu
%define c_f_ver 10
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu10-hpc-pthreads"
%define compiler_family gnu
%define c_f_ver 10
%define ext pthreads
%define build_flags USE_THREAD=1 USE_OPENMP=0
%{bcond_without hpc}
%endif

%if %{without hpc}
%if 0%{!?package_name:1}
%define package_name  %{pname}_%{flavor}
%endif
%define so_v 0
%define p_prefix %_prefix
%define p_includedir %_includedir/%pname
%define p_libdir %_libdir
%define p_cmakedir %{p_libdir}/cmake/%{pname}
%define num_threads 64

%else
# Magic for OBS Staging. Only build the flavors required by
# other packages in the ring.
%if %{with ringdisabled}
ExclusiveArch:  do_not_build
%endif

%define package_name %{hpc_package_name %_vers}

%define p_prefix %hpc_prefix
%define p_includedir %hpc_includedir
%define p_libdir %hpc_libdir
%define p_cmakedir %{hpc_libdir}/cmake
%define num_threads 256

%{hpc_init -c %{compiler_family} %{?c_f_ver:-v %{c_f_ver}} %{?ext:-e %{ext}}}
%endif

Name:           %{package_name}
Version:        %vers
Release:        0
Summary:        An optimized BLAS library based on GotoBLAS2
License:        BSD-3-Clause
Group:          Productivity/Scientific/Math
URL:            http://www.openblas.net
Source0:        https://github.com/xianyi/OpenBLAS/archive/v%{version}.tar.gz#/OpenBLAS-%{version}.tar.gz
Source1:        README.SUSE
Source2:        README.HPC.SUSE
# PATCH-FIX-UPSTREAM openblas-noexecstack.patch
Patch1:         openblas-noexecstack.patch
# PATCH port
Patch2:         openblas-s390.patch
# PATCH-FIX-UPSTREAM fix-build.patch
Patch3:         fix-build.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if %{without hpc}
BuildRequires:  gcc-fortran
BuildRequires:  update-alternatives
Requires(post): update-alternatives
Requires(preun): update-alternatives
%else
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  lua-lmod
BuildRequires:  suse-hpc
%global dep_summary %{summary}
%endif

%description
OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.

%package     -n lib%{name}%{?so_v}
Summary:        An optimized BLAS library based on GotoBLAS2, %{flavor} version
Group:          System/Libraries
%if %{without hpc}
Requires(post): update-alternatives
Requires(preun): update-alternatives
 %if "%flavor" == "serial"
Obsoletes:      lib%{pname}%{so_v} < %{version}
Provides:       lib%{pname}%{so_v} = %{version}
 %else
Obsoletes:      lib%{pname}0
 %endif
 %if "%flavor" == "pthreads"
Obsoletes:      lib%{pname}p0
 %endif
 %if "%flavor" == "openmp"
Obsoletes:      lib%{pname}o0
 %endif
%else # with hpc
%hpc_requires
%endif

%description -n lib%{name}%{?so_v}
OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.

%{?with_hpc:%{hpc_master_package  -l -L}}

%package     -n lib%{name}-devel
Summary:        Development libraries for OpenBLAS, %{flavor} version
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{?so_v} = %{version}
%if %{without hpc}
Requires:       %{pname}-devel-headers = %{version}
%else
%hpc_requires_devel
%endif

%description -n lib%{name}-devel
OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.

This package contains the development libraries for serial OpenBLAS version.

%{?with_hpc:%{hpc_master_package  -l -L  devel}}

%package        devel-static
Summary:        Static version of OpenBLAS
Group:          Development/Libraries/C and C++
%if %{without hpc}
Requires:       %{pname}-devel = %{version}
%else
Requires:       lib%{name}-devel = %{version}
%endif

%description    devel-static
OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.

This package contains the static libraries.

%package      -n %{pname}-devel
Summary:        Development headers and libraries for OpenBLAS
Group:          Development/Libraries/C and C++
Requires:       %{pname}-devel-headers = %{version}
%ifarch %ix86 x86_64
Requires:       lib%{pname}_pthreads-devel = %{version}
%else
Requires:       lib%{pname}_openmp-devel = %{version}
%endif

%description  -n %{pname}-devel
OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.

%package      -n %{pname}-devel-headers
Summary:        Development headers for OpenBLAS
Group:          Development/Libraries/C and C++
Conflicts:      %{pname}-devel < %{version}
BuildArch:      noarch

%description  -n %{pname}-devel-headers
OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.

This package contains headers for OpenBLAS.

%prep

%setup -q -n OpenBLAS-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%ifarch s390
sed -i -e "s@m32@m31@" Makefile.system
%endif

%if %{without hpc}
cp %{SOURCE1} .
%else
cp %{SOURCE2} .
%endif

%build

%if %{with hpc}
%hpc_debug
%hpc_setup_compiler
%endif

# Use DYNAMIC_ARCH everywhere - not sure about PPC?
%global openblas_target DYNAMIC_ARCH=1
# We specify TARGET= to avoid compile-time CPU-detection (boo#1100677)
%ifarch %ix86 x86_64
%global openblas_target %openblas_target TARGET=CORE2
%endif
%ifarch aarch64
%global openblas_target %openblas_target TARGET=ARMV8 
%endif  
%ifarch s390 s390x
%global openblas_target %openblas_target TARGET=ZARCH_GENERIC
%endif
%ifarch ppc64 ppc64le
%global openblas_target %openblas_target TARGET=POWER8
%endif
# force -mvsx for ppc64 to avoid build failure:
# ../kernel/power/sasum_microk_power8.c:41:3: error: '__vector' undeclared (first use in this function); did you mean '__cpow'?
# TODO why is it required ? (and not for ppc64le)
%ifarch ppc64
%define addopt -mvsx
%endif
# Make serial, threaded and OpenMP versions
make  %{?_smp_mflags} %{?openblas_target} %{?build_flags} \
    BUILD_BFLOAT16=1 COMMON_OPT="%{optflags} %{?addopt}" \
    NUM_THREADS=%{num_threads} V=1 \
    OPENBLAS_LIBRARY_DIR=%{p_libdir} \
    OPENBLAS_INCLUDE_DIR=%{hpc_includedir} \
    OPENBLAS_CMAKE_DIR=%{p_cmakedir} \
    PREFIX=%{p_prefix} \
    %{!?with_hpc:LIBNAMESUFFIX=%flavor FC=gfortran CC=gcc}

%install
%if %{with hpc}
%hpc_setup_compiler
%endif

# Install serial library and headers
%make_install  %{?build_flags} \
    OPENBLAS_LIBRARY_DIR=%{p_libdir} \
    OPENBLAS_INCLUDE_DIR=%{p_includedir} \
    OPENBLAS_CMAKE_DIR=%{p_cmakedir} \
    PREFIX=%{p_prefix} \
    %{!?with_hpc:LIBNAMESUFFIX=%flavor}

# Delete info about OBS host cpu
%ifarch %ix86 x86_64
 sed -i '/#define OPENBLAS_NEEDBUNDERSCORE/,/#define OPENBLAS_VERSION/{//!d}' \
    %{buildroot}%{p_includedir}/openblas_config.h
%endif

%if %{without hpc}

%if 0%{!?build_devel:1}
# We need the includes only once
rm -rf %{buildroot}%{p_includedir}/
rm -rf %{buildroot}%{p_libdir}/cmake/
%else
# Fix cmake config file
sed -i 's|%{buildroot}||g' %{buildroot}%{p_cmakedir}/*.cmake
sed -i 's|_serial||g' %{buildroot}%{p_cmakedir}/*.cmake
%endif

# Put libraries in correct location
rm -rf %{buildroot}%{p_libdir}/lib%{name}*

# Install the serial library
install -D -p -m 755 lib%{name}.so %{buildroot}%{p_libdir}/lib%{name}.so.0
install -D -p -m 644 lib%{name}.a %{buildroot}%{p_libdir}/lib%{name}.a

# Fix source permissions (also applies to LAPACK)
find -name \*.f -exec chmod 644 {} +

# Remove pkgconfig file, it can't be configured for different library suffixes we use and, as such, is useless
rm -fr %{buildroot}%{p_libdir}/pkgconfig/

# Dummy target for update-alternatives
install -d %{buildroot}/%{_sysconfdir}/alternatives
ln -s lib%{pname}.so.0 %{buildroot}/%{p_libdir}/lib%{pname}.so.0
ln -s lib%{pname}.so.0 %{buildroot}/%{_sysconfdir}/alternatives/lib%{pname}.so.0
ln -s lib%{pname}.so.0 %{buildroot}/%{p_libdir}/libblas.so.3
ln -s lib%{pname}.so.0 %{buildroot}/%{p_libdir}/libcblas.so.3
ln -s lib%{pname}.so.0 %{buildroot}/%{p_libdir}/liblapack.so.3
ln -s lib%{pname}.so.0 %{buildroot}/%{_sysconfdir}/alternatives/libblas.so.3
ln -s lib%{pname}.so.0 %{buildroot}/%{_sysconfdir}/alternatives/libcblas.so.3
ln -s lib%{pname}.so.0 %{buildroot}/%{_sysconfdir}/alternatives/liblapack.so.3

# Fix symlinks
pushd %{buildroot}%{p_libdir}
%if 0%{?build_devel}
ln -sf lib%{pname}.so.0 lib%{pname}.so
%endif
ln -sf lib%{name}.so.0 lib%{name}.so

%else # with hpc

# HPC module file
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{pname} library built with the %{compiler_family} compiler toolchain."
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{hpc_upcase %pname} built with %{compiler_family} toolchain"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{dep_summary}"
module-whatis "%{url}"

set     version             %{version}

prepend-path    LD_LIBRARY_PATH     %{p_libdir}

setenv          %{hpc_upcase %pname}_DIR        %{hpc_prefix}

if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    LIBRARY_PATH        %{p_libdir}
prepend-path    CPATH               %{p_includedir}
prepend-path    C_INCLUDE_PATH      %{p_includedir}
prepend-path    CPLUS_INCLUDE_PATH  %{p_includedir}
prepend-path    INCLUDE             %{p_includedir}
%hpc_modulefile_add_pkgconfig_path

setenv          %{hpc_upcase %pname}_DIR        %{hpc_prefix}
setenv          %{hpc_upcase %pname}_LIB        %{p_libdir}
setenv          %{hpc_upcase %pname}_INC        %{p_includedir}

}

family "openblas"
EOF
%{hpc_write_pkgconfig -l %{pname}}

%endif # with hpc

%if %{without hpc}

%post -n lib%{name}%{so_v}
%{_sbindir}/update-alternatives --install \
   %{p_libdir}/libblas.so.3 libblas.so.3 %{p_libdir}/lib%{name}.so.%{so_v}  20
%{_sbindir}/update-alternatives --install \
   %{p_libdir}/libcblas.so.3 libcblas.so.3 %{p_libdir}/lib%{name}.so.%{so_v}  20
%{_sbindir}/update-alternatives --install \
   %{p_libdir}/liblapack.so.3 liblapack.so.3 %{p_libdir}/lib%{name}.so.%{so_v}  20
%{_sbindir}/update-alternatives --install \
   %{p_libdir}/lib%{pname}.so.%{so_v} lib%{name}.so.%{so_v} %{p_libdir}/lib%{name}.so.%{so_v}  %openblas_so_prio
/sbin/ldconfig

%preun -n lib%{name}%{so_v}
if [ "$1" = 0 ] ; then
   %{_sbindir}/update-alternatives --remove libblas.so.3 %{p_libdir}/lib%{name}.so.%{so_v}
   %{_sbindir}/update-alternatives --remove libcblas.so.3 %{p_libdir}/lib%{name}.so.%{so_v}
   %{_sbindir}/update-alternatives --remove liblapack.so.3 %{p_libdir}/lib%{name}.so.%{so_v}
   %{_sbindir}/update-alternatives --remove lib%{name}.so.0 %{p_libdir}/lib%{name}.so.%{so_v}
fi

%postun -n lib%{name}%{so_v} -p /sbin/ldconfig

%posttrans -n lib%{name}%{so_v}
if [ "$1" = 0 ] ; then
  if ! [ -f %{p_libdir}/lib%{name}.so.%{so_v} ] ; then
      %{_sbindir}/update-alternatives --auto lib%{pname}.so.%{so_v}
  fi
fi

%else

%postun -n lib%{name}
%hpc_module_delete_if_default

%endif

%if %{without hpc}
%define libname %name
%else
%define libname %pname
%endif

%files -n lib%{name}%{?so_v}
%defattr(-,root,root,-)
%{p_libdir}/lib%{libname}.so.0
%if %{without hpc}
%ghost %{p_libdir}/lib%{pname}.so.%{so_v}
%ghost %{p_libdir}/libblas.so.3
%ghost %{p_libdir}/libcblas.so.3
%ghost %{p_libdir}/liblapack.so.3
%ghost %{_sysconfdir}/alternatives/lib%{pname}.so.%{so_v}
%ghost %{_sysconfdir}/alternatives/libblas.so.3
%ghost %{_sysconfdir}/alternatives/libcblas.so.3
%ghost %{_sysconfdir}/alternatives/liblapack.so.3
%else
%hpc_dirs
%{p_libdir}/libopenblas*r*.so
%hpc_modules_files
%endif

%files -n lib%{name}-devel
%defattr(-,root,root,-)
%{p_libdir}/lib%{libname}.so
%if %{with hpc}
%license LICENSE
%doc Changelog.txt GotoBLAS* README.md README.HPC.SUSE
%hpc_pkgconfig_file
%{p_cmakedir}/
%{p_includedir}/
%endif

%files devel-static
%defattr(-,root,root,-)
#%%{p_libdir}/lib%{libname}.a
%{p_libdir}/libopenblas*.a

%if 0%{?build_devel}
%files  -n %{pname}-devel
%defattr(-,root,root,-)
%license LICENSE
%doc Changelog.txt GotoBLAS* README.md README.SUSE
%{p_libdir}/libopenblas.so
%dir %{p_libdir}/cmake
%{p_cmakedir}/

%files -n %{pname}-devel-headers
%defattr(-,root,root,-)
%{p_includedir}/
%endif

%changelog
