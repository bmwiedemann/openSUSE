#
# spec file for package drbd-utils
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


%bcond_without drbdmon
# Man pages are included in the released tarball.
# Only need po4a to build man from git source code
%bcond_without prebuiltman
Name:           drbd-utils
Version:        9.14.0
Release:        0
Summary:        Distributed Replicated Block Device
License:        GPL-2.0-or-later
URL:            http://www.drbd.org/
Source:         http://www.linbit.com/downloads/drbd/utils/%{name}-%{version}.tar.gz
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch1:         init-script-fixes.diff
Patch2:         fix-libdir-in-Makefile.patch
Patch3:         fence-after-pacemaker-down.patch
# PATCH-SUSE-FIX: Disable quorum in default configuration (bsc#1032142)
Patch4:         0001-Disable-quorum-in-default-configuration-bsc-1032142.patch
Patch5:         move_fencing_from_disk_to_net_in_example.patch

Provides:       drbd-bash-completion = %{version}
Provides:       drbd-pacemaker = %{version}
Provides:       drbd-udev = %{version}
Obsoletes:      drbd-bash-completion < %{version}
Obsoletes:      drbd-pacemaker < %{version}
Obsoletes:      drbd-udev < %{version}
# drbd-utils first splict from drbd-8.4.5(only driver)
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
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

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
    --prefix=/ \
    --sbindir=/sbin \
    --libdir=%{_prefix}/lib \
    --mandir=%{_mandir} \
    --sysconfdir=%{_sysconfdir} \
    --datarootdir=%{_datadir} \
    --datadir=%{_datadir} \
    --libdir=%{_prefix}/lib \
    --exec_prefix=%{_prefix}/lib \
    %{?with_drbdmon:   --with-drbdmon}     \
    %{?with_prebuiltman: --with-prebuiltman} \
    --with-tmpfilesdir=%{_tmpfilesdir}

make OPTFLAGS="%{optflags}" %{?_smp_mflags}

%install
%make_install

mkdir -p %{buildroot}%{_localstatedir}/lib/drbd
%ifnarch %{ix86} x86_64
rm -rf %{buildroot}%{_sysconfdir}/xen
%else
d=%{_libexecdir}/xen/scripts
mkdir -p %{buildroot}$d
mv %{buildroot}%{_sysconfdir}/xen/scripts/block-drbd %{buildroot}$d
%if 0%{?suse_version} > 1500
rm -rf %{buildroot}%{_sysconfdir}/xen
%else
tee %{buildroot}%{_sysconfdir}/xen/scripts/block-drbd <<_EOS_
#!/bin/sh
# SUSE versions up to SLE15 populated /etc with files.
# This wrapper exists to remain compatible with their expected script path
exec $d/block-drbd "\$@"
_EOS_
%endif
%endif

%pre
%service_add_pre drbd.service

%post
%service_add_post drbd.service

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
%service_del_preun drbd.service

%postun
%service_del_postun drbd.service

%files -n drbd-utils
%defattr(-, root, root)
%config(noreplace) %{_sysconfdir}/drbd.conf
%config %{_sysconfdir}/bash_completion.d/drbdadm.sh
%config(noreplace) %{_sysconfdir}/drbd.d/global_common.conf
%config(noreplace) %{_sysconfdir}/multipath/conf.d/drbd.conf
%{_tmpfilesdir}/drbd.conf
%doc %{_mandir}/man5/drbd.*
%doc %{_mandir}/man8/drbd*
%doc %{_mandir}/man7/ocf_linbit_drbd.*
%doc %{_mandir}/ja/man5/drbd.*
%doc %{_mandir}/ja/man8/drbd*
%license COPYING
%doc README.md
%doc ChangeLog
%doc scripts/drbd.conf.example
%dir %{_sysconfdir}/drbd.d
%dir %{_sysconfdir}/multipath
%dir %{_sysconfdir}/multipath/conf.d
/sbin/drbdadm
/sbin/drbdsetup
/sbin/drbdmeta
%if %{with drbdmon}
/sbin/drbdmon
%endif
%ifarch %{ix86} x86_64
%if 0%{?suse_version} <= 1500
%dir %attr(700,root,root) %{_sysconfdir}/xen
%dir %{_sysconfdir}/xen/scripts
%attr(755,root,root) %{_sysconfdir}/xen/scripts/block-drbd
%endif
%{_libexecdir}/xen
%endif
%{_prefix}/lib/ocf/resource.d/linbit/drbd
%{_prefix}/lib/ocf/resource.d/linbit/drbd.shellfuncs.sh
%{_udevrulesdir}/65-drbd.rules
%{_unitdir}/drbd.service
%{_prefix}/lib/systemd/system/drbd.service
%defattr(-, root, root)
%{_localstatedir}/lib/drbd
%{_prefix}/lib/drbd
/lib/drbd
/lib/drbd/drbd*
%dir %{_prefix}/lib/ocf
%dir %{_prefix}/lib/ocf/resource.d
%dir %{_prefix}/lib/ocf/resource.d/linbit

%changelog
