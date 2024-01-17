#
# spec file for package dsvpn
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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

Name:           dsvpn
Version:        0.1.4
Release:        0
Summary:        A Dead Simple VPN
License:        MIT
Group:          Productivity/Networking/Security
URL:            https://github.com/jedisct1/dsvpn
Source:         https://github.com/jedisct1/dsvpn/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       iproute2
Requires:       iptables

%description
DSVPN is a Dead Simple VPN, designed to address the most common
use case for using a VPN:

[client device] -- (untrusted network) -- [vpn server] -- [the Internet]

Features:
 * Runs on TCP. Works pretty much everywhere, including on public WiFi
   where only TCP/443 is open or reliable.
 * Uses only modern cryptography, with formally verified implementations.
 * Small and constant memory footprint. Doesn't perform any heap memory
   allocations.
 * Small (~25 KB), with an equally small and readable code base.
 * Works out of the box. No lousy documentation to read. No configuration
   file. No post-configuration. Run a single-line command on the server,
   a similar one on the client and you're done.
   No firewall and routing rules to manually mess with.
 * Doesn't leak between reconnects if the network doesn't change.
   Blocks IPv6 on the client to prevent IPv6 leaks.

%prep
%setup -q

%build
echo %{optflags} > .cflags
%make_build

%install
install -Dpm 0755 dsvpn %{buildroot}/%{_sbindir}/dsvpn

%files
%license LICENSE
%doc README.md
%{_sbindir}/dsvpn

%changelog
