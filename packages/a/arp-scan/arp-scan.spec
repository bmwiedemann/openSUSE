#
# spec file for package arp-scan
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_without caps
Name:           arp-scan
Version:        1.10.0
Release:        0
Summary:        ARP scanning and fingerprinting tool
# strlcpy.c and strlcat.c have ISC header and embeded {getopt,obstack}.{c,h} has LGPL-2.1
License:        GPL-3.0-only AND LGPL-2.1-only AND ISC
URL:            https://github.com/royhills/arp-scan
Source:         https://github.com/royhills/arp-scan/releases/download/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM arp-scan-EACCES-as-ENOENT.patch boo#1210703 gh#royhills/arp-scan#120 -- treat EACCES like ENOENT when stat'ing the mapping file in CWD, so it falls through to the system datadir instead of failing with "Permission denied"
Patch0:         arp-scan-EACCES-as-ENOENT.patch
BuildRequires:  perl-macros
BuildRequires:  pkgconfig
BuildRequires:  perl(LWP::Simple)
BuildRequires:  pkgconfig(libpcap) >= 1.5.0
Requires:       perl(LWP::Simple)
%{perl_requires}
%if 0%{with caps}
# pre-installed in build root, but make explicit anyway
BuildRequires:  pkgconfig(libcap)
%endif

%description
arp-scan is a command-line tool that uses the ARP protocol to discover and fingerprint IP hosts on the local network.

%define debug_package_requires %{name} = %{version}-%{release}

%prep
%autosetup -p1

%build
%configure \
%if %{with caps}
	--with-libcap=yes \
%else
# defaults to auto
	--with-libcap=no \
%endif
	%{nil}
%make_build

%check
%make_build check

%install

%make_install
sed -i "s|env ||g" %{buildroot}%{_bindir}/*

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/arp-scan
%dir %{_sysconfdir}/arp-scan
%config(noreplace) %{_sysconfdir}/arp-scan/mac-vendor.txt
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man5/*.5%{?ext_man}

%changelog
