#
# spec file for package flashrom
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.3.0
Release:        0
Summary:        A universal flash programming utility
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://flashrom.org/Flashrom
Source0:        https://download.flashrom.org/releases/%{name}-v%{version}.tar.bz2
Source1:        https://download.flashrom.org/releases/%{name}-v%{version}.tar.bz2.asc#/%{name}-%{version}.tar.bz2.sig
# Got the key from David Hendricks
Source2:        %{name}.keyring
BuildRequires:  meson >= 0.53.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(libftdi1)
BuildRequires:  pkgconfig(libjaylink)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(zlib)
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 riscv64

%description
flashrom is a utility for reading, writing, verifying and erasing flash ROM
chips. It's often used to flash BIOS/EFI/coreboot/firmware images in-system
using a supported mainboard, but it also supports flashing of network
cards (NICs), SATA controller cards, and other external devices which can
program flash chips.

It supports a wide range of DIP32, PLCC32, DIP8, SO8/SOIC8, TSOP32, and
TSOP40 chips, which use various protocols such as LPC, FWH, parallel flash,
or SPI.

%package -n libflashrom1
Summary:        A universal flash programming utility
Group:          Development/Tools/Other

%description -n libflashrom1
flashrom is a utility for reading, writing, verifying and erasing flash ROM
chips. It's often used to flash BIOS/EFI/coreboot/firmware images in-system
using a supported mainboard, but it also supports flashing of network
cards (NICs), SATA controller cards, and other external devices which can
program flash chips.

%prep
%autosetup -p1 -n %{name}-v%{version}

%package devel
Summary:        A universal flash programming utility
Group:          Development/Tools/Other
Requires:       libflashrom1 = %{version}-%{release}

%description devel
flashrom is a utility for reading, writing, verifying and erasing flash ROM
chips. It's often used to flash BIOS/EFI/coreboot/firmware images in-system
using a supported mainboard, but it also supports flashing of network
cards (NICs), SATA controller cards, and other external devices which can
program flash chips.

This package contains the headers needed to compile against libflashrom.

%build
%meson \
    -Dtests=disabled
%meson_build

%install
%meson_install
rm %{buildroot}%{_libdir}/libflashrom.a

%post -n libflashrom1 -p /sbin/ldconfig
%postun -n libflashrom1 -p /sbin/ldconfig

%files
%license COPYING
%doc README
%{_sbindir}/flashrom
%{_mandir}/man8/flashrom.8%{ext_man}

%files -n libflashrom1
%{_libdir}/libflashrom.so.1
%{_libdir}/libflashrom.so.1.0.0

%files devel
%{_includedir}/libflashrom.h
%{_libdir}/libflashrom.so
%{_libdir}/pkgconfig/flashrom.pc

%changelog
