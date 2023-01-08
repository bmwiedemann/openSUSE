#
# spec file for package pmacct
#
# Copyright (c) 2023 SUSE LLC
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

%bcond_with ndpi

Name:           pmacct
Version:        1.7.8
Release:        0
Summary:        Accounting and aggregation toolsuite for IPv4 and IPv6
License:        GPL-2.0-only
Group:          Productivity/Networking/Diagnostic
URL:            http://www.pmacct.net/
Source:         http://www.pmacct.net/pmacct-%{version}.tar.gz
Source4:        pmacct.nfacctd.service
Source5:        pmacct.pmacctd.service
Source6:        pmacct.sfacctd.service
Source7:        pmacct.nfacctd.sysconfig
Source8:        pmacct.pmacctd.sysconfig
Source9:        pmacct.sfacctd.sysconfig
Source10:       nfacctd.conf
Source11:       pmacctd.conf
Source12:       sfacctd.conf
Source20:       pmacct.1
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libmysqlclient-devel
BuildRequires:  libpcap-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  sqlite-devel >= 3.0.0
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libmaxminddb)
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  pkgconfig(numa)
%if %{with ndpi}
BuildRequires:  pkgconfig(libndpi)
%endif
%if 0%{?is_opensuse} == 1
BuildRequires:  libnetfilter_log-devel
%endif

%description
pmacct is a set of passive network monitoring tools to measure, account,
classify and aggregate IPv4 and IPv6 traffic; a pluggable
architecture allows to store the collected traffic data into memory tables or
SQL (MySQL, SQLite, PostgreSQL) databases. pmacct supports customizable
historical data breakdown, flow sampling, filtering and tagging, recovery
actions, and triggers. Libpcap, sFlow v2/v4/v5 and NetFlow v1/v5/v7/v8/v9 are
supported, both unicast and multicast. A client program can export
export data to tools like RRDtool, GNUPlot, Net-SNMP, MRTG, and Cacti.

%prep
%setup -q -n %{name}-%{version}

# fix permissions
chmod -x sql/pmacct-*

%build
autoreconf -fiv
export CFLAGS="%{optflags} -Wno-return-type -fcommon"
%configure \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --docdir="%{_docdir}/%{name}" \
    --enable-mmap \
    --enable-l2 \
    --enable-mysql \
    --enable-pgsql \
    --enable-sqlite3 \
    %if %{with ndpi}
    --enable-ndpi \
    %endif
    --enable-geoipv2 \
    %if 0%{?suse_version} >= 1310 && 0%{?is_opensuse} == 1
    --enable-jansson \
    %endif
    --enable-64bit \
    %if 0%{?is_opensuse} == 1
    --enable-nflog \
    %endif
    --enable-threads

make %{?_smp_mflags}

%install
%make_install

install -d %{buildroot}%{_fillupdir}
install -m 0644 %{SOURCE7} %{buildroot}%{_fillupdir}/sysconfig.nfacctd
install -m 0644 %{SOURCE8} %{buildroot}%{_fillupdir}/sysconfig.pmacctd
install -m 0644 %{SOURCE9} %{buildroot}%{_fillupdir}/sysconfig.sfacctd

install -d %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/nfacctd.service
install -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/pmacctd.service
install -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/sfacctd.service

# examples
install -d %{buildroot}%{_sysconfdir}/pmacct/
install -m 0600 %{SOURCE10} %{buildroot}/%{_sysconfdir}/pmacct/nfacctd.conf
install -m 0600 %{SOURCE11} %{buildroot}/%{_sysconfdir}/pmacct/pmacctd.conf
install -m 0600 %{SOURCE12} %{buildroot}/%{_sysconfdir}/pmacct/sfacctd.conf

# manpage
install -d %{buildroot}%{_mandir}/man1
install -m 0644 %{SOURCE20} %{buildroot}%{_mandir}/man1

# remove unneeded files
rm -rf %{buildroot}/%{_datadir}/pmacct/examples/lg
rm -rf %{buildroot}/%{_libdir}/pmacct/examples/lg
rm -rf %{buildroot}/%{_libdir}/pmacct/examples/custom/libcustom.la
rm -rf %{buildroot}/%{_datadir}/pmacct/{CONFIG-KEYS,FAQS,QUICKSTART,UPGRADE,docs}

%pre
%service_add_pre nfacctd.service pmacctd.service sfacctd.service

%post
%service_add_post nfacctd.service pmacctd.service sfacctd.service
%{fillup_only -n nfacctd}
%{fillup_only -n pmacctd}
%{fillup_only -n sfacctd}

%preun
%service_del_preun nfacctd.service pmacctd.service sfacctd.service

%postun
%service_del_postun nfacctd.service pmacctd.service sfacctd.service

%files
%license COPYING
%doc AUTHORS ChangeLog CONFIG-KEYS FAQS QUICKSTART UPGRADE
%{_mandir}/man1/pmacct.1%{?ext_man}
%{_bindir}/pmacct
%{_sbindir}/nfacctd
%{_sbindir}/pmacctd
%{_sbindir}/sfacctd
%{_sbindir}/uacctd
%{_sbindir}/pmtelemetryd
%{_sbindir}/pmbgpd
%{_sbindir}/pmbmpd
%{_datadir}/pmacct
%{_unitdir}/*.service
%dir %{_sysconfdir}/pmacct
%config(noreplace) %{_sysconfdir}/pmacct/nfacctd.conf
%config(noreplace) %{_sysconfdir}/pmacct/pmacctd.conf
%config(noreplace) %{_sysconfdir}/pmacct/sfacctd.conf
%{_fillupdir}/sysconfig.*

%changelog
