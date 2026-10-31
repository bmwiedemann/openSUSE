#
# spec file for package hcxdumptool
#
# Copyright (c) 2021-2026, Martin Hauke <mardnh@gmx.de>
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


Name:           hcxdumptool
Version:        8.0.0
Release:        0
Summary:        A tool to capture packets wlan devices
License:        MIT
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/ZerBea/hcxdumptool
#Git-Clone:     https://github.com/ZerBea/hcxdumptool.git
Source:         https://github.com/ZerBea/hcxdumptool/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  openssl-devel >= 3.0
BuildRequires:  pkgconfig(libpcap)

%description
A tool to capture packets from wlan devices and detect weak
point within own WiFi networks - designed to run on Raspberry Pi's.
Capture format pcapng is compatible to Wireshark and tshark.

%prep
%autosetup

%build
%make_build

%install
%make_install PREFIX=%{_prefix}
install -Dm 0644 man/hcxdumptool.1 %{buildroot}%{_mandir}/man1/hcxdumptool.1

%files
%license license.txt
%doc changelog README.md
%{_bindir}/hcxnmealog
%{_bindir}/hcxdumptool
%{_mandir}/man1/hcxdumptool.1%{?ext_man}

%changelog
