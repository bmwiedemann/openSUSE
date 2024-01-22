#
# spec file for package rofi-network-manager
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


Name:		    rofi-network-manager
Version:    0.0.0.git~19a3780
Release:    0
Summary:	  A Network Manager for Tiling Window Managers
License:    MIT
URL:        http://github.com/P3rf/rofi-network-manager
Source:     %{name}-%{version}.tar.xz
Patch0:		  0001-Modified-for-System-wide-configuration.patch
BuildArch:	noarch
Requires:	  NetworkManager
Requires:	  NetworkManager-connection-editor
Requires:	  qrencode

%description
A Network manager for Tiling Window Managers [i3/bspwm/awesome/etc] or not. Inspired from rofi-wifi-menu.

%prep
%autosetup -p1

%build
# Nothing to Build

%install
install -Dm 755 rofi-network-manager.sh %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_distconfdir}/rofi
install -Dm 644 rofi-network-manager.conf %{buildroot}%{_distconfdir}/rofi/%{name}.conf
install -Dm 644 rofi-network-manager.rasi %{buildroot}%{_distconfdir}/rofi/%{name}.rasi

%files
%license LICENSE
%doc readme.md desktop.png options.png
%dir %{_distconfdir}/rofi
%{_bindir}/%{name}
%{_distconfdir}/rofi/%{name}.rasi
%{_distconfdir}/rofi/%{name}.conf

%changelog

