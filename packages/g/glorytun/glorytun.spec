#
# spec file for package glorytun
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

Name:           glorytun
Version:        0.3.4
Release:        0
Summary:        A small, simple and secure VPN
License:        BSD-2-Clause
Group:          Productivity/Networking/Security
URL:            https://github.com/angt/glorytun
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsodium) >= 1.0.4
Requires:       iproute2

%description
Glorytun is a small, simple and secure VPN over MUD.
MUD (Multipath UDP Deflector) is a secure, multipath network protocol
over UDP.

The key features of Glorytun come directly from MUD:
 * Fast and highly secure
 * Multipath and failover
 * Traffic shaping
 * Path MTU discovery without ICMP

%prep
%setup -q

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/glorytun

%changelog
