#
# spec file for package technisat-usb2-firmware
#
# Copyright (c) 2021 SUSE LLC
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


%{?!_firmwaredir:%define _firmwaredir /lib/firmware}

Name:           technisat-usb2-firmware
Summary:        Firmware for Technisat SkyStar USB HD
License:        SUSE-Firmware
Group:          Hardware/TV
Version:        17.63
Release:        0
URL:            http://kernellabs.com/firmware/technisat-usb2/
Source0:        dvb-usb-SkyStar_USB_HD_FW_v17_63.HEX.fw
Source1:        dvb-usb-SkyStar_USB_HD_FW_v17_63.HEX.fw.license.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Supplements:    modalias(usb:v14F7p0500d*dc*dsc*dp*ic*isc*ip*)

%description
This package provides the firmware images that should be automatically loaded
as needed by the hotplug system.

%prep
%setup -c -n firmware -T
cp -a %{S:0} .
cp -a %{S:1} .

%build

%install
mkdir -p -m 755 %{buildroot}%{_firmwaredir}
cp dvb-usb-SkyStar_USB_HD_FW_v17_63.HEX.fw %{buildroot}%{_firmwaredir}/

%files
%defattr(-,root,root)
%doc dvb-usb-SkyStar_USB_HD_FW_v17_63.HEX.fw.license.txt
%{_firmwaredir}/*

%changelog
