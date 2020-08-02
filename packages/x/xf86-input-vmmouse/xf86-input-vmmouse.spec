#
# spec file for package xf86-input-vmmouse
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%if 0%( test -d /usr/lib/udev/rules.d && echo "1" ) > 0
%define _udevrulesdir /usr/lib/udev/rules.d
%else
%define _udevrulesdir /lib/udev/rules.d
%endif

Name:           xf86-input-vmmouse
Version:        13.1.0
Release:        0
Summary:        VMware Mouse input driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
Source1:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
Patch2:         u_Don-t-access-hardware-register-while-switched-away.patch
Patch3:         u_conf-rename-to-70-vmmouse.conf.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.0.1
BuildRequires:  pkgconfig(xproto)
Requires:       udev
# no longer install this driver by default with kernel >= 4.1.x (fate #320612)
%if 0%{?suse_version} <= 1320 && !(0%{?suse_version} == 1315 && 0%{?is_opensuse})
Supplements:    xorg-x11-server
%endif
# This was part of the xorg-x11-driver-input package up to version 7.6
Conflicts:      xorg-x11-driver-input <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %ix86 x86_64
%x11_abi_xinput_req

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
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print
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
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_udevrulesdir}/69-xorg-vmmouse.rules
%dir %{_datadir}/X11/xorg.conf.d/
%{_datadir}/X11/xorg.conf.d/70-vmmouse.conf
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/input/vmmouse_drv.so
%{_bindir}/vmmouse_detect
%{_datadir}/man/man1/vmmouse_detect.1%{?ext_man}
%{_datadir}/man/man4/vmmouse.4%{?ext_man}

%changelog
