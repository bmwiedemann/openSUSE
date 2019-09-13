#
# spec file for package devmem2
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Guillaume GARDET <guillaume@opensuse.org>
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


Name:           devmem2
Version:        1.0
Release:        0
Summary:        Simple program to read/write from/to any location in memory
License:        GPL-2.0+
Group:          Hardware/Other
Url:            http://free-electrons.com/pub/mirror/devmem2.c
Source:         devmem2-1.0.tar.gz
Patch1:         fix_usage_on_64_bits.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Simple program to read/write from/to any location in memory.
Usage examples:
devmem2 0x48004B48 w 0x2 - write value 0x2 to addr 0x48004B48
devmem2 0x50000014 - read value from addr 0x50000014

%prep
%setup -q
%patch1

%build
cc %{optflags} devmem2.c -o devmem2

%install
install -D -m 0755 devmem2 %{buildroot}%{_sbindir}/devmem2

%files
%defattr(-,root,root)
%{_sbindir}/devmem2

%changelog
