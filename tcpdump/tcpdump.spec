#
# spec file for package tcpdump
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


%define min_libpcap_version 1.8.1
Name:           tcpdump
Version:        4.9.2
Release:        0
Summary:        A Packet Sniffer
License:        BSD-3-Clause
Group:          Productivity/Networking/Diagnostic
Url:            http://www.tcpdump.org/
Source:         http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
Source1:        tcpdump-qeth
Source2:        http://www.tcpdump.org/release/%{name}-%{version}.tar.gz.sig
Source3:        http://www.tcpdump.org/tcpdump-workers.asc#/%{name}.keyring
# PATCH-FIX-OPENSUSE tcpdump-ikev2pI2.patch - disabled failing test
Patch0:         tcpdump-ikev2pI2.patch
# PATCH-FIX-OPENSUSE tcpdump-CVE-2018-19519.patch - Initialize buf in print-hncp.c:print_prefix
Patch1:         tcpdump-CVE-2018-19519.patch
# PATCH-FIX-UPSTREAM bsc#1068716 CVE-2017-16808 Heap-based buffer over-read related to aoe_print and lookup_emem
Patch2:         tcpdump-CVE-2017-16808.patch
# PATCH-FIX-UPSTREAM bsc#1142439 CVE-2019-1010220 Buffer Over-read in print_prefix
Patch3:         tcpdump-CVE-2019-1010220.patch
BuildRequires:  libpcap-devel >= %{min_libpcap_version}
BuildRequires:  libsmi-devel
BuildRequires:  openssl-devel
Requires:       libpcap >= %{min_libpcap_version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This program can "read" all or only certain packets going over the
ethernet. It can be used to debug specific network problems.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export CFLAGS="%{optflags} -Wall -DGUESS_TSO -fstack-protector -fno-strict-aliasing"
%configure \
  --enable-ipv6
make %{?_smp_mflags}

%install
%make_install
%ifarch s390 s390x
  install -D -m 755 %{SOURCE1} %{buildroot}%{_sbindir}
%endif
rm %{buildroot}/%{_sbindir}/tcpdump.%{version}

%check
make check %{?_smp_mflags}

%files
%defattr(-,root,root)
%license LICENSE
%doc CHANGES CREDITS README* *.awk
%{_mandir}/man?/*
%{_sbindir}/tcpdump
%ifarch s390 s390x
%{_sbindir}/tcpdump-qeth
%endif

%changelog
