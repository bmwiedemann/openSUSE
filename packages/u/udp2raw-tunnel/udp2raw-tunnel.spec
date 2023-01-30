#
# spec file for package udp2raw-tunnel
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2019-2023, Martin Hauke <mardnh@gmx.de>
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


Name:           udp2raw-tunnel
Version:        20200818.0
Release:        0
Summary:        UDP over TCP/ICMP/UDP tunnel
# The following files are adapted from PolarSSL 1.3.19 (GPL-2.0)
#  lib/md5.cpp
#  lib/aes_acc/aesarm_table.h
#  lib/aes_acc/aesni.c
#  lib/aes_acc/aesacc.c
#  lib/aes_acc/aesni.h
# The following file is adapted from PolarSSL and is licenced under Apache-2.0 OR GPL-2.0
#  lib/pbkdf2-sha1.cpp
# Bundled libev is licenced under GPL-3.0+ or BSD-2-Clause
License:        MIT
Group:          Productivity/Networking/Other
URL:            https://github.com/wangyu-/udp2raw-tunnel
#Git-Clone:     https://github.com/wangyu-/udp2raw-tunnel.git
Source:         https://github.com/wangyu-/udp2raw-tunnel/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
Requires:       iptables

%description
A tunnel which turns UDP traffic into encrypted UDP/FakeTCP/ICMP traffic
by using raw sockets that can help bypass UDP firewalls (or
unstable UDP environments).

%prep
%setup -q
sed -i 's|-ggdb||' makefile
sed -i 's|-static||' makefile
sed -i 's|$(shell git rev-parse HEAD)|%{version}|g' makefile
chmod -x README.md
find doc -type f | xargs chmod -x
sed -i 's/\r$//' doc/README.zh-cn.md

%build
export OPT='%{optflags}'
make %{?_smp_mflags}

%install
install -D -m 0755 udp2raw %{buildroot}/%{_bindir}/udp2raw
install -D -m 0644 example.conf %{buildroot}/%{_sysconfdir}/udp2raw/example.conf

%files
%license LICENSE.md
%doc README.md doc/*
%dir %{_sysconfdir}/udp2raw
%config %{_sysconfdir}/udp2raw/example.conf
%{_bindir}/udp2raw

%changelog
