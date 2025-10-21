#
# spec file for package openblas
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

%undefine sha1
%define so_v 0
%define pname openblas

%bcond_with ringdisabled

%if 0%{?suse_version} > 1500
%define a_x _%{_arch}
%endif

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
%endif

%if "%flavor" == "pthreads"
%define build_flags USE_THREAD=1 USE_OPENMP=0
 %ifarch %ix86 x86_64
 %define arch_flavor 1
 %define openblas_so_prio 50
 %else
 %define openblas_so_prio 20
 %endif
%endif

%if "%flavor" == "openmp"
 %ifarch %ix86 x86_64
 %define openblas_so_prio 20
 %else
 %define arch_flavor 1
 %define openblas_so_prio 50
 %endif
%endif

%ifarch ppc64le
%if 0%{?c_f_ver} > 9
%else
%if 0%{?sle_version} == 150700
%define cc_v 14
%endif
%if 0%{?sle_version} == 150600
%define cc_v 13
%endif
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
%ifarch x86_64
 %if 0%{?sle_version} && 0%{?c_f_ver} < 11
  %define dynamic_list DYNAMIC_LIST="PRESCOTT CORE2 NEHALEM BARCELONA SANDYBRIDGE BULLDOZER PILEDRIVER STEAMROLLER EXCAVATOR HASWELL ZEN SKYLAKEX"
 %endif
%endif

%define so_a %{so_v}
%if 0%{!?package_name:1}
%define package_name  %{pname}_%{flavor}
%endif
%define p_prefix %_prefix
%define p_includedir %_includedir/%pname
%define p_libdir %_libdir/openblas%{?flavor:-%{flavor}}
%define p_testdir %_libexecdir/openblas%{?flavor:-%{flavor}}/tests
%define p_cmakedir %{p_libdir}/cmake/%{pname}
%define num_threads 64

%if 0%{?sha1:1}
%define v_string %{sha1}
%else
%define v_string v%{version}
%endif

Name:           %{package_name}
Version:        0.3.29
Release:        0
Summary:        An optimized BLAS library based on GotoBLAS2
License:        BSD-3-Clause
Group:          Productivity/Scientific/Math
URL:            http://www.openblas.net
Source0:        https://github.com/xianyi/OpenBLAS/archive/%{v_string}.tar.gz#/OpenBLAS-%{version}%{?sha1:_%{sha1}}.tar.gz
Source1:        README.SUSE
Source3:        openblas_tests.sh.in
Source4:        openblas.rpmlintrc
# PATCH port
Patch102:       Handle-s390-correctly.patch
Patch103:       openblas-ppc64be_up2_p8.patch
Patch104:       Restore-the-non-vectorized-code-from-before-PR4880-for-POWER8.patch

#BuildRequires:  cmake
BuildRequires:  memory-constraints
%if 0%{?cc_v:1}
BuildRequires:  gcc%{?cc_v}-fortran
%endif
BuildRequires:  gcc-fortran
BuildRequires:  update-alternatives
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description
OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.

%package     -n lib%{name}%{so_a}
Summary:        An optimized BLAS library based on GotoBLAS2, %{flavor} version
Group:          System/Libraries
Requires(post): update-alternatives
Requires(post): coreutils
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

%description -n lib%{name}%{so_a}
OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.

%package     -n lib%{name}-devel
Summary:        Development libraries for OpenBLAS, %{flavor} version
Group:          Development/Libraries/C and C++
Requires:       %{pname}-common-devel = %{version}
Requires:       lib%{name}%{so_a} = %{version}
%if 0%{?arch_flavor}
Provides:       %{pname}-devel = %version
Provides:       %{pname}-devel(default) = %version
%else
Provides:       %{pname}-devel(other) = %version
%endif

%description -n lib%{name}-devel
OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.

This package contains the development libraries for serial OpenBLAS version.

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
Requires(pre):  coreutils
Requires(post): coreutils
Obsoletes:      %{pname}-devel < %version
Obsoletes:      %{pname}-devel-headers < %version
Provides:       %{pname}-devel-headers = %version
Provides:       pkgconfig(openblas) = %version

%description  -n %{pname}-common-devel
OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.

This package contains headers for OpenBLAS.

%package   tests
Summary:        Unit Tests for openblas library
Group:          Development/Libraries/C and C++

%description tests
OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.

This package contains test binaries.

%prep

%setup -q -n OpenBLAS-%{?sha1:%{sha1}}%{!?sha1:%{version}}
%autopatch -p1
%ifarch s390
sed -i -e "s@m32@m31@" Makefile.system
%endif
sed -i -e '/FLDFLAGS = \|$(CC)\|$(CXX)/s@$@ $(LDFLAGS_TESTS)@' \
    test/Makefile ctest/Makefile utest/Makefile cpp_thread_test/Makefile
grep -q .note.GNU-stack cpuid.S || echo '.section        .note.GNU-stack,"",@progbits' >> cpuid.S
# Disable sgemmt and dgemmt tests on ppc64le when using gcc13
%if "%{?_arch}" == "ppc64le" && 0%{?gcc_version} == 13
%if %{suse_version} >= 1600 && !0%{?is_opensuse}
# with openblas_target POWER9 the tests work fine
%else
sed -i -e '/^OBJS_EXT+=/s@[^= ]*/test_sgemmt.o *@@' utest/Makefile
sed -i -e '/^OBJS_EXT+=/s@[^= ]*/test_dgemmt.o *@@' utest/Makefile
%endif
%endif

cp %{SOURCE1} .

# create baselibs.conf based on flavor
cat >  %{_sourcedir}/baselibs.conf <<EOF
lib%{name}%{so_a}
    +%{p_libdir}/libopenblas.*\.so\.*
lib%{name}-devel
    +%{p_libdir}/libopenblas\.so
    requires -%{name}-<targettype>
    requires "lib%{name}%{?so_a}-<targettype> = <version>"
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
%define openblas_opt BUILD_BFLOAT16=1
%endif
%ifarch s390 s390x
%global openblas_target %openblas_target TARGET=ZARCH_GENERIC
%endif
%ifarch ppc64le
%if %{suse_version} >= 1600 && !0%{?is_opensuse}
%global openblas_target %openblas_target TARGET=POWER9
%else
%global openblas_target %openblas_target TARGET=POWER8
%endif
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
%global addopt %{?addopt} -fno-strict-aliasing -Wa,--noexecstack -Wl,-z,noexecstack

# Make serial, threaded and OpenMP versions

# Calculate process limits
%limit_build -m 1500
[[ -n $_threads ]] && jobs=$_threads
[[ -z $jobs ]] && jobs=1
# NEVER use %%_smp_mflags with top level make:
# set MAKE_NB_JOBS instead and let the build do the work!
# Do not use LIBNAMESUFFIX for new builds as it will not allow
# the different flavors to be plugin replacements of each other
%if 0%{?suse_version} <= 1500
%define libnamesuffix LIBNAMESUFFIX=_%{flavor}
%endif
make MAKE_NB_JOBS=$jobs %{?openblas_target} %{?build_flags} \
     %{?openblas_opt} \
     COMMON_OPT="%{optflags} %{?addopt}" \
     NUM_THREADS=%{num_threads} V=1 \
     OPENBLAS_LIBRARY_DIR=%{p_libdir} \
     OPENBLAS_INCLUDE_DIR=%{p_includedir} \
     OPENBLAS_BINARY_DIR=%{p_testdir} \
     OPENBLAS_CMAKE_DIR=%{p_cmakedir} \
     PREFIX=%{p_prefix} \
     %{?dynamic_list} \
     %{?libnamesuffix} FC=gfortran CC=gcc%{?cc_v:-%{cc_v}} %{?cc_v:CEXTRALIB=""} \
     %{?ldflags_tests:LDFLAGS_TESTS=%{ldflags_tests}}

%install

# Install library and headers
# Pass NUM_THREADS again, as it is not propagated from the build step
# https://github.com/OpenMathLib/OpenBLAS/issues/4275
mkdir -p %{buildroot}/%{p_testdir}
%make_install install_tests %{?openblas_target} %{?build_flags} \
    %{?openblas_opt} \
    NUM_THREADS=%{num_threads} \
    OPENBLAS_LIBRARY_DIR=%{p_libdir} \
    OPENBLAS_INCLUDE_DIR=%{p_includedir} \
    OPENBLAS_BINARY_DIR=%{p_testdir} \
    OPENBLAS_CMAKE_DIR=%{p_cmakedir} \
    %{?libnamesuffix} FC=gfortran CC=gcc%{?cc_v:-%{cc_v}} %{?cc_v:CEXTRALIB=""} \
    %{?ldflags_tests:LDFLAGS_TESTS=%{ldflags_tests}} \
    PREFIX=%{p_prefix}
sed -e 's#@FLAVOR@#%{flavor}#' \
    -e 's#@COMPILER@#%{?compiler_family:%compiler_family}}#' \
    < %{S:3} > %{buildroot}/%{p_testdir}/openblas_tests.sh
chmod 0755 %{buildroot}/%{p_testdir}/openblas_tests.sh
for i in %{buildroot}/%{p_testdir}/*; do
    case $i in
	*.dat|*in*) chmod 0644 $i;;
	*)     chmod 0755 $i;;
    esac
done

# Delete info about OBS host cpu
%ifarch %ix86 x86_64
 sed -i '/#define OPENBLAS_NEEDBUNDERSCORE/,/#define OPENBLAS_VERSION/{//!d}' \
    %{buildroot}%{p_includedir}/openblas_config.h
%endif

%if 0%{!?build_devel:1}
# We need the includes only once
rm -rf %{buildroot}%{p_includedir}/
%endif

# Fix cmake config file
sed -i 's|%{buildroot}||g' %{buildroot}%{p_cmakedir}/*.cmake
sed -i 's|_%{flavor}||g' %{buildroot}%{p_cmakedir}/*.cmake

# Remove library type specific so. This is solved differently.
# Needed when not using LIBNAMESUFFIX.
%if 0%{!?libnamesuffix:1}
rm -f %{buildroot}%{p_libdir}/lib%{pname}*-r%{version}.so
rm -f %{buildroot}%{p_libdir}/lib%{pname}*-r%{version}.a
rm -f %{buildroot}%{p_libdir}/lib%{pname}.so
%endif
# Instead set up new 'devel'-link for flavor:
ln -s lib%{pname}.so.%{so_v} %{buildroot}%{p_libdir}/lib%{pname}.so

# Put libraries in correct location
rm -rf %{buildroot}%{p_libdir}/lib%{name}*

# Install library
%define orgname %{?libnamesuffix:%{name}}%{!?libnamesuffix:%{pname}}
install -D -p -m 755 lib%{orgname}.so %{buildroot}%{p_libdir}/lib%{pname}.so.%{so_v}
install -D -p -m 644 lib%{orgname}.a %{buildroot}%{p_libdir}/lib%{pname}.a

# Fix source permissions (also applies to LAPACK)
find -name \*.f -exec chmod 644 {} +

# update-alternatives strategy in %%post:
# update-alternatives:
#  /usr/lib64/libblas.so.<so_v> -> /etc/alternatives/libblas.so.<so_v>_<arch> -> /usr/lib64/openblas-<flavor>/libblas.so.<so_v>
#  /usr/lib64/openblas-default -> /etc/alternatives/openblas-default_<arch> -> /usr/lib64/openblas-<flavor>
# directly - default shared lib in default location
#  /usr/lib64/libopenblas.so.<so_v> -> /usr/lib64/openblas_default/libopenblas.so.<so_v>
#  /usr/lib64/libopenblas.so -> libopenblas.so.<so_v>

install -d %{buildroot}/%{_sysconfdir}/alternatives
for link in openblas-default libblas.so.3 liblapack.so.3 libcblas.so.3 liblapacke.so.3; do
    ln -s %{_sysconfdir}/alternatives/${link}%{?a_x} %{buildroot}/%{_libdir}/${link}
done

%if 0%{?build_devel}
install -d %{buildroot}%{_libdir}/pkgconfig/
ln -s %{_sysconfdir}/alternatives/openblas-default%{?a_x}/pkgconfig/openblas.pc %{buildroot}%{_libdir}/pkgconfig/
install -d %{buildroot}/%{_libdir}/cmake
ln -s %{_sysconfdir}/alternatives/openblas-default%{?a_x}/cmake/openblas %{buildroot}/%{_libdir}/cmake/
%endif

# Compatibility Links
%if 0%{?libnamesuffix:1}
ln -s openblas-%{flavor}/lib%{pname}.so.%{so_v} %{buildroot}%{_libdir}/lib%{name}.so.%{so_v}
ln -s openblas-%{flavor}/lib%{pname}.so %{buildroot}%{_libdir}/lib%{name}.so
%endif

# Ensure directory used in older versions are replaced by symlink properly
%pre -n %{pname}-common-devel
d=%{_libdir}/cmake/openblas
[ -d $d -a ! -L $d -a "$(rpm -q --qf '%%{NAME}' -f $d 2>/dev/null)" = "openblas-devel" ] \
    && { n=$(mktemp -d $(dirname $d)/tmpd-XXXXX); mv $d $n; rm -rf $n; } || true

%post -n lib%{name}%{so_v}
# There's no way to determine if a setting exists, so just remove it and ignore errors
%{?a_x:%{_sbindir}/update-alternatives --remove-all openblas-default 2>/dev/null || true}
%{_sbindir}/update-alternatives --install \
   %{_libdir}/openblas-default openblas-default%{?a_x} %{p_libdir} %openblas_so_prio
# Cannot package this link - brp-25-symlink doesn't recognize links created by update-alternatives
ln -sf openblas-default/lib%{pname}.so.%{so_v} %{_libdir}/lib%{pname}.so.%{so_v}
for lib in libblas.so.3 libcblas.so.3 liblapack.so.3 liblapacke.so.3; do
    %{?a_x:%{_sbindir}/update-alternatives --remove-all ${lib} 2>/dev/null || true}
    %{_sbindir}/update-alternatives --install \
     %{_libdir}/${lib} ${lib}%{?a_x} %{p_libdir}/lib%{pname}.so.%{so_v}  20
done
/sbin/ldconfig

%post -n %{pname}-common-devel
ln -sf lib%{pname}.so.%{so_v} %{_libdir}/lib%{pname}.so

%postun -n lib%{name}%{so_v}
if [ ! -f %{p_libdir}/lib%{pname}.so.%{so_v} ]; then
    for lib in libblas.so.3 libcblas.so.3 liblapack.so.3 liblapacke.so.3; do
	%{_sbindir}/update-alternatives --remove ${lib}%{?a_x} %{_libdir}/lib%{pname}.so.%{so_v}
    done
fi
if [ ! -d %{p_libdir} ]; then
    %{_sbindir}/update-alternatives --remove openblas-default%{?a_x} %{p_libdir}
fi
/sbin/ldconfig

%files -n lib%{name}%{so_a}
%defattr(-,root,root,-)
%{p_libdir}/lib%{pname}.so.%{so_v}
%dir %{p_libdir}
%{?libnamesuffix:%{_libdir}/lib%{name}.so.%{so_v}}
# Created by %%post
%ghost %{_libdir}/lib%{pname}.so.%{so_v}
%ghost %{_libdir}/openblas-default
%ghost %{_libdir}/libblas.so.3
%ghost %{_libdir}/libcblas.so.3
%ghost %{_libdir}/liblapack.so.3
%ghost %{_libdir}/liblapacke.so.3
%ghost %{_sysconfdir}/alternatives/openblas-default%{?a_x}
%ghost %{_sysconfdir}/alternatives/libblas.so.3%{?a_x}
%ghost %{_sysconfdir}/alternatives/libcblas.so.3%{?a_x}
%ghost %{_sysconfdir}/alternatives/liblapack.so.3%{?a_x}
%ghost %{_sysconfdir}/alternatives/liblapacke.so.3%{?a_x}

%files -n lib%{name}-devel
%{p_libdir}/lib%{pname}.so
%{?libnamesuffix:%{_libdir}/lib%{name}.so}
%{p_cmakedir}/
%dir %{p_libdir}/cmake
%dir %{p_libdir}/pkgconfig
%{p_libdir}/pkgconfig

%files tests
%dir %{p_testdir}
%dir %{dirname:%{p_testdir}}
%{p_testdir}/*

%files devel-static
%{p_libdir}/libopenblas*.a

%if 0%{?build_devel}
%files -n %{pname}-common-devel
%license LICENSE
%doc Changelog.txt GotoBLAS* README.md README.SUSE
# created by %%post
%ghost %{_libdir}/lib%{pname}.so
%{p_includedir}/
%{_libdir}/pkgconfig/openblas.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/openblas
%endif

%changelog
