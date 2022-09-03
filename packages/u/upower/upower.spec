#
# spec file for package upower
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


%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
%define libplist2 1
%else
%define libplist2 0
%endif

Name:           upower
Version:        1.90.0
Release:        0
Summary:        Power Device Enumeration Framework
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://upower.freedesktop.org/
Source:         https://gitlab.freedesktop.org/upower/upower/-/archive/v%{version}/upower-v%{version}.tar.bz2
BuildRequires:  gobject-introspection-devel >= 0.9.9
BuildRequires:  gtk-doc >= 1.11
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.16.1
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.34.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gudev-1.0) >= 235
BuildRequires:  pkgconfig(libimobiledevice-1.0) >= 0.9.7
%if %libplist2
BuildRequires:  pkgconfig(libplist-2.0)
%else
BuildRequires:  pkgconfig(libplist) >= 0.12
%endif
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.0
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
%{?systemd_requires}

%description
UPower is an abstraction for enumerating power devices, listening to
device events and querying history and statistics. Any application or
service on the system can access the org.freedesktop.UPower service
via the system message bus. Some operations (such as suspending the
system) are restricted using PolicyKit.

%package -n libupower-glib3
Summary:        Power Device Enumeration Framework - Library
Group:          System/Daemons
Recommends:     %{name}

%description -n libupower-glib3
UPower is an abstraction for enumerating power devices, listening to
device events and querying history and statistics. Any application or
service on the system can access the org.freedesktop.UPower service
via the system message bus. Some operations (such as suspending the
system) are restricted using PolicyKit.

%package -n typelib-1_0-UpowerGlib-1_0
Summary:        Power Device Enumeration Framework - Introspection bindings
Group:          System/Daemons

%description -n typelib-1_0-UpowerGlib-1_0
UPower is an abstraction for enumerating power devices, listening to
device events and querying history and statistics. Any application or
service on the system can access the org.freedesktop.UPower service
via the system message bus. Some operations (such as suspending the
system) are restricted using PolicyKit.

This package provides the GObject Introspection bindings for
libupower-glib.

%package -n libupower-glib-devel
Summary:        Power Device Enumeration Framework - Development Files
Group:          Development/Libraries/Other
Requires:       libupower-glib3 = %{version}
Requires:       typelib-1_0-UpowerGlib-1_0 = %{version}
Provides:       %{name}-devel = %{version}

%description -n libupower-glib-devel
UPower is an abstraction for enumerating power devices, listening to
device events and querying history and statistics. Any application or
service on the system can access the org.freedesktop.UPower service
via the system message bus. Some operations (such as suspending the
system) are restricted using PolicyKit.

%lang_package

%prep
%setup -q -n %{name}-v%{version}

%build
%meson \
	--libexecdir=%{_libexecdir}/upower \
	%{nil}
%meson_build

%install
%meson_install

install -d %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%find_lang %{name}

%pre
%service_add_pre upower.service

%post
%{?udev_rules_update:%udev_rules_update}
%service_add_post upower.service
%udev_hwdb_update

%preun
%service_del_preun upower.service

%postun
%service_del_postun upower.service
%udev_hwdb_update

%ldconfig_scriptlets -n libupower-glib3

%files
%license COPYING
%doc AUTHORS NEWS README
%dir %{_sysconfdir}/UPower
%config(noreplace) %{_sysconfdir}/UPower/UPower.conf
%{_bindir}/upower
%{_sbindir}/rc%{name}
%dir %{_libexecdir}/upower
%{_libexecdir}/upower/upowerd
%{_udevrulesdir}/*.rules
%{_udevhwdbdir}/*.hwdb
%{_unitdir}/upower.service
%{_datadir}/dbus-1/system.d/org.freedesktop.UPower.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.UPower.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.UPower.Device.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.UPower.KbdBacklight.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.UPower.service
%{_mandir}/man1/upower.1%{?ext_man}
%{_mandir}/man7/UPower.7%{?ext_man}
%{_mandir}/man8/upowerd.8%{?ext_man}
%dir %{_localstatedir}/lib/upower

%files -n libupower-glib3
%{_libdir}/libupower-glib.so.*

%files -n typelib-1_0-UpowerGlib-1_0
%{_libdir}/girepository-1.0/UPowerGlib-1.0.typelib

%files -n libupower-glib-devel
%doc %{_datadir}/gtk-doc/html/UPower/
%{_includedir}/libupower-glib/
%{_libdir}/pkgconfig/upower-glib.pc
%{_libdir}/libupower-glib.so
%{_datadir}/gir-1.0/UPowerGlib-1.0.gir

%files lang -f %{name}.lang

%changelog
