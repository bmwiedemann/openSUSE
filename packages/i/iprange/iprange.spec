#
# spec file for package iprange
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


Name:           iprange
Version:        2.0.0
Release:        0
Summary:        IP address range management tool for FireHOL
License:        GPL-2.0-or-later
URL:            https://firehol.org/
Source:         https://github.com/firehol/iprange/releases/download/v%{version}/iprange-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake

%description
This tool manages IP address ranges for FireHOL.

%prep
%autosetup
# Test expects permanent failure but no network connection means we
# only get temporary name resolution errors. Reported upstream:
# https://github.com/firehol/iprange/issues/42
rm -r tests.d/64-dns-failure-exit-status

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc ChangeLog README.md wiki
%{_mandir}/man1/iprange.1%{?ext_man}
%{_bindir}/iprange

%changelog
