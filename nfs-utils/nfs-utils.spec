#
# spec file for package nfs-utils
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           nfs-utils
Version:        2.1.1
Release:        0
Summary:        Support Utilities for Kernel nfsd
License:        GPL-2.0-or-later
Group:          Productivity/Networking/NFS
Url:            http://kernel.org/pub/linux/utils/nfs-utils/
Source0:        http://kernel.org/pub/linux/utils/nfs-utils/%{version}/nfs-utils-%{version}.tar.xz
# Download does not work:
# Source1:        ftp://nfs.sourceforge.net/pub/nfs/nfs.doc.tar.bz2
Source1:        nfs.doc.tar.bz2
Source4:        sysconfig.nfs
Source6:        README.NFSv4
Source7:        fw-client
Source8:        fw-server
Source11:       idmapd.conf
Source13:       nfs-utils.rpmlintrc
Source15:       nfsserver.service
Source16:       nfs.service
Source17:       nfs-server.nfsserver.conf
Source18:       nfs-client.nfs.conf
Source20:       nfs-mountd.options.conf
Source21:       nfs-server.options.conf
Source22:       rpc-gssd.options.conf
Source23:       rpc-statd.options.conf
Source24:       rpc-statd-notify.options.conf
Source25:       rpc-svcgssd.options.conf
Source26:       nfs.conf
Source27:       nfs-kernel-server.tmpfiles.conf
Patch0:         nfs-utils-1.0.7-bind-syntax.patch
Patch1:         0001-conffile-ignore-empty-environment-variables.patch
Patch2:         0002-mount-call-setgroups-before-setuid.patch
Patch3:         0003-nfs-server-generator-handle-noauto-mounts-correctly.patch
Patch4:         nsm-headers.patch
Patch5:         sysmacros.patch

BuildRequires:  e2fsprogs-devel
BuildRequires:  fedfs-utils-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(kdb)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libnfsidmap) >= 0.24
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(sqlite3)
Suggests:       python-base
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}

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
Requires(pre):  shadow
%if 0%{?suse_version} >= 1330
Requires(pre):  group(nogroup)
%endif
Obsoletes:      nfs-utils < 1.1.0

%description -n nfs-client
This package contains common NFS utilities which are needed for client
and kernel based server.

%package -n nfs-kernel-server
Summary:        Support Utilities for Kernel nfsd
Group:          Productivity/Networking/NFS
Requires:       netcfg
Requires:       nfs-client = %{version}
Requires:       rpcbind
Conflicts:      nfs-server
Provides:       nfs-utils = %{version}
Obsoletes:      nfs-utils < 1.1.0
PreReq:         permissions

%description -n nfs-kernel-server
This package contains support for the kernel based NFS server. You can
tune the number of server threads via the sysconfig variable
USE_KERNEL_NFSD_NUMBER. For quota over NFS support, install the quota
package.

%package -n nfs-doc
Summary:        Support Utilities for NFS
Group:          Productivity/Networking/NFS
Requires:       latex2html-pngicons
Obsoletes:      nfs-utils < 1.1.0
Supplements:    (nfs-utils and patterns-base-documentation)

%description -n nfs-doc
This package contains additional NFS documentation.

%prep
%setup -q -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

cp %{SOURCE6} .

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
	--enable-mountconfig
make %{?_smp_mflags}
cd nfs
for i in *.html ; do
sed -i \
 -e "s@%{_prefix}/lib/latex2html/icons.png/next_motif.png@%{_datadir}/latex2html/icons/next.png@" \
 -e "s@%{_prefix}/lib/latex2html/icons.png/up_motif_gr.png@%{_datadir}/latex2html/icons/up.png@" \
 -e "s@%{_prefix}/lib/latex2html/icons.png/previous_motif_gr.png@%{_datadir}/latex2html/icons/prev.png@" \
 $i
done

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
install -D -m 644 %{SOURCE15} %{buildroot}%{_unitdir}/nfsserver.service
install -D -m 644 %{SOURCE16} %{buildroot}%{_unitdir}/nfs.service
install -D -m 644 %{SOURCE17} %{buildroot}%{_unitdir}/nfs-server.service.d/nfsserver.conf
install -D -m 644 %{SOURCE18} %{buildroot}%{_unitdir}/nfs-client.target.d/nfs.conf
install -D -m 644 %{SOURCE20} %{buildroot}%{_unitdir}/nfs-mountd.service.d/options.conf
install -D -m 644 %{SOURCE21} %{buildroot}%{_unitdir}/nfs-server.service.d/options.conf
install -D -m 644 %{SOURCE22} %{buildroot}%{_unitdir}/rpc-gssd.service.d/options.conf
install -D -m 644 %{SOURCE23} %{buildroot}%{_unitdir}/rpc-statd.service.d/options.conf
install -D -m 644 %{SOURCE24} %{buildroot}%{_unitdir}/rpc-statd-notify.service.d/options.conf
install -D -m 644 %{SOURCE25} %{buildroot}%{_unitdir}/rpc-svcgssd.service.d/options.conf
install -D -m 644 %{SOURCE26} %{buildroot}%{_sysconfdir}/nfs.conf
install -D -m 644 %{SOURCE27} %{buildroot}%{_prefix}/lib/tmpfiles.d/nfs-kernel-server.conf
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcnfsserver
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcnfs-server
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcnfs
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
install -m 0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/nfs-client
install -m 0644 %{SOURCE8} %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/nfs-kernel-server
install -m 644 utils/mount/nfsmount.conf %{buildroot}%{_sysconfdir}/nfsmount.conf
#
# hack to avoid automatic python dependency
chmod 644 %{buildroot}%{_sbindir}/{mountstats,nfsiostat}

%pre -n nfs-client
/usr/bin/getent passwd statd >/dev/null || \
	/usr/sbin/useradd -r -c 'NFS statd daemon' \
	-s /sbin/nologin -d %{_localstatedir}/lib/nfs -g nogroup statd
%service_add_pre nfs.service auth-rpcgss-module.service nfs-idmapd.service nfs-blkmap.service rpc-statd-notify.service rpc-gssd.service rpc-statd.service rpc-svcgssd.service

%post -n nfs-client
chown statd:nogroup %{_localstatedir}/lib/nfs > /dev/null 2>&1 || :
for i in state sm sm.bak; do
	chown -R statd %{_localstatedir}/lib/nfs/$i > /dev/null 2>&1 || :
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
%set_permissions /sbin/mount.nfs
%service_add_post nfs.service auth-rpcgss-module.service nfs-idmapd.service nfs-blkmap.service rpc-statd-notify.service rpc-gssd.service rpc-statd.service rpc-svcgssd.service

%preun -n nfs-client
%service_del_preun nfs.service auth-rpcgss-module.service nfs-idmapd.service nfs-blkmap.service rpc-statd-notify.service rpc-gssd.service rpc-statd.service rpc-svcgssd.service

%postun -n nfs-client
%service_del_postun nfs.service auth-rpcgss-module.service nfs-idmapd.service nfs-blkmap.service rpc-statd-notify.service rpc-gssd.service rpc-statd.service rpc-svcgssd.service

%verifyscript -n nfs-client
%verify_permissions -e /sbin/mount.nfs

%pre -n nfs-kernel-server
%service_add_pre nfsserver.service nfs-svcgssd.service nfs-mountd.service nfs-server.service

%preun -n nfs-kernel-server
%service_del_preun nfsserver.service nfs-svcgssd.service nfs-mountd.service nfs-server.service

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
%service_add_post nfsserver.service nfs-mountd.service nfs-server.service
%tmpfiles_create nfs-kernel-server.conf
%set_permissions /var/lib/nfs/rmtab

%postun -n nfs-kernel-server
%service_del_postun nfsserver.service nfs-mountd.service nfs-server.service

%verifyscript -n nfs-kernel-server
%verify_permissions -e /var/lib/nfs/rmtab

%files -n nfs-client
%defattr(-,root,root)
%config %{_sysconfdir}/idmapd.conf
%config %{_sysconfdir}/nfsmount.conf
%config %{_sysconfdir}/nfs.conf
%verify(not mode) %attr(0755,root,root) /sbin/mount.nfs
/sbin/mount.nfs4
/sbin/umount.nfs
/sbin/umount.nfs4
/sbin/osd_login
%attr(0755,root,root) %{_sbindir}/mountstats
%attr(0755,root,root) %{_sbindir}/nfsiostat
%{_sbindir}/nfsidmap
%{_sbindir}/nfsstat
%{_sbindir}/rcnfs
%{_sbindir}/rcnfs-client
%{_sbindir}/rpc.gssd
%{_sbindir}/rpc.idmapd
%{_sbindir}/rpc.statd
%{_sbindir}/rpcdebug
%{_sbindir}/showmount
%{_sbindir}/sm-notify
%{_sbindir}/start-statd
%{_sbindir}/blkmapd
%{_sbindir}/rpc.svcgssd
%{_unitdir}/auth-rpcgss-module.service
%{_unitdir}/nfs-blkmap.service
%{_unitdir}/nfs-client.target
%{_unitdir}/nfs-idmapd.service
%{_unitdir}/nfs-utils.service
%{_unitdir}/rpc-gssd.service
%{_unitdir}/rpc-gssd.service.d
%{_unitdir}/rpc-gssd.service.d/options.conf
%{_unitdir}/rpc-statd-notify.service
%{_unitdir}/rpc-statd-notify.service.d
%{_unitdir}/rpc-statd-notify.service.d/options.conf
%{_unitdir}/rpc-statd.service
%{_unitdir}/rpc-statd.service.d
%{_unitdir}/rpc-statd.service.d/options.conf
%{_unitdir}/rpc-svcgssd.service
%{_unitdir}/rpc-svcgssd.service.d
%{_unitdir}/rpc-svcgssd.service.d/options.conf
%{_unitdir}/var-lib-nfs-rpc_pipefs.mount
%{_unitdir}/nfs.service
%dir %{_unitdir}/nfs-client.target.d
%{_unitdir}/nfs-client.target.d/nfs.conf
%dir /usr/lib/systemd/system-generators
/usr/lib/systemd/system-generators/nfs-server-generator
%{_mandir}/man5/nfsmount.conf.5%{ext_man}
%{_mandir}/man5/nfs.conf.5%{ext_man}
%{_mandir}/man5/nfs.5%{ext_man}
%{_mandir}/man7/nfs.systemd.7%{ext_man}
%{_mandir}/man8/mount.nfs.8%{ext_man}
%{_mandir}/man8/nfsidmap.8%{ext_man}
%{_mandir}/man8/nfsstat.8%{ext_man}
%{_mandir}/man8/rpc.sm-notify.8%{ext_man}
%{_mandir}/man8/showmount.8%{ext_man}
%{_mandir}/man8/sm-notify.8%{ext_man}
%{_mandir}/man8/umount.nfs.8%{ext_man}
%{_mandir}/man8/rpc.gssd.8%{ext_man}
%{_mandir}/man8/rpc.idmapd.8%{ext_man}
%{_mandir}/man8/gssd.8%{ext_man}
%{_mandir}/man8/idmapd.8%{ext_man}
%{_mandir}/man8/svcgssd.8%{ext_man}
%{_mandir}/man8/rpc.statd.8%{ext_man}
%{_mandir}/man8/rpcdebug.8%{ext_man}
%{_mandir}/man8/statd.8%{ext_man}
%{_mandir}/man8/mountstats.8%{ext_man}
%{_mandir}/man8/nfsiostat.8%{ext_man}
%{_mandir}/man8/blkmapd.8%{ext_man}
%{_mandir}/man8/rpc.svcgssd.8%{ext_man}
%{_fillupdir}/sysconfig.nfs
%attr(0711,statd,nogroup) %dir %{_localstatedir}/lib/nfs
%dir %{_localstatedir}/lib/nfs/rpc_pipefs
%dir %{_localstatedir}/lib/nfs/v4recovery
%attr(0700,statd,nogroup) %dir %{_localstatedir}/lib/nfs/sm
%attr(0700,statd,nogroup) %dir %{_localstatedir}/lib/nfs/sm.bak
%attr(0700,statd,nogroup) %ghost %{_localstatedir}/lib/nfs/state
%config %attr(0644,root,root) %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/nfs-client

%files -n nfs-kernel-server
%defattr(-,root,root)
%{_unitdir}/nfs-mountd.service
%{_unitdir}/nfs-mountd.service.d
%{_unitdir}/nfs-mountd.service.d/options.conf
%{_unitdir}/nfs-server.service
%{_unitdir}/nfs-server.service.d
%{_unitdir}/nfs-server.service.d/options.conf
%{_unitdir}/proc-fs-nfsd.mount
%{_unitdir}/nfsserver.service
%{_unitdir}/nfs-server.service.d/nfsserver.conf
%{_prefix}/lib/tmpfiles.d/nfs-kernel-server.conf
%{_sbindir}/exportfs
%{_sbindir}/rcnfsserver
%{_sbindir}/rcnfs-server
%{_sbindir}/rpc.mountd
%{_sbindir}/rpc.nfsd
/sbin/nfsdcltrack
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
%config %attr(0644,root,root) %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/nfs-kernel-server

%files -n nfs-doc
%defattr(-,root,root)
%doc nfs/*.html nfs/*.ps README.NFSv4

%changelog
