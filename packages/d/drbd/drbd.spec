#
# spec file for package drbd
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
# needssslcertforbuild


# RT enabled in Leap15.2(but not in Tumbleweed)
%if ! 0%{?is_opensuse} || 0%{?sle_version} >= 150200
%ifarch x86_64
%define buildrt 1
%endif
%endif
Name:           drbd
Version:        9.0.25~0+git.bd41626d
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
Patch2:         rely-on-sb-handlers.patch
Patch3:         drbd-fix-zero-metadata-limit-by-page-size-misaligned.patch
Patch4:         compat_remove_pgprot_88dca4c.patch
Patch5:         compat_remove_include_vermagic.patch
Patch6:         compat_remove_kernel_setsockopt.patch
# Compat to kernel v5.9
Patch7:         compat_generic_make_request.patch
Patch8:         blk_alloc_queue_make_request.patch
Patch9:         remove_congested_fn_congested_data.patch
Patch10:        compat_blk_queue_stack_limits.patch
Patch11:        fix-err-of-wrong-return-type.patch
Patch99:        suse-coccinelle.patch
#https://github.com/openSUSE/rpmlint-checks/blob/master/KMPPolicyCheck.py
BuildRequires:  coccinelle >= 1.0.8
BuildRequires:  kernel-source
BuildRequires:  kernel-syms
BuildRequires:  libelf-devel
BuildRequires:  modutils
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
ln -s -f %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{name}
rm -f drbd.conf

%files
%license COPYING
%doc ChangeLog
%{_sbindir}/rc%{name}

%changelog
