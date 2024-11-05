#
# spec file for package scapy
#
# Copyright (c) 2024 SUSE LLC
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


Name:           scapy
Version:        2.6.1
Release:        0
Summary:        Interactive Packet Manipulation Tool
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
URL:            https://scapy.net
Source:         https://github.com/secdev/scapy/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base >= 3.7
BuildRequires:  python3-setuptools
Requires:       python3-cryptography
Recommends:     python3-PyX
Recommends:     python3-ipython
Provides:       python-scapy = %version
Obsoletes:      python-scapy < 2.2.0
BuildArch:      noarch

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

# In (open)SUSE /etc/protocols and /etc/services
# moved to /usr/etc/
sed 's|%{_sysconfdir}/protocols|%{_prefix}%{_sysconfdir}/protocols|g' -i scapy/data.py
sed 's|%{_sysconfdir}/services|%{_prefix}%{_sysconfdir}/services|g' -i scapy/data.py

%build
%python3_build
#NOTE(saschpe): The documentation is CC-BY-SA-NC-2.5, thus we can not
# redistribute it (sr#172834):
rm -r doc/scapy

%install
%python3_install
# Fix non-executable-script rpmlint issue:
# WARN: Using simple globbing (*.py) will break manufdb loading
find %{buildroot}%{python3_sitelib} -name "pdu.py" -exec sed -i "/#!/d" {} \;
find %{buildroot}%{python3_sitelib} -name "doip.py" -exec sed -i "/#!/d" {} \;
%fdupes %{buildroot}%{python3_sitelib}

%check
cd test && ./run_tests -c configs/linux.utsc -K ci_only -K scanner -K netaccess

%files
%license LICENSE
%doc README.md
%{_bindir}/scapy
%{_mandir}/man1/scapy.1%{?ext_man}
%{python3_sitelib}/scapy*

%changelog
