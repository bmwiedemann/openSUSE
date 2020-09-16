#
# spec file for package grepcidr
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           grepcidr
Version:        2.0
Release:        0
Summary:        Filter IP addresses matching IPv4/IPv6 CIDR specification
License:        GPL-3.0-or-later
Group:          Productivity/Text/Utilities
URL:            http://www.pc-tools.net/unix/grepcidr/
Source:         http://www.pc-tools.net/files/unix/%{name}-%{version}.tar.gz
Patch0:         grepcidr-obey-cflags.patch

%description
grepcidr can be used as a stream filter when you need to compare a list of IP
addresses against one or more Classless Inter-Domain Routing (CIDR) mask
specifications. Think of grepcidr as a CIDR-aware grep; instead of using
'grep 1.2.3.4' you can use 'grepcidr -e 1.2.3.4/30', for example. Multiple
specifications, of arbitrary mask lengths, can be specified both on the
command line or loaded from a file.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS='%{optflags}'
%make_build

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install %{?_smp_mflags}

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/grepcidr
%{_mandir}/man1/grepcidr.1%{?ext_man}

%changelog
