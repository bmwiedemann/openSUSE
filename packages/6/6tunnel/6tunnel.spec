#
# spec file for package 6tunnel
#
# Copyright (c) 2024 SUSE LLC
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
Patch1:         https://github.com/wojtekka/6tunnel/commit/9e4119f03f57eec67b97dddbf09d363b638791dc.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  python3

%description
6tunnel allows using services provided by IPv6 hosts with IPv4-only
applications and vice versa. It can bind to any of the system's IPv4
or IPv6 addresses and forward all data to IPv4 or IPv6 hosts.

It can be used, for example, as an IPv6-capable IRC proxy.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/6tunnel
%{_mandir}/man1/6tunnel.1%{?ext_man}

%changelog
