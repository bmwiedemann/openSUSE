#
# spec file for package ngrep
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define tarver 1_47
Name:           ngrep
Version:        1.47
Release:        0
Summary:        Network grep
License:        BSD-4-Clause
Group:          Productivity/Networking/Diagnostic
Url:            https://github.com/jpr5/ngrep
Source:         https://github.com/jpr5/ngrep/archive/V%{tarver}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libpcap-devel
BuildRequires:  pcre-devel

%description
ngrep strives to provide most of GNU grep's common features, applying them
to the network layer. ngrep is a pcap-aware tool that allows you to specify
extended regular or hexadecimal expressions to match against data payloads
of packets. It currently recognizes IPv4/6, TCP, UDP, ICMPv4/6, IGMP and
Raw across Ethernet, PPP, SLIP, FDDI, Token Ring and null interfaces, and
understands BPF filter logic in the same fashion as more common packet
sniffing tools, such as tcpdump and snoop.

%prep
%setup -q -n %{name}-%{tarver}

%build
%configure \
    --enable-pcre \
    --enable-ipv6 \
    --with-pcap-includes=%{_includedir}/pcap

make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8%{ext_man}

%changelog
