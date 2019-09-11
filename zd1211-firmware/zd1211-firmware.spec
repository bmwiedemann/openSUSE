#
# spec file for package zd1211-firmware
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
# icecream 0


Name:           zd1211-firmware
Version:        1.5
Release:        0
Summary:        Firmware for ZD1211 USB WLAN sticks
License:        GPL-2.0+
Group:          Hardware/Wifi
Source:         http://downloads.sourceforge.net/zd1211/zd1211-firmware-%{version}.tar.bz2
Url:            http://zd1211.ath.cx/
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Modules: zd1211rw.ko
Supplements:    modalias(usb:v0053p5301d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0471p1236d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v050Dp705Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0586p340[129F]d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0586p341[023]d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v079Bp004Ad*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v079Bp0062d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v07B8p6001d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v083Ap4505d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0ACEp121[15]d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0ACEp2011d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0ACEp20FFd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0B05p170Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0B05p171Bd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0B3Bp[15]630d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0BAFp0121d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v0DF6p907[15]d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v126FpA006d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v13B1p001Ed*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v13B1p0024d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v1435p0711d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v14EApAB13d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v157Ep300[BD]d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v157Ep3204d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v1582p6003d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v1740p2000d*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v6891pA727d*dc*dsc*dp*ic*isc*ip*)
# Generated with: extract-modaliases zd1211rw

%description
Firmware for USB WLAN sticks based on the ZyDAS ZD1211 chip



%prep
%setup -n zd1211-firmware

%build

%install
install -d -m 755 %{buildroot}/lib/firmware/zd1211
install -m 644 zd* %{buildroot}/lib/firmware/zd1211

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README COPYING
/lib/firmware/zd1211

%changelog
