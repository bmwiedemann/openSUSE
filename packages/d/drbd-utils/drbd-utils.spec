#
# spec file for package drbd-utils
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


%define services drbd.service drbd-graceful-shutdown.service drbd-lvchange@.service drbd-promote@.service drbd-demote-or-escalate@.service drbd-reconfigure-suspend-or-error@.service drbd-services@.target drbd-wait-promotable@.service drbd@.service drbd@.target ocf.ra@.service
%if 0%{?suse_version} < 1550
  # for SLEs
  %define sbindir /sbin
  # see bsc#1203220 & usrmerge_move_lib_to_prefix_lib.patch for %{libdir}
  %define libdir  /usr/lib
%else
  # for opensuse
  %define sbindir %{_sbindir}
  %define libdir  %{_prefix}/lib
%endif
%bcond_without drbdmon
# Man pages are included in the released tarball.
# Only need po4a to build man from git source code
%bcond_without prebuiltman
Name:           drbd-utils
Version:        9.29.0
Release:        0
Summary:        Distributed Replicated Block Device
License:        GPL-2.0-or-later
Group:          Productivity/Clustering/HA
URL:            https://linbit.com/linbit-software-download-page-for-linstor-and-drbd-linux-driver/
Source:         https://pkg.linbit.com//downloads/drbd/utils/%{name}-%{version}.tar.gz
Source100:      %{name}.rpmlintrc

#############################################
# Upstream patches
Patch0001:      0001-drbd-verify.py-relax-host-key-checking.patch
Patch0002:      0002-DRBDmon-Disabled-DRBD-commands-warning-only-for-actu.patch
Patch0003:      0003-DRBDmon-Integrate-global-local-command-delegation.patch
Patch0004:      0004-DRBDmon-Adjust-events-log-supplier-program-name.patch
Patch0005:      0005-DRBDmon-Add-drbd-events-log-supplier.patch
Patch0006:      0006-DRBDmon-Adjust-Makefile.patch
Patch0007:      0007-DRBDmon-Version-V1R4M1.patch
Patch0008:      0008-drbdadm-add-proxy-options-to-add-connection-command.patch
Patch0009:      0009-Do-not-hardcode-paths-in-services-and-scripts.patch
Patch0010:      0010-Fix-typo-in-warning-there-is-no-po4a-translage-comma.patch
Patch0011:      0011-drbd.ocf-explicitly-timeout-crm_master-IPC-early.patch
Patch0012:      0012-drbd.ocf-the-text-output-of-crm_resource-locate-has-.patch

# SUSE specific patches
Patch1001:      init-script-fixes.diff
Patch1002:      fence-after-pacemaker-down.patch
Patch1003:      bsc-1032142_Disable-quorum-in-default-configuration.patch
Patch1004:      move_fencing_from_disk_to_net_in_example.patch
Patch1005:      pie-fix.patch
Patch1006:      bsc-1233273_drbd.ocf-replace-crm_master-with-ocf_promotion_score.patch
Patch1007:      bsc-1233273_drbd.ocf-update-for-OCF-1.1.patch
Patch1008:      rpmlint-build-error.patch
#############################################

Provides:       drbd-bash-completion = %{version}
Provides:       drbd-pacemaker = %{version}
Provides:       drbd-udev = %{version}
Obsoletes:      drbd-bash-completion < %{version}
Obsoletes:      drbd-pacemaker < %{version}
Obsoletes:      drbd-udev < %{version}
# drbd-utils first split from drbd-8.4.5(only driver)
# and suse let drbd driver goes in-kernel
# Provides:       drbd = 8.4.5
# Obsoletes:      drbd < 8.4.5
%ifarch %{ix86} x86_64
Provides:       drbd-xen = %{version}
Obsoletes:      drbd-xen < %{version}
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
%if %{with drbdmon}
BuildRequires:  gcc-c++
%endif
%if %{without prebuiltman}
BuildRequires:  po4a
%endif
Provides:       drbd-control
Provides:       drbdsetup
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Drbd is a distributed replicated block device. It mirrors a block
device over the network to another machine. Think of it as networked
raid 1. It is a building block for setting up clusters.

%prep
%autosetup -p1

%build
export WANT_DRBD_REPRODUCIBLE_BUILD=1
./autogen.sh
PATH=/sbin:$PATH ./configure \
    --with-udev \
    --with-distro=suse \
    --without-heartbeat \
    --with-pacemaker \
    --with-xen \
    --with-bashcompletion \
    --with-initscripttype=systemd \
    --with-systemdunitdir=%{_prefix}/lib/systemd/system \
%if 0%{?suse_version} < 1550
    --sbindir=/sbin \
%else
    --sbindir=%{_sbindir} \
%endif
    --prefix=%{_prefix} \
    --localstatedir=%{_localstatedir} \
    --mandir=%{_mandir} \
    --sysconfdir=%{_sysconfdir} \
    --datarootdir=%{_datadir} \
    --datadir=%{_datadir} \
    --libdir=%{_prefix}/lib \
    --exec_prefix=%{_prefix}/lib \
    %{?with_drbdmon:   --with-drbdmon}     \
    %{?with_prebuiltman: --with-prebuiltman} \
    --with-tmpfilesdir=%{_tmpfilesdir} \
    --without-83support \
    --without-84support

%make_build OPTFLAGS="%{optflags}"

%install
%make_install

%ifnarch %{ix86} x86_64
rm -rf %{buildroot}%{_sysconfdir}/xen
%endif

rm -rf %{buildroot}%{libdir}/drbd/crm-*fence-peer.sh     # bsc#1204276

%pre
%service_add_pre %{services}

%post
%tmpfiles_create %{_tmpfilesdir}/drbd.conf
%service_add_post %{services}

#May also overlap the $MAN_LINK in documentation/v9/Makefile.in
for f in drbd drbdadm drbdmeta drbdsetup; do
    ln -sf $f-9.0.8.gz %{_mandir}/man8/$f.8.gz
    ln -sf $f-9.0.8.gz %{_mandir}/ja/man8/$f.8.gz
done
ln -sf drbd.conf-9.0.5.gz %{_mandir}/man5/drbd.conf.5.gz
ln -sf drbd.conf-9.0.5.gz %{_mandir}/ja/man5/drbd.conf.5.gz
%if %{with drbdmon}
  ln -sf drbdmon-9.0.8.gz %{_mandir}/man8/drbdmon.8.gz
  ln -sf drbdmon-9.0.8.gz %{_mandir}/ja/man8/drbdmon.8.gz
%endif

%preun
%service_del_preun %{services}

%postun
%service_del_postun %{services}

%if 0%{?suse_version} < 1550
if [ -d /lib/drbd ]; then
  rm -rf /lib/drbd.rpmmoved
  mv /lib/drbd /lib/drbd.rpmmoved
elif [ ! -e %{libdir}/drbd ] && [ -L /lib/drbd ]; then
  rm /lib/drbd
fi
%endif

%posttrans
%if 0%{?suse_version} < 1550
if [ ! -e /lib/drbd ]; then
  ln -sf %{libdir}/drbd /lib/drbd
fi
%endif

%files -n drbd-utils
%config(noreplace) %{_sysconfdir}/drbd.conf
%config(noreplace) %{_sysconfdir}/drbd.d/global_common.conf
%config(noreplace) %{_sysconfdir}/multipath/conf.d/drbd.conf
%{_datadir}/bash-completion/completions/drbdadm
%{_tmpfilesdir}/drbd.conf
%{_mandir}/man5/drbd.*
%{_mandir}/man8/drbd*
%{_mandir}/man7/ocf*
%{_mandir}/man7/drbd*
%{_mandir}/ja/man5/drbd.*
%{_mandir}/ja/man8/drbd*
%license COPYING
%doc README.md
%doc ChangeLog
%doc scripts/drbd.conf.example
%dir %{_sysconfdir}/drbd.d
%dir %{_sysconfdir}/multipath
%dir %{_sysconfdir}/multipath/conf.d
%{libdir}/drbd
%{sbindir}/drbdadm
%{sbindir}/drbdsetup
%{sbindir}/drbdmeta
%if %{with drbdmon}
%{sbindir}/drbdmon
%{sbindir}/drbd-events-log-supplier
%endif
%ifarch %{ix86} x86_64
%dir %attr(700,root,root) %{_sysconfdir}/xen
%dir %{_sysconfdir}/xen/scripts
%attr(755,root,root) %{_sysconfdir}/xen/scripts/block-drbd
%endif
%{_prefix}/lib/ocf/resource.d/linbit/drbd
%{_prefix}/lib/ocf/resource.d/linbit/drbd-attr
%{_prefix}/lib/ocf/resource.d/linbit/drbd.shellfuncs.sh
%{_udevrulesdir}/65-drbd.rules
%{_unitdir}/drbd.service
%{_unitdir}/drbd-graceful-shutdown.service
%{_unitdir}/drbd-lvchange@.service
%{_unitdir}/drbd-promote@.service
%{_unitdir}/drbd-demote-or-escalate@.service
%{_unitdir}/drbd-reconfigure-suspend-or-error@.service
%{_unitdir}/drbd-services@.target
%{_unitdir}/drbd-wait-promotable@.service
%{_unitdir}/drbd@.service
%{_unitdir}/drbd@.target
%{_unitdir}/ocf.ra@.service
%dir %{_prefix}/lib/ocf
%dir %{_prefix}/lib/ocf/resource.d
%dir %{_prefix}/lib/ocf/resource.d/linbit
%dir %{_localstatedir}/lib/drbd

%changelog
