#
# spec file for package dfu-programmer
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           dfu-programmer
Version:        0.7.2
Release:        0
Summary:        A Device Firmware Update based USB programmer for Atmel chips
License:        GPL-2.0+
Group:          Development/Tools/Other
Url:            http://dfu-programmer.sourceforge.net
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libusb-1.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
dfu-programmer is an implementation of the Device Firmware Upgrade class
USB driver that enables firmware upgrades for various USB enabled (with the
correct bootloader) Atmel chips. This program was created because the
Atmel "FLIP" program for flashing devices does not support flashing via USB
on Linux, and because standard DFU loaders do not work for Atmel's chips.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-, root, root)
%doc AUTHORS NEWS README COPYING
%{_bindir}/dfu-programmer
%{_mandir}/man1/%{name}.1*

%changelog
