#
# spec file for package raspberrypi-firmware-dt
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


Name:           raspberrypi-firmware-dt
Version:        2025.05.14
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
Source6:        fixup-blconfig-overlay.dts
Source100:      get-from-git.sh
Patch0:         0001-ARM-dts-bcm2711-rpi-Reuse-bcm2836-vchiq-driver.patch
Patch1:         0001-ARM-dts-bcm27xx-Use-better-name-for-spidev.patch
Patch2:         0001-Revert-bcm2711-rpi-ds-Switch-to-dma40-channel-for-hd.patch
Patch3:         0002-ARM-dts-bcm2711-Fix-xHCI-power-domain.patch
Patch4:         0001-dts-rp1-Wrap-RP1-node-into-nexus-node-as-expected-by.patch
Patch5:         0001-ARM-dts-bcm2712-Remove-DMA-support.patch
Patch6:         0001-ARM-dts-bcm2712-Slow-down-eMMC-interface.patch
Patch7:         bcm2712-fix-compatible.patch
Patch8:         0001-Amend-the-RP1-ethernet-node-to-work-with-upstream-dr.patch
Patch9:         0001-dts-overlays-Adjust-them-for-RPi5.patch
Patch10:	0001-dts-bcm2712-Extend-PCIe-range-to-encompass-firmware-.patch
Patch11:	0001-dts-arm64-rp1-Fix-PCIe-topology.patch
Requires:       raspberrypi-firmware
Requires:       kernel >= 6.19.0
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
%autopatch -p1

%build
SRCDIR=`pwd`
mkdir pp
PPDIR=`pwd`/pp

export DTC_FLAGS="-R 4 -p 0x1000 -@ -H epapr"
for dts in arch/arm/boot/dts/broadcom/bcm27*dts arch/arm64/boot/dts/broadcom/bcm27*dts; do
    target=$(basename ${dts%*.dts})
    cpp -x assembler-with-cpp -undef -D__DTS__ -DFIRMWARE_UPDATED -nostdinc -I. -I$SRCDIR/include/ -I$SRCDIR/scripts/dtc/include-prefixes/ -P $dts -o $PPDIR/$target.dts
    dtc $DTC_FLAGS -I dts -O dtb -i ./$(dirname $dts) -o $PPDIR/$target.dtb $PPDIR/$target.dts
done

export DTC_FLAGS="-R 0 -p 0 -@ -H epapr"
for dts in arch/arm/boot/dts/overlays/*dts %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6}; do
    target=$(basename ${dts%*.dts})
    target=${target%*-overlay}
    mkdir -p $PPDIR/overlays
    cpp -x assembler-with-cpp -undef -D__DTS__ -DFIRMWARE_UPDATED -nostdinc -I. -I$SRCDIR/include/ -I$SRCDIR/scripts/dtc/include-prefixes/ -P $dts -o $PPDIR/overlays/$target.dts
    dtc $DTC_FLAGS -I dts -O dtb -i ./$(dirname $dts) -o $PPDIR/overlays/$target.dtbo $PPDIR/overlays/$target.dts
done

# These are loaded implicitly by the RPi 5 firmware and it
# expect these exact names.
mv $PPDIR/overlays/hat_map.dtbo $PPDIR/overlays/hat_map.dtb
mv $PPDIR/overlays/overlay_map.dtbo $PPDIR/overlays/overlay_map.dtb

# Include README file
cp arch/arm/boot/dts/overlays/README $PPDIR/overlays/

%define dtbdir /boot/vc

%install
install -m 700 -d %{buildroot}%{dtbdir}/
install -m 700 -d %{buildroot}%{dtbdir}/overlays

for dtb in pp/*.dtb; do
    install -m 644 $dtb %{buildroot}%{dtbdir}/
done

for dtbo in pp/overlays/*.dtb*; do
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
/boot/vc/overlays/*dtb
/boot/vc/overlays/README

%changelog
