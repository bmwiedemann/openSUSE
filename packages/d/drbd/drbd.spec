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
Version:        9.1.22
Release:        0
Summary:        Linux driver for the "Distributed Replicated Block Device"
License:        GPL-2.0-or-later
URL:            https://pkg.linbit.com/
Source:         %{name}-%{version}.tar.gz
Source1:        preamble
Source2:        Module.supported
Source3:        drbd_git_revision

########################
# upstream patch
Patch0001:  0001-drbd-properly-rate-limit-resync-progress-reports.patch
Patch0002:  0002-drbd-inherit-history-UUIDs-from-sync-source-when-res.patch
Patch0003:  0003-build-compat-fix-line-offset-in-annotation-pragmas-p.patch
Patch0004:  0004-drbd-fix-exposed_uuid-going-backward.patch
Patch0005:  0005-drbd-Proper-locking-around-new_current_uuid-on-a-dis.patch
Patch0006:  0006-build-CycloneDX-fix-bom-ref-add-purl.patch
Patch0007:  0007-build-Another-update-to-the-spdx-files.patch
Patch0008:  0008-build-generate-spdx.json-not-tag-value-format.patch
Patch0009:  0009-compat-fix-gen_patch_names-for-bdev_file_open_by_pat.patch
Patch0010:  0010-compat-fix-nla_nest_start_noflag-test.patch
Patch0011:  0011-compat-fix-blk_alloc_disk-rule.patch
Patch0012:  0012-drbd-remove-const-from-function-return-type.patch
Patch0013:  0013-drbd-don-t-set-max_write_zeroes_sectors-in-decide_on.patch
Patch0014:  0014-drbd-split-out-a-drbd_discard_supported-helper.patch
Patch0015:  0015-drbd-atomically-update-queue-limits-in-drbd_reconsid.patch
Patch0016:  0016-compat-test-and-patch-for-queue_limits_start_update.patch
Patch0017:  0017-compat-specify-which-essential-change-was-not-made.patch
Patch0018:  0018-gen_patch_names-reorder-blk_mode_t.patch
Patch0019:  0019-compat-fix-blk_queue_update_readahead-patch.patch
Patch0020:  0020-compat-test-and-patch-for-que_limits-max_hw_discard_.patch
Patch0021:  0021-compat-fixup-write_zeroes__no_capable.patch
Patch0022:  0022-compat-fixup-queue_flag_discard__yes_present.patch
Patch0023:  0023-drbd-move-flags-to-queue_limits.patch
Patch0024:  0024-compat-test-and-patch-for-queue_limits.features.patch
Patch0025:  0025-drbd-Annotate-struct-fifo_buffer-with-__counted_by.patch
Patch0026:  0026-compat-test-and-patch-for-__counted_by.patch
Patch0027:  0027-drbd-fix-function-cast-warnings-in-state-machine.patch
Patch0028:  0028-Add-missing-documentation-of-peer_device-parameter-t.patch
#  0029-ci-update-build-helpers.patch is fedora special, we ignore it.
Patch0029:  0030-drbd-kref_put-path-when-kernel_accept-fails.patch
Patch0030:  0031-build-fix-typo-in-Makefile.spatch.patch
Patch0031:  0032-drbd-open-do-not-delay-open-if-already-Primary.patch

# suse special patch
Patch1001:  bsc-1025089_fix-resync-finished-with-syncs-have-bits-set.patch
Patch1002:  suse-coccinelle.patch
Patch1003:  boo1231290_fix_drbd_build_error_against_kernel_v6.11.0.patch
Patch1004:  boo1233222_fix_drbd_build_error_against_kernel_v6.11.6.patch
########################

#https://github.com/openSUSE/rpmlint-checks/blob/master/KMPPolicyCheck.py
BuildRequires:  coccinelle >= 1.0.8
BuildRequires:  kernel-source
BuildRequires:  kernel-syms
BuildRequires:  libelf-devel
BuildRequires:  modutils
BuildRequires:  perl
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
    cp -a -r drbd $flavor
    cp $RPM_SOURCE_DIR/drbd_git_revision ${flavor}/.drbd_git_revision

    export DRBDSRC="$PWD/obj/$flavor"
    # bsc#1160194, check the coccicheck work.
    #make coccicheck

    # call make prep to generate drbd build dir
    make %{?_smp_mflags} -C $flavor KDIR=%{kernel_source $flavor} prep SPAAS=${SPAAS}

    cp -a %{_sourcedir}/Module.supported ${flavor}/build-current

    make %{?_smp_mflags} -C %{kernel_source $flavor} modules M=$PWD/$flavor/build-current SPAAS=${SPAAS}

    # Check the compat result
    cat $PWD/${flavor}/build-current/compat.h
done

%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
for flavor in %{flavors_to_build}; do
    make -C %{kernel_source $flavor} modules_install M=$PWD/$flavor/build-current
done

mkdir -p %{buildroot}/%{_sbindir}
ln -s service %{buildroot}/%{_sbindir}/rc%{name}
rm -f drbd.conf

%files
%license COPYING
%doc ChangeLog
%{_sbindir}/rc%{name}

%changelog
