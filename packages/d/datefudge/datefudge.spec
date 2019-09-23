#
# spec file for package datefudge
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           datefudge
Version:        1.22
Release:        0
Summary:        A preload library to fake system time
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
License:        GPL-2.0+
Group:          Development/Tools
Url:            http://packages.qa.debian.org/d/datefudge.html
Source:         http://cdn.debian.net/debian/pool/main/d/datefudge/%{name}_%{version}.tar.xz
Source2:        http://cdn.debian.net/debian/pool/main/d/datefudge/%{name}_%{version}.dsc#/%{name}.asc
Source3:        https://db.debian.org/fetchkey.cgi?fingerprint=35E876FAB4D3732E93B4D237631DE7553BE8AFD4#/%{name}.keyring

%description
This program fakes the system date so that programs think the
wall clock is different. The faking is not complete; timestamp
on files are not affected in any way.

%prep
# the signature is on the Debian .dsc. Extract the checksums and verify against source
echo "`grep -A1 "Files:" %{SOURCE2} | grep %{name}_%{version}.tar.xz | cut -d\  -f2`  %{SOURCE0}" | md5sum -c
echo "`grep -A1 "Checksums-Sha1" %{SOURCE2} | grep %{name}_%{version}.tar.xz | cut -d\  -f2`  %{SOURCE0}" | sha1sum -c
echo "`grep -A1 "Checksums-Sha256" %{SOURCE2} | grep %{name}_%{version}.tar.xz | cut -d\  -f2`  %{SOURCE0}" | sha256sum -c
%setup -q
sed "s/VERSION := \$\(.*\)/VERSION := %{version}/g" -i Makefile
sed 's/-o root -g root/-p/g' -i Makefile

%build
CFLAGS="%{optflags}" make libdir=%{_libdir} %{?_smp_mflags}

%install
make install libdir=%{_libdir} DESTDIR=%{buildroot} %{?_smp_mflags}

%files
%doc README COPYING
%{_mandir}/man1/datefudge.1%{ext_man}
%{_bindir}/datefudge
%{_libdir}/datefudge/datefudge.so
%dir %{_libdir}/datefudge

%changelog
