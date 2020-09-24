#
# spec file for package cross-arm-none-gcc7-bootstrap
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


%define pkgname cross-arm-none-gcc7-bootstrap
%define cross_arch arm-none
%define gcc_target_arch arm-none-eabi
%define gcc_target_newlib 1
%define gcc_libc_bootstrap 1
#
# spec file for package gcc (Version 4.0.1)
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://www.suse.de/feedback/
#

# nospeccleaner

%define build_cp 0%{!?gcc_accel:1}
%define build_ada 0
%define build_libjava 0
%define build_java 0

%define build_fortran 0
%define build_objc 0
%define build_objcp 0
%define build_go 0
%define build_hsa 0
%define build_nvptx 0

%define enable_plugins 0

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
%define build_cp 0
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
Version:        7.5.0+r278197
Release:        0
%define gcc_dir_version %(echo %version | sed 's/+.*//' | cut -d '.' -f 1)
%define gcc_snapshot_revision %(echo %version | sed 's/[3-9]\.[0-9]\.[0-6]//' | sed 's/+/-/')
%define binsuffix -7
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
# A set of patches from the RH srpm
Patch51:        gcc41-ppc32-retaddr.patch
# Some patches taken from Debian
Patch60:        gcc44-textdomain.patch
Patch61:        gcc44-rename-info-files.patch

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
BuildRequires:  cross-%{binutils_target}-binutils
Requires:       cross-%{binutils_target}-binutils
%endif
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
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
%ifarch %ix86 x86_64 ppc ppc64 s390 s390x ia64 %sparc hppa %arm
BuildRequires:  isl-devel
%endif
%ifarch ia64
BuildRequires:  libunwind-devel
%endif
%if 0%{!?gcc_icecream:1}
%if 0%{?gcc_target_newlib:1} && 0%{!?gcc_libc_bootstrap:1}
BuildRequires:  cross-%cross_arch-newlib-devel
%endif
%if 0%{!?gcc_libc_bootstrap:1} && "%{cross_arch}" == "avr"
BuildRequires:  avr-libc
%endif
%if 0%{?gcc_target_glibc:1}
BuildRequires:  cross-%cross_arch-glibc-devel
%endif
%if "%{cross_arch}" == "nvptx"
BuildRequires:  nvptx-tools
Requires:       cross-nvptx-newlib-devel >= %{version}-%{release}
Requires:       nvptx-tools
ExclusiveArch:  x86_64
%define nvptx_newlib 1
%endif
%endif
%if 0%{?gcc_icecream:1}
ExclusiveArch:  ppc64le ppc64 x86_64 s390x aarch64
%endif
%define _binary_payload w.ufdio
# Obsolete cross-ppc-gcc49 from cross-ppc64-gcc49 which has
# file conflicts with it and is no longer packaged
%if "%pkgname" == "cross-ppc64-gcc49"
Obsoletes:      cross-ppc-gcc49 <= 4.9.0+r209354
%endif
%if 0%{?gcc_target_newlib:1}
# Generally only one cross for the same target triplet can be installed
# at the same time as we are populating a non-version-specific sysroot
Provides:       %{gcc_target_arch}-gcc
Conflicts:      %selfconflict %{gcc_target_arch}-gcc
%endif
%if 0%{?gcc_libc_bootstrap:1}
# The -bootstrap packages file-conflict with the non-bootstrap variants.
# Even if we don't actually (want to) distribute the bootstrap variants
# the following avoids repo-checker spamming us endlessly.
Conflicts:      cross-%{cross_arch}-gcc7
%endif
#!BuildIgnore: gcc-PIE
BuildRequires:  update-alternatives
Requires(post): update-alternatives
Requires(preun): update-alternatives
Summary:        The GNU Compiler Collection targeting %{cross_arch}
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++

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
%if 0%{?nvptx_newlib:1}
%setup -q -n gcc-%{version} -a 5
ln -s nvptx-newlib/newlib .
%else
%setup -q -n gcc-%{version}
%endif

#test patching start

%patch2
%patch5
%patch6
%patch7
%if %{suse_version} < 1310
%patch9
%endif
%patch10
%patch11
%patch12
%patch14
%patch15
%patch17 -p1
%patch18
%patch19
%patch20
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch51
%patch60
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
nvptx-none=%{_prefix}/nvptx-none, \
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
	--build=%{GCCDIST} \
	--host=%{GCCDIST}

%if 0%{!?gcc_icecream:1} && 0%{!?gcc_libc_bootstrap:1}
make %{?_smp_mflags}
%else
make %{?_smp_mflags} all-host
%endif

%if 0%{?gcc_icecream:%gcc_icecream}
%package -n cross-%cross_arch-gcc7-icecream-backend
Summary:        Icecream backend for the GNU C Compiler
Group:          Development/Languages/C and C++

%description -n cross-%cross_arch-gcc7-icecream-backend
This package contains the icecream environment for the GNU C Compiler
%endif

%if 0%{?nvptx_newlib:1}
%package -n cross-nvptx-newlib7-devel
Summary:        newlib for the nvptx offload target
Group:          Development/Languages/C and C++
Provides:       cross-nvptx-newlib-devel = %{version}-%{release}
Conflicts:      cross-nvptx-newlib-devel

%description -n cross-nvptx-newlib7-devel
Newlib development files for the nvptx offload target compiler.
%endif

%define targetlibsubdir %{_libdir}/gcc/%{gcc_target_arch}/%{gcc_dir_version}

%install
cd obj-%{GCCDIST}

# install and fixup host parts
make DESTDIR=$RPM_BUILD_ROOT install-host
rm -rf $RPM_BUILD_ROOT/%{targetlibsubdir}/install-tools
rm -f $RPM_BUILD_ROOT/%{targetlibsubdir}/liblto_plugin.la
# common fixup
rm -f $RPM_BUILD_ROOT%{_libdir}/libiberty.a

# install and fixup target parts
# debugedit is not prepared for this and crashes
%if 0%{?gcc_icecream:1}
# so expect the sysroot to be populated from natively built binaries
%else
%if 0%{!?gcc_libc_bootstrap:1}
export NO_BRP_STRIP_DEBUG=true
export NO_DEBUGINFO_STRIP_DEBUG=true
%define __debug_install_post %{nil}
: >../debugfiles.list
: >../debugsourcefiles.list
: >../debugsources.list
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
          gcc-ar gcc-nm gcc-ranlib gcov gcov-dump gcov-tool; do
  ln -s %{_sysconfdir}/alternatives/%{gcc_target_arch}-$ex \
	%{buildroot}%{_bindir}/%{gcc_target_arch}-$ex
done

%post
%{_sbindir}/update-alternatives \
  --install %{_bindir}/%{gcc_target_arch}-gcc %{gcc_target_arch}-gcc %{_bindir}/%{gcc_target_arch}-gcc%{binsuffix} 7 \
  --slave %{_bindir}/%{gcc_target_arch}-cpp %{gcc_target_arch}-cpp %{_bindir}/%{gcc_target_arch}-cpp%{binsuffix} \
%if %{build_cp}
  --slave %{_bindir}/%{gcc_target_arch}-c++ %{gcc_target_arch}-c++ %{_bindir}/%{gcc_target_arch}-c++%{binsuffix} \
  --slave %{_bindir}/%{gcc_target_arch}-g++ %{gcc_target_arch}-g++ %{_bindir}/%{gcc_target_arch}-g++%{binsuffix} \
%endif
  --slave %{_bindir}/%{gcc_target_arch}-gcc-ar %{gcc_target_arch}-gcc-ar %{_bindir}/%{gcc_target_arch}-gcc-ar%{binsuffix} \
  --slave %{_bindir}/%{gcc_target_arch}-gcc-nm %{gcc_target_arch}-gcc-nm %{_bindir}/%{gcc_target_arch}-gcc-nm%{binsuffix} \
  --slave %{_bindir}/%{gcc_target_arch}-gcc-ranlib %{gcc_target_arch}-gcc-ranlib %{_bindir}/%{gcc_target_arch}-gcc-ranlib%{binsuffix} \
  --slave %{_bindir}/%{gcc_target_arch}-gcov %{gcc_target_arch}-gcov %{_bindir}/%{gcc_target_arch}-gcov%{binsuffix} \
  --slave %{_bindir}/%{gcc_target_arch}-gcov-dump %{gcc_target_arch}-gcov-dump %{_bindir}/%{gcc_target_arch}-gcov-dump%{binsuffix} \
  --slave %{_bindir}/%{gcc_target_arch}-gcov-tool %{gcc_target_arch}-gcov-tool %{_bindir}/%{gcc_target_arch}-gcov-tool%{binsuffix}

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
%{_prefix}/bin/%{gcc_target_arch}-gcov%{binsuffix}
%{_prefix}/bin/%{gcc_target_arch}-gcov-dump%{binsuffix}
%{_prefix}/bin/%{gcc_target_arch}-gcov-tool%{binsuffix}
%{_prefix}/bin/%{gcc_target_arch}-gcc
%{_prefix}/bin/%{gcc_target_arch}-cpp
%{_prefix}/bin/%{gcc_target_arch}-gcc-ar
%{_prefix}/bin/%{gcc_target_arch}-gcc-nm
%{_prefix}/bin/%{gcc_target_arch}-gcc-ranlib
%{_prefix}/bin/%{gcc_target_arch}-gcov
%{_prefix}/bin/%{gcc_target_arch}-gcov-dump
%{_prefix}/bin/%{gcc_target_arch}-gcov-tool
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-gcc
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-cpp
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-gcc-ar
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-gcc-nm
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-gcc-ranlib
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-gcov
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-gcov-dump
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-gcov-tool
%if %{build_cp}
%{_prefix}/bin/%{gcc_target_arch}-c++%{binsuffix}
%{_prefix}/bin/%{gcc_target_arch}-g++%{binsuffix}
%{_prefix}/bin/%{gcc_target_arch}-c++
%{_prefix}/bin/%{gcc_target_arch}-g++
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-c++
%ghost %{_sysconfdir}/alternatives/%{gcc_target_arch}-g++
%if 0%{!?gcc_libc_bootstrap:1}
%if %{cross_arch} == "avr" || 0%{?gcc_target_newlib:1} || 0%{?gcc_target_glibc:1}
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
%files -n cross-%cross_arch-gcc7-icecream-backend
%defattr(-,root,root)
/usr/share/icecream-envs
%endif

%if 0%{?nvptx_newlib:1}
%files -n cross-nvptx-newlib7-devel
%defattr(-,root,root)
%{_prefix}/%{gcc_target_arch}
%endif

%changelog
