#
# spec file for package bananapir2-firmware
#
# Copyright (c) 2025 SUSE LLC
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


Name:           bananapir2-firmware
Version:        0.0~git20201119.b0a0872
Release:        0
Summary:        Binary bootloader and firmware files for Banana Pi R2
License:        SUSE-Firmware
Group:          System/Boot
URL:            https://github.com/mbgg/bananapir2-firmware
Source0:        https://github.com/mbgg/bananapir2-firmware/raw/master/LICENCE.mediatek
Source1:        https://github.com/mbgg/bananapir2-firmware/raw/master//BPI-R2-HEAD440-0k.img.gz
Source2:        https://github.com/mbgg/bananapir2-firmware/raw/master/BPI-R2-HEAD1-512b.img.gz
Source3:        https://github.com/mbgg/bananapir2-firmware/raw/master/BPI-R2-preloader-DDR1600-20191024-2k.img.gz
BuildArch:      noarch
BuildRequires:  gzip

%description
Binary bootloader and firmware files for Banana Pi R2

%prep
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} ./
gunzip *.gz
cp %{SOURCE0} ./

%build

%install
mkdir -p %{buildroot}/boot/fw
install -D -m 0644 BPI-R2-HEAD440-0k.img %{buildroot}/boot/fw/BPI-R2-HEAD440-0k.img
install -D -m 0644 BPI-R2-HEAD1-512b.img %{buildroot}/boot/fw/BPI-R2-HEAD1-512b.img
install -D -m 0644 BPI-R2-preloader-DDR1600-20191024-2k.img %{buildroot}/boot/fw/preloader.bin

%files
%license LICENCE.mediatek
%defattr(-,root,root)
%dir /boot/fw
/boot/fw/*

%changelog
