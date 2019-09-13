#
# spec file for package flashrom
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           flashrom
Version:        1.1
Release:        0
Summary:        A universal flash programming utility
License:        GPL-2.0-only
Group:          Development/Tools/Other
Url:            https://flashrom.org/Flashrom
Source0:        https://download.flashrom.org/releases/%{name}-v%{version}.tar.bz2
Source1:        https://download.flashrom.org/releases/%{name}-v%{version}.tar.bz2.asc#/%{name}-%{version}.tar.bz2.sig
# Got the key from David Hendricks
Source2:        %{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libftdi1)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(zlib)
Requires:       dmidecode
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64

%description
flashrom is a utility for reading, writing, verifying and erasing flash ROM
chips. It's often used to flash BIOS/EFI/coreboot/firmware images in-system
using a supported mainboard, but it also supports flashing of network
cards (NICs), SATA controller cards, and other external devices which can
program flash chips.

It supports a wide range of DIP32, PLCC32, DIP8, SO8/SOIC8, TSOP32, and
TSOP40 chips, which use various protocols such as LPC, FWH, parallel flash,
or SPI.

%prep
%setup -q -n %{name}-v%{version}

%build
make %{?_smp_mflags} \
        CFLAGS="%{optflags}"

%install
install -d %{buildroot}/%{_sbindir}
install -d %{buildroot}/%{_mandir}/man8
install -m 0755 flashrom %{buildroot}/%{_sbindir}
install -m 0644 flashrom.8 %{buildroot}/%{_mandir}/man8

%files
%doc COPYING README
%{_sbindir}/flashrom
%{_mandir}/man8/flashrom.8%{ext_man}

%changelog
