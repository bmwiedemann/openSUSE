#
# spec file for package ssldump
#
# Copyright (c) 2023 SUSE LLC
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


Name:           ssldump
Version:        1.6
Release:        0
Summary:        SSLv3/TLS Network Protocol Analyzer
License:        BSD-3-Clause
Group:          Productivity/Networking/Diagnostic
URL:            https://adulau.github.io/ssldump/
#Git-Clone:     https://github.com/adulau/ssldump.git
Source:         https://github.com/adulau/ssldump/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libnet-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(json-c)
%if 0%{?suse_version} > 1320 || (0%{?is_opensuse} && 0%{?leap_version} == 420300)
BuildRequires:  libpcap-devel-static
%else
BuildRequires:  libpcap-devel
%endif

%description
ssldump is an SSLv3/TLS network protocol analyzer. It identifies TCP
connections on the chosen network interface and attempts to interpret
them as SSLv3/TLS traffic. When it identifies SSLv3/TLS traffic, it
decodes the records and outputs them in a textual form to stdout. If
provided with the appropriate keying material, it also decrypts the
connections and displays the application data traffic.

%prep
%setup -q

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

%files
%license COPYRIGHT
%doc ChangeLog NEWS README.md
%{_sbindir}/ssldump
%{_mandir}/man1/ssldump.1%{?ext_man}

%changelog
