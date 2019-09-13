#
# spec file for package xf86-input-evdev
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


Name:           xf86-input-evdev
Version:        2.10.6
Release:        0
Summary:        Generic Linux input driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
Source1:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
Source3:        11-evdev.conf
Source4:        50-elotouch.conf
Patch1:         u_01-Add-a-kiosk-mode-for-touch-screens.patch
Patch2:         u_02-Add-delay-between-button-press-and-release-to-kiosk-mode.patch

# Next three lines are needed for u_01-Add-a-kiosk-mode-for-touch-screens.patch
BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(libevdev) >= 0.4
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(xproto)
Requires:       udev
Provides:       x11-input-mtrack
Obsoletes:      x11-input-mtrack
Supplements:    xorg-x11-server
# This was part of the xorg-x11-driver-input package up to version 7.6
Conflicts:      xorg-x11-driver-input <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x
%x11_abi_xinput_req

%description
evdev is an Xorg input driver for Linux's generic event devices. It
therefore supports all input devices that the kernel knows about,
including most mice, keyboards, tablets and touchscreens.

%package devel
Summary:        Generic Linux input driver for the Xorg X server -- Development Files
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}

%description devel
evdev is an Xorg input driver for Linux's generic event devices. It
therefore supports all input devices that the kernel knows about,
including most mice, keyboards, tablets and touchscreens.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
# Once u_01-Add-a-kiosk-mode-for-touch-screens.patch is removed this is no longer needed
%{_bindir}/autoreconf -v --install --force
%configure
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print
install -D -m 644 %{SOURCE3} %{SOURCE4} %{buildroot}/%{_datadir}/X11/xorg.conf.d/

%post
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change || :

%postun
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change || :

%files
%defattr(-,root,root)
%doc COPYING README
%dir %{_datadir}/X11/xorg.conf.d
%{_datadir}/X11/xorg.conf.d/*.conf
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/input/evdev_drv.so
%{_mandir}/man4/evdev.4%{?ext_man}

%files devel
%defattr(-,root,root)
%{_includedir}/xorg/evdev-properties.h
%{_libdir}/pkgconfig/xorg-evdev.pc

%changelog
