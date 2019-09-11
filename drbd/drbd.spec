#
# spec file for package drbd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if ! 0%{?is_opensuse}
%ifarch x86_64
%define buildrt 1
%endif
%endif

Name:           drbd
Version:        9.0.19~1+git.8e93a5d9
Release:        0
Summary:        Linux driver for the "Distributed Replicated Block Device"
License:        GPL-2.0-or-later
Group:          Productivity/Clustering/HA
URL:            https://drbd.linbit.com/
Source:         %{name}-%{version}.tar.bz2
Source1:        preamble
#In kernel is: kernel/drivers/block/drbd/drbd.ko
Source2:        Module.supported
Source3:        drbd_git_revision
Patch1:         fix-resync-finished-with-syncs-have-bits-set.patch
Patch2:         rely-on-sb-handlers.patch
BuildRequires:  kernel-source
BuildRequires:  kernel-syms
BuildRequires:  libelf-devel
#https://github.com/openSUSE/rpmlint-checks/blob/master/KMPPolicyCheck.py
BuildRequires:  coccinelle
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
Group:          Productivity/Clustering/HA
Url:            http://drbd.linbit.com/

%description KMP
This module is the kernel-dependent driver for DRBD. This is split out so
that multiple kernel driver versions can be installed, one for each
installed kernel.

%prep
%setup -q -n drbd-%{version}
%patch1 -p1
%patch2 -p1

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

for flavor in %{flavors_to_build}; do
    rm -rf $flavor
    cp -r source $flavor
    cp %{_sourcedir}/Module.supported $flavor
    export DRBDSRC="$PWD/obj/$flavor"
    make -C %{kernel_source $flavor} modules M=$PWD/$flavor

    #Check the compat result
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
%doc COPYING
%doc ChangeLog
%{_sbindir}/rc%{name}

%changelog
