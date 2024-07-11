#
# spec file for package xf86-input-joystick
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


Name:           xf86-input-joystick
Version:        1.6.4
Release:        0
Summary:        Joystick input driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.9.99.2
BuildRequires:  pkgconfig(xproto)
Requires:       udev
Supplements:    xorg-x11-server
# This was part of the xorg-x11-driver-input package up to version 7.6
Conflicts:      xorg-x11-driver-input <= 7.6
ExcludeArch:    s390 s390x
%{x11_abi_xinput_req}

%description
joystick is an Xorg input driver for Joysticks. The driver reports
cursor movement as well as raw axis values through valuators.

%package devel
Summary:        Joystick input driver for the Xorg X server -- Development Files
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}

%description devel
joystick is an Xorg input driver for Joysticks. The driver reports
cursor movement as well as raw axis values through valuators.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change || :

%postun
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change || :

%files
%license COPYING
%doc ChangeLog README.md
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/input/joystick_drv.so
%{_mandir}/man4/joystick.4%{?ext_man}

%files devel
%{_includedir}/xorg/joystick-properties.h
%{_libdir}/pkgconfig/xorg-joystick.pc

%changelog
