#
# spec file for package gcc7
#
# Copyright (c) 2025 SUSE LLC
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


# Ada currently fails to build on a few platforms, enable it only
# on those that work
%if %{suse_version} >= 1310
%if %{suse_version} >= 1330
%define ada_arch %ix86 x86_64 ppc ppc64 ppc64le s390 s390x ia64 aarch64
%else
%define ada_arch %ix86 x86_64 ppc ppc64 s390 ia64
%endif
%else
%define ada_arch %ix86 x86_64 ppc s390 ia64
%endif

%ifarch %ada_arch
%define build_ada 1
%else
%define build_ada 0
%endif

%define quadmath_arch %ix86 x86_64 ia64
%define tsan_arch x86_64 aarch64 ppc ppc64 ppc64le
%define asan_arch x86_64 %ix86 ppc ppc64 ppc64le s390 s390x %sparc %arm aarch64
%define itm_arch x86_64 %ix86 %arm aarch64 ppc ppc64 ppc64le s390 s390x %sparc
%define atomic_arch x86_64 %ix86 %arm aarch64 ppc ppc64 ppc64le s390 s390x %sparc m68k ia64 riscv64
%define lsan_arch x86_64 aarch64 ppc ppc64 ppc64le
%define ubsan_arch x86_64 %ix86 ppc ppc64 ppc64le s390 s390x %arm aarch64
%if 0%{?build_libvtv:1}
%define vtv_arch x86_64 %ix86
%endif
%define cilkrts_arch x86_64 %ix86
%if %{suse_version} >= 1310 && %{suse_version} < 1600
%define mpx_arch x86_64 %ix86
%endif

%define build_cp 1
%define build_fortran 1
%define build_objc 1
%define build_objcp 1
%ifarch riscv64
%define build_go 0
%else
%define build_go 1
%endif

%if %{build_objcp}
%define build_cp 1
%define build_objc 1
%endif

# For optional compilers only build C, C++, Fortran, Ada and Go
%if 0%{?build_optional_compiler_languages:1}
%define build_objc 0
%define build_objcp 0
%endif

%ifarch x86_64
%define build_hsa 1
%define build_nvptx 1
%else
%define build_hsa 0
%define build_nvptx 0
%endif

# Enable plugins just for Tumbleweed, not for SLES
%if 0%{!?sle_version:1}
%define enable_plugins 1
%else
%define enable_plugins 0
%endif

# Shared library SONAME versions
%ifarch hppa
%define libgcc_s 4
%else
%ifarch m68k
%define libgcc_s 2
%else
%define libgcc_s 1
%endif
%endif
%define libgomp_sover 1
%define libstdcxx_sover 6
%define libobjc_sover 4
%define libgfortran_sover 4
%define libquadmath_sover 0
%define libasan_sover 4
%define libtsan_sover 0
%define libatomic_sover 1
%define libitm_sover 1
%define libubsan_sover 0
%define liblsan_sover 0
%define libvtv_sover 0
%define libcilkrts_sover 5
%define libgo_sover 11
%define libmpx_sover 2
%define libmpxwrappers_sover 2

# Shared library package suffix
# This is used for the "non-standard" set of libraries, the standard
# being defined by %%product_libs_gcc_ver, the GCC version that should
# provide un-suffixed shared library packages following the shared-library
# policy.  Even suffixed variants should provide the shared-library policy
# mandated names and ensure they conflict with each other.
# Individual shared libraries can be directed to be built from individual
# gcc versions by defining %%product_libs_gcc_ver_libgcc_s1 for example,
# generally %%product_libs_gcc_ver_%%name%%sover, similarly.

%define itsme7 1
%define plv_ %{!?product_libs_gcc_ver:7}%{?product_libs_gcc_ver}
%define plv() %{expand:%%{!?itsme%{expand:%%{!?product_libs_gcc_ver_%{1}%{2}:%%{plv_}}%%{?product_libs_gcc_ver_%{1}%{2}}}:-gcc7}}

%define libgcc_s_suffix %{plv libgcc_s %{libgcc_s}}
%define libgomp_suffix %{plv libgomp %{libgomp_sover}}
%define libstdcxx_suffix %{plv libstdcxx %{libstdcxx_sover}}
%define libobjc_suffix %{plv libobjc %{libobjc_sover}}
%define libgfortran_suffix %{plv libgfortran %{libgfortran_sover}}
%define libquadmath_suffix %{plv libquadmath %{libquadmath_sover}}
%define libasan_suffix %{plv libasan %{libasan_sover}}
%define libtsan_suffix %{plv libtsan %{libtsan_sover}}
%define libatomic_suffix %{plv libatomic %{libatomic_sover}}
%define libitm_suffix %{plv libitm %{libitm_sover}}
%define libubsan_suffix %{plv libubsan %{libubsan_sover}}
%define liblsan_suffix %{plv liblsan %{liblsan_sover}}
%define libvtv_suffix %{plv libvtv %{libvtv_sover}}
%define libcilkrts_suffix %{plv libcilkrts %{libcilkrts_sover}}
%define libgo_suffix %{plv libgo %{libgo_sover}}
%define libmpx_suffix %{plv libmpx %{libmpx_sover}}
%define libmpxwrappers_suffix %{plv libmpxwrappers %{libmpx_sover}}

# libFOO-devel package suffix
%define libdevel_suffix -gcc7

%if %{suse_version} >= 1220
%define selfconflict() %1
%else
%define selfconflict() otherproviders(%1)
%endif

Name:           gcc7
BuildRequires:  xz
# With generated files in src we could drop the following
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gettext-devel
%if %{suse_version} > 1220
BuildRequires:  makeinfo
%else
BuildRequires:  texinfo
%endif
# until here, but at least renaming and patching info files breaks this
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel-32bit
BuildRequires:  mpc-devel
BuildRequires:  mpfr-devel
BuildRequires:  perl
BuildRequires:  zlib-devel
%if %{suse_version} >= 1230
BuildRequires:  isl-devel
%endif
%if %{build_ada}
%if 0%{?gcc_version:%{gcc_version}} > 7
%define hostsuffix %{binsuffix}
BuildRequires:  gcc7-ada
BuildRequires:  gcc7-c++
%else
%if %{suse_version} < 1310
%define hostsuffix -4.8
BuildRequires:  gcc48-ada
BuildRequires:  gcc48-c++
%else
%define hostsuffix %{nil}
BuildRequires:  gcc-ada
%endif
%endif
%endif
%if 0%{?building_testsuite:1}
# For building the libstdc++ API reference
BuildRequires:  doxygen
BuildRequires:  graphviz
%endif
%ifarch ia64
BuildRequires:  libunwind-devel
%endif
%if 0%{?run_tests:1}
BuildRequires:  dejagnu
BuildRequires:  expect
BuildRequires:  gdb
%if %{build_nvptx}
BuildRequires:  cross-nvptx-gcc7
BuildRequires:  cross-nvptx-newlib7-devel
%endif
%endif
#!BuildIgnore: gcc-PIE

%define separate_bi32 0
%define separate_bi64 0
%if 0%{!?disable_32bit:1}
%ifarch ppc sparcv9
%define separate_bi64 1
%endif
%ifarch x86_64 s390x ppc64 sparc64
%define separate_bi32 1
%endif
%endif

# Define two macros to trigger -32bit or -64bit package variants
%define separate_biarch 0
%if %{separate_bi32}
%define separate_biarch 1
%define separate_biarch_suffix -32bit
%endif
%if %{separate_bi64}
%define separate_biarch 1
%define separate_biarch_suffix -64bit
%endif

%ifarch aarch64 x86_64 ia64 s390x alpha ppc64 ppc64le sparc64
# 64-bit is primary build target
%define build_primary_64bit 1
%else
%define build_primary_64bit 0
%endif

%define biarch_targets x86_64 s390x powerpc64 powerpc sparc sparc64

URL:            https://gcc.gnu.org/
Version:        7.5.0+r278197
Release:        0
%define gcc_dir_version %(echo %version | sed 's/+.*//' | cut -d '.' -f 1)
%define gcc_snapshot_revision %(echo %version | sed 's/[3-9]\.[0-9]\.[0-6]//' | sed 's/+/-/')
%define binsuffix -7

%if !0%{?building_testsuite:1}
Requires:       binutils
Requires:       cpp7 = %{version}-%{release}
Requires:       glibc-devel
Requires:       libgcc_s%{libgcc_s} >= %{version}-%{release}
Requires:       libgomp%{libgomp_sover} >= %{version}-%{release}
%ifarch %asan_arch
Requires:       libasan%{libasan_sover} >= %{version}-%{release}
%endif
%ifarch %tsan_arch
%if %{build_primary_64bit}
Requires:       libtsan%{libtsan_sover} >= %{version}-%{release}
%endif
%endif
%ifarch %atomic_arch
Requires:       libatomic%{libatomic_sover} >= %{version}-%{release}
%endif
%ifarch %itm_arch
Requires:       libitm%{libitm_sover} >= %{version}-%{release}
%endif
%ifarch %cilkrts_arch
Requires:       libcilkrts%{libcilkrts_sover} >= %{version}-%{release}
%endif
%ifarch %lsan_arch
%if %{build_primary_64bit}
Requires:       liblsan%{liblsan_sover} >= %{version}-%{release}
%endif
%endif
%ifarch %ubsan_arch
Requires:       libubsan%{libubsan_sover} >= %{version}-%{release}
%endif
%ifarch %vtv_arch
Requires:       libvtv%{libvtv_sover} >= %{version}-%{release}
%endif
%ifarch %mpx_arch
Requires:       libmpx%{libmpx_sover} >= %{version}-%{release}
Requires:       libmpxwrappers%{libmpxwrappers_sover} >= %{version}-%{release}
%endif
Suggests:       gcc7-info gcc7-locale
%endif

Group:          Development/Languages/C and C++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         gcc-%{version}.tar.xz
Source1:        change_spec
Source3:        gcc7-rpmlintrc
Source4:        README.First-for.SuSE.packagers
Source5:        nvptx-newlib.tar.xz
Patch2:         gcc-add-defaultsspec.diff
Patch5:         tls-no-direct.diff
Patch6:         gcc43-no-unwind-tables.diff
Patch7:         gcc48-libstdc++-api-reference.patch
Patch9:         gcc48-remove-mpfr-2.4.0-requirement.patch
Patch10:        gcc5-no-return-gcc43-workaround.patch
Patch11:        gcc7-remove-Wexpansion-to-defined-from-Wextra.patch
Patch12:        gcc7-stack-probe.diff
Patch14:        gcc7-pr82248.diff
Patch15:        gcc7-avoid-fixinc-error.diff
Patch17:        gcc7-flive-patching.patch
Patch18:        gcc7-bsc1146475.patch
Patch19:        gcc7-pr85887.patch
Patch20:        gcc7-bsc1160086.patch
Patch21:        gcc7-pr92154.patch
Patch22:        gcc7-pr93246.patch
Patch23:        gcc7-pr92692.patch
Patch24:        gcc48-bsc1161913.patch
Patch25:        gcc7-pr93965.patch
Patch26:        gcc7-pr93888.patch
Patch27:        gcc7-pr94148.patch
Patch29:        gcc7-pr97535.patch
Patch30:        gcc7-pr88522.patch
Patch31:        gcc7-testsuite-fixes.patch
Patch32:        gcc7-pr81942.patch
Patch33:        gcc7-sanitizer-cyclades.patch
Patch34:        gcc7-ada-MINSTKSZ.patch
Patch35:        gcc7-pr55917.patch
Patch36:        gcc7-ada-Target_Name.patch
Patch37:        gcc7-pr78263.patch
Patch38:        gcc7-libsanitizer-cherry-pick-9cf13067cb5088626ba7-from-u.patch
Patch39:        gcc7-libgo-don-t-include-linux-fs.h-when-building-gen-sys.patch
Patch40:        gcc7-pr72764.patch
Patch41:        gcc7-pr89124.patch
Patch42:        libgcc-riscv-div.patch
Patch43:        gcc7-aarch64-bsc1214052.patch
Patch44:        gcc7-aarch64-untyped_call.patch
Patch45:        gcc7-lra-elim.patch
Patch46:        gcc7-bsc1216488.patch
Patch47:        gcc7-pr87723.patch
Patch48:        gcc7-pr82463.patch
Patch49:        gcc7-bsc1239566.patch
Patch50:        gcc7-enable-mpx-in-as.patch
# A set of patches from the RH srpm
Patch51:        gcc41-ppc32-retaddr.patch
# Some patches taken from Debian
Patch60:        gcc44-textdomain.patch
Patch61:        gcc44-rename-info-files.patch
# Feature backports
Patch100:       gcc7-aarch64-moutline-atomics.patch
Patch101:       gcc7-fix-retrieval-of-testnames.patch
Patch102:       gcc7-aarch64-sls-miti-1.patch
Patch103:       gcc7-aarch64-sls-miti-2.patch
Patch104:       gcc7-aarch64-sls-miti-3.patch
Patch105:       gcc7-pfe-0001-Backport-Add-entry-for-patchable_function_entry.patch
Patch106:       gcc7-pfe-0002-Backport-Skip-fpatchable-function-entry-tests-for-nv.patch
Patch107:       gcc7-pfe-0003-Backport-Error-out-on-nvptx-for-fpatchable-function-.patch
Patch108:       gcc7-pfe-0004-Backport-Adapt-scan-assembler-times-for-alpha.patch
Patch109:       gcc7-pfe-0005-Backport-patchable_function_entry-decl.c-Use-3-NOPs-.patch
Patch110:       gcc7-pfe-0006-Backport-IBM-Z-Use-the-dedicated-NOP-instructions-fo.patch
Patch111:       gcc7-pfe-0007-Backport-Add-regex-to-search-for-uppercase-NOP-instr.patch
Patch112:       gcc7-pfe-0008-Backport-ICE-segmentation-fault-with-patchable_funct.patch
Patch113:       gcc7-pfe-0009-Backport-patchable_function_entry-decl.c-Pass-mcpu-g.patch
Patch114:       gcc7-pfe-0010-Backport-patchable_function_entry-decl.c-Do-not-run-.patch
Patch115:       gcc7-pfe-0011-Backport-patchable_function_entry-decl.c-Add-fno-pie.patch
Patch116:       gcc7-pfe-0012-Backport-PR-c-89946-ICE-in-assemble_start_function-a.patch
Patch117:       gcc7-pfe-0013-Backport-targhooks.c-default_print_patchable_functio.patch
Patch118:       gcc7-pfe-0014-Backport-Align-__patchable_function_entries-to-POINT.patch
Patch119:       gcc7-pfe-0015-Backport-Fix-PR-93242-patchable-function-entry-broke.patch
Patch120:       gcc7-pfe-0016-Backport-Fix-patchable-function-entry-on-arc.patch
Patch121:       gcc7-pfe-0017-Backport-Add-patch_area_size-and-patch_area_entry-to.patch
Patch122:       gcc7-pfe-0018-Backport-testsuite-Adjust-patchable_function-tests-f.patch
Patch123:       gcc7-pfe-0019-Backport-Use-the-section-flag-o-for-__patchable_func.patch
Patch124:       gcc7-pfe-0020-Backport-varasm-Fix-up-__patchable_function_entries-.patch
Patch125:       gcc7-pfe-0021-Backport-rs6000-Avoid-fpatchable-function-entry-regr.patch
Patch126:       gcc7-pfe-0022-Fix-unwinding-issues-when-pfe-is-enabled.patch
Patch127:       gcc7-pr88345-min-func-alignment.diff

License:        GPL-3.0-or-later
Summary:        The GNU C Compiler and Support Files

%description
Core package for the GNU Compiler Collection, including the C language
frontend.

Language frontends other than C are split to different sub-packages,
namely gcc-ada, gcc-c++, gcc-fortran, gcc-obj, gcc-obj-c++ and gcc-go.

%package -n gcc7-32bit
Summary:        The GNU C Compiler 32bit support
Group:          Development/Languages/C and C++
Requires:       gcc7 = %{version}-%{release}
Requires:       libgcc_s%{libgcc_s}-32bit >= %{version}-%{release}
Requires:       libgomp%{libgomp_sover}-32bit >= %{version}-%{release}
%ifarch %asan_arch
Requires:       libasan%{libasan_sover}-32bit >= %{version}-%{release}
%endif
%ifarch %atomic_arch
Requires:       libatomic%{libatomic_sover}-32bit >= %{version}-%{release}
%endif
%ifarch %itm_arch
Requires:       libitm%{libitm_sover}-32bit >= %{version}-%{release}
%endif
%ifarch %cilkrts_arch
Requires:       libcilkrts%{libcilkrts_sover}-32bit >= %{version}-%{release}
%endif
%ifarch %ubsan_arch
Requires:       libubsan%{libubsan_sover}-32bit >= %{version}-%{release}
%endif
%ifarch %vtv_arch
Requires:       libvtv%{libvtv_sover}-32bit >= %{version}-%{release}
%endif
%ifarch %mpx_arch
Requires:       libmpx%{libmpx_sover}-32bit >= %{version}-%{release}
Requires:       libmpxwrappers%{libmpxwrappers_sover}-32bit >= %{version}-%{release}
%endif
Requires:       glibc-devel-32bit

%description -n gcc7-32bit
This package contains 32bit support for the GNU Compiler Collection.

%package -n gcc7-64bit
Summary:        The GNU C Compiler 64bit support
Group:          Development/Languages/C and C++
Requires:       gcc7 = %{version}-%{release}
Requires:       libgcc_s%{libgcc_s}-64bit >= %{version}-%{release}
Requires:       libgomp%{libgomp_sover}-64bit >= %{version}-%{release}
%ifarch %asan_arch
Requires:       libasan%{libasan_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %tsan_arch
Requires:       libtsan%{libtsan_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %atomic_arch
Requires:       libatomic%{libatomic_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %itm_arch
Requires:       libitm%{libitm_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %cilkrts_arch
Requires:       libcilkrts%{libcilkrts_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %lsan_arch
Requires:       liblsan%{liblsan_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %ubsan_arch
Requires:       libubsan%{libubsan_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %vtv_arch
Requires:       libvtv%{libvtv_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %mpx_arch
Requires:       libmpx%{libmpx_sover}-64bit >= %{version}-%{release}
Requires:       libmpxwrappers%{libmpxwrappers_sover}-64bit >= %{version}-%{release}
%endif
Requires:       glibc-devel-64bit

%description -n gcc7-64bit
This package contains 64bit support for the GNU Compiler Collection.

%package devel
Summary:        GCC plugins development enviroment
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc7 = %{version}-%{release}
Requires:       gmp-devel
Requires:       mpc-devel

%description devel
Files required for developing and compiling GCC plugins.

%package locale
Summary:        Locale Data for the GNU Compiler Collection
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc7 = %{version}-%{release}

%description locale
Locale data for the GNU Compiler Collection (GCC) to give error message
in the current locale.

%package c++
Summary:        The GNU C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc7 = %{version}-%{release}
Requires:       gcc7-c++ = %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix} = %{version}-%{release}

%description c++
This package contains the GNU compiler for C++.

%package c++-32bit
Summary:        The GNU C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc7-32bit = %{version}-%{release}
Requires:       gcc7-c++ = %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}-32bit = %{version}-%{release}

%description c++-32bit
This package contains the GNU compiler for C++.

%package c++-64bit
Summary:        The GNU C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc7-64bit = %{version}-%{release}
Requires:       gcc7-c++ = %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}-64bit = %{version}-%{release}

%description c++-64bit
This package contains the GNU compiler for C++.

%package -n libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}
Summary:        Include Files and Libraries mandatory for Development
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          Development/Languages/C and C++
Requires:       glibc-devel
Requires:       libstdc++%{libstdcxx_sover} >= %{version}-%{release}
%ifarch ia64
Requires:       libunwind-devel
%endif

%description -n libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}
This package contains all the headers and libraries of the standard C++
library. It is needed for compiling C++ code.

%package -n libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}-32bit
Summary:        Include Files and Libraries mandatory for Development
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          Development/Languages/C and C++
Requires:       glibc-devel-32bit
Requires:       libstdc++%{libstdcxx_sover}-32bit >= %{version}-%{release}
%ifarch ia64
Requires:       libunwind-devel
%endif

%description -n libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}-32bit
This package contains all the headers and libraries of the standard C++
library. It is needed for compiling C++ code.

%package -n libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}-64bit
Summary:        Include Files and Libraries mandatory for Development
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          Development/Languages/C and C++
Requires:       glibc-devel-64bit
Requires:       libstdc++%{libstdcxx_sover}-64bit >= %{version}-%{release}
%ifarch ia64
Requires:       libunwind-devel
%endif

%description -n libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}-64bit
This package contains all the headers and libraries of the standard C++
library. It is needed for compiling C++ code.

%package -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}
Summary:        C compiler runtime library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          System/Base
Provides:       libgcc_s%{libgcc_s} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgcc_s%{libgcc_s}

%description -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}
Libgcc is needed for dynamically linked C programs.

%post -n libgcc_s%{libgcc_s}%{libgcc_s_suffix} -p /sbin/ldconfig

%postun -n libgcc_s%{libgcc_s}%{libgcc_s_suffix} -p /sbin/ldconfig

%package -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-32bit
Summary:        C compiler runtime library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          System/Base
Provides:       libgcc_s%{libgcc_s}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgcc_s%{libgcc_s}-32bit

%description -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-32bit
Libgcc is needed for dynamically linked C programs.

%post -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-32bit -p /sbin/ldconfig

%postun -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-32bit -p /sbin/ldconfig

%package -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-64bit
Summary:        C compiler runtime library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          System/Base
Provides:       libgcc_s%{libgcc_s}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgcc_s%{libgcc_s}-64bit

%description -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-64bit
Libgcc is needed for dynamically linked C programs.

%post -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-64bit -p /sbin/ldconfig

%postun -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-64bit -p /sbin/ldconfig

%package -n libgomp%{libgomp_sover}%{libgomp_suffix}
Summary:        The GNU compiler collection OpenMP runtime library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          System/Base
Provides:       libgomp%{libgomp_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgomp%{libgomp_sover}

%description -n libgomp%{libgomp_sover}%{libgomp_suffix}
This is the OpenMP runtime library needed by OpenMP enabled programs
that were built with the -fopenmp compiler option and by programs that
were auto-parallelized via the -ftree-parallelize-loops compiler
option.


%post -n libgomp%{libgomp_sover}%{libgomp_suffix} -p /sbin/ldconfig

%postun -n libgomp%{libgomp_sover}%{libgomp_suffix} -p /sbin/ldconfig

%package -n libgomp%{libgomp_sover}%{libgomp_suffix}-32bit
Summary:        The GNU compiler collection OpenMP runtime library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          System/Base
Provides:       libgomp%{libgomp_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgomp%{libgomp_sover}-32bit

%description -n libgomp%{libgomp_sover}%{libgomp_suffix}-32bit
This is the OpenMP runtime library needed by OpenMP enabled programs
that were built with the -fopenmp compiler option and by programs that
were auto-parallelized via the -ftree-parallelize-loops compiler
option.


%post -n libgomp%{libgomp_sover}%{libgomp_suffix}-32bit -p /sbin/ldconfig

%postun -n libgomp%{libgomp_sover}%{libgomp_suffix}-32bit -p /sbin/ldconfig

%package -n libgomp%{libgomp_sover}%{libgomp_suffix}-64bit
Summary:        The GNU compiler collection OpenMP runtime library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          System/Base
Provides:       libgomp%{libgomp_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgomp%{libgomp_sover}-64bit

%description -n libgomp%{libgomp_sover}%{libgomp_suffix}-64bit
This is the OpenMP runtime library needed by OpenMP enabled programs
that were built with the -fopenmp compiler option and by programs that
were auto-parallelized via the -ftree-parallelize-loops compiler
option.


%post -n libgomp%{libgomp_sover}%{libgomp_suffix}-64bit -p /sbin/ldconfig

%postun -n libgomp%{libgomp_sover}%{libgomp_suffix}-64bit -p /sbin/ldconfig

%package -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}
Summary:        The standard C++ shared library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          System/Libraries
Suggests:       libstdc++%{libstdcxx_sover}-locale
Provides:       libstdc++%{libstdcxx_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libstdc++%{libstdcxx_sover}

%description -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}
The standard C++ library, needed for dynamically linked C++ programs.


%post -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix} -p /sbin/ldconfig

%postun -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix} -p /sbin/ldconfig

%package -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-32bit
Summary:        The standard C++ shared library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          System/Libraries
Suggests:       libstdc++%{libstdcxx_sover}-locale
Provides:       libstdc++%{libstdcxx_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libstdc++%{libstdcxx_sover}-32bit

%description -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-32bit
The standard C++ library, needed for dynamically linked C++ programs.


%post -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-32bit -p /sbin/ldconfig

%postun -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-32bit -p /sbin/ldconfig

%package -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-64bit
Summary:        The standard C++ shared library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          System/Libraries
Suggests:       libstdc++%{libstdcxx_sover}-locale
Provides:       libstdc++%{libstdcxx_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libstdc++%{libstdcxx_sover}-64bit

%description -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-64bit
The standard C++ library, needed for dynamically linked C++ programs.


%post -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-64bit -p /sbin/ldconfig

%postun -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-64bit -p /sbin/ldconfig

%package -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-locale
Summary:        Standard C++ Library Locales
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          System/Libraries
Provides:       libstdc++%{libstdcxx_sover}-locale = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libstdc++%{libstdcxx_sover}-locale

%description -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-locale
The standard C++ library locale data.

%package info
Summary:        Documentation for the GNU compiler collection
License:        GFDL-1.2-only
Group:          Documentation/Other
PreReq:         %{install_info_prereq}
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description info
GNU info-pages for the GNU compiler collection covering both user-level
and internals documentation.

%package objc
Summary:        GNU Objective C Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc7 = %{version}-%{release}
Requires:       gcc7-objc = %{version}-%{release}
Requires:       libobjc%{libobjc_sover} >= %{version}-%{release}

%description objc
This package contains the GNU Objective C compiler. Objective C is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package objc-32bit
Summary:        GNU Objective C Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc7-32bit = %{version}-%{release}
Requires:       gcc7-objc = %{version}-%{release}
Requires:       libobjc%{libobjc_sover}-32bit >= %{version}-%{release}

%description objc-32bit
This package contains the GNU Objective C compiler. Objective C is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package objc-64bit
Summary:        GNU Objective C Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc7-64bit = %{version}-%{release}
Requires:       gcc7-objc = %{version}-%{release}
Requires:       libobjc%{libobjc_sover}-64bit >= %{version}-%{release}

%description objc-64bit
This package contains the GNU Objective C compiler. Objective C is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package -n libobjc%{libobjc_sover}%{libobjc_suffix}
Summary:        Library for the GNU Objective C Compiler
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          Development/Libraries/Other
Provides:       libobjc%{libobjc_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libobjc%{libobjc_sover}

%description -n libobjc%{libobjc_sover}%{libobjc_suffix}
The library for the GNU Objective C compiler.

%post -n libobjc%{libobjc_sover}%{libobjc_suffix} -p /sbin/ldconfig

%postun -n libobjc%{libobjc_sover}%{libobjc_suffix} -p /sbin/ldconfig

%package -n libobjc%{libobjc_sover}%{libobjc_suffix}-32bit
Summary:        Library for the GNU Objective C Compiler
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          Development/Libraries/Other
Provides:       libobjc%{libobjc_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libobjc%{libobjc_sover}-32bit

%description -n libobjc%{libobjc_sover}%{libobjc_suffix}-32bit
The library for the GNU Objective C compiler.

%post -n libobjc%{libobjc_sover}%{libobjc_suffix}-32bit -p /sbin/ldconfig

%postun -n libobjc%{libobjc_sover}%{libobjc_suffix}-32bit -p /sbin/ldconfig

%package -n libobjc%{libobjc_sover}%{libobjc_suffix}-64bit
Summary:        Library for the GNU Objective C Compiler
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          Development/Libraries/Other
Provides:       libobjc%{libobjc_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libobjc%{libobjc_sover}-64bit

%description -n libobjc%{libobjc_sover}%{libobjc_suffix}-64bit
The library for the GNU Objective C compiler.

%post -n libobjc%{libobjc_sover}%{libobjc_suffix}-64bit -p /sbin/ldconfig

%postun -n libobjc%{libobjc_sover}%{libobjc_suffix}-64bit -p /sbin/ldconfig

%package obj-c++
Summary:        GNU Objective C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc7-c++ = %{version}-%{release}
Requires:       gcc7-obj-c++ = %{version}-%{release}
Requires:       gcc7-objc = %{version}-%{release}

%description obj-c++
This package contains the GNU Objective C++ compiler. Objective C++ is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package obj-c++-32bit
Summary:        GNU Objective C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc7-c++-32bit = %{version}-%{release}
Requires:       gcc7-obj-c++ = %{version}-%{release}
Requires:       gcc7-objc-32bit = %{version}-%{release}

%description obj-c++-32bit
This package contains the GNU Objective C++ compiler. Objective C++ is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package obj-c++-64bit
Summary:        GNU Objective C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc7-c++-64bit = %{version}-%{release}
Requires:       gcc7-obj-c++ = %{version}-%{release}
Requires:       gcc7-objc-64bit = %{version}-%{release}

%description obj-c++-64bit
This package contains the GNU Objective C++ compiler. Objective C++ is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package -n cpp7
Summary:        The GCC Preprocessor
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++

%description -n cpp7
This Package contains just the preprocessor that is used by the X11
packages.

%package ada
Summary:        GNU Ada Compiler Based on GCC (GNAT)
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc7 = %{version}-%{release}
Requires:       gcc7-ada = %{version}-%{release}
Requires:       libada7 = %{version}-%{release}

%description ada
This package contains an Ada compiler and associated development
tools based on the GNU GCC technology.

%package ada-32bit
Summary:        GNU Ada Compiler Based on GCC (GNAT)
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc7-32bit = %{version}-%{release}
Requires:       gcc7-ada = %{version}-%{release}
Requires:       libada7-32bit = %{version}-%{release}

%description ada-32bit
This package contains an Ada compiler and associated development
tools based on the GNU GCC technology.

%package ada-64bit
Summary:        GNU Ada Compiler Based on GCC (GNAT)
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc7-64bit = %{version}-%{release}
Requires:       gcc7-ada = %{version}-%{release}
Requires:       libada7-64bit = %{version}-%{release}

%description ada-64bit
This package contains an Ada compiler and associated development
tools based on the GNU GCC technology.

%package -n libada7
Summary:        GNU Ada Runtime Libraries
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          System/Libraries
Provides:       libgnarl-7 = %{version}-%{release}
Conflicts:      %selfconflict libgnarl-7
Provides:       libgnat-7 = %{version}-%{release}
Conflicts:      %selfconflict libgnat-7

%description -n libada7
This package contains the shared libraries required to run programs
compiled with the GNU Ada compiler (GNAT) if they are compiled to use
shared libraries. It also contains the shared libraries for the
Implementation of the Ada Semantic Interface Specification (ASIS), the
implementation of Distributed Systems Programming (GLADE) and the Posix
1003.5 Binding (Florist).

%post -n libada7 -p /sbin/ldconfig

%postun -n libada7 -p /sbin/ldconfig

%package -n libada7-32bit
Summary:        GNU Ada Runtime Libraries
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          System/Libraries
Provides:       libgnarl-7-32bit = %{version}-%{release}
Conflicts:      %selfconflict libgnarl-7-32bit
Provides:       libgnat-7-32bit = %{version}-%{release}
Conflicts:      %selfconflict libgnat-7-32bit

%description -n libada7-32bit
This package contains the shared libraries required to run programs
compiled with the GNU Ada compiler (GNAT) if they are compiled to use
shared libraries. It also contains the shared libraries for the
Implementation of the Ada Semantic Interface Specification (ASIS), the
implementation of Distributed Systems Programming (GLADE) and the Posix
1003.5 Binding (Florist).

%post -n libada7-32bit -p /sbin/ldconfig

%postun -n libada7-32bit -p /sbin/ldconfig

%package -n libada7-64bit
Summary:        GNU Ada Runtime Libraries
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          System/Libraries
Provides:       libgnarl-7-64bit = %{version}-%{release}
Conflicts:      %selfconflict libgnarl-7-64bit
Provides:       libgnat-7-64bit = %{version}-%{release}
Conflicts:      %selfconflict libgnat-7-64bit

%description -n libada7-64bit
This package contains the shared libraries required to run programs
compiled with the GNU Ada compiler (GNAT) if they are compiled to use
shared libraries. It also contains the shared libraries for the
Implementation of the Ada Semantic Interface Specification (ASIS), the
implementation of Distributed Systems Programming (GLADE) and the Posix
1003.5 Binding (Florist).

%post -n libada7-64bit -p /sbin/ldconfig

%postun -n libada7-64bit -p /sbin/ldconfig

%package fortran
Summary:        The GNU Fortran Compiler and Support Files
License:        GPL-3.0-or-later
Group:          Development/Languages/Fortran
Requires:       gcc7 = %{version}-%{release}
Requires:       gcc7-fortran = %{version}-%{release}
Requires:       libgfortran%{libgfortran_sover} >= %{version}-%{release}
%ifarch %quadmath_arch
Requires:       libquadmath%{libquadmath_sover} >= %{version}-%{release}
%endif

%description fortran
This is the Fortran compiler of the GNU Compiler Collection (GCC).

%package fortran-32bit
Summary:        The GNU Fortran Compiler and Support Files
License:        GPL-3.0-or-later
Group:          Development/Languages/Fortran
Requires:       gcc7-32bit = %{version}-%{release}
Requires:       gcc7-fortran = %{version}-%{release}
Requires:       libgfortran%{libgfortran_sover}-32bit >= %{version}-%{release}
%ifarch %quadmath_arch
Requires:       libquadmath%{libquadmath_sover}-32bit >= %{version}-%{release}
%endif

%description fortran-32bit
This is the Fortran compiler of the GNU Compiler Collection (GCC).

%package fortran-64bit
Summary:        The GNU Fortran Compiler and Support Files
License:        GPL-3.0-or-later
Group:          Development/Languages/Fortran
Requires:       gcc7-64bit = %{version}-%{release}
Requires:       gcc7-fortran = %{version}-%{release}
Requires:       libgfortran%{libgfortran_sover}-64bit >= %{version}-%{release}
%ifarch %quadmath_arch
Requires:       libquadmath%{libquadmath_sover}-64bit >= %{version}-%{release}
%endif

%description fortran-64bit
This is the Fortran compiler of the GNU Compiler Collection (GCC).

%package -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}
Summary:        The GNU Fortran Compiler Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          Development/Languages/Fortran
%ifarch %quadmath_arch
Requires:       libquadmath%{libquadmath_sover} >= %{version}-%{release}
%endif
Provides:       libgfortran%{libgfortran_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgfortran%{libgfortran_sover}

%description -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}
The runtime library needed to run programs compiled with the Fortran compiler
of the GNU Compiler Collection (GCC).

%post -n libgfortran%{libgfortran_sover}%{libgfortran_suffix} -p /sbin/ldconfig

%postun -n libgfortran%{libgfortran_sover}%{libgfortran_suffix} -p /sbin/ldconfig

%package -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}-32bit
Summary:        The GNU Fortran Compiler Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          Development/Languages/Fortran
%ifarch %quadmath_arch
Requires:       libquadmath%{libquadmath_sover}-32bit >= %{version}-%{release}
%endif
Provides:       libgfortran%{libgfortran_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgfortran%{libgfortran_sover}-32bit

%description -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}-32bit
The runtime library needed to run programs compiled with the Fortran compiler
of the GNU Compiler Collection (GCC).

%post -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}-32bit -p /sbin/ldconfig

%postun -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}-32bit -p /sbin/ldconfig

%package -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}-64bit
Summary:        The GNU Fortran Compiler Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          Development/Languages/Fortran
%ifarch %quadmath_arch
Requires:       libquadmath%{libquadmath_sover}-64bit >= %{version}-%{release}
%endif
Provides:       libgfortran%{libgfortran_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgfortran%{libgfortran_sover}-64bit

%description -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}-64bit
The runtime library needed to run programs compiled with the Fortran compiler
of the GNU Compiler Collection (GCC).

%post -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}-64bit -p /sbin/ldconfig

%postun -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}-64bit -p /sbin/ldconfig

%package -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}
Summary:        The GNU Fortran Compiler Quadmath Runtime Library
License:        LGPL-2.1-only
Group:          Development/Languages/Fortran
Provides:       libquadmath%{libquadmath_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libquadmath%{libquadmath_sover}

%description -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}
The runtime library needed to run programs compiled with the Fortran compiler
of the GNU Compiler Collection (GCC) and quadruple precision floating point
operations.

%post -n libquadmath%{libquadmath_sover}%{libquadmath_suffix} -p /sbin/ldconfig

%postun -n libquadmath%{libquadmath_sover}%{libquadmath_suffix} -p /sbin/ldconfig

%package -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}-32bit
Summary:        The GNU Fortran Compiler Quadmath Runtime Library
License:        LGPL-2.1-only
Group:          Development/Languages/Fortran
Provides:       libquadmath%{libquadmath_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libquadmath%{libquadmath_sover}-32bit

%description -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}-32bit
The runtime library needed to run programs compiled with the Fortran compiler
of the GNU Compiler Collection (GCC) and quadruple precision floating point
operations.

%post -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}-32bit -p /sbin/ldconfig

%postun -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}-32bit -p /sbin/ldconfig

%package -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}-64bit
Summary:        The GNU Fortran Compiler Quadmath Runtime Library
License:        LGPL-2.1-only
Group:          Development/Languages/Fortran
Provides:       libquadmath%{libquadmath_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libquadmath%{libquadmath_sover}-64bit

%description -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}-64bit
The runtime library needed to run programs compiled with the Fortran compiler
of the GNU Compiler Collection (GCC) and quadruple precision floating point
operations.

%post -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}-64bit -p /sbin/ldconfig

%postun -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}-64bit -p /sbin/ldconfig

%package -n libitm%{libitm_sover}%{libitm_suffix}
Summary:        The GNU Compiler Transactional Memory Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libitm%{libitm_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libitm%{libitm_sover}

%description -n libitm%{libitm_sover}%{libitm_suffix}
The runtime library needed to run programs compiled with the
-fgnu-tm option of the GNU Compiler Collection (GCC).

%post -n libitm%{libitm_sover}%{libitm_suffix} -p /sbin/ldconfig

%postun -n libitm%{libitm_sover}%{libitm_suffix} -p /sbin/ldconfig

%package -n libitm%{libitm_sover}%{libitm_suffix}-32bit
Summary:        The GNU Compiler Transactional Memory Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libitm%{libitm_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libitm%{libitm_sover}-32bit

%description -n libitm%{libitm_sover}%{libitm_suffix}-32bit
The runtime library needed to run programs compiled with the
-fgnu-tm option of the GNU Compiler Collection (GCC).

%post -n libitm%{libitm_sover}%{libitm_suffix}-32bit -p /sbin/ldconfig

%postun -n libitm%{libitm_sover}%{libitm_suffix}-32bit -p /sbin/ldconfig

%package -n libitm%{libitm_sover}%{libitm_suffix}-64bit
Summary:        The GNU Compiler Transactional Memory Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libitm%{libitm_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libitm%{libitm_sover}-64bit

%description -n libitm%{libitm_sover}%{libitm_suffix}-64bit
The runtime library needed to run programs compiled with the
-fgnu-tm option of the GNU Compiler Collection (GCC).

%post -n libitm%{libitm_sover}%{libitm_suffix}-64bit -p /sbin/ldconfig

%postun -n libitm%{libitm_sover}%{libitm_suffix}-64bit -p /sbin/ldconfig

%package -n libasan%{libasan_sover}%{libasan_suffix}
Summary:        The GNU Compiler Address Sanitizer Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libasan%{libasan_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libasan%{libasan_sover}

%description -n libasan%{libasan_sover}%{libasan_suffix}
The runtime library needed to run programs compiled with the
-fsanitize=address option of the GNU Compiler Collection (GCC).

%post -n libasan%{libasan_sover}%{libasan_suffix} -p /sbin/ldconfig

%postun -n libasan%{libasan_sover}%{libasan_suffix} -p /sbin/ldconfig

%package -n libasan%{libasan_sover}%{libasan_suffix}-32bit
Summary:        The GNU Compiler Address Sanitizer Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libasan%{libasan_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libasan%{libasan_sover}-32bit

%description -n libasan%{libasan_sover}%{libasan_suffix}-32bit
The runtime library needed to run programs compiled with the
-fsanitize=address option of the GNU Compiler Collection (GCC).

%post -n libasan%{libasan_sover}%{libasan_suffix}-32bit -p /sbin/ldconfig

%postun -n libasan%{libasan_sover}%{libasan_suffix}-32bit -p /sbin/ldconfig

%package -n libasan%{libasan_sover}%{libasan_suffix}-64bit
Summary:        The GNU Compiler Address Sanitizer Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libasan%{libasan_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libasan%{libasan_sover}-64bit

%description -n libasan%{libasan_sover}%{libasan_suffix}-64bit
The runtime library needed to run programs compiled with the
-fsanitize=address option of the GNU Compiler Collection (GCC).

%post -n libasan%{libasan_sover}%{libasan_suffix}-64bit -p /sbin/ldconfig

%postun -n libasan%{libasan_sover}%{libasan_suffix}-64bit -p /sbin/ldconfig

%package -n libtsan%{libtsan_sover}%{libtsan_suffix}
Summary:        The GNU Compiler Thread Sanitizer Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libtsan%{libtsan_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libtsan%{libtsan_sover}

%description -n libtsan%{libtsan_sover}%{libtsan_suffix}
The runtime library needed to run programs compiled with the
-fsanitize=thread option of the GNU Compiler Collection (GCC).

%post -n libtsan%{libtsan_sover}%{libtsan_suffix} -p /sbin/ldconfig

%postun -n libtsan%{libtsan_sover}%{libtsan_suffix} -p /sbin/ldconfig

%package -n libtsan%{libtsan_sover}%{libtsan_suffix}-32bit
Summary:        The GNU Compiler Thread Sanitizer Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libtsan%{libtsan_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libtsan%{libtsan_sover}-32bit

%description -n libtsan%{libtsan_sover}%{libtsan_suffix}-32bit
The runtime library needed to run programs compiled with the
-fsanitize=thread option of the GNU Compiler Collection (GCC).

%post -n libtsan%{libtsan_sover}%{libtsan_suffix}-32bit -p /sbin/ldconfig

%postun -n libtsan%{libtsan_sover}%{libtsan_suffix}-32bit -p /sbin/ldconfig

%package -n libtsan%{libtsan_sover}%{libtsan_suffix}-64bit
Summary:        The GNU Compiler Thread Sanitizer Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libtsan%{libtsan_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libtsan%{libtsan_sover}-64bit

%description -n libtsan%{libtsan_sover}%{libtsan_suffix}-64bit
The runtime library needed to run programs compiled with the
-fsanitize=thread option of the GNU Compiler Collection (GCC).

%post -n libtsan%{libtsan_sover}%{libtsan_suffix}-64bit -p /sbin/ldconfig

%postun -n libtsan%{libtsan_sover}%{libtsan_suffix}-64bit -p /sbin/ldconfig

%package -n libatomic%{libatomic_sover}%{libatomic_suffix}
Summary:        The GNU Compiler Atomic Operations Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          Development/Languages/C and C++
Provides:       libatomic%{libatomic_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libatomic%{libatomic_sover}

%description -n libatomic%{libatomic_sover}%{libatomic_suffix}
The runtime library for atomic operations of the GNU Compiler Collection (GCC).

%post -n libatomic%{libatomic_sover}%{libatomic_suffix} -p /sbin/ldconfig

%postun -n libatomic%{libatomic_sover}%{libatomic_suffix} -p /sbin/ldconfig

%package -n libatomic%{libatomic_sover}%{libatomic_suffix}-32bit
Summary:        The GNU Compiler Atomic Operations Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          Development/Languages/C and C++
Provides:       libatomic%{libatomic_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libatomic%{libatomic_sover}-32bit

%description -n libatomic%{libatomic_sover}%{libatomic_suffix}-32bit
The runtime library for atomic operations of the GNU Compiler Collection (GCC).

%post -n libatomic%{libatomic_sover}%{libatomic_suffix}-32bit -p /sbin/ldconfig

%postun -n libatomic%{libatomic_sover}%{libatomic_suffix}-32bit -p /sbin/ldconfig

%package -n libatomic%{libatomic_sover}%{libatomic_suffix}-64bit
Summary:        The GNU Compiler Atomic Operations Runtime Library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          Development/Languages/C and C++
Provides:       libatomic%{libatomic_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libatomic%{libatomic_sover}-64bit

%description -n libatomic%{libatomic_sover}%{libatomic_suffix}-64bit
The runtime library for atomic operations of the GNU Compiler Collection (GCC).

%post -n libatomic%{libatomic_sover}%{libatomic_suffix}-64bit -p /sbin/ldconfig

%postun -n libatomic%{libatomic_sover}%{libatomic_suffix}-64bit -p /sbin/ldconfig

%package -n libcilkrts%{libcilkrts_sover}%{libcilkrts_suffix}
Summary:        The GNU Compiler Cilk+ Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libcilkrts%{libcilkrts_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libcilkrts%{libcilkrts_sover}

%description -n libcilkrts%{libcilkrts_sover}%{libcilkrts_suffix}
The runtime library needed to run programs compiled with the
-fcilkplus option of the GNU Compiler Collection (GCC).

%post -n libcilkrts%{libcilkrts_sover}%{libcilkrts_suffix} -p /sbin/ldconfig

%postun -n libcilkrts%{libcilkrts_sover}%{libcilkrts_suffix} -p /sbin/ldconfig

%package -n libcilkrts%{libcilkrts_sover}%{libcilkrts_suffix}-32bit
Summary:        The GNU Compiler Cilk+ Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libcilkrts%{libcilkrts_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libcilkrts%{libcilkrts_sover}-32bit

%description -n libcilkrts%{libcilkrts_sover}%{libcilkrts_suffix}-32bit
The runtime library needed to run programs compiled with the
-fcilkplus option of the GNU Compiler Collection (GCC).

%post -n libcilkrts%{libcilkrts_sover}%{libcilkrts_suffix}-32bit -p /sbin/ldconfig

%postun -n libcilkrts%{libcilkrts_sover}%{libcilkrts_suffix}-32bit -p /sbin/ldconfig

%package -n libcilkrts%{libcilkrts_sover}%{libcilkrts_suffix}-64bit
Summary:        The GNU Compiler Cilk+ Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libcilkrts%{libcilkrts_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libcilkrts%{libcilkrts_sover}-64bit

%description -n libcilkrts%{libcilkrts_sover}%{libcilkrts_suffix}-64bit
The runtime library needed to run programs compiled with the
-fcilkplus option of the GNU Compiler Collection (GCC).

%post -n libcilkrts%{libcilkrts_sover}%{libcilkrts_suffix}-64bit -p /sbin/ldconfig

%postun -n libcilkrts%{libcilkrts_sover}%{libcilkrts_suffix}-64bit -p /sbin/ldconfig

%package -n liblsan%{liblsan_sover}%{liblsan_suffix}
Summary:        The GNU Compiler Leak Sanitizer Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       liblsan%{liblsan_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict liblsan%{liblsan_sover}

%description -n liblsan%{liblsan_sover}%{liblsan_suffix}
The runtime library needed to run programs compiled with the
-fsanitize=leak option of the GNU Compiler Collection (GCC).

%post -n liblsan%{liblsan_sover}%{liblsan_suffix} -p /sbin/ldconfig

%postun -n liblsan%{liblsan_sover}%{liblsan_suffix} -p /sbin/ldconfig

%package -n liblsan%{liblsan_sover}%{liblsan_suffix}-32bit
Summary:        The GNU Compiler Leak Sanitizer Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       liblsan%{liblsan_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict liblsan%{liblsan_sover}-32bit

%description -n liblsan%{liblsan_sover}%{liblsan_suffix}-32bit
The runtime library needed to run programs compiled with the
-fsanitize=leak option of the GNU Compiler Collection (GCC).

%post -n liblsan%{liblsan_sover}%{liblsan_suffix}-32bit -p /sbin/ldconfig

%postun -n liblsan%{liblsan_sover}%{liblsan_suffix}-32bit -p /sbin/ldconfig

%package -n liblsan%{liblsan_sover}%{liblsan_suffix}-64bit
Summary:        The GNU Compiler Leak Sanitizer Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       liblsan%{liblsan_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict liblsan%{liblsan_sover}-64bit

%description -n liblsan%{liblsan_sover}%{liblsan_suffix}-64bit
The runtime library needed to run programs compiled with the
-fsanitize=leak option of the GNU Compiler Collection (GCC).

%post -n liblsan%{liblsan_sover}%{liblsan_suffix}-64bit -p /sbin/ldconfig

%postun -n liblsan%{liblsan_sover}%{liblsan_suffix}-64bit -p /sbin/ldconfig

%package -n libubsan%{libubsan_sover}%{libubsan_suffix}
Summary:        The GNU Compiler Undefined Sanitizer Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libubsan%{libubsan_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libubsan%{libubsan_sover}

%description -n libubsan%{libubsan_sover}%{libubsan_suffix}
The runtime library needed to run programs compiled with the
-fsanitize=undefined option of the GNU Compiler Collection (GCC).

%post -n libubsan%{libubsan_sover}%{libubsan_suffix} -p /sbin/ldconfig

%postun -n libubsan%{libubsan_sover}%{libubsan_suffix} -p /sbin/ldconfig

%package -n libubsan%{libubsan_sover}%{libubsan_suffix}-32bit
Summary:        The GNU Compiler Undefined Sanitizer Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libubsan%{libubsan_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libubsan%{libubsan_sover}-32bit

%description -n libubsan%{libubsan_sover}%{libubsan_suffix}-32bit
The runtime library needed to run programs compiled with the
-fsanitize=undefined option of the GNU Compiler Collection (GCC).

%post -n libubsan%{libubsan_sover}%{libubsan_suffix}-32bit -p /sbin/ldconfig

%postun -n libubsan%{libubsan_sover}%{libubsan_suffix}-32bit -p /sbin/ldconfig

%package -n libubsan%{libubsan_sover}%{libubsan_suffix}-64bit
Summary:        The GNU Compiler Undefined Sanitizer Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libubsan%{libubsan_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libubsan%{libubsan_sover}-64bit

%description -n libubsan%{libubsan_sover}%{libubsan_suffix}-64bit
The runtime library needed to run programs compiled with the
-fsanitize=undefined option of the GNU Compiler Collection (GCC).

%post -n libubsan%{libubsan_sover}%{libubsan_suffix}-64bit -p /sbin/ldconfig

%postun -n libubsan%{libubsan_sover}%{libubsan_suffix}-64bit -p /sbin/ldconfig

%package -n libvtv%{libvtv_sover}%{libvtv_suffix}
Summary:        The GNU Compiler Vtable Verifier Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libvtv%{libvtv_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libvtv%{libvtv_sover}

%description -n libvtv%{libvtv_sover}%{libvtv_suffix}
The runtime library needed to run programs compiled with the
-fvtable-verify option of the GNU Compiler Collection (GCC).

%post -n libvtv%{libvtv_sover}%{libvtv_suffix} -p /sbin/ldconfig

%postun -n libvtv%{libvtv_sover}%{libvtv_suffix} -p /sbin/ldconfig

%package -n libvtv%{libvtv_sover}%{libvtv_suffix}-32bit
Summary:        The GNU Compiler Vtable Verifier Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libvtv%{libvtv_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libvtv%{libvtv_sover}-32bit

%description -n libvtv%{libvtv_sover}%{libvtv_suffix}-32bit
The runtime library needed to run programs compiled with the
-fvtable-verify option of the GNU Compiler Collection (GCC).

%post -n libvtv%{libvtv_sover}%{libvtv_suffix}-32bit -p /sbin/ldconfig

%postun -n libvtv%{libvtv_sover}%{libvtv_suffix}-32bit -p /sbin/ldconfig

%package -n libvtv%{libvtv_sover}%{libvtv_suffix}-64bit
Summary:        The GNU Compiler Vtable Verifier Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libvtv%{libvtv_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libvtv%{libvtv_sover}-64bit

%description -n libvtv%{libvtv_sover}%{libvtv_suffix}-64bit
The runtime library needed to run programs compiled with the
-fvtable-verify option of the GNU Compiler Collection (GCC).

%post -n libvtv%{libvtv_sover}%{libvtv_suffix}-64bit -p /sbin/ldconfig

%postun -n libvtv%{libvtv_sover}%{libvtv_suffix}-64bit -p /sbin/ldconfig

%package -n libmpx%{libmpx_sover}%{libmpx_suffix}
Summary:        The GNU Compiler MPX Runtime Library
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
Provides:       libmpx%{libmpx_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libmpx%{libmpx_sover}

%description -n libmpx%{libmpx_sover}%{libmpx_suffix}
The runtime library needed to run programs compiled with the
-fcheck-pointer-bounds option of the GNU Compiler Collection (GCC).

%post -n libmpx%{libmpx_sover}%{libmpx_suffix} -p /sbin/ldconfig

%postun -n libmpx%{libmpx_sover}%{libmpx_suffix} -p /sbin/ldconfig

%package -n libmpx%{libmpx_sover}%{libmpx_suffix}-32bit
Summary:        The GNU Compiler MPX Runtime Library
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
Provides:       libmpx%{libmpx_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libmpx%{libmpx_sover}-32bit

%description -n libmpx%{libmpx_sover}%{libmpx_suffix}-32bit
The runtime library needed to run programs compiled with the
-fcheck-pointer-bounds option of the GNU Compiler Collection (GCC).

%post -n libmpx%{libmpx_sover}%{libmpx_suffix}-32bit -p /sbin/ldconfig

%postun -n libmpx%{libmpx_sover}%{libmpx_suffix}-32bit -p /sbin/ldconfig

%package -n libmpx%{libmpx_sover}%{libmpx_suffix}-64bit
Summary:        The GNU Compiler MPX Runtime Library
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
Provides:       libmpx%{libmpx_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libmpx%{libmpx_sover}-64bit

%description -n libmpx%{libmpx_sover}%{libmpx_suffix}-64bit
The runtime library needed to run programs compiled with the
-fcheck-pointer-bounds option of the GNU Compiler Collection (GCC).

%post -n libmpx%{libmpx_sover}%{libmpx_suffix}-64bit -p /sbin/ldconfig

%postun -n libmpx%{libmpx_sover}%{libmpx_suffix}-64bit -p /sbin/ldconfig

%package -n libmpxwrappers%{libmpxwrappers_sover}%{libmpxwrappers_suffix}
Summary:        The GNU Compiler MPX Runtime Library
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
Provides:       libmpxwrappers%{libmpxwrappers_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libmpxwrappers%{libmpxwrappers_sover}

%description -n libmpxwrappers%{libmpxwrappers_sover}%{libmpxwrappers_suffix}
The runtime library needed to run programs compiled with the
-fcheck-pointer-bounds option of the GNU Compiler Collection (GCC).

%post -n libmpxwrappers%{libmpxwrappers_sover}%{libmpxwrappers_suffix} -p /sbin/ldconfig

%postun -n libmpxwrappers%{libmpxwrappers_sover}%{libmpxwrappers_suffix} -p /sbin/ldconfig

%package -n libmpxwrappers%{libmpxwrappers_sover}%{libmpxwrappers_suffix}-32bit
Summary:        The GNU Compiler MPX Runtime Library
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
Provides:       libmpxwrappers%{libmpxwrappers_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libmpxwrappers%{libmpxwrappers_sover}-32bit

%description -n libmpxwrappers%{libmpxwrappers_sover}%{libmpxwrappers_suffix}-32bit
The runtime library needed to run programs compiled with the
-fcheck-pointer-bounds option of the GNU Compiler Collection (GCC).

%post -n libmpxwrappers%{libmpxwrappers_sover}%{libmpxwrappers_suffix}-32bit -p /sbin/ldconfig

%postun -n libmpxwrappers%{libmpxwrappers_sover}%{libmpxwrappers_suffix}-32bit -p /sbin/ldconfig

%package -n libmpxwrappers%{libmpxwrappers_sover}%{libmpxwrappers_suffix}-64bit
Summary:        The GNU Compiler MPX Runtime Library
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
Provides:       libmpxwrappers%{libmpxwrappers_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libmpxwrappers%{libmpxwrappers_sover}-64bit

%description -n libmpxwrappers%{libmpxwrappers_sover}%{libmpxwrappers_suffix}-64bit
The runtime library needed to run programs compiled with the
-fcheck-pointer-bounds option of the GNU Compiler Collection (GCC).

%post -n libmpxwrappers%{libmpxwrappers_sover}%{libmpxwrappers_suffix}-64bit -p /sbin/ldconfig

%postun -n libmpxwrappers%{libmpxwrappers_sover}%{libmpxwrappers_suffix}-64bit -p /sbin/ldconfig

%package -n libstdc++%{libstdcxx_sover}%{libdevel_suffix}-doc
Summary:        Documentation for the GNU C++ standard library
License:        GPL-3.0-or-later
Group:          Documentation/HTML
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description -n libstdc++%{libstdcxx_sover}%{libdevel_suffix}-doc
Extensive HTML documentation for the GNU C++ standard library.

%package go
Summary:        GNU Go Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc7 = %{version}-%{release}
Requires:       gcc7-go = %{version}-%{release}
Requires:       libgo%{libgo_sover} >= %{version}-%{release}

%description go
This package contains a Go compiler and associated development
files based on the GNU GCC technology.

%package go-32bit
Summary:        GNU Go Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc7-32bit = %{version}-%{release}
Requires:       gcc7-go = %{version}-%{release}
Requires:       libgo%{libgo_sover}-32bit >= %{version}-%{release}

%description go-32bit
This package contains a Go compiler and associated development
files based on the GNU GCC technology.

%package go-64bit
Summary:        GNU Go Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc7-64bit = %{version}-%{release}
Requires:       gcc7-go = %{version}-%{release}
Requires:       libgo%{libgo_sover}-64bit >= %{version}-%{release}

%description go-64bit
This package contains a Go compiler and associated development
files based on the GNU GCC technology.

%package -n libgo%{libgo_sover}%{libgo_suffix}
Summary:        GNU Go compiler runtime library
License:        BSD-3-Clause
Group:          Development/Languages/Other
Provides:       libgo%{libgo_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgo%{libgo_sover}

%description -n libgo%{libgo_sover}%{libgo_suffix}
Runtime library for the GNU Go language.

%post -n libgo%{libgo_sover}%{libgo_suffix} -p /sbin/ldconfig

%postun -n libgo%{libgo_sover}%{libgo_suffix} -p /sbin/ldconfig

%package -n libgo%{libgo_sover}%{libgo_suffix}-32bit
Summary:        GNU Go compiler runtime library
License:        BSD-3-Clause
Group:          Development/Languages/Other
Provides:       libgo%{libgo_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgo%{libgo_sover}-32bit

%description -n libgo%{libgo_sover}%{libgo_suffix}-32bit
Runtime library for the GNU Go language.

%post -n libgo%{libgo_sover}%{libgo_suffix}-32bit -p /sbin/ldconfig

%postun -n libgo%{libgo_sover}%{libgo_suffix}-32bit -p /sbin/ldconfig

%package -n libgo%{libgo_sover}%{libgo_suffix}-64bit
Summary:        GNU Go compiler runtime library
License:        BSD-3-Clause
Group:          Development/Languages/Other
Provides:       libgo%{libgo_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgo%{libgo_sover}-64bit

%description -n libgo%{libgo_sover}%{libgo_suffix}-64bit
Runtime library for the GNU Go language.

%post -n libgo%{libgo_sover}%{libgo_suffix}-64bit -p /sbin/ldconfig

%postun -n libgo%{libgo_sover}%{libgo_suffix}-64bit -p /sbin/ldconfig

%package -n gcc7-testresults
Summary:        Testsuite results
License:        SUSE-Public-Domain
Group:          Development/Languages/C and C++

%description -n gcc7-testresults
Results from running the gcc and target library testsuites.




# Define the canonical target and host architecture
#   %%gcc_target_arch  is supposed to be the full target triple
#   %%cross_arch       is supposed to be the rpm target variant arch
#   %%TARGET_ARCH      will be the canonicalized target CPU part
#   %%HOST_ARCH        will be the canonicalized host CPU part
%if 0%{?gcc_target_arch:1}
%define TARGET_ARCH %(echo %{cross_arch} | sed -e "s/i.86/i586/;s/ppc/powerpc/;s/sparc64.*/sparc64/;s/sparcv.*/sparc/;")
%else
%define TARGET_ARCH %(echo %{_target_cpu} | sed -e "s/i.86/i586/;s/ppc/powerpc/;s/sparc64.*/sparc64/;s/sparcv.*/sparc/;")
%endif
%if 0%{?disable_32bit:1}
%define biarch 0
%else
%define biarch %(case " %{biarch_targets} " in (*" %{TARGET_ARCH} "*) echo 1;; (*) echo 0;; esac)
%endif

%define HOST_ARCH %(echo %{_target_cpu} | sed -e "s/i.86/i586/;s/ppc/powerpc/;s/sparc64.*/sparc64/;s/sparcv.*/sparc/;")
%ifarch ppc
%define GCCDIST powerpc64-suse-linux
%else
%ifarch %sparc
%define GCCDIST sparc64-suse-linux
%else
%ifarch %arm
%define GCCDIST %{HOST_ARCH}-suse-linux-gnueabi
%else
%define GCCDIST %{HOST_ARCH}-suse-linux
%endif
%endif
%endif

%define libsubdir %{_libdir}/gcc/%{GCCDIST}/%{gcc_dir_version}
%define gxxinclude %{_prefix}/include/c++/%{gcc_dir_version}

# Versionspecific directories
%define versmainlibdir %{libsubdir}
%define versmainlibdirbi32 %{libsubdir}/32
%define versmainlibdirbi64 %{libsubdir}/64
%ifarch ppc
%define versmainlibdirbi32 %{libsubdir}
%define versmainlibdirbi64 %{libsubdir}/64
%endif
%if %{build_primary_64bit}
%define versmainlibdirbi %{versmainlibdirbi32}
%else
%define versmainlibdirbi %{versmainlibdirbi64}
%endif

%define mainlibdir %{_libdir}
%define mainlibdirbi32 %{_prefix}/lib
%define mainlibdirbi64 %{_prefix}/lib64
%if %{build_primary_64bit}
%define mainlibdirbi %{mainlibdirbi32}
%else
%define mainlibdirbi %{mainlibdirbi64}
%endif

# Now define a few macros that make it easy to package libs and
# related files just to the right package, without caring for the
# exact path the files are in.
#   %%mainlib  package X from all dirs that belong to the main package
#   %%biarchlib   package X from all dirs that belong to the -32/64bit package
%define mainlib() %{mainlibdir}/%1\
%{nil}
%define biarchlib() %{nil}
%if %{biarch}
%if !%{separate_biarch}
%define mainlib() %{mainlibdir}/%1\
%{mainlibdirbi}/%1\
%{nil}
%else
%define biarchlib() %{mainlibdirbi}/%1\
%{nil}
%endif
%endif

%define versmainlib() %{versmainlibdir}/%1\
%{nil}
%define versbiarchlib() %{nil}
%if %{biarch}
%if !%{separate_biarch}
%define versmainlib() %{versmainlibdir}/%1\
%{versmainlibdirbi}/%1\
%{nil}
%else
%define versbiarchlib() %{versmainlibdirbi}/%1\
%{nil}
%endif
%endif

%prep
%if 0%{?nvptx_newlib:1}
%setup -q -n gcc-%{version} -a 5
ln -s nvptx-newlib/newlib .
%else
%setup -q -n gcc-%{version}
%endif

#test patching start

%patch -P 2
%patch -P 5
%patch -P 6
%patch -P 7
%if %{suse_version} < 1310
%patch -P 9
%endif
%patch -P 10
%patch -P 11
%patch -P 12
%patch -P 14
%patch -P 15
%patch -P 17 -p1
%patch -P 18
%patch -P 19
%patch -P 20
%patch -P 21 -p1
%patch -P 22 -p1
%patch -P 24 -p1
%patch -P 25 -p1
%patch -P 26 -p1
%patch -P 27 -p1
%patch -P 29
%patch -P 30 -p1
%patch -P 31 -p1
%patch -P 32 -p1
%patch -P 33 -p1
%patch -P 34 -p1
%patch -P 35 -p1
%patch -P 36 -p1
%patch -P 37 -p1
%patch -P 38 -p1
%patch -P 39 -p1
%patch -P 40 -p1
%patch -P 41 -p1
%patch -P 42 -p1
%patch -P 43 -p1
%patch -P 44 -p1
%patch -P 45 -p1
%patch -P 46 -p1
%patch -P 47 -p1
%patch -P 48 -p1
%patch -P 49 -p1
%patch -P 50 -p1
%patch -P 51
%patch -P 60
%patch -P 61
%patch -P 100 -p1
%patch -P 23 -p1
%patch -P 101 -p1
%patch -P 102 -p1
%patch -P 103 -p1
%patch -P 104 -p1
%patch -P 105 -p1
%patch -P 106 -p1
%patch -P 107 -p1
%patch -P 108 -p1
%patch -P 109 -p1
%patch -P 110 -p1
%patch -P 111 -p1
%patch -P 112 -p1
%patch -P 113 -p1
%patch -P 114 -p1
%patch -P 115 -p1
%patch -P 116 -p1
%patch -P 117 -p1
%patch -P 118 -p1
%patch -P 119 -p1
%patch -P 120 -p1
%patch -P 121 -p1
%patch -P 122 -p1
%patch -P 123 -p1
%patch -P 124 -p1
%patch -P 125 -p1
%patch -P 126 -p1
%patch -P 127 -p1

#test patching end

%build
%define _lto_cflags %{nil}
# Avoid rebuilding of generated files
contrib/gcc_update --touch

# SLE11 does not allow empty rpms
%if %{suse_version} < 1310
echo "This is a dummy package to provide a dependency." > README
%endif

rm -rf obj-%{GCCDIST}
mkdir obj-%{GCCDIST}
cd obj-%{GCCDIST}
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -U_FORTIFY_SOURCE"
RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS|sed -e 's/-fno-rtti//g' -e 's/-fno-exceptions//g' -e 's/-Wmissing-format-attribute//g' -e 's/-fstack-protector[^ ]*//g' -e 's/-ffortify=.//g' -e 's/-Wall//g' -e 's/-m32//g' -e 's/-m64//g'`
%ifarch %ix86
# -mcpu is superceded by -mtune but -mtune is not supported by
# our bootstrap compiler.  -mcpu gives a warning that stops
# the build process, so remove it for now.  Also remove all other
# -march and -mtune flags.  They are superseeded by proper
# default compiler settings now.
RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS|sed -e 's/-mcpu=i.86//g' -e 's/-march=i.86//g' -e 's/-mtune=i.86//g'`
%endif
%ifarch s390 s390x
RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS|sed -e 's/-fsigned-char//g'`
RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS|sed -e 's/-O1/-O2/g'`
%endif
%ifarch aarch64
%if %{build_ada}
# -mbranch-protection=standard flag is unsupported in gcc7 and we use GCC7 to build GCC7
RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS|sed -e 's/-mbranch-protection=standard//g'`
%endif
%endif
%if 0%{?gcc_target_arch:1}
# Kill all -march/tune/cpu because that screws building the target libs
RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS|sed -e 's/-m\(arch\|tune\|cpu\)=[^ ]*//g'`
%endif
# Replace 2 spaces by one finally
RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS|sed -e 's/  / /g'`

languages=c
%if %{build_cp}
languages=$languages,c++
%endif
%if %{build_objc}
languages=$languages,objc
%endif
%if %{build_fortran}
languages=$languages,fortran
%endif
%if %{build_objcp}
languages=$languages,obj-c++
%endif
%if %{build_ada}
languages=$languages,ada
%endif
%if %{build_go}
languages=$languages,go
%endif

# In general we want to ship release checking enabled compilers
# which is the default for released compilers
#ENABLE_CHECKING="--enable-checking=yes"
ENABLE_CHECKING="--enable-checking=release"
#ENABLE_CHECKING=""

# Work around tail/head -1 changes
export _POSIX2_VERSION=199209

%if %{build_ada}
# Using the host gnatmake like
#   CC="gcc%%{hostsuffix}" GNATBIND="gnatbind%%{hostsuffix}"
#   GNATMAKE="gnatmake%%{hostsuffix}"
# doesn't work due to PR33857, so an un-suffixed gnatmake has to be
# available
mkdir -p host-tools/bin
cp -a /usr/bin/gnatmake%{hostsuffix} host-tools/bin/gnatmake
cp -a /usr/bin/gnatlink%{hostsuffix} host-tools/bin/gnatlink
cp -a /usr/bin/gnatbind%{hostsuffix} host-tools/bin/gnatbind
cp -a /usr/bin/gcc%{hostsuffix} host-tools/bin/gcc
cp -a /usr/bin/g++%{hostsuffix} host-tools/bin/g++
ln -sf /usr/%{_lib} host-tools/%{_lib}
export PATH="`pwd`/host-tools/bin:$PATH"
%endif
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" XCFLAGS="$RPM_OPT_FLAGS" \
TCFLAGS="$RPM_OPT_FLAGS" \
../configure \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libdir} \
	--enable-languages=$languages \
%if %{build_hsa} || %{build_nvptx}
	--enable-offload-targets=\
%if %{build_hsa}
hsa,\
%endif
%if %{build_nvptx}
nvptx-none, \
%endif
%endif
%if %{build_nvptx}
	--without-cuda-driver \
%endif
	$ENABLE_CHECKING \
	--disable-werror \
	--with-gxx-include-dir=%{_prefix}/include/c++/%{gcc_dir_version} \
	--enable-ssp \
	--disable-libssp \
%if 0%{!?build_libvtv:1}
	--disable-libvtv \
%endif
%ifnarch %mpx_arch
	--disable-libmpx \
%endif
	--disable-libcc1 \
%if %{enable_plugins}
	--enable-plugin \
%else
	--disable-plugin \
%endif
	--with-bugurl="https://bugs.opensuse.org/" \
	--with-pkgversion="SUSE Linux" \
	--with-slibdir=/%{_lib} \
	--with-system-zlib \
	--enable-libstdcxx-allocator=new \
	--disable-libstdcxx-pch \
%if 0%{suse_version} <= 1320
	--with-default-libstdcxx-abi=gcc4-compatible \
%endif
	--enable-version-specific-runtime-libs \
	--with-gcc-major-version-only \
	--enable-linker-build-id \
	--enable-linux-futex \
%if %{suse_version} >= 1315
%ifarch %ix86 x86_64 ppc ppc64 ppc64le %arm aarch64 s390 s390x %sparc
	--enable-gnu-indirect-function \
%endif
%endif
	--program-suffix=%{binsuffix} \
%if 0%{?disable_32bit:1}
	--disable-multilib \
%endif
%if 0%{!?gcc_target_arch:1}
%ifarch ia64
	--with-system-libunwind \
%else
	--without-system-libunwind \
%endif
%endif
%if 0%{?gcc_target_arch:1}
	--program-prefix=%{gcc_target_arch}- \
	--target=%{gcc_target_arch} \
	--disable-nls \
%if 0%{?sysroot:1}
	--with-sysroot=%sysroot \
%endif
%if 0%{?build_sysroot:1}
	--with-build-sysroot=%{build_sysroot} \
%else
%if 0%{?sysroot:1}
	--with-build-sysroot=%{sysroot} \
%endif
%endif
%if 0%{?binutils_os:1}
	--with-build-time-tools=/usr/%{binutils_os}/bin \
%endif
%if 0%{?gcc_target_newlib}
	--with-newlib \
%if 0%{?gcc_libc_bootstrap:1}
	--without-headers \
%endif
%endif
%if "%{TARGET_ARCH}" == "spu"
	--with-gxx-include-dir=%sysroot/include/c++/%{gcc_dir_version} \
	--with-newlib \
%endif
%if "%{TARGET_ARCH}" == "nvptx"
	--enable-as-accelerator-for=%{GCCDIST} \
	--disable-sjlj-exceptions \
	--enable-newlib-io-long-long \
%endif
%if "%{TARGET_ARCH}" == "avr"
	--enable-lto \
	--without-gxx-include-dir \
	--with-native-system-header-dir=/include \
%endif
%endif
%if "%{TARGET_ARCH}" == "arm"
        --with-arch=armv6zk \
        --with-tune=arm1176jzf-s \
	--with-float=hard \
	--with-abi=aapcs-linux \
	--with-fpu=vfp \
	--disable-sjlj-exceptions \
%endif
%if "%{TARGET_ARCH}" == "armv5tel"
	--with-arch=armv5te \
	--with-float=soft \
	--with-mode=arm \
	--with-abi=aapcs-linux \
	--disable-sjlj-exceptions \
%endif
%if "%{TARGET_ARCH}" == "armv6hl"
        --with-arch=armv6zk \
        --with-tune=arm1176jzf-s \
        --with-float=hard \
        --with-abi=aapcs-linux \
        --with-fpu=vfp \
        --disable-sjlj-exceptions \
%endif
%if "%{TARGET_ARCH}" == "armv7hl"
	--with-arch=armv7-a \
	--with-tune=cortex-a15 \
	--with-float=hard \
	--with-abi=aapcs-linux \
	--with-fpu=vfpv3-d16 \
	--disable-sjlj-exceptions \
%endif
%if "%{TARGET_ARCH}" == "aarch64"
	--enable-fix-cortex-a53-835769 \
	--enable-fix-cortex-a53-843419 \
%endif
%if "%{TARGET_ARCH}" == "powerpc" || "%{TARGET_ARCH}" == "powerpc64" || "%{TARGET_ARCH}" == "powerpc64le"
%if "%{TARGET_ARCH}" == "powerpc"
        --with-cpu=default32 \
%endif
%if "%{TARGET_ARCH}" == "powerpc64le"
%if %{suse_version} >= 1350
	--with-cpu=power8 \
	--with-tune=power9 \
%else
%if %{suse_version} >= 1315 && %{suse_version} != 1320
	--with-cpu=power8 \
	--with-tune=power8 \
%else
	--with-cpu=power7 \
	--with-tune=power7 \
%endif
%endif
%else
	--with-cpu-64=power4 \
%endif
	--enable-secureplt \
	--with-long-double-128 \
%if "%{TARGET_ARCH}" == "powerpc64le"
	--enable-targets=powerpcle-linux \
	--disable-multilib \
%endif
%endif
%if "%{TARGET_ARCH}" == "sparc64"
	--with-cpu=ultrasparc \
	--with-long-double-128 \
%endif
%if "%{TARGET_ARCH}" == "sparc"
	--with-cpu=v8 \
	--with-long-double-128 \
%endif
%if "%{TARGET_ARCH}" == "i586"
%if 0%{?sle_version:%sle_version} >= 150000
	--with-arch-32=x86-64 \
%else
	--with-arch-32=i586 \
%endif
	--with-tune=generic \
%endif
%if "%{TARGET_ARCH}" == "x86_64"
	--enable-multilib \
	--with-arch-32=x86-64 \
	--with-tune=generic \
%endif
%if "%{TARGET_ARCH}" == "s390"
%if %{suse_version} >= 1310
        --with-tune=zEC12 --with-arch=z196 \
%else
	--with-tune=z9-109 --with-arch=z900 \
%endif
	--with-long-double-128 \
	--enable-decimal-float \
%endif
%if "%{TARGET_ARCH}" == "s390x"
%if %{suse_version} >= 1310
        --with-tune=zEC12 --with-arch=z196 \
%else
	--with-tune=z9-109 --with-arch=z900 \
%endif
	--with-long-double-128 \
	--enable-decimal-float \
%endif
%if "%{TARGET_ARCH}" == "m68k"
	--disable-multilib \
%endif
%if "%{TARGET_ARCH}" == "riscv64"
	--disable-multilib \
%endif
	--build=%{GCCDIST} \
	--host=%{GCCDIST}

STAGE1_FLAGS="-g -O2"
%if 0%{?do_profiling}
%define profiledbootstraprule profiledbootstrap
%endif
# Only run profiled bootstrap on archs where it works and matters
%ifarch x86_64 %ix86 ppc64le s390x aarch64
setarch `arch` -R make %{?profiledbootstraprule} STAGE1_CFLAGS="$STAGE1_FLAGS" BOOT_CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}
%else
make STAGE1_CFLAGS="$STAGE1_FLAGS" BOOT_CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}
%endif
make info
%if 0%{?run_tests:1}
echo "Run testsuite"
(make -C %{GCCDIST}/libstdc++-v3 check-abi || true)
mv %{GCCDIST}/libstdc++-v3/testsuite/libstdc++.log %{GCCDIST}/libstdc++-v3/testsuite/libstdc++-abi.log
mv %{GCCDIST}/libstdc++-v3/testsuite/libstdc++.sum %{GCCDIST}/libstdc++-v3/testsuite/libstdc++-abi.sum
# asan needs a whole shadow address space
ulimit -v unlimited || true
make -k check %{?_smp_mflags} || true
mkdir ../testresults
../contrib/test_summary | tee ../testresults/test_summary.txt
%endif

%define __provides_exclude_from ^%{libsubdir}/.*\.so.*$

%install
# Make sure libtool re-linking libasan at install time doesn't drop the
# libstdc++ reference to make asan of C++ modules in python work
export SUSE_ASNEEDED=0
export NO_BRP_CHECK_BYTECODE_VERSION=true
cd obj-%{GCCDIST}
# Work around tail/head -1 changes
export _POSIX2_VERSION=199209
export LIBRARY_PATH=$RPM_BUILD_ROOT%{libsubdir}:$RPM_BUILD_ROOT%{mainlibdirbi}
make install DESTDIR=$RPM_BUILD_ROOT

# verify libasan really ended up with libstdc++ as NEEDED.
%ifarch %asan_arch
  readelf -d $RPM_BUILD_ROOT%{versmainlibdir}/libasan.so.%{libasan_sover}* | grep 'NEEDED.*libstdc++' || exit 1
%if %{biarch}
  readelf -d $RPM_BUILD_ROOT%{versmainlibdirbi}/libasan.so.%{libasan_sover}* | grep 'NEEDED.*libstdc++' || exit 1
%endif
%endif

# Remove some useless .la files
for lib in libobjc libgfortran libquadmath libcaf_single \
    libgomp libgomp-plugin-hsa libstdc++ libsupc++ libgo \
    libasan libatomic libitm libtsan libcilkrts liblsan libubsan libvtv \
    libmpx libmpxwrappers libstdc++fs libgomp-plugin-nvptx; do
  rm -f $RPM_BUILD_ROOT%{versmainlibdir}/$lib.la
%if %{biarch}
  rm -f $RPM_BUILD_ROOT%{versmainlibdirbi}/$lib.la
%endif
done

mkdir -p $RPM_BUILD_ROOT%{_libdir}
%if %{biarch}
%if %{build_primary_64bit}
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib
%else
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib64
%endif
%endif

%if %{build_cp}
# Merge multilib c++config.h to allow omitting the duplicate and
# identical other arch specific headers
dir_ml=
cxxconfig="`find %{GCCDIST}/libstdc++-v3/include -name c++config.h`"
for i in `find %{GCCDIST}/[36]*/libstdc++-v3/include -name c++config.h 2>/dev/null`; do
  if ! diff -up $cxxconfig $i; then
    file_32=x
    file_64=x
    case $i in
      %{GCCDIST}/32/*)
        file_32=$i
        file_64=$cxxconfig
        dir_ml=32
	;;
      %{GCCDIST}/64/*)
        file_32=$cxxconfig
	file_64=$i
        dir_ml=64
	;;
    esac
    if ! ( test -f "$file_32" && test -f "$file_64" ); then
      echo "Urgs?"
      exit 1
    fi

    cat > $RPM_BUILD_ROOT%{_prefix}/include/c++/%{gcc_dir_version}/%{GCCDIST}/bits/c++config.h <<EOF
#ifndef _CPP_CPPCONFIG_WRAPPER
#define _CPP_CPPCONFIG_WRAPPER 1
#include <bits/wordsize.h>
#if __WORDSIZE == 32
`cat $file_32`
#else
`cat $file_64`
#endif
#endif
EOF
    break
  fi
done
rm -rf $RPM_BUILD_ROOT%{_prefix}/include/c++/%{gcc_dir_version}/%{GCCDIST}/[36]*
if ! test -z "$dir_ml"; then
  ln -s . $RPM_BUILD_ROOT%{_prefix}/include/c++/%{gcc_dir_version}/%{GCCDIST}/$dir_ml
fi
%endif

# move shared libs from versionspecific dir to main libdir, keep a copy
# for link-editing in the .so
for libname in \
%if %{build_fortran}
  libgfortran \
%endif
%ifarch %quadmath_arch
  libquadmath \
%endif
%if %{build_objc}
  libobjc \
%endif
%if %{build_cp}
  libstdc++ \
%endif
%if %{build_go}
  libgo \
%endif
  libgomp \
%if %{build_hsa}
  libgomp-plugin-hsa \
%endif
%if %{build_nvptx}
  libgomp-plugin-nvptx \
%endif
%ifarch %atomic_arch
  libatomic \
%endif
%ifarch %itm_arch
  libitm \
%endif
%ifarch %asan_arch
  libasan \
%endif
%ifarch %tsan_arch
  libtsan \
%endif
%ifarch %cilkrts_arch
  libcilkrts \
%endif
%ifarch %lsan_arch
  liblsan \
%endif
%ifarch %ubsan_arch
  libubsan \
%endif
%ifarch %vtv_arch
  libvtv \
%endif
%ifarch %mpx_arch
  libmpx libmpxwrappers \
%endif
    ; do
  for lib in `find $RPM_BUILD_ROOT%{versmainlibdir} -maxdepth 1 -name $libname.so.*`; do
    mv $lib $RPM_BUILD_ROOT%{mainlibdir}/
  done
  if test -L $RPM_BUILD_ROOT%{versmainlibdir}/$libname.so; then
    cp $RPM_BUILD_ROOT%{mainlibdir}/`readlink $RPM_BUILD_ROOT%{versmainlibdir}/$libname.so` \
         $RPM_BUILD_ROOT%{versmainlibdir}/$libname.so.tem
    rm $RPM_BUILD_ROOT%{versmainlibdir}/$libname.so
    mv $RPM_BUILD_ROOT%{versmainlibdir}/$libname.so.tem $RPM_BUILD_ROOT%{versmainlibdir}/$libname.so
    strip -g $RPM_BUILD_ROOT%{versmainlibdir}/$libname.so
  else
    if test -e $RPM_BUILD_ROOT%{versmainlibdir}/$libname.so; then
      echo ERROR: unexpected linker script for $libname.so
      exit 1
    fi
  fi
%if %{biarch}
  if test -d $RPM_BUILD_ROOT%{versmainlibdirbi}; then
    for lib in `find $RPM_BUILD_ROOT%{versmainlibdirbi} -maxdepth 1 -name "$libname.so.*"`; do
      mv $lib $RPM_BUILD_ROOT%{mainlibdirbi}/
    done
    if test -L $RPM_BUILD_ROOT%{versmainlibdirbi}/$libname.so; then
      cp $RPM_BUILD_ROOT%{mainlibdirbi}/`readlink $RPM_BUILD_ROOT%{versmainlibdirbi}/$libname.so`  \
         $RPM_BUILD_ROOT%{versmainlibdirbi}/$libname.so.tem
      rm $RPM_BUILD_ROOT%{versmainlibdirbi}/$libname.so
      mv $RPM_BUILD_ROOT%{versmainlibdirbi}/$libname.so.tem $RPM_BUILD_ROOT%{versmainlibdirbi}/$libname.so
      strip -g $RPM_BUILD_ROOT%{versmainlibdirbi}/$libname.so
    else
      if test -e $RPM_BUILD_ROOT%{versmainlibdirbi}/$libname.so; then
        echo ERROR: unexpected linker script for $libname.so
	exit 1
      fi
    fi
  fi
%endif
done
%if %{build_cp}
# And we want to move the shlib gdb pretty printers to a more sane
# place so ldconfig does not complain
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gdb/auto-load%{mainlibdir}
mv $RPM_BUILD_ROOT%{mainlibdir}/libstdc++.so.*-gdb.py $RPM_BUILD_ROOT%{_datadir}/gdb/auto-load%{mainlibdir}/
sed -i -e '/^libdir/s/\/gcc\/%{GCCDIST}\/%{gcc_dir_version}//g' $RPM_BUILD_ROOT%{_datadir}/gdb/auto-load%{mainlibdir}/libstdc++.so.*-gdb.py
%if %{biarch}
  if test -d $RPM_BUILD_ROOT%{versmainlibdirbi}; then
    mkdir -p $RPM_BUILD_ROOT%{_datadir}/gdb/auto-load%{mainlibdirbi}
    mv $RPM_BUILD_ROOT%{mainlibdirbi}/libstdc++.so.*-gdb.py $RPM_BUILD_ROOT%{_datadir}/gdb/auto-load%{mainlibdirbi}/
    sed -i -e '/^libdir/s/\/gcc\/%{GCCDIST}\/%{gcc_dir_version}//g' $RPM_BUILD_ROOT%{_datadir}/gdb/auto-load%{mainlibdirbi}/libstdc++.so.*-gdb.py
  fi
%endif
%endif

# Move libgcc_s around, make sure a version specific copy is available
# for link editing
chmod a+x $RPM_BUILD_ROOT/%{_lib}/libgcc_s.so.%{libgcc_s}
if test -L $RPM_BUILD_ROOT/%{_lib}/libgcc_s.so; then
  rm -f $RPM_BUILD_ROOT/%{_lib}/libgcc_s.so
  cp $RPM_BUILD_ROOT/%{_lib}/libgcc_s.so.%{libgcc_s} $RPM_BUILD_ROOT%{versmainlibdir}/libgcc_s.so
  strip -g $RPM_BUILD_ROOT%{versmainlibdir}/libgcc_s.so
else
  mv $RPM_BUILD_ROOT/%{_lib}/libgcc_s.so $RPM_BUILD_ROOT%{versmainlibdir}/
  cp $RPM_BUILD_ROOT/%{_lib}/libgcc_s.so.%{libgcc_s} $RPM_BUILD_ROOT%{versmainlibdir}/libgcc_s.so.%{libgcc_s}
  strip -g $RPM_BUILD_ROOT%{versmainlibdir}/libgcc_s.so.%{libgcc_s}
fi
%if %{biarch}
%if %{build_primary_64bit}
chmod a+x $RPM_BUILD_ROOT/lib/libgcc_s.so.%{libgcc_s}
if test -L $RPM_BUILD_ROOT/lib/libgcc_s.so; then
  rm -f $RPM_BUILD_ROOT/lib/libgcc_s.so
  cp $RPM_BUILD_ROOT/lib/libgcc_s.so.%{libgcc_s} $RPM_BUILD_ROOT%{versmainlibdirbi32}/libgcc_s.so
  strip -g $RPM_BUILD_ROOT%{versmainlibdirbi32}/libgcc_s.so
else
  mv $RPM_BUILD_ROOT/lib/libgcc_s.so $RPM_BUILD_ROOT%{versmainlibdirbi32}/
  cp $RPM_BUILD_ROOT/lib/libgcc_s.so.%{libgcc_s} $RPM_BUILD_ROOT%{versmainlibdirbi32}/libgcc_s.so.%{libgcc_s}
  strip -g $RPM_BUILD_ROOT%{versmainlibdirbi32}/libgcc_s.so.%{libgcc_s}
fi
ln -sf %{versmainlibdirbi32}/libgcc_s.so $RPM_BUILD_ROOT%{versmainlibdirbi32}/libgcc_s_32.so
%else
# 32-bit biarch systems
chmod a+x $RPM_BUILD_ROOT/lib64/libgcc_s.so.%{libgcc_s}
if test -L $RPM_BUILD_ROOT/lib64/libgcc_s.so; then
  rm -f $RPM_BUILD_ROOT/lib64/libgcc_s.so
  cp $RPM_BUILD_ROOT/lib64/libgcc_s.so.%{libgcc_s} $RPM_BUILD_ROOT%{versmainlibdirbi64}/libgcc_s.so
  strip -g $RPM_BUILD_ROOT%{versmainlibdirbi64}/libgcc_s.so
else
  mv $RPM_BUILD_ROOT/lib64/libgcc_s.so $RPM_BUILD_ROOT%{versmainlibdirbi64}/
  cp $RPM_BUILD_ROOT/lib64/libgcc_s.so.%{libgcc_s} $RPM_BUILD_ROOT%{versmainlibdirbi64}/libgcc_s.so.%{libgcc_s}
  strip -g $RPM_BUILD_ROOT%{versmainlibdirbi64}/libgcc_s.so.%{libgcc_s}
fi
ln -sf %{versmainlibdirbi64}/libgcc_s.so $RPM_BUILD_ROOT%{versmainlibdirbi64}/libgcc_s_64.so
%endif
%endif

%if %{build_ada}
mv $RPM_BUILD_ROOT%{libsubdir}/adalib/lib*-*.so $RPM_BUILD_ROOT%{_libdir}
ln -sf %{_libdir}/libgnarl%{binsuffix}.so $RPM_BUILD_ROOT%{libsubdir}/adalib/libgnarl.so
ln -sf %{_libdir}/libgnat%{binsuffix}.so $RPM_BUILD_ROOT%{libsubdir}/adalib/libgnat.so
chmod a+x $RPM_BUILD_ROOT%{_libdir}/libgna*-*.so
%if %{biarch}
mv $RPM_BUILD_ROOT%{versmainlibdirbi}/adalib/lib*-*.so $RPM_BUILD_ROOT%{mainlibdirbi}/
ln -sf %{mainlibdirbi}/libgnarl%{binsuffix}.so $RPM_BUILD_ROOT%{versmainlibdirbi}/adalib/libgnarl.so
ln -sf %{mainlibdirbi}/libgnat%{binsuffix}.so $RPM_BUILD_ROOT%{versmainlibdirbi}/adalib/libgnat.so
chmod a+x $RPM_BUILD_ROOT%{mainlibdirbi}/libgna*-*.so
%endif
%endif

rm -f $RPM_BUILD_ROOT%{_prefix}/bin/c++%{binsuffix}

# Remove some crap from the .la files:
for l in `find $RPM_BUILD_ROOT -name '*.la'`; do
  echo "changing $l"
  sed -e '/^dependency_libs/s| -L%{_builddir}/[^ ]*||g' \
      -e '/^dependency_libs/s| -L/usr/%{GCCDIST}/bin||g' \
      -e '/^dependency_libs/s|-lm \(-lm \)*|-lm |' \
      -e '/^dependency_libs/s|-L[^ ]* ||g' \
%if %{biarch}
%if %{build_primary_64bit}
      -e '/^libdir/s|%{_libdir}/32|%{_prefix}/lib|' \
      -e '/^libdir/s|lib64/\.\./||' \
%else
      -e '/^libdir/s|%{_libdir}/64|%{_prefix}/lib64|' \
%endif
%endif
      < $l  > $l.new
  mv $l.new $l
done

%if 0%{?run_tests:1}
cp `find . -name "*.sum"` ../testresults/
cp `find . -name "*.log"  \! -name "config.log" | grep -v 'acats.\?/tests' ` ../testresults/
chmod 644 ../testresults/*
%endif
# Remove files that we do not need to clean up filelist
rm -f $RPM_BUILD_ROOT%{_prefix}/bin/%{GCCDIST}-*
rm -rf $RPM_BUILD_ROOT%{libsubdir}/install-tools
rm -f $RPM_BUILD_ROOT%{libsubdir}/include-fixed/zutil.h
rm -f $RPM_BUILD_ROOT%{libsubdir}/include-fixed/linux/a.out.h
rm -f $RPM_BUILD_ROOT%{libsubdir}/include-fixed/linux/vt.h
rm -f $RPM_BUILD_ROOT%{libsubdir}/include-fixed/asm-generic/socket.h
rm -f $RPM_BUILD_ROOT%{libsubdir}/include-fixed/bits/mathdef.h
rm -f $RPM_BUILD_ROOT%{libsubdir}/include-fixed/sys/ucontext.h
rm -f $RPM_BUILD_ROOT%{libsubdir}/include-fixed/bits/statx.h
rm -f $RPM_BUILD_ROOT%{libsubdir}/include-fixed/pthread.h
rm -f $RPM_BUILD_ROOT%{libsubdir}/include-fixed/bits/unistd_ext.h
rm -f $RPM_BUILD_ROOT%{libsubdir}/include-fixed/sys/rseq.h
rm -f $RPM_BUILD_ROOT%{libsubdir}/include-fixed/sys/mount.h
rm -f $RPM_BUILD_ROOT%{libsubdir}/include-fixed/bits/sched.h
%if !%{enable_plugins}
# no plugins
rm -rf $RPM_BUILD_ROOT%{libsubdir}/plugin
%endif
rm -f  $RPM_BUILD_ROOT%{_infodir}/dir

rm -f $RPM_BUILD_ROOT%{_mandir}/man7/fsf-funding.7
rm -f $RPM_BUILD_ROOT%{_mandir}/man7/gfdl.7
rm -f $RPM_BUILD_ROOT%{_mandir}/man7/gpl.7
rm -f $RPM_BUILD_ROOT%{_libdir}/libiberty.a
%if %{biarch}
%if %{build_primary_64bit}
rm -f $RPM_BUILD_ROOT%{_prefix}/lib/libiberty.a
%else
rm -f $RPM_BUILD_ROOT%{_prefix}/lib64/libiberty.a
%endif
%endif
rm -f $RPM_BUILD_ROOT%{libsubdir}/liblto_plugin.a
rm -f $RPM_BUILD_ROOT%{libsubdir}/liblto_plugin.la
%if %{build_go}
# gccgo.info isn't properly versioned
rm $RPM_BUILD_ROOT%{_infodir}/gccgo.info*
%endif

# For regular build, some info files do not get renamed properly.
# Do so here.
mv $RPM_BUILD_ROOT%{_infodir}/libgomp.info $RPM_BUILD_ROOT%{_infodir}/libgomp%{binsuffix}.info
%ifarch %itm_arch
mv $RPM_BUILD_ROOT%{_infodir}/libitm.info $RPM_BUILD_ROOT%{_infodir}/libitm%{binsuffix}.info
%endif
%if %{build_fortran}
%ifarch %quadmath_arch
mv $RPM_BUILD_ROOT%{_infodir}/libquadmath.info $RPM_BUILD_ROOT%{_infodir}/libquadmath%{binsuffix}.info
%endif
%endif
%if %{build_ada}
mv $RPM_BUILD_ROOT%{_infodir}/gnat-style.info $RPM_BUILD_ROOT%{_infodir}/gnat-style%{binsuffix}.info
mv $RPM_BUILD_ROOT%{_infodir}/gnat_rm.info $RPM_BUILD_ROOT%{_infodir}/gnat_rm%{binsuffix}.info
mv $RPM_BUILD_ROOT%{_infodir}/gnat_ugn.info $RPM_BUILD_ROOT%{_infodir}/gnat_ugn%{binsuffix}.info
%endif

cd ..
%find_lang cpplib%{binsuffix}
%find_lang gcc%{binsuffix}
%find_lang libstdc++
cat cpplib%{binsuffix}.lang gcc%{binsuffix}.lang > gcc7-locale.lang

%post info
%install_info --info-dir=%{_infodir} %{_infodir}/cpp%{binsuffix}.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/cppinternals%{binsuffix}.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/gcc%{binsuffix}.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/gccint%{binsuffix}.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/gccinstall%{binsuffix}.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/libgomp%{binsuffix}.info.gz
%ifarch %itm_arch
%install_info --info-dir=%{_infodir} %{_infodir}/libitm%{binsuffix}.info.gz
%endif
%if %{build_fortran}
%install_info --info-dir=%{_infodir} %{_infodir}/gfortran%{binsuffix}.info.gz
%ifarch %quadmath_arch
%install_info --info-dir=%{_infodir} %{_infodir}/libquadmath%{binsuffix}.info.gz
%endif
%endif
%if %{build_ada}
%install_info --info-dir=%{_infodir} %{_infodir}/gnat-style%{binsuffix}.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/gnat_rm%{binsuffix}.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/gnat_ugn%{binsuffix}.info.gz
%endif

%preun info
%install_info_delete --info-dir=%{_infodir} %{_infodir}/cpp%{binsuffix}.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/cppinternals%{binsuffix}.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gcc%{binsuffix}.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gccint%{binsuffix}.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gccinstall%{binsuffix}.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libgomp%{binsuffix}.info.gz
%ifarch %itm_arch
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libitm%{binsuffix}.info.gz
%endif
%if %{build_fortran}
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gfortran%{binsuffix}.info.gz
%ifarch %quadmath_arch
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libquadmath%{binsuffix}.info.gz
%endif
%endif
%if %{build_ada}
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gnat-style%{binsuffix}.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gnat_rm%{binsuffix}.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gnat_ugn%{binsuffix}.info.gz
%endif

%files
%defattr(-,root,root)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{GCCDIST}
%dir %{libsubdir}
%dir %{libsubdir}/include
%dir %{libsubdir}/include-fixed
%if %{biarch}
%if %{build_primary_64bit}
%dir %{libsubdir}/32
%else
%dir %{libsubdir}/64
%endif
%endif
%{_prefix}/bin/gcc%{binsuffix}
%{_prefix}/bin/gcov%{binsuffix}
%{_prefix}/bin/gcov-dump%{binsuffix}
%{_prefix}/bin/gcov-tool%{binsuffix}
%{_prefix}/bin/gcc-ar%{binsuffix}
%{_prefix}/bin/gcc-nm%{binsuffix}
%{_prefix}/bin/gcc-ranlib%{binsuffix}
%{libsubdir}/collect2
%{libsubdir}/lto1
%{libsubdir}/lto-wrapper
%{libsubdir}/liblto_plugin.so*
%{libsubdir}/include-fixed/README
%{libsubdir}/include-fixed/limits.h
%{libsubdir}/include-fixed/syslimits.h
%{libsubdir}/include/omp.h
%{libsubdir}/include/float.h
%{libsubdir}/include/iso646.h
%{libsubdir}/include/stdarg.h
%{libsubdir}/include/stdbool.h
%{libsubdir}/include/stdfix.h
%{libsubdir}/include/stddef.h
%{libsubdir}/include/unwind.h
%{libsubdir}/include/varargs.h
%{libsubdir}/include/stdint.h
%{libsubdir}/include/stdint-gcc.h
%{libsubdir}/include/stdnoreturn.h
%{libsubdir}/include/stdalign.h
%{libsubdir}/include/stdatomic.h
%{libsubdir}/include/openacc.h
%{libsubdir}/include/gcov.h
%ifarch %sparc
%{libsubdir}/include/visintrin.h
%endif
%ifarch ppc ppc64 ppc64le
%{libsubdir}/include/altivec.h
%{libsubdir}/include/ppc-asm.h
%{libsubdir}/include/paired.h
%{libsubdir}/include/ppu_intrinsics.h
%{libsubdir}/include/si2vmx.h
%{libsubdir}/include/spe.h
%{libsubdir}/include/spu2vmx.h
%{libsubdir}/include/vec_types.h
%{libsubdir}/include/htmintrin.h
%{libsubdir}/include/htmxlintrin.h
%endif
%ifarch s390 s390x
%{libsubdir}/include/htmintrin.h
%{libsubdir}/include/htmxlintrin.h
%{libsubdir}/include/s390intrin.h
%{libsubdir}/include/vecintrin.h
%endif
%ifarch ia64
%{libsubdir}/include/ia64intrin.h
%endif
%ifarch %arm
%{libsubdir}/include/mmintrin.h
%{libsubdir}/include/unwind-arm-common.h
%{libsubdir}/include/arm_cmse.h
%endif
%ifarch %arm aarch64
%{libsubdir}/include/arm_neon.h
%{libsubdir}/include/arm_acle.h
%{libsubdir}/include/arm_fp16.h
%endif
%ifarch %ix86 x86_64
%{libsubdir}/include/cross-stdarg.h
%{libsubdir}/include/cpuid.h
%{libsubdir}/include/mm3dnow.h
%{libsubdir}/include/mmintrin.h
%{libsubdir}/include/ammintrin.h
%{libsubdir}/include/bmmintrin.h
%{libsubdir}/include/emmintrin.h
%{libsubdir}/include/immintrin.h
%{libsubdir}/include/avxintrin.h
%{libsubdir}/include/pmmintrin.h
%{libsubdir}/include/xmmintrin.h
%{libsubdir}/include/tmmintrin.h
%{libsubdir}/include/nmmintrin.h
%{libsubdir}/include/smmintrin.h
%{libsubdir}/include/wmmintrin.h
%{libsubdir}/include/x86intrin.h
%{libsubdir}/include/ia32intrin.h
%{libsubdir}/include/mm_malloc.h
%{libsubdir}/include/fma4intrin.h
%{libsubdir}/include/xopintrin.h
%{libsubdir}/include/lwpintrin.h
%{libsubdir}/include/popcntintrin.h
%{libsubdir}/include/bmiintrin.h
%{libsubdir}/include/tbmintrin.h
%{libsubdir}/include/avx2intrin.h
%{libsubdir}/include/bmi2intrin.h
%{libsubdir}/include/fmaintrin.h
%{libsubdir}/include/lzcntintrin.h
%{libsubdir}/include/f16cintrin.h
%{libsubdir}/include/adxintrin.h
%{libsubdir}/include/fxsrintrin.h
%{libsubdir}/include/prfchwintrin.h
%{libsubdir}/include/rdseedintrin.h
%{libsubdir}/include/rtmintrin.h
%{libsubdir}/include/xsaveintrin.h
%{libsubdir}/include/xsaveoptintrin.h
%{libsubdir}/include/xtestintrin.h
%{libsubdir}/include/avx512cdintrin.h
%{libsubdir}/include/avx512erintrin.h
%{libsubdir}/include/avx512fintrin.h
%{libsubdir}/include/avx512pfintrin.h
%{libsubdir}/include/shaintrin.h
%{libsubdir}/include/avx512bwintrin.h
%{libsubdir}/include/avx512dqintrin.h
%{libsubdir}/include/avx512vlbwintrin.h
%{libsubdir}/include/avx512vldqintrin.h
%{libsubdir}/include/avx512vlintrin.h
%{libsubdir}/include/avx512ifmaintrin.h
%{libsubdir}/include/avx512ifmavlintrin.h
%{libsubdir}/include/avx512vbmiintrin.h
%{libsubdir}/include/avx512vbmivlintrin.h
%{libsubdir}/include/avx5124fmapsintrin.h
%{libsubdir}/include/avx5124vnniwintrin.h
%{libsubdir}/include/avx512vpopcntdqintrin.h
%{libsubdir}/include/clwbintrin.h
%{libsubdir}/include/clflushoptintrin.h
%{libsubdir}/include/xsavecintrin.h
%{libsubdir}/include/xsavesintrin.h
%{libsubdir}/include/mwaitxintrin.h
%{libsubdir}/include/clzerointrin.h
%{libsubdir}/include/pkuintrin.h
%{libsubdir}/include/sgxintrin.h
%endif
%ifarch m68k
%{libsubdir}/include/math-68881.h
%endif
%ifarch %cilkrts_arch
%{libsubdir}/include/cilk
%endif
%ifarch %asan_arch
%{libsubdir}/include/sanitizer
%endif
%versmainlib *crt*.o
%versmainlib libgcc*.a
%versmainlib libgcov.a
%versmainlib libgcc_s*.so*
%versmainlib libgomp.so
%versmainlib libgomp.a
%versmainlib libgomp.spec
%if %{build_hsa}
%versmainlib libgomp-plugin-hsa.so
%endif
%if %{build_nvptx}
%versmainlib libgomp-plugin-nvptx.so
%endif
%ifarch %itm_arch
%versmainlib libitm.so
%versmainlib libitm.a
%versmainlib libitm.spec
%endif
%ifarch %atomic_arch
%versmainlib libatomic.so
%versmainlib libatomic.a
%endif
%ifarch %asan_arch
%versmainlib libasan.so
%versmainlib libasan.a
%versmainlib libasan_preinit.o
%endif
%ifarch %tsan_arch
%if %build_primary_64bit
%versmainlib libtsan.so
%versmainlib libtsan.a
%versmainlib libtsan_preinit.o
%endif
%endif
%ifarch %cilkrts_arch
%versmainlib libcilkrts.so
%versmainlib libcilkrts.a
%versmainlib libcilkrts.spec
%endif
%ifarch %lsan_arch
%if %build_primary_64bit
%versmainlib liblsan.so
%versmainlib liblsan.a
%endif
%endif
%ifarch %ubsan_arch
%versmainlib libubsan.so
%versmainlib libubsan.a
%endif
%ifarch %asan_arch %ubsan_arch %tsan_arch %lsan_arch
%versmainlib libsanitizer.spec
%endif
%ifarch %vtv_arch
%versmainlib libvtv.so
%versmainlib libvtv.a
%endif
%ifarch %mpx_arch
%versmainlib libmpx.so
%versmainlib libmpx.a
%versmainlib libmpxwrappers.so
%versmainlib libmpxwrappers.a
%versmainlib libmpx.spec
%endif
%doc %{_mandir}/man1/gcc%{binsuffix}.1.gz
%doc %{_mandir}/man1/gcov%{binsuffix}.1.gz
%doc %{_mandir}/man1/gcov-dump%{binsuffix}.1.gz
%doc %{_mandir}/man1/gcov-tool%{binsuffix}.1.gz

%if %{separate_biarch}
%files -n gcc7%{separate_biarch_suffix}
%defattr(-,root,root)
%versbiarchlib *crt*.o
%versbiarchlib libgcc*.a
%versbiarchlib libgcov.a
%versbiarchlib libgcc_s*.so*
%versbiarchlib libgomp.so
%versbiarchlib libgomp.a
%versbiarchlib libgomp.spec
%if %{build_nvptx}
%versbiarchlib libgomp-plugin-nvptx.so
%endif
%ifarch %itm_arch
%versbiarchlib libitm.so
%versbiarchlib libitm.a
%versbiarchlib libitm.spec
%endif
%ifarch %atomic_arch
%versbiarchlib libatomic.a
%versbiarchlib libatomic.so
%endif
%ifarch %asan_arch
%versbiarchlib libasan.a
%versbiarchlib libasan.so
%versbiarchlib libasan_preinit.o
%endif
%ifarch %ubsan_arch
%versbiarchlib libubsan.a
%versbiarchlib libubsan.so
%endif
%ifarch %cilkrts_arch
%versbiarchlib libcilkrts.a
%versbiarchlib libcilkrts.so
%versbiarchlib libcilkrts.spec
%endif
%ifarch %tsan_arch
%if %separate_bi64
%versbiarchlib libtsan.a
%versbiarchlib libtsan.so
%versbiarchlib libtsan_preinit.o
%endif
%endif
%ifarch %lsan_arch
%if %separate_bi64
%versbiarchlib liblsan.a
%versbiarchlib liblsan.so
%endif
%endif
%ifarch %asan_arch %ubsan_arch %tsan_arch %lsan_arch
%versbiarchlib libsanitizer.spec
%endif
%ifarch %vtv_arch
%versbiarchlib libvtv.a
%versbiarchlib libvtv.so
%endif
%ifarch %mpx_arch
%versbiarchlib libmpx.so
%versbiarchlib libmpx.a
%versbiarchlib libmpxwrappers.so
%versbiarchlib libmpxwrappers.a
%versbiarchlib libmpx.spec
%endif
%endif

%if %{enable_plugins}
%files devel
%defattr(-,root,root)
%dir %{libsubdir}/plugin
%{libsubdir}/plugin
%endif

%files locale -f gcc7-locale.lang

%files -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-locale -f libstdc++.lang

%if %{build_cp}
%files c++
%defattr(-,root,root)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{GCCDIST}
%dir %{libsubdir}
%{_prefix}/bin/g++%{binsuffix}
%doc %{_mandir}/man1/g++%{binsuffix}.1.gz
%{libsubdir}/cc1plus

%if %{separate_biarch}
%files c++%{separate_biarch_suffix}
%defattr(-,root,root)
# empty - only for the dependency
%if %{suse_version} < 1310
%doc README
%endif
%endif

%files -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}
%defattr(-,root,root)
%mainlib libstdc++.so.%{libstdcxx_sover}*

%if %{separate_biarch}
%files -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libstdc++.so.%{libstdcxx_sover}*
%endif

%files -n libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}
%defattr(-,root,root)
%versmainlib libstdc++.a
%versmainlib libstdc++fs.a
%versmainlib libstdc++.so
%versmainlib libsupc++.a
%{_prefix}/include/c++
%dir %{_datadir}/gdb
%dir %{_datadir}/gdb/auto-load
%dir %{_datadir}/gdb/auto-load%{_prefix}
%dir %{_datadir}/gdb/auto-load/%{mainlibdir}
%{_datadir}/gdb/auto-load/%{mainlibdir}/libstdc++.so.*-gdb.py
%{_datadir}/gcc%{binsuffix}

%if %{separate_biarch}
%files -n libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%versbiarchlib libstdc++.a
%versbiarchlib libstdc++fs.a
%versbiarchlib libstdc++.so
%versbiarchlib libsupc++.a
%dir %{_datadir}/gdb/auto-load/%{mainlibdirbi}
%{_datadir}/gdb/auto-load/%{mainlibdirbi}/libstdc++.so.*-gdb.py
%endif
%endif

%files -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}
%defattr(-,root,root)
/%{_lib}/libgcc_s.so.%{libgcc_s}
%if %{biarch}
%if %{build_primary_64bit}
%if !%{separate_bi32}
/lib/libgcc_s.so.%{libgcc_s}
%endif
%else
%if !%{separate_bi64}
/lib64/libgcc_s.so.%{libgcc_s}
%endif
%endif
%endif

%if %{separate_bi64}
%files -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-64bit
%defattr(-,root,root)
/lib64/libgcc_s.so.%{libgcc_s}
%endif

%if %{separate_bi32}
%files -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-32bit
%defattr(-,root,root)
/lib/libgcc_s.so.%{libgcc_s}
%endif

%files -n libgomp%{libgomp_sover}%{libgomp_suffix}
%defattr(-,root,root)
%mainlib libgomp.so.%{libgomp_sover}*
%if %{build_hsa}
%mainlib libgomp-plugin-hsa.so.%{libgomp_sover}*
%endif
%if %{build_nvptx}
%mainlib libgomp-plugin-nvptx.so.%{libgomp_sover}*
%endif

%if %{separate_biarch}
%files -n libgomp%{libgomp_sover}%{libgomp_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libgomp.so.%{libgomp_sover}*
%endif
%if %{build_nvptx}
%biarchlib libgomp-plugin-nvptx.so.%{libgomp_sover}*
%endif

%ifarch %asan_arch
%files -n libasan%{libasan_sover}%{libasan_suffix}
%defattr(-,root,root)
%mainlib libasan.so.%{libasan_sover}*

%if %{separate_biarch}
%files -n libasan%{libasan_sover}%{libasan_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libasan.so.%{libasan_sover}*
%endif
%endif

%ifarch %lsan_arch
%if %build_primary_64bit
%files -n liblsan%{liblsan_sover}%{liblsan_suffix}
%defattr(-,root,root)
%mainlib liblsan.so.%{liblsan_sover}*
%endif

%if %{separate_biarch} && %{separate_bi64}
%files -n liblsan%{liblsan_sover}%{liblsan_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib liblsan.so.%{liblsan_sover}*
%endif
%endif

%ifarch %tsan_arch
%if %build_primary_64bit
%files -n libtsan%{libtsan_sover}%{libtsan_suffix}
%defattr(-,root,root)
%mainlib libtsan.so.%{libtsan_sover}*
%endif

%if %{separate_biarch} && %{separate_bi64}
%files -n libtsan%{libtsan_sover}%{libtsan_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libtsan.so.%{libtsan_sover}*
%endif
%endif

%ifarch %atomic_arch
%files -n libatomic%{libatomic_sover}%{libatomic_suffix}
%defattr(-,root,root)
%mainlib libatomic.so.%{libatomic_sover}*

%if %{separate_biarch}
%files -n libatomic%{libatomic_sover}%{libatomic_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libatomic.so.%{libatomic_sover}*
%endif
%endif

%ifarch %itm_arch
%files -n libitm%{libitm_sover}%{libitm_suffix}
%defattr(-,root,root)
%mainlib libitm.so.%{libitm_sover}*

%if %{separate_biarch}
%files -n libitm%{libitm_sover}%{libitm_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libitm.so.%{libitm_sover}*
%endif
%endif

%ifarch %cilkrts_arch
%files -n libcilkrts%{libcilkrts_sover}%{libcilkrts_suffix}
%defattr(-,root,root)
%mainlib libcilkrts.so.%{libcilkrts_sover}*

%if %{separate_biarch}
%files -n libcilkrts%{libcilkrts_sover}%{libcilkrts_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libcilkrts.so.%{libcilkrts_sover}*
%endif
%endif

%ifarch %ubsan_arch
%files -n libubsan%{libubsan_sover}%{libubsan_suffix}
%defattr(-,root,root)
%mainlib libubsan.so.%{libubsan_sover}*

%if %{separate_biarch}
%files -n libubsan%{libubsan_sover}%{libubsan_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libubsan.so.%{libubsan_sover}*
%endif
%endif

%ifarch %vtv_arch
%files -n libvtv%{libvtv_sover}%{libvtv_suffix}
%defattr(-,root,root)
%mainlib libvtv.so.%{libvtv_sover}*

%if %{separate_biarch}
%files -n libvtv%{libvtv_sover}%{libvtv_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libvtv.so.%{libvtv_sover}*
%endif
%endif

%ifarch %mpx_arch
%files -n libmpx%{libmpx_sover}%{libmpx_suffix}
%defattr(-,root,root)
%mainlib libmpx.so.%{libmpx_sover}*

%if %{separate_biarch}
%files -n libmpx%{libmpx_sover}%{libmpx_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libmpx.so.%{libmpx_sover}*
%endif

%files -n libmpxwrappers%{libmpxwrappers_sover}%{libmpxwrappers_suffix}
%defattr(-,root,root)
%mainlib libmpxwrappers.so.%{libmpxwrappers_sover}*

%if %{separate_biarch}
%files -n libmpxwrappers%{libmpxwrappers_sover}%{libmpxwrappers_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libmpxwrappers.so.%{libmpxwrappers_sover}*
%endif
%endif

%if %{build_fortran}
%files fortran
%defattr(-,root,root)
%dir %{libsubdir}/finclude
%{_prefix}/bin/gfortran%{binsuffix}
%{libsubdir}/f951
%{libsubdir}/finclude/*
%versmainlib libgfortran.a
%versmainlib libgfortran.so
%versmainlib libgfortran.spec
%versmainlib libcaf_single.a
%ifarch %quadmath_arch
%{libsubdir}/include/quadmath.h
%{libsubdir}/include/quadmath_weak.h
%versmainlib libquadmath.a
%versmainlib libquadmath.so
%endif
%doc %{_mandir}/man1/gfortran%{binsuffix}.1.gz

%if %{separate_biarch}
%files fortran%{separate_biarch_suffix}
%defattr(-,root,root)
%dir %{versmainlibdirbi}/finclude
%{versmainlibdirbi}/finclude/*
%versbiarchlib libgfortran.a
%versbiarchlib libgfortran.so
%versbiarchlib libgfortran.spec
%versbiarchlib libcaf_single.a
%ifarch %quadmath_arch
%versbiarchlib libquadmath.a
%versbiarchlib libquadmath.so
%endif
%endif

%files -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}
%defattr(-,root,root)
%mainlib libgfortran.so.%{libgfortran_sover}*

%if %{separate_biarch}
%files -n libgfortran%{libgfortran_sover}%{libgfortran_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libgfortran.so.%{libgfortran_sover}*
%endif

%ifarch %quadmath_arch
%files -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}
%defattr(-,root,root)
%mainlib libquadmath.so.%{libquadmath_sover}*

%if %{separate_biarch}
%files -n libquadmath%{libquadmath_sover}%{libquadmath_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libquadmath.so.%{libquadmath_sover}*
%endif
%endif
%endif

%files info
%defattr(-,root,root)
%doc %{_infodir}/cpp%{binsuffix}.info*.gz
%doc %{_infodir}/cppinternals%{binsuffix}.info*.gz
%doc %{_infodir}/gcc%{binsuffix}.info*.gz
%doc %{_infodir}/gccint%{binsuffix}.info*.gz
%doc %{_infodir}/gccinstall%{binsuffix}.info*.gz
%doc %{_infodir}/libgomp%{binsuffix}.info*.gz
%ifarch %itm_arch
%doc %{_infodir}/libitm%{binsuffix}.info*.gz
%endif
%if %{build_fortran}
%doc %{_infodir}/gfortran%{binsuffix}.info*.gz
%ifarch %quadmath_arch
%doc %{_infodir}/libquadmath%{binsuffix}.info*.gz
%endif
%endif
%if %{build_ada}
%doc %{_infodir}/gnat-style%{binsuffix}.info*gz
%doc %{_infodir}/gnat_rm%{binsuffix}.info*gz
%doc %{_infodir}/gnat_ugn%{binsuffix}.info*gz
%endif

%files -n cpp7
%defattr(-,root,root)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{GCCDIST}
%dir %{libsubdir}
%{_prefix}/bin/cpp%{binsuffix}
%{libsubdir}/cc1
%doc %{_mandir}/man1/cpp%{binsuffix}.1.gz

%if %{build_objc}
%files objc
%defattr(-,root,root)
%{libsubdir}/cc1obj
%{libsubdir}/include/objc
%versmainlib libobjc.a
%versmainlib libobjc.so

%if %{separate_biarch}
%files objc%{separate_biarch_suffix}
%defattr(-,root,root)
%versbiarchlib libobjc.a
%versbiarchlib libobjc.so
%endif

%files -n libobjc%{libobjc_sover}%{libobjc_suffix}
%defattr(-,root,root)
%mainlib libobjc.so.%{libobjc_sover}*

%if %{separate_biarch}
%files -n libobjc%{libobjc_sover}%{libobjc_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libobjc.so.%{libobjc_sover}*
%endif
%endif

%if %{build_objcp}
%files obj-c++
%defattr(-,root,root)
%{libsubdir}/cc1objplus

%if %{separate_biarch}
%files obj-c++%{separate_biarch_suffix}
%defattr(-,root,root)
# empty - only for the dependency
%if %{suse_version} < 1310
%doc README
%endif
%endif
%endif

%if %{build_ada}
%files ada
%defattr(-,root,root)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{GCCDIST}
%dir %{libsubdir}
%{_prefix}/bin/gnat*
%dir %{versmainlibdir}/adalib
%{versmainlibdir}/adainclude
%{versmainlibdir}/adalib/*.ali
%{versmainlibdir}/adalib/*.a
%{versmainlibdir}/adalib/libgnarl.so
%{versmainlibdir}/adalib/libgnat.so
%{versmainlibdir}/gnat1

%if %{separate_biarch}
%files ada%{separate_biarch_suffix}
%defattr(-,root,root)
%dir %{versmainlibdirbi}/adalib
%{versmainlibdirbi}/adainclude
%{versmainlibdirbi}/adalib/*.ali
%{versmainlibdirbi}/adalib/*.a
%{versmainlibdirbi}/adalib/libgnarl.so
%{versmainlibdirbi}/adalib/libgnat.so
%endif

%files -n libada7
%defattr(-,root,root)
%mainlib libgnarl%{binsuffix}.so
%mainlib libgnat%{binsuffix}.so

%if %{separate_biarch}
%files -n libada7%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libgnarl%{binsuffix}.so
%biarchlib libgnat%{binsuffix}.so
%endif
%endif

%if %{build_go}
%files go
%defattr(-,root,root)
%{_prefix}/bin/gccgo%{binsuffix}
%{_prefix}/bin/go%{binsuffix}
%{_prefix}/bin/gofmt%{binsuffix}
%{libsubdir}/go1
%versmainlib libgo.a
%versmainlib libgo.so
%versmainlib libgobegin.a
%versmainlib libgolibbegin.a
%versmainlibdir/cgo
%dir %mainlibdir/go
%dir %mainlibdir/go/%{gcc_dir_version}
%mainlibdir/go/%{gcc_dir_version}/%{GCCDIST}
%doc %{_mandir}/man1/gccgo%{binsuffix}.1.gz
%doc %{_mandir}/man1/go%{binsuffix}.1.gz
%doc %{_mandir}/man1/gofmt%{binsuffix}.1.gz

%if %{separate_biarch}
%files go%{separate_biarch_suffix}
%defattr(-,root,root)
%versbiarchlib libgo.a
%versbiarchlib libgo.so
%versbiarchlib libgobegin.a
%versbiarchlib libgolibbegin.a
%dir %mainlibdirbi/go
%dir %mainlibdirbi/go/%{gcc_dir_version}
%mainlibdirbi/go/%{gcc_dir_version}/%{GCCDIST}
%endif

%files -n libgo%{libgo_sover}%{libgo_suffix}
%defattr(-,root,root)
%mainlib libgo.so.%{libgo_sover}*

%if %{separate_biarch}
%files -n libgo%{libgo_sover}%{libgo_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libgo.so.%{libgo_sover}*
%endif
%endif

%if 0%{?run_tests:1}
%files -n gcc7-testresults
%defattr(-,root,root)
%doc testresults/test_summary.txt
%doc testresults/*.sum
%doc testresults/*.log
%endif

%changelog
