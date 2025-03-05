#
# spec file for package rsstail
#
# Copyright (c) 2025 SUSE LLC
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


Name:           rsstail
Version:        2.2
Release:        0
Summary:        RSS Feed Reader
License:        GPL-2.0-only
Group:          Productivity/Networking/Web/Utilities
URL:            http://www.vanheusden.com/rsstail/
Source:         https://github.com/folkertvanheusden/rsstail/archive/refs/tags/v%{version}.tar.gz#/rsstail-%{version}.tgz
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libmrss-devel >= 0.16
BuildRequires:  make

%description
RSSTail is more or less an RSS reader: it monitors an RSS feed and if it
detects a new entry, it will emit only that new entry.

%prep
%autosetup

%build
make %{?_smp_mflags} DEBUG="-g %{optflags}" CC="gcc"

%install
install -D -m 0755 rsstail %{buildroot}%{_bindir}/rsstail
install -D -m 0644 -t %{buildroot}%{_mandir}/man1 rsstail.1

%check
./rsstail -V
./rsstail -h

%files
%doc README.md
%license LICENSE
%{_bindir}/rsstail
%{_mandir}/man1/rsstail.1*

%changelog
