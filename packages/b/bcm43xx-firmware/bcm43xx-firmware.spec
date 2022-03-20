#
# spec file for package bcm43xx-firmware
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


%if !%{defined _firmwaredir}
%define _firmwaredir /lib/firmware
%endif

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
# The BCM43XXXX.hcd files are under this license
Source3:        https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/LICENCE.cypress
#BCM4329
Source291:      https://raw.githubusercontent.com/SolidRun/meta-solidrun-arm-imx6/fido/recipes-bsp/broadcom-nvram-config/files/solidrun-imx6/brcmfmac4329-sdio.txt#/brcmfmac4329-sdio.solidrun,cubox-i-dl.txt
#BCM4330
Source301:      https://raw.githubusercontent.com/SolidRun/meta-solidrun-arm-imx6/fido/recipes-bsp/broadcom-nvram-config/files/solidrun-imx6/brcmfmac4330-sdio.txt#/brcmfmac4330-sdio.solidrun,cubox-i-q.txt
#BCM4339
Source391:      brcmfmac4339-sdio.tronsmart,vega-s95-telos.txt
#BCM43362
Source3622:     https://github.com/Bananian/bananian/raw/master/deb/u-boot-m2-bananian_armhf/lib/firmware/brcm/brcmfmac43362-sdio.txt#/brcmfmac43362-sdio.sinovoip,bpi-m2.txt
#BCM43430
Source4309:     https://github.com/RPi-Distro/bluez-firmware/raw/master/broadcom/BCM43430A1.hcd
Source4310:     https://github.com/RPi-Distro/bluez-firmware/raw/master/broadcom/BCM43430B0.hcd
#brcmfmac4356-pcie.txt is taken from ChromeOS repo
# https://chromium.googlesource.com/chromiumos/third_party/linux-firmware/+/f151f016b4fe656399f199e28cabf8d658bcb52b/brcm/brcmfmac4356-pcie.txt
Source4356:     brcmfmac4356-pcie.txt
#BCM43456
Source4561:     https://github.com/RPi-Distro/firmware-nonfree/raw/buster/brcm/brcmfmac43456-sdio.bin
Source4562:     https://github.com/RPi-Distro/firmware-nonfree/raw/buster/brcm/brcmfmac43456-sdio.clm_blob
Source4563:     https://github.com/RPi-Distro/firmware-nonfree/raw/buster/brcm/brcmfmac43456-sdio.txt
Source4564:     https://github.com/RPi-Distro/bluez-firmware/raw/master/broadcom/BCM4345C5.hcd
Source4559:     https://github.com/RPi-Distro/bluez-firmware/raw/master/broadcom/BCM4345C0.hcd
#BCM43436 aka BCM43430b0
Source4600:     https://github.com/RPi-Distro/firmware-nonfree/raw/buster/brcm/brcmfmac43436-sdio.bin
Source4601:     https://github.com/RPi-Distro/firmware-nonfree/raw/buster/brcm/brcmfmac43436-sdio.clm_blob
Source4602:     https://github.com/RPi-Distro/firmware-nonfree/raw/buster/brcm/brcmfmac43436-sdio.txt
# Owns /lib/firmware/brcm and potentially conflicts
BuildRequires:  kernel-firmware-brcm
# Owns /etc/modprobe.d
BuildRequires:  suse-module-tools
Requires:       kernel-firmware-brcm
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
# Used by brcmfmac
mkdir -p %{buildroot}%{_firmwaredir}/brcm
install -c -m 0644 %{SOURCE291} %{buildroot}%{_firmwaredir}/brcm/
install -c -m 0644 %{SOURCE301} %{buildroot}%{_firmwaredir}/brcm/
install -c -m 0644 %{SOURCE391} %{buildroot}%{_firmwaredir}/brcm/
install -c -m 0644 %{SOURCE3622} %{buildroot}%{_firmwaredir}/brcm/
install -c -m 0644 %{SOURCE4356} %{buildroot}%{_firmwaredir}/brcm/
install -c -m 0644 %{SOURCE4561} %{buildroot}%{_firmwaredir}/brcm/
install -c -m 0644 %{SOURCE4562} %{buildroot}%{_firmwaredir}/brcm/
install -c -m 0644 %{SOURCE4563} %{buildroot}%{_firmwaredir}/brcm/
install -c -m 0644 %{SOURCE4600} %{buildroot}%{_firmwaredir}/brcm/
install -c -m 0644 %{SOURCE4601} %{buildroot}%{_firmwaredir}/brcm/
install -c -m 0644 %{SOURCE4602} %{buildroot}%{_firmwaredir}/brcm/
ln -s brcmfmac43456-sdio.txt %{buildroot}%{_firmwaredir}/brcm/brcmfmac43456-sdio.raspberrypi,400.txt
ln -s brcmfmac43436-sdio.bin %{buildroot}%{_firmwaredir}/brcm/brcmfmac43430b0-sdio.raspberrypi,model-zero-2-w.bin
ln -s brcmfmac43436-sdio.txt %{buildroot}%{_firmwaredir}/brcm/brcmfmac43430b0-sdio.raspberrypi,model-zero-2-w.txt
ln -s brcmfmac43436-sdio.clm_blob %{buildroot}%{_firmwaredir}/brcm/brcmfmac43430b0-sdio.clm_blob
# We have conflicting versions of CM4's brcmfmac configuration, some
# pre-release dev versions depend on 43456 whereas store bought ones depend on
# 43455. Let's keep both for now.
ln -s brcmfmac43456-sdio.txt %{buildroot}%{_firmwaredir}/brcm/brcmfmac43456-sdio.raspberrypi,4-compute-module.txt
ln -s brcmfmac43455-sdio.raspberrypi,4-model-b.txt.xz  %{buildroot}%{_firmwaredir}/brcm/brcmfmac43455-sdio.raspberrypi,4-compute-module.txt.xz

# serdev configured RPi Bluetooth driver expects the firmware files to be
# stored in '/lib/firmware/brcm'
install -c -m 0644 %{SOURCE4309} %{buildroot}%{_firmwaredir}/brcm/
install -c -m 0644 %{SOURCE4310} %{buildroot}%{_firmwaredir}/brcm/
install -c -m 0644 %{SOURCE4559} %{buildroot}%{_firmwaredir}/brcm/
install -c -m 0644 %{SOURCE4564} %{buildroot}%{_firmwaredir}/brcm/
# Symlinks for compatibility with deprecated hciattach
ln -s brcm/BCM4345C0.hcd %{buildroot}%{_firmwaredir}/BCM4345C0.hcd
ln -s brcm/BCM4345C5.hcd %{buildroot}%{_firmwaredir}/BCM4345C5.hcd
ln -s brcm/BCM43430A1.hcd %{buildroot}%{_firmwaredir}/BCM43430A1.hcd
ln -s brcm/BCM43430B0.hcd %{buildroot}%{_firmwaredir}/BCM43430B0.hcd

%files
%license LICENCE.broadcom_bcm43xx LICENCE.cypress
%{_firmwaredir}/BCM43430A1.hcd
%{_firmwaredir}/BCM43430B0.hcd
%{_firmwaredir}/BCM4345C0.hcd
%{_firmwaredir}/BCM4345C5.hcd
%{_firmwaredir}/brcm/BCM43430A1.hcd
%{_firmwaredir}/brcm/BCM43430B0.hcd
%{_firmwaredir}/brcm/BCM4345C0.hcd
%{_firmwaredir}/brcm/BCM4345C5.hcd
%{_firmwaredir}/brcm/brcmfmac4329-sdio.solidrun,cubox-i-dl.txt
%{_firmwaredir}/brcm/brcmfmac4330-sdio.solidrun,cubox-i-q.txt
%{_firmwaredir}/brcm/brcmfmac4339-sdio.tronsmart,vega-s95-telos.txt
%{_firmwaredir}/brcm/brcmfmac43362-sdio.sinovoip,bpi-m2.txt
%{_firmwaredir}/brcm/brcmfmac43430b0-sdio.clm_blob
%{_firmwaredir}/brcm/brcmfmac43430b0-sdio.raspberrypi,model-zero-2-w.bin
%{_firmwaredir}/brcm/brcmfmac43430b0-sdio.raspberrypi,model-zero-2-w.txt
%{_firmwaredir}/brcm/brcmfmac43436-sdio.bin
%{_firmwaredir}/brcm/brcmfmac43436-sdio.clm_blob
%{_firmwaredir}/brcm/brcmfmac43436-sdio.txt
%{_firmwaredir}/brcm/brcmfmac4356-pcie.txt
%{_firmwaredir}/brcm/brcmfmac43456-sdio.bin
%{_firmwaredir}/brcm/brcmfmac43456-sdio.clm_blob
%{_firmwaredir}/brcm/brcmfmac43456-sdio.txt
%{_firmwaredir}/brcm/brcmfmac43456-sdio.raspberrypi,400.txt
%{_firmwaredir}/brcm/brcmfmac43456-sdio.raspberrypi,4-compute-module.txt
%{_firmwaredir}/brcm/brcmfmac43455-sdio.raspberrypi,4-compute-module.txt.xz

%changelog
