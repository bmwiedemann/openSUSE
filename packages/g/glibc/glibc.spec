#
# spec file for package glibc
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


# Run with osc --with=fast_build to have a shorter turnaround
# It will avoid building some parts of glibc
%bcond_with    fast_build

%define build_snapshot 0
%bcond_with ringdisabled

%define flavor @BUILD_FLAVOR@%{nil}

%bcond_with build_all
%define build_main 1
%define build_utils %{with build_all}
%define build_testsuite %{with build_all}
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

%if %{build_main}
%define name_suffix %{nil}
%else
%define name_suffix -%{flavor}-src
%endif

Name:           glibc%{name_suffix}
Summary:        Standard Shared Libraries (from the GNU C Library)
License:        LGPL-2.1-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND GPL-2.0-or-later
Group:          System/Libraries
BuildRequires:  audit-devel
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  libcap-devel
BuildRequires:  libselinux-devel
BuildRequires:  makeinfo
BuildRequires:  python3-base
BuildRequires:  shadow
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemtap-headers
BuildRequires:  xz
%if %{build_testsuite}
BuildRequires:  gcc-c++
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
%if "%flavor" == "i686"
ExclusiveArch:  i586 i686
BuildArch:      i686
%endif

%define __filter_GLIBC_PRIVATE 1
%ifarch i686
# For i686 let's only build what's different from i586, so
# no need to build documentation
%define build_profile 1
%define build_locales 1
%define build_html 0
%else
%if %{with fast_build} || %{build_utils} && %{without build_all}
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
%ifarch ppc ppc64
 %define optimize_power 1
 %ifarch ppc
 %define powerpc_optimize_base %{nil}
 %define powerpc_optimize_tune power3
 %define powerpc_optimize_cpu_power4 1
 %else
 %define powerpc_optimize_base %{nil}
 %define powerpc_optimize_tune power5
 %define powerpc_optimize_cpu_power4 0
 %endif
 # We are not building Power CPU specific optimizations for openSUSE.
 %define powerpc_optimize_cpu_power6 0
 %define powerpc_optimize_cpu_power7 0
 %define powerpc_optimize_cpu_cell 0
%else
 %define optimize_power 0
 %define powerpc_optimize_base %{nil}
 %define powerpc_optimize_cpu_power4 0
 %define powerpc_optimize_cpu_power6 0
 %define powerpc_optimize_cpu_power7 0
 %define powerpc_optimize_cpu_cell 0
%endif
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

Version:        2.32
Release:        0
%if !%{build_snapshot}
%define git_id 0a8262a1b2
%define libversion %version
%else
%define git_id %(echo %version | sed 's/.*\.g//')
%define libversion %(echo %version | sed 's/\.[^.]*\.g.*//')
%endif
URL:            http://www.gnu.org/software/libc/libc.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if !%{build_snapshot}
Source:         http://ftp.gnu.org/pub/gnu/glibc/glibc-%{version}.tar.xz
Source1:        http://ftp.gnu.org/pub/gnu/glibc/glibc-%{version}.tar.xz.sig
%else
Source:         glibc-%{version}.tar.xz
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

%if %{build_main}
# ngpt was used in 8.1 and SLES8
Obsoletes:      ngpt < 2.2.2
Obsoletes:      ngpt-devel < 2.2.2
Provides:       ngpt = 2.2.2
Provides:       ngpt-devel = 2.2.2
Conflicts:      kernel < %{enablekernel}
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
Provides:       rtld(GNU_HASH)
%endif
%if %{build_utils}
Requires:       glibc = %{version}
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#

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
# PATCH-FIX-OPENSUSE prefer -lang rpm packages
Patch15:        glibc-2.3.90-langpackdir.diff
# PATCH-FEATURE-SLE Use nscd user for nscd
Patch19:        nscd-server-user.patch
# PATCH-FEATURE-SLE read nsswich.conf from /usr
Patch20:        glibc-nsswitch-usr.diff

### Locale related patches
# PATCH-FIX-OPENSUSE Add additional locales
Patch100:       add-locales.patch
# PATCH-FIX-OPENSUSE -- Add no_NO back (XXX: Still needed?)
Patch102:       glibc-2.4.90-no_NO.diff
# PATCH-FIX-OPENSUSE -- Renames for China
Patch103:       glibc-2.4-china.diff
# PATCH-FIX-OPENSUSE -- Add C.UTF-8 locale
Patch104:       glibc-c-utf8-locale.patch
# PATCH-FIX-OPENSUSE -- Disable gettext for C.UTF-8 locale
Patch105:       glibc-disable-gettext-for-c-utf8.patch

### Network related patches
# PATCH-FIX-OPENSUSE Warn about usage of mdns in resolv.conv
Patch304:       glibc-resolv-mdnshint.diff
# PATCH-FIX-OPENSUSE disable rewriting ::1 to 127.0.0.1 for /etc/hosts bnc#684534, bnc#706719
Patch306:       glibc-fix-double-loopback.diff

###
# Patches from upstream
###
# PATCH-FIX-UPSTREAM Correct locking and cancellation cleanup in syslog functions (BZ #26100)
Patch1000:      syslog-locking.patch
# PATCH-FIX-UPSTREAM x86-64: Fix FMA4 detection in ifunc (BZ #26534)
Patch1001:      ifunc-fma4.patch

### 
# Patches awaiting upstream approval
###
# PATCH-FIX-UPSTREAM Always to locking when accessing streams (BZ #15142)
Patch2000:      fix-locking-in-_IO_cleanup.patch
# PATCH-FIX-UPSTREAM Avoid concurrency problem in ldconfig (BZ #23973)
Patch2001:      ldconfig-concurrency.patch
# PATCH-FIX-UPSTREAM Fix buffer overrun in EUC-KR conversion module (BZ #24973)
Patch2002:      euc-kr-overrun.patch
# PATCH-FIX-UPSTREAM nscd: bump GC cycle during cache pruning (BZ #26130)
Patch2003:      nscd-gc-cycle.patch

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
Requires(post): /bin/cat
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
Requires(pre):  shadow
%{?systemd_requires}

%description -n nscd
Nscd caches name service lookups and can dramatically improve
performance with NIS, NIS+, and LDAP.

%package profile
Summary:        Libc Profiling and Debugging Versions
License:        LGPL-2.1-or-later AND LGPL-2.1-or-later WITH GCC-exception-2.0 AND GPL-2.0-or-later
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

# makedb requires libselinux. We add this program in a separate
# package so that glibc does not require libselinux.
%package extra
Summary:        Extra binaries from GNU C Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       glibc = %{version}

%description extra
The glibc-extra package contains some extra binaries for glibc that
are not essential but recommend to use.

makedb: A program to create a database for nss

%lang_package
%endif

%prep
%setup -n glibc-%{version} -q -a 4
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch10 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch19 -p1
%patch20 -p1

%patch100 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1

%patch304 -p1
%patch306 -p1

%patch1000 -p1
%patch1001 -p1

%patch2000 -p1
%patch2001 -p1
%patch2002 -p1
%patch2003 -p1

%patch3000

#
# Inconsistency detected by ld.so: dl-close.c: 719: _dl_close: Assertion `map->l_init_called' failed!
#
# Glibc 2.8 introduced the HP_TIMING element to the rtld_global_ro struct # definition.
# If the base is built without power4 the loader won't have this element in
# the struct whereas the power4/5/6/... libc will, so there will be a disconnect
# between the size of the rtld_global_ro struct between the two and dl_close
# ends up getting called incorrectly when it's actually attempting to call a
# resolver function.  This is because the GLRO() macro simply attempts to
# compute an offset and gets the wrong one.
# Building the base glibc with --with-cpu=power4 solves this problem.
# But: ppc32 can not default to -mcpu=power4 because it would emit instructions
# which are not available on G3, G4 etc.
#
# We simply remove the power4 files, and build the base glibc for a generic powerpc cpu
# Additional cputuned libs can now be used on powerpc32
#
rm -fv sysdeps/powerpc/powerpc32/power4/hp-timing.c sysdeps/powerpc/powerpc32/power4/hp-timing.h
find . -name configure | xargs touch

%build
# Disable LTO due to a usage of top-level assembler that
#  causes LTO issues (boo#1138807).
%define _lto_cflags %{nil}
%if "%flavor" == "i686"
%global optflags %(echo "%optflags"|sed -e s/i586/i686/) -march=i686 -mtune=generic
%endif
if [ -x /bin/uname.bin ]; then
	/bin/uname.bin -a
else
	uname -a
fi
uptime || :
ulimit -a
nice
# We do not want configure to figure out the system its building one
# to support a common ground and thus set build and host to the
# target_cpu.
%ifarch %arm
%define target %{_target_cpu}-suse-linux-gnueabi
%else
%define target %{_target_cpu}-suse-linux
%endif
# Don't use as-needed, it breaks glibc assumptions
# Before enabling it, run the testsuite and verify that it
# passes completely
export SUSE_ASNEEDED=0
# Adjust glibc version.h
echo "#define CONFHOST \"%{target}\"" >> version.h
echo "#define GITID \"%{git_id}\"" >> version.h
#
# Default CFLAGS and Compiler
#
BuildFlags="%{optflags} -U_FORTIFY_SOURCE"
enable_stack_protector=
for opt in $BuildFlags; do
  case $opt in
    -fstack-protector-strong) enable_stack_protector=strong ;;
    -fstack-protector-all) enable_stack_protector=all ;;
    -fstack-protector) enable_stack_protector=yes ;;
  esac
done
BuildFlags=$(echo $BuildFlags | sed -e 's#-fstack-protector[^ ]*##' -e 's#-ffortify=[0-9]*##')
BuildCC="%__cc"
BuildCCplus="%__cxx"
#
#now overwrite for some architectures
#
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
%endif
%ifarch ppc64
	BuildCC="$BuildCC -m64"
	BuildCCplus="$BuildCCplus -m64"
%endif
%ifarch hppa
	BuildFlags="$BuildFlags -mpa-risc-1-1 -fstrict-aliasing"
%endif
# Add flags for all plattforms except AXP
%ifnarch alpha
	BuildFlags="$BuildFlags -g"
%endif
%if %{disable_assert}
	BuildFlags="$BuildFlags -DNDEBUG=1"
%endif
%ifarch mipsel
	# fails to build otherwise - need to recheck and fix
	%define enable_stackguard_randomization 0
%endif

configure_and_build_glibc() {
	local dirname="$1"; shift
	local cflags="$1"; shift
	mkdir "cc-$dirname"
	cd "cc-$dirname"
%ifarch %arm aarch64
	# remove asynchronous-unwind-tables during configure as it causes
	# some checks to fail spuriously on arm
	conf_cflags="${cflags/-fasynchronous-unwind-tables/}"
	conf_cflags="${conf_cflags/-funwind-tables/}"
%else
	conf_cflags="$cflags"
%endif

	profile="--disable-profile"
%if %{build_profile}
        if [ "$dirname" = "base" ] ; then
	    profile="--enable-profile"
	fi
%endif
	../configure \
		CFLAGS="$conf_cflags" BUILD_CFLAGS="$conf_cflags" \
		CC="$BuildCC" CXX="$BuildCCplus" \
		--prefix=%{_prefix} \
		--libexecdir=%{_libexecdir} --infodir=%{_infodir} \
	        $profile \
		"$@" \
		--build=%{target} --host=%{target} \
%ifarch armv7hl ppc ppc64 ppc64le i686 x86_64 sparc sparc64 s390 s390x
		--enable-multi-arch \
%endif
%ifarch mipsel
		--without-fp \
%endif
%ifarch ppc64p7
		--with-cpu=power7 \
%endif
%if %{enable_stackguard_randomization}
		--enable-stackguard-randomization \
%endif
		${enable_stack_protector:+--enable-stack-protector=$enable_stack_protector} \
		--enable-tunables \
		--enable-kernel=%{enablekernel} \
		--with-bugurl=http://bugs.opensuse.org \
		--enable-bind-now \
		--enable-systemtap \
		--disable-timezone-tools \
		--disable-crypt
	# explicitly set CFLAGS to use the full CFLAGS (not the reduced one for configure)
	make %{?_smp_mflags} CFLAGS="$cflags" BUILD_CFLAGS="$cflags"
	cd ..
}

%if !%{optimize_power}
	#
	# Build base glibc
	#
	configure_and_build_glibc base "$BuildFlags"
%else
	#
	# Build POWER-optimized glibc
	#
	# First, base build:
	pBuildFlags="$BuildFlags -mtune=%{powerpc_optimize_tune}"
	%if "%{powerpc_optimize_base}" != ""
	pBuildFlags+=" -mcpu=%{powerpc_optimize_base}"
	%endif
	%if "%{powerpc_optimize_base}" != ""
	configure_and_build_glibc base "$pBuildFlags" --with-cpu=%{powerpc_optimize_base}
	%else
	# Use no default CPU
	configure_and_build_glibc base "$pBuildFlags"
	%endif
	%if %{build_variants}
	# Then other power variants:
	for pcpu in \
	%if %{powerpc_optimize_cpu_power4}
		power4 \
	%endif
	%if %{powerpc_optimize_cpu_power6}
		power6 \
	%endif
	%if %{powerpc_optimize_cpu_power7}
		power7 \
	%endif
	; do
		configure_and_build_glibc $pcpu "$BuildFlags -mcpu=$pcpu" \
			--with-cpu=$pcpu
	done
	# Eventually, special Cell variant:
	%if %{powerpc_optimize_cpu_cell}
		configure_and_build_glibc ppc-cell-be "$BuildFlags -mcpu=cell"
	%endif
	%endif
%endif

#
# Build html documentation
#
%if %{build_html}
make %{?_smp_mflags} -C cc-base html
%endif

%check
%if %{build_testsuite}
# The testsuite will fail if asneeded is used
export SUSE_ASNEEDED=0
# Increase timeout
export TIMEOUTFACTOR=16
# The testsuite does its own malloc checking
unset MALLOC_CHECK_
make %{?_smp_mflags} -C cc-base -k check || {
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
make %{?_smp_mflags} -C cc-base check-abi
%endif

%install
%if !%{build_testsuite}
%ifarch riscv64
mkdir -p %{buildroot}%{_libdir}
ln -s . %{buildroot}%{_libdir}/lp64d
mkdir -p %{buildroot}/%{_lib}
ln -s . %{buildroot}/%{_lib}/lp64d
%endif
%endif

%if %{build_main}
# We don't want to strip the .symtab from our libraries in find-debuginfo.sh,
# certainly not from libpthread.so.* because it is used by libthread_db to find
# some non-exported symbols in order to detect if threading support
# should be enabled.  These symbols are _not_ exported, and we can't easily
# export them retroactively without changing the ABI.  So we have to
# continue to "export" them via .symtab, instead of .dynsym :-(
# But we also want to keep .symtab and .strtab of other libraries since some
# debugging tools currently require these sections directly inside the main
# files - specifically valgrind and PurifyPlus.
export STRIP_KEEP_SYMTAB=*.so*

# Install base glibc
make %{?_smp_mflags} install_root=%{buildroot} install -C cc-base

install_optimized_variant() {
	local dirname="$1"; shift
	local subdir="$1"; shift
	local subdir_up="$1"; shift

cd "cc-$dirname"
destdir=$RPM_BUILD_ROOT/%{_lib}/$subdir
mkdir -p $destdir
# Don't run a complete make install, we know which libraries
# we want
for lib in libc math/libm nptl/libpthread rt/librt nptl_db/libthread_db
do
  libbase=${lib#*/}
  libbaseso=$(basename $RPM_BUILD_ROOT/%{_lib}/${libbase}-*.so)
  # Only install if different from base lib
  if cmp -s ${lib}.so ../cc-base/${lib}.so; then
    ln -sf $subdir_up/$libbaseso $destdir/$libbaseso
  else
    cp -a ${lib}.so $destdir/$libbaseso
  fi
done
cd ..
cc-base/elf/ldconfig -vn $destdir
}

# Install power-optimized glibc
%if %{optimize_power}
	%if %{powerpc_optimize_cpu_power4}
	install_optimized_variant power4 power4 ".."
	%endif
	%if %{powerpc_optimize_cpu_power6}
	install_optimized_variant power6 power6 ".."
	%endif
	%if %{powerpc_optimize_cpu_power7}
	install_optimized_variant power7 power7 ".."
	%endif
	%if %{powerpc_optimize_cpu_cell}
	install_optimized_variant ppc-cell-be ppc-cell-be ".."
	%endif
	%if %{powerpc_optimize_cpu_power6}
	# power6 is compatible with power6x
	# doing a directory symlink doesnt work, ldconfig follows them and accepts only the first real dir
	if test -d %{buildroot}/%{_lib}/power6; then
	    mkdir -p %{buildroot}/%{_lib}/power6x
	    for i in %{buildroot}/%{_lib}/power6/*.so; do
		b=$(basename $i)
		ln -vs ../power6/$b %{buildroot}/%{_lib}/power6x/$b
	    done
	    cc-base/elf/ldconfig -vn %{buildroot}/%{_lib}/power6x
	fi
	%endif
%endif

# Install locales
%if %{build_locales}
	# XXX Do not install locales in parallel!
	cd cc-base
	# localedef creates hardlinks to other locales if possible
	# this will not work if we generate them in parallel.
	# thus we need to run fdupes on  /usr/lib/locale/
	# Still, on my system this is a speed advantage:
	# non-parallel build for install-locales: 9:34mins
	# parallel build with fdupes: 7:08mins
	make %{?_smp_mflags} install_root=%{buildroot} localedata/install-locales
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
install -m 644 %{SOURCE5} %{buildroot}/etc
%endif

mkdir -p %{buildroot}/etc/default
install -m 644 nis/nss %{buildroot}/etc/default/

mkdir -p %{buildroot}%{_includedir}/resolv
install -m 0644 resolv/mapv4v6addr.h %{buildroot}%{_includedir}/resolv/
install -m 0644 resolv/mapv4v6hostent.h %{buildroot}%{_includedir}/resolv/

%if %{build_html}
mkdir -p %{buildroot}%{_datadir}/doc/glibc
cp -p cc-base/manual/libc/*.html %{buildroot}%{_datadir}/doc/glibc
%endif

cd manpages; make install_root=%{buildroot} install; cd ..

# nscd tools:

%ifnarch i686
cp nscd/nscd.conf %{buildroot}/etc
mkdir -p %{buildroot}/etc/init.d
ln -sf /sbin/service %{buildroot}/usr/sbin/rcnscd
mkdir -p %{buildroot}/run/nscd
mkdir -p %{buildroot}/var/lib/nscd
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

rm -f %{buildroot}/sbin/sln

# Remove the buildflags tracking section and the build-id
for o in %{buildroot}/%{_libdir}/crt[1in].o %{buildroot}/%{_libdir}/lib*_nonshared.a; do
	objcopy -R ".comment.SUSE.OPTs" -R ".note.gnu.build-id" $o
done

%ifnarch i686
mkdir -p %{buildroot}/usr/lib/tmpfiles.d/
install -m 644 %{SOURCE20} %{buildroot}/usr/lib/tmpfiles.d/
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 644 %{SOURCE21} %{buildroot}/usr/lib/systemd/system
%endif

%ifarch armv6hl armv7hl
# Provide compatibility link
ln -s ld-%{libversion}.so %{buildroot}/lib/ld-linux.so.3
%endif

# Move getconf to %{_libexecdir}/getconf/ to avoid cross device link
mv %{buildroot}%{_bindir}/getconf %{buildroot}%{_libexecdir}/getconf/getconf
ln -s %{_libexecdir}/getconf/getconf %{buildroot}%{_bindir}/getconf

%if !%{build_utils}
# Remove unwanted files (packaged in glibc-utils)
rm -f %{buildroot}/%{_lib}/libmemusage*
rm -f %{buildroot}/%{_lib}/libpcprofile*
rm -f %{buildroot}%{_bindir}/memusage*
rm -f %{buildroot}%{_bindir}/mtrace
rm -f %{buildroot}%{_bindir}/pcprofiledump
rm -f %{buildroot}%{_bindir}/sotruss
rm -f %{buildroot}%{_bindir}/xtrace
rm -f %{buildroot}%{_bindir}/pldd
rm -rf %{buildroot}%{_libdir}/audit

%ifarch i686
# Remove files from glibc-{extra,info,i18ndata} and nscd
rm -rf %{buildroot}%{_infodir} %{buildroot}%{_prefix}/share/i18n
rm -f %{buildroot}%{_bindir}/makedb %{buildroot}/var/lib/misc/Makefile
rm -f %{buildroot}%{_sbindir}/nscd
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
ln -sf /%{_lib}/ld-linux.so.2 $RPM_BUILD_ROOT/%{_lib}/ld-lsb.so.3
%endif
%ifarch x86_64
ln -sf /%{_lib}/ld-linux-x86-64.so.2 $RPM_BUILD_ROOT/%{_lib}/ld-lsb-x86-64.so.3
%endif
%ifarch ppc
ln -sf /%{_lib}/ld.so.1 $RPM_BUILD_ROOT/%{_lib}/ld-lsb-ppc32.so.3
%endif
%ifarch ppc64
ln -sf /%{_lib}/ld64.so.1 $RPM_BUILD_ROOT/%{_lib}/ld-lsb-ppc64.so.3
%endif
%ifarch s390
ln -sf /%{_lib}/ld.so.1 $RPM_BUILD_ROOT/%{_lib}/ld-lsb-s390.so.3
%endif
%ifarch s390x
ln -sf /%{_lib}/ld64.so.1 $RPM_BUILD_ROOT/%{_lib}/ld-lsb-s390x.so.3
%endif

%else

%if %{build_utils}

make %{?_smp_mflags} install_root=%{buildroot} install -C cc-base \
  subdirs='malloc debug elf'
cd manpages; make install_root=%{buildroot} install; cd ..
# Remove unwanted files
rm -f %{buildroot}/%{_lib}/ld*.so* %{buildroot}/%{_lib}/lib[!mp]*
rm -f %{buildroot}/lib/ld*.so*
rm -f %{buildroot}%{_libdir}/lib*
rm -f %{buildroot}%{_bindir}/{catchsegv,ldd*,sprof}
rm -rf %{buildroot}%{_mandir}/man*
rm -rf %{buildroot}/sbin %{buildroot}%{_includedir}
%ifarch riscv64
rm %{buildroot}/%{_lib}/lp64d %{buildroot}%{_libdir}/lp64d
%endif

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
  "/%{_lib}/i686/",
%endif
%ifarch ppc ppc64
%if !%{powerpc_optimize_cpu_power4}
  "/%{_lib}/power4/", "/%{_lib}/ppc970/",
%endif
  "/%{_lib}/power5/", "/%{_lib}/power5+/",
%if !%{powerpc_optimize_cpu_power6}
  "/%{_lib}/power6/", "/%{_lib}/power6x/",
%endif
%if !%{powerpc_optimize_cpu_power7}
  "/%{_lib}/power7/",
%endif
%if !%{powerpc_optimize_cpu_cell}
  "/%{_lib}/ppc-cell-be/",
%endif
%endif
  "/%{_lib}/tls/"
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
if posix.access("/sbin/ldconfig", "x") then
  exec("/sbin/ldconfig", "-X")
end
if posix.utime("%{_libdir}/gconv/gconv-modules.cache") then
  exec("/usr/sbin/iconvconfig", "-o", "%{_libdir}/gconv/gconv-modules.cache",
       "--nostdlib", "%{_libdir}/gconv")
end

%postun -p /sbin/ldconfig

%post locale-base
/usr/sbin/iconvconfig

%post info
%install_info --info-dir=%{_infodir} %{_infodir}/libc.info.gz

%preun info
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libc.info.gz

%pre -n nscd
getent group nscd >/dev/null || %{_sbindir}/groupadd -r nscd
getent passwd nscd >/dev/null || %{_sbindir}/useradd -r -g nscd -c "User for nscd" -s /sbin/nologin -d /run/nscd nscd
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
%config(noreplace) /etc/default/nss
%doc %{_mandir}/man1/gencat.1.gz
%doc %{_mandir}/man1/getconf.1.gz
%doc %{_mandir}/man5/*
/%{_lib}/ld-%{libversion}.so

# Each architecture has a different name for the dynamic linker:
%ifarch %arm
%ifarch armv6hl armv7hl
/%{_lib}/ld-linux-armhf.so.3
# Keep compatibility link
/%{_lib}/ld-linux.so.3
%else
/%{_lib}/ld-linux.so.3
%endif
%endif
%ifarch ia64
/%{_lib}/ld-linux-ia64.so.2
%endif
%ifarch ppc s390 mips hppa m68k
/%{_lib}/ld.so.1
%endif
%ifarch ppc64
/%{_lib}/ld64.so.1
%endif
%ifarch ppc64le
/%{_lib}/ld64.so.2
%endif
%ifarch s390x
/lib/ld64.so.1
/%{_lib}/ld64.so.1
%endif
%ifarch x86_64
/%{_lib}/ld-linux-x86-64.so.2
%endif
%ifarch %ix86 %sparc
/%{_lib}/ld-linux.so.2
%endif
%ifarch aarch64
/lib/ld-linux-aarch64.so.1
/%{_lib}/ld-linux-aarch64.so.1
%endif
%ifarch riscv64
/lib/ld-linux-riscv64-lp64d.so.1
/%{_lib}/ld-linux-riscv64-lp64d.so.1
/%{_lib}/lp64d
%{_libdir}/lp64d
%endif
%ifarch %ix86 x86_64 ppc ppc64 s390 s390x
# LSB
/%{_lib}/*-lsb*.so.3
%endif

/%{_lib}/libBrokenLocale-%{libversion}.so
/%{_lib}/libBrokenLocale.so.1
/%{_lib}/libSegFault.so
/%{_lib}/libanl-%{libversion}.so
/%{_lib}/libanl.so.1
/%{_lib}/libc-%{libversion}.so
/%{_lib}/libc.so.6*
/%{_lib}/libdl-%{libversion}.so
/%{_lib}/libdl.so.2*
/%{_lib}/libm-%{libversion}.so
/%{_lib}/libm.so.6*
%ifarch x86_64
/%{_lib}/libmvec-%{libversion}.so
/%{_lib}/libmvec.so.1
%endif
/%{_lib}/libnsl-%{libversion}.so
/%{_lib}/libnsl.so.1
/%{_lib}/libnss_compat-%{libversion}.so
/%{_lib}/libnss_compat.so.2
/%{_lib}/libnss_db-%{libversion}.so
/%{_lib}/libnss_db.so.2
/%{_lib}/libnss_dns-%{libversion}.so
/%{_lib}/libnss_dns.so.2
/%{_lib}/libnss_files-%{libversion}.so
/%{_lib}/libnss_files.so.2
/%{_lib}/libnss_hesiod-%{libversion}.so
/%{_lib}/libnss_hesiod.so.2
/%{_lib}/libpthread-%{libversion}.so
/%{_lib}/libpthread.so.0
/%{_lib}/libresolv-%{libversion}.so
/%{_lib}/libresolv.so.2
/%{_lib}/librt-%{libversion}.so
/%{_lib}/librt.so.1
/%{_lib}/libthread_db-1.0.so
/%{_lib}/libthread_db.so.1
/%{_lib}/libutil-%{libversion}.so
/%{_lib}/libutil.so.1
%define optimized_libs() \
	%dir %attr(0755,root,root) /%{_lib}/%1\
	/%{_lib}/%1/libc-%{libversion}.so\
	/%{_lib}/%1/libc.so.6*\
	/%{_lib}/%1/libm-%{libversion}.so\
	/%{_lib}/%1/libm.so.6*\
	/%{_lib}/%1/libpthread-%{libversion}.so\
	/%{_lib}/%1/libpthread.so.0\
	/%{_lib}/%1/librt-%{libversion}.so\
	/%{_lib}/%1/librt.so.1\
	/%{_lib}/%1/libthread_db-1.0.so\
	/%{_lib}/%1/libthread_db.so.1

%if %{optimize_power}
	%if %{powerpc_optimize_cpu_power4}
		%{optimized_libs power4}
	%endif
	%if %{powerpc_optimize_cpu_power6}
		%{optimized_libs power6}
		%{optimized_libs power6x}
	%endif
	%if %{powerpc_optimize_cpu_power7}
		%{optimized_libs power7}
	%endif
	%if %{powerpc_optimize_cpu_cell}
		%{optimized_libs ppc-cell-be}
	%endif
%endif
%dir %attr(0700,root,root) /var/cache/ldconfig
/sbin/ldconfig
%{_bindir}/gencat
%{_bindir}/getconf
%{_bindir}/getent
%{_bindir}/iconv
%attr(755,root,root) %{_bindir}/ldd
%ifarch %ix86 sparc sparcv9 m68k
	%{_bindir}/lddlibc4
%endif
%{_bindir}/locale
%{_bindir}/localedef
%dir %attr(0755,root,root) %{_libexecdir}/getconf
%{_libexecdir}/getconf/*
%{_sbindir}/iconvconfig

%files locale-base
%defattr(-,root,root)
%{_datadir}/locale/locale.alias
%if %{build_locales}
%dir %{_prefix}/lib/locale
%{_prefix}/lib/locale/C.utf8
%{_prefix}/lib/locale/en_US.utf8
%endif
%dir %{_libdir}/gconv
%{_libdir}/gconv/*.so
%{_libdir}/gconv/gconv-modules
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %{_libdir}/gconv/gconv-modules.cache

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
%doc %{_mandir}/man1/catchsegv.1.gz
%doc %{_mandir}/man3/*
%{_bindir}/catchsegv
%{_bindir}/sprof
%{_includedir}/*
%{_libdir}/*.o
%{_libdir}/*.so
# These static libraries are needed even for shared builds
%{_libdir}/libc_nonshared.a
%{_libdir}/libg.a
%ifarch ppc ppc64 ppc64le s390 s390x sparc sparcv8 sparcv9 sparcv9v
# This is not built on sparc64.
	%{_libdir}/libnldbl_nonshared.a
%endif
%{_libdir}/libmcheck.a

%files devel-static
%defattr(-,root,root)
%{_libdir}/libBrokenLocale.a
%{_libdir}/libanl.a
%{_libdir}/libc.a
%{_libdir}/libdl.a
%{_libdir}/libm.a
%ifarch x86_64
%{_libdir}/libm-%{libversion}.a
%{_libdir}/libmvec.a
%endif
%{_libdir}/libpthread.a
%{_libdir}/libresolv.a
%{_libdir}/librt.a
%{_libdir}/libutil.a

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

%files -n nscd
%defattr(-,root,root)
%config(noreplace) /etc/nscd.conf
%{_sbindir}/nscd
%{_sbindir}/rcnscd
/usr/lib/systemd/system/nscd.service
%dir /usr/lib/tmpfiles.d
/usr/lib/tmpfiles.d/nscd.conf
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

%if %{build_profile}
%files profile
%defattr(-,root,root)
%{_libdir}/libc_p.a
%{_libdir}/libBrokenLocale_p.a
%{_libdir}/libanl_p.a
%{_libdir}/libm_p.a
%ifarch x86_64
%{_libdir}/libmvec_p.a
%endif
%{_libdir}/libpthread_p.a
%{_libdir}/libresolv_p.a
%{_libdir}/librt_p.a
%{_libdir}/libutil_p.a
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

%endif

%if %{build_utils}
%files -n glibc-utils
%defattr(-,root,root)
/%{_lib}/libmemusage.so
/%{_lib}/libpcprofile.so
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
