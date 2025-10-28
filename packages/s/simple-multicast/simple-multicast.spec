#
# spec file for package simple-multicast
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           simple-multicast
Version:        0.2.5.2
Release:        0
Summary:        Multicast Server and Client application
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            https://github.com/anubisg1/simple-multicast
Source:         https://github.com/anubisg1/simple-multicast/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake

%description
Simple multicast Server/Client application.
Supports:

 * IPv4 AND IPv6
 * Multicast Server
 * Multicast client
 * Source Specific Multicast client

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
%make_build CFLAGS="%{optflags} -std=gnu99"

%install
%make_install
rm -rf %{buildroot}/%{_datadir}/doc/multicast

%files
%license COPYING
%doc README AUTHORS ChangeLog
%{_bindir}/multicast

%changelog
