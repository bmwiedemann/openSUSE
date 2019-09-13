#
# spec file for package bcm43xx-firmware
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


Name:           bcm43xx-firmware
Version:        20180314
Release:        0
Summary:        Firmware for the Broadcom/Cypress BCM43xx chipset family
License:        SUSE-Firmware
Group:          System/Kernel
URL:            https://community.cypress.com/community/linux
# From https://github.com/raspberrypi/linux/issues/1325#issuecomment-195560582
# Phil Elwell (Raspberry Pi Foundation) wrote: "Broadcom have said that
# the firmware files for the BCM43438 are covered under this licence:"
Source0:        https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/plain/LICENCE.broadcom_bcm43xx
Source1:        50-brcmfmac.conf
Source2:        install-brcmfmac.sh
# The BCM43XXXX.hcd files are under this license
Source3:        https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/LICENCE.cypress
#BCM4329
Source291:      https://raw.githubusercontent.com/SolidRun/meta-solidrun-arm-imx6/fido/recipes-bsp/broadcom-nvram-config/files/solidrun-imx6/brcmfmac4329-sdio.txt#/brcmfmac4329-sdio-cubox-i.txt
#BCM4330
Source301:      https://raw.githubusercontent.com/SolidRun/meta-solidrun-arm-imx6/fido/recipes-bsp/broadcom-nvram-config/files/solidrun-imx6/brcmfmac4330-sdio.txt#/brcmfmac4330-sdio-cubox-i.txt
#BCM4339
Source391:      brcmfmac4339-sdio-vega-s95-telos.txt
#BCM43362
Source3621:     http://dl.cubieboard.org/public/Cubieboard/benn/firmware/ap6210/nvram_ap6210.txt#/brcmfmac43362-sdio-cubietruck.txt
Source3622:     https://github.com/Bananian/bananian/raw/master/deb/u-boot-m2-bananian_armhf/lib/firmware/brcm/brcmfmac43362-sdio.txt#/brcmfmac43362-sdio-bananapi-m2.txt
#BCM43430
Source4309:     https://github.com/RPi-Distro/bluez-firmware/raw/master/broadcom/BCM43430A1.hcd
#brcmfmac4356-pcie.txt is taken from ChromeOS repo
# https://chromium.googlesource.com/chromiumos/third_party/linux-firmware/+/f151f016b4fe656399f199e28cabf8d658bcb52b/brcm/brcmfmac4356-pcie.txt
Source4356:     brcmfmac4356-pcie.txt
#BCM43455
Source4559:     https://github.com/RPi-Distro/bluez-firmware/raw/master/broadcom/BCM4345C0.hcd
# Owns /lib/firmware/brcm and potentially conflicts
BuildRequires:  kernel-firmware
# Owns /etc/modprobe.d
BuildRequires:  suse-module-tools
Requires:       kernel-firmware
# BCM4356 PCI
Supplements:    modalias(pci:v000014E4d000043ECsv*sd*bc*sc*i*)
# Raspberry Pi 3 Model B
Supplements:    modalias(sdio:c*v02D0dA9A6*)
BuildArch:      noarch

%description
This package provides the firmware files needed for the
Broadcom (now Cypress) BCM43430 Wifi+Bluetooth chipset
as well as NVRAM config files for BCM43362, BCM43430 and
further related chipsets.

%prep
%setup -q -c -T
cp %{SOURCE0} %{SOURCE3} .

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d
install -c -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/modprobe.d
mkdir -p %{buildroot}%{_sbindir}
install -c -m 0755 %{SOURCE2} %{buildroot}%{_sbindir}/install-brcmfmac
# Used by brcmfmac
mkdir -p %{buildroot}/lib/firmware/brcm
install -c -m 0644 %{SOURCE291} %{buildroot}/lib/firmware/brcm/
install -c -m 0644 %{SOURCE301} %{buildroot}/lib/firmware/brcm/
install -c -m 0644 %{SOURCE391} %{buildroot}/lib/firmware/brcm/
install -c -m 0644 %{SOURCE3621} %{buildroot}/lib/firmware/brcm/
install -c -m 0644 %{SOURCE3622} %{buildroot}/lib/firmware/brcm/
install -c -m 0644 %{SOURCE4356} %{buildroot}/lib/firmware/brcm/
# Used by bluez (hciattach)
install -c -m 0644 %{SOURCE4309} %{buildroot}/lib/firmware/
install -c -m 0644 %{SOURCE4559} %{buildroot}/lib/firmware/

%files
%license LICENCE.broadcom_bcm43xx LICENCE.cypress
/lib/firmware/*.hcd
/lib/firmware/brcm/*.txt
%ghost /lib/firmware/brcm/brcmfmac4329-sdio.txt
%ghost /lib/firmware/brcm/brcmfmac4330-sdio.txt
%ghost /lib/firmware/brcm/brcmfmac4339-sdio.txt
%ghost /lib/firmware/brcm/brcmfmac43362-sdio.txt
%ghost /lib/firmware/brcm/brcmfmac43430-sdio.txt
%ghost /lib/firmware/brcm/brcmfmac43455-sdio.txt
%{_sysconfdir}/modprobe.d/50-brcmfmac.conf
%{_sbindir}/install-brcmfmac

%changelog
