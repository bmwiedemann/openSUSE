#
# spec file
#
# Copyright (c) 2024 SUSE LLC
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
%bcond_with for_chroot

%if "%flavor" == "testsuite"
%if %{with ringdisabled}
ExclusiveArch:  do_not_build
%endif
%if 0%{?qemu_user_space_build}
# In a qemu_user_space_build ptrace is not supported, so we can't test gdb.
ExclusiveArch:  do_not_build
%endif

# Disable big-endian ppc testing.
ExcludeArch:    ppc ppc64

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
License:        GPL-3.0-only WITH GCC-exception-3.1 AND GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Group:          Development/Languages/C and C++
%endif
%if %{build_testsuite}
Summary:        GDB testsuite results
License:        SUSE-Public-Domain
Group:          Development/Languages/C and C++
%endif
Name:           gdb%{name_suffix}

Version:        14.2
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
%if 0%{?suse_version} >= 1200
%define python python3
%else
# Skip for SLE-11 due to lack of python3.
%define _without_python 1
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
%global libipt_version 2.0.5
Source7:        v%{libipt_version}.tar.gz

# Infrastructure to sync patches from the Fedora rpm
Source10:       patchlist.pl
Source11:       patchname_get.sh
Source12:       baselibs.conf
Source13:       gdb-rpmlintrc

# Infrastructure to maintain package.
Source14:       clean.sh
Source15:       import-patches.sh
Source16:       qa.sh
Source17:       qa-local.sh
Source18:       qa-remote.sh
Source19:       README.qa
Source20:       import-fedora.sh

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
NoSource:       14
NoSource:       15
NoSource:       16
NoSource:       17
NoSource:       18
NoSource:       19
NoSource:       20
%endif

# Fedora import from branch f38, commit 82cc8e0.

#Fedora Packages begin
Patch2:         gdb-6.3-gstack-20050411.patch
Patch3:         gdb-6.5-bz185337-resolve-tls-without-debuginfo-v2.patch
Patch4:         gdb-6.5-bz218379-ppc-solib-trampoline-test.patch
Patch5:         gdb-6.6-bz229517-gcore-without-terminal.patch
Patch6:         gdb-6.6-testsuite-timeouts.patch
Patch7:         gdb-6.6-bz237572-ppc-atomic-sequence-test.patch
Patch8:         gdb-6.3-attach-see-vdso-test.patch
Patch9:         gdb-6.5-bz243845-stale-testing-zombie-test.patch
Patch10:        gdb-6.6-buildid-locate.patch
Patch11:        gdb-6.6-buildid-locate-solib-missing-ids.patch
Patch12:        gdb-6.6-buildid-locate-rpm.patch
Patch14:        gdb-6.5-gcore-buffer-limit-test.patch
Patch15:        gdb-6.3-mapping-zero-inode-test.patch
Patch16:        gdb-6.5-section-num-fixup-test.patch
Patch18:        gdb-simultaneous-step-resume-breakpoint-test.patch
Patch19:        gdb-core-open-vdso-warning.patch
Patch20:        gdb-archer-next-over-throw-cxx-exec.patch
Patch21:        gdb-6.6-buildid-locate-rpm-librpm-workaround.patch
Patch22:        gdb-test-bt-cfi-without-die.patch
Patch23:        gdb-bz634108-solib_address.patch
Patch24:        gdb-test-dw2-aranges.patch
Patch25:        gdb-glibc-strstr-workaround.patch
Patch26:        gdb-rhbz-818343-set-solib-absolute-prefix-testcase.patch
Patch27:        gdb-rhbz947564-findvar-assertion-frame-failed-testcase.patch
Patch28:        gdb-rhbz1007614-memleak-infpy_read_memory-test.patch
Patch31:        gdb-rhbz1149205-catch-syscall-after-fork-test.patch
Patch32:        gdb-rhbz1084404-ppc64-s390x-wrong-prologue-skip-O2-g-3of3.patch
Patch33:        gdb-fedora-libncursesw.patch
Patch34:        gdb-rhbz1261564-aarch64-hw-watchpoint-test.patch
Patch36:        gdb-linux_perf-bundle.patch
Patch38:        gdb-rhbz2232086-refactor-selftest-support.patch
Patch39:        gdb-rhbz-2232086-reduce-size-of-gdb-index.patch
Patch40:        gdb-rhbz-2232086-cpp-ify-mapped-symtab.patch
Patch41:        gdb-rhbz-2232086-generate-gdb-index-consistently.patch
Patch42:        gdb-rhbz-2232086-generate-dwarf-5-index-consistently.patch
Patch43:        gdb-rhbz2250652-gdbpy_gil.patch
Patch44:        gdb-rhbz2250652-avoid-PyOS_ReadlineTState.patch
Patch45:        gdb-ftbs-swapped-calloc-args.patch
Patch46:        gdb-rhbz2261580-intrusive_list-assertion-fix.patch
#Fedora Packages end

# Fedora patches fixup
# These need a number with at least four digits, otherwise patchlist.pl removes
# them when upgrading.

Patch1000:      fixup-gdb-linux_perf-bundle.patch
Patch1003:      fixup-gdb-glibc-strstr-workaround.patch
Patch1004:      fixup-gdb-6.5-bz243845-stale-testing-zombie-test.patch
Patch1005:      fixup-gdb-test-bt-cfi-without-die.patch
Patch1007:      fixup-gdb-test-dw2-aranges.patch
Patch1008:      fixup-gdb-bz634108-solib_address.patch
Patch1009:      fixup-gdb-6.3-gstack-20050411.patch
Patch1010:      fixup-gdb-6.3-attach-see-vdso-test.patch
Patch1012:      fixup-gdb-rhbz1261564-aarch64-hw-watchpoint-test.pat.patch
# Fixes up several patches, should be dropped when updating to
# rawhide @ 08bfd0a.
Patch1013:      fixup-skip-tests.patch

# openSUSE specific

# Hardcodes /bin/bash, given that path is known.
Patch1100:      gdb-gcore-bash.patch
# Make gdb emit zypper install hints, rather than debuginfo-install hints.
Patch1101:      gdb-6.6-buildid-locate-rpm-suse.patch

# openSUSE specific -- testsuite

# Silences ada pie compilation FAILs.  Todo: Fix ada pie compilation.
Patch1200:      gdb-testsuite-ada-pie.patch
# Tests the zypper install hints.
Patch1203:      gdb-testsuite-add-gdb.suse-zypper-hint.exp.patch
# Tests that no branding is leaked from sourcing the fedora package.
Patch1204:      gdb-testsuite-add-gdb.suse-debranding.exp.patch

# Patches to upstream

# https://sourceware.org/bugzilla/show_bug.cgi?id=25703
Patch1500:      gdb-symtab-set-default-dwarf-max-cache-age-1000.patch
# https://bugzilla.suse.com/show_bug.cgi?id=1179210
Patch1501:      gdb-tui-enable-work-around-libncurses-segfault.patch
# Fixes: gdb.x86_64: W: potential-bashisms /usr/bin/gdb-add-index
Patch1503:      gdb-add-index.sh-fix-bashism.patch
# Fixes:
# FAIL: gdb.mi/new-ui-mi-sync.exp: sync-command=run: add-inferior (timeout)
Patch1504:      fix-gdb.mi-new-ui-mi-sync.exp.patch
# Fixes:
# FAIL: gdb.base/step-over-syscall.exp: fork: displaced=off: \
# pc after stepi matches insn addr after syscall
Patch1505:      gdb-testsuite-fix-gdb.base-step-over-syscall.exp-with-m32-amd-case.patch

# Backports from current release branch (GDB 14).

#

# Backports from master, available in next release (GDB 15).

Patch2000:      gdb-symtab-work-around-pr-gas-29517.patch
Patch2001:      gdb-symtab-add-producer_is_gas.patch
Patch2002:      gdb-symtab-work-around-gas-pr28629.patch
Patch2003:      gdb-tdep-fix-nr-array-elements-in-ppc64_aggregate_ca.patch
Patch2004:      gdb-tui-fix-wmaybe-uninitialized-in-tui_find_disasse.patch
Patch2005:      gdb-testsuite-add-missing-no-prompt-anchor-in-gdb.ba.patch
Patch2006:      gdb-testsuite-remove-spurious-in-save_vars.patch
Patch2007:      make-pascal_language-print_type-handle-varstring-nul.patch
Patch2008:      gdb-symtab-work-around-pr-gas-29517-dwarf2-case.patch
Patch2010:      fix-the-gdb.ada-inline-section-gc.exp-test.patch
Patch2011:      gdb-testsuite-handle-pac-marker.patch
Patch2012:      change-gdb.base-examine-backwards.exp-for-aix.patch
Patch2013:      gdb-testsuite-fix-spurious-fails-with-examine-backwa.patch
Patch2014:      gdb-testsuite-make-gdb.base-solib-search.exp-more-ro.patch
Patch2015:      gdb-testsuite-fix-regexp-in-vgdb_start.patch
Patch2016:      powerpc-and-aarch64-fix-reverse-stepping-failure.patch
Patch2017:      gdb-tdep-fix-gdb.base-watch-bitfields.exp-on-aarch64.patch
Patch2018:      gdb-tdep-fix-gdb.base-watchpoint-unaligned.exp-on-aa.patch
Patch2019:      gdb-testsuite-add-pr-gdb-26967-kfail-in-two-more-tes.patch
Patch2020:      gdb-testsuite-fix-gdb.base-eh_return.exp.patch
Patch2021:      fixup-powerpc-and-aarch64-fix-reverse-stepping-failu.patch
Patch2022:      gdb-exp-fix-printing-of-out-of-bounds-struct-members.patch
Patch2023:      gdb-fix-heap-use-after-free-in-select_event_lwp.patch
Patch2024:      fix-regression-on-aarch64-linux-gdbserver.patch
Patch2025:      gdb-testsuite-factor-out-proc-get_portnum.patch
Patch2026:      gdb-testsuite-make-portnum-a-persistent-global.patch
Patch2027:      gdb-testsuite-factor-out-proc-with_lock.patch
Patch2028:      gdb-testsuite-factor-out-proc-lock_dir.patch
Patch2029:      gdb-testsuite-move-gpu-parallel.lock-to-cache-dir.patch
Patch2030:      gdb-testsuite-use-unique-portnum-in-parallel-testing.patch
Patch2031:      gdb-testsuite-use-unique-portnum-in-parallel-testing-check-slash-slash-case.patch
Patch2032:      gdb-tdep-fix-reverse-execution-of-ldr-immediate-t4.patch
Patch2033:      gdb-exp-fix-cast-handling-for-indirection.patch
Patch2034:      gdb-remote-fix-abort-on-remote_close_error.patch
Patch2035:      gdb-testsuite-use-find_gnatmake-instead-of-gdb_find_.patch
Patch2036:      gdb-testsuite-simplify-gdb.server-server-kill-python.patch
Patch2037:      gdb-testsuite-fix-gdbserver-pid-in-gdb.server-server.patch
Patch2038:      gdb-testsuite-add-missing-include-in-gdb.base-ctf-pt.patch
Patch2039:      gdb-testsuite-fix-gdb.ada-verylong.exp-on-32-bit-tar.patch
Patch2040:      gdb-testsuite-add-missing-includes-in-gdb.trace-coll.patch
Patch2041:      gdb-testsuite-fix-missing-return-type-in-gdb.linespe.patch
Patch2042:      gdb-testsuite-fix-gdb.base-ending-run.exp-on-manjaro.patch
Patch2043:      gdb-testsuite-fix-test-case-gdb.threads-attach-stopp.patch
Patch2044:      gdb-testsuite-add-missing-include-in-gdb.base-rtld-s.patch
Patch2045:      gdb-testsuite-fix-valgrind-tests-on-debian.patch
Patch2046:      gdb-testsuite-fix-gdb.server-server-connect.exp-for-.patch
Patch2047:      gdb-testsuite-handle-core-without-build-id-in-gdb.ba.patch
Patch2048:      gdb-testsuite-fix-gdb.base-list-no-debug.exp-on-debi.patch
Patch2049:      gdb-testsuite-reset-errcnt-and-warncnt-in-default_gd.patch
Patch2050:      gdb-testsuite-fix-test-in-gdb.python-py-finish-break.patch
Patch2051:      gdb-testsuite-further-handle-long-filenames-in-gdb.b.patch
Patch2052:      gdb-testsuite-fix-license-text-in-gdb.reverse-map-to.patch
Patch2053:      gdb-testsuite-call-ldd-version-in-gdb.testsuite-dump.patch
Patch2054:      gdb-testsuite-fix-gdb.mi-mi-dprintf.exp-with-read1.patch
Patch2055:      gdb-testsuite-fix-gdb.cp-namespace.exp-with-read1.patch
Patch2056:      gdb-testsuite-fix-typo-in-gdb.base-catch-syscall.exp.patch
Patch2057:      gdb-testsuite-use-more-progbits-for-arm.patch
Patch2058:      gdb-testsuite-fix-gdb.dwarf2-dw2-gas-workaround.exp.patch
Patch2059:      gdb-fix-segfault-in-for_each_block-part-1.patch
Patch2060:      gdb-fix-segfault-in-for_each_block-part-2.patch
Patch2061:      gdb-tui-allow-command-window-of-1-or-2-lines.patch
Patch2062:      gdb-tui-fix-resizing-of-terminal-to-1-or-2-lines.patch
Patch2063:      gdb-symtab-workaround-pr-gas-31115.patch
Patch2064:      gdb-arm-remove-tpidruro-register-from-non-freebsd-ta.patch
Patch2065:      gdb-tdep-fix-catching-syscall-execve-exit-for-arm.patch
Patch2066:      gdb-arm-fix-epilogue-frame-id.patch
Patch2070:      rs6000-unwind-on-each-instruction-fix.patch
Patch2071:      gdb-python-make-gdb.unwindinfo.add_saved_register-mo.patch
Patch2072:      gdb-arm-remove-thumb-bit-in-arm_adjust_breakpoint_ad.patch
Patch2073:      gdb-build-fix-gdbserver-linux-aarch64-low.cc-build.patch
Patch2074:      powerpc-fix-test-gdb.ada-finish-large.exp.patch
Patch2075:      gdb-python-make-gdb.unwindinfo.add_saved_register-mo-fixup.patch
Patch2076:      gdb-exp-redo-cast-handling-for-indirection.patch

# Backports from master, not yet available in next release (GDB 16).

Patch2090:      gdb-python-fix-gdb.python-py-disasm.exp-on-arm-linux.patch
Patch2091:      gdb-testsuite-fix-gdb.fortran-array-bounds.exp-on-ar.patch

#

# Backport from gdb-patches

# https://sourceware.org/pipermail/gdb-patches/2021-September/182226.html
Patch2100:      gdb-python-finishbreakpoint-update.patch
# https://sourceware.org/pipermail/gdb-patches/2021-October/182444.html
Patch2101:      gdb-testsuite-prevent-compilation-fails-with-unix-fpie-pie.patch
# https://sourceware.org/pipermail/gdb-patches/2021-May/178990.html
Patch2102:      gdb-cli-add-ignore-errors-command.patch
# https://sourceware.org/pipermail/gdb-patches/2024-May/209469.html
Patch2103:      gdb-testsuite-fix-error-in-gdb.server-server-kill-py.patch
# https://sourceware.org/pipermail/gdb-patches/2024-May/209504.html
Patch2104:      gdb-testsuite-fix-timeout-in-gdb.tui-resize-2.exp.patch
# https://sourceware.org/pipermail/gdb-patches/2024-June/209736.html
Patch2105:      gdb-tdep-fix-gdb.base-watchpoint-running-on-arm-ppc6.patch

# https://sourceware.org/pipermail/gdb-patches/2023-December/205054.html
Patch2120:      gdb-symtab-refactor-condition-in-scan_attributes.patch
Patch2121:      gdb-symtab-factor-out-m_die_range_map-usage.patch
Patch2122:      gdb-symtab-handle-nullptr-parent-in-parent_map-set_p.patch
Patch2123:      gdb-symtab-factor-out-m_deferred_entries-usage.patch
Patch2124:      gdb-symtab-resolve-deferred-entries-inter-shard-case.patch
Patch2125:      gdb-testsuite-add-gdb.dwarf2-forward-spec-inter-cu.e.patch
Patch2126:      gdb-testsuite-add-gdb.dwarf2-backward-spec-inter-cu..patch
Patch2127:      gdb-symtab-keep-track-of-processed-dies-in-shard.patch
Patch2128:      gdb-symtab-resolve-deferred-entries-intra-shard-case.patch
Patch2129:      gdb-symtab-don-t-defer-backward-refs-inter-cu-intra-.patch
Patch2130:      gdb-symtab-recurse-into-c-dw_tag_subprogram-dies-for.patch
Patch2131:      gdb-symtab-keep-track-of-all-parents-for-cooked-inde.patch
Patch2132:      gdb-symtab-fix-dw_tag_inlined_subroutine-entries-in-.patch

# Debug patches.

#

# Other.  Needs comment for each patch.

#

# End of patches.

BuildRequires:  bison
BuildRequires:  flex
%if 0%{suse_version} > 1110
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc48
BuildRequires:  gcc48-c++
%endif
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

# Dependency is there for SLE-11, but configure test fails.
BuildRequires:  mpfr-devel

BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  readline-devel
BuildRequires:  rpm-devel
# SLE-10 doesn't have xz-devel.
%if 0%{suse_version} >= 1110
BuildRequires:  xz-devel
%endif
BuildRequires:  zlib-devel

%if 0%{!?_without_python:1}
%if %{build_testsuite}
BuildRequires:  %{python}-base
%else
Requires:       %{python}-base
%endif
BuildRequires:  %{python}-devel
%endif	# 0%{!?_without_python:1}

%global have_libdebuginfod 0
# Enable for SLE15-SP4/Leap-15.4, ALP/Factory.
%if 0%{?sle_version} >= 150400 || 0%{?suse_version} >= 1600
%global have_libdebuginfod 1
%endif

%if 0%{have_libdebuginfod}
BuildRequires:  libdebuginfod-devel
# Indicate that we prefer libdebuginfod1 over libdebuginfod1-dummy.
BuildRequires:  libdebuginfod1
%endif

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

%ifarch i386 x86_64 ppc64 ppc64le aarch64 riscv64
%if %{suse_version} >= 1500
BuildRequires:  babeltrace-devel
%endif
%endif

%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_regex-devel
BuildRequires:  libsource-highlight-devel
%endif

%if 0%{?suse_version} >= 1500
BuildRequires:  libzstd-devel
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

BuildRequires:  gcc-fortran
BuildRequires:  gcc-objc
%ifarch %ada_arch
BuildRequires:  gcc-ada
%endif

%define supported_32bit_arch x86_64 ppc64

%if 0%{!?disable_32bit:1}
%ifarch %{supported_32bit_arch}

%if 0%{suse_version} >= 1330
# Older distros miss this pseudo package, the Ada
# testsuite won't work completely
BuildRequires:  gcc-ada-32bit
%endif

%if 0%{suse_version} > 1110
BuildRequires:  gcc-c++-32bit
%else
# Use system g++ for testing for SLE-11.
BuildRequires:  gcc-c++
%endif

%if 0%{suse_version} >= 1210 && 0%{suse_version} != 1315
BuildRequires:  glibc-devel-static-32bit
%endif

%endif # supported_32bit_arch
%endif # !disable_32bit

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

%if %{with fpc} && 0%{?is_opensuse}
%ifarch x86_64 aarch64 armv7l
# Tumbleweed and Leap 15.x.
%if 0%{?suse_version} >= 1500
BuildRequires:  fpc
%endif
%ifarch %{ix86}
# Tumbleweed and Leap 15.{0,1,2}.
# fpc seems to be unavailable for Leap 15.{3,4}/i586.
%if 0%{?suse_version} > 1500 || (0%{?sle_version} >= 150000 && 0%{?sle_version} <= 150200)
BuildRequires:  fpc
%endif
%endif
%endif
%endif

%if 0%{?suse_version} >= 1200
%ifnarch s390
# s390 (for SLE12) doesn't have valgrind
BuildRequires:  valgrind
%endif
%endif

%if 0%{?suse_version} >= 1200
BuildRequires:  systemtap-sdt-devel
%endif

%if 0%{have_libdebuginfod}
BuildRequires:  curl
BuildRequires:  elfutils-debuginfod
# Fix: unresolvable: have choice for debuginfod-client needed by
# elfutils-debuginfod: debuginfod-client debuginfod-dummy-client.
BuildRequires:  debuginfod-client
%endif

# SLE-10 doesn't have xz.
%if 0%{suse_version} >= 1110
# Missing on SLE-11
BuildRequires:  xz
%endif

%if 0%{!?_without_python:1}
# Provide python package xml.etree.ElementTree, used by test-case
# gdb.python/py-send-packet.exp.
BuildRequires:  %{python}-xml
%endif

%endif # %%{build_testsuite}

%ifarch ia64
BuildRequires:  libunwind-devel
Requires:       libunwind
%endif

%if %{build_main}

%if 0%{!?_without_python:1}
%if 0%{?suse_version} >= 1500
# For SLE-15 and later, we use source-highlight by default, and
# pygments as fallback.  So, suggests rather than recommends is what we want.
# Don't bother older releases with this.
Suggests:       %{python}-Pygments
%endif
%endif

%description
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Java, and other languages, by executing them in a controlled fashion
and printing their data.

%package -n gdbserver
Summary:        A standalone server for GDB (the GNU source-level debugger)
License:        GPL-3.0-only WITH GCC-exception-3.1 AND GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Group:          Development/Tools/Debuggers

%description -n gdbserver
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Java, and other languages, by executing them in a controlled fashion
and printing their data.

This package provides a program that allows you to run GDB on a different
machine than the one which is running the program being debugged.

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
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 12 -p1
%patch -P 14 -p1
%patch -P 15 -p1
%patch -P 16 -p1
%patch -P 18 -p1
%patch -P 19 -p1
%patch -P 20 -p1
%patch -P 21 -p1
%patch -P 22 -p1
%patch -P 23 -p1
%patch -P 24 -p1
%patch -P 25 -p1
%patch -P 26 -p1
%patch -P 27 -p1
%patch -P 28 -p1
%patch -P 31 -p1
%patch -P 32 -p1
%patch -P 33 -p1
%patch -P 34 -p1
%patch -P 36 -p1
%patch -P 38 -p1
%patch -P 39 -p1
%patch -P 40 -p1
%patch -P 41 -p1
%patch -P 42 -p1
%patch -P 43 -p1
%patch -P 44 -p1
%patch -P 45 -p1
%patch -P 46 -p1
#Fedora patching end

%patch -P 1000 -p1
%patch -P 1003 -p1
%patch -P 1004 -p1
%patch -P 1005 -p1
%patch -P 1007 -p1
%patch -P 1008 -p1
%patch -P 1009 -p1
%patch -P 1010 -p1
%patch -P 1012 -p1
%patch -P 1013 -p1

%patch -P 1100 -p1
%patch -P 1101 -p1

%patch -P 1200 -p1
%patch -P 1203 -p1
%patch -P 1204 -p1

%patch -P 1500 -p1
%patch -P 1501 -p1
%patch -P 1503 -p1
%patch -P 1504 -p1
%patch -P 1505 -p1

%patch -P 2000 -p1
%patch -P 2001 -p1
%patch -P 2002 -p1
%patch -P 2003 -p1
%patch -P 2004 -p1
%patch -P 2005 -p1
%patch -P 2006 -p1
%patch -P 2007 -p1
%patch -P 2008 -p1
%patch -P 2010 -p1
%patch -P 2011 -p1
%patch -P 2012 -p1
%patch -P 2013 -p1
%patch -P 2014 -p1
%patch -P 2015 -p1
%patch -P 2016 -p1
%patch -P 2017 -p1
%patch -P 2018 -p1
%patch -P 2019 -p1
%patch -P 2020 -p1
%patch -P 2021 -p1
%patch -P 2022 -p1
%patch -P 2023 -p1
%patch -P 2024 -p1
%patch -P 2025 -p1
%patch -P 2026 -p1
%patch -P 2027 -p1
%patch -P 2028 -p1
%patch -P 2029 -p1
%patch -P 2030 -p1
%patch -P 2031 -p1
%patch -P 2032 -p1
%patch -P 2033 -p1
%patch -P 2034 -p1
%patch -P 2035 -p1
%patch -P 2036 -p1
%patch -P 2037 -p1
%patch -P 2038 -p1
%patch -P 2039 -p1
%patch -P 2040 -p1
%patch -P 2041 -p1
%patch -P 2042 -p1
%patch -P 2043 -p1
%patch -P 2044 -p1
%patch -P 2045 -p1
%patch -P 2046 -p1
%patch -P 2047 -p1
%patch -P 2048 -p1
%patch -P 2049 -p1
%patch -P 2050 -p1
%patch -P 2051 -p1
%patch -P 2052 -p1
%patch -P 2053 -p1
%patch -P 2054 -p1
%patch -P 2055 -p1
%patch -P 2056 -p1
%patch -P 2057 -p1
%patch -P 2058 -p1
%patch -P 2059 -p1
%patch -P 2060 -p1
%patch -P 2061 -p1
%patch -P 2062 -p1
%patch -P 2063 -p1
%patch -P 2064 -p1
%patch -P 2065 -p1
%patch -P 2066 -p1
%patch -P 2070 -p1
%patch -P 2071 -p1
%patch -P 2072 -p1
%patch -P 2073 -p1
%patch -P 2074 -p1
%patch -P 2075 -p1
%patch -P 2076 -p1

%patch -P 2090 -p1
%patch -P 2091 -p1

%patch -P 2100 -p1
%patch -P 2101 -p1
%patch -P 2102 -p1
%patch -P 2103 -p1
%patch -P 2104 -p1
%patch -P 2105 -p1

%patch -P 2120 -p1
%patch -P 2121 -p1
%patch -P 2122 -p1
%patch -P 2123 -p1
%patch -P 2124 -p1
%patch -P 2125 -p1
%patch -P 2126 -p1
%patch -P 2127 -p1
%patch -P 2128 -p1
%patch -P 2129 -p1
%patch -P 2130 -p1
%patch -P 2131 -p1
%patch -P 2132 -p1

#unpack libipt
%if 0%{have_libipt}
tar xzf %{SOURCE7}
mv libipt-%{libipt_version} processor-trace-%{libipt_version}
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

# Fixes problem building release tarball with --with-system-readline.
# Reported here:
# - https://sourceware.org/pipermail/gdb/2021-July/049552.html
# - https://sourceware.org/bugzilla/show_bug.cgi?id=27808
rm -f gdb/doc/GDBvn.texi

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
for opt in -Wno-error=odr -Wno-error=enum-int-mismatch; do
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

%define extra_target_list_common i686 powerpc64le s390x x86_64 aarch64
%if 0%{?is_opensuse}
%define extra_target_list %{extra_target_list_common} powerpc powerpc64 s390 arm m68k ia64 riscv64
%define have_elf_extra_target_list 1
%define elf_extra_target_list avr pru spu
%else
%define extra_target_list %{extra_target_list_common}
%define have_elf_extra_target_list 0
%endif

%define DIST %(echo '%distribution' | sed 's, /.*,,')

%if %build_multitarget
EXTRA_TARGETS="%(printf ,%%s-suse-linux %{extra_target_list})"
%if %{have_elf_extra_target_list}
EXTRA_TARGETS="$EXTRA_TARGETS%(printf ,%%s-elf %{elf_extra_target_list})"
%endif
%else
EXTRA_TARGETS=
%endif

# Reenable enable-werror on tumbleweed when upgrading to 13.1 (bsc#1211052)
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
%if %{suse_version} <= 1110 || %{suse_version} > 1500
	--disable-werror					\
%else
	--enable-werror						\
%endif
%endif
	--with-separate-debug-dir=/usr/lib/debug		\
%if 0%{have_libdebuginfod}
	--with-debuginfod=yes                                   \
%endif
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
	--with-libunwind-ia64					\
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
$(: ia64 is obsolete. )                                         \
	--enable-obsolete                                       \
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
CC=gcc
CXX=g++
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
  DISABLE_TESTS=
  DISABLE_TESTS="$DISABLE_TESTS gdb.base/bigcore.exp"
  DISABLE_TESTS="$DISABLE_TESTS gdb.threads/attach-many-short-lived-threads.exp"
  %if 0%{suse_version} == 1110
  DISABLE_TESTS="$DISABLE_TESTS gdb.base/break-interp.exp"
  %endif
  for test in $DISABLE_TESTS; do
    mv -f ../../gdb/testsuite/$test ../../gdb/testsuite/$test-DISABLED || :
  done

  # Run all the scheduled testsuite runs also in the PIE mode.
  # See also: gdb-runtest-pie-override.exp
  if rpm -q gcc-PIE; then
      CHECK="$(echo $CHECK | sed 's#check//unix/[^ ]*#& &/-fno-PIE/-no-pie#g')"
  else
      CHECK="$(echo $CHECK | sed 's#check//unix/[^ ]*#& &/-fPIE/-pie#g')"
  fi

%if %{with for_chroot}
  # When we want to chroot into a local osc build and run a test-case, we
  # need -M testsuite to add all the buildrequires, but there's no need
  # to run the testsuite.  Instead, fail %check to make sure %clean doesn't
  # remove buildroot.
  false
%else
  ./orphanripper make %{?_smp_mflags} -k $CHECK || :
%endif
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
  touch -r $RPM_BUILD_DIR/%{gdb_src}/gdb/version.in $i
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
  touch -r $RPM_BUILD_DIR/%{gdb_src}/gdb/version.in $i
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
rm -f $RPM_BUILD_ROOT%{_infodir}/sframe-spec*
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT/%{_libdir}/lib{bfd*,opcodes*,iberty*,ctf*,sframe*}

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
rm -f $RPM_BUILD_ROOT%{_infodir}/ctf-spec*

# Delete this too because the dir file will be updated at rpm install time.
# We don't want a gdb specific one overwriting the system wide one.

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

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
%ifnarch sparcv9 hppa
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
