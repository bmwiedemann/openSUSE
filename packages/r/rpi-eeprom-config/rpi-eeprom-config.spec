#
# spec file for package rpi-eeprom-config
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


Name:           rpi-eeprom-config
Version:        0.0.20200625~9342fdb
Release:        0
Summary:        Raspberry Pi 4 eeprom firmware configuration tool
License:        BSD-3-Clause
Group:          System/Management
URL:            https://github.com/raspberrypi/rpi-eeprom.git
# Get it at: https://github.com/raspberrypi/rpi-eeprom/archive/master.zip
Source0:        rpi-eeprom-master.zip
Source1:        README
BuildRequires:  unzip
Requires:       raspberrypi-firmware-eeprom
Supplements:    modalias(of:N*T*Cbrcm,bcm2711*C*)
BuildArch:      noarch

%description
rpi-eeprom-config allows generating/extracting eeprom firmware configurations.

%prep
%setup -q -n rpi-eeprom-master
# Remove files which are not under BSD-3 license
rm -rf firmware/
cp -f %{SOURCE1} README

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -c -m 0755 rpi-eeprom-config %{buildroot}%{_bindir}

%files
%doc README
%{_bindir}/rpi-eeprom-config

 %changelog
