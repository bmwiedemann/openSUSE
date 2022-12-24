#
# spec file for package raspberrypi-firmware-config
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


Name:           raspberrypi-firmware-config
Version:        2022.12.12
Release:        0
Summary:        Configuration for the Raspberry Pi firmware loader
License:        MIT
Group:          System/Boot
URL:            https://github.com/raspberrypi/firmware/
Source:         config.txt
BuildRequires:  raspberrypi-firmware
Requires:       raspberrypi-firmware = %{version}
Supplements:    modalias(of:NfirmwareT*Craspberrypi%2Cbcm2835-firmwareC*)
Conflicts:      kernel < 4.12.14
%if "%{name}" == "raspberrypi-firmware-config-camera"
Conflicts:      raspberrypi-firmware-config
Requires:       (raspberrypi-firmware-extra or raspberrypi-firmware-extra-pi4)
%else
Conflicts:      raspberrypi-firmware-config-camera
%endif
Provides:       raspberrypi-firmware-branding-openSUSE = %{version}
Obsoletes:      raspberrypi-firmware-branding-openSUSE < %{version}
Provides:       raspberrypi-firmware-config = %{version}
Provides:       raspberrypi-firmware-config-rpi = %{version}
Obsoletes:      raspberrypi-firmware-config-rpi < %{version}
Provides:       raspberrypi-firmware-config-rpi0w = %{version}
Obsoletes:      raspberrypi-firmware-config-rpi0w < %{version}
Provides:       raspberrypi-firmware-config-rpi2 = %{version}
Obsoletes:      raspberrypi-firmware-config-rpi2 < %{version}
Provides:       raspberrypi-firmware-config-rpi3 = %{version}
Obsoletes:      raspberrypi-firmware-config-rpi3 < %{version}
BuildArch:      noarch

%description
This package configures the Raspberry Pi boot process.
2 flavors are available:
  * raspberrypi-firmware-config - the default config
  * raspberrypi-firmware-config-camera - the config which enables
  start_x=1 and increase gpu_mem to be able to use a camera module

Note: config.txt should not be used to set manually params (gpu_mem, etc.)
please create extraconfig.txt instead.

%prep

%build

%install
install -D -p -m 0644 %{SOURCE0} %{buildroot}/boot/vc/config.txt
%if "%{name}" == "raspberrypi-firmware-config-camera"
sed -i "s/gpu_mem=32/# gpu_mem=32/" %{buildroot}/boot/vc/config.txt
sed -i "s/# start_x=1/start_x=1/" %{buildroot}/boot/vc/config.txt
sed -i "s/# gpu_mem=128/gpu_mem=128/" %{buildroot}/boot/vc/config.txt
%endif

%post
if mountpoint -q /boot/efi && [ ! -L /boot/efi ]; then
  [ -f /boot/efi/config.txt ] && cp /boot/efi/config.txt /boot/efi/config.txt.rpmsave
  cp /boot/vc/config.txt /boot/efi/config.txt
fi

%files
%defattr(-,root,root)
%config /boot/vc/config.txt

%changelog
