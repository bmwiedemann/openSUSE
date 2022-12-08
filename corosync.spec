#
# spec file for package corosync
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

# Conditionals
# Invoke "rpmbuild --without <feature>" or "rpmbuild --with <feature>"
# to disable or enable specific features
%bcond_without testagents
%bcond_with watchdog
%bcond_with monitoring
%bcond_with snmp
%bcond_with rdma
%bcond_with dbus
%bcond_with upstart
%bcond_with xmlconf
%bcond_without runautogen
%bcond_without systemd
%bcond_without qdevices
%bcond_without qnetd

%if 0%{?sles_version} == 12
%ifnarch s390 s390x
%define buildib 1
%endif
%endif

Name:           corosync
Summary:        The Corosync Cluster Engine and Application Programming Interfaces
License:        BSD-3-Clause
Group:          Productivity/Clustering/HA
Version:        2.4.6
Release:        0
URL:            http://corosync.github.io/corosync/
Source0:        %{name}-%{version}.tar.gz
Source2:        baselibs.conf
Patch1:         upstream-afd97d7884940_coroapi-Use-size_t-for-private_data_size.patch
Patch2:         Fix-compile-warnings-with-GCC-7.2.1.patch
Patch3:         bug-1083561_upgrade-from-1-x-y.patch
Patch4:         bug-882449_corosync-conf-example.patch
Patch5:         bug-1032634_fix-ifdown-udp.patch
Patch6:         bug-1001164_corosync.conf-example.patch
Patch7:         corosync-2.3.4-fix-bashisms.patch
Patch8:         corosync-init-lockfile-path-error.patch
Patch9:         corosync-start-stop-level.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# openais is indeed gone and should be uninstalled. Yes, we do not
# provide openais on purpose, the package has been deleted.
Obsoletes:      openais < 1.2
Conflicts:      openais < 1.2

# Runtime bits
Requires:       libcfg6 = %{version}-%{release}
Requires:       libcmap4 = %{version}-%{release}
Requires:       libcorosync_common4 = %{version}-%{release}
Requires:       libcpg4 = %{version}-%{release}
Requires:       libquorum5 = %{version}-%{release}
Requires:       libsam4 = %{version}-%{release}
Requires:       libtotem_pg5 = %{version}-%{release}
Requires:       libvotequorum8 = %{version}-%{release}
Conflicts:      openais <= 0.89
Conflicts:      openais-devel <= 0.89

# Build bits

BuildRequires:  groff-full
BuildRequires:  libqb-devel
BuildRequires:  mozilla-nss-devel
BuildRequires:  zlib-devel
%if %{with runautogen}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif
%if %{with monitoring}
BuildRequires:  libstatgrab-devel
%endif
%if %{with rdma}
BuildRequires:  libibverbs-devel
BuildRequires:  librdmacm-devel
%endif
%if %{with snmp}
BuildRequires:  net-snmp-devel
%endif
%if %{with dbus}
BuildRequires:  dbus-1-devel
%endif
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%{systemd_ordering}
%endif
%if %{with xmlconf}
Requires:       libxslt
%endif
%if %{with qdevices} || %{with qnetd}
Requires:       mozilla-nss-tools
%endif
%if %{with qnetd}
BuildRequires:  sed
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
rm -f .git*
echo %{version} > .tarball-version
echo %{version} > .version

%build
%if %{with runautogen}
./autogen.sh
%endif

%if %{with rdma}
export ibverbs_CFLAGS=-I/usr/include/infiniband \
export ibverbs_LIBS=-libverbs \
export rdmacm_CFLAGS=-I/usr/include/rdma \
export rdmacm_LIBS=-lrdmacm \
%endif
%{configure} \
%if %{with testagents}
    --enable-testagents \
%endif
%if %{with watchdog}
    --enable-watchdog \
%endif
%if %{with monitoring}
    --enable-monitoring \
%endif
%if %{with snmp}
    --enable-snmp \
%endif
%if %{with dbus}
    --enable-dbus \
%endif
%if %{with rdma}
    --enable-rdma \
%endif
%if %{with systemd}
    --enable-systemd \
%endif
%if %{with upstart}
    --enable-upstart \
%endif
%if %{with xmlconf}
    --enable-xmlconf \
%endif
%if %{with qdevices}
    --enable-qdevices \
%endif
%if %{with qnetd}
    --enable-qnetd \
%endif
    --with-initddir=%{_initrddir} \
    --with-systemddir=%{_unitdir} \
    --with-upstartdir=%{_sysconfdir}/init \
    --with-tmpfilesdir=%{_tmpfilesdir}

make %{_smp_mflags}

%install
%make_install

%if %{with dbus}
mkdir -p -m 0700 %{buildroot}/%{_sysconfdir}/dbus-1/system.d
install -m 644 %{_builddir}/%{name}-%{version}/conf/corosync-signals.conf %{buildroot}/%{_sysconfdir}/dbus-1/system.d/corosync-signals.conf
%endif
%if %{with systemd}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rccorosync
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rccorosync-qnetd
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rccorosync-qdevice
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rccorosync-notifyd
%endif

## tree fixup
# drop static libs
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la
# drop docs and html docs for now
rm -rf %{buildroot}%{_docdir}/*
#remove init scripts for corosync, corosync-qdevice, corosync-qnetd
rm -rf init/corosync init/corosync-qnetd init/corosync-qdevice
mkdir -p  %{buildroot}/usr/share/doc/packages/corosync/
mkdir -p  %{buildroot}%{_fillupdir}/
mkdir -p  %{buildroot}%{_sysconfdir}/init.d/
install -m 0644 conf/corosync.conf.example* %{buildroot}/usr/share/doc/packages/corosync/
mkdir -p %{buildroot}/usr/lib/corosync
install -m 0755 init/upgrade.sh %{buildroot}/usr/lib/corosync
rm -rf %{buildroot}/etc/corosync/corosync.conf.example*
rm -rf %{buildroot}/etc/logrotate.d/
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -m 644 init/corosync.sysconfig.example \
   %{buildroot}%{_fillupdir}/sysconfig.corosync
install -m 0644 tools/corosync-notifyd.sysconfig.example \
   %{buildroot}%{_fillupdir}/sysconfig.corosync-notifyd
rm -rf %{buildroot}%{localstatedir}/run/
%if %{with qdevices}
install -m 644 init/corosync-qdevice.sysconfig.example \
   %{buildroot}%{_fillupdir}/sysconfig.corosync-qdevice
install -m 770 -d %{buildroot}/run/corosync-qdevice
%endif

%if %{with qnetd}
install -m 644 init/corosync-qnetd.sysconfig.example \
   %{buildroot}%{_fillupdir}/sysconfig.corosync-qnetd
install -m 770 -d %{buildroot}/run/corosync-qnetd
%if %{with systemd}
sed -i -e 's/^#User=/User=/' \
   %{buildroot}%{_unitdir}/corosync-qnetd.service
%else
sed -i -e 's/^COROSYNC_QNETD_RUNAS=""$/COROSYNC_QNETD_RUNAS="coroqnetd"/' \
   %{buildroot}%{_sysconfdir}/sysconfig/corosync-qnetd
%endif
%endif

%description
This package contains the Corosync Cluster Engine Executive, several default
APIs and libraries, default configuration files, and an init script.

%pre
%service_add_pre corosync.service corosync-notifyd.service

%post
/usr/lib/corosync/upgrade.sh
%{fillup_only -n corosync}
%{fillup_only -n corosync-notifyd}
# Upgrade
if [ $1 -eq 2 ]; then
    # restore configured /etc/sysconfig/corosync(bsc#1155792)
    cp %{_sysconfdir}/sysconfig/corosync %{_fillupdir}/tmp.corosync_sysconfig
fi

%service_add_post corosync.service corosync-notifyd.service

rm -rf  %{_sysconfdir}/corosync/corosync.conf.example %{_sysconfdir}/corosync/corosync.conf.example.unicast
ln -s /usr/share/doc/packages/corosync/corosync.conf.example %{_sysconfdir}/corosync/
ln -s /usr/share/doc/packages/corosync/corosync.conf.example.udpu %{_sysconfdir}/corosync/corosync.conf.example.unicast

%preun
%service_del_preun corosync.service corosync-notifyd.service

%postun
if [ -f %{_sysconfdir}/sysconfig/corosync ]; then
    rm %{_sysconfdir}/sysconfig/corosync
fi

%posttrans
if [ ! -f %{_sysconfdir}/sysconfig/corosync ]; then
    mv %{_fillupdir}/tmp.corosync_sysconfig %{_sysconfdir}/sysconfig/corosync
fi

%files
%defattr(-,root,root,-)
%doc SECURITY
%license LICENSE
%{_sbindir}/corosync
%{_sbindir}/corosync-keygen
%{_sbindir}/corosync-cmapctl
%{_sbindir}/corosync-cfgtool
%{_sbindir}/corosync-cpgtool
%{_sbindir}/corosync-quorumtool
%{_sbindir}/corosync-notifyd
%if %{with systemd}
%{_sbindir}/rccorosync
%{_sbindir}/rccorosync-notifyd
%endif
%{_bindir}/corosync-blackbox
%if %{with xmlconf}
%{_bindir}/corosync-xmlproc
%config(noreplace) %{_sysconfdir}/corosync/corosync.xml.example
%dir %{_datadir}/corosync
%{_datadir}/corosync/xml2conf.xsl
%{_mandir}/man8/corosync-xmlproc.8*
%{_mandir}/man5/corosync.xml.5*
%endif
%dir %{_sysconfdir}/corosync
%dir %{_sysconfdir}/corosync/uidgid.d
%dir %{_datadir}/doc/corosync/
%dir /usr/lib/corosync/
/usr/lib/corosync/upgrade.sh
%config(noreplace) /usr/share/doc/packages/corosync/corosync.conf.example
%config(noreplace) /usr/share/doc/packages/corosync/corosync.conf.example.udpu
%config(noreplace) %{_fillupdir}/sysconfig.corosync-notifyd
%config(noreplace) %{_fillupdir}/sysconfig.corosync

%if %{with dbus}
%{_sysconfdir}/dbus-1/system.d/corosync-signals.conf
%endif
%if %{with snmp}
%{_datadir}/snmp/mibs/COROSYNC-MIB.txt
%endif
%if %{with systemd}
%{_unitdir}/corosync.service
%{_unitdir}/corosync-notifyd.service
%dir %{_datadir}/corosync
%{_datadir}/corosync/corosync
%{_datadir}/corosync/corosync-notifyd
%endif
%if %{with upstart}
%{_sysconfdir}/init/corosync.conf
%{_sysconfdir}/init/corosync-notifyd.conf
%endif
%dir %{_localstatedir}/lib/corosync
%dir %{_localstatedir}/log/cluster
%{_mandir}/man8/corosync_overview.8*
%{_mandir}/man8/corosync.8*
%{_mandir}/man8/corosync-blackbox.8*
%{_mandir}/man8/corosync-cmapctl.8*
%{_mandir}/man8/corosync-keygen.8*
%{_mandir}/man8/corosync-cfgtool.8*
%{_mandir}/man8/corosync-cpgtool.8*
%{_mandir}/man8/corosync-notifyd.8*
%{_mandir}/man8/corosync-quorumtool.8*
%{_mandir}/man5/corosync.conf.5*
%{_mandir}/man5/votequorum.5*
%{_mandir}/man8/cmap_keys.8*
%{_datadir}/doc/corosync/*
# optional testagent rpm
#
%if %{with testagents}

%package -n corosync-testagents
Summary:        The Corosync Cluster Engine Test Agents
Group:          Development/Tools/Other
Requires:       %{name} = %{version}

%description -n corosync-testagents
This package contains corosync test agents.

%files -n corosync-testagents
%defattr(755,root,root,-)
%dir %{_datadir}/corosync/tests

%{_datadir}/corosync/tests/mem_leak_test.sh
%{_datadir}/corosync/tests/net_breaker.sh
%{_datadir}/corosync/tests/cmap-dispatch-deadlock.sh
%{_datadir}/corosync/tests/shm_leak_audit.sh
%{_bindir}/cpg_test_agent
%{_bindir}/sam_test_agent
%{_bindir}/votequorum_test_agent

%endif

%package -n libcfg6
Summary:        Corosync configuration database library
Group:          System/Libraries

%description -n libcfg6
This package contains the Corosync configuration database library.

%package -n libcmap4
Summary:        Corosync configuration map library
Group:          System/Libraries

%description -n libcmap4
The CMAP library is used to interact with the configuration database
used by Corosync. The library provides a mechanism to
create/chage/remove keys, iterate over them and track changes to
keys.

%package -n libcorosync_common4
Summary:        The Corosync Cluster Engine library
# openais is indeed gone and should be uninstalled. Yes, we do not
# provide libopenais on purpose, the package has been deleted.
Group:          System/Libraries
Obsoletes:      libopenais3 < 1.2
Conflicts:      libopenais3 < 1.2
Obsoletes:      libcorosync4 < %{version}-%{release}
Provides:       libcorosync4 = %{version}-%{release}

%description -n libcorosync_common4
This package contains the central Corosync library.

%package -n libcpg4
Summary:        Corosync group message API
Group:          System/Libraries

%description -n libcpg4
A group message API called CPG, part of Corosync. This library is
used to create distributed applications that operate properly during
cluster partitions, merges, and faults.

%package -n libquorum5
Summary:        Corosync quorum library
Group:          System/Libraries

%description -n libquorum5
The quorum library is the external interface to the quorum service.
This service is loaded into all nodes in a Corosync cluster and track
the quorum status of a node.

%package -n libsam4
Summary:        Corosync Simple Availability Manager API
Group:          System/Libraries

%description -n libsam4
The SAM library provide a tool to check the health of an application.
The main purpose of SAM is to restart a local process when it fails
to respond to a healthcheck request in a configured time interval.

%package -n libtotem_pg5
Summary:        Corosync Totem protocol
Group:          System/Libraries

%description -n libtotem_pg5
An implementation of the Totem Single Ring Ordering and Membership
protocol providing the Extended Virtual Synchrony model for messaging
and membership.

%package -n libvotequorum8
Summary:        Corosync vote quorum library
Group:          System/Libraries

%description -n libvotequorum8
The votequorum library is the external interface to the vote-based
quorum service. This service is optionally loaded into all nodes in a
Corosync cluster to avoid split-brain situations. It does this by
having a number of votes assigned to each system in the cluster and
ensuring that only when a majority of the votes are present, cluster
operations are allowed to proceed.

%files -n libcfg6
%defattr(-,root,root)
%{_libdir}/libcfg.so.*

%files -n libcmap4
%defattr(-,root,root)
%{_libdir}/libcmap.so.*

%files -n libcpg4
%defattr(-,root,root)
%{_libdir}/libcpg.so.*

%files -n libcorosync_common4
%defattr(-,root,root)
%{_libdir}/libcorosync_common.so.*

%files -n libquorum5
%defattr(-,root,root)
%{_libdir}/libquorum.so.*

%files -n libsam4
%defattr(-,root,root)
%{_libdir}/libsam.so.*

%files -n libtotem_pg5
%defattr(-,root,root)
%{_libdir}/libtotem_pg.so.*

%files -n libvotequorum8
%defattr(-,root,root)
%{_libdir}/libvotequorum.so.*

%post   -n libcfg6 -p /sbin/ldconfig
%postun -n libcfg6 -p /sbin/ldconfig
%post   -n libcmap4 -p /sbin/ldconfig
%postun -n libcmap4 -p /sbin/ldconfig
%post   -n libcorosync_common4 -p /sbin/ldconfig
%postun -n libcorosync_common4 -p /sbin/ldconfig
%post   -n libcpg4 -p /sbin/ldconfig
%postun -n libcpg4 -p /sbin/ldconfig
%post   -n libquorum5 -p /sbin/ldconfig
%postun -n libquorum5 -p /sbin/ldconfig
%post   -n libsam4 -p /sbin/ldconfig
%postun -n libsam4 -p /sbin/ldconfig
%post   -n libtotem_pg5 -p /sbin/ldconfig
%postun -n libtotem_pg5 -p /sbin/ldconfig
%post   -n libvotequorum8 -p /sbin/ldconfig
%postun -n libvotequorum8 -p /sbin/ldconfig

%package -n libcorosync-devel
Summary:        The Corosync Cluster Engine Development Kit
Group:          Development/Libraries/C and C++
Requires:       libcfg6 = %{version}-%{release}
Requires:       libcmap4 = %{version}-%{release}
Requires:       libcorosync_common4 = %{version}-%{release}
Requires:       libcpg4 = %{version}-%{release}
Requires:       libqb-devel
Requires:       libquorum5 = %{version}-%{release}
Requires:       libsam4 = %{version}-%{release}
Requires:       libtotem_pg5 = %{version}-%{release}
Requires:       libvotequorum8 = %{version}-%{release}
Requires:       pkgconfig
Provides:       corosync-devel = %{version}
Obsoletes:      corosync-devel < 0.92-7

%description -n libcorosync-devel
This package contains include files and man pages used to develop using
The Corosync Cluster Engine APIs.

%files -n libcorosync-devel
%defattr(-,root,root,-)
%doc LICENSE
%dir %{_includedir}/corosync/
%{_includedir}/corosync/corodefs.h
%{_includedir}/corosync/cfg.h
%{_includedir}/corosync/cmap.h
%{_includedir}/corosync/corotypes.h
%{_includedir}/corosync/cpg.h
%{_includedir}/corosync/hdb.h
%{_includedir}/corosync/sam.h
%{_includedir}/corosync/quorum.h
%{_includedir}/corosync/votequorum.h
%dir %{_includedir}/corosync/totem/
%{_includedir}/corosync/totem/totem.h
%{_includedir}/corosync/totem/totemip.h
%{_includedir}/corosync/totem/totempg.h
%{_libdir}/libcfg.so
%{_libdir}/libcpg.so
%{_libdir}/libcmap.so
%{_libdir}/libtotem_pg.so
%{_libdir}/libquorum.so
%{_libdir}/libvotequorum.so
%{_libdir}/libsam.so
%{_libdir}/libcorosync_common.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/cpg_*3*
%{_mandir}/man3/quorum_*3*
%{_mandir}/man3/votequorum_*3*
%{_mandir}/man3/sam_*3*
%{_mandir}/man8/cpg_overview.8*
%{_mandir}/man8/votequorum_overview.8*
%{_mandir}/man8/sam_overview.8*
%{_mandir}/man3/cmap_*3*
%{_mandir}/man8/cmap_overview.8*
%{_mandir}/man8/quorum_overview.8*
%post -n libcorosync-devel -p /sbin/ldconfig
%postun -n libcorosync-devel -p /sbin/ldconfig

%if %{with qdevices}

%package -n corosync-qdevice
Summary:        The Corosync Cluster Engine Qdevice
Group:          System/Base
Requires:       corosync
Requires:       mozilla-nss-tools

%if %{with systemd}
%{systemd_ordering}
%endif

%description -n corosync-qdevice
This package contains the Corosync Cluster Engine Qdevice, script for creating
NSS certificates and an init script.

%pre -n corosync-qdevice
%service_add_pre corosync-qdevice.service

%post -n corosync-qdevice
%{fillup_only -n corosync-qdevice}
# Upgrade
if [ $1 -eq 2 ]; then
    cp %{_sysconfdir}/sysconfig/corosync-qdevice %{_fillupdir}/tmp.corosync-qdevice_sysconfig
fi

%if %{sles_version} > 0
ln -s /run/corosync-qdevice /var/run/
%endif
%service_add_post corosync-qdevice.service

%preun -n corosync-qdevice
%service_del_preun corosync-qdevice.service

%if %{sles_version}
unlink /var/run/corosync-qdevice
%endif

%service_del_postun corosync-qdevice.service

%postun -n corosync-qdevice
if [ -f %{_sysconfdir}/sysconfig/corosync-qdevice ]; then
    rm %{_sysconfdir}/sysconfig/corosync-qdevice
fi

%posttrans -n corosync-qdevice
if [ ! -f %{_sysconfdir}/sysconfig/corosync-qdevice ]; then
    mv %{_fillupdir}/tmp.corosync-qdevice_sysconfig %{_sysconfdir}/sysconfig/corosync-qdevice
fi

%files -n corosync-qdevice
%defattr(-,root,root,-)
%dir %{_sysconfdir}/corosync/qdevice
%dir %config(noreplace) %{_sysconfdir}/corosync/qdevice/net
#change corosync-qdevice to /run as /var/run is symlink nowdays
%ghost /run/corosync-qdevice
%{_sbindir}/corosync-qdevice
%{_sbindir}/corosync-qdevice-net-certutil
%{_sbindir}/corosync-qdevice-tool
%config(noreplace) %{_fillupdir}/sysconfig.corosync-qdevice
%if %{with systemd}
%{_unitdir}/corosync-qdevice.service
%{_sbindir}/rccorosync-qdevice
%dir %{_datadir}/corosync
%{_datadir}/corosync/corosync-qdevice
%endif
%{_mandir}/man8/corosync-qdevice-tool.8*
%{_mandir}/man8/corosync-qdevice-net-certutil.8*
%{_mandir}/man8/corosync-qdevice.8*
%endif

%if %{with qnetd}

%package -n corosync-qnetd
Summary:        The Corosync Cluster Engine Qdevice Network Daemon
Group:          System/Base
Requires:       mozilla-nss-tools
Requires(pre):  /usr/sbin/useradd

%if %{with systemd}
%{systemd_ordering}
%endif

%description -n corosync-qnetd
This package contains the Corosync Cluster Engine Qdevice Network Daemon, script for creating
NSS certificates and an init script.

%pre -n corosync-qnetd
getent group coroqnetd >/dev/null || groupadd -r coroqnetd -g 701
getent passwd coroqnetd >/dev/null || useradd -r -g coroqnetd -u 701 -s /sbin/nologin -c "User for corosync-qnetd" coroqnetd

%service_add_pre corosync-qnetd.service

exit 0

%post -n corosync-qnetd
%if %{sles_version} > 0
ln -s /run/corosync-qnetd /var/run/
%endif
%{fillup_only -n corosync-qnetd}
# Upgrade
if [ $1 -eq 2 ]; then
    cp %{_sysconfdir}/sysconfig/corosync-qnetd %{_fillupdir}/tmp.corosync-qnetd_sysconfig
fi

%service_add_post corosync-qnetd.service

%preun -n corosync-qnetd
%service_del_preun corosync-qnetd.service

%if %{sles_version} > 0
unlink /var/run/corosync-qnetd
%endif

%service_del_postun corosync-qnetd.service

%postun -n corosync-qnetd
if [ -f %{_sysconfdir}/sysconfig/corosync-qnetd ]; then
    rm %{_sysconfdir}/sysconfig/corosync-qnetd
fi

%posttrans -n corosync-qnetd
if [ ! -f %{_sysconfdir}/sysconfig/corosync-qnetd ]; then
    mv %{_fillupdir}/tmp.corosync-qnetd_sysconfig %{_sysconfdir}/sysconfig/corosync-qnetd
fi

%files -n corosync-qnetd
%defattr(-,root,root,-)
%dir %config(noreplace) %attr(750, coroqnetd, coroqnetd) %{_sysconfdir}/corosync/qnetd
#change corosync-qnetd to /run as /var/run is just symlink nowadays
%ghost %attr (750, coroqnetd, coroqnetd) /run/corosync-qnetd
%{_bindir}/corosync-qnetd
%{_bindir}/corosync-qnetd-certutil
%{_bindir}/corosync-qnetd-tool
%config(noreplace) %{_fillupdir}/sysconfig.corosync-qnetd
%if %{with systemd}
%{_unitdir}/corosync-qnetd.service
%{_sbindir}/rccorosync-qnetd
%dir %{_datadir}/corosync
%{_datadir}/corosync/corosync-qnetd
%endif
%{_mandir}/man8/corosync-qnetd-tool.8*
%{_mandir}/man8/corosync-qnetd-certutil.8*
%{_mandir}/man8/corosync-qnetd.8*
%endif

%changelog
