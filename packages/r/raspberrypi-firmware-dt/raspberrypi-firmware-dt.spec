#
# spec file for package raspberrypi-firmware-dt
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


Name:           raspberrypi-firmware-dt
Version:        2022.12.21
Release:        0
Summary:        Device trees for the Raspberry Pi firmware loader
License:        GPL-2.0-only
Group:          System/Boot
URL:            https://github.com/raspberrypi/linux/
Source:         raspberrypi-firmware-dt-%{version}.tar.xz
Source1:        disable-vc4-overlay.dts
Source2:        uboot-bcm2835-pl011-overlay.dts
Source3:        disable-v3d-overlay.dts
Source4:        enable-bt-overlay.dts
Source5:        smbios-overlay.dts
Source100:      get-from-git.sh
Requires:       raspberrypi-firmware
BuildRequires:  dtc
BuildRequires:  raspberrypi-firmware
BuildArch:      noarch
Conflicts:      kernel < 4.12.14
Supplements:    modalias(of:NfirmwareT*Craspberrypi%2Cbcm2835-firmwareC*)

%description
This package provides additional device tree base files as well as overlays
for the Raspberry Pi boot process.

%prep
%setup -q

%build
SRCDIR=`pwd`
mkdir pp
PPDIR=`pwd`/pp

export DTC_FLAGS="-R 4 -p 0x1000 -@ -H epapr"
for dts in arch/arm/boot/dts/bcm27*dts arch/arm64/boot/dts/broadcom/bcm27*dts; do
    target=$(basename ${dts%*.dts})
    cpp -x assembler-with-cpp -undef -D__DTS__ -nostdinc -I. -I$SRCDIR/include/ -I$SRCDIR/scripts/dtc/include-prefixes/ -P $dts -o $PPDIR/$target.dts
    dtc $DTC_FLAGS -I dts -O dtb -i ./$(dirname $dts) -o $PPDIR/$target.dtb $PPDIR/$target.dts
done

export DTC_FLAGS="-R 0 -p 0 -@ -H epapr"
for dts in arch/arm/boot/dts/overlays/*dts %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5}; do
    target=$(basename ${dts%*.dts})
    target=${target%*-overlay}
    mkdir -p $PPDIR/overlays
    cpp -x assembler-with-cpp -undef -D__DTS__ -nostdinc -I. -I$SRCDIR/include/ -I$SRCDIR/scripts/dtc/include-prefixes/ -P $dts -o $PPDIR/overlays/$target.dts
    dtc $DTC_FLAGS -I dts -O dtb -i ./$(dirname $dts) -o $PPDIR/overlays/$target.dtbo $PPDIR/overlays/$target.dts
done
# Include README file
cp arch/arm/boot/dts/overlays/README $PPDIR/overlays/

%define dtbdir /boot/vc

%install
install -m 700 -d %{buildroot}%{dtbdir}/
install -m 700 -d %{buildroot}%{dtbdir}/overlays

for dtb in pp/*.dtb; do
    install -m 644 $dtb %{buildroot}%{dtbdir}/
done

for dtbo in pp/overlays/*.dtbo; do
    install -m 644 $dtbo %{buildroot}%{dtbdir}/overlays/
done
install -m 644 pp/overlays/README %{buildroot}%{dtbdir}/overlays/

%post
if mountpoint -q /boot/efi && [ ! -L /boot/efi ]; then
    cp -r /boot/vc/*dtb /boot/vc/overlays /boot/efi/
fi

%files
%defattr(-,root,root)
%license COPYING
%dir /boot/vc/overlays
/boot/vc/*dtb
/boot/vc/overlays/*dtbo
/boot/vc/overlays/README

%changelog
