#
# spec file for package linuxconsoletools
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


Name:           linuxconsoletools
Version:        1.8.1
Release:        0
Summary:        A set of utilities for joysticks
License:        GPL-2.0-or-later
Group:          Hardware/Joystick
URL:            http://sourceforge.net/projects/linuxconsole/
Source0:        http://sourceforge.net/projects/linuxconsole/files/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE 0001-fix-bashisms.patch
Patch0:         0001-fix-bashisms.patch
BuildRequires:  libSDL2-devel
BuildRequires:  linux-kernel-headers
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(udev)
# moved in 13.2
Provides:       input-utils = 2007.06.22
Obsoletes:      input-utils < 2007.06.22

%description
This package contains the following utilities and associated
documentation:
* joystick utilities - calibrate and test joysticks and joypads

The following utilities are provided to calibrate and test joysticks:
* evdev-joystick - test & calibrate joysticks using evdev devices
* ffcfstress, ffmvforce, fftest - test force-feedback devices
* ffset - set force-feedback device parameters
* jscal - calibrate joystick devices, reconfigure the axes and buttons
* jscal-store, jscal-restore - store and retrieve joystick device settings as configured using jscal
* jstest - test joystick devices

%prep
%autosetup -p1

%build
make %{?_smp_mflags} \
    CFLAGS="%{optflags}" \
    PREFIX=%{_prefix} \
    SYSTEMD_SUPPORT=1

%install
make %{?_smp_mflags} \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    install
# fix permissions
chmod 644 %{buildroot}%{_mandir}/man1/*
# Fix udev dirs
mkdir -p %{buildroot}%{_prefix}/lib/udev
mv %{buildroot}/lib/udev/js-set-enum-leds %{buildroot}%{_prefix}/lib/udev/js-set-enum-leds
mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}/lib/udev/rules.d/80-stelladaptor-joystick.rules %{buildroot}%{_udevrulesdir}/80-stelladaptor-joystick.rules
rm %{buildroot}/%{_bindir}/inputattach \
   %{buildroot}/%{_mandir}/man1/inputattach.1

%files
%license COPYING
%doc NEWS README
%{_bindir}/evdev-joystick
%{_bindir}/ffcfstress
%{_bindir}/ffmvforce
%{_bindir}/ffset
%{_bindir}/fftest
%{_bindir}/jscal
%{_bindir}/jscal-restore
%{_bindir}/jscal-store
%{_bindir}/jstest
%{_mandir}/man1/ffcfstress.1%{ext_man}
%{_mandir}/man1/ffmvforce.1%{ext_man}
%{_mandir}/man1/ffset.1%{ext_man}
%{_mandir}/man1/fftest.1%{ext_man}
%{_mandir}/man1/jscal-restore.1%{ext_man}
%{_mandir}/man1/jscal-store.1%{ext_man}
%{_mandir}/man1/jscal.1%{ext_man}
%{_mandir}/man1/jstest.1%{ext_man}
%{_mandir}/man1/evdev-joystick.1%{ext_man}
%{_datadir}/joystick/
%{_prefix}/lib/udev/js-set-enum-leds
%{_udevrulesdir}/80-stelladaptor-joystick.rules

%changelog
