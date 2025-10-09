# spec file for package steamdeck-firmware
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

%global _firmwarepath   /usr/lib/firmware

Name:           steamdeck-firmware
Version:        20250731.1
Release:        0
Summary:        Steam Deck OLED firmware for wifi and bluetooth
License:        SUSE-NonFree
URL:            https://gitlab.com/evlaV/linux-firmware-neptune
Group:          System Environment/Base
Source0:        linux-firmware-neptune-%{version}.tar.xz
Source99:       steamdeck-firmware.rpmlintrc
ExclusiveArch:  x86_64
BuildRequires:  filesystem
Requires:       steamdeck-dsp
Requires:       galileo-mura
Provides:       linux-firmware-neptune = %{version}

%description
This package contains the Steam Deck OLED firmware
for wifi and bluetooth.

%prep
%autosetup -n linux-firmware-neptune-%{version}

%build

%install

# Create necessary directories in buildroot
install -d %{buildroot}%{_firmwarepath}/ath11k/QCA2066/hw2.1/
install -m 0644 ath11k/QCA2066/hw2.1/amss.bin %{buildroot}%{_firmwarepath}/ath11k/QCA2066/hw2.1/amss.bin
install -m 0644 ath11k/QCA2066/hw2.1/board-2.bin %{buildroot}%{_firmwarepath}/ath11k/QCA2066/hw2.1/board-2.bin
install -m 0644 ath11k/QCA2066/hw2.1/m3.bin %{buildroot}%{_firmwarepath}/ath11k/QCA2066/hw2.1/m3.bin
install -m 0644 ath11k/QCA2066/hw2.1/Notice.txt %{buildroot}%{_firmwarepath}/ath11k/QCA2066/hw2.1/Notice.txt

install -d %{buildroot}%{_firmwarepath}/qca/
install -m 0644 qca/hpbtfw21.tlv %{buildroot}%{_firmwarepath}/qca/hpbtfw21.tlv
install -m 0644 qca/hpnv21.309 %{buildroot}%{_firmwarepath}/qca/hpnv21.309
install -m 0644 qca/hpnv21.bin %{buildroot}%{_firmwarepath}/qca/hpnv21.bin
install -m 0644 qca/hpnv21g.309 %{buildroot}%{_firmwarepath}/qca/hpnv21g.309
install -m 0644 qca/hpnv21g.bin %{buildroot}%{_firmwarepath}/qca/hpnv21g.bin

%files
%dir %{_firmwarepath}/qca
%{_firmwarepath}/qca/hpbtfw21.tlv
%{_firmwarepath}/qca/hpnv21.309
%{_firmwarepath}/qca/hpnv21.bin
%{_firmwarepath}/qca/hpnv21g.309
%{_firmwarepath}/qca/hpnv21g.bin
%dir %{_firmwarepath}/ath11k
%dir %{_firmwarepath}/ath11k/QCA2066
%dir %{_firmwarepath}/ath11k/QCA2066/hw2.1
%{_firmwarepath}/ath11k/QCA2066/hw2.1/amss.bin
%{_firmwarepath}/ath11k/QCA2066/hw2.1/board-2.bin
%{_firmwarepath}/ath11k/QCA2066/hw2.1/m3.bin
%{_firmwarepath}/ath11k/QCA2066/hw2.1/Notice.txt


%changelog
