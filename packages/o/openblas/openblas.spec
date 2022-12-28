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

%define _vers 0_3_21
%define vers 0.3.21
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
 %define arch_flavor 1
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
 %define arch_flavor 1
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

%ifarch ppc64le x86_64 s390x
%if 0%{?c_f_ver} > 9
%else
%if 0%{?sle_version} == 150500
%define cc_v 12
%endif
%if 0%{?sle_version} == 150400
%define cc_v 11
%endif
%if 0%{?sle_version} == 150300
%define cc_v 10
%endif
%endif
%endif

%if %{without hpc}
%if 0%{!?package_name:1}
%define package_name  %{pname}_%{flavor}
%endif
%define so_v 0
%define p_prefix %_prefix
%define p_includedir %_includedir/%pname
%define p_libdir %_libdir/openblas%{?flavor:-%{flavor}}
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
Patch1:         Use-blasint-for-INTERFACE64-compatibility.patch
Patch2:         remove-spurious-loops.patch
Patch101:       Link-library-with-z-noexecstack.patch
# PATCH port
Patch102:       Handle-s390-correctly.patch
Patch103:       openblas-ppc64be_up2_p8.patch

#BuildRequires:  cmake
BuildRequires:  memory-constraints
%if 0%{?cc_v:1}
BuildRequires:  gcc%{?cc_v}-fortran
%endif
%if %{without hpc}
BuildRequires:  gcc-fortran
BuildRequires:  update-alternatives
Requires(post): update-alternatives
Requires(preun):update-alternatives
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
Requires(preun):update-alternatives
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
Requires:       %{pname}-common-devel = %{version}
%if 0%{?arch_flavor}
Provides:       %{pname}-devel = %version
Provides:       %{pname}-devel(default) = %version
%else
Provides:       %{pname}-devel(other) = %version
%endif
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
Requires:       lib%{name}-devel = %{version}

%description    devel-static
OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.

This package contains the static libraries.

%package      -n %{pname}-common-devel
Summary:        Development headers and libraries for OpenBLAS
Group:          Development/Libraries/C and C++
Requires:       (%{pname}-devel(default) or %{pname}-devel(other))
Obsoletes:      %{pname}-devel < %version
Obsoletes:      %{pname}-devel-headers < %version
Provides:       %{pname}-devel-headers = %version
Provides:       pkgconfig(openblas) = %version

%description  -n %{pname}-common-devel
OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.

This package contains headers for OpenBLAS.

%prep

%setup -q -n OpenBLAS-%{version}
%autopatch -p1
%ifarch s390
sed -i -e "s@m32@m31@" Makefile.system
%endif
sed -i -e '/FLDFLAGS = \|$(CC)\|$(CXX)/s@$@ $(LDFLAGS_TESTS)@' \
    test/Makefile ctest/Makefile utest/Makefile cpp_thread_test/Makefile

%if %{without hpc}
cp %{SOURCE1} .
%else
cp %{SOURCE2} .
%endif

# create baselibs.conf based on flavor
cat >  %{_sourcedir}/baselibs.conf <<EOF
lib%{name}%{?so_v}
    +%{p_libdir}/libopenblas.*\.so\.*
lib%{name}-devel
    +%{p_libdir}/libopenblas\.so
    requires -%{name}-<targettype>
    requires "lib%{name}%{?so_v}-<targettype> = <version>"
EOF

%build

# For static libraries use -ffat-lto-objects to make sure the 'regular'
# assembler code is generated as well as the intermediate code will be
# stripped during pre-packaging post-processing. Also, set ldflags_tests
# to speed up building of tests.
%if "%{?_lto_cflags}" != ""
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%global ldflags_tests -fno-lto
%endif

# disable lto for ppc64le, boo#1181733
%ifarch ppc64le
%define  _lto_cflags %{nil}
%endif

%if %{with hpc}
%hpc_debug
%hpc_setup_compiler
%endif

# Use DYNAMIC_ARCH everywhere - not sure about PPC?
# Use DYNAMIC_ARCH to build for multiple targets, use TARGET to specify
# the CPU model assumed for the common code. It should be set to the
# oldest CPU model one expects to encounter.
%global openblas_target DYNAMIC_ARCH=1
# We specify TARGET= to avoid compile-time CPU-detection (boo#1100677)
%ifarch %ix86 x86_64
%global openblas_target %openblas_target TARGET=CORE2
%define openblas_opt BUILD_BFLOAT16=1
%endif
%ifarch aarch64
%global openblas_target %openblas_target TARGET=ARMV8
%if 0%{?suse_version} < 1550
# Only enable targets without sve when using GCC < 9
%global openblas_target %openblas_target DYNAMIC_LIST="ARMV8 CORTEXA53 CORTEXA57 CORTEXA72 CORTEXA73 CORTEXA55 FALKOR THUNDERX THUNDERX2T99 TSV110 EMAG8180 NEOVERSEN1 NEOVERSEV1 THUNDERX3T110"
%endif
%define openblas_opt BUILD_BFLOAT16=1
%endif
%ifarch s390 s390x
%global openblas_target %openblas_target TARGET=ZARCH_GENERIC
%endif
%ifarch ppc64le
%global openblas_target %openblas_target TARGET=POWER8
%define openblas_opt BUILD_BFLOAT16=1
%endif
%ifarch ppc64
%global openblas_target %openblas_target TARGET=POWER8
%endif
%ifarch riscv64
%global openblas_target %openblas_target TARGET=RISCV64_GENERIC
%endif
# force -mvsx for ppc64 to avoid build failure:
# ../kernel/power/sasum_microk_power8.c:41:3: error: '__vector' undeclared (first use in this function); did you mean '__cpow'?
# TODO why is it required ? (and not for ppc64le)
%ifarch ppc64
%global addopt -mvsx
%endif
%global addopt %{?addopt} -fno-strict-aliasing

# Make serial, threaded and OpenMP versions

# Calculate process limits
%limit_build -m 1500
[[ -n $_threads ]] && jobs=$_threads
[[ -z $jobs ]] && jobs=1
# NEVER use %%_smp_mflags with top level make:
# set MAKE_NB_JOBS instead and let the build do the work!
make MAKE_NB_JOBS=$jobs %{?openblas_target} %{?build_flags} \
     %{?openblas_opt} \
     COMMON_OPT="%{optflags} %{?addopt}" \
     NUM_THREADS=%{num_threads} V=1 \
     OPENBLAS_LIBRARY_DIR=%{p_libdir} \
     OPENBLAS_INCLUDE_DIR=%{p_includedir} \
     OPENBLAS_CMAKE_DIR=%{p_cmakedir} \
     PREFIX=%{p_prefix} \
     %{!?with_hpc:LIBNAMESUFFIX=%flavor FC=gfortran CC=gcc%{?cc_v:-%{cc_v}} %{?cc_v:CEXTRALIB=""}} \
     %{?ldflags_tests:LDFLAGS_TESTS=%{ldflags_tests}} \
     %{?with_hpc:%{?cc_v:CC=gcc-%{cc_v} CEXTRALIB=""}}

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
%endif

# Fix cmake config file
sed -i 's|%{buildroot}||g' %{buildroot}%{p_cmakedir}/*.cmake
sed -i 's|_%{flavor}||g' %{buildroot}%{p_cmakedir}/*.cmake

# Put libraries in correct location
rm -rf %{buildroot}%{p_libdir}/lib%{name}*

# Install the serial library
install -D -p -m 755 lib%{name}.so %{buildroot}%{p_libdir}/lib%{pname}.so.0
install -D -p -m 644 lib%{name}.a %{buildroot}%{p_libdir}/lib%{pname}.a

# Fix source permissions (also applies to LAPACK)
find -name \*.f -exec chmod 644 {} +

# Dummy target for update-alternatives
install -d %{buildroot}/%{_sysconfdir}/alternatives
ln -sf %{_sysconfdir}/alternatives/libblas.so.3 %{buildroot}/%{_libdir}/libblas.so.3
ln -sf %{_sysconfdir}/alternatives/libcblas.so.3 %{buildroot}/%{_libdir}/libcblas.so.3
ln -sf %{_sysconfdir}/alternatives/liblapack.so.3 %{buildroot}/%{_libdir}/liblapack.so.3
ln -sf %{_sysconfdir}/alternatives/liblapacke.so.3 %{buildroot}/%{_libdir}/liblapacke.so.3
ln -sf %{_sysconfdir}/alternatives/openblas-default %{buildroot}/%{_libdir}/openblas-default
ln -s lib%{pname}.so.%{so_v} %{buildroot}%{p_libdir}/lib%{pname}.so
ln -s %{p_libdir}/lib%{pname}.so.%{so_v} %{buildroot}/%{_libdir}/lib%{name}.so.%{so_v}
ln -s %{p_libdir}/lib%{pname}.so %{buildroot}/%{_libdir}/lib%{name}.so
ln -s %{_libdir}/openblas-default %{buildroot}%{_sysconfdir}/alternatives/openblas-default
ln -s %{_sysconfdir}/alternatives/openblas-default/lib%{pname}.so.%{so_v} %{buildroot}%{_libdir}/lib%{pname}.so.%{so_v}
%if 0%{?build_devel}
ln -s lib%{pname}.so.%{so_v} %{buildroot}%{_libdir}/lib%{pname}.so
install -d %{buildroot}%{_libdir}/pkgconfig/
ln -s %{_sysconfdir}/alternatives/openblas-default/pkgconfig/openblas.pc %{buildroot}%{_libdir}/pkgconfig/
install -d %{buildroot}/%{_libdir}/cmake
ln -s %{_sysconfdir}/alternatives/openblas-default/cmake/openblas %{buildroot}/%{_libdir}/cmake/
%endif

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

# Ensure directory used in older versions are replaced by symlink properly
%pre -n %{pname}-common-devel
d=%{_libdir}/cmake/openblas
[ -d $d -a ! -L $d -a "$(rpm -q --qf '%%{NAME}' -f $d 2>/dev/null)" = "openblas-devel" ] \
    && { n=$(mktemp -d $(dirname $d)/tmpd-XXXXX); mv $d $n; rm -rf $n; } || true

%post -n lib%{name}%{so_v}
%{_sbindir}/update-alternatives --install \
   %{_libdir}/openblas-default openblas-default %{p_libdir} %openblas_so_prio
for lib in libblas.so.3 libcblas.so.3 liblapack.so.3 liblapacke.so.3; do
    %{_sbindir}/update-alternatives --install \
     %{_libdir}/${lib} ${lib} %{_libdir}/lib%{pname}.so.%{so_v}  20
done
/sbin/ldconfig

%postun -n lib%{name}%{so_v}
if [ ! -f %{p_libdir}/lib%{pname}.so.%{so_v} ]; then
    for lib in libblas.so.3 libcblas.so.3 liblapack.so.3 liblapacke.so.3; do
	%{_sbindir}/update-alternatives --remove ${lib} %{_libdir}/lib%{pname}.so.%{so_v}
    done
fi
if [ ! -d %{p_libdir} ]; then
    %{_sbindir}/update-alternatives --remove openblas-default %{p_libdir}
fi
/sbin/ldconfig

%posttrans -n lib%{name}%{so_v}
if [ "$1" = 0 ] ; then
  if  [ ! -d %{_libdir}/openblas-default ] ; then
      %{_sbindir}/update-alternatives --auto openblas-default
  fi
  for lib in libblas.so.3 libcblas.so.3 liblapack.so.3 liblapacke.so.3; do
      if ! [ -f %{_libdir}/${lib} ] ; then
	  %{_sbindir}/update-alternatives --auto ${lib}
      fi
  done
fi

%else

%postun -n lib%{name}
%hpc_module_delete_if_default

%endif

%files -n lib%{name}%{?so_v}
%defattr(-,root,root,-)
%{p_libdir}/lib%{pname}.so.0
%if %{without hpc}
%dir %{p_libdir}
%{_libdir}/openblas-default
%{_libdir}/lib%{name}.so.%{so_v}
%{_libdir}/lib%{pname}.so.%{so_v}
%ghost %{_libdir}/libblas.so.3
%ghost %{_libdir}/libcblas.so.3
%ghost %{_libdir}/liblapack.so.3
%ghost %{_libdir}/liblapacke.so.3
%ghost %{_sysconfdir}/alternatives/openblas-default
%ghost %{_sysconfdir}/alternatives/libblas.so.3
%ghost %{_sysconfdir}/alternatives/libcblas.so.3
%ghost %{_sysconfdir}/alternatives/liblapack.so.3
%ghost %{_sysconfdir}/alternatives/liblapacke.so.3
%else
%hpc_dirs
%{p_libdir}/libopenblas*r*.so
%hpc_modules_files
%endif

%files -n lib%{name}-devel
%{p_libdir}/lib%{pname}.so
%{p_cmakedir}/
%if %{with hpc}
%license LICENSE
%doc Changelog.txt GotoBLAS* README.md README.HPC.SUSE
%hpc_pkgconfig_file
%{p_includedir}/
%else
%{_libdir}/lib%{name}.so
%dir %{p_libdir}/cmake
%dir %{p_libdir}/pkgconfig
%{p_libdir}/pkgconfig
%endif

%files devel-static
%{p_libdir}/libopenblas*.a

%if 0%{?build_devel}
%files -n %{pname}-common-devel
%license LICENSE
%doc Changelog.txt GotoBLAS* README.md README.SUSE
%{_libdir}/lib%{pname}.so
%{p_includedir}/
%{_libdir}/pkgconfig/openblas.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/openblas
%endif

%changelog
