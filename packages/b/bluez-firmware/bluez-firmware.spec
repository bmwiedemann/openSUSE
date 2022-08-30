#
# spec file for package bluez-firmware
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


Name:           bluez-firmware
Version:        1.2
Release:        0
Summary:        Bluetooth(TM) Firmware
License:        GPL-2.0-only AND GPL-2.0-or-later AND SUSE-Firmware
Group:          Hardware/Mobile
URL:            http://www.bluez.org/
Source0:        http://bluez.sf.net/download/%{name}-%{version}.tar.gz
Source1:        bfusb.tar.bz2
BuildRequires:  automake
# Modules: bcm203x.ko bfusb.ko
Supplements:    modalias(usb:v057Cp2200d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0A5Cp2033d*dc*dsc*dp*ic*isc*ip*)
Obsoletes:      bluez-bluefw
# Generated with: extract-modaliases -i bcm203x -i bfusb kernel-default.rpm

%description
Bluetooth(TM) Firmware. Package contains firmware images for some
   Bluetooth(TM) adapters. Currently supported are: * Broadcom
   Corporation BCM2033

* AVM Computersysteme Vertriebs GmbH BLUEFRITZ! USB

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., USA.

%prep
%setup -q -b 1

%build
autoreconf -fi
%configure \
	--libdir=%{_firmwaredir}/../
%make_build

%install
%make_install
rm %{buildroot}%{_firmwaredir}/BCM-LEGAL.txt
install -D -m 644 ../bfusb/bfubase.frm %{buildroot}%{_firmwaredir}/bfubase.frm

%files
%{_firmwaredir}/*
%license COPYING
%doc AUTHORS INSTALL ChangeLog README broadcom/BCM-LEGAL.txt

%changelog
