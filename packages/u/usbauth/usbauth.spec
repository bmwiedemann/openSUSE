#
# spec file for package usbauth
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2017 Stefan Koch <stefan.koch10@gmail.com>
# Copyright (c) 2015 SUSE LLC. All Rights Reserved.
# Author: Stefan Koch <skoch@suse.de>
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


%define _name   usbauth-all
Name:           usbauth
Version:        1.0.3
Release:        0
Summary:        USB firewall against BadUSB attacks
License:        GPL-2.0-only
Group:          Productivity/Security
URL:            https://github.com/kochstefan/usbauth-all/
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
Requires:       systemd
Requires:       udev
BuildRequires:  libtool
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusbauth-configparser)

%{!?_udevrulesdir: %global _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d }

%description
It is a firewall against BadUSB attacks.
A config file describes in which way devices would be accepted.

%prep
%autosetup -n %{_name}-%{version}

%build
cd usbauth
autoreconf -f -i
%configure
%make_build

%install
cd usbauth
%make_install udevrulesdir=%_udevrulesdir

%files
%doc %{name}/README %{name}/CHANGELOG.md
%license %{name}/COPYING
%_sbindir/usbauth
%config %_sysconfdir/dbus-1/system.d/org.opensuse.usbauth.conf
%config(noreplace) %_sysconfdir/usbauth.conf
%_udevrulesdir/20-usbauth.rules
%_mandir/man8/usbauth.8.*

%changelog
