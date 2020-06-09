#
# spec file for package hex2bin
#
# Copyright (c) 2020 SUSE LLC
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


Name:           hex2bin
Version:        2.5
Release:        0
Summary:        Converts Motorola and Intel hex files to binary
License:        BSD-2-Clause
Group:          Development/Tools/Building
URL:            https://sourceforge.net/projects/hex2bin
Source:         https://downloads.sourceforge.net/%{name}/Hex2bin-%{version}.tar.bz2
BuildRequires:  dos2unix
# PATCH-FIX-OPENSUSE Hex2bin-gcc10.patch
Patch0:         Hex2bin-gcc10.patch

%description
Converts Motorola and Intel hex files to binary. For other formats, check this
project also on sourceforge: srecord

%prep
%autosetup -p1 -n Hex2bin-%{version}
rm -f hex2bin mot2bin
dos2unix doc/S-record.txt doc/srec.txt
sed -e 's/^CPFLAGS =.*/CPFLAGS = -std=c99 %{optflags}/' \
    -e 's/gcc -O2 -Wall/gcc $(CPFLAGS)/' \
    -i Makefile

%build
%make_build

%install
install -d %{buildroot}/%{_bindir} %{buildroot}/%{_mandir}/man1
install -m 0755 hex2bin mot2bin %{buildroot}/%{_bindir}
install -m 0644 hex2bin.1 %{buildroot}%{_mandir}/man1

%files
%doc doc/*
%{_bindir}/hex2bin
%{_bindir}/mot2bin
%{_mandir}/man1/hex2bin.1%{ext_man}

%changelog
