#
# spec file for package u-boot
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010 Texas Instruments Inc by Nishanth Menon
# Copyright (c) 2007-2010 by Silvan Calarco <silvan.calarco@mambasoft.it>
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


# 'archive_version' differs from 'version' for RC version only
%define archive_version 2019.04

Name:           u-boot
Version:        2019.04
Release:        0
Summary:        Tools for the U-Boot Firmware
License:        GPL-2.0-only
Group:          System/Boot
Url:            http://www.denx.de/wiki/U-Boot
Source:         ftp://ftp.denx.de/pub/u-boot/u-boot-%{archive_version}.tar.bz2
Source1:        ftp://ftp.denx.de/pub/u-boot/u-boot-%{archive_version}.tar.bz2.sig
Patch0001:      0001-XXX-openSUSE-XXX-Prepend-partition-.patch
Patch0002:      0002-Revert-Revert-omap3-Use-raw-SPL-by-.patch
Patch0003:      0003-rpi-Use-firmware-provided-device-tr.patch
Patch0004:      0004-Temp-workaround-for-Chromebook-snow.patch
Patch0005:      0005-zynqmp-Add-generic-target.patch
Patch0006:      0006-tools-zynqmpbif-Add-support-for-loa.patch
Patch0007:      0007-boo-1123170-Remove-ubifs-support-fr.patch
Patch0008:      0008-zynqmp-generic-fix-compilation.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libopenssl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Das U-Boot (or just "U-Boot" for short) is Open Source Firmware for Embedded PowerPC, ARM, MIPS and x86 processors.
This package contains:
mkimage- a tool that creates kernel bootable images for U-Boot.


%package tools
Summary:        Tools for the U-Boot Firmware
Group:          System/Boot

%description tools
Das U-Boot (or just "U-Boot" for short) is Open Source Firmware for Embedded PowerPC, ARM, MIPS and x86 processors.
This package contains:
mkimage- a tool that creates kernel bootable images for U-Boot.

%prep
%setup -q -n u-boot-%{archive_version}
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1

%build
# needed for include/config/auto.conf
make defconfig
make syncconfig
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" tools-only

%install
install -D -m 0755 tools/mkimage %{buildroot}%{_bindir}/mkimage
install -D -m 0644 doc/mkimage.1 %{buildroot}%{_mandir}/man1/mkimage.1

%files tools
%defattr(-,root,root)
%license Licenses/gpl-2.0.txt
%{_bindir}/mkimage
%{_mandir}/man1/mkimage.1.gz

%changelog
