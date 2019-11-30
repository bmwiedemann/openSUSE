#
# spec file for package dnsmeter
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


Name:           dnsmeter
Version:        1.0.1
Release:        0
Summary:        DNS performance and infrastructure testing
License:        GPL-3.0-only
Group:          Productivity/Networking/DNS/Utilities
URL:            https://www.dns-oarc.net/tools/dnsmeter
#Git-Clone:     https://github.com/DNS-OARC/dnsmeter.git
Source:         https://www.dns-oarc.net/files/dnsmeter/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(zlib)

%description
DNSMeter is a tool for testing performance of nameserver and/or
infrastructure around it.
It generates dns queries and sends them via UDP to a target nameserver
and counts the answers.

Features:
 - payload can be given as text file or pcap file
 - can automatically run different load steps, which can be given as
   list or ranges
 - results per load step can be stored in CSV file
 - sender address can be spoofed from a given network or from pcap file,
   if payload is a pcap file
 - answers are counted, even if source address is spoofed, if answers get
   routed back to the load generator
 - roundtrip-times are measured (average, min, mix)
 - amount of DNSSEC queries can be given as percentage of total traffic
 - optimized for high amount of packets. On an Intel(R) Xeon(R) CPU E5-2430
   v2 @ 2.50GHz it can generate more than 900.000 packets per second

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}/%{_datadir}/doc

%files
%license LICENSE
%doc CHANGES README.md
%{_bindir}/dnsmeter
%{_mandir}/man1/dnsmeter.1%{?ext_man}

%changelog
