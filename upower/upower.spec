#
# spec file for package upower
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


%{!?_udevrulesdir: %global _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d}
%define systemdutildir %(pkg-config --variable systemdutildir systemd)
%if !0%{?is_opensuse}
%define         _udevdir %(pkg-config --variable=udevdir udev)
BuildRequires:  pkgconfig(udev)
%endif
Name:           upower
Version:        0.99.11
Release:        0
Summary:        Power Device Enumeration Framework
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://upower.freedesktop.org/
#Source0:        https://gitlab.freedesktop.org/upower/upower/uploads/c438511024b9bc5a904f8775cfc8e4c4/%%{name}-%%{version}.tar.xz
Source:         %{name}-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE upower-hibernate-insteadof-hybridsleep.patch boo#985741 dimstar@opensuse.org -- Set the system per default to hibernate, not hybridsleep
Patch0:         upower-hibernate-insteadof-hybridsleep.patch

BuildRequires:  gobject-introspection-devel >= 0.9.9
BuildRequires:  gtk-doc >= 1.11
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.16.1
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.34.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gudev-1.0) >= 147
BuildRequires:  pkgconfig(libimobiledevice-1.0) >= 0.9.7
BuildRequires:  pkgconfig(libplist) >= 0.12
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.0
BuildRequires:  pkgconfig(systemd)
Recommends:     %{name}-lang
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
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-static \
	--libexecdir=%{_libexecdir}/upower \
	--enable-gtk-doc \
	--with-udevrulesdir=%{_udevrulesdir} \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
install -d %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%find_lang %{name}

%pre
%service_add_pre upower.service

%post
%{?udev_rules_update:%udev_rules_update}
%service_add_post upower.service

%preun
%service_del_preun upower.service

%postun
%service_del_postun upower.service

%post -n libupower-glib3 -p /sbin/ldconfig
%postun -n libupower-glib3 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README
%dir %{_sysconfdir}/UPower
%config(noreplace) %{_sysconfdir}/UPower/UPower.conf
%{_bindir}/upower
%{_sbindir}/rc%{name}
%dir %{_libexecdir}/upower
%{_libexecdir}/upower/upowerd
%if !0%{?is_opensuse}
%dir %{_udevdir}
%dir %{_udevrulesdir}
%endif
%{_udevrulesdir}/*.rules
%{_unitdir}/upower.service
%{_datadir}/dbus-1/system.d/org.freedesktop.UPower.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.UPower.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.UPower.Device.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.UPower.KbdBacklight.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.UPower.Wakeups.xml
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
