#
# spec file for package nast
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           nast
Version:        0.2.0
Release:        1
License:        GPL-2.0
Summary:        Packet sniffer and a LAN analyzer based on Libnet and Libpcap
Url:            http://nast.berlios.de/
Group:          Productivity/Networking/Diagnostic
Source:         %{name}-%{version}.tar.bz2
Patch0:         nast-%{version}-config.patch
%if 0%{?suse_version} > 1010
Patch1:         nast-%{version}-include.patch
%endif
%if 0%{?suse_version} > 1130
BuildRequires:  libnet-devel
%else
BuildRequires:  libnet
%endif
BuildRequires:  libpcap-devel
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Nast is a packet sniffer and a LAN analyzer based on Libnet and Libpcap.

It can sniff in normal mode or in promiscuos mode the packets on a network interface and log it.  It dumps the headers of packets and
the payload in ascii or ascii-hex format.  You can apply a filter. The sniffed data can be saved in a separated file.

As analyzer tool, it has many features like:
* Build LAN hosts list
* Follow a TCP-DATA stream
* Find LAN internet gateways
* Discorver promiscous nodes
* Reset an established connection
* Perform a single half-open portscanner
* Perform a multi half-open portscanner
* Find link type (hub or switch)
* Catch daemon banner of LAN nodes
* Control arp answers to discover possible arp-spoofings
* Byte couting with an optional filter
* Write reports logging

It also provides a new ncurses interface

%prep
%setup -q
%patch0
%if 0%{?suse_version} > 1010
%patch1 -p1
%endif

%build
export CFLAGS="$RPM_OPT_FLAGS"
%configure
make

%install
%{__make} install DESTDIR=%{?buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NCURSES_README BUGS TODO CREDITS AUTHORS VERSION
%doc %{_mandir}/man8/*
%{_bindir}/nast*

%changelog
