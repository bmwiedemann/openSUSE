#
# spec file for package arp-scan
#
# Copyright (c) 2022 SUSE LLC
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


Name:           arp-scan
Version:        1.9.8
Release:        0
Summary:        ARP scanning and fingerprinting tool
# strlcpy.c and strlcat.c have ISC header and embeded {getopt,obstack}.{c,h} has LGPL-2.1
License:        GPL-3.0-only AND LGPL-2.1-only AND ISC
Group:          Productivity/Networking/Security
URL:            https://github.com/royhills/arp-scan
Source:         https://github.com/royhills/arp-scan/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libpcap-devel >= 1.5.0
BuildRequires:  perl-macros
BuildRequires:  perl(LWP::Simple)
Requires:       perl(LWP::Simple)
%{perl_requires}

%description
arp-scan is a command-line tool that uses the ARP protocol to discover and fingerprint IP hosts on the local network.

%define debug_package_requires %{name} = %{version}-%{release}

%prep
%setup -q

%build
autoreconf -fiv
%configure
%make_build

%check
make %{?_smp_mflags} check

%install
%make_install
sed -i "s|env ||g" %{buildroot}%{_bindir}/*

%files
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/arp-fingerprint
%{_bindir}/arp-scan
%{_bindir}/get-iab
%{_bindir}/get-oui
%{_datadir}/arp-scan
%{_mandir}/man1/arp-fingerprint.1%{?ext_man}
%{_mandir}/man1/arp-scan.1%{?ext_man}
%{_mandir}/man1/get-iab.1%{?ext_man}
%{_mandir}/man1/get-oui.1%{?ext_man}
%{_mandir}/man5/mac-vendor.5%{?ext_man}

%changelog
