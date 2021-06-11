#
# spec file for package stm32flash
#
# Copyright (c) 2021 SUSE LLC
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


Name:           stm32flash
Version:        0.6
Release:        0
Summary:        Flash Program for the STM32 Bootloader
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            https://sourceforge.net/p/stm32flash/wiki/Home
Source:         https://download.sourceforge.net/stm32flash/stm32flash-0.6.tar.gz
# PATCH-FIX-OPENSUSE stm32flash-i2c-tools-headers-clash.patch sbrabec@suse.cz -- Prevent clash between i2c.h and i2c-dev.h defining the same.
Patch3:         stm32flash-i2c-tools-headers-clash.patch
BuildRequires:  i2c-tools

%description
Open source flash program for the STM32 ARM processors using the ST
serial bootloader over UART or I2C.

Features:
- UART and I2C transports supported
- device identification
- write to flash/ram
- read from flash/ram
- auto-detect Intel HEX or raw binary input format with option to force
  binary
- flash from binary file
- save flash to binary file
- verify & retry up to N times on failed writes
- start execution at specified address
- software reset the device when finished if -R is specified
- resume already initialized connection (for when reset fails, UART only)
- GPIO signalling to enter bootloader mode (hardware dependent)

%prep
%setup -q
%if 0%{?suse_version} < 1315 || 0%{?suse_version} == 1320
%patch3 -p1
%endif

%build
%make_build CFLAGS="-O2 %{optflags}" PREFIX=%{_prefix}

%install
make %{?_smp_mflags} CFLAGS="-O2 %{optflags}" PREFIX=%{_prefix} DESTDIR=%{buildroot} install

%files
%license gpl-2.0.txt
%doc HOWTO I2C.txt protocol.txt TODO
%{_bindir}/stm32flash
%{_mandir}/man1/stm32flash.1*

%changelog
