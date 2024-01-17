#
# spec file for package elftoaout (Version 2.3)
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



Name:           elftoaout
Version:        2.3
Release:        1
Group:          Development/Tools/Building
Summary:        Utility for converting ELF binaries to a.out
License:        GPL-2.0+
#URL:		http://sparc-boot.org/	#defunct
Source:         elftoaout-2.3.tgz
Patch1:         elftoaout-include.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The elftoaout utility converts a static ELF binary to a static a.out
binary.  If you are using an ELF system on a SPARC, you will need to
run elftoaout on the kernel image so that the SPARC PROM can boot the
image.

%prep
%setup -q
%patch -P 1 -p1

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -Rf "%buildroot"
mkdir "%buildroot";
mkdir -p "%buildroot/%_bindir" "%buildroot/%_mandir/man1"
install -pm0755 elftoaout "%buildroot/%_bindir/"
install -pm0644 elftoaout.1 "%buildroot/%_mandir/man1/"

%files
%defattr(-,root,root)
%_bindir/*
%_mandir/*/*

%changelog
