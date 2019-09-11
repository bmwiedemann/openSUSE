#
# spec file for package usbmuxd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           usbmuxd
Version:        1.1.0
Release:        0
Summary:        A socket daemon to multiplex connections from and to iOS devices
License:        GPL-2.0-only OR GPL-3.0-only
Group:          System/Libraries
Url:            http://cgit.sukimashita.com/usbmuxd.git
Source:         http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  libimobiledevice-devel >= 1.1.6
BuildRequires:  libplist-devel >= 1.11
BuildRequires:  libtool
BuildRequires:  libusb-1_0-devel >= 1.0.3
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
Requires:       libusbmuxd4 >= 1.0.10
%if 0%{?suse_version} >= 1330
Requires(pre):  group(nogroup)
%endif
Requires(pre):  shadow
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{!?_udevrulesdir: %global _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d}
%{?systemd_requires}

%description
This package provides the usbmuxd daemon for software to use through the
libusbmuxd library to talk with iPhone/iPod Touch devices.

Usbmux is an encapsulation protocol (think IP, ATM, PPP) that allows
multiplexing several conversations onto a single pair of wires.

%prep
%setup -q

%build
%configure --with-udevrulesdir=%{_udevrulesdir} --with-systemdsystemunitdir=%{_unitdir}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
getent passwd usbmux >/dev/null || useradd -r -g nogroup -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "%{name} daemon" usbmux
%service_add_pre usbmuxd.service
exit 0

%preun
%service_del_preun usbmuxd.service

%post
%{?udev_rules_update:%{udev_rules_update}}
%service_add_post usbmuxd.service
/sbin/ldconfig

%postun
%service_del_postun usbmuxd.service
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING.GPLv2 COPYING.GPLv3 README
%doc %{_mandir}/man1/usbmuxd.1%{?ext_man}
%{_sbindir}/usbmuxd
%{_sbindir}/rc%{name}
%{_udevrulesdir}/39-usbmuxd.rules
%{_unitdir}/usbmuxd.service

%changelog
