#
# spec file for package pullin-bcm43xx-firmware
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pullin-bcm43xx-firmware
Version:        1.0
Release:        0
Summary:        download broadcom firmware files
License:        MIT
Group:          Hardware/Wifi
Source0:        pullin-bcm43xx-firmware.service
Source1:        install_bcm43xx_firmware_wrapper
BuildRequires:  pciutils
BuildRequires:  systemd
Requires:       b43-fwcutter
Requires:       pciutils
Supplements:    b43-fwcutter
BuildArch:      noarch

%description
automatically download broadcom firmware files needed for bcm43xx WLAN chips

%prep

%build

%install
install -d %{buildroot}%{_prefix}/lib/systemd/system/
install -p -m 644 %{SOURCE0} %{buildroot}%{_prefix}/lib/systemd/system/
install -d %{buildroot}%{_sbindir}/
install -p -m 755 %{SOURCE1} %{buildroot}%{_sbindir}/

%post
if lspci -nn|grep -q -i broadcom ; then
  systemctl enable %{name}.service
  systemctl start %{name}.service
fi

%files
%defattr(-, root, root, 0755)
%{_sbindir}/install_bcm43xx_firmware_wrapper
%{_prefix}/lib/systemd/system/%{name}.service

%changelog
