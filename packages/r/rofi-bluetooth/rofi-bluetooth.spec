#
# spec file for package rofi-bluetooth
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


Name:           rofi-bluetooth
Version:        0+git.1745170630.9f2b944
Release:        0
Summary:        Bluetooth manager for rofi
License:        GPL-3.0-only
URL:            https://github.com/nickclyde/rofi-bluetooth
Source:         %{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       bluez

%description
Bluetooth device and connection manager for use with rofi

%prep
%autosetup -p1

%build
# Nothing to Build

%install
install -Dm 755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
