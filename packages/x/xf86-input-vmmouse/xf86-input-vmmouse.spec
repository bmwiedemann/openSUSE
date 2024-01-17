#
# spec file for package xf86-input-vmmouse
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


%if 0%( test -d %{_prefix}/lib/udev/rules.d && echo "1" ) > 0
%define _udevrulesdir %{_prefix}/lib/udev/rules.d
%else
%define _udevrulesdir /lib/udev/rules.d
%endif
Name:           xf86-input-vmmouse
Version:        13.2.0
Release:        0
Summary:        VMware Mouse input driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            https://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.xz
Source1:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Patch2:         u_Don-t-access-hardware-register-while-switched-away.patch
Patch3:         u_conf-rename-to-70-vmmouse.conf.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.0.1
BuildRequires:  pkgconfig(xproto)
Requires:       udev
# This was part of the xorg-x11-driver-input package up to version 7.6
Conflicts:      xorg-x11-driver-input <= 7.6
ExclusiveArch:  %{ix86} x86_64
%{x11_abi_xinput_req}
# no longer install this driver by default with kernel >= 4.1.x (fate #320612)
%if 0%{?suse_version} <= 1320 && !(0%{?suse_version} == 1315 && 0%{?is_opensuse})
Supplements:    xorg-x11-server
%endif

%description
vmmouse is an Xorg input driver for mice. The driver supports most
available mouse types and interfaces. USB mice are only supported on
some OSs, and the level of support for PS/2 mice depends on the OS.

%prep
%setup -q
%patch2 -p1
%patch3 -p1

%build
autoreconf -fi
%configure --with-xorg-conf-dir=%{_datadir}/X11/xorg.conf.d/ --with-udev-rules-dir=%{_udevrulesdir}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Drop hal support
rm %{buildroot}%{_datadir}/hal/fdi/policy/20thirdparty/11-x11-vmmouse.fdi
rm %{buildroot}%{_libdir}/hal/hal-probe-vmmouse

%post
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change || :
exit 0

%postun
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change || :
exit 0

%files
%license COPYING
%doc ChangeLog README
%{_udevrulesdir}/69-xorg-vmmouse.rules
%dir %{_datadir}/X11/xorg.conf.d/
%{_datadir}/X11/xorg.conf.d/70-vmmouse.conf
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/input/vmmouse_drv.so
%{_bindir}/vmmouse_detect
%{_mandir}/man1/vmmouse_detect.1%{?ext_man}
%{_mandir}/man4/vmmouse.4%{?ext_man}

%changelog
