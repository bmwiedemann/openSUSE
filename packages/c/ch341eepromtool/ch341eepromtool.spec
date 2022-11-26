#
# spec file for package ch341eepromtool
#
# Copyright (c) 2022 SUSE LLC
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


Name:           ch341eepromtool
Version:        0.5
Release:        0
Summary:        I2C Serial EEPROM Programming Tool for the WCH CH341A
License:        GPL-3.0-or-later
Group:          Hardware/Other
URL:            https://sourceforge.net/projects/ch341eepromtool/
Patch1:         ch341eepromtool-printf.patch
Patch2:         ch341eepromtool-extern_readbuf.patch
BuildRequires:  libusb-1_0-devel
BuildRequires:  pkgconfig
Source:         %{name}_%{version}.tar.gz

%description
An I2C serial EEPROM programming tool for cheap Winchiphead CH341 IC based programmers.

%prep
%setup -q -n %{name}_%{version}
%patch1 -p1
%patch2 -p1

%build
gcc -Wall -O2 %{optflags} ch341eeprom.c ch341funcs.c -lusb-1.0 -o ch341eeprom $(pkg-config libusb-1.0 --libs --cflags)

%install
mkdir -p %{buildroot}%{_bindir}
install ch341eeprom %{buildroot}%{_bindir}/

%files
%license COPYING
%doc README
%{_bindir}/*

%changelog
