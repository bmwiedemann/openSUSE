#
# spec file for package prtconf (Version 1.3)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           prtconf
Version:        1.3
Release:        1
Group:          System/Console
Summary:        SPARC OpenPROM dump utility
License:        GPL-2.0+
Url:            http://ultra.linux.cz/

#Source:	http://www.cs.elte.hu/pub/Linux/sunsite.mff.cuni.cz/prtconf/prtconf-1.3.tgz
Source:         prtconf-1.3.tar.xz

ExclusiveArch:  %sparc
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This utility will dump SPARC OpenPROM device tree in the format
similar to Solaris prtconf, that is, in a nicely readable compact
format.

%prep
%setup -q

%build
sed -i '/^CFLAGS/d' Makefile
make %{?_smp_mflags} CFLAGS="%optflags"

%install
b="%buildroot"
rm -Rf "$b"
mkdir "$b"
mkdir -p "$b/%_sbindir" "$b/%_mandir/man8"
install -pm0755 eeprom prtconf "$b/%_sbindir/"
install -pm0644 {eeprom,prtconf}.8 "$b/%_mandir/man8/"

%files
%defattr(-,root,root)
%doc COPYING
%_sbindir/*
%doc %_mandir/*/*

%changelog
