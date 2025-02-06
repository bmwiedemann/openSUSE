#
# spec file for package glibc
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


# Run with osc --with=fast_build to have a shorter turnaround
# It will avoid building some parts of glibc
%bcond_with    fast_build

%bcond_with snapshot
%bcond_with ringdisabled

%define flavor @BUILD_FLAVOR@%{nil}

# We need to map from flavor to cross-arch, but as we need the
# result in BuildRequires where the build service evaluates, we
# can use only simple RPM expressions, no lua, no shell, no '{expand:'
# expression :-/  Ideally we'd like to just strip the 'cross_' prefix,
# but we can't.  So enumerate the possibilities for now.
%define cross_arch %{cross_cpu}
%if "%flavor" == "cross-aarch64"
%define cross_cpu aarch64
%endif
%if "%flavor" == "cross-riscv64"
%define cross_cpu riscv64
%endif
%if "%flavor" == "cross-s390x"
%define cross_cpu s390x
%endif
%if "%flavor" == "cross-ppc64le"
%define cross_arch ppc64le
%define cross_cpu powerpc64le
%endif

%if 0%{?cross_cpu:1}
%define binutils_os %{cross_cpu}-suse-linux
# use same sysroot as in binutils.spec
%define sysroot %{_prefix}/%{binutils_os}/sys-root
%endif

%if 0%{?suse_version} >= 1550
%bcond_without usrmerged
%else
%bcond_with usrmerged
%endif

%if 0%{?suse_version} >= 1600
%bcond_with nscd
%else
%bcond_without nscd
%endif

%if 0%{?gcc_version} < 13
%define with_gcc 13
%endif

%bcond_with build_all
%define build_main 1
%define build_utils %{with build_all}
%define build_testsuite %{with build_all}
%define build_cross 0
%if "%flavor" == "utils"
%if %{with ringdisabled}
ExclusiveArch:  do_not_build
%endif
%define build_main 0
%define build_utils 1
%define build_testsuite 0
%endif
%if "%flavor" == "testsuite"
%if %{with ringdisabled}
ExclusiveArch:  do_not_build
%endif
%define build_main 0
%define build_utils 0
%define build_testsuite 1
%endif
%if 0%{?cross_cpu:1}
%define build_main 0
%define build_utils 0
%define build_testsuite 0
%define build_cross 1
%undefine _build_create_debug
%define _enable_debug_packages 0
ExcludeArch:    %{cross_arch}
%if 0%{?suse_version} < 1600
ExclusiveArch:  do_not_build
%endif
%endif
%define host_arch %{?cross_cpu}%{!?cross_cpu:%{_target_cpu}}

# Enable support for livepatching.
%define have_livepatching_support 0
%if %{build_cross}
%if "%{cross_arch}" == "x86_64"
%define have_livepatching_support 1
%endif
%else
%ifarch x86_64
%define have_livepatching_support 1
%endif
%endif

%if %{have_livepatching_support}
%bcond_without livepatching
%else
%bcond_with livepatching
%endif

%if %{build_main}
%define name_suffix %{nil}
%else
%define name_suffix -%{flavor}-src
%endif

%define __filter_GLIBC_PRIVATE 1
%ifarch i686
# For i686 let's only build what's different from i586, so
# no need to build documentation
%define build_profile 1
%define build_locales 1
%define build_html 0
%else
%if %{with fast_build} || %{build_cross} || %{build_utils} && %{without build_all}
%define build_profile 0
%define build_locales 0
%define build_html 0
%else
# Default:
%define build_profile 1
%define build_locales 1
%define build_html 1
%endif
%endif

%define build_variants %{build_main}

%define disable_assert 0
%define enable_stackguard_randomization 1
# glibc requires at least kernel 3.2
%define enablekernel 3.2
# some architectures need a newer kernel
%ifarch ppc64le
%define enablekernel 3.10
%endif
%ifarch aarch64
%define enablekernel 3.7
%endif
%ifarch ia64
%define enablekernel 3.2.18
%endif
%ifarch riscv64
%define enablekernel 4.15
%endif
%ifarch loongarch64
%define enablekernel 5.19
%endif

# Before 2.29
%define libnsl_archs %ix86 %alpha hppa m68k %mips32 %mips64 %sparc ppc ppc64 ppc64le x86_64 s390 s390x %arm aarch64 riscv64
# Before 2.34
%define libutil_archs %libnsl_archs
# Before 2.35
%define libanl_archs %libutil_archs

Name:           glibc%{name_suffix}
Summary:        Standard Shared Libraries (from the GNU C Library)
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0
Group:          System/Libraries
Version:        2.40
Release:        0
%if %{without snapshot}
%define git_id ef321e23c2
%define libversion %version
%else
%define git_id %(echo %version | sed 's/.*\.g//')
%define libversion %(echo %version | sed 's/\.[^.]*\.g.*//')
%endif
URL:            https://www.gnu.org/software/libc/libc.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         https://ftp.gnu.org/pub/gnu/glibc/glibc-%{version}.tar.xz
%if %{without snapshot}
Source1:        https://ftp.gnu.org/pub/gnu/glibc/glibc-%{version}.tar.xz.sig
%endif
Source2:        http://savannah.gnu.org/project/memberlist-gpgkeys.php?group=libc&download=1#/glibc.keyring
Source4:        manpages.tar.bz2
Source5:        nsswitch.conf
Source7:        bindresvport.blacklist
Source9:        glibc.rpmlintrc
Source10:       baselibs.conf
# For systemd
Source20:       nscd.conf
Source21:       nscd.service
Source22:       nscd.sysusers

%if %{build_main}
# ngpt was used in 8.1 and SLES8
Obsoletes:      ngpt < 2.2.2
Obsoletes:      ngpt-devel < 2.2.2
Provides:       ngpt = 2.2.2
Provides:       ngpt-devel = 2.2.2
%if %{without nscd}
Obsoletes:      nscd <= %{version}
%endif
Conflicts:      kernel < %{enablekernel}
%if %{with usrmerged}
# make sure we have post-usrmerge filesystem package
Conflicts:      filesystem < 15.6
%endif
# bug437293 - handle update from SLES10 on PowerPC
%ifarch ppc64
Obsoletes:      glibc-64bit
%endif
%ifarch ppc
Obsoletes:      glibc-32bit
%endif
%ifarch armv6hl armv7hl
# The old runtime linker link gets not provided by rpm find.provides, but it exists
Provides:       ld-linux.so.3
Provides:       ld-linux.so.3(GLIBC_2.4)
%endif
Requires(pre):  filesystem
Recommends:     glibc-extra
Recommends:     glibc-gconv-modules-extra
Provides:       rtld(GNU_HASH)
%endif
%if %{build_utils}
Requires:       glibc = %{version}
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  audit-devel
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  libcap-devel
BuildRequires:  libselinux-devel
BuildRequires:  makeinfo
BuildRequires:  python3-base
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemtap-headers
BuildRequires:  sysuser-tools
BuildRequires:  xz
%if 0%{?with_gcc:1}
BuildRequires:  gcc%{with_gcc}
%endif
%if %{build_testsuite}
BuildRequires:  gcc%{?with_gcc}-c++
BuildRequires:  gdb
BuildRequires:  glibc-devel-static
BuildRequires:  libidn2-0
BuildRequires:  libstdc++-devel
BuildRequires:  python3-pexpect
%endif
%if %{build_utils}
BuildRequires:  gd-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
%endif
%if %{build_cross}
BuildRequires:  cross-%{cross_arch}-gcc%{!?with_gcc:%{gcc_version}}%{?with_gcc}-bootstrap
BuildRequires:  cross-%{cross_arch}-linux-glibc-devel
%endif
%if "%flavor" == "i686"
ExclusiveArch:  i586 i686
BuildArch:      i686
# Sync only this build counter with the main build
#!BcntSyncTag:  glibc
%endif

###
# Patches are ordered in the following groups:
# Patches that we will never upstream or which have not been looked at: 0-999
# Patches taken from upstream: 1000-2000
# Patches that are going upstream, waiting approval: 2000-3000
###

###
# Patches that upstream will not accept
###

###
# openSUSE specific patches - won't go upstream
###
### openSUSE extensions, configuration
# PATCH-FIX-OPENSUSE Fix path for nscd databases
Patch6:         glibc-2.3.3-nscd-db-path.diff
# PATCH-FIX-OPENSUSE Fix path for nss_db (bnc#753657) - aj@suse.de
Patch7:         nss-db-path.patch
# PATCH-FIX-OPENSUSE adjust nscd.conf
Patch8:         glibc-nscd.conf.patch
# PATCH-FIX-OPENSUSE -- add some extra information to version output - kukuk@suse.de
Patch10:        glibc-version.diff
# PATCH-FIX-OPENSUSE -- Make --no-archive default for localedef - kukuk@suse.de
Patch13:        glibc-2.3.2.no_archive.diff
# PATCH-FIX-OPENSUSE -- add blacklist for bindresvport
Patch14:        glibc-bindresvport-blacklist.diff
# PATCH-FEATURE-SLE Use nscd user for nscd
Patch19:        nscd-server-user.patch
# PATCH-FEATURE-SLE read nsswich.conf from /usr
Patch20:        glibc-nsswitch-usr.diff
# PATCH-FEATURE-SLE Add ULP prologue into ASM functions
Patch21:        ulp-prologue-into-asm-functions.patch

### Locale related patches
# PATCH-FIX-OPENSUSE Add additional locales
Patch100:       add-locales.patch
# PATCH-FIX-OPENSUSE -- Add no_NO back (XXX: Still needed?)
Patch102:       glibc-2.4.90-no_NO.diff
# PATCH-FIX-OPENSUSE -- Renames for China
Patch103:       glibc-2.4-china.diff

### Network related patches
# PATCH-FIX-OPENSUSE Warn about usage of mdns in resolv.conv
Patch304:       glibc-resolv-mdnshint.diff
# PATCH-FIX-OPENSUSE disable rewriting ::1 to 127.0.0.1 for /etc/hosts bnc#684534, bnc#706719
Patch306:       glibc-fix-double-loopback.diff

%if %{without snapshot}
###
# Patches from upstream
# PATCH-FIX-UPSTREAM Fix missing randomness in __gen_tempname (BZ #32214)
Patch1000:      gen-tempname-randomness.patch
###
%endif

###
# Patches awaiting upstream approval
###
# PATCH-FIX-UPSTREAM Avoid concurrency problem in ldconfig (BZ #23973)
Patch2000:      ldconfig-concurrency.patch

# Non-glibc patches
# PATCH-FIX-OPENSUSE Remove debianisms from manpages
Patch3000:      manpages.patch

%description
The GNU C Library provides the most important standard libraries used
by nearly all programs: the standard C library, the standard math
library, and the POSIX thread library. A system is not functional
without these libraries.

%package -n glibc-utils
Summary:        Development utilities from the GNU C Library
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++
Requires:       glibc = %{version}

%description -n glibc-utils
The glibc-utils package contains mtrace, a memory leak tracer and
xtrace, a function call tracer which can be helpful during program
debugging.

If you are unsure if you need this, do not install this package.

%package -n glibc-testsuite
Summary:        Testsuite results from the GNU C Library
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++

%description -n glibc-testsuite
This package contains the testsuite results from the GNU C Library.

%if %{build_main}
%package info
Summary:        Info Files for the GNU C Library
License:        GFDL-1.1-only
Group:          Documentation/Other
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
BuildArch:      noarch

%description info
This package contains the documentation for the GNU C library stored as
info files. Due to a lack of resources, this documentation is not
complete and is partially out of date.

%package html
Summary:        HTML Documentation for the GNU C Library
License:        GFDL-1.1-only
Group:          Documentation/HTML
BuildArch:      noarch

%description html
This package contains the HTML documentation for the GNU C library. Due
to a lack of resources, this documentation is not complete and is
partially out of date.

%package i18ndata
Summary:        Database Sources for 'locale'
License:        GPL-2.0-or-later AND MIT
Group:          System/Libraries
BuildArch:      noarch

%description i18ndata
This package contains the data needed to build the locale data files to
use the internationalization features of the GNU libc. It is normally
not necessary to install this packages, the data files are already
created.

%package locale-base
Summary:        en_US Locale Data for Localized Programs
License:        GPL-2.0-or-later AND MIT AND LGPL-2.1-or-later
Group:          System/Libraries
Requires:       glibc = %{version}

%description locale-base
Locale data for the internationalisation features of the GNU C library.
This package contains only the U.S. English locale.

%package locale
Summary:        Locale Data for Localized Programs
License:        GPL-2.0-or-later AND MIT AND LGPL-2.1-or-later
Group:          System/Libraries
Requires:       glibc-locale-base = %{version}
# bug437293
%ifarch ppc64
Obsoletes:      glibc-locale-64bit
%endif
%ifarch ppc
Obsoletes:      glibc-locale-32bit
%endif

%description locale
Locale data for the internationalisation features of the GNU C library.

%package -n nscd
Summary:        Name Service Caching Daemon
License:        GPL-2.0-or-later
Group:          System/Daemons
Provides:       glibc:/usr/sbin/nscd
Requires:       glibc = %{version}
Obsoletes:      unscd <= 0.48
%{?sysusers_requires}
%{?systemd_requires}

%description -n nscd
Nscd caches name service lookups and can dramatically improve
performance with NIS, NIS+, and LDAP.

%package gconv-modules-extra
Summary:        Non-essential gconv modules
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       glibc = %{version}
Provides:       glibc-locale-base:%{_libdir}/gconv/BIG5.so

%description gconv-modules-extra
Modules for use by the iconv facility, to support encodings other than
Latin-1 and UTF based.

%package profile
Summary:        Libc Profiling and Debugging Versions
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0
Group:          Development/Libraries/C and C++
Requires:       glibc = %{version}
# bug437293
%ifarch ppc64
Obsoletes:      glibc-profile-64bit
%endif
%ifarch ppc
Obsoletes:      glibc-profile-32bit
%endif

%description profile
This package contains special versions of the GNU C library which are
necessary for profiling and debugging.

%package devel
Summary:        Include Files and Libraries Mandatory for Development
License:        BSD-3-Clause AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Obsoletes:      epoll = 1.0
Provides:       epoll < 1.0
# bug437293
%ifarch ppc64
Obsoletes:      glibc-devel-64bit
%endif
%ifarch ppc
Obsoletes:      glibc-devel-32bit
%endif
Requires:       glibc = %{version}
Requires:       libxcrypt-devel
Requires:       linux-kernel-headers

%description devel
These libraries are needed to develop programs which use the standard C
library.

%package devel-static
Summary:        C library static libraries for -static linking
License:        BSD-3-Clause AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libxcrypt-devel-static
# Provide Fedora name for package to make packaging easier
Provides:       %{name}-static = %{version}

%description devel-static
The glibc-devel-static package contains the C library static libraries
for -static linking.  You don't need these, unless you link statically,
which is highly discouraged.

%package extra
# makedb requires libselinux. We add this program in a separate
# package so that glibc does not require libselinux.
Summary:        Extra binaries from GNU C Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       glibc = %{version}

%description extra
The glibc-extra package contains some extra binaries for glibc that
are not essential but recommend for use.

makedb: A program to create a database for nss

%lang_package
%endif

%package -n cross-%{cross_arch}-glibc-devel
Summary:        Include Files and Libraries Mandatory for Development
License:        BSD-3-Clause AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       cross-%{cross_arch}-linux-glibc-devel
BuildArch:      noarch
AutoReqProv:    off

%description -n cross-%{cross_arch}-glibc-devel
These libraries are needed to develop programs which use the standard C
library in a cross compilation setting.

%package -n libnsl1
Summary:        Legacy Network Support Library (NIS)
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libnsl1
Network Support Library for legacy architectures.  This library does not
have support for IPv6.

%if 0%{suse_version} >= 1500
%define make_output_sync -Oline
%endif

%prep
%autosetup -n glibc-%{version} -a 4 -p1

rm -f manpages/catchsegv.1

%build
# Disable LTO due to a usage of top-level assembler that
#  causes LTO issues (boo#1138807).
%define _lto_cflags %{nil}
if [ -x /bin/uname.bin ]; then
	/bin/uname.bin -a
else
	uname -a
fi
uptime || :
ulimit -a
nice
# We do not want configure to figure out the system its building one
# to support a common ground and thus set build and host ourself.
target="%{host_arch}-suse-linux"
case " %arm " in
  *" %{host_arch} "*) target="%{host_arch}-suse-linux-gnueabi" ;;
esac
%ifarch %arm
%define build %{_target_cpu}-suse-linux-gnueabi
%else
%define build %{_target_cpu}-suse-linux
%endif
# Don't use as-needed, it breaks glibc assumptions
# Before enabling it, run the testsuite and verify that it
# passes completely
export SUSE_ASNEEDED=0
# This is controlled by --enable-bind-now.
export SUSE_ZNOW=0
# Adjust glibc version.h
echo "#define CONFHOST \"${target}\"" >> version.h
echo "#define GITID \"%{git_id}\"" >> version.h
#
# Default CFLAGS and Compiler
#
enable_stack_protector=
BuildFlags=
tmp="%{optflags}"
for opt in $tmp; do
  case $opt in
    -fstack-protector-*) enable_stack_protector=${opt#-fstack-protector-} ;;
    -fstack-protector) enable_stack_protector=yes ;;
    -D_FORTIFY_SOURCE=*) enable_fortify_source=${opt#-D_FORTIFY_SOURCE=} ;;
    -ffortify=* | *_FORTIFY_SOURCE*) ;;
%if "%flavor" == "i686"
    *i586*) BuildFlags+=" ${opt/i586/i686}" ;;
%endif
%if %{build_cross}
    -m*) ;;  # remove all machine specific options for crosses
%endif
    *) BuildFlags+=" $opt" ;;
  esac
done
%if "%flavor" == "i686"
BuildFlags+=" -march=i686 -mtune=generic"
%else
%if !%{build_cross}
%ifarch i586
# workaround for unaligned stack in java-11-openjdk and mariadb
# by avoiding use of SSE
BuildFlags+=" -march=i586"
%endif
%endif
%endif
%if 0%{?with_gcc:1}
BuildCC="gcc-%{with_gcc}"
BuildCCplus="g++-%{with_gcc}"
%else
BuildCC="%__cc"
BuildCCplus="%__cxx"
%endif

#
#now overwrite for some architectures
#
%if %{build_cross}
BuildCC=%{cross_cpu}-suse-linux-gcc
BuildCCplus=%{cross_cpu}-suse-linux-g++
%else
%ifarch sparc64
	BuildFlags="-O2 -mcpu=ultrasparc -mvis -fcall-used-g6"
	BuildCC="gcc -m64"
	BuildCCplus="$BuildCCplus -m64"
%endif
%ifarch sparc
	BuildFlags="$BuildFlags -fcall-used-g6"
	BuildCC="gcc -m32"
	BuildCCplus="$BuildCCplus -m32"
%endif
%ifarch sparcv9
	BuildFlags="$BuildFlags -mcpu=ultrasparc -fcall-used-g6"
	BuildCC="gcc -m32"
	BuildCCplus="$BuildCCplus -m32"
%endif
%ifarch alphaev6
	BuildFlags="-mcpu=ev6"
%endif
%ifarch ppc ppc64
	BuildFlags="$(echo $BuildFlags | sed 's#-mminimal-toc##')"
	BuildFlags+=" -mtune=power5"
%endif
%ifarch ppc64
	BuildCC="$BuildCC -m64"
	BuildCCplus="$BuildCCplus -m64"
%endif
%ifarch hppa
	BuildFlags="$BuildFlags -mpa-risc-1-1 -fstrict-aliasing"
%endif
%if %{disable_assert}
	BuildFlags="$BuildFlags -DNDEBUG=1"
%endif
%ifarch mipsel
	# fails to build otherwise - need to recheck and fix
	%define enable_stackguard_randomization 0
%endif
%endif

#
# Build base glibc
#
mkdir cc-base
cd cc-base
%if %{build_profile}
profile="--enable-profile"
%else
profile="--disable-profile"
%endif

../configure \
	CFLAGS="$BuildFlags" BUILD_CFLAGS="$BuildFlags" \
	CC="$BuildCC" CXX="$BuildCCplus" \
	--prefix=%{_prefix} \
	--libexecdir=%{_libexecdir} --infodir=%{_infodir} \
        $profile \
	--build=%{build} --host=${target} \
%if %{build_cross}
	--with-headers=%{sysroot}/usr/include \
%else
%ifarch armv7hl ppc ppc64 ppc64le i686 x86_64 sparc sparc64 s390 s390x
	--enable-multi-arch \
%endif
%ifarch aarch64
	--enable-memory-tagging \
%endif
%ifarch mipsel
	--without-fp \
%endif
%ifarch ppc
	--with-cpu=power4 \
%endif
%ifarch ppc64p7
	--with-cpu=power7 \
%endif
%ifarch x86_64
%if %suse_version > 1500
	--enable-cet \
%endif
%endif
	--enable-systemtap \
%endif
%if %{enable_stackguard_randomization}
	--enable-stackguard-randomization \
%endif
	${enable_stack_protector:+--enable-stack-protector=$enable_stack_protector} \
%if !%{build_cross}
	${enable_fortify_source:+--enable-fortify-source=$enable_fortify_source} \
%endif
	--enable-tunables \
	--enable-kernel=%{enablekernel} \
	--with-bugurl=http://bugs.opensuse.org \
	--enable-bind-now \
	--disable-timezone-tools \
%if %{with livepatching}
	--enable-userspace-livepatch \
%endif
	--disable-crypt \
%if %{without nscd}
        --disable-build-nscd \
        --disable-nscd \
%endif
  || {
    rc=$?;
    echo "------- BEGIN config.log ------";
    %{__cat} config.log;
    echo "------- END config.log ------";
    exit $rc;
  }

%if %{build_main} && %{with livepatching}
# Append necessary flags for livepatch support, if enabled.  Only objects
# included in shared libraries should be prepared for live patching.
echo 'CFLAGS-.os += -fdump-ipa-clones' \
     >> Makeconfig
%endif

make %{?_smp_mflags} %{?make_output_sync}
cd ..

#
# Build html documentation
#
%if %{build_html}
make %{?_smp_mflags} %{?make_output_sync} -C cc-base html
%endif

%if %{with nscd}
# sysusers.d
%sysusers_generate_pre %{SOURCE22} nscd nscd.conf
%endif

%check
%if %{build_testsuite}
# The testsuite will fail if asneeded is used
export SUSE_ASNEEDED=0
# The testsuite will fail if -znow is used
export SUSE_ZNOW=0
# Increase timeout
export TIMEOUTFACTOR=16
# The testsuite does its own malloc checking
unset MALLOC_CHECK_ MALLOC_PERTURB_
make %{?_smp_mflags} %{?make_output_sync} -C cc-base -k check || {
  cd cc-base
  o=$-
  set +x
  for sum in subdir-tests.sum */subdir-tests.sum; do
    while read s t; do
      case $s in
	XPASS:|PASS:)
	  echo ++++++ $s $t ++++++
	  ;;
	*) # X?FAIL:
	  echo ------ $s $t ------
	  test ! -f $t.out || cat $t.out
	  ;;
	esac
    done < $sum
  done
  set -$o
  # Fail build if there where compilation errors during testsuite run
  test -f tests.sum
}
%else
# This has to pass on all platforms!
# Exceptions:
# None!
make %{?_smp_mflags} %{?make_output_sync} -C cc-base check-abi
make %{?_smp_mflags} %{?make_output_sync} -C cc-base test t=elf/check-localplt
%endif

%define rtldlib %{_lib}
# Each architecture has a different name for the dynamic linker:
%ifarch %arm
%ifarch armv6hl armv7hl
%define rtld_name ld-linux-armhf.so.3
# Keep compatibility link
%define rtld_oldname ld-linux.so.3
%else
%define rtld_name ld-linux.so.3
%endif
%endif
%ifarch ia64
%define rtld_name ld-linux-ia64.so.2
%endif
%ifarch ppc s390 mips hppa m68k
%define rtld_name ld.so.1
%endif
%ifarch ppc64
%define rtld_name ld64.so.1
%endif
%ifarch ppc64le
%define rtld_name ld64.so.2
%endif
%ifarch s390x
%define rtldlib lib
%define rtld_name ld64.so.1
%endif
%ifarch x86_64
%define rtld_name ld-linux-x86-64.so.2
%endif
%ifarch %ix86 %sparc
%define rtld_name ld-linux.so.2
%endif
%ifarch aarch64
%define rtldlib lib
%define rtld_name ld-linux-aarch64.so.1
%endif
%ifarch riscv64
%define rtldlib lib
%define rtld_name ld-linux-riscv64-lp64d.so.1
%endif
%ifarch loongarch64
%define rtld_name ld-linux-loongarch-lp64d.so.1
%endif

%if %{with usrmerged}
%define rootsbindir %{_sbindir}
%define slibdir %{_libdir}
%define rtlddir %{_prefix}/%{rtldlib}
%else
%define rootsbindir /sbin
%define slibdir /%{_lib}
%define rtlddir /%{rtldlib}
%endif

%install
%if !%{build_testsuite}

%if %{with usrmerged}
mkdir -p %{buildroot}%{_libdir}
ln -s %{buildroot}%{_libdir} %{buildroot}/%{_lib}
%if "%{rtldlib}" != "%{_lib}"
mkdir -p %{buildroot}%{rtlddir}
ln -s %{buildroot}%{rtlddir} %{buildroot}/%{rtldlib}
%endif
mkdir -p %{buildroot}%{_sbindir}
ln -s %{buildroot}%{_sbindir} %{buildroot}/sbin
%endif

%if !%{build_cross}
%ifarch riscv64
mkdir -p %{buildroot}%{_libdir}
ln -s . %{buildroot}%{_libdir}/lp64d
%if "%{slibdir}" != "%{_libdir}"
mkdir -p %{buildroot}%{slibdir}
ln -s . %{buildroot}%{slibdir}/lp64d
%endif
%endif
%endif

%if %{build_main}

%if %{with livepatching}
%define tar_basename glibc-livepatch-%{version}-%{release}
%define tar_package_name %{tar_basename}.%{_arch}.tar.xz
%define clones_dest_dir %{tar_basename}/%{_arch}

# Ipa-clones are files generated by gcc which logs changes made across
# functions, and we need to know such changes to build livepatches
# correctly. These files are intended to be used by the livepatch
# developers and may be retrieved by using `osc getbinaries`.
#
# Create ipa-clones destination folder and move clones there.
mkdir -p ipa-clones/%{clones_dest_dir}
find . -name "*.ipa-clones" ! -empty \
       -exec cp -t ipa-clones/%{clones_dest_dir} --parents {} +

# Create tarball with ipa-clones.
tar -cJf %{tar_package_name} -C ipa-clones \
    --owner root --group root --sort name %{tar_basename}

# Copy tarball to the OTHER folder to store it as artifact.
cp %{tar_package_name} %{_topdir}/OTHER

%endif

# We don't want to strip the .symtab from our libraries in find-debuginfo.sh,
# certainly not from libc.so.* because it is used by libthread_db to find
# some non-exported symbols in order to detect if threading support
# should be enabled.  These symbols are _not_ exported, and we can't easily
# export them retroactively without changing the ABI.  So we have to
# continue to "export" them via .symtab, instead of .dynsym :-(
# But we also want to keep .symtab and .strtab of other libraries since some
# debugging tools currently require these sections directly inside the main
# files - specifically valgrind and PurifyPlus.
export STRIP_KEEP_SYMTAB=*.so*

# Install base glibc
make %{?_smp_mflags} %{?make_output_sync} install_root=%{buildroot} install -C cc-base

# Install locales
%if %{build_locales}
	cd cc-base
	# localedef creates hardlinks to other locales if possible
	# this will not work if we generate them in parallel.
	# thus we need to run fdupes on  /usr/lib/locale/
	# Still, on my system this is a speed advantage:
	# non-parallel build for install-locales: 9:34mins
	# parallel build with fdupes: 7:08mins
	make %{?_smp_mflags} %{?make_output_sync} install_root=%{buildroot} localedata/install-locales
	# Avoid hardlinks across subpackages
	mv %{buildroot}/usr/lib/locale/{en_US,C}.utf8 .
	%fdupes %{buildroot}/usr/lib/locale
	mv {en_US,C}.utf8 %{buildroot}/usr/lib/locale/
	cd ..
%endif

%ifnarch i686
# Create file list for glibc-lang package
%{find_lang} libc
%else
# The translations are shared with the base flavour
rm -rf %{buildroot}%{_datadir}/locale/*/
%endif

# Miscelanna:

install -m 644 %{SOURCE7} %{buildroot}/etc
%if %suse_version > 1500
install -D -m 644 %{SOURCE5} %{buildroot}%{_prefix}/etc/nsswitch.conf
%else
install -m 644 %{SOURCE5} %{buildroot}/etc/nsswitch.conf
%endif

%if %{build_html}
mkdir -p %{buildroot}%{_datadir}/doc/glibc
cp -p cc-base/manual/libc/*.html %{buildroot}%{_datadir}/doc/glibc
%endif

cd manpages; make install_root=%{buildroot} install; cd ..

%if %{with nscd}
# nscd tools:

%ifnarch i686
cp nscd/nscd.conf %{buildroot}/etc
mkdir -p %{buildroot}/etc/init.d
ln -sf %{rootsbindir}/service %{buildroot}%{_sbindir}/rcnscd
mkdir -p %{buildroot}/run/nscd
mkdir -p %{buildroot}/var/lib/nscd
%endif
%endif

#
# Create ld.so.conf
#
cat > %{buildroot}/etc/ld.so.conf <<EOF
%if "%{_lib}" != "lib"
/usr/local/%{_lib}
%endif
%ifarch ppc
/usr/local/lib64
%endif
/usr/local/lib
include /etc/ld.so.conf.d/*.conf
# /lib64, /lib, /usr/lib64 and /usr/lib gets added
# automatically by ldconfig after parsing this file.
# So, they do not need to be listed.
EOF
# Add ldconfig cache directory for directory ownership
mkdir -p %{buildroot}/var/cache/ldconfig
# Empty the ld.so.cache:
rm -f %{buildroot}/etc/ld.so.cache
touch %{buildroot}/etc/ld.so.cache

# Don't look at ldd! We don't wish a /bin/sh requires
chmod 644 %{buildroot}%{_bindir}/ldd

rm -f %{buildroot}%{rootsbindir}/sln

%if %{with nscd}
%ifnarch i686
mkdir -p %{buildroot}/usr/lib/tmpfiles.d/
install -m 644 %{SOURCE20} %{buildroot}/usr/lib/tmpfiles.d/
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 644 %{SOURCE21} %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}/usr/lib/sysusers.d/
install -m 644 %{SOURCE22} %{buildroot}/usr/lib/sysusers.d/nscd.conf
%endif
%endif

%if 0%{?rtld_oldname:1}
# Provide compatibility link
ln -s %{rtlddir}/%{rtld_name} %{buildroot}%{rtlddir}/%{rtld_oldname}
%endif

# Move getconf to %{_libexecdir}/getconf/ to avoid cross device link
mv %{buildroot}%{_bindir}/getconf %{buildroot}%{_libexecdir}/getconf/getconf
ln -s %{_libexecdir}/getconf/getconf %{buildroot}%{_bindir}/getconf

%if !%{build_utils}
# Remove unwanted files (packaged in glibc-utils)
rm -f %{buildroot}%{slibdir}/libmemusage*
rm -f %{buildroot}%{slibdir}/libpcprofile*
rm -f %{buildroot}%{_bindir}/memusage*
rm -f %{buildroot}%{_bindir}/mtrace
rm -f %{buildroot}%{_bindir}/pcprofiledump
rm -f %{buildroot}%{_bindir}/sotruss
rm -f %{buildroot}%{_bindir}/xtrace
rm -f %{buildroot}%{_bindir}/pldd
rm -rf %{buildroot}%{_libdir}/audit

%ifarch i686
# Remove files from glibc-{extra,info,i18ndata}, nscd
rm -rf %{buildroot}%{_infodir} %{buildroot}%{_prefix}/share/i18n
rm -f %{buildroot}%{_bindir}/makedb %{buildroot}/var/lib/misc/Makefile
%if %{with nscd}
rm -f %{buildroot}%{_sbindir}/nscd
%endif
%endif

%ifnarch i686
# /var/lib/misc is incompatible with transactional updates (bsc#1138726)
mkdir %{buildroot}%{_prefix}/share/misc
mv %{buildroot}/var/lib/misc/Makefile %{buildroot}%{_prefix}/share/misc/Makefile.makedb
ln -s %{_prefix}/share/misc/Makefile.makedb %{buildroot}/var/lib/misc/Makefile
%endif

%endif

# LSB
%ifarch %ix86
ln -sf %{rtlddir}/%{rtld_name} $RPM_BUILD_ROOT%{slibdir}/ld-lsb.so.3
%endif
%ifarch x86_64
ln -sf %{rtlddir}/%{rtld_name} $RPM_BUILD_ROOT%{slibdir}/ld-lsb-x86-64.so.3
%endif
%ifarch ppc
ln -sf %{rtlddir}/%{rtld_name} $RPM_BUILD_ROOT%{slibdir}/ld-lsb-ppc32.so.3
%endif
%ifarch ppc64
ln -sf %{rtlddir}/%{rtld_name} $RPM_BUILD_ROOT%{slibdir}/ld-lsb-ppc64.so.3
%endif
%ifarch s390
ln -sf %{rtlddir}/%{rtld_name} $RPM_BUILD_ROOT%{slibdir}/ld-lsb-s390.so.3
%endif
%ifarch s390x
ln -sf %{rtlddir}/%{rtld_name} $RPM_BUILD_ROOT%{slibdir}/ld-lsb-s390x.so.3
%endif

%else

%if %{build_utils}

make %{?_smp_mflags} install_root=%{buildroot} install -C cc-base \
  subdirs='malloc debug elf'
cd manpages; make install_root=%{buildroot} install; cd ..
# Remove unwanted files
rm -f %{buildroot}%{rtlddir}/ld*.so* %{buildroot}%{slibdir}/lib[!mp]*
%if "%{_libdir}" != "%{slibdir}"
rm -f %{buildroot}%{_libdir}/lib*
%else
rm -f %{buildroot}%{_libdir}/lib*.a
%endif
rm -f %{buildroot}%{_bindir}/{ld.so,ldd,sprof}
rm -rf %{buildroot}%{_mandir}/man*
rm -rf %{buildroot}%{rootsbindir} %{buildroot}%{_includedir}
%ifarch riscv64
rm %{buildroot}%{_libdir}/lp64d
%if "%{slibdir}" != "%{_libdir}"
rm %{buildroot}%{slibdir}/lp64d
%endif
%endif

%endif

%if %{build_cross}
# See above
export STRIP_KEEP_SYMTAB=*.so*
export NO_BRP_STRIP_DEBUG=true
make %{?_smp_mflags} install_root=%{buildroot}/%{sysroot} install -C cc-base
rm -rf %{buildroot}/%{sysroot}/%{_libdir}/audit
rm -rf %{buildroot}/%{sysroot}/%{_libdir}/gconv
rm -rf %{buildroot}/%{sysroot}/%{_infodir}
rm -rf %{buildroot}/%{sysroot}/%{_datadir}
rm -rf %{buildroot}/%{sysroot}/%{_libexecdir}
rm -rf %{buildroot}/%{sysroot}/%{_bindir}
rm -rf %{buildroot}/%{sysroot}/%{_sbindir}
rm -rf %{buildroot}/%{sysroot}/etc
rm -rf %{buildroot}/%{sysroot}/var

# Some programs look for <prefix>/lib/../$subdir where subdir is
# for instance "lib64".  For this path lookup to succeed we need the
# ../lib subdir, even if it's empty, so enforce its existence.
mkdir -p %{buildroot}/%{sysroot}/lib
mkdir -p %{buildroot}/%{sysroot}/%{_prefix}/lib

%endif

%endif

%if %{with usrmerged}

rm %{buildroot}/%{_lib}
%if "%{rtldlib}" != "%{_lib}"
rm %{buildroot}/%{rtldlib}
%endif
rm %{buildroot}/sbin

%endif

%endif

%if %{build_main}

%post -p <lua>
function exec(path, ...)
  local pid = posix.fork()
  if pid == 0 then
     posix.exec(path, ...)
     io.write(path, ": exec failed: ", posix.errno(), "\n")
     os.exit(1)
  end
  if not pid then
     error(path .. ": fork failed: " .. posix.errno() .. "\n")
  end
  posix.wait(pid)
end

-- First, get rid of platform-optimized libraries. We remove any we have
-- ever built, since otherwise we might end up using some old leftover
-- libraries when new ones aren't installed in their place anymore.
libraries = { "libc.so.6", "libc.so.6.1", "libm.so.6", "libm.so.6.1",
	      "librt.so.1", "libpthread.so.0", "libthread_db.so.1" }
remove_dirs = {
%ifarch i586
  "%{slibdir}/i686/",
%endif
%ifarch ppc ppc64
  "%{slibdir}/power4/", "%{slibdir}/ppc970/",
  "%{slibdir}/power5/", "%{slibdir}/power5+/",
  "%{slibdir}/power6/", "%{slibdir}/power6x/",
  "%{slibdir}/power7/",
  "%{slibdir}/ppc-cell-be/",
%endif
  "%{slibdir}/tls/"
}
for i, remove_dir in ipairs(remove_dirs) do
  for j, library in ipairs(libraries) do
    local file = remove_dir .. library
    -- This file could be a symlink to library-%{version}.so, so check
    -- this and don't remove only the link, but also the library itself.
    local link = posix.readlink(file)
    if link then
      if link:sub(1, 1) ~= "/" then link = remove_dir .. link end
      os.remove(link)
    end
    os.remove(file)
  end
end
if posix.access("%{rootsbindir}/ldconfig", "x") then
  exec("%{rootsbindir}/ldconfig", "-X")
end
if posix.utime("%{_libdir}/gconv/gconv-modules.cache") then
  exec("%{_sbindir}/iconvconfig", "-o", "%{_libdir}/gconv/gconv-modules.cache",
       "--nostdlib", "%{_libdir}/gconv")
end

%postun -p %{rootsbindir}/ldconfig

%post gconv-modules-extra -p %{_sbindir}/iconvconfig
%postun gconv-modules-extra -p %{_sbindir}/iconvconfig

%post info
%install_info --info-dir=%{_infodir} %{_infodir}/libc.info.gz

%preun info
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libc.info.gz

%pre -n nscd -f nscd.pre
%service_add_pre nscd.service

%preun -n nscd
%service_del_preun nscd.service

%post -n nscd
%service_add_post nscd.service
%tmpfiles_create /usr/lib/tmpfiles.d/nscd.conf
# Previously we had nscd.socket, remove it
test -x /usr/bin/systemctl && /usr/bin/systemctl stop nscd.socket 2>/dev/null || :
test -x /usr/bin/systemctl && /usr/bin/systemctl disable nscd.socket 2>/dev/null  || :
# Hard removal in case the above did not work
rm -f /etc/systemd/system/sockets.target.wants/nscd.socket
exit 0

%postun -n nscd
%service_del_postun nscd.service
exit 0

%files
# glibc
%defattr(-,root,root)
%license LICENSES
%config(noreplace) /etc/bindresvport.blacklist
%config /etc/ld.so.conf
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /etc/ld.so.cache
%config(noreplace) /etc/rpc
%if %suse_version > 1500
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /etc/nsswitch.conf
%{_prefix}/etc/nsswitch.conf
%else
%verify(not md5 size mtime) %config(noreplace) /etc/nsswitch.conf
%endif
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /etc/gai.conf
%doc posix/gai.conf
%doc %{_mandir}/man1/gencat.1.gz
%doc %{_mandir}/man1/getconf.1.gz
%doc %{_mandir}/man5/*

%{_bindir}/ld.so
%{rtlddir}/%{rtld_name}
%if 0%{?rtld_oldname:1}
%{rtlddir}/%{rtld_oldname}
%endif
%ifarch %ix86 x86_64 ppc ppc64 s390 s390x
# LSB
%{slibdir}/*-lsb*.so.3
%endif

%ifarch riscv64
%{_libdir}/lp64d
%if "%{slibdir}" != "%{_libdir}"
%{slibdir}/lp64d
%endif
%endif

%{slibdir}/libBrokenLocale.so.1
%ifarch %libanl_archs
%{slibdir}/libanl.so.1
%endif
%{slibdir}/libc.so.6*
%{slibdir}/libc_malloc_debug.so.0
%{slibdir}/libdl.so.2*
%{slibdir}/libm.so.6*
%ifarch x86_64 aarch64
%{slibdir}/libmvec.so.1
%endif
%{slibdir}/libnss_compat.so.2
%{slibdir}/libnss_db.so.2
%{slibdir}/libnss_dns.so.2
%{slibdir}/libnss_files.so.2
%{slibdir}/libnss_hesiod.so.2
%{slibdir}/libpthread.so.0
%{slibdir}/libresolv.so.2
%{slibdir}/librt.so.1
%{slibdir}/libthread_db.so.1
%ifarch %libutil_archs
%{slibdir}/libutil.so.1
%endif
%dir %attr(0700,root,root) /var/cache/ldconfig
%{rootsbindir}/ldconfig
%{_bindir}/gencat
%{_bindir}/getconf
%{_bindir}/getent
%{_bindir}/iconv
%attr(755,root,root) %{_bindir}/ldd
%{_bindir}/locale
%{_bindir}/localedef
%dir %attr(0755,root,root) %{_libexecdir}/getconf
%{_libexecdir}/getconf/*
%{_sbindir}/iconvconfig
%dir %{_libdir}/gconv
%{_libdir}/gconv/ANSI_X3.110.so
%{_libdir}/gconv/CP1252.so
%{_libdir}/gconv/ISO8859-1.so
%{_libdir}/gconv/ISO8859-15.so
%{_libdir}/gconv/UNICODE.so
%{_libdir}/gconv/UTF-16.so
%{_libdir}/gconv/UTF-32.so
%{_libdir}/gconv/UTF-7.so
%{_libdir}/gconv/gconv-modules
%dir %{_libdir}/gconv/gconv-modules.d
%ifarch s390x
%{_libdir}/gconv/gconv-modules.d/gconv-modules-s390.conf
%{_libdir}/gconv/ISO-8859-1_CP037_Z900.so
%{_libdir}/gconv/UTF8_UTF32_Z9.so
%{_libdir}/gconv/UTF16_UTF32_Z9.so
%{_libdir}/gconv/UTF8_UTF16_Z9.so
%endif
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %{_libdir}/gconv/gconv-modules.cache

%files gconv-modules-extra
%dir %{_libdir}/gconv
%dir %{_libdir}/gconv/gconv-modules.d
%{_libdir}/gconv/gconv-modules.d/*.conf
%{_libdir}/gconv/*.so
%exclude %{_libdir}/gconv/ANSI_X3.110.so
%exclude %{_libdir}/gconv/CP1252.so
%exclude %{_libdir}/gconv/ISO8859-1.so
%exclude %{_libdir}/gconv/ISO8859-15.so
%exclude %{_libdir}/gconv/UNICODE.so
%exclude %{_libdir}/gconv/UTF-16.so
%exclude %{_libdir}/gconv/UTF-32.so
%exclude %{_libdir}/gconv/UTF-7.so
%ifarch s390x
%exclude %{_libdir}/gconv/gconv-modules.d/gconv-modules-s390.conf
%exclude %{_libdir}/gconv/ISO-8859-1_CP037_Z900.so
%exclude %{_libdir}/gconv/UTF8_UTF32_Z9.so
%exclude %{_libdir}/gconv/UTF16_UTF32_Z9.so
%exclude %{_libdir}/gconv/UTF8_UTF16_Z9.so
%endif

%files locale-base
%defattr(-,root,root)
%{_datadir}/locale/locale.alias
%if %{build_locales}
%dir %{_prefix}/lib/locale
%{_prefix}/lib/locale/C.utf8
%{_prefix}/lib/locale/en_US.utf8
%endif

%files locale
%defattr(-,root,root)
%if %{build_locales}
%{_prefix}/lib/locale
%exclude %{_prefix}/lib/locale/C.utf8
%exclude %{_prefix}/lib/locale/en_US.utf8
%endif

%files devel
%defattr(-,root,root)
%license COPYING COPYING.LIB
%doc NEWS README
%doc %{_mandir}/man3/*
%{_bindir}/sprof
%{_includedir}/*
%{_libdir}/*.o
%{_libdir}/libBrokenLocale.so
%ifarch %libanl_archs
%{_libdir}/libanl.so
%endif
%{_libdir}/libc.so
%{_libdir}/libc_malloc_debug.so
%{_libdir}/libm.so
%ifarch x86_64 aarch64
%{_libdir}/libmvec.so
%endif
%{_libdir}/libnss_compat.so
%{_libdir}/libnss_db.so
%{_libdir}/libnss_hesiod.so
%{_libdir}/libresolv.so
%{_libdir}/libthread_db.so
# These static libraries are needed even for shared builds
%{_libdir}/libc_nonshared.a
%{_libdir}/libdl.a
%{_libdir}/libg.a
%ifarch ppc ppc64 ppc64le s390 s390x sparc sparcv8 sparcv9 sparcv9v
# This is not built on sparc64.
	%{_libdir}/libnldbl_nonshared.a
%endif
%{_libdir}/libmcheck.a
%{_libdir}/libpthread.a
%{_libdir}/librt.a
%{_libdir}/libutil.a

%files devel-static
%defattr(-,root,root)
%{_libdir}/libBrokenLocale.a
%ifarch %libanl_archs
%{_libdir}/libanl.a
%endif
%{_libdir}/libc.a
%{_libdir}/libm.a
%ifarch x86_64 aarch64
%{_libdir}/libm-%{libversion}.a
%{_libdir}/libmvec.a
%endif
%{_libdir}/libresolv.a

%ifnarch i686
%files info
%defattr(-,root,root)
%doc %{_infodir}/libc.info.gz
%doc %{_infodir}/libc.info-?.gz
%doc %{_infodir}/libc.info-??.gz

%if %{build_html}
%files html
%defattr(-,root,root)
%doc %{_prefix}/share/doc/glibc
%endif

%files i18ndata
%defattr(-,root,root)
%{_prefix}/share/i18n

%if %{with nscd}
%files -n nscd
%defattr(-,root,root)
%config(noreplace) /etc/nscd.conf
%{_sbindir}/nscd
%{_sbindir}/rcnscd
/usr/lib/systemd/system/nscd.service
%dir /usr/lib/tmpfiles.d
/usr/lib/tmpfiles.d/nscd.conf
%dir /usr/lib/sysusers.d
/usr/lib/sysusers.d/nscd.conf
%dir %attr(0755,root,root) %ghost /run/nscd
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /run/nscd/nscd.pid
%attr(0666,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /run/nscd/socket
%dir %attr(0755,root,root) /var/lib/nscd
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/nscd/passwd
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/nscd/group
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/nscd/hosts
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/nscd/services
%attr(0600,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/lib/nscd/netgroup
%endif
%endif

%if %{build_profile}
%files profile
%defattr(-,root,root)
%{_libdir}/libc_p.a
%{_libdir}/libBrokenLocale_p.a
%ifarch %libanl_archs
%{_libdir}/libanl_p.a
%endif
%{_libdir}/libm_p.a
%ifarch x86_64 aarch64
%{_libdir}/libmvec_p.a
%endif
%{_libdir}/libpthread_p.a
%{_libdir}/libresolv_p.a
%{_libdir}/librt_p.a
%ifarch %libutil_archs
%{_libdir}/libutil_p.a
%endif
%{_libdir}/libdl_p.a
%endif

%ifnarch i686
%files extra
%defattr(-,root,root)
%{_bindir}/makedb
%{_prefix}/share/misc/Makefile.makedb
/var/lib/misc/Makefile

%files lang -f libc.lang
%endif

%ifarch %libnsl_archs
%files -n libnsl1
%{slibdir}/libnsl.so.1
%endif

%endif

%if %{build_cross}
%files -n cross-%{cross_arch}-glibc-devel
%defattr(-,root,root)
%license COPYING COPYING.LIB
%{sysroot}
%endif

%if %{build_utils}
%files -n glibc-utils
%defattr(-,root,root)
%{slibdir}/libmemusage.so
%{slibdir}/libpcprofile.so
%dir %{_libdir}/audit
%{_libdir}/audit/sotruss-lib.so
%{_bindir}/memusage
%{_bindir}/memusagestat
%{_bindir}/mtrace
%{_bindir}/pcprofiledump
%{_bindir}/sotruss
%{_bindir}/xtrace
%{_bindir}/pldd
%endif

%changelog
