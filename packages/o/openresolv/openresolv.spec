#
# spec file for package openresolv
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           openresolv
Version:        3.9.2
Release:        0
Summary:        DNS management framework
License:        BSD-2-Clause
URL:            https://roy.marples.name/projects/openresolv
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
sed -i -e 's/^#!\/bin\/sh$//' named.in pdnsd.in dnsmasq.in unbound.in libc.in pdns_recursor.in

%build
./configure --bindir=%{_sbindir} --libexecdir=%{_libexecdir}/resolvconf
make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/resolvconf.conf
%dir %{_libexecdir}/resolvconf
%{_libexecdir}/resolvconf/*
%{_sbindir}/resolvconf
%{_mandir}/man5/resolvconf.conf.5%{?ext_man}
%{_mandir}/man8/resolvconf.8%{?ext_man}

%changelog
