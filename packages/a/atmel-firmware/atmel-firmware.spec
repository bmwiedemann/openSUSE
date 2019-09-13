#
# spec file for package atmel-firmware
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           atmel-firmware
Version:        1.3
Release:        0
Summary:        Firmware for Atmel at76c50x Wireless Network Chips
License:        GPL-2.0+ and SUSE-Firmware
Group:          Hardware/Wifi
Url:            http://www.thekelleys.org.uk/atmel
Source0:        http://www.thekelleys.org.uk/atmel/atmel-firmware-%{version}.tar.gz
# Modules: at76c503-i3861.ko at76c503-i3863.ko at76c503.ko
#	   at76c503-rfmd-acc.ko at76c503-rfmd.ko at76c505a-rfmd2958.ko
#	   at76c505-rfmd2958.ko at76c505-rfmd.ko at76_usbdfu.ko
Supplements:    modalias(usb:v03EBp4102d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v03EBp760[3456]d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v03EBp761[347]d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v03F0p011Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v049Fp0032d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04A5p900[01]d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v04BBp0919d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0506p0A01d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v050Dp0050d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v055DpA000d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v05DDpFF31d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v066Bp2211d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0681p001Bd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v069Ap032[01]d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v069Ap0821d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v077Bp2219d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v077Bp2227d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v07AAp7613d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v07B8pB000d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v083Ap3501d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0864p410[02]d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0B3Bp1612d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0CDEp0001d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0D5CpA00[12]d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0D8Ep71[01]0d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0DB0p1020d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v1044p8003d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v12FDp1001d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v1371p0002d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v1371p001[34]d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v1371p5743d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v1668p7605d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v1915p2233d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v2001p3200d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v2019p3220d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v8086p0200d*dc*dsc*dp*ic*isc*ip*)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
# Generated with: extract-modaliases wlan-kmp-default.rpm

%description
The drivers for Atmel at76c50x wireless network chips in the Linux 2.6.x kernel
and at http://at76c503a.berlios.de/ do not include the firmware and this
firmware needs to be loaded by the host on most cards using these chips.

This package provides the firmware images that should be automatically loaded
as needed by the hotplug system. It also provides a small loader utility that
can be used to accomplish the same thing when hotplug is not in use.

%prep
%setup -q

%build

%install
mkdir -p -m 755 %{buildroot}/lib/firmware
cp images/* %{buildroot}/lib/firmware/
cp images.usb/* %{buildroot}/lib/firmware/
install -Dm755 atmel_fwl.pl %{buildroot}/%{_sbindir}/atmel_fwl
install -Dm644 atmel_fwl.8  %{buildroot}/%{_mandir}/man8/atmel_fwl.8

%files
%defattr(-,root,root)
%doc README COPYING
%{_sbindir}/atmel_fwl
%{_mandir}/man8/atmel_fwl.8.gz
/lib/firmware/*

%changelog
