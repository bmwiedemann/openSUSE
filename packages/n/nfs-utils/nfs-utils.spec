#
# spec file for package nfs-utils
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
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           nfs-utils
Version:        2.6.2
Release:        0
Summary:        Support Utilities for Kernel nfsd
License:        GPL-2.0-or-later
Group:          Productivity/Networking/NFS
URL:            https://kernel.org/pub/linux/utils/nfs-utils/
Source0:        https://kernel.org/pub/linux/utils/nfs-utils/%{version}/nfs-utils-%{version}.tar.xz
Source4:        sysconfig.nfs
Source11:       idmapd.conf
Source12:       statd-user.conf
Source13:       nfs-utils.rpmlintrc
Source20:       nfs-mountd.options.conf
Source21:       nfs-server.options.conf
Source22:       rpc-gssd.options.conf
Source23:       rpc-statd.options.conf
Source24:       rpc-statd-notify.options.conf
Source25:       rpc-svcgssd.options.conf
Source26:       nfs.conf
Source27:       nfs-kernel-server.tmpfiles.conf
Patch0:         nfs-utils-1.0.7-bind-syntax.patch
Patch5:         0005-modprobe-avoid-error-messages-if-sbin-sysctl-fail.patch
Patch6:         0006-nfsd-allow-server-scope-to-be-set-with-config-or-com.patch
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  rpcgen
BuildRequires:  sysuser-tools
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(kdb)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(sqlite3)
Suggests:       python-base
%{?systemd_ordering}

%description
This package contains the NFS utilities. You can tune the number of
server threads via the sysconfig variable USE_KERNEL_NFSD_NUMBER. For
quota over NFS support, install the quota package.

%package -n nfs-client
Summary:        Support Utilities for NFS
Group:          Productivity/Networking/NFS
Requires:       keyutils
Requires:       netcfg
Requires:       rpcbind
Requires(post): %fillup_prereq
Requires(pre):  permissions
Obsoletes:      nfs-utils < 1.1.0
%sysusers_requires

%description -n nfs-client
This package contains common NFS utilities which are needed for client
and kernel based server.

%package -n nfs-kernel-server
Summary:        Support Utilities for Kernel nfsd
Group:          Productivity/Networking/NFS
Requires:       netcfg
Requires:       nfs-client = %{version}
Requires:       rpcbind
Requires:       (kmod(nfsd.ko) if kernel)
Conflicts:      nfs-server
Provides:       nfs-utils = %{version}
Obsoletes:      nfs-utils < 1.1.0
PreReq:         permissions

%description -n nfs-kernel-server
This package contains support for the kernel based NFS server. You can
tune the number of server threads via the sysconfig variable
USE_KERNEL_NFSD_NUMBER. For quota over NFS support, install the quota
package.

%package -n libnfsidmap1
Summary:        NFSv4 ID Mapping Library
Group:          Productivity/Networking/NFS
Version:        1.0
Release:        0
Obsoletes:      nfsidmap

%package -n nfsidmap-devel
Summary:        NFSv4 ID Mapping Library development libraries
Group:          Development/Libraries/C and C++
Version:        1.0
Release:        0
Requires:       libnfsidmap1 = %{version}

%description -n libnfsidmap1
In NFSv4, identities of users are conveyed by names rather than user ID
and group ID. Both the NFS server and client code in the kernel need to
translate these to numeric IDs.

%description -n nfsidmap-devel
In NFSv4, identities of users are conveyed by names rather than user ID
and group ID. Both the NFS server and client code in the kernel need to
translate these to numeric IDs.

%prep
%autosetup -p1

%build
autoreconf -fvi
export CFLAGS="%{optflags} -fPIE"
export LDFLAGS="-pie"
%configure \
	--with-systemd \
	--enable-nfsv4 \
	--enable-gss \
	--enable-svcgss \
	--enable-ipv6 \
	--enable-nfsdcltrack \
	--enable-mount \
	--enable-libmount-mount \
	--disable-static \
	--disable-sbin-override \
	--with-pluginpath=%{_libdir}/libnfsidmap-1.0.0 \
	--enable-mountconfig
make %{?_smp_mflags}
%sysusers_generate_pre %{SOURCE12} statd statd-user.conf

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
find %{buildroot} -type f -name '*.la' -delete -print
install -D -m 644 %{SOURCE20} %{buildroot}%{_unitdir}/nfs-mountd.service.d/options.conf
install -D -m 644 %{SOURCE21} %{buildroot}%{_unitdir}/nfs-server.service.d/options.conf
install -D -m 644 %{SOURCE22} %{buildroot}%{_unitdir}/rpc-gssd.service.d/options.conf
install -D -m 644 %{SOURCE23} %{buildroot}%{_unitdir}/rpc-statd.service.d/options.conf
install -D -m 644 %{SOURCE24} %{buildroot}%{_unitdir}/rpc-statd-notify.service.d/options.conf
install -D -m 644 %{SOURCE25} %{buildroot}%{_unitdir}/rpc-svcgssd.service.d/options.conf
install -D -m 644 %{SOURCE26} %{buildroot}%{_sysconfdir}/nfs.conf
install -D -m 644 %{SOURCE27} %{buildroot}%{_prefix}/lib/tmpfiles.d/nfs-kernel-server.conf
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcnfs-server
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcnfs-client
# sysconfig-data
mkdir -p %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE4} %{buildroot}%{_fillupdir}
# idmapd setup
install -D -m 644 %{SOURCE11} %{buildroot}%{_sysconfdir}/idmapd.conf
mkdir -p -m 755 %{buildroot}%{_localstatedir}/lib/nfs/rpc_pipefs
mkdir -p -m 755 %{buildroot}%{_localstatedir}/lib/nfs/v4recovery
# sm-notify state
mkdir -p -m 755 %{buildroot}%{_localstatedir}/lib/nfs/sm
mkdir -p -m 755 %{buildroot}%{_localstatedir}/lib/nfs/sm.bak
touch %{buildroot}%{_localstatedir}/lib/nfs/state
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services
install -m 644 utils/mount/nfsmount.conf %{buildroot}%{_sysconfdir}/nfsmount.conf
#
# hack to avoid automatic python dependency
chmod 644 `grep -l -r '^#!/usr/bin/python' %{buildroot}%{_sbindir}`
# Install sysusers.d template
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE12} %{buildroot}%{_sysusersdir}/

%pre -n nfs-client -f statd.pre
%service_add_pre auth-rpcgss-module.service nfs-idmapd.service nfs-blkmap.service rpc-statd-notify.service rpc-gssd.service rpc-statd.service rpc-svcgssd.service

%post -n nfs-client
# lib/nfs must be root-owned.
# sm and sm.back and contents should be statd:statd,
# but only chown if the dirs are currently root-owned.
# This is needed for some upgraded, but chown is best avoided
# when not necessary
chown root:root %{_localstatedir}/lib/nfs > /dev/null 2>&1 || :
for i in sm sm.bak; do
    p=%{_localstatedir}/lib/nfs/$i
    if [ -d "$b" -a -n "`chown 2> /dev/null -c --from root statd:statd $p`" ]; then
	chown -R statd:statd $p > /dev/null 2>&1 || :
    fi
done
### migrate from /var/lock/subsys
[ -d /run/nfs ] || mkdir /run/nfs
if [ -f %{_localstatedir}/lock/subsys/nfs-rpc.idmapd ]; then
	mv %{_localstatedir}/lock/subsys/nfs-rpc.idmapd /run/nfs
fi
if [ -f %{_localstatedir}/lock/subsys/nfsserver-rpc.idmapd ]; then
	mv %{_localstatedir}/lock/subsys/nfsserver-rpc.idmapd /run/nfs
fi
###
%{fillup_only -n nfs nfs}
#
%set_permissions %{_sbindir}/mount.nfs
/sbin/ldconfig
%service_add_post auth-rpcgss-module.service nfs-idmapd.service nfs-blkmap.service rpc-statd-notify.service rpc-gssd.service rpc-statd.service rpc-svcgssd.service

%preun -n nfs-client
%service_del_preun auth-rpcgss-module.service nfs-idmapd.service nfs-blkmap.service rpc-statd-notify.service rpc-gssd.service rpc-statd.service rpc-svcgssd.service

%postun -n nfs-client
/sbin/ldconfig
%service_del_postun auth-rpcgss-module.service nfs-idmapd.service nfs-blkmap.service rpc-statd-notify.service rpc-gssd.service rpc-statd.service rpc-svcgssd.service

%verifyscript -n nfs-client
%verify_permissions -e %{_sbindir}/mount.nfs

%pre -n nfs-kernel-server
%service_add_pre nfs-svcgssd.service nfs-mountd.service nfs-server.service

%preun -n nfs-kernel-server
%service_del_preun nfs-svcgssd.service nfs-mountd.service nfs-server.service

%post -n nfs-kernel-server
### migrate from /var/lock/subsys
[ -d /run/nfs ] || mkdir /run/nfs
if [ -f %{_localstatedir}/lock/subsys/nfs-rpc.idmapd ]; then
	mv %{_localstatedir}/lock/subsys/nfs-rpc.idmapd /run/nfs
fi
if [ -f %{_localstatedir}/lock/subsys/nfsserver-rpc.idmapd ]; then
	mv %{_localstatedir}/lock/subsys/nfsserver-rpc.idmapd /run/nfs
fi
###
%service_add_post nfs-mountd.service nfs-server.service nfsdcld.service
%tmpfiles_create nfs-kernel-server.conf
%set_permissions /var/lib/nfs/rmtab

%postun -n nfs-kernel-server
%service_del_postun nfs-mountd.service nfs-server.service nfsdcld.service

%post   -n libnfsidmap1 -p /sbin/ldconfig
%postun -n libnfsidmap1 -p /sbin/ldconfig

%verifyscript -n nfs-kernel-server
%verify_permissions -e /var/lib/nfs/rmtab

%files -n nfs-client
%license COPYING
%config %{_sysconfdir}/idmapd.conf
%config %{_sysconfdir}/nfsmount.conf
%config %{_sysconfdir}/nfs.conf
%verify(not mode) %attr(0755,root,root) %{_sbindir}/mount.nfs
%{_sbindir}/mount.nfs4
%{_sbindir}/umount.nfs
%{_sbindir}/umount.nfs4
%attr(0755,root,root) %{_sbindir}/mountstats
%attr(0755,root,root) %{_sbindir}/nfsiostat
%{_sbindir}/nfsdcld
%{_sbindir}/nfsidmap
%{_sbindir}/nfsstat
%{_sbindir}/rcnfs-client
%{_sbindir}/rpc.gssd
%{_sbindir}/rpc.idmapd
%{_sbindir}/rpc.statd
%{_sbindir}/rpcctl
%{_sbindir}/rpcdebug
%{_sbindir}/showmount
%{_sbindir}/sm-notify
%{_sbindir}/start-statd
%{_sbindir}/blkmapd
%{_sbindir}/rpc.svcgssd
%{_sbindir}/nfsconf
%{_udevrulesdir}/99-nfs.rules
%{_unitdir}/auth-rpcgss-module.service
%{_unitdir}/nfs-blkmap.service
%{_unitdir}/nfs-client.target
%{_unitdir}/nfs-idmapd.service
%{_unitdir}/nfs-utils.service
%{_unitdir}/nfsdcld.service
%{_unitdir}/rpc-gssd.service
%{_unitdir}/rpc-gssd.service.d
%{_unitdir}/rpc_pipefs.target
%{_unitdir}/rpc-statd-notify.service
%{_unitdir}/rpc-statd-notify.service.d
%{_unitdir}/rpc-statd.service
%{_unitdir}/rpc-statd.service.d
%{_unitdir}/rpc-svcgssd.service
%{_unitdir}/rpc-svcgssd.service.d
%{_unitdir}/var-lib-nfs-rpc_pipefs.mount
%dir %{_systemdgeneratordir}
%{_systemdgeneratordir}/nfs-server-generator
%{_systemdgeneratordir}/rpc-pipefs-generator
%{_modprobedir}/50-nfs.conf
%{_mandir}/man5/idmapd.conf.5%{ext_man}
%{_mandir}/man5/nfs.5%{ext_man}
%{_mandir}/man5/nfs.conf.5%{ext_man}
%{_mandir}/man5/nfsmount.conf.5%{ext_man}
%{_mandir}/man5/nfsrahead.5%{ext_man}
%{_mandir}/man7/nfs.systemd.7%{ext_man}
%{_mandir}/man8/blkmapd.8%{ext_man}
%{_mandir}/man8/gssd.8%{ext_man}
%{_mandir}/man8/idmapd.8%{ext_man}
%{_mandir}/man8/mount.nfs.8%{ext_man}
%{_mandir}/man8/mountstats.8%{ext_man}
%{_mandir}/man8/nfsconf.8%{ext_man}
%{_mandir}/man8/nfsdcld.8%{ext_man}
%{_mandir}/man8/nfsdclddb.8%{ext_man}
%{_mandir}/man8/nfsdclnts.8%{ext_man}
%{_mandir}/man8/nfsidmap.8%{ext_man}
%{_mandir}/man8/nfsiostat.8%{ext_man}
%{_mandir}/man8/nfsstat.8%{ext_man}
%{_mandir}/man8/rpc.gssd.8%{ext_man}
%{_mandir}/man8/rpc.idmapd.8%{ext_man}
%{_mandir}/man8/rpc.sm-notify.8%{ext_man}
%{_mandir}/man8/rpc.statd.8%{ext_man}
%{_mandir}/man8/rpc.svcgssd.8%{ext_man}
%{_mandir}/man8/rpcctl.8%{ext_man}
%{_mandir}/man8/rpcdebug.8%{ext_man}
%{_mandir}/man8/showmount.8%{ext_man}
%{_mandir}/man8/sm-notify.8%{ext_man}
%{_mandir}/man8/statd.8%{ext_man}
%{_mandir}/man8/svcgssd.8%{ext_man}
%{_mandir}/man8/umount.nfs.8%{ext_man}
%{_fillupdir}/sysconfig.nfs
%{_sysusersdir}/statd-user.conf
%dir %{_localstatedir}/lib/nfs
%dir %{_localstatedir}/lib/nfs/rpc_pipefs
%dir %{_localstatedir}/lib/nfs/v4recovery
%attr(0700,statd,statd) %dir %{_localstatedir}/lib/nfs/sm
%attr(0700,statd,statd) %dir %{_localstatedir}/lib/nfs/sm.bak
%ghost %{_localstatedir}/lib/nfs/state
%{_libexecdir}/nfsrahead

%files -n nfs-kernel-server
%{_unitdir}/nfs-mountd.service
%{_unitdir}/nfs-mountd.service.d
%{_unitdir}/nfs-server.service
%{_unitdir}/nfs-server.service.d
%{_unitdir}/proc-fs-nfsd.mount
%{_prefix}/lib/tmpfiles.d/nfs-kernel-server.conf
%{_sbindir}/exportfs
%{_sbindir}/rcnfs-server
%{_sbindir}/rpc.mountd
%{_sbindir}/rpc.nfsd
%{_sbindir}/nfsdcltrack
%attr(0755,root,root) %{_sbindir}/nfsdclddb
%attr(0755,root,root) %{_sbindir}/nfsdclnts
%{_mandir}/man5/exports.5%{ext_man}
%{_mandir}/man7/nfsd.7%{ext_man}
%{_mandir}/man8/exportfs.8%{ext_man}
%{_mandir}/man8/mountd.8%{ext_man}
%{_mandir}/man8/nfsd.8%{ext_man}
%{_mandir}/man8/rpc.mountd.8%{ext_man}
%{_mandir}/man8/rpc.nfsd.8%{ext_man}
%{_mandir}/man8/nfsdcltrack.8%{ext_man}
%config(noreplace) %{_localstatedir}/lib/nfs/etab
%config(noreplace) %{_localstatedir}/lib/nfs/rmtab

%files -n libnfsidmap1
%{_libdir}/libnfsidmap-1.0.0/
%{_libdir}/libnfsidmap.so.1*

%files -n nfsidmap-devel
%{_libdir}/libnfsidmap.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/libnfsidmap.pc
%{_mandir}/man3/*
%doc support/nfsidmap/README

%changelog
