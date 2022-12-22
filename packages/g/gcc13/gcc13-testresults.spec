#
# spec file for package gcc13-testresults
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


%define building_testsuite 1
%define run_tests 1
#
# spec file for package gcc${version}
#
# Copyright (c) 2021 SUSE LLC
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

# nospeccleaner

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

Name:           gcc13-testresults
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

Summary:        Testsuite results
License:        SUSE-Public-Domain
Group:          Development/Languages/C and C++

%description
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
%if 0%{?run_tests:1}
cp `find . -name "*.sum"` ../testresults/
cp `find . -name "*.log"  \! -name "config.log" | grep -v 'acats.\?/tests' | grep -v libbacktrace` ../testresults/
chmod 644 ../testresults/*
%endif

%if 0%{?run_tests:1}
%files
%defattr(-,root,root)
%doc testresults/test_summary.txt
%doc testresults/*.sum
%doc testresults/*.log
%endif

%changelog
