#
# spec file for package xf86-input-synaptics
#
# Copyright (c) 2020 SUSE LLC
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


Name:           xf86-input-synaptics
Version:        1.9.1
Release:        0
Summary:        Synaptics touchpad input driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
Source1:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
Patch0:         n_xf86-input-synaptics-wait.diff
Patch2:         n_xf86-input-synaptics-xorg.conf.d_snippet.diff
Patch5:         n_xf86-input-synaptics-default-tap.diff
BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(libevdev) >= 1.0.99.1
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(recordproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi) >= 1.2
BuildRequires:  pkgconfig(xorg-macros) >= 1.13
BuildRequires:  pkgconfig(xorg-server) >= 1.7
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtst)
Requires:       udev
# This was part of the xorg-x11-driver-input package up to version 7.6
Conflicts:      xorg-x11-driver-input <= 7.6
Provides:       x11-input-synaptics = %{version}
Obsoletes:      x11-input-synaptics < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x
%x11_abi_xinput_req

%description
synaptics is an Xorg input driver for touchpads.

Even though touchpads can be handled by the normal evdev or mouse
drivers, this driver allows more advanced features of the touchpad to
become available.

%package devel
Summary:        Synaptics touchpad input driver for the Xorg X server -- Development Files
Group:          Development/Libraries/X11

%description devel
synaptics is an Xorg input driver for touchpads.

Even though touchpads can be handled by the normal evdev or mouse
drivers, this driver allows more advanced features of the touchpad to
become available.

%prep
%setup -q
%patch0 -p1
%patch2 -p1
%patch5 -p1

%build
autoreconf -fiv
%configure \
  --with-xorg-conf-dir=%{_datadir}/X11/xorg.conf.d/
make %{?_smp_mflags} V=1

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
%dir %{_datadir}/X11/xorg.conf.d/
%{_datadir}/X11/xorg.conf.d/70-synaptics.conf
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/input/synaptics_drv.so
%{_bindir}/synclient
%{_bindir}/syndaemon
%{_datadir}/man/man1/synclient.1%{?ext_man}
%{_datadir}/man/man1/syndaemon.1%{?ext_man}
%{_datadir}/man/man4/synaptics.4%{?ext_man}

%files devel
%defattr(-,root,root)
%{_includedir}/xorg/synaptics-properties.h
%{_libdir}/pkgconfig/xorg-synaptics.pc

%changelog
