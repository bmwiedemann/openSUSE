#
# spec file for package nemesis
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


Name:           nemesis
Version:        1.7
Release:        0
Summary:        TCP/IP Packet Injection Suite
License:        BSD-4-Clause
Group:          Productivity/Networking/Diagnostic
URL:            http://troglobit.com/projects/nemesis/
#Git-Clone:     https://github.com/troglobit/nemesis
Source:         https://github.com/troglobit/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libnet-devel

%description
A commandline-based IP stack for Linux. The suite is broken down by
protocol and allows for scripting of injected packet streams from
shell scripts.

Key features:
 * support for ARP, DNS, ICMP, IGMP, OSPF, RIP, TCP, UDP protocols
 * layer 2 or layer 3 injection
 * packet payload from file

%prep
%setup -q

%build
export CFLAGS="%optflags -fcommon"
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}/%{_datadir}/doc

%files
%doc docs/CREDITS ChangeLog.md README.md
%license LICENSE
%{_bindir}/nemesis
%{_mandir}/man1/nemesis*.1%{?ext_man}

%changelog
