#
# spec file for package packit
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


Name:           packit
Version:        1.8.1
Release:        0
Summary:        Network injection and capture
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/eribertomota/packit
Source0:        https://github.com/eribertomota/packit/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE packit-1.7-fix_automake_1.16.5_build.patch
#Patch0:         packit-1.7-fix_automake_1.16.5_build.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libnet-devel
BuildRequires:  libpcap-devel

%description
Packit (Packet toolkit) is a network auditing tool. It
can customize, inject, monitor, and manipulate IP traffic.
By being able to construct nearly all TCP, UDP, ICMP, IP, ARP,
RARP, and Ethernet header options, Packit can be useful in testing
firewalls, intrusion detection/prevention systems, port scanning,
simulating network traffic, and general TCP/IP auditing.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%doc ChangeLog README.md docs/ICMP.txt
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8%{?ext_man}

%changelog
