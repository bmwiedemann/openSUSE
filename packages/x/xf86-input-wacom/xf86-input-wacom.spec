#
# spec file for package xf86-input-wacom
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


Name:           xf86-input-wacom
Version:        0.39.0
Release:        0
Summary:        Wacom input driver for the Xorg X server
License:        GPL-2.0-or-later
Group:          System/X11/Servers/XF86_4
URL:            https://github.com/linuxwacom/xf86-input-wacom
Source0:        https://github.com/linuxwacom/xf86-input-wacom/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
Patch7:         n_01-Add-option-to-enable-logging.patch
Patch8:         n_02-Log-PROXIMITY-LOW-LEVEL-events.patch
Patch9:         n_03-Log-PRESSURE-low-level-events.patch
Patch10:        n_04-Log-BUTTON-HIGH-LEVEL-events.patch
Patch12:        n_disable-touchscreen.patch
# For directory ownership
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(kbproto)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.7.0
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xrandr)
Requires:       pkgconfig(udev)
Supplements:    xorg-x11-server
# This was part of the xorg-x11-driver-input package up to version 7.6
Conflicts:      xorg-x11-driver-input <= 7.6
Provides:       x11-input-wacom = %{version}
Obsoletes:      x11-input-wacom < %{version}
Provides:       x11-input-wacom-tools = %{version}
Obsoletes:      x11-input-wacom-tools < %{version}
ExcludeArch:    s390 s390x
%{?systemd_ordering}
%{x11_abi_xinput_req}

%description
wacom is an X input driver and utilities for Wacom devices.

%package devel
Summary:        Development files for the Xorg X server Wacom input driver
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}
Provides:       x11-input-wacom-devel = %{version}
Obsoletes:      x11-input-wacom-devel < %{version}

%description devel
wacom is an X input driver and utilities for Wacom devices.

%prep
%setup -q
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch12 -p1

%build
autoreconf -fi
%configure \
    --with-xorg-conf-dir=%{_datadir}/X11/xorg.conf.d/ \
    --enable-logging \
    --with-systemd-unit-dir=%{_unitdir} \
    --with-udev-rules-dir=%{_udevrulesdir} \
    --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
mv %{buildroot}%{_udevrulesdir}/wacom.rules  %{buildroot}%{_udevrulesdir}/65-wacom.rules

%check
make %{?_smp_mflags} check

%pre
%service_add_pre wacom-inputattach@.service

%post
%service_add_post wacom-inputattach@.service
if [ "$1" -eq 1 ]; then
    %udev_rules_update
    %{_bindir}/systemctl daemon-reload >/dev/null 2>&1 || :
fi
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change
exit 0

%preun
%service_del_preun wacom-inputattach@.service

%postun
%service_del_postun wacom-inputattach@.service
if [ "$1" -eq 1 ]; then
    %udev_rules_update
    %{_bindir}/systemctl daemon-reload >/dev/null 2>&1 || :
fi
# re-plug the input devices
udevadm trigger --subsystem-match=input --action=change
exit 0

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog GPL
%{_udevrulesdir}/65-wacom.rules
%{_unitdir}/wacom-inputattach@.service
%dir %{_datadir}/X11/xorg.conf.d/
%{_datadir}/X11/xorg.conf.d/70-wacom.conf
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/input/wacom_drv.so
%{_bindir}/xsetwacom
%{_mandir}/man1/xsetwacom.1%{?ext_man}
%{_mandir}/man4/wacom.4%{?ext_man}
%{_bindir}/isdv4-serial-inputattach

%files devel
%defattr(-,root,root)
%{_includedir}/xorg/Xwacom.h
%{_includedir}/xorg/isdv4.h
%{_includedir}/xorg/wacom-properties.h
%{_includedir}/xorg/wacom-util.h
# not useful for most people
%{_bindir}/isdv4-serial-debugger
%{_libdir}/pkgconfig/xorg-wacom.pc

%changelog
