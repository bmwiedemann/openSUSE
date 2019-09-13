#
# spec file for package addrwatch
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


Name:           addrwatch
Version:        1.0.1
Release:        0
Summary:        A tool for IPv4/IPv6 and Ethernet address pairing monitoring
License:        GPL-3.0-only
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/fln/addrwatch
Source0:        https://github.com/fln/addrwatch/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-db-reconnect-issue.patch
BuildRequires:  autoconf >= 2.68
BuildRequires:  automake
BuildRequires:  libevent-devel
BuildRequires:  libmysqlclient-devel
BuildRequires:  libpcap-devel
BuildRequires:  sqlite3-devel

%description
This is a tool similar to arpwatch. It main purpose is to monitor
network and log discovered Ethernet to IPv4/IPv6 address
pairings. It supports monitoring multiple network interfaces,
monitoring of VLAN tagged (802.1Q) packets, and can output to
stdout, plain text file, syslog, sqlite3 and MySQL. Addrwatch
tracks IPv6 addresses of hosts using IPv6 privacy extensions
(RFC4941).

The main difference between arpwatch and addrwatch is the format
of output files.

While arpwatch stores only current state of the pairings and
allows to send email notification when a pairing change occurs,
addrwatch do not keep persistent network pairings' state, but
instead logs all the events that allow pairing discovery.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --enable-mysql --enable-sqlite3 --bindir=%{_sbindir}
make %{?_smp_mflags}

%install
%make_install
chmod -x scripts/dump2pcap.pl

%files
%license COPYING
%doc NEWS README.md scripts/dump2pcap.pl
%{_sbindir}/addrwatch
%{_sbindir}/addrwatch_mysql
%{_sbindir}/addrwatch_stdout
%{_sbindir}/addrwatch_syslog
%{_mandir}/man8/addrwatch.8%{?ext_man}

%changelog
