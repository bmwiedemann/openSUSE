#
# spec file for package raspberrypi-eeprom
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


%if 0%{?suse_version} < 1550
%define _firmwaredir /lib/firmware
%endif

Name:           raspberrypi-eeprom
Version:        2023.01.11
Release:        0
Summary:        Raspberry Pi 4 EEPROM firmware
License:        SUSE-Firmware
Group:          System/Boot
URL:            https://github.com/raspberrypi/rpi-eeprom
Source0:        %{name}-%{version}.tar.xz
Patch0:         add-suse-config.patch
Patch1:         dont-use-env.patch
Patch2:         rpi-eeprom-update-Use-tr-instead-of-strings.patch
Provides:       rpi-eeprom
Supplements:    modalias(of:N*T*Cbrcm%2Cbcm2711*C*)
Requires:       raspberrypi-firmware >= 2021.03.03
Requires:       raspberrypi-firmware-dt >= 2021.03.03
Provides:       rpi-eeprom-config = %{version}
Obsoletes:      rpi-eeprom-config < %{version}
Requires:       pciutils
Requires:       raspberrypi-eeprom-firmware
BuildArch:      noarch

%description
First stage bootloader packages for Raspberry Pi 4

%package firmware
Summary:        Raspberry Pi 4 EEPROM firmware blobs
Group:          System/Boot
Provides:       raspberrypi-firmware-eeprom = %{version}
Obsoletes:      raspberrypi-firmware-eeprom < %{version}
Requires:       raspberrypi-eeprom
BuildRequires:  fdupes

%description firmware
First stage bootloader fimware blobs for Raspberry Pi 4

%prep
%autosetup -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 rpi-eeprom-config %{buildroot}%{_bindir}
install -m 0755 rpi-eeprom-digest %{buildroot}%{_bindir}
install -m 0755 rpi-eeprom-update %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/default
install -m 644 rpi-eeprom-update-default %{buildroot}/etc/default/rpi-eeprom-update

mkdir -p %{buildroot}/%{_firmwaredir}/raspberrypi/bootloader
mv firmware/beta %{buildroot}/%{_firmwaredir}/raspberrypi/bootloader
mv firmware/critical %{buildroot}/%{_firmwaredir}/raspberrypi/bootloader
mv firmware/stable %{buildroot}/%{_firmwaredir}/raspberrypi/bootloader
cp -a firmware/latest %{buildroot}/%{_firmwaredir}/raspberrypi/bootloader
cp -a firmware/default %{buildroot}/%{_firmwaredir}/raspberrypi/bootloader
%fdupes -s %{buildroot}/%{_firmwaredir}/raspberrypi/bootloader

%files
%license LICENSE
%{_bindir}/rpi-eeprom-config
%{_bindir}/rpi-eeprom-digest
%{_bindir}/rpi-eeprom-update
%config /etc/default/rpi-eeprom-update

%files firmware
%{_firmwaredir}
%{_firmwaredir}/raspberrypi
%{_firmwaredir}/raspberrypi/bootloader/beta
%{_firmwaredir}/raspberrypi/bootloader/critical
%{_firmwaredir}/raspberrypi/bootloader/stable
%{_firmwaredir}/raspberrypi/bootloader/latest
%{_firmwaredir}/raspberrypi/bootloader/default

%changelog
