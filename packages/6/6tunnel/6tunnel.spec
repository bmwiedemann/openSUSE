#
# spec file for package 6tunnel
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


Name:           6tunnel
Version:        0.13
Release:        0
Summary:        TCP proxy for non-IPv6 applications
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            https://github.com/wojtekka/6tunnel
#Git-Clone:     https://github.com/wojtekka/6tunnel.git
Source:         https://github.com/wojtekka/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  python2

%description
6tunnel allows using services provided by IPv6 hosts with IPv4-only
applications and vice versa. It can bind to any of the system's IPv4
or IPv6 addresses and forward all data to IPv4 or IPv6 hosts.

It can be used, for example, as an IPv6-capable IRC proxy.

%prep
%setup -q
sed -i 's|#!/usr/bin/env python|#!/usr/bin/python2|' test.py

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install

%check
make %{?_smp_mflags} check

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/6tunnel
%{_mandir}/man1/6tunnel.1%{?ext_man}

%changelog
