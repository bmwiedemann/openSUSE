# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           openresolv
Version:        3.9.0
Release:        0
Summary:        DNS management framework
License:        BSD-2-Clause
Group:          Productivity/Networking/DNS/Utilities
Url:            https://roy.marples.name/projects/openresolv
Source:         https://roy.marples.name/downloads/openresolv/%{name}-%{version}.tar.xz
Requires:       bash
BuildArch:      noarch

%description
/etc/resolv.conf is a file that holds the configuration for the local resolution of domain names.
Normally this file is either static or maintained by a local daemon, normally a DHCP daemon.
openresolv will make sure, that multiple processes (eg. dhcpcd, NetworkManager, openvpn)
can write the resolv.conf without overwriting each others changes.

openresolv can generate a combined resolv.conf or a configuration file for a local nameserver
(like unbound, dnsmasq or bind) that will route the dns requests according to the search domain.

%prep
%setup -q
sed -i -e 's/^#!\/bin\/sh$//' named.in pdnsd.in dnsmasq.in unbound.in libc.in

%build
./configure --bindir=/usr/sbin --libexecdir=/usr/lib/resolvconf
make

%install
%make_install

%files
%doc README
%config(noreplace) %{_sysconfdir}/resolvconf.conf
%dir /usr/lib/resolvconf
/usr/lib/resolvconf/*
/usr/sbin/resolvconf
/usr/share/man/man5/resolvconf.*
/usr/share/man/man8/resolvconf.*

%changelog

