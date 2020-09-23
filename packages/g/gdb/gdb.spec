#
# spec file for package gdb
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012 RedHat
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


%define flavor @BUILD_FLAVOR@%{nil}

%bcond_with ringdisabled

%if "%flavor" == "testsuite"
%if %{with ringdisabled}
ExclusiveArch:  do_not_build
%endif
%if 0%{?qemu_user_space_build}
# In a qemu_user_space_build ptrace is not supported, so we can't test gdb.
ExclusiveArch:  do_not_build
%endif
%define build_main 0
%define build_testsuite 1
%else
%define build_main 1
%define build_testsuite 0
%endif

%if %{build_testsuite}
%define debug_package %{nil}
%endif

%if %{build_main}
%define name_suffix %{nil}
%else
%if %{build_testsuite}
%define name_suffix -testresults
%else
%define name_suffix -%{flavor}
%endif
%endif

%bcond_without fpc

%if %{build_main}
Summary:        A GNU source-level debugger for C, C++, Fortran and other languages
License:        GPL-3.0-or-later AND GPL-3.0-with-GCC-exception AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Group:          Development/Tools/Debuggers
%endif
%if %{build_testsuite}
Summary:        GDB testsuite results
License:        SUSE-Public-Domain
Group:          Development/Languages/C and C++
%endif
Name:           gdb%{name_suffix}

Version:        9.2
Release:        0

# The release always contains a leading reserved number, start it at 1.
# `upstream' is not a part of `name' to stay fully rpm dependencies compatible for the testing.

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Do not provide URL for snapshots as the file lasts there only for 2 days.
# ftp://sourceware.org/pub/gdb/releases/gdb-%%{version}.tar.gz
Source:         gdb-%{version}.tar.bz2
URL:            http://gnu.org/software/gdb/

%if "%{scl}" == "devtoolset-1.1"
Obsoletes:      devtoolset-1.0-%{pkg_name}
%endif

# For our convenience
%global gdb_src gdb-%{version}
%global gdb_build build-%{_target_platform}
%global gdb_docdir %{_docdir}/gdb-doc

%global have_inproctrace 0
%ifarch %{ix86} x86_64
%global have_inproctrace 1
%endif # %%{ix86} x86_64

# Choose python version
%if 0%{?suse_version} >= 1320
%define python python3
%else
%define python python
%endif

# GDB patches have the format `gdb-<version>-bz<red-hat-bz-#>-<desc>.patch'.
# They should be created using patch level 1: diff -up ./gdb (or gdb-6.3/gdb).

#=
#push=Should be pushed upstream.
#maybepush=Should be pushed upstream unless it got obsoleted there.
#fedora=Should stay as a Fedora patch.
#ia64=Drop after RHEL-5 rebases and rebuilds are no longer meaningful.
#fedoratest=Keep it in Fedora only as a regression test safety.
#+ppc=Specific for ppc32/ppc64/ppc*
#+work=Requires some nontrivial work.

# Cleanup any leftover testsuite processes as it may stuck mock(1) builds.
#=push
Source2:        gdb-orphanripper.c

# Man page for gstack(1).
#=push
Source3:        gdb-gstack.man

# /etc/gdbinit (from Debian but with Fedora compliant location).
#=fedora
Source4:        gdbinit
Source5:        gdbinit.without-python

# libipt: Intel Processor Trace Decoder Library
%global libipt_version 2.0.1
Source7:        v%{libipt_version}.tar.gz

# Infrastructure to sync patches from the Fedora rpm
Source10:       patchlist.pl
Source11:       patchname_get.sh
Source12:       baselibs.conf
Source13:       gdb-rpmlintrc
%if %{build_testsuite}
NoSource:       0
NoSource:       2
NoSource:       3
NoSource:       4
NoSource:       5
NoSource:       7
NoSource:       10
NoSource:       11
NoSource:       12
NoSource:       13
%endif

#Fedora Packages begin
Patch2:         gdb-vla-intel-fortran-strides.patch
Patch3:         gdb-vla-intel-fortran-vla-strings.patch
Patch4:         gdb-vla-intel-stringbt-fix.patch
Patch5:         gdb-6.3-gstack-20050411.patch
Patch6:         gdb-6.3-test-pie-20050107.patch
Patch7:         gdb-6.3-test-self-20050110.patch
Patch8:         gdb-6.3-test-dtorfix-20050121.patch
Patch9:         gdb-6.3-test-movedir-20050125.patch
Patch10:        gdb-6.3-threaded-watchpoints2-20050225.patch
Patch11:        gdb-6.3-inferior-notification-20050721.patch
Patch12:        gdb-6.3-inheritancetest-20050726.patch
Patch13:        gdb-6.5-bz185337-resolve-tls-without-debuginfo-v2.patch
Patch14:        gdb-6.5-sharedlibrary-path.patch
Patch15:        gdb-6.5-BEA-testsuite.patch
Patch16:        gdb-6.5-last-address-space-byte-test.patch
Patch17:        gdb-6.5-readline-long-line-crash-test.patch
Patch18:        gdb-6.5-bz218379-ppc-solib-trampoline-test.patch
Patch19:        gdb-6.5-bz218379-solib-trampoline-lookup-lock-fix.patch
Patch20:        gdb-6.5-bz109921-DW_AT_decl_file-test.patch
Patch21:        gdb-6.3-bz140532-ppc-unwinding-test.patch
Patch22:        gdb-6.3-bz202689-exec-from-pthread-test.patch
Patch23:        gdb-6.6-bz230000-power6-disassembly-test.patch
Patch24:        gdb-6.6-bz229517-gcore-without-terminal.patch
Patch25:        gdb-6.6-testsuite-timeouts.patch
Patch26:        gdb-6.6-bz237572-ppc-atomic-sequence-test.patch
Patch27:        gdb-6.3-attach-see-vdso-test.patch
Patch28:        gdb-6.5-bz243845-stale-testing-zombie-test.patch
Patch29:        gdb-6.6-buildid-locate.patch
Patch30:        gdb-6.6-buildid-locate-solib-missing-ids.patch
Patch31:        gdb-6.6-buildid-locate-rpm.patch
Patch32:        gdb-6.7-charsign-test.patch
Patch33:        gdb-6.7-ppc-clobbered-registers-O2-test.patch
Patch34:        gdb-6.7-testsuite-stable-results.patch
Patch35:        gdb-6.5-ia64-libunwind-leak-test.patch
Patch36:        gdb-6.5-missed-trap-on-step-test.patch
Patch37:        gdb-6.5-gcore-buffer-limit-test.patch
Patch38:        gdb-6.3-mapping-zero-inode-test.patch
Patch39:        gdb-6.3-focus-cmd-prev-test.patch
Patch40:        gdb-6.8-bz442765-threaded-exec-test.patch
Patch41:        gdb-6.5-section-num-fixup-test.patch
Patch42:        gdb-6.8-bz466901-backtrace-full-prelinked.patch
Patch43:        gdb-simultaneous-step-resume-breakpoint-test.patch
Patch44:        gdb-core-open-vdso-warning.patch
Patch45:        gdb-bz533176-fortran-omp-step.patch
Patch46:        gdb-ccache-workaround.patch
Patch47:        gdb-archer-pie-addons.patch
Patch48:        gdb-archer-pie-addons-keep-disabled.patch
Patch49:        gdb-lineno-makeup-test.patch
Patch50:        gdb-ppc-power7-test.patch
Patch51:        gdb-moribund-utrace-workaround.patch
Patch52:        gdb-archer-next-over-throw-cxx-exec.patch
Patch53:        gdb-bz601887-dwarf4-rh-test.patch
Patch54:        gdb-6.6-buildid-locate-core-as-arg.patch
Patch55:        gdb-6.6-buildid-locate-rpm-librpm-workaround.patch
Patch56:        gdb-test-bt-cfi-without-die.patch
Patch57:        gdb-bz634108-solib_address.patch
Patch58:        gdb-test-pid0-core.patch
Patch59:        gdb-test-dw2-aranges.patch
Patch60:        gdb-test-expr-cumulative-archer.patch
Patch61:        gdb-physname-pr11734-test.patch
Patch62:        gdb-physname-pr12273-test.patch
Patch63:        gdb-test-ivy-bridge.patch
Patch64:        gdb-runtest-pie-override.patch
Patch65:        gdb-attach-fail-reasons-5of5.patch
Patch66:        gdb-glibc-strstr-workaround.patch
Patch67:        gdb-rhel5.9-testcase-xlf-var-inside-mod.patch
Patch68:        gdb-rhbz-818343-set-solib-absolute-prefix-testcase.patch
Patch69:        gdb-rhbz947564-findvar-assertion-frame-failed-testcase.patch
Patch70:        gdb-gnat-dwarf-crash-3of3.patch
Patch71:        gdb-rhbz1007614-memleak-infpy_read_memory-test.patch
Patch73:        gdb-archer-vla-tests.patch
Patch74:        gdb-vla-intel-tests.patch
Patch75:        gdb-btrobust.patch
Patch76:        gdb-fortran-frame-string.patch
Patch77:        gdb-rhbz1156192-recursive-dlopen-test.patch
Patch78:        gdb-jit-reader-multilib.patch
Patch79:        gdb-rhbz1149205-catch-syscall-after-fork-test.patch
Patch80:        gdb-rhbz1186476-internal-error-unqualified-name-re-set-test.patch
Patch81:        gdb-rhbz1350436-type-printers-error.patch
Patch82:        gdb-rhbz1084404-ppc64-s390x-wrong-prologue-skip-O2-g-3of3.patch
Patch83:        gdb-bz1219747-attach-kills.patch
Patch84:        gdb-fedora-libncursesw.patch
Patch85:        gdb-opcodes-clflushopt-test.patch
Patch86:        gdb-dts-rhel6-python-compat.patch
Patch87:        gdb-6.6-buildid-locate-rpm-scl.patch
Patch88:        gdb-6.8-quit-never-aborts.patch
Patch89:        gdb-rhbz1261564-aarch64-hw-watchpoint-test.patch
Patch90:        gdb-container-rh-pkg.patch
Patch91:        gdb-rhbz1325795-framefilters-test.patch
Patch92:        gdb-linux_perf-bundle.patch
Patch94:        gdb-rhbz1398387-tab-crash-test.patch
Patch95:        gdb-archer.patch
Patch96:        gdb-vla-intel-fix-print-char-array.patch
Patch97:        gdb-rhbz1553104-s390x-arch12-test.patch
Patch98:        gdb-rhbz1818011-bfd-gcc10-error.patch
#Fedora Packages end

# Fedora Packages not copied:
# - gdb-libexec-add-index.patch
# - gdb-6.3-rh-testversion-20041202.patch
# - gdb-6.6-buildid-locate-misleading-warning-missing-debuginfo-rhbz981154.patch

# Fedora patches fixup

Patch500:       gdb-testsuite-avoid-pagination-in-attach-32.exp.patch
Patch501:       gdb-testsuite-fix-perror-in-gdb.opt-fortran-string.exp.patch

# openSUSE specific

Patch1000:      gdb-gcore-bash.patch
Patch1002:      gdb-6.6-buildid-locate-rpm-suse.patch
Patch1003:      gdb-testsuite-ada-pie.patch

# Patches to upstream
Patch1500:      gdb-fix-debug-agent-odr-bool-int.patch
Patch1501:      gdbserver-fix-build-with-make-3.81.patch

# Backports from master

Patch2018:      gdb-fix-toplevel-types-with-fdebug-types-section.patch
Patch2019:      gdb-fix-range-loop-index-in-find_method.patch
Patch2020:      gdb-fix-python3.9-related-runtime-problems.patch
Patch2021:      gdb-fix-unused-function-error.patch
Patch2022:      gdb-fix-the-thread-pool.c-compilation.patch
Patch2023:      gdb-aarch64-fix-erroneous-use-of-spu-architecture-bfd.patch

# Proposed patch for PR threads/25478
Patch2502:      gdb-threads-fix-hang-in-stop_all_threads-after-killing-inferior.patch

# Testsuite patches

# -

# libipt support
Patch3000:      v1.5-libipt-static.patch

BuildRequires:  bison
BuildRequires:  flex
%if 0%{suse_version} > 1110
%define gcc gcc
%else
%define gcc gcc48
%endif
BuildRequires:  %{gcc}
BuildRequires:  %{gcc}-c++
BuildRequires:  gettext
BuildRequires:  glibc-devel
%if 0%{suse_version} > 1110 && 0%{suse_version} < 1330
# GDB supports guile 2.0, but not guile 2.2 (swo#21104).  Disable guile
# support for newer distro versions in anticipation of a move to guile 2.2.
BuildRequires:  guile-devel
%endif
BuildRequires:  libexpat-devel
%if 0%{suse_version} >= 1200
BuildRequires:  makeinfo
%else
BuildRequires:  texinfo
%endif
BuildRequires:  expect
BuildRequires:  mpfr-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  readline-devel
BuildRequires:  rpm-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
%if 0%{!?_without_python:1}
Requires:       %{python}-base
BuildRequires:  %{python}-devel
%endif	# 0%{!?_without_python:1}

%global have_libipt 0
%if 0%{suse_version} > 1110
%ifarch %{ix86} x86_64
%global have_libipt 1
BuildRequires:  cmake
%endif
%endif

# BuildArch would break RHEL-5 by overriding arch and not building noarch.
%if 0%{?el5:1}
ExclusiveArch:  noarch i386 x86_64 ppc ppc64 ia64 s390 s390x
%endif # 0%{?el5:1}

%ifarch s390x
%if %{suse_version} > 1500
BuildRequires:  babeltrace-devel
%endif
%endif
%ifarch ppc64
%if %{suse_version} >= 1500
BuildRequires:  babeltrace-devel
%endif
%endif
%ifarch %{ix86} x86_64
%if %{suse_version} >= 1200
BuildRequires:  babeltrace-devel
%endif
%endif
%ifarch aarch64 riscv64
BuildRequires:  babeltrace-devel
%endif

%if %{build_testsuite}

# Copied from gcc9/gcc.spec.in
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

# Ensure the devel libraries are installed for both multilib arches.
%global bits_local %{?_isa}
%global bits_other %{?_isa}
%if 0%{!?el5:1}
%ifarch s390x
%global bits_other (%{__isa_name}-32)
%else #!s390x
%ifarch ppc
%global bits_other (%{__isa_name}-64)
%else #!ppc
%ifarch sparc64 ppc64 s390x x86_64
%global bits_other (%{__isa_name}-32)
%endif #sparc64 ppc64 s390x x86_64
%endif #!ppc
%endif #!s390x
%endif #!el5

BuildRequires:  dejagnu
BuildRequires:  sharutils
# gcc-objc++ is not covered by the GDB testsuite.
BuildRequires:  %{gcc}-fortran
%if 0%{?gcc_version} < 7 && 0%{suse_version} > 1110
BuildRequires:  %{gcc}-java
%endif
BuildRequires:  %{gcc}-objc
%ifarch %ada_arch
BuildRequires:  %{gcc}-ada
%endif
%if 0%{!?disable_32bit:1}
# openSUSE for s390x doesn't build 32bit libs
%if 0%{suse_version} > 1110
%ifarch x86_64 ppc64 s390x
%if 0%{suse_version} >= 1330
# Older distros miss this pseudo package, the Ada
# testsuite won't work completely
BuildRequires:  %{gcc}-ada-32bit
%endif
BuildRequires:  %{gcc}-c++-32bit
%if 0%{suse_version} >= 1210 && 0%{suse_version} != 1315
BuildRequires:  glibc-devel-static-32bit
%endif
%endif
%endif
%endif
%if 0%{suse_version} >= 1210
BuildRequires:  glibc-devel-static
%endif
%if 0%{?suse_version} > 1500
# The gccgo command is used by make check for some gdb.go test-cases, so we
# need the gcc-go package.  However, the gccgo command was missing from the
# gcc-go package (bsc#1096677), so we only require it for known fixed
# versions.
BuildRequires:  gcc-go
%endif
%if 0%{?suse_version} >= 1500 && 0%{?is_opensuse}
%ifarch %{ix86} x86_64 aarch64 armv7l
%if %{with fpc}
BuildRequires:  fpc
%endif
%endif
%endif
%if 0%{?suse_version} >= 1200
%ifnarch s390
# s390 (for SLE12) doesn't have valgrind
BuildRequires:  valgrind
%endif
%endif

%ifarch s390x
%if 0%{?suse_version} >= 1500
# s390x (for SLE12 and earlier) doesn't have binutils-gold
BuildRequires:  binutils-gold
%endif
%else
BuildRequires:  binutils-gold
%endif

%if 0%{?suse_version} >= 1200
BuildRequires:  systemtap-sdt-devel
%endif

%endif # %%{build_testsuite}

%ifarch ia64
BuildRequires:  libunwind-devel
Requires:       libunwind
%endif

%if %{build_main}

%description
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Java, and other languages, by executing them in a controlled fashion
and printing their data.

%ifnarch riscv64
%package -n gdbserver
Summary:        A standalone server for GDB (the GNU source-level debugger)
License:        GPL-3.0-or-later AND GPL-3.0-with-GCC-exception AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Group:          Development/Tools/Debuggers

%description -n gdbserver
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Java, and other languages, by executing them in a controlled fashion
and printing their data.

This package provides a program that allows you to run GDB on a different
machine than the one which is running the program being debugged.
%endif

%package doc
Summary:        Documentation for GDB (the GNU source-level debugger)
License:        GFDL-1.3-only
Group:          Documentation/Other
PreReq:         %{install_info_prereq}

%if "%{scl}" == "devtoolset-1.1"
Obsoletes:      devtoolset-1.0-%{pkg_name}-doc
%endif

%description doc
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Java, and other languages, by executing them in a controlled fashion
and printing their data.

This package provides INFO, HTML and PDF user manual for GDB.
%endif

%if %{build_testsuite}
%description
Results from running the GDB testsuite. 
%endif

%prep
%setup -q -n %{gdb_src}

%if 0%{?rhel:1} && 0%{?rhel} <= 6
# libstdc++ pretty printers.
tar xjf %{SOURCE5}
%endif # 0%{?rhel:1} && 0%{?rhel} <= 6

# Files have `# <number> <file>' statements breaking VPATH / find-debuginfo.sh .
rm -f gdb/ada-exp.c gdb/ada-lex.c gdb/c-exp.c gdb/cp-name-parser.c gdb/f-exp.c
rm -f gdb/jv-exp.c gdb/m2-exp.c gdb/objc-exp.c gdb/p-exp.c gdb/go-exp.c

# *.info* is needlessly split in the distro tar; also it would not get used as
# we build in %%{gdb_build}, just to be sure.
find -name "*.info*"|xargs rm -f

#Fedora patching start
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
#Fedora patching end

%patch500 -p1
%patch501 -p1

%patch1000 -p1
%patch1002 -p1
%patch1003 -p1

%patch1500 -p1
%patch1501 -p1

%patch2018 -p1
%patch2019 -p1
%patch2020 -p1
%patch2021 -p1
%patch2022 -p1
%patch2023 -p1

%patch2502 -p1

#unpack libipt
%if 0%{have_libipt}
tar xzf %{SOURCE7}
(
 cd processor-trace-%{libipt_version}
%patch3000 -p1
)
%endif

find -name "*.orig" | xargs rm -f
! find -name "*.rej" # Should not happen.

# Remove the info and other generated files added by the FSF release
# process.
rm -f libdecnumber/gstdint.h
rm -f bfd/doc/*.info
rm -f bfd/doc/*.info-*
rm -f gdb/doc/*.info
rm -f gdb/doc/*.info-*

%build

# Identify the build directory with the version of gdb as well as the
# architecture, to allow for mutliple versions to be installed and
# built.
# Initially we're in the %%{gdb_src} directory.

for fprofile in %{?_with_profile:-fprofile} ""
do

mkdir %{gdb_build}$fprofile
cd %{gdb_build}$fprofile

%if 0%{suse_version} > 1110
CC=gcc
CXX=g++
%else
CC=gcc-4.8
CXX=g++-4.8
%endif
export CC
export CXX
export CFLAGS="$RPM_OPT_FLAGS"

# Add your -Wno-x/-Wno-error=y options here:
for opt in -Wno-error=odr; do
  # checking for acceptance of -Wno-foo is a bit wieldy: GCC doesn't 
  # warn about unknown -Wno- flags, _except_ if there are other
  # diagnostics as well, so let's force an uninitialized use warning
  # and grep for the diagnostic about the -Wno flag:
  if ! echo "int foo(void) { int a; return a;} " | \
     $CC  -x c -c - -o /dev/null -W ${opt} 2>&1 | \
     grep -E "Wno|no option" >/dev/null; then
    CFLAGS="$CFLAGS ${opt}"
  fi
done
%if %{have_libipt}
CFLAGS="$CFLAGS -DPERF_ATTR_SIZE_VER5_BUNDLE"
(
 mkdir processor-trace-%{libipt_version}-root
 mkdir processor-trace-%{libipt_version}-build
 cd    processor-trace-%{libipt_version}-build
 # -DPTUNIT:BOOL=ON has no effect on ctest.
 cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DBUILD_SHARED_LIBS=OFF \
        -DPTUNIT:BOOL=OFF \
        -DDEVBUILD:BOOL=ON \
        ../../processor-trace-%{libipt_version}
 make VERBOSE=1 %{?_smp_mflags}
 ctest -V %{?_smp_mflags}
 make install DESTDIR=../processor-trace-%{libipt_version}-root
)
# There is also: --with-libipt-prefix
CFLAGS="$CFLAGS -I$PWD/processor-trace-%{libipt_version}-root%{_includedir}"
LDFLAGS="$LDFLAGS -L$PWD/processor-trace-%{libipt_version}-root%{_libdir}"
%endif

export CXXFLAGS="$CFLAGS"

export LIBRPM=$(ldd /bin/rpm \
		    | grep librpm.so \
		    | awk '{print $3}')
if [ "$LIBRPM" != "" ]; then
    [ -f "$LIBRPM" ]
else
    export LIBRPM=no
fi

%ifarch %ix86 ia64 ppc ppc64 ppc64le s390 s390x x86_64 aarch64 riscv64
%define build_multitarget 1
%else
%define build_multitarget 0
%endif
%define target_list i686 powerpc powerpc64 powerpc64le s390 s390x x86_64 arm aarch64 m68k ia64 riscv64
%define DIST %(echo '%distribution' | sed 's, /.*,,')
%if %build_multitarget
EXTRA_TARGETS="%(printf ,%%s-suse-linux %target_list)"
EXTRA_TARGETS="$EXTRA_TARGETS,spu-elf"
%else
EXTRA_TARGETS=
%endif

../configure							\
	--prefix=%{_prefix}					\
	--libdir=%{_libdir}					\
	--sysconfdir=%{_sysconfdir}				\
	--mandir=%{_mandir}					\
	--infodir=%{_infodir}					\
	--htmldir=%{gdb_docdir}					\
	--pdfdir=%{gdb_docdir}					\
	--with-system-gdbinit=%{_sysconfdir}/gdbinit		\
	--with-gdb-datadir=%{_datadir}/gdb			\
	--enable-gdb-build-warnings=,-Wno-unused		\
%ifnarch %{ix86} alpha ia64 ppc s390 s390x x86_64 ppc64 ppc64le sparc sparcv9 sparc64 riscv64 aarch64
	--disable-werror					\
%else
%if %{suse_version} <= 1110
	--disable-werror					\
%else
	--enable-werror						\
%endif
%endif
	--with-separate-debug-dir=/usr/lib/debug		\
	--disable-sim						\
	--disable-rpath						\
	--with-system-zlib					\
%if %{suse_version} >= 1500
	--with-system-readline					\
%else
	--without-system-readline				\
%endif
	--with-expat						\
$(: ppc64 host build crashes on ppc variant of libexpat.so )	\
	--without-libexpat-prefix				\
	--enable-tui						\
%if 0%{!?_without_python:1}
	--with-python=%{_bindir}/%{python}			\
%else
	--without-python					\
%endif
%if %{suse_version} >= 1130
	--with-rpm=$LIBRPM					\
%else
	--without-rpm						\
%endif
%ifarch ia64
	--with-libunwind					\
%else
	--without-libunwind					\
%endif
%ifarch sparc sparcv9 sparc64
	--without-mmap						\
%endif
	--enable-64-bit-bfd					\
%if %{have_inproctrace}
	--enable-inprocess-agent				\
%else
	--disable-inprocess-agent				\
%endif
%if %{have_libipt}
        --with-intel-pt                                         \
%else
        --without-intel-pt                                      \
%endif
	--with-bugurl=http://bugs.opensuse.org/ \
	--with-pkgversion="GDB; %{DIST}" \
	${EXTRA_TARGETS:+--enable-targets="${EXTRA_TARGETS#,}"} \
%ifarch sparc sparcv9
	--build=sparc-%{_vendor}-%{_target_os}%{?_gnu}
%else
$(: It breaks RHEL-5 by %{_target_platform} being noarch-redhat-linux-gnu ) \
%ifarch noarch
	$(:)
%else
	--build=%{_target_platform}
%endif
%endif

if [ -z "%{!?_with_profile:no}" ]
then
  # Run all the configure tests being incompatible with $FPROFILE_CFLAGS.
  make %{?_smp_mflags} configure-host configure-target
  make %{?_smp_mflags} clean

  # Workaround -fprofile-use:
  # linux-x86-low.c:2225: Error: symbol `start_i386_goto' is already defined
  make %{?_smp_mflags} -C gdb/gdbserver linux-x86-low.o
fi

# Global CFLAGS would fail on:
# conftest.c:1:1: error: coverage mismatch for function 'main' while reading counter 'arcs'
if [ "$fprofile" = "-fprofile" ]
then
  FPROFILE_CFLAGS='-fprofile-generate'
elif [ -z "%{!?_with_profile:no}" ]
then
  FPROFILE_CFLAGS='-fprofile-use'
  # We cannot use -fprofile-dir as the bare filenames clash.
  (cd ../%{gdb_build}-fprofile;
   # It was 333 on x86_64.
   test $(find -name "*.gcda"|wc -l) -gt 300
   find -name "*.gcda" | while read -r i
   do
     ln $i ../%{gdb_build}/$i
   done
  )
else
  FPROFILE_CFLAGS=""
fi

# Prepare gdb/config.h first.
make %{?_smp_mflags} V=1 CFLAGS="$CFLAGS $FPROFILE_CFLAGS" LDFLAGS="$LDFLAGS $FPROFILE_CFLAGS" maybe-configure-gdb
perl -i.relocatable -pe 's/^(D\[".*_RELOCATABLE"\]=" )1(")$/${1}0$2/' gdb/config.status

make %{?_smp_mflags} V=1 CFLAGS="$CFLAGS $FPROFILE_CFLAGS" LDFLAGS="$LDFLAGS $FPROFILE_CFLAGS"

! grep '_RELOCATABLE.*1' gdb/config.h

if [ "$fprofile" = "-fprofile" ]
then
  cd gdb
  cp -p gdb gdb-withindex
  PATH="$PWD:$PATH" sh ../../gdb/gdb-add-index $PWD/gdb-withindex
  ./gdb -nx -ex q ./gdb-withindex
  ./gdb -nx -readnow -ex q ./gdb-withindex
  cd ..
fi

# This is a build-time test, but still a test.  So, skip if we don't do tests.
# This is relevant for %%qemu_user_space_build == 1 builds, which atm is
# the case for riscv64.
%if %{build_testsuite}
if [ "$LIBRPM" != "no" ]; then
    cd gdb
    cat \
	> hello.c \
	<<EOF
#include <stdio.h>
int
main (void)
{
  printf ("hello\n");
  return 0;
}
EOF
    $CC hello.c
    libc=$(ldd a.out \
	       | grep libc.so \
	       | awk '{print $3}')
    if readelf -SW $libc \
	    | grep -q "\.gnu_debuglink"; then
	cat \
	    > test.exp \
	    <<EOF
expect {
  "(gdb) " {
    puts "\nPASS: first prompt"
    send "start\n"
  }
  default {
    puts "\nFAIL: first prompt (eof or timeout)"
    exit 1
  }
}
expect {
  -re {Missing separate debuginfos, use: zypper install glibc-debuginfo-.*\(gdb\) } {
    puts "\nPASS: zypper install message"
    send "quit\n"
    exit 0
  }
  "(gdb) " {
    puts "\nFAIL: zypper install message"
    send "quit\n"
    exit 1
  }
  default {
    puts "\nFAIL: zypper install message (eof or timeout)"
    exit 1
  }
}
EOF
	gdb="./gdb -q -nw -nx -data-directory $(pwd -P)/data-directory"
        # Due to bsc#1146899 "gdb's zypper install message disappears with
	# -batch", we need to use an expect test.
	expect -c "spawn $gdb ./a.out" -f test.exp
	rm ./test.exp
    else
	# If packages are not build with debuginfo, we cannot expect a zypper
	# install message.
	echo "UNSUPPORTED: zypper install message"
    fi
    rm ./hello.c ./a.out
    cd ..
fi
%endif

cd ..

done	# fprofile

cd %{gdb_build}

#make %{?_smp_mflags} -C gdb/doc {gdb,annotate}{.info,/index.html,.pdf} MAKEHTMLFLAGS=--no-split

# Copy the <sourcetree>/gdb/NEWS file to the directory above it.
cp $RPM_BUILD_DIR/%{gdb_src}/gdb/NEWS $RPM_BUILD_DIR/%{gdb_src}

%check
# Initially we're in the %%{gdb_src} directory.
cd %{gdb_build}

%if !%{build_testsuite}
echo ====================TESTSUITE DISABLED=========================
%else
echo ====================TESTING=========================
cd gdb
%if 0%{suse_version} > 1110
CC=gcc
CXX=g++
%else
CC=gcc-4.8
CXX=g++-4.8
mkdir progs
for i in gcc g++ gcj gfortran gnat gnatbind gnatmake; do
  test -f /usr/bin/${i}-4.8 && ln -sf /usr/bin/${i}-4.8 progs/$i
done
PATH="`pwd`"/progs:${PATH}
%endif
export CC
export CXX
$CC -o ./orphanripper %{SOURCE2} -Wall -lutil -ggdb2
# Need to use a single --ignore option, second use overrides first.
# No `%{?_smp_mflags}' here as it may race.
# WARNING: can't generate a core file - core tests suppressed - check ulimit
# "readline-overflow.exp" - Testcase is broken, functionality is OK.
(
  # ULIMIT required for `gdb.base/auxv.exp'.
  ulimit -H -c
  ulimit -c unlimited || :

  # Setup $CHECK as `check//unix/' or `check//unix/-m64' for explicit bitsize.
  # Never use two different bitsizes as it fails on ppc64.
  echo 'int main (void) { return 0; }' >biarch.c
  CHECK=""
  for BI in -m64 -m32 -m31 ""
  do
    # Do not use size-less options if any of the sizes works.
    # On ia64 there is no -m64 flag while we must not leave a bare `check' here
    # as it would switch over some testing scripts to the backward compatibility
    # mode: when `make check' was executed from inside the testsuite/ directory.
    if [ -z "$BI" -a -n "$CHECK" ];then
      continue
    fi
    # Do not use $RPM_OPT_FLAGS as the other non-size options will not be used
    # in the real run of the testsuite.
    if ! $CC $BI -o biarch biarch.c
    then
      continue
    fi
    CHECK="$CHECK check//unix/$BI"
  done
  # Do not try -m64 inferiors for -m32 GDB as it cannot handle inferiors larger
  # than itself.
  # s390 -m31 still uses the standard ELF32 binary format.
  $CC $RPM_OPT_FLAGS -o biarch biarch.c
  RPM_SIZE="$(file ./biarch|sed -n 's/^.*: ELF \(32\|64\)-bit .*$/\1/p')"
  if [ "$RPM_SIZE" != "64" ]
  then
    CHECK="$(echo " $CHECK "|sed 's# check//unix/-m64 # #')"
  fi

  # Disable some problematic testcases.
  # RUNTESTFLAGS='--ignore ...' is not used below as it gets separated by the
  # `check//...' target spawn and too much escaping there would be dense.
  for test in				\
    gdb.base/readline-overflow.exp	\
    gdb.base/bigcore.exp		\
    gdb.threads/attach-many-short-lived-threads.exp \
  ; do
    mv -f ../../gdb/testsuite/$test ../../gdb/testsuite/$test-DISABLED || :
  done

  # Run all the scheduled testsuite runs also in the PIE mode.
  # See also: gdb-runtest-pie-override.exp
  if rpm -q gcc-PIE; then
      CHECK="$(echo $CHECK | sed 's#check//unix/[^ ]*#& &/-fno-PIE/-no-pie#g')"
  else
      CHECK="$(echo $CHECK | sed 's#check//unix/[^ ]*#& &/-fPIE/-pie#g')"
  fi

  ./orphanripper make %{?_smp_mflags} -k $CHECK || :
)
for t in sum log
do
  for file in testsuite*/gdb.$t
  do
    suffix="${file#testsuite.unix.}"
    suffix="${suffix%/gdb.$t}"
    ln $file gdb-%{_target_platform}$suffix.$t || :
  done
done
# `tar | bzip2 | uuencode' may have some piping problems in Brew.
#tar cjf gdb-%%{_target_platform}.tar.bz2 gdb-%%{_target_platform}*.{sum,log}
#uuencode gdb-%%{_target_platform}.tar.bz2 gdb-%%{_target_platform}.tar.bz2
# Strip dates and completion times from the log to make build-compare happy
sed -i -e '/Test Run By abuild on/d' -e 's/completed in [0-9]* seconds//' *.{sum,log}
cd ../..
echo ====================TESTING END=====================
%endif

%install
# Initially we're in the %%{gdb_src} directory.
cd %{gdb_build}

# It would break RHEL-5 by leaving excessive files for the doc subpackage.
%ifnarch noarch

make %{?_smp_mflags} install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gdbinit.d
touch -r %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/gdbinit.d

%if 0%{!?_without_python:1}
sed 's#%%{_sysconfdir}#%{_sysconfdir}#g' <%{SOURCE4} >$RPM_BUILD_ROOT%{_sysconfdir}/gdbinit
touch -r %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/gdbinit
%else
sed 's#%%{_sysconfdir}#%{_sysconfdir}#g' <%{SOURCE5} >$RPM_BUILD_ROOT%{_sysconfdir}/gdbinit
touch -r %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/gdbinit
%endif

for i in `find $RPM_BUILD_ROOT%{_datadir}/gdb/python/gdb -name "*.py"`
do
  # Files could be also patched getting the current time.
  touch -r $RPM_BUILD_DIR/%{gdb_src}/gdb/ChangeLog $i
done

%if 0%{?_enable_debug_packages:1} && 0%{!?_without_python:1}
mkdir -p $RPM_BUILD_ROOT/usr/lib/debug%{_bindir}
cp -p $RPM_BUILD_DIR/%{gdb_src}/gdb/gdb-gdb.py $RPM_BUILD_ROOT/usr/lib/debug%{_bindir}/
for pyo in "" "-O";do
  # RHEL-5: AttributeError: 'module' object has no attribute 'compile_file'
  %{python} $pyo -c 'import compileall, re, sys; sys.exit (not compileall.compile_dir("'"$RPM_BUILD_ROOT/usr/lib/debug%{_bindir}"'", 1, "'"/usr/lib/debug%{_bindir}"'"))'
done
%endif # 0%{?_enable_debug_packages:1} && 0%{!?_without_python:1}

mkdir $RPM_BUILD_ROOT%{_datadir}/gdb/auto-load
%if 0%{?rhel:1} && 0%{?rhel} <= 6
%if 0%{!?_without_python:1}
# Temporarily now:
for LIB in lib lib64;do
  LIBPATH="$RPM_BUILD_ROOT%{_datadir}/gdb/auto-load%{_root_prefix}/$LIB"
  mkdir -p $LIBPATH
  # basename is being run only for the native (non-biarch) file.
  sed -e 's,@pythondir@,%{_datadir}/gdb/python,'		\
      -e 's,@toolexeclibdir@,%{_root_prefix}/'"$LIB,"		\
      < $RPM_BUILD_DIR/%{gdb_src}/%{libstdcxxpython}/hook.in	\
      > $LIBPATH/$(basename %{_root_prefix}/%{_lib}/libstdc++.so.6.*)-gdb.py
  # Test the filename 'libstdc++.so.6.*' has matched.
  test -f $LIBPATH/libstdc++.so.6.[0-9]*-gdb.py
done
test ! -e $RPM_BUILD_ROOT%{_datadir}/gdb/python/libstdcxx
cp -a $RPM_BUILD_DIR/%{gdb_src}/%{libstdcxxpython}/libstdcxx	\
      $RPM_BUILD_ROOT%{_datadir}/gdb/python/libstdcxx
for i in `find $RPM_BUILD_ROOT%{_datadir}/gdb/python -name "*.py"` \
         `find $RPM_BUILD_ROOT%{_datadir}/gdb/auto-load%{_prefix} -name "*.py"` \
; do
  # Files come from gdb-archer.patch and can be also further patched.
  touch -r $RPM_BUILD_DIR/%{gdb_src}/gdb/ChangeLog $i
done
%endif # 0%{!?_without_python:1}
%endif # 0%{?rhel:1} && 0%{?rhel} <= 6

# Remove the files that are part of a gdb build but that are owned and
# provided by other packages.
# These are part of binutils

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/
rm -f $RPM_BUILD_ROOT%{_infodir}/bfd*
rm -f $RPM_BUILD_ROOT%{_infodir}/standard*
rm -f $RPM_BUILD_ROOT%{_infodir}/configure*
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT/%{_libdir}/lib{bfd*,opcodes*,iberty*}

%if %{build_testsuite}
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/gdbinit
rm -rf $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_libdir}
rm -rf $RPM_BUILD_ROOT%{_datadir}/gdb
rm -rf $RPM_BUILD_ROOT%{_infodir}
rm -rf $RPM_BUILD_ROOT%{_mandir}
rm -rf $RPM_BUILD_ROOT/usr/src
%endif

# pstack obsoletion

%if %{build_main}
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/man1/gstack.1
%endif
%endif	# 0%{!?_with_upstream:1}

%if %{build_main}
# Packaged GDB is not a cross-target one.
(cd $RPM_BUILD_ROOT%{_datadir}/gdb/syscalls
 rm -f mips*.xml
%ifnarch sparc sparcv9 sparc64
 rm -f sparc*.xml
%endif
%ifnarch x86_64
 rm -f amd64-linux.xml
%endif
%ifnarch %{ix86} x86_64
 rm -f i386-linux.xml
%endif
%ifnarch ppc ppc64
 rm -f ppc{,64}-linux.xml
%endif
%ifnarch ppc64le
 rm -f ppc64le-linux.xml
%endif
)

# It would break RHEL-5 by leaving excessive files for the doc subpackage.
%if 0%{?el5:1}
rm -f $RPM_BUILD_ROOT%{_infodir}/annotate.info*
rm -f $RPM_BUILD_ROOT%{_infodir}/gdb.info*
%endif # 0%{?el5:1} 
# -j1: There is some race resulting in:
# /usr/bin/texi2dvi: texinfo.tex appears to be broken, quitting.
make -j1 -C gdb/doc install DESTDIR=$RPM_BUILD_ROOT

# Documentation only for development; keep 'rm's here after "noarch" above.
rm -f $RPM_BUILD_ROOT%{_infodir}/gdbint*
rm -f $RPM_BUILD_ROOT%{_infodir}/stabs*

# Delete this too because the dir file will be updated at rpm install time.
# We don't want a gdb specific one overwriting the system wide one.

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%ifarch riscv64
# Work around RPM build error:
# ...
#   Installed (but unpackaged) file(s) found:
#   /usr/share/man/man1/gdbserver.1.gz
# ...
# Filed at PR24575 - "gdbserver.1 should only be installed if gdbserver was
# build" ( https://sourceware.org/bugzilla/show_bug.cgi?id=24575 ).
rm %{buildroot}/usr/share/man/man1/gdbserver.1
%endif
%endif

%post
# This step is part of the installation of the RPM. Not to be confused
# with the 'make install ' of the build (rpmbuild) process.

# For --excludedocs:
if [ -e %{_infodir}/gdb.info.gz ]
then
  %install_info --info-dir=%{_infodir} %{_infodir}/annotate.info.gz
  %install_info --info-dir=%{_infodir} %{_infodir}/gdb.info.gz
fi

%preun
if [ $1 = 0 ]
then
  # For --excludedocs:
  if [ -e %{_infodir}/gdb.info.gz ]
  then
    %install_info_delete --delete --info-dir=%{_infodir} %{_infodir}/annotate.info.gz
    %install_info_delete --delete --info-dir=%{_infodir} %{_infodir}/gdb.info.gz
  fi
fi

%if %{build_main}
%files
%defattr(-,root,root)
%doc README NEWS
%if 0%{suse_version} >= 1320
%license COPYING3 COPYING COPYING.LIB
%else
%doc COPYING3 COPYING COPYING.LIB
%endif
%{_bindir}/gcore
%{_mandir}/*/gcore.1*
%{_bindir}/gdb
%config(noreplace) %{_sysconfdir}/gdbinit
%{_sysconfdir}/gdbinit.d
%{_mandir}/*/gdb.1*
%{_bindir}/gstack
%{_mandir}/*/gstack.1*
%{_bindir}/gdb-add-index
%{_mandir}/*/gdb-add-index.1*
%{_mandir}/*/gdbinit.5*
%{_datadir}/gdb
%{_infodir}/annotate.info*
%{_infodir}/gdb.info*
%endif

%if %{build_testsuite}
%files
%defattr(-,root,root)
%doc %{gdb_build}/gdb/gdb-*.sum
%doc %{gdb_build}/gdb/gdb-*.log
%endif

# don't include the files in include, they are part of binutils

%if %{build_main}
%ifnarch riscv64 sparcv9 hppa
%files -n gdbserver
%defattr(-,root,root)
%{_bindir}/gdbserver
%{_mandir}/*/gdbserver.1*
%if %{have_inproctrace}
%{_libdir}/libinproctrace.so
%endif # %%{have_inproctrace}
%endif
%endif

%if %{build_main}
%post doc
# This step is part of the installation of the RPM. Not to be confused
# with the 'make install ' of the build (rpmbuild) process.

# For --excludedocs:
if [ -e %{_infodir}/gdb.info.gz ]
then
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/annotate.info.gz || :
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/gdb.info.gz || :
fi

%preun doc
if [ $1 = 0 ]
then
  # For --excludedocs:
  if [ -e %{_infodir}/gdb.info.gz ]
  then
    /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/annotate.info.gz || :
    /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/gdb.info.gz || :
  fi
fi
%endif

%changelog
