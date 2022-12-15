#
# spec file for package crash
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
# needssslcertforbuild


%define whitepaper_version 2003
%define scripts_version  2008-02-08
%define gcore_version  2011-09-22

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

Name:           crash
%ifarch ppc
%define build_sial 0
%define build_eppic 0
%else
%define build_sial 0
%define build_eppic 1
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
URL:            https://crash-utility.github.io/
Summary:        Crash utility for live systems; netdump, diskdump, LKCD or mcore dumpfiles
License:        GFDL-1.2-only AND GPL-3.0-or-later
Group:          Development/Tools/Debuggers
Version:        7.3.1
Release:        0
Source:         https://github.com/crash-utility/crash/archive/7.3.1.tar.gz#/%{name}-%{version}.tar.gz
Source1:        http://ftp.gnu.org/gnu/gdb/gdb-7.6.tar.gz
Source2:        crash_whitepaper-%{whitepaper_version}.tar.bz2
Source3:        README.SUSE
Source4:        sial-scripts-%{scripts_version}.tar.bz2
Source5:        gcore-%{gcore_version}.tar.bz2
Source6:        Module.supported
Source7:        http://ftp.gnu.org/gnu/gdb/gdb-7.6.tar.gz.sig
Source8:        gnu.keyring
Source95:       get-kernel-flavors.sh
Source96:       depmod.sh
Source97:       mkinitrd.sh
Source98:       %{name}-kmp-preamble
Source99:       crash-rpmlintrc
Source100:      %{name}-gdb-7.6.series
Patch1:         %{name}-make-emacs-default.diff
Patch2:         %{name}-sles9-quirk.patch
Patch4:         %{name}-sles9-time.patch
Patch8:         %{name}-missing-declarations.patch
Patch9:         %{name}-debuginfo-compressed.patch
Patch10:        %{name}_enable_lzo_support.patch
Patch11:        %{name}-compressed-booted-kernel.patch
Patch12:        eppic-switch-to-system-lib.patch
Patch13:        %{name}-patch-gdb.patch
Patch15:        %{name}_enable_snappy_support.patch
Patch16:        eppic-support-arm64.patch
Patch18:        %{name}-stop_read_error_when_intent_is_retry.patch
Patch21:        %{name}-allow-use-of-sadump-captured-KASLR-kernel.patch
Patch23:        %{name}-SLE15-SP1-With-Linux-4.19-rc1-up-MAX_PHYSMEM_BITS-to-128TB.patch
Patch24:        %{name}-SLE15-SP1-Fix-for-PPC64-kernel-virtual-address-translation-in.patch
Patch27:        %{name}-Define-fallback-PN_XNUM.patch
Patch29:        eppic-remove-duplicate-symbols.patch
Patch30:        %{name}-enable-zstd-support.patch
Patch31:        %{name}-extensions-rule-for-defs.patch
Patch66:        0019-Add-kernel-version-dependent-check-for-getting-lengt.patch
Patch90:        %{name}-sial-ps-2.6.29.diff
Patch99:        %{name}-usrmerge.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libeppic-devel
BuildRequires:  lzo-devel
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
ExclusiveArch:  %ix86 x86_64 ia64 s390 s390x ppc64 ppc64le alpha aarch64
# Source code says it can do ppc32. Excluded here?
ExcludeArch:    ppc
%if 0%{?build_kmp}
BuildRequires:  kernel-syms
%endif
%ifarch x86_64
%if 0%{?suse_version} >= 1520 && 0%{?suse_version} < 1550
BuildRequires:  kernel-syms-rt
%endif
%endif
%if 0%{?suse_version} >= 1130
BuildRequires:  kernel-devel
%endif
BuildRequires:  %kernel_module_package_buildreqs
BuildRequires:  module-init-tools

%if 0%{?build_kmp}
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

%if %build_eppic
%package eppic
Requires:       %{name} = %{version}
%if %build_sial
# Nothing to do
%else
Provides:       %{name}-sial = %{version}
Obsoletes:      %{name}-sial < %{version}
%endif
Summary:        Embeddable Pre-Processor and Interpreter for C extension for crash
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers

%description eppic
EPPIC is a C interpreter that permits easy access to the symbol and type
information stored in a executable image like a coredump or live memory
interfaces (e.g. /dev/kmem, /dev/mem). Although it has a strong association
with live or postmortem kernel analysis, it is not constraint to it and can be
embedded in any tools that is C friendly.


Authors:
--------
    Luc Chouinard <lucchouina@gmail.com>

%endif

%if %build_sial

%package sial
Requires:       %{name} = %{version}
Summary:        SIAL extension for crash
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers

%description sial
This module is a prerequisite for the loading of SIAL scripts.

Upon loading the sial.so object file with extend, any SIAL scripts
located in the /usr/share/sial/crash or $HOME/.sial directories will be
loaded automatically.



Authors:
--------
    David Anderson <anderson@redhat.com>

%endif

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
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch13 -p1
%patch18 -p1
%patch21 -p1
# Patches for SLE 15 SP1 potentially break support for SLE15 and SLE 12 SP4
# Don't apply on these (and earlier) versions - see bsc#1148197
%if 0%{?sle_version} > 120400 && 0%{?sle_version} != 150000
%patch23 -p1
%patch24 -p1
%endif
%patch27 -p1
%patch66 -p1
%if %{have_snappy}
%patch15 -p1
%endif
%if %{have_zstd}
%patch30 -p1
%endif
## GDB patches
#for f in %{S:XXX} ; do
#    base=`basename "$f"`
#    cp "$f" "${base#%{name}-}"
#done

%patch31 -p1

## SIAL patches
cd sial-scripts-%{scripts_version}
%patch90 -p1
cd -
## gcore extension
cd extensions
tar xfvj %{S:5}
cd -
%patch12 -p1
%patch16 -p1
%patch29 -p1
cp %{S:3} .
mkdir kbuild
cp %{S:6} memory_driver
%if 0%{?suse_version} > 1550
%patch99 -p1
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
%if %build_eppic
install -m 0644 extensions/eppic.so $RPM_BUILD_ROOT/%{_libdir}/crash/extensions
%endif
%if %build_sial
install -m 0644 extensions/sial.so $RPM_BUILD_ROOT/%{_libdir}/crash/extensions
%endif
%if %build_eppic
# scripts
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/sial/crash
install -m 0644 sial-scripts-%{scripts_version}/*.c \
                $RPM_BUILD_ROOT/%{_datadir}/sial/crash
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

%clean
rm -rf %{buildroot}

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

%if %build_eppic
%files eppic
%defattr(-,root,root)
%{_libdir}/crash/extensions/eppic.so
%{_datadir}/sial/crash
%dir %{_datadir}/sial
%endif

%if %build_sial
%files sial
%defattr(-,root,root)
%doc extensions/libsial/README
%{_libdir}/crash/extensions/sial.so
%{_datadir}/sial/crash
%dir %{_datadir}/sial
%endif

%if %build_gcore

%files gcore
%defattr(-,root,root)
%{_libdir}/crash/extensions/gcore.so
%doc extensions/README.gcore
%endif

%changelog
