#
# spec file for package ipw-firmware
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


Name:           ipw-firmware
Summary:        Firmware for Intel PRO/Wireless WLAN Cards
License:        SUSE-Firmware
Group:          Hardware/Wifi
Version:        9
Release:        0
%define version_2100 1.3
%define version_2200 2.4
%define version_3945 1.14.2
URL:            http://ipw2200.sourceforge.net/firmware.php
Source0:        ipw2100-fw-%{version_2100}.tar.bz2
Source1:        ipw2200-fw-%{version_2200}.tar.bz2
Source2:        ipw2200-fw-2.3.tar.bz2
Source3:        ipw2200-fw-2.2.tar.bz2
Source4:        ipw2200-fw-3.1.tar.bz2
BuildArch:      noarch
Requires(post): modutils grep
# Modules: ipw2100.ko ipw2200.ko
Supplements:    modalias(pci:v00008086d00001043sv0000103Csd00002741bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001043sv00008086sd0000252[0123456789BCD]bc*)
Supplements:    modalias(pci:v00008086d00001043sv00008086sd0000255[01345]bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001043sv00008086sd0000256[0123567]bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001043sv00008086sd000025[78]0bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001043sv00008086sd0000258[123567]bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001043sv00008086sd0000259[012368]bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001043sv00008086sd000025A0bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001043sv00008086sd0000270[12]bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001043sv00008086sd0000271[12]bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001043sv00008086sd0000272[12]bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001043sv00008086sd0000273[12]bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001043sv00008086sd0000274[12]bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001043sv00008086sd0000275[1234]bc*sc*i*)
Supplements:    modalias(pci:v00008086d00001043sv00008086sd0000276[12]bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000104Fsv*sd*bc*sc*i*)
Supplements:    modalias(pci:v00008086d0000422[0134]sv*sd*bc*sc*i*)
# Generated with: extract-modaliases -i ipw* kernel-default.rpm

%description
This package contains firmware binaries needed for Intel PRO/Wireless
2100/2200BG (aka Centrino) WLAN cards. The package is covered by the
Intel license. See http://ipw2100.sourceforge.net/firmware.php?fid=4.

%prep
%setup -cq -a1 -a2 -a3 -a4

%build

%install
mkdir -p %{buildroot}/lib/firmware
cp *fw ipw2200-fw-3.1/*fw %{buildroot}/lib/firmware
cp LICENSE %{buildroot}/lib/firmware/LICENSE.ipw2x00

%post
test -f /.buildenv && exit 0
driver_active()
{
	for i in /sys/class/net/*/device/driver ; do
		test -e $i || continue
		DRV=$(basename `readlink $i`)
		test "$DRV" = "$1" && return 0
	done
	return 1
}
for M in ipw2100 ipw2200 ; do
	if /sbin/lsmod | grep -q ^$M ; then
		driver_active $M ||
		{ echo "Reloading module $M"; rmmod $M; modprobe $M; }
	fi
done

%files
/lib/firmware/*

%changelog
