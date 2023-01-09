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


%define pkgname cross-aarch64-gcc11
%define cross_arch aarch64
%define gcc_target_arch aarch64-suse-linux
%define gcc_target_glibc 1
# nospeccleaner

# In the staging/ring projects, we don't want to build the unneeded
#  cross-* packages, but by default, we do:
%bcond_with ringdisabled

%if "%{cross_arch}" != "arm-none" && "%{cross_arch}" != "arm" && "%{cross_arch}" != "aarch64" && "%{cross_arch}" != "riscv64" && %{with ringdisabled}
ExclusiveArch:  do-not-build
%endif

%define build_cp 0%{!?gcc_accel:1}
%if 0%{?gcc_libc_bootstrap:1}
%define build_cp 0
%endif
%define build_ada 0
%define build_libjava 0
%define build_java 0

%define build_fortran 0%{?gcc_accel:1}
%define build_objc 0
%define build_objcp 0
%define build_go 0
%define build_nvptx 0
%define build_gcn 0
%define build_d 0

%define enable_plugins 0
%define build_jit 0
%define use_lto_bootstrap 0

%define binutils_target %{cross_arch}
%if "%{cross_arch}" == "armv7l" || "%{cross_arch}" == "armv7hl"
%define binutils_target arm
%endif
%if "%{cross_arch}" == "armv6l" || "%{cross_arch}" == "armv6hl"
%define binutils_target arm
%endif
%if "%{cross_arch}" == "armv5tel"
%define binutils_target arm
%endif
%if "%{cross_arch}" == "arm-none"
%define binutils_target arm
%endif
%if "%{cross_arch}" == "riscv64-elf"
%define binutils_target riscv64
%endif
%if "%{cross_arch}" == "sparcv9"
%define binutils_target sparc
%endif
%define canonical_target %(echo %{binutils_target} | sed -e "s/i.86/i586/;s/ppc/powerpc/;s/sparc64.*/sparc64/;s/sparcv.*/sparc/;")
%if "%{binutils_target}" == "avr" || "%{binutils_target}" == "spu"
%define binutils_os %{canonical_target}
%else
%if "%{binutils_target}" == "epiphany" || "%{binutils_target}" == "nds32le" || "%{binutils_target}" == "rl78" || "%{binutils_target}" == "rx"
%define binutils_os %{canonical_target}-elf
%else
%if "%{binutils_target}" == "arm"
%define binutils_os %{canonical_target}-suse-linux-gnueabi
%else
%if 0%{?gcc_accel:1}
%define binutils_os %{gcc_target_arch}
%else
%define binutils_os %{canonical_target}-suse-linux
%endif
%endif
%endif
%endif

%if 0%{?gcc_icecream:1}
%define sysroot %{_prefix}/%{gcc_target_arch}
%else
# offloading builds newlib in-tree and can install in
# the GCC private path without extra sysroot
%if 0%{!?gcc_accel:1}
# use same sysroot as in binutils.spec
%define sysroot %{_prefix}/%{binutils_os}/sys-root
%endif
%endif

%if %{suse_version} >= 1220
%define selfconflict() %1
%else
%define selfconflict() otherproviders(%1)
%endif

Name:           %{pkgname}
%define biarch_targets x86_64 s390x powerpc64 powerpc sparc sparc64

URL:            https://gcc.gnu.org/
Version:        11.3.1+git2076
Release:        0
%define gcc_dir_version %(echo %version |  sed 's/+.*//' | cut -d '.' -f 1)
%define gcc_snapshot_revision %(echo %version | sed 's/[3-9]\.[0-9]\.[0-6]//' | sed 's/+/-/')
%define binsuffix -11
%if %{suse_version} < 1310
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%endif
Group:          Development/Languages/C and C++
Source:         gcc-%{version}.tar.xz
Source1:        change_spec
Source2:        gcc11-rpmlintrc
Source3:        gcc11-testresults-rpmlintrc
Source4:        README.First-for.SuSE.packagers
Source5:        newlib-4.1.0.tar.xz
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
Patch52:        gcc10-foffload-default.patch
# Some patches taken from Debian
Patch60:        gcc44-textdomain.patch
Patch61:        gcc44-rename-info-files.patch
# Patches for embedded newlib
Patch100:       newlib-4.1.0-aligned_alloc.patch

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

%if "%{cross_arch}" != "nvptx"
%if "%{cross_arch}" != "amdgcn"
BuildRequires:  cross-%{binutils_target}-binutils
Requires:       cross-%{binutils_target}-binutils
%endif
%endif
%define hostsuffix %{nil}
%if 0%{suse_version} < 1220
%define hostsuffix -4.8
BuildRequires:  gcc48-c++
%else
BuildRequires:  gcc-c++
%endif
%if %{suse_version} > 1500
BuildRequires:  libzstd-devel
%endif
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gettext-devel
BuildRequires:  glibc-devel-32bit
BuildRequires:  mpc-devel
BuildRequires:  mpfr-devel
BuildRequires:  perl
%if %{suse_version} > 1220
BuildRequires:  makeinfo
%else
BuildRequires:  texinfo
%endif
BuildRequires:  zlib-devel
%if %{suse_version} >= 1230
BuildRequires:  isl-devel
%endif
%ifarch ia64
BuildRequires:  libunwind-devel
%endif
%if 0%{!?gcc_icecream:1}
%if 0%{!?gcc_libc_bootstrap:1}
%if 0%{?gcc_target_newlib:1}
BuildRequires:  cross-%cross_arch-newlib-devel
%endif
%if "%{cross_arch}" == "avr"
BuildRequires:  avr-libc
%endif
%if 0%{?gcc_target_glibc:1}
BuildRequires:  cross-%cross_arch-glibc-devel
Requires:       cross-%cross_arch-glibc-devel
%endif
%endif
%if "%{cross_arch}" == "nvptx"
BuildRequires:  nvptx-tools
Requires:       cross-nvptx-newlib-devel >= %{version}-%{release}
Requires:       nvptx-tools
ExclusiveArch:  x86_64
%define nvptx_newlib 1
%endif
%if "%{cross_arch}" == "amdgcn"
# amdgcn uses the llvm assembler and linker, llvm-mc-12 doesn't
# work at the moment so require llvm11
BuildRequires:  llvm11
BuildRequires:  lld
Requires:       cross-amdgcn-newlib-devel >= %{version}-%{release}
Requires:       lld
Requires:       llvm11
# SLE12 does not fulfil build requirements for GCN, SLE15 SP1 does
# technically also SLE12 SP5 but do not bother there
%if %{suse_version} >= 1550 || 0%{?sle_version:%sle_version} >= 150100
ExclusiveArch:  x86_64
%else
ExclusiveArch:  do-not-build
%endif
%define amdgcn_newlib 1
%endif
%endif
%if 0%{?gcc_icecream:1}%{?gcc_target_glibc:1}%{?gcc_libc_bootstrap:1}
ExclusiveArch:  i586 ppc64le ppc64 x86_64 s390x  riscv64
%endif
%define _binary_payload w.ufdio
# Obsolete cross-ppc-gcc49 from cross-ppc64-gcc49 which has
# file conflicts with it and is no longer packaged
%if "%pkgname" == "cross-ppc64-gcc49"
Obsoletes:      cross-ppc-gcc49 <= 4.9.0+r209354
%endif
%if 0%{?gcc_target_newlib:1}%{?gcc_target_glibc:1}
# Generally only one cross for the same target triplet can be installed
# at the same time as we are populating a non-version-specific sysroot
Provides:       %{gcc_target_arch}-gcc
Conflicts:      %selfconflict %{gcc_target_arch}-gcc
%endif
%if 0%{?gcc_libc_bootstrap:1}
# The -bootstrap packages file-conflict with the non-bootstrap variants.
# Even if we don't actually (want to) distribute the bootstrap variants
# the following avoids repo-checker spamming us endlessly.
Conflicts:      cross-%{cross_arch}-gcc11
%endif
#!BuildIgnore: gcc-PIE
%if 0%{build_cp:1}
# The cross compiler only packages the arch specific c++ headers, so
# we need to depend on the host libstdc++ devel headers (we wouldn't need
# the libs, though)
Requires:       libstdc++6-devel-gcc11
%endif
AutoReqProv:    off
BuildRequires:  update-alternatives
Requires(post): update-alternatives
Requires(preun):update-alternatives
Summary:        The GNU Compiler Collection targeting %{cross_arch}
License:        GPL-3.0-or-later

%description
The GNU Compiler Collection as a cross-compiler targeting %{cross_arch}.
%if 0%{?gcc_icecream:1}
Note this is only useful for building freestanding things like the
kernel since it fails to include target libraries and headers.
%endif
%if 0%{?gcc_libc_bootstrap:1}
This is a package that is necessary for bootstrapping another package
only, it is not intended for any other use.
%endif

%prep
%if 0%{?nvptx_newlib:1}%{?amdgcn_newlib:1}
%setup -q -n gcc-%{version} -a 5
ln -s newlib-4.1.0/newlib .
cd newlib
%patch100 -p1
cd ..
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
%if "%{TARGET_ARCH}" == "amdgcn"
%patch18 -p1
%endif
# In SLE15 and earlier default to dwarf4, not dwarf5
%if %{suse_version} < 1550
%patch19 -p1
%endif
%patch20 -p1
%patch51
%patch52 -p1
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

%if 0%{!?gcc_icecream:1}
make %{?_smp_mflags}
%else
make %{?_smp_mflags} all-host
%endif

%if 0%{?gcc_icecream:%gcc_icecream}
%package -n cross-%cross_arch-gcc11-icecream-backend
Summary:        Icecream backend for the GNU C Compiler
Group:          Development/Languages/C and C++

%description -n cross-%cross_arch-gcc11-icecream-backend
This package contains the icecream environment for the GNU C Compiler
%endif

%if 0%{?nvptx_newlib:1}
%package -n cross-nvptx-newlib11-devel
Summary:        Newlib for the nvptx offload target
Group:          Development/Languages/C and C++
Provides:       cross-nvptx-newlib-devel = %{version}-%{release}
Conflicts:      cross-nvptx-newlib-devel

%description -n cross-nvptx-newlib11-devel
Newlib development files for the nvptx offload target compiler.
%endif

%if 0%{?amdgcn_newlib:1}
%package -n cross-amdgcn-newlib11-devel
Summary:        Newlib for the amdgcn offload target
Group:          Development/Languages/C and C++
Provides:       cross-amdgcn-newlib-devel = %{version}-%{release}
Conflicts:      cross-amdgcn-newlib-devel

%description -n cross-amdgcn-newlib11-devel
Newlib development files for the amdgcn offload target compiler.
%endif

%define targetlibsubdir %{_libdir}/gcc/%{gcc_target_arch}/%{gcc_dir_version}

%install
cd obj-%{GCCDIST}

%if "%{TARGET_ARCH}" == "amdgcn"
# libtool needs to be able to call ranlib
export PATH="`pwd`/target-tools/bin:$PATH"
%endif

# install and fixup host parts
make DESTDIR=$RPM_BUILD_ROOT install-host
rm -rf $RPM_BUILD_ROOT/%{targetlibsubdir}/install-tools
rm -f $RPM_BUILD_ROOT/%{targetlibsubdir}/liblto_plugin.la
# common fixup
rm -f $RPM_BUILD_ROOT%{_libdir}/libiberty.a

# install and fixup target parts
%if 0%{?gcc_icecream:1}
# so expect the sysroot to be populated from natively built binaries
%else
# We want shared libraries to reside in the sysroot but the .so symlinks
# on the host.  Once we have a cross target that has shared libs we need
# to manually fix up things here like we do for non-cross compilers
mkdir -p $RPM_BUILD_ROOT/%{?sysroot:%sysroot}
make DESTDIR=$RPM_BUILD_ROOT install-target
%if %{build_cp}
# So we installed libstdc++ headers into %prefix where they conflict
# with other host compilers.  Rip out the non-target specific parts
# again.  Note not all cross targets support libstdc++, so create the
# directory to make things easier.
mkdir -p $RPM_BUILD_ROOT/%_prefix/include/c++/%{gcc_dir_version}
find $RPM_BUILD_ROOT/%_prefix/include/c++/%{gcc_dir_version} -mindepth 1 -maxdepth 1 -type d -a -not -name %{gcc_target_arch} | xargs -r rm -r
find $RPM_BUILD_ROOT/%_prefix/include/c++/%{gcc_dir_version} -maxdepth 1 -type f | xargs -r rm
# And also remove installed pretty printers which conflict in similar ways
rm -rf $RPM_BUILD_ROOT/%{_datadir}/gcc%{binsuffix}
%endif
%endif

%if 0%{?binutils_os:1}
for prog in as ld; do
  ln -s /usr/%{binutils_os}/bin/$prog $RPM_BUILD_ROOT%{targetlibsubdir}/
done
%endif

# remove docs
rm -rf $RPM_BUILD_ROOT%{_mandir}
rm -rf $RPM_BUILD_ROOT%{_infodir}

# for accelerators remove all frontends but lto1 and also install-tools
%if 0%{?gcc_accel:1}
rm -f $RPM_BUILD_ROOT%{libsubdir}/accel/%{gcc_target_arch}/cc1
rm -f $RPM_BUILD_ROOT%{libsubdir}/accel/%{gcc_target_arch}/cc1plus
rm -rf $RPM_BUILD_ROOT%{libsubdir}/accel/%{gcc_target_arch}/install-tools
rm -rf $RPM_BUILD_ROOT%{targetlibsubdir}/install-tools
# also move things from target directories into the accel path since
# that is the place where we later search for (only)
( cd $RPM_BUILD_ROOT%{targetlibsubdir} && tar cf - . ) | ( cd $RPM_BUILD_ROOT%{libsubdir}/accel/%{gcc_target_arch} && tar xf - )
rm -rf $RPM_BUILD_ROOT%{targetlibsubdir}
%endif
# for amdgcn install the symlinks to the llvm tools
# follow alternatives symlinks to the hardcoded version requirement
%if "%{TARGET_ARCH}" == "amdgcn"
mkdir -p $RPM_BUILD_ROOT%{_prefix}/amdgcn-amdhsa/bin
ln -s `readlink -f /usr/bin/llvm-ar` $RPM_BUILD_ROOT%{_prefix}/amdgcn-amdhsa/bin/ar
ln -s `readlink -f /usr/bin/llvm-mc` $RPM_BUILD_ROOT%{_prefix}/amdgcn-amdhsa/bin/as
ln -s /usr/bin/lld $RPM_BUILD_ROOT%{_prefix}/amdgcn-amdhsa/bin/ld
ln -s `readlink -f /usr/bin/llvm-nm` $RPM_BUILD_ROOT%{_prefix}/amdgcn-amdhsa/bin/nm
ln -s `readlink -f /usr/bin/llvm-ranlib` $RPM_BUILD_ROOT%{_prefix}/amdgcn-amdhsa/bin/ranlib
ln -s %{_prefix}/amdgcn-amdhsa/bin/ar $RPM_BUILD_ROOT%{_prefix}/bin/amdgcn-amdhsa-ar
ln -s %{_prefix}/amdgcn-amdhsa/bin/as $RPM_BUILD_ROOT%{_prefix}/bin/amdgcn-amdhsa-as
ln -s %{_prefix}/amdgcn-amdhsa/bin/ld $RPM_BUILD_ROOT%{_prefix}/bin/amdgcn-amdhsa-ld
ln -s %{_prefix}/amdgcn-amdhsa/bin/nm $RPM_BUILD_ROOT%{_prefix}/bin/amdgcn-amdhsa-nm
ln -s %{_prefix}/amdgcn-amdhsa/bin/ranlib $RPM_BUILD_ROOT%{_prefix}/bin/amdgcn-amdhsa-ranlib
%endif

%if 0%{?gcc_icecream:%gcc_icecream}
# Build an icecream environment
# The assembler comes from the cross-binutils, and hence is _not_
# named funnily, not even on ppc, so there we need the original target
install -s -D %{_prefix}/bin/%{binutils_os}-as \
	$RPM_BUILD_ROOT/env/usr/bin/as
install -s $RPM_BUILD_ROOT/%{_prefix}/bin/%{gcc_target_arch}-g++%{binsuffix} \
	$RPM_BUILD_ROOT/env/usr/bin/g++
install -s $RPM_BUILD_ROOT/%{_prefix}/bin/%{gcc_target_arch}-gcc%{binsuffix} \
	$RPM_BUILD_ROOT/env/usr/bin/gcc

for back in cc1 cc1plus; do
	install -s -D $RPM_BUILD_ROOT/%{targetlibsubdir}/$back \
		$RPM_BUILD_ROOT/env%{targetlibsubdir}/$back
done
if test -f $RPM_BUILD_ROOT/%{targetlibsubdir}/liblto_plugin.so; then
  install -s -D $RPM_BUILD_ROOT/%{targetlibsubdir}/liblto_plugin.so \
		$RPM_BUILD_ROOT/env%{targetlibsubdir}/liblto_plugin.so
fi

# Make sure to also pull in all shared library requirements for the
# binaries we put into the environment which is operated by chrooting
# into it and execing the compiler
libs=`for bin in $RPM_BUILD_ROOT/env/usr/bin/* $RPM_BUILD_ROOT/env%{targetlibsubdir}/*; do \
  ldd $bin | sed -n '\,^[^/]*\(/[^ ]*\).*,{ s//\1/; p; }'  ;\
done | sort -u `
for lib in $libs; do
  # Check wether the same library also exists in the parent directory,
  # and prefer that on the assumption that it is a more generic one.
  baselib=`echo "$lib" | sed 's,/[^/]*\(/[^/]*\)$,\1,'`
  test -f "$baselib" && lib=$baselib
  install -s -D $lib $RPM_BUILD_ROOT/env$lib
done

cd $RPM_BUILD_ROOT/env
tar --no-recursion --mtime @${SOURCE_DATE_EPOCH:-$(date +%s)} --format=gnu -cv `find *|LC_ALL=C sort` |\
  gzip -n9 > ../%{name}_%{_arch}.tar.gz
cd ..
mkdir -p usr/share/icecream-envs
mv %{name}_%{_arch}.tar.gz usr/share/icecream-envs
rpm -q --changelog glibc >  usr/share/icecream-envs/%{name}_%{_arch}.glibc
rpm -q --changelog binutils >  usr/share/icecream-envs/%{name}_%{_arch}.binutils
rm -r env
%endif

# we provide update-alternatives for selecting a compiler version for
# crosses
%if 0%{!?gcc_accel:1}
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
for ex in gcc cpp \
%if %{build_cp}
          c++ g++ \
%endif
          gcc-ar gcc-nm gcc-ranlib lto-dump \
%if 0%{!?gcc_libc_bootstrap:1}
          gcov gcov-dump gcov-tool \
%endif
	  ; do
  ln -s %{_sysconfdir}/alternatives/%{gcc_target_arch}-$ex \
	%{buildroot}%{_bindir}/%{gcc_target_arch}-$ex
done

%post
%{_sbindir}/update-alternatives \
  --install %{_bindir}/%{gcc_target_arch}-gcc %{gcc_target_arch}-gcc %{_bindir}/%{gcc_target_arch}-gcc%{binsuffix} 11 \
  --slave %{_bindir}/%{gcc_target_arch}-cpp %{gcc_target_arch}-cpp %{_bindir}/%{gcc_target_arch}-cpp%{binsuffix} \
%if %{build_cp}
  --slave %{_bindir}/%{gcc_target_arch}-c++ %{gcc_target_arch}-c++ %{_bindir}/%{gcc_target_arch}-c++%{binsuffix} \
  --slave %{_bindir}/%{gcc_target_arch}-g++ %{gcc_target_arch}-g++ %{_bindir}/%{gcc_target_arch}-g++%{binsuffix} \
%endif
  --slave %{_bindir}/%{gcc_target_arch}-gcc-ar %{gcc_target_arch}-gcc-ar %{_bindir}/%{gcc_target_arch}-gcc-ar%{binsuffix} \
  --slave %{_bindir}/%{gcc_target_arch}-gcc-nm %{gcc_target_arch}-gcc-nm %{_bindir}/%{gcc_target_arch}-gcc-nm%{binsuffix} \
  --slave %{_bindir}/%{gcc_target_arch}-lto-dump %{gcc_target_arch}-lto-dump %{_bindir}/%{gcc_target_arch}-lto-dump%{binsuffix} \
  --slave %{_bindir}/%{gcc_target_arch}-gcc-ranlib %{gcc_target_arch}-gcc-ranlib %{_bindir}/%{gcc_target_arch}-gcc-ranlib%{binsuffix} \
%if 0%{!?gcc_libc_bootstrap:1}
  --slave %{_bindir}/%{gcc_target_arch}-gcov %{gcc_target_arch}-gcov %{_bindir}/%{gcc_target_arch}-gcov%{binsuffix} \
  --slave %{_bindir}/%{gcc_target_arch}-gcov-dump %{gcc_target_arch}-gcov-dump %{_bindir}/%{gcc_target_arch}-gcov-dump%{binsuffix} \
  --slave %{_bindir}/%{gcc_target_arch}-gcov-tool %{gcc_target_arch}-gcov-tool %{_bindir}/%{gcc_target_arch}-gcov-tool%{binsuffix} \
%endif

%postun
if [ ! -f %{_bindir}/%{gcc_target_arch}-gcc ] ; then
  %{_sbindir}/update-alternatives --remove %{gcc_target_arch}-gcc %{_bindir}/%{gcc_target_arch}-gcc%{binsuffix}
fi
%endif

%files
%defattr(-,root,root)
%if 0%{?gcc_accel:1}
%{_prefix}/bin/%{GCCDIST}-accel-%{gcc_target_arch}-*
%dir %{libsubdir}
%dir %{libsubdir}/accel
%{libsubdir}/accel/%{gcc_target_arch}
%else
%{_prefix}/bin/%{gcc_target_arch}-gcc%{binsuffix}
%{_prefix}/bin/%{gcc_target_arch}-cpp%{binsuffix}
%{_prefix}/bin/%{gcc_target_arch}-gcc-ar%{binsuffix}
%{_prefix}/bin/%{gcc_target_arch}-gcc-nm%{binsuffix}
%{_prefix}/bin/%{gcc_target_arch}-gcc-ranlib%{binsuffix}
%{_prefix}/bin/%{gcc_target_arch}-lto-dump%{binsuffix}
%if 0%{!?gcc_libc_bootstrap:1}
%{_prefix}/bin/%{gcc_target_arch}-gcov%{binsuffix}
%{_prefix}/bin/%{gcc_target_arch}-gcov-dump%{binsuffix}
%{_prefix}/bin/%{gcc_target_arch}-gcov-tool%{binsuffix}
%{_prefix}/bin/%{gcc_target_arch}-gcov
%{_prefix}/bin/%{gcc_target_arch}-gcov-dump
%{_prefix}/bin/%{gcc_target_arch}-gcov-tool
%endif
%{_prefix}/bin/%{gcc_target_arch}-gcc
%{_prefix}/bin/%{gcc_target_arch}-cpp
%{_prefix}/bin/%{gcc_target_arch}-gcc-ar
%{_prefix}/bin/%{gcc_target_arch}-gcc-nm
%{_prefix}/bin/%{gcc_target_arch}-gcc-ranlib
%{_prefix}/bin/%{gcc_target_arch}-lto-dump
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-gcc
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-cpp
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-gcc-ar
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-gcc-nm
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-gcc-ranlib
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-lto-dump
%if 0%{!?gcc_libc_bootstrap:1}
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-gcov
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-gcov-dump
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-gcov-tool
%endif
%if %{build_cp}
%{_prefix}/bin/%{gcc_target_arch}-c++%{binsuffix}
%{_prefix}/bin/%{gcc_target_arch}-g++%{binsuffix}
%{_prefix}/bin/%{gcc_target_arch}-c++
%{_prefix}/bin/%{gcc_target_arch}-g++
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-c++
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-g++
%if 0%{!?gcc_libc_bootstrap:1}
%if "%{cross_arch}" == "avr" || 0%{?gcc_target_newlib:1} || 0%{?gcc_target_glibc:1}
%{_prefix}/include/c++
%endif
%endif
%endif
%dir %{targetlibsubdir}
%dir %{_libdir}/gcc/%{gcc_target_arch}
%{targetlibsubdir}
%endif
%if 0%{!?gcc_icecream:1} && 0%{!?gcc_libc_bootstrap:1} && 0%{?sysroot:1}
%{sysroot}
%endif

%if 0%{?gcc_icecream:%gcc_icecream}
%files -n cross-%cross_arch-gcc11-icecream-backend
%defattr(-,root,root)
/usr/share/icecream-envs
%endif

%if 0%{?nvptx_newlib:1}
%files -n cross-nvptx-newlib11-devel
%defattr(-,root,root)
%{_prefix}/%{gcc_target_arch}
%endif

%if 0%{?amdgcn_newlib:1}
%files -n cross-amdgcn-newlib11-devel
%defattr(-,root,root)
%{_prefix}/%{gcc_target_arch}
%{_prefix}/bin/amdgcn-amdhsa-ar
%{_prefix}/bin/amdgcn-amdhsa-as
%{_prefix}/bin/amdgcn-amdhsa-ld
%{_prefix}/bin/amdgcn-amdhsa-nm
%{_prefix}/bin/amdgcn-amdhsa-ranlib
%endif

%changelog
