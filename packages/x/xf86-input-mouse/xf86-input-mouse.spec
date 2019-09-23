#
# spec file for package xf86-input-mouse
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xf86-input-mouse
Version:        1.9.3
Release:        0
Summary:        Mouse input driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2

BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.5.99.901
BuildRequires:  pkgconfig(xproto)
Requires:       udev
Supplements:    xorg-x11-server
# This was part of the xorg-x11-driver-input package up to version 7.6
Conflicts:      xorg-x11-driver-input <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x
%x11_abi_xinput_req

%description
mouse is an Xorg input driver for mice. The driver supports most
available mouse types and interfaces, though the level of support for
types of mice depends on the OS.

%package devel
Summary:        Development files for the Mouse input driver
Group:          Development/Libraries/X11
Requires:       %name >= %version

%description devel
Development files for the Mouse input driver for the Xorg X server.

%prep
%setup -q

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%post
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change || :

%postun
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change || :

%files
%defattr(-,root,root)
%doc COPYING README
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/input/mouse_drv.so
%{_datadir}/man/man4/mousedrv.4%{?ext_man}

%files devel
%defattr(-,root,root)
%{_includedir}/xorg/xf86*.h
%{_libdir}/pkgconfig/*.pc

%changelog
