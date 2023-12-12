#
# spec file for package scapy
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           scapy
Version:        2.5.0
Release:        0
Summary:        Interactive Packet Manipulation Tool
Source:         https://github.com/secdev/scapy/archive/v%{version}.tar.gz
URL:            https://scapy.net
Group:          Productivity/Networking/Security
License:        GPL-2.0
BuildRequires:  fdupes
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# Testing requirements: (require root permission and a fully functional network stack)
#BuildRequires:  tcpdump
BuildArch:      noarch
Provides:       python-scapy = %version
Obsoletes:      python-scapy < 2.2.0

%description
Scapy is a powerful interactive packet manipulation tool, packet generator,
network scanner, network discovery tool, and packet sniffer. It provides
classes to interactively create packets or sets of packets, manipulate them,
send them over the wire, sniff other packets from the wire, match answers and
replies, and more. Interaction is provided by the Python interpreter, so Python
programming structures can be used (such as variables, loops, and functions).
Report modules are possible and easy to make. It is intended to do about the
same things as ttlscan, nmap, hping, queso, p0f, xprobe, arping, arp-sk,
arpspoof, firewalk, irpas, tethereal, tcpdump, etc.

%prep
%setup -q -n scapy-%{version}
# Fix non-executable-script rpmlint issue:
find scapy -name "*.py" -exec sed -i "/#!/d" {} \;

%build
%python3_build
#NOTE(saschpe): The documentation is CC-BY-SA-NC-2.5, thus we can not 
# redistribute it (sr#172834):
rm -r doc/scapy

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}
rm -Rv %{buildroot}%{python3_sitelib}/test/

#%%check
#cd test && ./run_tests

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%{_bindir}/scapy
%{_mandir}/man1/scapy.1%{ext_man}
%{python3_sitelib}/scapy*

%changelog
