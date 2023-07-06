#
# spec file for package bittwist
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2016-2023, Martin Hauke <mardnh@gmx.de>
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


Name:           bittwist
Version:        3.7
Release:        0
Summary:        A libpcap-based Ethernet packet generator
License:        GPL-2.0-only
Group:          Productivity/Networking/Diagnostic
#Git-Clone:     https://github.com/ayeowch/bittwist.git
URL:            https://bittwist.sourceforge.io
Source:         http://downloads.sourceforge.net/%{name}/Linux/Bit-Twist%%20%{version}/%{name}-linux-%{version}.tar.gz
Patch0:         bittwist-makefile.diff
BuildRequires:  libpcap-devel

%description
Bit-Twist is a libpcap-based Ethernet packet generator complementing
tcpdump. It replays traffic captured in .pcap files onto a live
network. It comes with a trace file editor to allow you to change the
contents of a trace file.

A packet generator is useful in simulating networking traffic or
testing firewall, IDS, and IPS, and troubleshooting various network
problems.

%prep
%setup -q -n %{name}-linux-%{version}
%patch0 -p1

%build
export CFLAGS="%{optflags}"
%make_build

%install
%make_install prefix=/usr

%files
%license COPYING
%doc AUTHORS BUGS CHANGES README.md VERSION
%{_bindir}/bittwist
%{_bindir}/bittwiste
%{_mandir}/man1/bittwist.1%{?ext_man}
%{_mandir}/man1/bittwiste.1%{?ext_man}

%changelog
