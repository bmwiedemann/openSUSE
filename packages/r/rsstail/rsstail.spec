#
# spec file for package rsstail
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           rsstail
Version:        2.1
Release:        0
Summary:        RSS Feed Reader
License:        GPL-2.0
Group:          Productivity/Networking/Web/Utilities
Url:            http://www.vanheusden.com/rsstail/
Source:         https://github.com/folkertvanheusden/rsstail/archive/refs/tags/v%{version}.tar.gz#/rsstail-%{version}.tgz
# PATCH-FIX-UPSTREAM makefile-tweaks.patch -- adds --std=gnu11
Patch1:         https://github.com/folkertvanheusden/rsstail/commit/a09dac78a2936a83fbc35aab81405783fe6fba36.patch#/makefile-tweaks.patch
# PATCH-FIX-UPSTREAM remove-iconv-dependency.patch -- iconv is not used in the package, and not available. Remove it from the Makefile
Patch2:         https://github.com/folkertvanheusden/rsstail/commit/844a6fe5e54ecddf6abc22e5c284860cca107939.patch#/remove-iconv-dependency.patch
# PATCH-FIX-UPSTREAM fix-exit-codes.patch -- fix exit codes for help and version parameters
Patch3:         https://github.com/folkertvanheusden/rsstail/pull/5.patch#/fix-exit-codes.patch
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
%license license.txt
%{_bindir}/rsstail
%{_mandir}/man1/rsstail.1*

%changelog
