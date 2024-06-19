#
# spec file for package drbd
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
# needssslcertforbuild


# RT enabled in Leap15.2(but not in Tumbleweed)
%if ! 0%{?is_opensuse} || 0%{?sle_version} >= 150200
%ifarch x86_64
%define buildrt 1
%endif
%endif
Name:           drbd
Version:        9.1.16
Release:        0
Summary:        Linux driver for the "Distributed Replicated Block Device"
License:        GPL-2.0-or-later
URL:            https://drbd.linbit.com/
Source:         %{name}-%{version}.tar.gz
Source1:        preamble
Source2:        Module.supported
Source3:        drbd_git_revision

########################
# upstream patch
Patch0001:   0001-drbd-allow-transports-to-take-additional-krefs-on-a-.patch
Patch0002:   0002-drbd-improve-decision-about-marking-a-failed-disk-Ou.patch
Patch0003:   0003-drbd-fix-error-path-in-drbd_get_listener.patch
Patch0004:   0004-drbd-build-fix-spurious-re-build-attempt-of-compat.p.patch
Patch0005:   0005-drbd-log-error-code-when-thread-fails-to-start.patch
Patch0006:   0006-drbd-log-numeric-value-of-drbd_state_rv-as-well-as-s.patch
Patch0007:   0007-drbd-stop-defining-__KERNEL_SYSCALLS__.patch
Patch0008:   0008-compat-block-introduce-holder-ops.patch
Patch0009:   0009-drbd-reduce-net_ee-not-empty-info-to-a-dynamic-debug.patch
Patch0010:   0010-drbd-do-not-send-P_CURRENT_UUID-to-DRBD-8-peer-when-.patch
Patch0011:   0011-compat-block-pass-a-gendisk-to-open.patch
Patch0012:   0012-drbd-Restore-DATA_CORKED-and-CONTROL_CORKED-bits.patch
Patch0013:   0013-drbd-remove-unused-extern-for-conn_try_outdate_peer.patch
Patch0014:   0014-drbd-include-source-of-state-change-in-log.patch
Patch0015:   0015-compat-block-use-the-holder-as-indication-for-exclus.patch
Patch0016:   0016-drbd-Fix-net-options-set-defaults-to-not-clear-the-t.patch
Patch0017:   0017-drbd-propagate-exposed-UUIDs-only-into-established-c.patch
Patch0018:   0018-drbd-rework-autopromote.patch
Patch0019:   0019-compat-block-remove-the-unused-mode-argument-to-rele.patch
Patch0020:   0020-drbd-do-not-allow-auto-demote-to-be-interrupted-by-s.patch
Patch0021:   0021-compat-sock-Remove-sendpage-in-favour-of-sendmsg-MSG.patch
Patch0022:   0022-compat-block-replace-fmode_t-with-a-block-specific-t.patch
Patch0023:   0023-compat-genetlink-remove-userhdr-from-struct-genl_inf.patch
Patch0024:   0024-compat-fixup-FMODE_READ-FMODE_WRITE-usage.patch
Patch0025:   0025-compat-drdb-Convert-to-use-bdev_open_by_path.patch
Patch0026:   0026-compat-gate-blkdev_-patches-behind-bdev_open_by_path.patch
# suse special patch
Patch1001:   bsc-1025089_fix-resync-finished-with-syncs-have-bits-set.patch
Patch1002:   suse-coccinelle.patch
Patch1003:   bsc1226510-fix-build-err-against-6.9.3.patch
########################

#https://github.com/openSUSE/rpmlint-checks/blob/master/KMPPolicyCheck.py
BuildRequires:  coccinelle >= 1.0.8
BuildRequires:  kernel-source
BuildRequires:  kernel-syms
BuildRequires:  libelf-devel
BuildRequires:  modutils
BuildRequires:  %kernel_module_package_buildreqs
Requires:       drbd-utils >= 9.3.0
Supplements:    drbd-utils >= 9.3.0
Obsoletes:      drbd-kmp < %{version}
ExcludeArch:    i586 s390
%kernel_module_package -n drbd -p %{_sourcedir}/preamble
%if 0%{?buildrt} == 1
BuildRequires:  kernel-source-rt
BuildRequires:  kernel-syms-rt
%endif

%description
DRBD is a distributed replicated block device. It mirrors a block
device over the network to another machine. Think of it as networked
raid 1. It is a building block for setting up clusters.

%package KMP
Summary:        Kernel driver
URL:            http://drbd.linbit.com/

%description KMP
This module is the kernel-dependent driver for DRBD. This is split out so
that multiple kernel driver versions can be installed, one for each
installed kernel.

%prep
%autosetup -p1 -n drbd-%{version}

mkdir source
cp -a drbd/. source/. || :
cp $RPM_SOURCE_DIR/drbd_git_revision source/.drbd_git_revision

%build
rm -rf obj
mkdir obj
ln -s ../scripts obj/

export WANT_DRBD_REPRODUCIBLE_BUILD=1
export CONFIG_BLK_DEV_DRBD=m
export EXTRA_CFLAGS='-DVERSION=\"%{version}\"'
# Unset SPAAS or set as 'true' will use `spatch-as-a-service` from drbd.io
# when "coccinelle" not installed. Set SPAAS to 'false' to force an ERROR.
export SPAAS='false'

for flavor in %{flavors_to_build}; do
    rm -rf $flavor
    cp -a -r source $flavor
    cp -a %{_sourcedir}/Module.supported $flavor
    export DRBDSRC="$PWD/obj/$flavor"
    # bsc#1160194, check the coccicheck work.
    #make coccicheck
    make %{?_smp_mflags} -C %{kernel_source $flavor} modules M=$PWD/$flavor SPAAS=${SPAAS}

    # Check the compat result
    cat $PWD/$flavor/compat.h
done

%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
for flavor in %{flavors_to_build}; do
    make -C %{kernel_source $flavor} modules_install M=$PWD/$flavor
done

mkdir -p %{buildroot}/%{_sbindir}
ln -s service %{buildroot}/%{_sbindir}/rc%{name}
rm -f drbd.conf

%files
%license COPYING
%doc ChangeLog
%{_sbindir}/rc%{name}

%changelog
