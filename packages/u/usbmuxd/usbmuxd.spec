#
# spec file for package usbmuxd
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


%{!?_udevrulesdir: %global _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d}
Name:           usbmuxd
Version:        1.1.1+git48.01c94c7
Release:        0
Summary:        A socket daemon to multiplex connections from and to iOS devices
License:        GPL-2.0-only OR GPL-3.0-only
Group:          System/Libraries
URL:            https://github.com/libimobiledevice/usbmuxd
Source:         %{name}-%{version}.tar.gz
Source1:        %{name}.sysusers
Source99:       baselibs.conf
Patch2:         usbmuxd-run-dir.patch
Patch3:         harden_usbmuxd.service.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(libimobiledevice-1.0) >= 1.3.0
BuildRequires:  pkgconfig(libplist-2.0) >= 2.3.0
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.9
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
Requires(pre):  group(nogroup)
%sysusers_requires
%{?systemd_requires}

%description
This package provides the usbmuxd daemon for software to use through the
libusbmuxd library to talk with iPhone/iPod Touch devices.

Usbmux is an encapsulation protocol (think IP, ATM, PPP) that allows
multiplexing several conversations onto a single pair of wires.

%prep
%autosetup -p1

%build
%sysusers_generate_pre %{SOURCE1} %{name} %{name}.conf
autoreconf -fiv
%configure \
  --with-udevrulesdir=%{_udevrulesdir} \
  --with-systemdsystemunitdir=%{_unitdir} \
  PACKAGE_VERSION=%{version}
%make_build

%install
%make_install
%if 0%{?suse_version} < 1600
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%endif
install -Dm0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

%pre -f %{name}.pre
%service_add_pre usbmuxd.service

%preun
%service_del_preun usbmuxd.service

%post
%{?udev_rules_update:%udev_rules_update}
%service_add_post usbmuxd.service

%postun
%service_del_postun usbmuxd.service

%files
%license COPYING.GPLv2 COPYING.GPLv3
%doc AUTHORS README.md
%{_sbindir}/usbmuxd
%if 0%{?suse_version} < 1600
%{_sbindir}/rc%{name}
%endif
%{_mandir}/man8/usbmuxd.8%{?ext_man}
%{_udevrulesdir}/39-usbmuxd.rules
%{_unitdir}/usbmuxd.service
%{_sysusersdir}/%{name}.conf

%changelog
