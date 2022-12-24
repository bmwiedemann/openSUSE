#
# spec file for package dfu-util
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


Name:           dfu-util
Version:        0.11
Release:        0
Summary:        DFU firmware upgrade utility
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            http://dfu-util.sourceforge.net
Source:         http://dfu-util.sourceforge.net/releases/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.0

%description
This is a host side implementation of the DFU 1.0 and DFU 1.1 specifications of
the USB forum. DFU is intended to download and upload firmware to/from devices
connected over USB. It ranges from small devices like micro-controller boards
to mobile phones.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
install -m 755 dfuse-pack.py %{buildroot}/%{_bindir}/dfuse-pack
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|g' %{buildroot}/%{_bindir}/dfuse-pack

%files
%license COPYING
%doc AUTHORS ChangeLog DEVICES.txt README
%{_bindir}/dfu-*
%{_bindir}/dfuse-pack
%{_mandir}/man1/dfu-util.1%{?ext_man}
%{_mandir}/man1/dfu-prefix.1%{?ext_man}
%{_mandir}/man1/dfu-suffix.1%{?ext_man}

%changelog
