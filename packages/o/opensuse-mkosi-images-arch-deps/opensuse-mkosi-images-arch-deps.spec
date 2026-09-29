#
# spec file for package patterns-images
#
# Copyright (c) 2025 SUSE LLC
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


Name:           opensuse-mkosi-images-arch-deps
Version:        1.0
Release:        0
Summary:        Architecture specific RPMs for mkosi images in OBS
License:        MIT
Source:         LICENSE
ExclusiveArch:  x86_64 aarch64
%ifarch aarch64
Requires:       raspberrypi-eeprom
Requires:       raspberrypi-firmware
Requires:       raspberrypi-firmware-config
Requires:       raspberrypi-firmware-dt
Requires:       u-boot-rpiarm64
%endif

%description
This RPM requires architecture specific packages for building
openSUSE images with mkosi in OBS.

%prep
cp %{SOURCE0} .

%build
# empty on purpose

%install

%files
%license LICENSE

%changelog
