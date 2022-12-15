#
# spec file for package gcc13
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


%if !0%{?usrmerged}
%define _slibdir  /%{_lib}
%define slibdir   /lib
%define slibdir64 /lib64
%else
%define _slibdir  %{_libdir}
%define slibdir   %{_prefix}/lib
%define slibdir64 %{_prefix}/lib64
%endif

# Ada currently fails to build on a few platforms, enable it only
# on those that work
%if %{suse_version} >= 1310
%if %{suse_version} >= 1330
%define ada_arch %ix86 x86_64 ppc ppc64 ppc64le s390 s390x ia64 aarch64 riscv64
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

%define quadmath_arch %ix86 x86_64 ia64 ppc64le
%define tsan_arch x86_64 aarch64 ppc ppc64 ppc64le s390 s390x
%define asan_arch x86_64 %ix86 ppc ppc64 ppc64le s390 s390x %sparc %arm aarch64 riscv64
%define hwasan_arch aarch64 x86_64
%define itm_arch x86_64 %ix86 %arm aarch64 ppc ppc64 ppc64le riscv64 s390 s390x %sparc
%define atomic_arch x86_64 %ix86 %arm aarch64 ppc ppc64 ppc64le s390 s390x %sparc m68k ia64 riscv64
%define lsan_arch x86_64 aarch64 ppc ppc64 ppc64le s390 s390x
%define ubsan_arch x86_64 %ix86 ppc ppc64 ppc64le s390 s390x %arm aarch64 riscv64
%if 0%{?build_libvtv:1}
%define vtv_arch x86_64 %ix86
%endif

%define build_cp 1
%define build_fortran 1
%define build_objc 1
%define build_objcp 1
%define build_go 1
%ifarch x86_64 %ix86 %arm aarch64 riscv64 s390x
%define build_d 1
%else
%define build_d 0
%endif

%if %{build_objcp}
%define build_cp 1
%define build_objc 1
%endif

# For optional compilers only build C, C++, Fortran, Ada and Go
%if 0%{?build_optional_compiler_languages:1}
%define build_objc 0
%define build_objcp 0
%define build_d 0
%endif

%ifarch x86_64
%define build_nvptx 1
%else
%define build_nvptx 0
%endif

%ifarch x86_64
# SLE12 does not fulfil build requirements for GCN, SLE15 SP1 does
# technically also SLE12 SP5 but do not bother there
%if %{suse_version} >= 1550 || 0%{?sle_version:%sle_version} >= 150100
%define build_gcn 1
%else
%define build_gcn 0
%endif
%else
%define build_gcn 0
%endif

%define use_lto_bootstrap 0
%ifarch x86_64 ppc64le s390x aarch64
%if %{suse_version} > 1500
%define use_lto_bootstrap 1
%endif
%endif

# Enable plugins just for Tumbleweed, not for SLES
%if 0%{!?sle_version:1}
%define enable_plugins 1
%define build_jit 1
%else
%define enable_plugins 0
%define build_jit 0
%endif

%if 0%{suse_version} >= 1599 || 0%{?sle_version:%sle_version} >= 150300
# FIXME: more once glibc 2.37 is released
%define glibc_version %(rpm -q glibc --qf '%%{VERSION}')
%define floatn_fixed_glibc %(case " %{glibc_version} " in (*9000*) echo 1;; (*) echo 0;; esac)
%else
# The headers are not present in earlier glibc
%define floatn_fixed_glibc 1
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
%define libgfortran_sover 5
%define libquadmath_sover 0
%define libasan_sover 8
%define libtsan_sover 2
%define libhwasan_sover 0
%define libatomic_sover 1
%define libitm_sover 1
%define libubsan_sover 1
%define liblsan_sover 0
%define libvtv_sover 0
%define libgo_sover 22
%define libgphobos_sover 4
%define libgdruntime_sover 4
%define libgccjit_sover 0

# Shared library package suffix
# This is used for the "non-standard" set of libraries, the standard
# being defined by %%product_libs_gcc_ver, the GCC version that should
# provide un-suffixed shared library packages following the shared-library
# policy.  Even suffixed variants should provide the shared-library policy
# mandated names and ensure they conflict with each other.
# Individual shared libraries can be directed to be built from individual
# gcc versions by defining %%product_libs_gcc_ver_libgcc_s1 for example,
# generally %%product_libs_gcc_ver_%%name%%sover, similarly.

%define itsme13 1
%define plv_ %{!?product_libs_gcc_ver:13}%{?product_libs_gcc_ver}
%define plv() %{expand:%%{!?itsme%{expand:%%{!?product_libs_gcc_ver_%{1}%{2}:%%{plv_}}%%{?product_libs_gcc_ver_%{1}%{2}}}:-gcc13}}

%define libgcc_s_suffix %{plv libgcc_s %{libgcc_s}}
%define libgomp_suffix %{plv libgomp %{libgomp_sover}}
%define libstdcxx_suffix %{plv libstdcxx %{libstdcxx_sover}}
%define libobjc_suffix %{plv libobjc %{libobjc_sover}}
%define libgfortran_suffix %{plv libgfortran %{libgfortran_sover}}
%define libquadmath_suffix %{plv libquadmath %{libquadmath_sover}}
%define libasan_suffix %{plv libasan %{libasan_sover}}
%define libtsan_suffix %{plv libtsan %{libtsan_sover}}
%define libhwasan_suffix %{plv libhwasan %{libhwasan_sover}}
%define libatomic_suffix %{plv libatomic %{libatomic_sover}}
%define libitm_suffix %{plv libitm %{libitm_sover}}
%define libubsan_suffix %{plv libubsan %{libubsan_sover}}
%define liblsan_suffix %{plv liblsan %{liblsan_sover}}
%define libvtv_suffix %{plv libvtv %{libvtv_sover}}
%define libgo_suffix %{plv libgo %{libgo_sover}}
%define libgphobos_suffix %{plv libgphobos %{libgphobos_sover}}
%define libgdruntime_suffix %{plv libgdruntime %{libgdruntime_sover}}
%define libgccjit_suffix %{plv libgccjit %{libgccjit_sover}}

# libFOO-devel package suffix
%define libdevel_suffix -gcc13

%if %{suse_version} >= 1220
%define selfconflict() %1
%else
%define selfconflict() otherproviders(%1)
%endif

%define biarch_targets x86_64 s390x powerpc64 powerpc sparc sparc64

URL:            https://gcc.gnu.org/
Version:        13.0.0+git197351
Release:        0
%define gcc_dir_version %(echo %version |  sed 's/+.*//' | cut -d '.' -f 1)
%define gcc_snapshot_revision %(echo %version | sed 's/[3-9]\.[0-9]\.[0-6]//' | sed 's/+/-/')
%define binsuffix -13

Name:           gcc13
BuildRequires:  xz
%if %{suse_version} > 1500
BuildRequires:  libzstd-devel
%endif
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
%if %{suse_version} >= 1500
# for SDT markers in the C++ unwinder and gdb breakpoints on exceptions
BuildRequires:  systemtap-headers
%endif
%if %{suse_version} >= 1230
BuildRequires:  isl-devel
%endif
%define hostsuffix %{nil}
%if %{build_ada}
%if 0%{?gcc_version:%{gcc_version}} > 13
%define hostsuffix %{binsuffix}
BuildRequires:  gcc13-ada
BuildRequires:  gcc13-c++
%else
%if %{suse_version} <= 1315
%define hostsuffix -7
BuildRequires:  gcc7-ada
BuildRequires:  gcc7-c++
%else
%define hostsuffix %{nil}
BuildRequires:  gcc-ada
%endif
%endif
%endif
%if %{build_d}
%if %{suse_version} < 1550
BuildRequires:  gcc11-d
BuildRequires:  libstdc++6-devel-gcc11
%else
BuildRequires:  gcc-d
%endif
%endif
# We now require a C++ 11 capable compiler for bootstrapping
%if %{suse_version} < 1220
%define hostsuffix -4.8
BuildRequires:  gcc48-c++
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
%if %{build_go}
BuildRequires:  netcfg
BuildRequires:  procps
%endif
%if %{build_nvptx}
BuildRequires:  cross-nvptx-gcc13
BuildRequires:  cross-nvptx-newlib13-devel
%endif
%if %{build_gcn}
BuildRequires:  cross-amdgcn-gcc13
BuildRequires:  cross-amdgcn-newlib13-devel
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
%define disable_multilib_arch %{nil}
%else
%define disable_multilib_arch ppc sparcv9 x86_64 s390x ppc64 sparc64
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

%if !0%{?building_testsuite:1}
Requires:       binutils
Requires:       cpp13 = %{version}-%{release}
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
%ifarch %hwasan_arch
Requires:       libhwasan%{libhwasan_sover} >= %{version}-%{release}
%endif
%ifarch %atomic_arch
Requires:       libatomic%{libatomic_sover} >= %{version}-%{release}
%endif
%ifarch %itm_arch
Requires:       libitm%{libitm_sover} >= %{version}-%{release}
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
Suggests:       gcc13-info gcc13-locale
%endif

%if %{suse_version} < 1310
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%endif
Group:          Development/Languages/C and C++
Source:         gcc-%{version}.tar.xz
Source1:        change_spec
Source2:        gcc13-rpmlintrc
Source3:        gcc13-testresults-rpmlintrc
Source4:        README.First-for.SuSE.packagers
Source5:        newlib-4.2.0.20211231.tar.xz
Patch2:         gcc-add-defaultsspec.diff
Patch5:         tls-no-direct.diff
Patch6:         gcc43-no-unwind-tables.diff
Patch7:         gcc48-libstdc++-api-reference.patch
Patch11:        gcc7-remove-Wexpansion-to-defined-from-Wextra.patch
Patch15:        gcc7-avoid-fixinc-error.diff
Patch16:        gcc9-reproducible-builds.patch
Patch17:        gcc9-reproducible-builds-buildid-for-checksum.patch
Patch18:        gcc10-amdgcn-llvm-as.patch
Patch19:        gcc11-gdwarf-4-default.patch
Patch20:        gcc11-amdgcn-disable-hot-cold-partitioning.patch
# A set of patches from the RH srpm
Patch51:        gcc41-ppc32-retaddr.patch
# Some patches taken from Debian
Patch60:        gcc44-textdomain.patch
Patch61:        gcc44-rename-info-files.patch

License:        GPL-3.0-or-later
Summary:        The GNU C Compiler and Support Files

%description
Core package for the GNU Compiler Collection, including the C language
frontend.

Language frontends other than C are split to different sub-packages,
namely gcc-ada, gcc-c++, gcc-fortran, gcc-obj, gcc-obj-c++ and gcc-go.

%package -n gcc13-32bit
Summary:        The GNU C Compiler 32bit support
Group:          Development/Languages/C and C++
Requires:       gcc13 = %{version}-%{release}
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
%ifarch %ubsan_arch
Requires:       libubsan%{libubsan_sover}-32bit >= %{version}-%{release}
%endif
%ifarch %vtv_arch
Requires:       libvtv%{libvtv_sover}-32bit >= %{version}-%{release}
%endif
Requires:       glibc-devel-32bit

%description -n gcc13-32bit
This package contains 32bit support for the GNU Compiler Collection.

%package -n gcc13-64bit
Summary:        The GNU C Compiler 64bit support
Group:          Development/Languages/C and C++
Requires:       gcc13 = %{version}-%{release}
Requires:       libgcc_s%{libgcc_s}-64bit >= %{version}-%{release}
Requires:       libgomp%{libgomp_sover}-64bit >= %{version}-%{release}
%ifarch %asan_arch
Requires:       libasan%{libasan_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %tsan_arch
Requires:       libtsan%{libtsan_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %hwasan_arch
Requires:       libhwasan%{libhwasan_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %atomic_arch
Requires:       libatomic%{libatomic_sover}-64bit >= %{version}-%{release}
%endif
%ifarch %itm_arch
Requires:       libitm%{libitm_sover}-64bit >= %{version}-%{release}
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
Requires:       glibc-devel-64bit

%description -n gcc13-64bit
This package contains 64bit support for the GNU Compiler Collection.

%package devel
Summary:        GCC plugins development enviroment
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc13 = %{version}-%{release}
Requires:       gmp-devel
Requires:       mpc-devel

%description devel
Files required for developing and compiling GCC plugins.

%package locale
Summary:        Locale Data for the GNU Compiler Collection
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc13 = %{version}-%{release}

%description locale
Locale data for the GNU Compiler Collection (GCC) to give error message
in the current locale.

%package PIE
Summary:        A default configuration to build all binaries in PIE mode
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc13 = %{version}-%{release}

%description PIE
This package contains a configuration file (spec) that changes the
compilers default setting to build all ELF binaries in the Position
Independend Executable (PIE) variant. This enables better address
space randomization (ASLR).

%package c++
Summary:        The GNU C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc13 = %{version}-%{release}
Requires:       gcc13-c++ = %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix} = %{version}-%{release}

%description c++
This package contains the GNU compiler for C++.

%package c++-32bit
Summary:        The GNU C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc13-32bit = %{version}-%{release}
Requires:       gcc13-c++ = %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-devel%{libdevel_suffix}-32bit = %{version}-%{release}

%description c++-32bit
This package contains the GNU compiler for C++.

%package c++-64bit
Summary:        The GNU C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       gcc13-64bit = %{version}-%{release}
Requires:       gcc13-c++ = %{version}-%{release}
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

%package -n libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix}
Summary:        GDB pretty printers for the C++ standard library
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
# The -pp packages are tied to a specific shared library
Requires:       libstdc++%{libstdcxx_sover} = %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix} = %{version}-%{release}
Provides:       libstdc++%{libstdcxx_sover}-pp = %{version}-%{release}
# To allow updates from libstdc++6-pp-gccM to libstdc++6-pp we need
# enumerates Obsoletes, the separate -pp package was introduced with GCC9
# and dropped somewhen during the GCC11 to GCC12 transition
Obsoletes:      libstdc++6-pp-gcc9 libstdc++6-pp-gcc10
Obsoletes:      libstdc++6-pp-gcc11
Provides:       libstdc++6-pp-gcc10
Provides:       libstdc++6-pp-gcc11
Provides:       libstdc++6-pp-gcc9
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libstdc++%{libstdcxx_sover}-pp
# packageand() does not work with versioned specifications so the fallback
# is a Requires from libstdc++-devel to preserve previous behavior.
%if %{suse_version} >= 1500
Supplements:    (gdb and libstdc++%{libstdcxx_sover} = %{version}-%{release})
%endif

%description -n libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix}
This package contains pretty printers for the C++ standard library usable
from GDB.

%package -n libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix}-32bit
Summary:        GDB pretty printers for the C++ standard library
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
# The -pp packages are tied to a specific shared library
Requires:       libstdc++%{libstdcxx_sover}-32bit = %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix} = %{version}-%{release}
Provides:       libstdc++%{libstdcxx_sover}-pp-32bit = %{version}-%{release}
# To allow updates from libstdc++6-pp-gccM to libstdc++6-pp we need
# enumerates Obsoletes, the separate -pp package was introduced with GCC9
# and dropped somewhen during the GCC11 to GCC12 transition
Obsoletes:      libstdc++6-pp-gcc9-32bit libstdc++6-pp-gcc10-32bit
Obsoletes:      libstdc++6-pp-gcc11-32bit
Provides:       libstdc++6-pp-gcc10-32bit
Provides:       libstdc++6-pp-gcc11-32bit
Provides:       libstdc++6-pp-gcc9-32bit
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libstdc++%{libstdcxx_sover}-pp-32bit
# packageand() does not work with versioned specifications so the fallback
# is a Requires from libstdc++-devel to preserve previous behavior.
%if %{suse_version} >= 1500
Supplements:    (gdb and libstdc++%{libstdcxx_sover}-32bit = %{version}-%{release})
%endif

%description -n libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix}-32bit
This package contains pretty printers for the C++ standard library usable
from GDB.

%package -n libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix}-64bit
Summary:        GDB pretty printers for the C++ standard library
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
# The -pp packages are tied to a specific shared library
Requires:       libstdc++%{libstdcxx_sover}-64bit = %{version}-%{release}
Requires:       libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix} = %{version}-%{release}
Provides:       libstdc++%{libstdcxx_sover}-pp-64bit = %{version}-%{release}
# To allow updates from libstdc++6-pp-gccM to libstdc++6-pp we need
# enumerates Obsoletes, the separate -pp package was introduced with GCC9
# and dropped somewhen during the GCC11 to GCC12 transition
Obsoletes:      libstdc++6-pp-gcc9-64bit libstdc++6-pp-gcc10-64bit
Obsoletes:      libstdc++6-pp-gcc11-64bit
Provides:       libstdc++6-pp-gcc10-64bit
Provides:       libstdc++6-pp-gcc11-64bit
Provides:       libstdc++6-pp-gcc9-64bit
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libstdc++%{libstdcxx_sover}-pp-64bit
# packageand() does not work with versioned specifications so the fallback
# is a Requires from libstdc++-devel to preserve previous behavior.
%if %{suse_version} >= 1500
Supplements:    (gdb and libstdc++%{libstdcxx_sover}-64bit = %{version}-%{release})
%endif

%description -n libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix}-64bit
This package contains pretty printers for the C++ standard library usable
from GDB.

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
# Fallback for non-existing Supplements support
%if %{suse_version} < 1500
Recommends:     libstdc++%{libstdcxx_sover}-pp = %{version}-%{release}
%endif

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
# Fallback for non-existing Supplements support
%if %{suse_version} < 1500
Recommends:     libstdc++%{libstdcxx_sover}-pp-32bit = %{version}-%{release}
%endif

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
# Fallback for non-existing Supplements support
%if %{suse_version} < 1500
Recommends:     libstdc++%{libstdcxx_sover}-pp-64bit = %{version}-%{release}
%endif

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
Requires:       gcc13 = %{version}-%{release}
Requires:       gcc13-objc = %{version}-%{release}
Requires:       libobjc%{libobjc_sover} >= %{version}-%{release}

%description objc
This package contains the GNU Objective C compiler. Objective C is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package objc-32bit
Summary:        GNU Objective C Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc13-32bit = %{version}-%{release}
Requires:       gcc13-objc = %{version}-%{release}
Requires:       libobjc%{libobjc_sover}-32bit >= %{version}-%{release}

%description objc-32bit
This package contains the GNU Objective C compiler. Objective C is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package objc-64bit
Summary:        GNU Objective C Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc13-64bit = %{version}-%{release}
Requires:       gcc13-objc = %{version}-%{release}
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
Requires:       gcc13-c++ = %{version}-%{release}
Requires:       gcc13-obj-c++ = %{version}-%{release}
Requires:       gcc13-objc = %{version}-%{release}

%description obj-c++
This package contains the GNU Objective C++ compiler. Objective C++ is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package obj-c++-32bit
Summary:        GNU Objective C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc13-c++-32bit = %{version}-%{release}
Requires:       gcc13-obj-c++ = %{version}-%{release}
Requires:       gcc13-objc-32bit = %{version}-%{release}

%description obj-c++-32bit
This package contains the GNU Objective C++ compiler. Objective C++ is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package obj-c++-64bit
Summary:        GNU Objective C++ Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc13-c++-64bit = %{version}-%{release}
Requires:       gcc13-obj-c++ = %{version}-%{release}
Requires:       gcc13-objc-64bit = %{version}-%{release}

%description obj-c++-64bit
This package contains the GNU Objective C++ compiler. Objective C++ is an
object oriented language, created by Next Inc. and used in their
Nextstep OS. The source code is available in the gcc package.

%package -n cpp13
Summary:        The GCC Preprocessor
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++

%description -n cpp13
This Package contains just the preprocessor that is used by the X11
packages.

%package ada
Summary:        GNU Ada Compiler Based on GCC (GNAT)
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc13 = %{version}-%{release}
Requires:       gcc13-ada = %{version}-%{release}
Requires:       libada13 = %{version}-%{release}

%description ada
This package contains an Ada compiler and associated development
tools based on the GNU GCC technology.

%package ada-32bit
Summary:        GNU Ada Compiler Based on GCC (GNAT)
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc13-32bit = %{version}-%{release}
Requires:       gcc13-ada = %{version}-%{release}
Requires:       libada13-32bit = %{version}-%{release}

%description ada-32bit
This package contains an Ada compiler and associated development
tools based on the GNU GCC technology.

%package ada-64bit
Summary:        GNU Ada Compiler Based on GCC (GNAT)
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc13-64bit = %{version}-%{release}
Requires:       gcc13-ada = %{version}-%{release}
Requires:       libada13-64bit = %{version}-%{release}

%description ada-64bit
This package contains an Ada compiler and associated development
tools based on the GNU GCC technology.

%package -n libada13
Summary:        GNU Ada Runtime Libraries
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          System/Libraries
Provides:       libgnarl-13 = %{version}-%{release}
Conflicts:      %selfconflict libgnarl-13
Provides:       libgnat-13 = %{version}-%{release}
Conflicts:      %selfconflict libgnat-13

%description -n libada13
This package contains the shared libraries required to run programs
compiled with the GNU Ada compiler (GNAT) if they are compiled to use
shared libraries. It also contains the shared libraries for the
Implementation of the Ada Semantic Interface Specification (ASIS), the
implementation of Distributed Systems Programming (GLADE) and the Posix
1003.5 Binding (Florist).

%post -n libada13 -p /sbin/ldconfig

%postun -n libada13 -p /sbin/ldconfig

%package -n libada13-32bit
Summary:        GNU Ada Runtime Libraries
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          System/Libraries
Provides:       libgnarl-13-32bit = %{version}-%{release}
Conflicts:      %selfconflict libgnarl-13-32bit
Provides:       libgnat-13-32bit = %{version}-%{release}
Conflicts:      %selfconflict libgnat-13-32bit

%description -n libada13-32bit
This package contains the shared libraries required to run programs
compiled with the GNU Ada compiler (GNAT) if they are compiled to use
shared libraries. It also contains the shared libraries for the
Implementation of the Ada Semantic Interface Specification (ASIS), the
implementation of Distributed Systems Programming (GLADE) and the Posix
1003.5 Binding (Florist).

%post -n libada13-32bit -p /sbin/ldconfig

%postun -n libada13-32bit -p /sbin/ldconfig

%package -n libada13-64bit
Summary:        GNU Ada Runtime Libraries
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Group:          System/Libraries
Provides:       libgnarl-13-64bit = %{version}-%{release}
Conflicts:      %selfconflict libgnarl-13-64bit
Provides:       libgnat-13-64bit = %{version}-%{release}
Conflicts:      %selfconflict libgnat-13-64bit

%description -n libada13-64bit
This package contains the shared libraries required to run programs
compiled with the GNU Ada compiler (GNAT) if they are compiled to use
shared libraries. It also contains the shared libraries for the
Implementation of the Ada Semantic Interface Specification (ASIS), the
implementation of Distributed Systems Programming (GLADE) and the Posix
1003.5 Binding (Florist).

%post -n libada13-64bit -p /sbin/ldconfig

%postun -n libada13-64bit -p /sbin/ldconfig

%package fortran
Summary:        The GNU Fortran Compiler and Support Files
License:        GPL-3.0-or-later
Group:          Development/Languages/Fortran
Requires:       gcc13 = %{version}-%{release}
Requires:       gcc13-fortran = %{version}-%{release}
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
Requires:       gcc13-32bit = %{version}-%{release}
Requires:       gcc13-fortran = %{version}-%{release}
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
Requires:       gcc13-64bit = %{version}-%{release}
Requires:       gcc13-fortran = %{version}-%{release}
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

%package -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}
Summary:        The GNU Compiler Hardware-assisted Address Sanitizer Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libhwasan%{libhwasan_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libhwasan%{libhwasan_sover}

%description -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}
The runtime library needed to run programs compiled with the
-fsanitize=hwaddress option of the GNU Compiler Collection (GCC).

%post -n libhwasan%{libhwasan_sover}%{libhwasan_suffix} -p /sbin/ldconfig

%postun -n libhwasan%{libhwasan_sover}%{libhwasan_suffix} -p /sbin/ldconfig

%package -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}-32bit
Summary:        The GNU Compiler Hardware-assisted Address Sanitizer Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libhwasan%{libhwasan_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libhwasan%{libhwasan_sover}-32bit

%description -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}-32bit
The runtime library needed to run programs compiled with the
-fsanitize=hwaddress option of the GNU Compiler Collection (GCC).

%post -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}-32bit -p /sbin/ldconfig

%postun -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}-32bit -p /sbin/ldconfig

%package -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}-64bit
Summary:        The GNU Compiler Hardware-assisted Address Sanitizer Runtime Library
License:        MIT
Group:          Development/Languages/C and C++
Provides:       libhwasan%{libhwasan_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libhwasan%{libhwasan_sover}-64bit

%description -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}-64bit
The runtime library needed to run programs compiled with the
-fsanitize=hwaddress option of the GNU Compiler Collection (GCC).

%post -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}-64bit -p /sbin/ldconfig

%postun -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}-64bit -p /sbin/ldconfig

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
Requires:       gcc13 = %{version}-%{release}
Requires:       gcc13-go = %{version}-%{release}
Requires:       libgo%{libgo_sover} >= %{version}-%{release}

%description go
This package contains a Go compiler and associated development
files based on the GNU GCC technology.

%package go-32bit
Summary:        GNU Go Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc13-32bit = %{version}-%{release}
Requires:       gcc13-go = %{version}-%{release}
Requires:       libgo%{libgo_sover}-32bit >= %{version}-%{release}

%description go-32bit
This package contains a Go compiler and associated development
files based on the GNU GCC technology.

%package go-64bit
Summary:        GNU Go Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc13-64bit = %{version}-%{release}
Requires:       gcc13-go = %{version}-%{release}
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

%package d
Summary:        GNU D Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc13 = %{version}-%{release}
Requires:       gcc13-d = %{version}-%{release}
Requires:       libgdruntime%{libgdruntime_sover} >= %{version}-%{release}
Requires:       libgphobos%{libgphobos_sover} >= %{version}-%{release}

%description d
This package contains a D compiler and associated development
files based on the GNU GCC technology.

%package d-32bit
Summary:        GNU D Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc13-32bit = %{version}-%{release}
Requires:       gcc13-d = %{version}-%{release}
Requires:       libgdruntime%{libgdruntime_sover}-32bit >= %{version}-%{release}
Requires:       libgphobos%{libgphobos_sover}-32bit >= %{version}-%{release}

%description d-32bit
This package contains a D compiler and associated development
files based on the GNU GCC technology.

%package d-64bit
Summary:        GNU D Compiler
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Requires:       gcc13-64bit = %{version}-%{release}
Requires:       gcc13-d = %{version}-%{release}
Requires:       libgdruntime%{libgdruntime_sover}-64bit >= %{version}-%{release}
Requires:       libgphobos%{libgphobos_sover}-64bit >= %{version}-%{release}

%description d-64bit
This package contains a D compiler and associated development
files based on the GNU GCC technology.

%package -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}
Summary:        GNU D compiler runtime library
License:        BSL-1.0
Group:          Development/Languages/Other
Provides:       libgphobos%{libgphobos_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgphobos%{libgphobos_sover}

%description -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}
Runtime library for the GNU D language.

%post -n libgphobos%{libgphobos_sover}%{libgphobos_suffix} -p /sbin/ldconfig

%postun -n libgphobos%{libgphobos_sover}%{libgphobos_suffix} -p /sbin/ldconfig

%package -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}-32bit
Summary:        GNU D compiler runtime library
License:        BSL-1.0
Group:          Development/Languages/Other
Provides:       libgphobos%{libgphobos_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgphobos%{libgphobos_sover}-32bit

%description -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}-32bit
Runtime library for the GNU D language.

%post -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}-32bit -p /sbin/ldconfig

%postun -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}-32bit -p /sbin/ldconfig

%package -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}-64bit
Summary:        GNU D compiler runtime library
License:        BSL-1.0
Group:          Development/Languages/Other
Provides:       libgphobos%{libgphobos_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgphobos%{libgphobos_sover}-64bit

%description -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}-64bit
Runtime library for the GNU D language.

%post -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}-64bit -p /sbin/ldconfig

%postun -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}-64bit -p /sbin/ldconfig

%package -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}
Summary:        GNU D compiler runtime library
License:        BSL-1.0
Group:          Development/Languages/Other
Provides:       libgdruntime%{libgdruntime_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgdruntime%{libgdruntime_sover}

%description -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}
Runtime library for the GNU D language.

%post -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix} -p /sbin/ldconfig

%postun -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix} -p /sbin/ldconfig

%package -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}-32bit
Summary:        GNU D compiler runtime library
License:        BSL-1.0
Group:          Development/Languages/Other
Provides:       libgdruntime%{libgdruntime_sover}-32bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgdruntime%{libgdruntime_sover}-32bit

%description -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}-32bit
Runtime library for the GNU D language.

%post -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}-32bit -p /sbin/ldconfig

%postun -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}-32bit -p /sbin/ldconfig

%package -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}-64bit
Summary:        GNU D compiler runtime library
License:        BSL-1.0
Group:          Development/Languages/Other
Provides:       libgdruntime%{libgdruntime_sover}-64bit = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgdruntime%{libgdruntime_sover}-64bit

%description -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}-64bit
Runtime library for the GNU D language.

%post -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}-64bit -p /sbin/ldconfig

%postun -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}-64bit -p /sbin/ldconfig

%package -n libgccjit%{libgccjit_sover}%{libgccjit_suffix}
Summary:        The GNU Compiler Collection JIT library
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Provides:       libgccjit%{libgccjit_sover} = %{version}-%{release}
# Only one package may provide this - allows multiple gcc versions
# to co-exist without an overly large list of provides/obsoletes
Conflicts:      %selfconflict libgccjit%{libgccjit_sover}
Requires:       gcc13

%description -n libgccjit%{libgccjit_sover}%{libgccjit_suffix}
Support for embedding GCC inside programs and libraries

%post -n libgccjit%{libgccjit_sover}%{libgccjit_suffix} -p /sbin/ldconfig

%postun -n libgccjit%{libgccjit_sover}%{libgccjit_suffix} -p /sbin/ldconfig

%package -n libgccjit%{libgccjit_sover}-devel%{libdevel_suffix}
Summary:        Support for embedding GCC inside programs and libraries
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
Provides:       libgccjit%{libgccjit_sover}-devel = %{version}-%{release}
# Only one gccjit package can be installed at the same time since
# header files conflict
Conflicts:      %selfconflict libgccjit%{libgccjit_sover}-devel
Requires:       libgccjit%{libgccjit_sover}%{libgccjit_suffix}

%description -n libgccjit%{libgccjit_sover}-devel%{libdevel_suffix}
Package contains header files and documentation for GCC JIT front-end.

%package -n gcc13-testresults
Summary:        Testsuite results
License:        SUSE-Public-Domain
Group:          Development/Languages/C and C++

%description -n gcc13-testresults
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

%define HOST_ARCH %(echo %{_host_cpu} | sed -e "s/i.86/i586/;s/ppc/powerpc/;s/sparc64.*/sparc64/;s/sparcv.*/sparc/;")
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

%if 0%{suse_version} >= 1500
# Synchronize output by lines, useful for configure output
%define make_output_sync -Oline
%endif

%prep
%if 0%{?nvptx_newlib:1}%{?amdgcn_newlib:1}
%setup -q -n gcc-%{version} -a 5
ln -s newlib-4.2.0.20211231/newlib .
%else
%setup -q -n gcc-%{version}
%endif

#test patching start

%patch2
%patch5
%patch6
%patch7
%patch11
%patch15
%patch16
%patch17 -p1
# These patches are needed only for llvm11
%if "%{TARGET_ARCH}" == "amdgcn" && %{suse_version} < 1550
%patch18 -p1
%patch20 -p1
%endif
# In SLE15 and earlier default to dwarf4, not dwarf5
%if %{suse_version} < 1550
%patch19 -p1
%endif
%patch51
%patch60 -p1
%patch61

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
%if %{build_d}
languages=$languages,d
%endif
%if %{build_jit}
languages=$languages,jit
%endif

# In general we want to ship release checking enabled compilers
# which is the default for released compilers
#ENABLE_CHECKING="--enable-checking=yes"
ENABLE_CHECKING="--enable-checking=release"
#ENABLE_CHECKING=""

# Work around tail/head -1 changes
export _POSIX2_VERSION=199209

%if "%{TARGET_ARCH}" == "amdgcn"
mkdir -p target-tools/bin
ln -s /usr/bin/llvm-ar target-tools/bin/amdgcn-amdhsa-ar
ln -s /usr/bin/llvm-mc target-tools/bin/amdgcn-amdhsa-as
ln -s /usr/bin/lld target-tools/bin/amdgcn-amdhsa-ld
ln -s /usr/bin/llvm-nm target-tools/bin/amdgcn-amdhsa-nm
ln -s /usr/bin/llvm-ranlib target-tools/bin/amdgcn-amdhsa-ranlib
export PATH="`pwd`/target-tools/bin:$PATH"
%endif

%if "%{hostsuffix}" != ""
mkdir -p host-tools/bin
# Using the host gnatmake like
#   CC="gcc%%{hostsuffix}" GNATBIND="gnatbind%%{hostsuffix}"
#   GNATMAKE="gnatmake%%{hostsuffix}"
# doesn't work due to PR33857, so an un-suffixed gnatmake has to be
# available
%if %{build_ada}
cp -a /usr/bin/gnatmake%{hostsuffix} host-tools/bin/gnatmake
cp -a /usr/bin/gnatlink%{hostsuffix} host-tools/bin/gnatlink
cp -a /usr/bin/gnatbind%{hostsuffix} host-tools/bin/gnatbind
%endif
cp -a /usr/bin/gcc%{hostsuffix} host-tools/bin/gcc
cp -a /usr/bin/g++%{hostsuffix} host-tools/bin/g++
ln -sf /usr/%{_lib} host-tools/%{_lib}
export PATH="`pwd`/host-tools/bin:$PATH"
%endif

%if %{build_d} && %{suse_version} < 1550
# We are using gcc11-d to bootstrap d
export GDC=gdc-11
%endif

# libsanitizer needs <crypt.h> and since the glibc/libxcrypt split
# we don't have that yet in a pure cross environment
%if 0%{?gcc_target_arch:1}
	CONFARGS="$CONFARGS --disable-libsanitizer"
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
%if %{build_nvptx} || %{build_gcn}
	--enable-offload-targets=\
%if %{build_nvptx}
nvptx-none,\
%endif
%if %{build_gcn}
amdgcn-amdhsa,\
%endif
  --enable-offload-defaulted \
%endif
%if %{build_nvptx}
	--without-cuda-driver \
%endif
%if %{build_jit}
  --enable-host-shared \
%endif
	$ENABLE_CHECKING \
	--disable-werror \
	--with-gxx-include-dir=%{_prefix}/include/c++/%{gcc_dir_version} \
	--enable-ssp \
	--disable-libssp \
%if 0%{!?build_libvtv:1}
	--disable-libvtv \
%endif
%if 0%{suse_version} >= 1500
	--enable-cet=auto \
%else
	--disable-cet \
%endif
	--disable-libcc1 \
%if %{enable_plugins}
	--enable-plugin \
%else
	--disable-plugin \
%endif
	--with-bugurl="https://bugs.opensuse.org/" \
	--with-pkgversion="SUSE Linux" \
%if 0%{?sysroot:1}
	--with-slibdir=%{sysroot}/%{_lib} \
%else
	--with-slibdir=/%{_lib} \
%endif
	--with-system-zlib \
	--enable-libstdcxx-allocator=new \
	--disable-libstdcxx-pch \
%if 0%{suse_version} <= 1320
	--with-default-libstdcxx-abi=gcc4-compatible \
%endif
%if %{build_d}
	--enable-libphobos \
%endif
	--enable-version-specific-runtime-libs \
	--with-gcc-major-version-only \
%if 0%{!?gcc_target_arch:1}
	--enable-linker-build-id \
%else
%if 0%{?gcc_target_glibc:1}
	--enable-linker-build-id \
%endif
%endif
	--enable-linux-futex \
%if %{suse_version} >= 1315
%ifarch %ix86 x86_64 ppc ppc64 ppc64le %arm aarch64 s390 s390x %sparc
	--enable-gnu-indirect-function \
%endif
%endif
	--program-suffix=%{binsuffix} \
%ifarch %{disable_multilib_arch}
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
	--disable-gcov \
%endif
%else
%if 0%{?gcc_libc_bootstrap:1}
	--disable-gcov --disable-threads --disable-shared \
	--disable-libmudflap --disable-libssp --disable-libgomp \
	--disable-libquadmath --disable-libatomic \
	--without-headers --with-newlib \
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
%if "%{TARGET_ARCH}" == "amdgcn"
	--enable-as-accelerator-for=%{GCCDIST} \
	--enable-libgomp \
%endif
%if "%{TARGET_ARCH}" == "avr"
	--enable-lto \
	--without-gxx-include-dir \
	--with-native-system-header-dir=/include \
%endif
%endif
%if "%{TARGET_ARCH}" == "arm-none"
	--enable-multilib \
	--with-multilib-list=aprofile,rmprofile \
	--disable-decimal-float \
	--disable-libffi \
	--disable-libgomp \
	--disable-libmudflap \
	--disable-libquadmath \
	--disable-shared \
	--disable-threads \
	--disable-tls \
%endif
%if "%{TARGET_ARCH}" == "armv6hl" || "%{TARGET_ARCH}" == "arm"
	--with-cpu=arm1176jzf-s \
        --with-float=hard \
        --with-abi=aapcs-linux \
        --with-fpu=vfpv2 \
        --disable-sjlj-exceptions \
%endif
%if "%{TARGET_ARCH}" == "armv7hl"
	--with-cpu=generic-armv7-a \
	--with-float=hard \
	--with-abi=aapcs-linux \
	--with-fpu=vfpv3-d16 \
	--disable-sjlj-exceptions \
%endif
%if "%{TARGET_ARCH}" == "aarch64"
	--enable-fix-cortex-a53-835769 \
	--enable-fix-cortex-a53-843419 \
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
%if %{suse_version} > 1500
	--with-long-double-format=ieee \
%else
	--with-long-double-format=ibm \
%endif
	--enable-secureplt \
	--with-long-double-128 \
	--enable-targets=powerpcle-linux \
	--disable-multilib \
%endif
%if "%{TARGET_ARCH}" == "powerpc" || "%{TARGET_ARCH}" == "powerpc64"
%if "%{TARGET_ARCH}" == "powerpc"
        --with-cpu=default32 \
%endif
	--with-cpu-64=power4 \
	--enable-secureplt \
	--with-long-double-128 \
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
%ifnarch %{disable_multilib_arch}
	--enable-multilib \
	--with-arch-32=x86-64 \
%endif
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
%if %{use_lto_bootstrap} && !0%{?building_testsuite:1}
	--with-build-config=bootstrap-lto-lean \
	--enable-link-mutex \
%endif
%ifarch riscv64
	--enable-link-mutex \
%endif
	$CONFARGS \
	--build=%{GCCDIST} \
	--host=%{GCCDIST} || \
  {
    rc=$?;
    echo "------- BEGIN config.log ------";
    %{__cat} config.log;
    echo "------- END config.log ------";
    exit $rc;
  }

STAGE1_FLAGS="-g -O2"
%if 0%{?do_profiling} && !0%{?building_testsuite:1}
%ifarch x86_64 %ix86 ppc64le s390x aarch64
%define use_pgo_bootstrap 1
%endif
%endif
%{?use_pgo_bootstrap:setarch `arch` -R} make %{?make_output_sync} %{?use_pgo_bootstrap:profiledbootstrap} STAGE1_CFLAGS="$STAGE1_FLAGS" BOOT_CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}
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

%install
# Make sure libtool re-linking libasan at install time doesn't drop the
# libstdc++ reference to make asan of C++ modules in python work
export SUSE_ASNEEDED=0
export NO_BRP_CHECK_BYTECODE_VERSION=true
cd obj-%{GCCDIST}
# Work around tail/head -1 changes
export _POSIX2_VERSION=199209
export LIBRARY_PATH=%{buildroot}/%{libsubdir}:%{buildroot}/%{mainlibdirbi}

%make_install

# verify libasan really ended up with libstdc++ as NEEDED.
%ifarch %asan_arch
  readelf -d %{buildroot}/%{versmainlibdir}/libasan.so.%{libasan_sover}* | grep 'NEEDED.*libstdc++' || exit 1
%if %{biarch}
  readelf -d %{buildroot}/%{versmainlibdirbi}/libasan.so.%{libasan_sover}* | grep 'NEEDED.*libstdc++' || exit 1
%endif
%endif

# Remove some useless .la files
for lib in libobjc libgfortran libquadmath libcaf_single \
    libgomp libgomp-plugin-hsa libstdc++ libsupc++ libgo \
    libasan libhwasan libatomic libitm libtsan liblsan libubsan libvtv \
    libstdc++fs libgomp-plugin-nvptx libgomp-plugin-gcn \
    libgdruntime libgphobos libstdc++exp; do
  rm -f %{buildroot}/%{versmainlibdir}/$lib.la
%if %{biarch}
  rm -f %{buildroot}/%{versmainlibdirbi}/$lib.la
%endif
done

mkdir -p %{buildroot}/%{_libdir}
%if %{biarch}
%if %{build_primary_64bit}
mkdir -p %{buildroot}/%{_prefix}/lib
%else
mkdir -p %{buildroot}/%{_prefix}/lib64
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

    cat > %{buildroot}/%{_prefix}/include/c++/%{gcc_dir_version}/%{GCCDIST}/bits/c++config.h <<EOF
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
rm -rf %{buildroot}/%{_prefix}/include/c++/%{gcc_dir_version}/%{GCCDIST}/[36]*
if ! test -z "$dir_ml"; then
  ln -s . %{buildroot}/%{_prefix}/include/c++/%{gcc_dir_version}/%{GCCDIST}/$dir_ml
fi
%endif

# move shared libs from versionspecific dir to main libdir
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
%if %{build_d}
  libgdruntime \
  libgphobos \
%endif
  libgomp \
%if %{build_nvptx}
  libgomp-plugin-nvptx \
%endif
%if %{build_gcn}
  libgomp-plugin-gcn \
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
%ifarch %lsan_arch
  liblsan \
%endif
%ifarch %ubsan_arch
  libubsan \
%endif
%ifarch %hwasan_arch
  libhwasan \
%endif
%ifarch %vtv_arch
  libvtv \
%endif
    ; do
  for lib in `find %{buildroot}/%{versmainlibdir} -maxdepth 1 -name $libname.so.*`; do
    mv $lib %{buildroot}/%{mainlibdir}/
  done
  if test -L %{buildroot}/%{versmainlibdir}/$libname.so; then
    ln -sf %{mainlibdir}/`readlink %{buildroot}/%{versmainlibdir}/$libname.so | sed -e 's/\(.*\.so\.[^\.]*\).*/\1/'`  \
         %{buildroot}/%{versmainlibdir}/$libname.so
  fi
%if %{biarch}
  if test -d %{buildroot}/%{versmainlibdirbi}; then
    for lib in `find %{buildroot}/%{versmainlibdirbi} -maxdepth 1 -name "$libname.so.*"`; do
      mv $lib %{buildroot}/%{mainlibdirbi}/
    done
    if test -L %{buildroot}/%{versmainlibdirbi}/$libname.so; then
      ln -sf %{mainlibdirbi}/`readlink %{buildroot}/%{versmainlibdirbi}/$libname.so | sed -e 's/\(.*\.so\.[^\.]*\).*/\1/'`  \
         %{buildroot}/%{versmainlibdirbi}/$libname.so
    fi
  fi
%endif
done
%if %{build_cp}
# And we want to move the shlib gdb pretty printers to a more sane
# place so ldconfig does not complain
mkdir -p %{buildroot}/%{_datadir}/gdb/auto-load%{mainlibdir}
mv %{buildroot}/%{mainlibdir}/libstdc++.so.*-gdb.py %{buildroot}/%{_datadir}/gdb/auto-load%{mainlibdir}/
sed -i -e '/^libdir/s/\/gcc\/%{GCCDIST}\/%{gcc_dir_version}//g' %{buildroot}/%{_datadir}/gdb/auto-load%{mainlibdir}/libstdc++.so.*-gdb.py
%if %{biarch}
  if test -d %{buildroot}/%{versmainlibdirbi}; then
    mkdir -p %{buildroot}/%{_datadir}/gdb/auto-load%{mainlibdirbi}
    mv %{buildroot}/%{mainlibdirbi}/libstdc++.so.*-gdb.py %{buildroot}/%{_datadir}/gdb/auto-load%{mainlibdirbi}/
    sed -i -e '/^libdir/s/\/gcc\/%{GCCDIST}\/%{gcc_dir_version}//g' %{buildroot}/%{_datadir}/gdb/auto-load%{mainlibdirbi}/libstdc++.so.*-gdb.py
  fi
%endif
%endif

# Move libgcc_s around
if test -L %{buildroot}/%{_lib}/libgcc_s.so; then
  rm -f %{buildroot}/%{_lib}/libgcc_s.so
  ln -sf /%{_lib}/libgcc_s.so.%{libgcc_s} %{buildroot}/%{versmainlibdir}/libgcc_s.so
else
  mv %{buildroot}/%{_lib}/libgcc_s.so %{buildroot}/%{versmainlibdir}/
fi
chmod a+x %{buildroot}/%{_lib}/libgcc_s.so.%{libgcc_s}
%if 0%{?usrmerged}
mv %{buildroot}/%{_lib}/libgcc_s.so.%{libgcc_s} %{buildroot}/%{_slibdir}/libgcc_s.so.%{libgcc_s}
%endif
%if %{biarch}
%if %{build_primary_64bit}
if test -L %{buildroot}/lib/libgcc_s.so; then
  rm -f %{buildroot}/lib/libgcc_s.so
  ln -sf /lib/libgcc_s.so.%{libgcc_s} %{buildroot}/%{versmainlibdirbi32}/libgcc_s.so
else
  mv %{buildroot}/lib/libgcc_s.so %{buildroot}/%{versmainlibdirbi32}/
fi
ln -sf %{versmainlibdirbi32}/libgcc_s.so %{buildroot}/%{versmainlibdirbi32}/libgcc_s_32.so
chmod a+x %{buildroot}/lib/libgcc_s.so.%{libgcc_s}
%if 0%{?usrmerged}
mv %{buildroot}/lib/libgcc_s.so.%{libgcc_s} %{buildroot}/%{slibdir}/libgcc_s.so.%{libgcc_s}
%endif
%else
# 32-bit biarch systems
if test -L %{buildroot}/lib64/libgcc_s.so; then
  rm -f %{buildroot}/lib64/libgcc_s.so
  ln -sf /lib64/libgcc_s.so.%{libgcc_s} %{buildroot}/%{versmainlibdirbi64}/libgcc_s.so
else
  mv %{buildroot}/lib64/libgcc_s.so %{buildroot}/%{versmainlibdirbi64}/
fi
ln -sf %{versmainlibdirbi64}/libgcc_s.so %{buildroot}/%{versmainlibdirbi64}/libgcc_s_64.so
chmod a+x %{buildroot}/lib64/libgcc_s.so.%{libgcc_s}
%if 0%{?usrmerged}
mv %{buildroot}/lib64/libgcc_s.so.%{libgcc_s} %{buildroot}/%{slibdir64}/libgcc_s.so.%{libgcc_s}
%endif
%endif
%endif

%if %{build_ada}
mv %{buildroot}/%{libsubdir}/adalib/lib*-*.so %{buildroot}/%{_libdir}
ln -sf %{_libdir}/libgnarl%{binsuffix}.so %{buildroot}/%{libsubdir}/adalib/libgnarl.so
ln -sf %{_libdir}/libgnat%{binsuffix}.so %{buildroot}/%{libsubdir}/adalib/libgnat.so
chmod a+x %{buildroot}/%{_libdir}/libgna*-*.so
%if %{biarch}
mv %{buildroot}/%{versmainlibdirbi}/adalib/lib*-*.so %{buildroot}/%{mainlibdirbi}/
ln -sf %{mainlibdirbi}/libgnarl%{binsuffix}.so %{buildroot}/%{versmainlibdirbi}/adalib/libgnarl.so
ln -sf %{mainlibdirbi}/libgnat%{binsuffix}.so %{buildroot}/%{versmainlibdirbi}/adalib/libgnat.so
chmod a+x %{buildroot}/%{mainlibdirbi}/libgna*-*.so
%endif
%endif

rm -f %{buildroot}/%{_prefix}/bin/c++%{binsuffix}

# Remove some crap from the .la files:
for l in `find %{buildroot} -name '*.la'`; do
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

# The spec for the PIE subpackage
cat > %{buildroot}/%{libsubdir}/defaults.spec <<EOF
*default_spec:
%%{pie|fpic|fPIC|fpie|fPIE|no-pie|fno-pic|fno-PIC|fno-pie|fno-PIE|shared|static|nostdlib|nodefaultlibs|nostartfiles:;:-fPIE}%%{fno-pic|fno-PIC|fno-pie|fno-PIE|pie|no-pie|shared|static|nostdlib|nodefaultlibs|nostartfiles:;: -pie}
EOF

%if 0%{?run_tests:1}
cp `find . -name "*.sum"` ../testresults/
cp `find . -name "*.log"  \! -name "config.log" | grep -v 'acats.\?/tests' | grep -v libbacktrace` ../testresults/
chmod 644 ../testresults/*
%endif
# Remove files that we do not need to clean up filelist

# Preserve %{GCCDIST}-gcc%{binsuffix} binary for libgccjit as it is used as a driver
mv %{buildroot}/%{_prefix}/bin/%{GCCDIST}-gcc%{binsuffix} %{buildroot}
rm -f %{buildroot}/%{_prefix}/bin/%{GCCDIST}-*
mv %{buildroot}/%{GCCDIST}-gcc%{binsuffix} %{buildroot}/%{_prefix}/bin/

rm -rf %{buildroot}/%{libsubdir}/install-tools
rm -f %{buildroot}/%{libsubdir}/include-fixed/zutil.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/linux/a.out.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/linux/vt.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/asm-generic/socket.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/bits/mathdef.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/bits/unistd_ext.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/sys/ucontext.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/bits/statx.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/pthread.h
rm -f %{buildroot}/%{libsubdir}/include-fixed/sys/rseq.h
%if !%{enable_plugins}
# no plugins
rm -rf %{buildroot}/%{libsubdir}/plugin
%endif
rm -f  %{buildroot}/%{_infodir}/dir

rm -f %{buildroot}/%{_mandir}/man7/fsf-funding.7
rm -f %{buildroot}/%{_mandir}/man7/gfdl.7
rm -f %{buildroot}/%{_mandir}/man7/gpl.7
rm -f %{buildroot}/%{_libdir}/libiberty.a
%if %{biarch}
%if %{build_primary_64bit}
rm -f %{buildroot}/%{_prefix}/lib/libiberty.a
%else
rm -f %{buildroot}/%{_prefix}/lib64/libiberty.a
%endif
%endif
rm -f %{buildroot}/%{libsubdir}/liblto_plugin.a
rm -f %{buildroot}/%{libsubdir}/liblto_plugin.la
%if %{build_go}
# gccgo.info isn't properly versioned
rm %{buildroot}/%{_infodir}/gccgo.info*
rm -f %{buildroot}/%{libsubdir}/test2json
rm -f %{buildroot}/%{libsubdir}/vet
%endif

# For regular build, some info files do not get renamed properly.
# Do so here.
mv %{buildroot}/%{_infodir}/libgomp.info %{buildroot}/%{_infodir}/libgomp%{binsuffix}.info
%ifarch %itm_arch
mv %{buildroot}/%{_infodir}/libitm.info %{buildroot}/%{_infodir}/libitm%{binsuffix}.info
%endif
%if %{build_fortran}
%ifarch %quadmath_arch
mv %{buildroot}/%{_infodir}/libquadmath.info %{buildroot}/%{_infodir}/libquadmath%{binsuffix}.info
%endif
%endif
%if %{build_ada}
mv %{buildroot}/%{_infodir}/gnat-style.info %{buildroot}/%{_infodir}/gnat-style%{binsuffix}.info
mv %{buildroot}/%{_infodir}/gnat_rm.info %{buildroot}/%{_infodir}/gnat_rm%{binsuffix}.info
mv %{buildroot}/%{_infodir}/gnat_ugn.info %{buildroot}/%{_infodir}/gnat_ugn%{binsuffix}.info
%endif

cd ..
%find_lang cpplib%{binsuffix}
%find_lang gcc%{binsuffix}
%find_lang libstdc++
cat cpplib%{binsuffix}.lang gcc%{binsuffix}.lang > gcc13-locale.lang

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
%if !%{floatn_fixed_glibc}
%dir %{libsubdir}/include-fixed/bits
%endif
%if %{biarch}
%if %{build_primary_64bit}
%dir %{libsubdir}/32
%else
%dir %{libsubdir}/64
%endif
%endif
%{_prefix}/bin/gcc%{binsuffix}
%{_prefix}/bin/%{GCCDIST}-gcc%{binsuffix}
%{_prefix}/bin/gcov%{binsuffix}
%{_prefix}/bin/gcov-dump%{binsuffix}
%{_prefix}/bin/gcov-tool%{binsuffix}
%{_prefix}/bin/gcc-ar%{binsuffix}
%{_prefix}/bin/gcc-nm%{binsuffix}
%{_prefix}/bin/gcc-ranlib%{binsuffix}
%{_prefix}/bin/lto-dump%{binsuffix}
%{libsubdir}/collect2
%{libsubdir}/lto1
%{libsubdir}/lto-wrapper
%{libsubdir}/liblto_plugin.so*
%{libsubdir}/include/limits.h
%{libsubdir}/include/syslimits.h
%if !%{floatn_fixed_glibc}
%{libsubdir}/include-fixed/README
%{libsubdir}/include-fixed/bits/floatn-common.h
%{libsubdir}/include-fixed/bits/floatn.h
%endif
%{libsubdir}/include-fixed/README
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
%{libsubdir}/include/acc_prof.h
%ifarch %sparc
%{libsubdir}/include/visintrin.h
%endif
%ifarch ppc ppc64 ppc64le
%{libsubdir}/include/altivec.h
%{libsubdir}/include/ppc-asm.h
%{libsubdir}/include/ppu_intrinsics.h
%{libsubdir}/include/si2vmx.h
%{libsubdir}/include/spu2vmx.h
%{libsubdir}/include/vec_types.h
%{libsubdir}/include/htmintrin.h
%{libsubdir}/include/htmxlintrin.h
%{libsubdir}/include/amo.h
%{libsubdir}/include/bmi2intrin.h
%{libsubdir}/include/bmiintrin.h
%{libsubdir}/include/emmintrin.h
%{libsubdir}/include/mm_malloc.h
%{libsubdir}/include/mmintrin.h
%{libsubdir}/include/x86intrin.h
%{libsubdir}/include/xmmintrin.h
%{libsubdir}/include/pmmintrin.h
%{libsubdir}/include/tmmintrin.h
%{libsubdir}/include/smmintrin.h
%{libsubdir}/include/rs6000-vecdefines.h
%{libsubdir}/include/immintrin.h
%{libsubdir}/include/nmmintrin.h
%{libsubdir}/include/x86gprintrin.h
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
%{libsubdir}/include/arm_mve.h
%{libsubdir}/include/arm_mve_types.h
%{libsubdir}/include/arm_cde.h
%endif
%ifarch %arm aarch64
%{libsubdir}/include/arm_neon.h
%{libsubdir}/include/arm_acle.h
%{libsubdir}/include/arm_fp16.h
%{libsubdir}/include/arm_bf16.h
%endif
%ifarch aarch64
%{libsubdir}/include/arm_sve.h
%endif
%ifarch riscv64
%{libsubdir}/include/riscv_vector.h
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
%{libsubdir}/include/avx512vbmi2intrin.h
%{libsubdir}/include/avx512vbmi2vlintrin.h
%{libsubdir}/include/avx512vnniintrin.h
%{libsubdir}/include/avx512vnnivlintrin.h
%{libsubdir}/include/avx512bitalgintrin.h
%{libsubdir}/include/avx512vpopcntdqvlintrin.h
%{libsubdir}/include/avx512bf16intrin.h
%{libsubdir}/include/avx512bf16vlintrin.h
%{libsubdir}/include/avx512vp2intersectintrin.h
%{libsubdir}/include/avx512vp2intersectvlintrin.h
%{libsubdir}/include/vpclmulqdqintrin.h
%{libsubdir}/include/enqcmdintrin.h
%{libsubdir}/include/cet.h
%{libsubdir}/include/vaesintrin.h
%{libsubdir}/include/clwbintrin.h
%{libsubdir}/include/clflushoptintrin.h
%{libsubdir}/include/xsavecintrin.h
%{libsubdir}/include/xsavesintrin.h
%{libsubdir}/include/mwaitxintrin.h
%{libsubdir}/include/clzerointrin.h
%{libsubdir}/include/pkuintrin.h
%{libsubdir}/include/sgxintrin.h
%{libsubdir}/include/cetintrin.h
%{libsubdir}/include/gfniintrin.h
%{libsubdir}/include/pconfigintrin.h
%{libsubdir}/include/wbnoinvdintrin.h
%{libsubdir}/include/movdirintrin.h
%{libsubdir}/include/cldemoteintrin.h
%{libsubdir}/include/waitpkgintrin.h
%{libsubdir}/include/serializeintrin.h
%{libsubdir}/include/tsxldtrkintrin.h
%{libsubdir}/include/amxbf16intrin.h
%{libsubdir}/include/amxint8intrin.h
%{libsubdir}/include/amxtileintrin.h
%{libsubdir}/include/x86gprintrin.h
%{libsubdir}/include/hresetintrin.h
%{libsubdir}/include/uintrintrin.h
%{libsubdir}/include/keylockerintrin.h
%{libsubdir}/include/avxvnniintrin.h
%{libsubdir}/include/mwaitintrin.h
%{libsubdir}/include/avx512fp16intrin.h
%{libsubdir}/include/avx512fp16vlintrin.h
%{libsubdir}/include/avxifmaintrin.h
%{libsubdir}/include/avxvnniint8intrin.h
%{libsubdir}/include/avxneconvertintrin.h
%{libsubdir}/include/amxfp16intrin.h
%{libsubdir}/include/cmpccxaddintrin.h
%{libsubdir}/include/prfchiintrin.h
%{libsubdir}/include/raointintrin.h
%endif
%ifarch m68k
%{libsubdir}/include/math-68881.h
%endif
%ifarch %asan_arch
%{libsubdir}/include/sanitizer
%endif
%if %{build_fortran}
%{libsubdir}/include/ISO_Fortran_binding.h
%endif
%versmainlib *crt*.o
%versmainlib libgcc*.a
%versmainlib libgcov.a
%versmainlib libgcc_s*.so
%versmainlib libgomp.so
%versmainlib libgomp.a
%versmainlib libgomp.spec
%if %{build_nvptx}
%versmainlib libgomp-plugin-nvptx.so
%endif
%if %{build_gcn}
%versmainlib libgomp-plugin-gcn.so
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
%ifarch %lsan_arch
%if %build_primary_64bit
%versmainlib liblsan.so
%versmainlib liblsan.a
%versmainlib liblsan_preinit.o
%endif
%endif
%ifarch %ubsan_arch
%versmainlib libubsan.so
%versmainlib libubsan.a
%endif
%ifarch %hwasan_arch
%versmainlib libhwasan.so
%versmainlib libhwasan.a
%endif
%ifarch %asan_arch %ubsan_arch %tsan_arch %lsan_arch %hwasan_arch
%versmainlib libsanitizer.spec
%endif
%ifarch %vtv_arch
%versmainlib libvtv.so
%versmainlib libvtv.a
%endif
%doc %{_mandir}/man1/gcc%{binsuffix}.1.gz
%doc %{_mandir}/man1/gcov%{binsuffix}.1.gz
%doc %{_mandir}/man1/gcov-dump%{binsuffix}.1.gz
%doc %{_mandir}/man1/gcov-tool%{binsuffix}.1.gz
%doc %{_mandir}/man1/lto-dump%{binsuffix}.1.gz

%if %{separate_biarch}
%files -n gcc13%{separate_biarch_suffix}
%defattr(-,root,root)
%versbiarchlib *crt*.o
%versbiarchlib libgcc*.a
%versbiarchlib libgcov.a
%versbiarchlib libgcc_s*.so
%versbiarchlib libgomp.so
%versbiarchlib libgomp.a
%versbiarchlib libgomp.spec
# No 32-bit plugins for nvptx and gcn
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
%versbiarchlib liblsan_preinit.o
%endif
%endif
# libhwasan.{a,so} is not built in 32-bit mode
%ifarch %asan_arch %ubsan_arch %tsan_arch %lsan_arch %hwasan_arch
%versbiarchlib libsanitizer.spec
%endif
%ifarch %vtv_arch
%versbiarchlib libvtv.a
%versbiarchlib libvtv.so
%endif
%endif

%if %{enable_plugins}
%files devel
%defattr(-,root,root)
%dir %{libsubdir}/plugin
%{libsubdir}/plugin
%endif

%files locale -f gcc13-locale.lang

%files -n libstdc++%{libstdcxx_sover}%{libstdcxx_suffix}-locale -f libstdc++.lang

%files PIE
%defattr(-,root,root)
%dir %{libsubdir}
%{libsubdir}/defaults.spec

%if %{build_cp}
%files c++
%defattr(-,root,root)
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{GCCDIST}
%dir %{libsubdir}
%{_prefix}/bin/g++%{binsuffix}
%doc %{_mandir}/man1/g++%{binsuffix}.1.gz
%{libsubdir}/cc1plus
%{libsubdir}/g++-mapper-server

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
%versmainlib libstdc++exp.a
%versmainlib libstdc++.so
%versmainlib libsupc++.a
%{_prefix}/include/c++

%files -n libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix}
%defattr(-,root,root)
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
%versbiarchlib libstdc++exp.a
%versbiarchlib libstdc++.so
%versbiarchlib libsupc++.a

%files -n libstdc++%{libstdcxx_sover}-pp%{libstdcxx_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%dir %{_datadir}/gdb/auto-load/%{mainlibdirbi}
%{_datadir}/gdb/auto-load/%{mainlibdirbi}/libstdc++.so.*-gdb.py
%endif
%endif

%files -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}
%defattr(-,root,root)
%{_slibdir}/libgcc_s.so.%{libgcc_s}
%if %{biarch}
%if %{build_primary_64bit}
%if !%{separate_bi32}
%{slibdir}/libgcc_s.so.%{libgcc_s}
%endif
%else
%if !%{separate_bi64}
%{slibdir64}/libgcc_s.so.%{libgcc_s}
%endif
%endif
%endif

%if %{separate_bi64}
%files -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-64bit
%defattr(-,root,root)
%{slibdir64}/libgcc_s.so.%{libgcc_s}
%endif

%if %{separate_bi32}
%files -n libgcc_s%{libgcc_s}%{libgcc_s_suffix}-32bit
%defattr(-,root,root)
%{slibdir}/libgcc_s.so.%{libgcc_s}
%endif

%files -n libgomp%{libgomp_sover}%{libgomp_suffix}
%defattr(-,root,root)
%mainlib libgomp.so.%{libgomp_sover}*
%if %{build_nvptx}
%mainlib libgomp-plugin-nvptx.so.%{libgomp_sover}*
%endif
%if %{build_gcn}
%mainlib libgomp-plugin-gcn.so.%{libgomp_sover}*
%endif

%if %{separate_biarch}
%files -n libgomp%{libgomp_sover}%{libgomp_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libgomp.so.%{libgomp_sover}*
%endif
# No 32-bit plugins for nvptx and gcn

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

%ifarch %hwasan_arch
%files -n libhwasan%{libhwasan_sover}%{libhwasan_suffix}
%defattr(-,root,root)
%mainlib libhwasan.so.%{libhwasan_sover}*
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
%if %{build_d}
%doc %{_infodir}/gdc%{binsuffix}.info*gz
%endif

%files -n cpp13
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
%{versmainlibdir}/ada_target_properties

%if %{separate_biarch}
%files ada%{separate_biarch_suffix}
%defattr(-,root,root)
%dir %{versmainlibdirbi}/adalib
%{versmainlibdirbi}/adainclude
%{versmainlibdirbi}/adalib/*.ali
%{versmainlibdirbi}/adalib/*.a
%{versmainlibdirbi}/adalib/libgnarl.so
%{versmainlibdirbi}/adalib/libgnat.so
%{versmainlibdirbi}/ada_target_properties
%endif

%files -n libada13
%defattr(-,root,root)
%mainlib libgnarl%{binsuffix}.so
%mainlib libgnat%{binsuffix}.so

%if %{separate_biarch}
%files -n libada13%{separate_biarch_suffix}
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
%versmainlibdir/buildid
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

%if %{build_d}
%files d
%defattr(-,root,root)
%{_prefix}/bin/gdc%{binsuffix}
%{libsubdir}/d21
%versmainlib libgphobos.a
%versmainlib libgphobos.so
%versmainlib libgdruntime.a
%versmainlib libgdruntime.so
%versmainlib libgphobos.spec
%{versmainlibdir}/include/d
%doc %{_mandir}/man1/gdc%{binsuffix}.1.gz

%if %{separate_biarch}
%files d%{separate_biarch_suffix}
%defattr(-,root,root)
%versbiarchlib libgphobos.a
%versbiarchlib libgphobos.so
%versbiarchlib libgdruntime.a
%versbiarchlib libgdruntime.so
%versbiarchlib libgphobos.spec
%endif

%files -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}
%defattr(-,root,root)
%mainlib libgphobos.so.%{libgphobos_sover}*

%if %{separate_biarch}
%files -n libgphobos%{libgphobos_sover}%{libgphobos_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libgphobos.so.%{libgphobos_sover}*
%endif

%files -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}
%defattr(-,root,root)
%mainlib libgdruntime.so.%{libgdruntime_sover}*

%if %{separate_biarch}
%files -n libgdruntime%{libgdruntime_sover}%{libgdruntime_suffix}%{separate_biarch_suffix}
%defattr(-,root,root)
%biarchlib libgdruntime.so.%{libgdruntime_sover}*
%endif
%endif

%if %{build_jit}
%files -n libgccjit%{libgccjit_sover}%{libgccjit_suffix}
%defattr(-,root,root)
%{_prefix}/%{_lib}/libgccjit.so.%{libgccjit_sover}*

%files -n libgccjit%{libgccjit_sover}-devel%{libdevel_suffix}
%defattr(-,root,root)
%doc gcc/jit/docs/examples
%{_prefix}/%{_lib}/libgccjit.so
%{_prefix}/include/libgccjit.h
%{_prefix}/include/libgccjit++.h
%{_infodir}/libgccjit.info.gz
%endif

%if 0%{?run_tests:1}
%files -n gcc13-testresults
%defattr(-,root,root)
%doc testresults/test_summary.txt
%doc testresults/*.sum
%doc testresults/*.log
%endif

%changelog
