#
# spec file for package pingtunnel
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild

%define oname   PingTunnel

Name:           pingtunnel
Version:        0.72
Release:        0
Summary:        Reliably tunnel TCP connections over ICMP packets
License:        BSD-3-Clause
Group:          Productivity/Networking/Security
Url:            http://www.cs.uit.no/~daniels/PingTunnel/
Source0:        http://www.cs.uit.no/~daniels/%{oname}/%{oname}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  libpcap-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       ptunnel = %{version}-%{release}

%description
Ping Tunnel is a tool for reliably tunneling TCP connections over ICMP echo
request and reply packets (commonly known as ping requests and replies). It
is useful for evading firewalls that, for whatever reason, prevent outgoing
TCP connections, but allow in- and outgoing ICMP packets. The tunnel works
by having a proxy run on a machine ping-able from the inside of the
firewall, with the client running on the local machine from which TCP access
is required.

The following example illustrates the main motivation in creating ptunnel:

Setting: You're on the go, and stumble across an open wireless network.
The network gives you an IP address, but won't let you send TCP or UDP
packets out to the rest of the internet, for instance to check your mail.
What to do? By chance, you discover that the network will allow you to ping
any computer on the rest of the internet. With ptunnel, you can utilize
this feature to check your mail, or do other things that require TCP.


%prep
%setup -q -n %{oname}

# Remove not needed files
rm -f web/._index.html web/._setup.png

# SED-FIX-OPENSUSE -- Fix paths
sed -i -e 's|= /usr|= $(DESTDIR)/usr|' Makefile

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -fno-strict-aliasing"

%install
%make_install

%files
%defattr(-,root,root,-)
%attr(0644,-,-) %doc CHANGELOG LICENSE README web/*
%attr(0644,-,-) %{_mandir}/man8/ptunnel.8%{ext_man}
%{_bindir}/ptunnel

%changelog
