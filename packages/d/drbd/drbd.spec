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
Version:        9.0.30~1+git.8e9c0812
Release:        0
Summary:        Linux driver for the "Distributed Replicated Block Device"
License:        GPL-2.0-or-later
URL:            https://drbd.linbit.com/
Source:         %{name}-%{version}.tar.bz2
Source1:        preamble
#In kernel is: kernel/drivers/block/drbd/drbd.ko
Source2:        Module.supported
Source3:        drbd_git_revision
Patch1:         fix-resync-finished-with-syncs-have-bits-set.patch
Patch2:         bsc-1192929_01-make_block_holder_optional.patch
Patch3:         bsc-1192929_02-move_kvmalloc_related_to_slab.patch
Patch4:         bsc-1192929_03-polling_to_bio_base.patch
Patch5:         bsc-1192929_04-pass_gend_to_blk_queue_update_readahead.patch
Patch6:         bsc-1192929_07-add_disk_error_handle.patch
Patch7:         bsc-1192929_08-have_void_drbd_submit_bio.patch
Patch8:         bsc-1192929_09-remove_bdgrab.patch
Patch9:         bsc-1201335_01-compat-test-and-cocci-patch-for-bdi-in-gendisk.patch
Patch10:        bsc-1201335_02-compat-only-apply-bdi-pointer-patch-if-bdi-is-in-req.patch
Patch11:        bsc-1201335_03-genhd.patch
Patch12:        bsc-1201335_04-bio_alloc_bioset.patch
Patch13:        bsc-1201335_05-bio_alloc.patch
Patch14:        bsc-1201335_06-bdi.patch
Patch15:        bsc-1201335_07-write-same.patch
Patch16:        bsc-1201335_08-bio_clone_fast.patch
Patch17:        bsc-1202600_01-remove-QUEUE_FLAG_DISCARD.patch
Patch18:        bsc-1202600_02-dax-introduce-DAX_RECOVERY_WRITE-dax-access-mode.patch
Patch19:        bsc-1202600_03-block-decouple-REQ_OP_SECURE_ERASE-from-REQ_OP_DISCA.patch
Patch20:        bsc-1202600_04-remove-assign_p_sizes_qlim.patch
Patch21:        bsc-1204596_01-block-remove-blk_cleanup_disk.patch
Patch22:        bsc-1204596_02-drbd-remove-usage-of-bdevname.patch
Patch23:        bsc-1206791-01-drbd-add-comments-explaining-removal-of-bdi-congesti.patch
Patch24:        bsc-1206791-02-drbd-fix-static-analysis-warnings.patch
Patch25:        bsc-1206791-03-drbd-fix-warning-about-initializing-multiple-struct-.patch
Patch26:        bsc-1206791-04-blk_queue_split__no_present.patch
Patch27:        bsc-1206791-05-prandom_u32_max.patch
Patch28:        bsc-1206791-06-write_zeroes__no_capable.patch
Patch29:        bsc-1206791-07-drbd-fix-use-after-free-bugs-in-get_initial_state.patch
Patch30:        bsc-1206791-08-lib-lru_cache-Fixed-array-overflow-caused-by-incorre.patch
Patch31:        bsc-1206791-09-pmem-use-fs_dax_get_by_bdev-instead-of-dax_get_by_ho.patch
Patch99:        suse-coccinelle.patch
#https://github.com/openSUSE/rpmlint-checks/blob/master/KMPPolicyCheck.py
BuildRequires:  coccinelle >= 1.0.8
BuildRequires:  kernel-source
BuildRequires:  kernel-syms
BuildRequires:  libelf-devel
BuildRequires:  modutils
BuildRequires:  %kernel_module_package_buildreqs
Requires:       drbd-utils >= 9.2.0
Supplements:    drbd-utils >= 9.2.0
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
%setup -q -n drbd-%{version}
%patch1 -p1
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
%patch99 -p1

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
