#
# spec file for package raspberrypi-rpiboot
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


Name:           raspberrypi-rpiboot
Version:        0~git0.e5e4994
Release:        0
Summary:        Raspberry Pi rpiboot tool
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/raspberrypi/usbboot.git
Source0:        %{name}-%{version}.tar
BuildRequires:  libusb-1_0-devel

%description
The raspberrypi-usbboot allows you to flash the eMMC through an USB cable.

%prep
%setup -q

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
install -c -m 0755 rpiboot %{buildroot}%{_bindir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_bindir}/rpiboot

%changelog
