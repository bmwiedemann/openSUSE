#
# spec file for package hping
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           hping
Version:        3.0.0_alpha_1
Release:        0
Summary:        Command-line oriented TCP/IP packet assembler/analyzer
License:        GPL-2.0
Group:          Productivity/Networking/Diagnostic
Url:            https://github.com/antirez/hping
# Downloaded from https://github.com/antirez/hping
# Packed as tar.bz2
Source:         %{name}-%{version}+git-3547c76.tar.bz2
Source1:        %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM - hping-3.0.0_alpha_1-Makefile.in.patch -- fix build https://github.com/antirez/hping/issues/10
Patch0:         %{name}-3.0.0_alpha_1-Makefile.in.patch
# PATCH-FIX-UPSTREAM - hping-3.0.0_alpha_1-ars.c.patch -- fix build https://github.com/antirez/hping/issues/10
Patch1:         %{name}-3.0.0_alpha_1-ars.c.patch
BuildRequires:  libpcap-devel
BuildRequires:  tcl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
hping3 is a network tool able to send custom TCP/IP packets and to display
target replies like ping do with ICMP replies. hping3 can handle
fragmentation, and almost arbitrary packet size and content, using the
command line interface.

Since version 3, hping implements scripting capabilties, read the API.txt
file under the /docs directory to know more about it.

As a command line utility, hping is useful to test at many kind of
networking devices like firewalls, routers, and so. It can be used as
a traceroute alike program over all the supported protocols, firewalk usage,
OS fingerprinting, port-scanner (see the --scan option introduced with hping3),
TCP/IP stack auditing.

%package -n %{name}-doc
Summary:        Documentation for the hping
Group:          Documentation
BuildArch:      noarch

%description -n %{name}-doc
hping3 is a network tool able to send custom TCP/IP packets and to display
target replies like ping do with ICMP replies. hping3 can handle
fragmentation, and almost arbitrary packet size and content, using the
command line interface.

Since version 3, hping implements scripting capabilties, read the API.txt
file under the /docs directory to know more about it.

As a command line utility, hping is useful to test at many kind of
networking devices like firewalls, routers, and so. It can be used as
a traceroute alike program over all the supported protocols, firewalk usage,
OS fingerprinting, port-scanner (see the --scan option introduced with hping3),
TCP/IP stack auditing.

Documentation for the package hping.

%prep
%setup -q -n %{name}
%patch0
%patch1

# SED-FIX-UPSTREAM -- add 64bit https://github.com/antirez/hping/issues/9
sed -i 's|/usr/lib|/usr/lib/ /usr/lib64/|' configure

# SED-FIX-UPSTREAM -- fix includes https://github.com/antirez/hping/issues/9
sed -i 's|net/bpf.h|pcap-bpf.h|' script.c libpcap_stuff.c

# SED-FIX-UPSTREAM -- fix build https://github.com/antirez/hping/issues/10
sed -i 's|icmp, p, sizeof(subtcp|icmp, p, sizeof(icmp|' scan.c

%build

%configure
make %{?_smp_mflags} CCOPT="%{optflags}"

%install
%make_install strip

%files
%defattr(-,root,root,-)
%{_sbindir}/hping*
%{_mandir}/man8/%{name}*.8%{ext_man}
%{_mandir}/fr/man8/%{name}2-fr.8%{ext_man}

%files -n %{name}-doc
%defattr(-,root,root,-)
%{_defaultdocdir}/%{name}

%changelog
