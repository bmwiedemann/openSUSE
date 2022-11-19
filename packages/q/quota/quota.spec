#
# spec file for package quota
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           quota
Version:        4.09
Release:        0
Summary:        Disk Quota System
License:        GPL-2.0-only
Group:          System/Filesystems
URL:            https://sourceforge.net/projects/linuxquota/
Source0:        https://downloads.sourceforge.net/project/linuxquota/quota-tools/%{version}/%{name}-%{version}.tar.gz
Source1:        sysconfig.nfs-quota
Source2:        quotad.service
Source3:        quotad_env.sh
BuildRequires:  e2fsprogs-devel
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  rpcgen
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libnl-3.0) >= 3.1
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(systemd)

%description
The quota subsystem allows a system administrator to set soft and hard
limits on used space and the number of inodes used for users and
groups. The kernel must be compiled with disk quota support enabled
(SUSE kernels have this support).

%package nfs
Summary:        Disk Quota System on NFS
Group:          System/Filesystems
Requires:       nfs-kernel-server
Requires:       quota = %{version}
# Require the services needed to be present for quotad service: portmap, nfsserver, network
Requires:       rpcbind
Requires:       sysconfig
Requires(post): %fillup_prereq
%{?systemd_requires}

%description nfs
The quotad init script, which provides quota support on NFS mounts.

%prep
%setup -q

%build
%configure \
    --docdir=%{_docdir}/%{name} \
    --disable-silent-rules \
    --enable-ldapmail \
    --enable-rpc \
    --enable-rpcsetquota
%make_build

%install
%make_install

#installing ldap-scripts
install -m 755 ldap-scripts/*pl %{buildroot}%{_sbindir}/
install -m 755 ldap-scripts/edquota_editor %{buildroot}%{_sbindir}/

mkdir -p %{buildroot}%{_unitdir}
cp %{SOURCE2} %{buildroot}%{_unitdir}/quotad.service
ln -s service %{buildroot}%{_sbindir}/rcquotad
# systemd unit file sucks so bash script to work around it is provided
install -d -m 755 %{buildroot}%{_unitdir}/../scripts/
install -m 755 %{SOURCE3} %{buildroot}%{_unitdir}/../scripts/quotad_env.sh

install -d -m 755 %{buildroot}%{_fillupdir}
cp %{SOURCE1} %{buildroot}%{_fillupdir}/sysconfig.nfs-quota

%find_lang %{name}

%pre nfs
%service_add_pre quotad.service

%post nfs
%{fillup_only -an nfs}
%service_add_post quotad.service

%preun nfs
%service_del_preun quotad.service

%postun nfs
%service_del_postun quotad.service

%files -f %{name}.lang
%license COPYING
%config %{_sysconfdir}/quotagrpadmins
%config %{_sysconfdir}/quotatab
%config %{_sysconfdir}/warnquota.conf
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*
%{_mandir}/man?/*
%{_bindir}/quota
%{_bindir}/quotasync
%{_sbindir}/applySystemQuotas.pl
%{_sbindir}/convertquota
%{_sbindir}/edquota
%{_sbindir}/edquota_editor
%{_sbindir}/quota_nld
%{_sbindir}/quotacheck
%{_sbindir}/quotaoff
%{_sbindir}/quotaon
%{_sbindir}/quotastats
%{_sbindir}/repquota
%{_sbindir}/setSystemQuotas.pl
%{_sbindir}/setquota
%{_sbindir}/setquota-ldap.pl
%{_sbindir}/warnquota
%{_sbindir}/xqmstats

%files nfs
%{_sbindir}/rpc.rquotad
%{_sbindir}/rcquotad
%{_unitdir}/quotad.service
%{_unitdir}/../scripts
%{_unitdir}/../scripts/quotad_env.sh
%{_fillupdir}/sysconfig.nfs-quota
# these files conflicts with glibc rpm
%exclude %{_includedir}/rpcsvc/*

%changelog
