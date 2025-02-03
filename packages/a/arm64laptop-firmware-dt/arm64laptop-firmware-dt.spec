#
# spec file for package arm64laptop-firmware-dt
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


Name:           arm64laptop-firmware-dt
Version:        2023.10.16
Release:        0
Summary:        Device trees for arm64 laptop firmware
License:        GPL-2.0-only
ExclusiveArch:  aarch64
Group:          System/Boot
URL:            https://www.kernel.org/
%define         instdir /usr/share/%{name}

%description
This package installs device trees required by arm64 laptops which do not
have Linux ACPI support from UEFI-firmware/bootloader.

%prep

%build

%package -n lenovo-x13s-firmware-dt
Summary:        Lenovo X13s DTB installation
Group:          System/Boot
BuildRequires:  dtb-qcom
ExclusiveArch:  aarch64
Supplements:    modalias(of:NscmT*Cqcom,scm-sc8280xpCqcom,scm)

%description -n lenovo-x13s-firmware-dt
Install DTB on ESP for Lenovo X13s.

%install
install -m 755 -d %{buildroot}%{instdir}/lenovo-x13s
install -m 644 /boot/dtb-*/qcom/sc8280xp-lenovo-thinkpad-x13s.dtb %{buildroot}%{instdir}/lenovo-x13s/

%post -n lenovo-x13s-firmware-dt
if mountpoint -q /boot/efi && [ ! -L /boot/efi ]; then
    cp %{instdir}/lenovo-x13s/sc8280xp-lenovo-thinkpad-x13s.dtb /boot/efi/
fi

%postun -n lenovo-x13s-firmware-dt
if mountpoint -q /boot/efi && [ ! -L /boot/efi ]; then
    rm /boot/efi/sc8280xp-lenovo-thinkpad-x13s.dtb
fi

%files -n lenovo-x13s-firmware-dt
%defattr(-,root,root)
%dir %{instdir}
%dir %{instdir}/lenovo-x13s
%{instdir}/lenovo-x13s/*dtb

%changelog
