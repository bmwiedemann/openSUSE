#
# spec file for package flashrom
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


Name:           flashrom
Version:        1.2
Release:        0
Summary:        A universal flash programming utility
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://flashrom.org/Flashrom
Source0:        https://download.flashrom.org/releases/%{name}-v%{version}.tar.bz2
Source1:        https://download.flashrom.org/releases/%{name}-v%{version}.tar.bz2.asc#/%{name}-%{version}.tar.bz2.sig
# Got the key from David Hendricks
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM https://github.com/flashrom/flashrom/commit/7aea04f7099ad4dde7b1f5900b54ef603eadf25e
Patch1:         flashrom-install-man-file.patch
# PATCH-FIX-UPSTREAM https://github.com/flashrom/flashrom/commit/13a356815d2438103689a6ea1ac7e58d4d508ddb
Patch2:         flashrom-j-link-spi.patch
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libftdi1)
%ifarch %{ix86} x86_64
BuildRequires:  pkgconfig(libjaylink)
%endif
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
%ifarch %{ix86} x86_64
  -Dconfig_jlink_spi=true \
  -Dconfig_internal=true \
%else
  -Dconfig_atahpt=false \
  -Dconfig_atapromise=false \
  -Dconfig_atavia=false \
  -Dconfig_drkaiser=false \
  -Dconfig_gfxnvidia=false \
  -Dconfig_it8212=false \
  -Dconfig_jlink_spi=false \
  -Dconfig_nic3com=false \
  -Dconfig_nicintel_eeprom=false \
  -Dconfig_nicintel=false \
  -Dconfig_nicintel_spi=false \
  -Dconfig_nicnatsemi=false \
  -Dconfig_nicrealtek=false \
  -Dconfig_ogp_spi=false \
  -Dconfig_rayer_spi=false \
  -Dconfig_satamv=false \
  -Dconfig_satasii=false \
  -Dconfig_internal=false \
%endif
  %{nil}

%meson_build

%install
%meson_install

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
