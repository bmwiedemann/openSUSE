#
# spec file for package kernel-firmware
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

Name:           kernel-firmware-all
Version:        20250206
Release:        0
Summary:        Compatibility metapackage for kernel firmware files
License:        GPL-2.0-only AND SUSE-Firmware AND GPL-2.0-or-later AND MIT
Group:          System/Kernel
URL:            https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
Source0:        README
Conflicts:      kernel < 5.3
Provides:       kernel-firmware = %{version}
Obsoletes:      kernel-firmware <= %{version}
Provides:       compat-wireless-firmware = 4.4
Obsoletes:      compat-wireless-firmware < 4.4
Requires:       kernel-firmware-amdgpu
Requires:       kernel-firmware-ath10k
Requires:       kernel-firmware-ath11k
Requires:       kernel-firmware-ath12k
Requires:       kernel-firmware-atheros
Requires:       kernel-firmware-bluetooth
Requires:       kernel-firmware-bnx2
Requires:       kernel-firmware-brcm
Requires:       kernel-firmware-chelsio
Requires:       kernel-firmware-dpaa2
Requires:       kernel-firmware-i915
Requires:       kernel-firmware-intel
Requires:       kernel-firmware-iwlwifi
Requires:       kernel-firmware-liquidio
Requires:       kernel-firmware-marvell
Requires:       kernel-firmware-media
Requires:       kernel-firmware-mediatek
Requires:       kernel-firmware-mellanox
Requires:       kernel-firmware-mwifiex
Requires:       kernel-firmware-network
Requires:       kernel-firmware-nfp
Requires:       kernel-firmware-nvidia
Requires:       kernel-firmware-platform
Requires:       kernel-firmware-prestera
Requires:       kernel-firmware-qcom
Requires:       kernel-firmware-qlogic
Requires:       kernel-firmware-radeon
Requires:       kernel-firmware-realtek
Requires:       kernel-firmware-serial
Requires:       kernel-firmware-sound
Requires:       kernel-firmware-ti
Requires:       kernel-firmware-ueagle
Requires:       kernel-firmware-usb-network
BuildArch:      noarch

%description
This package is a catch-all compatibility metapackage for providing
all files that have been provided by kernel-firmware package.

%prep
%setup -q -c -T
cp %{SOURCE0} .

%build
# nothing to do

%install

%files
%doc README

%changelog
