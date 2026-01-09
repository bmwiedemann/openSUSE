#
# spec file for package corosync
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_with watchdog
%bcond_with monitoring
%bcond_with snmp
%bcond_with dbus
%bcond_without systemd
%bcond_with xmlconf
%bcond_with nozzle
%bcond_with vqsim
%bcond_without runautogen
%bcond_with userflags

%global gitver %{?numcomm:.%{numcomm}}%{?alphatag:.%{alphatag}}%{?dirty:.%{dirty}}
%global gittarver %{?numcomm:.%{numcomm}}%{?alphatag:-%{alphatag}}%{?dirty:-%{dirty}}

Name:           corosync
Summary:        The Corosync Cluster Engine and Application Programming Interfaces
License:        BSD-3-Clause
Group:          Productivity/Clustering/HA
Version:        3.1.10
Release:        0
URL:            http://corosync.github.io/corosync/
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.tmpfiles.d.conf
Patch0:         0001-harden-services-with-systemd-sandboxing.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# Runtime bits
# The automatic dependency overridden in favor of explicit version lock
Requires:       %{name}-libs = %{version}-%{release}

# Support crypto reload
Requires:       libknet1 >= 1.28
# NSS crypto plugin should be always installed
Requires:       libknet1-crypto-nss-plugin >= 1.28

# Build bits
BuildRequires:  gcc

BuildRequires:  groff-full
BuildRequires:  libknet-devel >= 1.28
BuildRequires:  libqb-devel
BuildRequires:  zlib-devel
%if %{with runautogen}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif
%if %{with monitoring}
BuildRequires:  libstatgrab-devel
%endif
%if %{with snmp}
BuildRequires:  net-snmp-devel
%endif
%if %{with dbus}
BuildRequires:  dbus-1-devel
%endif
%if %{with nozzle}
BuildRequires:  libnozzle-devel
%endif
%if %{with systemd}
%{?systemd_requires}
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(systemd)
%endif
%if %{with xmlconf}
Requires:       libxslt
%endif
%if %{with vqsim}
BuildRequires:  readline-devel
%endif
Obsoletes:      libcfg6
Obsoletes:      libcmap4
Obsoletes:      libcorosync_common4
Obsoletes:      libcpg4
Obsoletes:      libquorum5
Obsoletes:      libsam4
Obsoletes:      libtotem_pg5
Obsoletes:      libvotequorum8

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%prep
%autosetup -p1 -n %{name}-%{version}

rm -f .git*
echo %{version} > .tarball-version
echo %{version} > .version

%build
%if %{with runautogen}
./autogen.sh
%endif

%{configure} \
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
%if %{with systemd}
	--enable-systemd \
%endif
%if %{with xmlconf}
	--enable-xmlconf \
%endif
%if %{with nozzle}
	--enable-nozzle \
%endif
%if %{with vqsim}
  --enable-vqsim \
%endif
%if %{with userflags}
   --enable-user-flags \
%endif
	--with-initddir=%{_initrddir} \
	--with-systemddir=%{_unitdir}

make %{_smp_mflags}

%install
%make_install

%if %{with dbus}
mkdir -p -m 0700 %{buildroot}/%{_datadir}/dbus-1/system.d
install -m 644 %{_builddir}/%{name}-%{version}/conf/corosync-signals.conf %{buildroot}/%{_datadir}/dbus-1/system.d/corosync-signals.conf
%endif
%if %{with systemd}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rccorosync
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rccorosync-notifyd
%endif

## tree fixup
# drop static libs
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la
# drop docs and html docs for now
rm -rf %{buildroot}%{_docdir}/*

rm -rf %{buildroot}/etc/logrotate.d/
rm -rf %{buildroot}/etc/corosync/corosync.conf.example*
rm -rf %{buildroot}%{localstatedir}/run/

mkdir -p  %{buildroot}%{_fillupdir}/
# /etc/sysconfig/corosync-notifyd
install -m 644 tools/corosync-notifyd.sysconfig.example \
   %{buildroot}%{_fillupdir}/sysconfig.corosync-notifyd
# /etc/sysconfig/corosync
install -m 644 init/corosync.sysconfig.example \
   %{buildroot}%{_fillupdir}/sysconfig.corosync

mkdir -p  %{buildroot}/%{_datadir}/doc/packages/corosync/
install -m 0644 conf/corosync.conf.example* %{buildroot}/%{_datadir}/doc/packages/corosync/

%description
This package contains the Corosync Cluster Engine Executive, several default
APIs and libraries, default configuration files, and an init script.

%pre
%service_add_pre corosync.service corosync-notifyd.service

%post
%{fillup_and_insserv -n corosync}
%{fillup_and_insserv -n corosync-notifyd}
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post corosync.service corosync-notifyd.service

rm -rf  %{_sysconfdir}/corosync/corosync.conf.example %{_sysconfdir}/corosync/corosync.conf.example.unicast
ln -s %{_datadir}/doc/packages/corosync/corosync.conf.example %{_sysconfdir}/corosync/

%preun
%if %{with systemd}
%service_del_preun corosync.service corosync-notifyd.service
%endif

%postun
%if %{with systemd}
%service_del_postun corosync.service corosync-notifyd.service
%endif

if [ -f /etc/sysconfig/corosync ]; then
    rm /etc/sysconfig/corosync
fi

%files
%defattr(-,root,root,-)
%doc LICENSE
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
%dir %{_datadir}/corosync
%config(noreplace) %{_sysconfdir}/corosync/corosync.xml.example
%{_datadir}/corosync/xml2conf.xsl
%{_mandir}/man8/corosync-xmlproc.8*
%{_mandir}/man5/corosync.xml.5*
%endif
%dir %{_sysconfdir}/corosync
%dir %{_sysconfdir}/corosync/uidgid.d
%dir %{_datadir}/doc/corosync/
%{_datadir}/doc/packages/corosync/corosync.conf.example
%{_fillupdir}/sysconfig.corosync-notifyd
%{_fillupdir}/sysconfig.corosync

%if %{with dbus}
%{_datadir}/dbus-1/system.d/corosync-signals.conf
%endif
%if %{with snmp}
%{_datadir}/snmp/mibs/COROSYNC-MIB.txt
%endif
%if %{with systemd}
%{_unitdir}/corosync.service
%{_unitdir}/corosync-notifyd.service
%{_tmpfilesdir}/%{name}.conf
%else
%dir %{_datadir}/corosync
%{_datadir}/corosync/corosync
%{_datadir}/corosync/corosync-notifyd
%endif
%ghost %{_localstatedir}/lib/corosync
%ghost %{_localstatedir}/log/cluster
%{_mandir}/man7/corosync_overview.7*
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
%{_mandir}/man7/cmap_keys.7*
%{_datadir}/doc/corosync/*

# library
#
%package libs
Summary:        The corosync Cluster Engine Libraries

%description libs
This package contains corosync libraries.

%files libs
%doc LICENSE
%{_libdir}/libcfg.so.*
%{_libdir}/libcpg.so.*
%{_libdir}/libcmap.so.*
%{_libdir}/libquorum.so.*
%{_libdir}/libvotequorum.so.*
%{_libdir}/libsam.so.*
%{_libdir}/libcorosync_common.so.*

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%package devel
Summary:        The Corosync Cluster Engine Development Kit
Group:          Development/Libraries/C and C++
Requires:       %{name}-libs = %{version}-%{release}
Requires:       pkgconfig
Provides:       %{name}-devel = %{version}

%description devel
This package contains include files and man pages used to develop using
The Corosync Cluster Engine APIs.

%files devel
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
%{_libdir}/libcfg.so
%{_libdir}/libcpg.so
%{_libdir}/libcmap.so
%{_libdir}/libquorum.so
%{_libdir}/libvotequorum.so
%{_libdir}/libsam.so
%{_libdir}/libcorosync_common.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/cpg_*3*
%{_mandir}/man3/quorum_*3*
%{_mandir}/man3/votequorum_*3*
%{_mandir}/man3/sam_*3*
%{_mandir}/man3/cmap_*3*

%if %{with vqsim}
%package vqsim
Summary:        The Corosync Cluster Engine - Votequorum Simulator
Requires:       %{name}-libs = %{version}-%{release}
Requires:       pkgconfig

%description vqsim
A command-line simulator for the corosync votequorum subsystem.
It uses the same code as the corosync quorum system but forks
them into subprocesses to simulate nodes.
Nodes can be added and removed as well as partitioned (to simulate
network splits)

%files vqsim
%doc LICENSE
%{_bindir}/corosync-vqsim
%{_mandir}/man8/corosync-vqsim.8*
%endif

%changelog
