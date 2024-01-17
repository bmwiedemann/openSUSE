#
# spec file for package ipv6toolkit
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


Name:           ipv6toolkit
Version:        2.0
Release:        0
Summary:        Security assessment and troubleshooting tool for the IPv6 protocols
License:        GPL-3.0-or-later
Group:          Productivity/Networking/System
URL:            https://www.si6networks.com/tools/ipv6toolkit/
#Git-Clone:     https://github.com/fgont/ipv6toolkit.git
Source:         https://www.si6networks.com/tools/ipv6toolkit/%{name}-v%{version}.tar.gz
Source98:       https://www.si6networks.com/tools/ipv6toolkit/%{name}-v%{version}.tar.gz.sig
#https://www.si6networks.com/tools/ipv6toolkit/%%{name}-v%%{version}.tar.gz.gpg
Source99:       %{name}.keyring
BuildRequires:  libpcap-devel

%description
SI6 Networks's IPv6 toolkit is a set of IPv6 security and
trouble-shooting tools that can send arbitrary IPv6-based
packets.

List of tools:
 * addr6: An IPv6 address analysis and manipulation tool.
 * flow6: A tool to perform a security asseessment of the IPv6 Flow
   Label.
 * frag6: A tool to perform IPv6 fragmentation-based attacks and to
   perform a security assessment of a number of fragmentation-related
   aspects.
 * icmp6: A tool to perform attacks based on ICMPv6 error messages.
 * jumbo6: A tool to assess potential flaws in the handling of IPv6
   Jumbograms.
 * na6: A tool to send arbitrary Neighbor Advertisement messages.
 * ni6: A tool to send arbitrary ICMPv6 Node Information messages,
    and assess possible flaws in the processing of such packets.
 * ns6: A tool to send arbitrary Neighbor Solicitation messages.
 * ra6: A tool to send arbitrary Router Advertisement messages.
 * rd6: A tool to send arbitrary ICMPv6 Redirect messages.
 * rs6: A tool to send arbitrary Router Solicitation messages.
 * scan6: An IPv6 address scanning tool.
 * tcp6: A tool to send arbitrary TCP segments and perform a variety
   of TCP-based attacks.

%prep
%setup -q -n %{name}-v%{version}

%build
export CFLAGS='%{optflags} -fcommon'
make %{?_smp_mflags}

%install
%make_install PREFIX="%{_prefix}"

%files
%doc CHANGES.TXT CREDITS.TXT README.TXT
%license LICENSE.TXT
%config %{_sysconfdir}/ipv6toolkit.conf
%{_bindir}/addr6
%{_sbindir}/blackhole6
%{_sbindir}/flow6
%{_sbindir}/frag6
%{_sbindir}/icmp6
%{_sbindir}/jumbo6
%{_sbindir}/na6
%{_sbindir}/ni6
%{_sbindir}/ns6
%{_sbindir}/path6
%{_sbindir}/ra6
%{_sbindir}/rd6
%{_sbindir}/rs6
%{_sbindir}/scan6
%{_sbindir}/script6
%{_sbindir}/tcp6
%{_sbindir}/udp6
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/oui.txt
%{_datadir}/%{name}/service-names-port-numbers.csv
%{_mandir}/man?/*?%{ext_man}

%changelog
