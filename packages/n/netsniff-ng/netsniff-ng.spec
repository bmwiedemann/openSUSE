#
# spec file for package netsniff-ng
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           netsniff-ng
Version:        0.6.9
Release:        0
Summary:        Network Sniffer for Packet Inspection
License:        GPL-2.0-only
Group:          Productivity/Networking/Diagnostic
URL:            http://netsniff-ng.org/
Source:         http://pub.netsniff-ng.org/netsniff-ng/netsniff-ng-%{version}.tar.xz
Patch0:         netsniff-ng-ncursesw.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libcli-devel
BuildRequires:  libnet-devel
BuildRequires:  libnetfilter_conntrack-devel
BuildRequires:  libnl3-devel
BuildRequires:  libpcap-devel
BuildRequires:  libsodium-devel
BuildRequires:  libtool
BuildRequires:  liburcu-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(ncursesw)

%description
netsniff-ng is a network sniffer for packet inspection. It is similar
to tcpdump, and likewise uses a memory mapped area for accessing
packets. It can be used for protocol analysis and reverse
engineering, network debugging, measurement of performance
throughput, or network statistics creation of incoming packets on
central network nodes like routers or firewalls.

The netsniff-ng toolkit consists of the following utilities:

* netsniff-ng, a zero-copy analyzer, pcap capturing and replaying tool
* trafgen, a multithreaded low-level zero-copy network packet generator
* mausezahn, high-level packet generator for HW/SW appliances with Cisco-CLI
* bpfc, a Berkeley Packet Filter compiler, Linux BPF JIT disassembler
* ifpps, a top-like kernel networking statistics tool
* flowtop, a top-like netfilter connection tracking tool
* curvetun, a curve25519-based IP tunnel
* astraceroute, an autonomous system (AS) trace route utility

%prep
%autosetup -p1

%build
export NACL_LIB=sodium
export NACL_INC_DIR=%{_includedir}/sodium
./configure --disable-geoip
%make_build ETCDIR=%{_sysconfdir} Q= STRIP=: CFLAGS="%{optflags}"

%install
# disable parrallel execution with -j1 because it cause an error with make 4.4
make -j1 install PREFIX=%{_prefix} ETCDIR=%{_sysconfdir} DESTDIR=%{buildroot}
rm -Rf %{buildroot}%{_docdir}/netsniff-ng %{buildroot}%{_datadir}/licenses/

%files
%license COPYING
%doc AUTHORS README REPORTING-BUGS
%dir %{_sysconfdir}/netsniff-ng
%config(noreplace) %{_sysconfdir}/netsniff-ng/*
%{_sbindir}/astraceroute
%{_sbindir}/bpfc
%{_sbindir}/curvetun
%{_sbindir}/flowtop
%{_sbindir}/ifpps
%{_sbindir}/mausezahn
%{_sbindir}/netsniff-ng
%{_sbindir}/trafgen
%{_mandir}/man8/astraceroute.8%{?ext_man}
%{_mandir}/man8/bpfc.8%{?ext_man}
%{_mandir}/man8/curvetun.8%{?ext_man}
%{_mandir}/man8/flowtop.8%{?ext_man}
%{_mandir}/man8/ifpps.8%{?ext_man}
%{_mandir}/man8/mausezahn.8%{?ext_man}
%{_mandir}/man8/netsniff-ng.8%{?ext_man}
%{_mandir}/man8/trafgen.8%{?ext_man}

%changelog
