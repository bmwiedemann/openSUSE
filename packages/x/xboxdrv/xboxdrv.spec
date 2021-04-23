#
# spec file for package xboxdrv
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


Name:           xboxdrv
Version:        0.8.8
Release:        0
Summary:        Xbox/Xbox360 USB Gamepad Driver for Userspace
License:        GPL-3.0-or-later
Group:          Hardware/Joystick
URL:            https://xboxdrv.gitlab.io/
Source:         https://xboxdrv.gitlab.io/%{name}-linux-%{version}.tar.bz2
Source1:        50-xpad.conf
Source2:        %{name}.conf
Source3:        %{name}.service
# PATCH-FIX-UPSTREAM xboxdrv-fix-delay.patch -- Fix 60 seconds delay, from https://github.com/xboxdrv/xboxdrv/pull/214
Patch0:         %{name}-fix-delay.patch
# PATCH-FIX-UPSTREAM xboxdrv-scons3.patch -- Fix build with python, from https://github.com/xboxdrv/xboxdrv/pull/240
Patch1:         xboxdrv-scons3.patch
#PATCH-FIX-OPENSUSE xboxdrv-add-new-device.patch malcolmlewis@opensuse.org -- Add new wireless controller device (0x02a9, "Microsoft X-Box pad v? (?)).
Patch2:         xboxdrv-add-new-device.patch
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  pkgconfig
BuildRequires:  scons
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(x11)

%description
Xboxdrv is a Xbox/Xbox360 gamepad driver for Linux that works in
userspace. It is an alternative to the xpad kernel driver and has
support for Xbox1 gamepads, Xbox360 USB gamepads and Xbox360
wireless gamepads. The Xbox360 guitar and some Xbox1 dancemats
might work too. The Xbox 360 racing wheel is not supported, but
shouldn't be to hard to add if somebody is interested.

%prep
%setup -q -n %{name}-linux-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

cp -f %{SOURCE1} 50-xpad.conf
cp -f %{SOURCE2} %{name}.conf
cp -f %{SOURCE3} %{name}.service

tee custom.py << EOF
CCFLAGS = "%{optflags}"
EOF

%build
scons %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}

chmod a-x %{buildroot}%{_mandir}/man1/%{name}.1

install -Dpm 0644 50-xpad.conf \
  %{buildroot}%{_sysconfdir}/modprobe.d/50-xpad.conf

install -Dpm 0644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf
install -Dpm 0644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service

mkdir -p %{buildroot}%{_sbindir}/
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

#Drop python2 xboxdrvctl and just use systemd service or xboxdrv binary
rm %{buildroot}%{_bindir}/%{name}ctl

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc AUTHORS NEWS PROTOCOL README.md TODO
%config(noreplace) %{_sysconfdir}/%{name}.conf
%dir %{_sysconfdir}/modprobe.d/
%config %{_sysconfdir}/modprobe.d/50-xpad.conf
%{_bindir}/%{name}
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
