#
# spec file
#
# Copyright (c) 2024 SUSE LLC
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

Name:           kernel-firmware-nvidia-jetson
URL:            https://developer.nvidia.com/embedded/jetson-linux-r363
Version:        36.4.0_20240912212859
Release:        0
Summary:        Firmware files for NVIDIA Jetson Orin (graphics) drivers
License:        SUSE-Firmware
Group:          System/Kernel
Source0:        nvidia-l4t-firmware_36.4.0-20240912212859_arm64.tbz2
BuildRequires:  fdupes
ExclusiveArch:  aarch64

%description
This package includes the needed firmware files for NVIDIA Jetson
Orin (graphics) drivers.

%prep

%build

%install
tar xjf $RPM_SOURCE_DIR/nvidia-l4t-firmware_*_arm64.tbz2 -C $RPM_BUILD_ROOT/
pushd $RPM_BUILD_ROOT/
# etc/systemd/
mkdir -p usr/lib/systemd/system
mv etc/systemd/*.sh  usr/lib/systemd
mv etc/systemd/system/*.service usr/lib/systemd/system
sed -i 's+/etc+/usr/lib+g' usr/lib/systemd/system/nvwifibt.service
rmdir etc/systemd/system
rmdir etc/systemd
rmdir etc
# lib/systemd/system/bluetooth.service/
mv lib/systemd/system/bluetooth.service.d usr/lib/systemd/system
rmdir lib/systemd/system
rmdir lib/systemd
# usr/share/doc
mkdir -p usr/share/doc/packages/kernel-firmware-nvidia-jetson
mv usr/share/doc/{bluez,nvidia-l4t-firmware,nvidia-tegra} usr/share/doc/packages/kernel-firmware-nvidia-jetson
ln -snf service usr/sbin/rcnvwifibt
popd

%fdupes -s %{buildroot}/lib/firmware

%files -n kernel-firmware-nvidia-jetson
%doc /usr/share/doc/packages/kernel-firmware-nvidia-jetson/
/lib/firmware/
/usr/lib/systemd/
/usr/sbin/brcm_patchram_plus
/usr/sbin/rcnvwifibt

%changelog
