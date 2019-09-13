#
# spec file for package ipcalc
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ipcalc
Version:        0.41
Release:        0
Summary:        IPv4 Address Calculator
License:        GPL-2.0+
Group:          Productivity/Networking/System
Url:            http://jodies.de/ipcalc
Source0:        http://jodies.de/ipcalc-archive/ipcalc-%{version}.tar.gz
Patch1:         http://jodies.de/ipcalc-archive/patch-queue
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
ipcalc takes an IP address and netmask and calculates the resulting
broadcast, network, Cisco wildcard mask, and host range. By giving a
second netmask, you can design subnets and supernets. It is also
presents the subnetting results as easy-to-understand binary values.

Enter your netmask(s) in CIDR notation (/25) or dotted decimals
(255.255.255.0). Inverse netmasks are recognized. If you omit the
netmask ipcalc uses the default netmask for the class of your network.

%prep
%setup -q
%patch1

%build

%install
install -D -m 0755 ipcalc "%{buildroot}%{_bindir}/ipcalc"

%files
%defattr(-,root,root)
%doc license changelog contributors
%{_bindir}/ipcalc

%changelog
