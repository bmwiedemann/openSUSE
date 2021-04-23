#
# spec file for package raspberrypi-firmware-eeprom
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

%define         archive_version 2020-09-03-vl805-000138a1
# url version is a bit different
%define         url_version 2020.09.03-138a1
Name:           raspberrypi-firmware-eeprom
Version:        2020.09.03.138a1
Release:        0
Summary:        Raspberry Pi 4 EEPROM firmware upgrade package
License:        SUSE-Firmware
Group:          System/Boot
URL:            https://github.com/raspberrypi/rpi-eeprom
Source0:        https://github.com/raspberrypi/rpi-eeprom/releases/download/v%{url_version}/rpi-boot-eeprom-recovery-%{archive_version}.zip
Source1:        get-latest-release.sh
BuildRequires:  raspberrypi-firmware
BuildRequires:  unzip
Requires:       raspberrypi-firmware
Requires(post): util-linux
Requires(preun): util-linux
Supplements:    modalias(of:N*T*Cbrcm,bcm2711*C*)
BuildArch:      noarch

%description
First stage bootloader fimware upgrade package for Raspberry Pi 4

How this is meant to work:

The update mechanism writes recovery.bin and the EEPROM update image(s)
(pieeprom.upd and vl805.bin) to the EFI partition. The SHA256 hash of the
corresponding images are written to pieeprom.sig and/or vl805.sig. This guards
against file system corruption which could cause the EEPROM to be flashed with
an invalid image. This is not a security check.

At the next reboot the ROM runs recovery.bin which updates EEPROM(s).  If the
update was successful recovery.bin renames itself to RECOVERY.000 to prevent it
from running a second time then resets the system.  The system should then boot
normally.

Upon upgrading rasperrypi-firmware-eeprom we make sure that the RECOVERY.000 is
deleted, so as not to bloat the EFI partition.

%prep
%setup -q -c -n rpi-boot-eeprom-recovery-%{archive_version}

%build

%install
mkdir -p %{buildroot}/boot/vc/firmware
for file in pieeprom.bin pieeprom.sig recovery.bin vl805.bin vl805.sig; do
	install -D -p -m 0644 ${file} %{buildroot}/boot/vc/firmware
done
mv %{buildroot}/boot/vc/firmware/pieeprom.bin %{buildroot}/boot/vc/firmware/pieeprom.upd

%post
if mountpoint -q /boot/efi && [[ ! -L /boot/efi ]]; then
	cp /boot/vc/firmware/* /boot/efi
fi

%postun
if mountpoint -q /boot/efi && [[ ! -L /boot/efi ]]; then
	rm -f /boot/efi/RECOVERY.*

	[ $1 -eq 0 ] && for file in pieeprom.upd pieeprom.sig recovery.bin vl805.bin vl805.sig; do
		rm -f /boot/efi/${file}
	done || true
fi

%files
%dir /boot/vc/firmware/
/boot/vc/firmware/pieeprom*
/boot/vc/firmware/vl805*
/boot/vc/firmware/recovery*

%changelog
