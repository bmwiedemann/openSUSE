#
# spec file for package xf86-input-keyboard
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


Name:           xf86-input-keyboard
Version:        1.9.0
Release:        0
Summary:        Keyboard input driver for the Xorg X server
License:        GPL-2.0-or-later
Group:          System/X11/Servers/XF86_4
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.4
BuildRequires:  pkgconfig(xproto)
Requires:       udev
Requires:       xkeyboard-config >= 1.5
Supplements:    xorg-x11-server
# This was part of the xorg-x11-driver-input package up to version 7.6
Conflicts:      xorg-x11-driver-input <= 7.6
ExcludeArch:    s390 s390x
%{x11_abi_xinput_req}

%description
kbd is an Xorg input driver for keyboards. The driver supports the
standard OS-provided keyboard interface, but these are currently only
available to this driver module for Linux, BSD, and Solaris.

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
%doc README
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/input/kbd_drv.so
%{_mandir}/man4/kbd.4%{?ext_man}

%changelog
