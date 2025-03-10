#
# spec file for package crash
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
# needssslcertforbuild


%define whitepaper_version 2003
%define scripts_version  2008-02-08
%define gcore_version  2023-02-28

%if 0%{!?have_snappy:1}
%if 0%{?suse_version} >= 1310
%define have_snappy 1
%else
%define have_snappy 0
%endif
%endif

%if 0%{!?have_zstd:1}
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
# the zstd patch depends on the snappy patch
%define have_zstd %{have_snappy}
%else
%define have_zstd 0
%endif
%endif

%ifarch %ix86 x86_64
%define build_gcore 1
%else
%define build_gcore 0
%endif

%define build_kmp 1
%if 0%{?suse_version} <= 1500 && 0%{?suse_version} >= 1315
# kernel is missing on 32bit SLE - cannot build a KMP
%ifarch %ix86 s390
%define build_kmp 0
%endif
%endif
# kernel is missing on 32-bit ppc
%ifarch ppc
%define build_kmp 0
%endif

Name:           crash
URL:            https://crash-utility.github.io/
Summary:        Crash utility for live systems; netdump, diskdump, LKCD or mcore dumpfiles
License:        GFDL-1.2-only AND GPL-3.0-or-later
Group:          Development/Tools/Debuggers
Version:        8.0.5
Release:        0
Source:         https://github.com/crash-utility/crash/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/gdb/gdb-10.2.tar.gz
Source2:        crash_whitepaper-%{whitepaper_version}.tar.bz2
Source3:        README.SUSE
Source4:        sial-scripts-%{scripts_version}.tar.bz2
Source5:        gcore-%{gcore_version}.tar.bz2
Source6:        Module.supported
Source7:        https://ftp.gnu.org/gnu/gdb/gdb-10.2.tar.gz.sig
Source8:        gnu.keyring
Source95:       get-kernel-flavors.sh
Source96:       depmod.sh
Source97:       mkinitrd.sh
Source98:       %{name}-kmp-preamble
Source99:       crash-rpmlintrc
Source100:      %{name}-gdb-10.2.series
Source101:      %{name}-gdb-gnulib-define-warndecl.patch
Patch1:         %{name}-make-emacs-default.diff
Patch2:         %{name}-sles9-quirk.patch
Patch4:         %{name}-sles9-time.patch
Patch9:         %{name}-debuginfo-compressed.patch
Patch10:        %{name}_enable_lzo_support.patch
Patch11:        %{name}-compressed-booted-kernel.patch
Patch13:        %{name}-patch-gdb.patch
Patch15:        %{name}_enable_snappy_support.patch
Patch18:        %{name}-stop_read_error_when_intent_is_retry.patch
Patch21:        %{name}-allow-use-of-sadump-captured-KASLR-kernel.patch
Patch23:        %{name}-SLE15-SP1-With-Linux-4.19-rc1-up-MAX_PHYSMEM_BITS-to-128TB.patch
Patch24:        %{name}-SLE15-SP1-Fix-for-PPC64-kernel-virtual-address-translation-in.patch
Patch30:        %{name}-enable-zstd-support.patch
Patch32:        %{name}-extensions-rule-for-defs.patch
Patch90:        %{name}-sial-ps-2.6.29.diff
Patch99:        %{name}-usrmerge.patch
Patch100:       0001-arm64-section_size_bits-compatible-with-macro-defini.patch
Patch101:       0002-Reflect-__-start-end-_init_task-kernel-symbols-renam.patch
Patch102:       0003-x86_64-fix-for-adding-top_of_kernel_stack_padding-fo.patch
Patch103:       0004-Fix-kmem-v-option-on-Linux-6.9-and-later-kernels.patch
Patch104:       0005-X86-64-fix-for-crash-session-loading-failure.patch
Patch105:       0006-Fix-for-failing-to-load-kernel-module.patch
Patch106:       0007-X86-64-fix-a-regression-issue-about-kernel-stack-pad.patch
Patch107:       0008-Fix-kmem-i-and-swap-commands-on-Linux-6.10-rc1-and-l.patch
Patch108:       0009-List-enable-LIST_HEAD_FORMAT-for-r-option.patch
Patch109:       0010-arm64-fix-a-potential-segfault-when-unwind-frame.patch
Patch110:       0011-arm64-Fix-bt-command-show-wrong-stacktrace-on-ramdum.patch
Patch111:       fix_extensions_makefile_race_condition.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  lzo-devel
BuildRequires:  makeinfo
BuildRequires:  ncurses-devel
%if %{have_snappy}
BuildRequires:  snappy-devel
%endif
%if %{have_zstd}
BuildRequires:  libzstd-devel
%endif
BuildRequires:  libelf-devel
BuildRequires:  zlib-devel
Requires:       /usr/bin/nm
ExclusiveArch:  %ix86 x86_64 ia64 s390 s390x ppc ppc64 ppc64le alpha aarch64 %arm riscv64
%if 0%{?build_kmp}
BuildRequires:  kernel-syms
%ifarch x86_64
%if 0%{?suse_version} >= 1520 && 0%{?suse_version} < 1550
BuildRequires:  kernel-syms-rt
%endif
%endif
%if 0%{?suse_version} >= 1130
BuildRequires:  kernel-devel
%endif
%if %{defined kernel_module_package_buildreqs}
BuildRequires:  %kernel_module_package_buildreqs
%endif
BuildRequires:  module-init-tools
%endif

%if 0%{?build_kmp} && %{defined suse_kernel_module_package}
%suse_kernel_module_package -n crash -p %_sourcedir/%{name}-kmp-preamble um
%define arch %_target_cpu
%define kmp_pkg KMP
%endif

%description
The core analysis suite is a self-contained tool that can be used to
investigate either live systems, kernel core dumps created from the
netdump and diskdump packages from Red Hat Linux, the mcore kernel
patch offered by Mission Critical Linux, or the LKCD kernel patch.



Authors:
--------
    David Anderson <anderson@redhat.com>

%package doc
Requires:       %{name} = %{version}
Summary:        Documentation for Crash
License:        GFDL-1.2-only
Group:          Development/Tools/Debuggers

%description doc
This subpackage contains the crash whitepaper from Dave Anderson.



Authors:
--------
    David Anderson <anderson@redhat.com>

%package devel
Requires:       %{name} = %{version}
Summary:        Development files for crash
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
Requires:       zlib-devel

%description devel
This files are required to build extensions for crash.

Crash is the core analysis suite that can be used to investigate either
live systems, kernel core dumps created from the netdump and diskdump
packages from Red Hat Linux, the mcore kernel patch offered by Mission
Critical Linux, or the LKCD kernel patch.



Authors:
--------
    David Anderson <anderson@redhat.com>

%if %build_gcore

%package gcore
Requires:       %{name} = %{version}
Summary:        Gcore extension for crash
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers

%description gcore
Create a core dump file of a user-space task that was running in a
kernel dumpfile.



Authors:
--------
    Daisuke Hatayama  <d.hatayama@jp.fujitsu.com>

%endif

%package %kmp_pkg
Summary:        Memory driver for the crash utility
License:        GPL-2.0-only
Group:          System/Kernel

%description %kmp_pkg
To run the crash utility on a live system, a memory device must be present.
Due to many limitations of the /dev/mem interface, a separate kernel module
is provided to access all RAM through the /dev/crash device.

Authors:
--------
    David Anderson <anderson@redhat.com>

# Compatibility cruft
# there is no %%license prior to SLE12
%if %{undefined _defaultlicensedir}
%define license %doc
%else
# filesystem before SLE12 SP3 lacks /usr/share/licenses
%if 0%(test ! -d %{_defaultlicensedir} && echo 1)
%define _defaultlicensedir %{_defaultdocdir}
%endif
%endif
# End of compatibility cruft

%prep
%setup -q -a 2 -a 4
ln -s %{SOURCE1} .
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 4 -p1
%patch -P 9 -p1
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 13 -p1
%patch -P 18 -p1
%patch -P 21 -p1
# Patches for SLE 15 SP1 potentially break support for SLE15 and SLE 12 SP4
# Don't apply on these (and earlier) versions - see bsc#1148197
%if 0%{?sle_version} > 120400 && 0%{?sle_version} != 150000
%patch -P 23 -p1
%patch -P 24 -p1
%endif
%if %{have_snappy}
%patch -P 15 -p1
%endif
%if %{have_zstd}
%patch -P 30 -p1
%endif
## GDB patches
for f in %{S:100} %{S:101}; do
    base=`basename "$f"`
    cp "$f" "${base#%{name}-}"
done

%patch -P 32 -p1
%patch -P 100 -p1
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

## SIAL patches
cd sial-scripts-%{scripts_version}
%patch -P 90 -p1
cd -
cd extensions
## gcore extension
tar xfvj %{S:5}
cd -
cp %{S:3} .
mkdir kbuild
cp %{S:6} memory_driver
%if 0%{?suse_version} > 1550
%patch -P 99 -p1
%endif

%build
%ifarch ppc64le ppc64
# for ppc64le use -mfull-toc needed by lto as per boo#1146646
export CFLAGS="$RPM_OPT_FLAGS -fno-builtin-memset -fno-strict-aliasing -mfull-toc"
%else
export CFLAGS="$RPM_OPT_FLAGS -fno-builtin-memset -fno-strict-aliasing"
%endif
export GDB="gdb-%{gdb_version}"
make RPMPKG="`cat .rh_rpm_package`" %{?jobs:-j%jobs}
make extensions %{?jobs:-j%jobs}
%if 0%{?build_kmp}
export EXTRA_CFLAGS='-DVERSION=\"%version\"'
for flavor in %flavors_to_build; do
    rm -rf kbuild/$flavor
    cp -r memory_driver kbuild/$flavor
    make -C /usr/src/linux-obj/%arch/$flavor modules \
      M=$PWD/kbuild/$flavor
done
%endif

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_mandir}/man8
install -m 0644 crash.8 %{buildroot}%{_mandir}/man8/crash.8
# devel files
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/crash
install -m 0644 defs.h $RPM_BUILD_ROOT/%{_includedir}/crash
# permissions
chmod 644 COPYING3
# extensions
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/crash/extensions
install -m 0644 extensions/dminfo.so extensions/snap.so \
    $RPM_BUILD_ROOT/%{_libdir}/crash/extensions
%if %build_gcore
install -m 0644 extensions/gcore.so $RPM_BUILD_ROOT/%{_libdir}/crash/extensions
%endif
%if 0%{?build_kmp}
# memory driver module
export INSTALL_MOD_PATH=$RPM_BUILD_ROOT
export INSTALL_MOD_DIR=updates
for flavor in %flavors_to_build; do
     make -C /usr/src/linux-obj/%arch/$flavor modules_install \
       M=$PWD/kbuild/$flavor
done
%endif

%files
%defattr(-,root,root)
%{_bindir}/crash
%{_mandir}/man8/crash.8*
%license COPYING3
%doc README README.SUSE
%dir %{_libdir}/crash
%dir %{_libdir}/crash/extensions
%{_libdir}/crash/extensions/dminfo.so
%{_libdir}/crash/extensions/snap.so

%files devel
%defattr(-,root,root)
%{_includedir}/*

%files doc
%defattr(-,root,root)
%doc crash_whitepaper/*

%if %build_gcore

%files gcore
%defattr(-,root,root)
%{_libdir}/crash/extensions/gcore.so
%doc extensions/README.gcore
%endif

%changelog
