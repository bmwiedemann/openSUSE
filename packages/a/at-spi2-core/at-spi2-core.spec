#
# spec file for package at-spi2-core
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


Name:           at-spi2-core
Version:        2.36.1
Release:        0
Summary:        Assistive Technology Service Provider Interface - D-Bus based implementation
License:        LGPL-2.1-or-later
URL:            https://www.gnome.org/
Source0:        https://download.gnome.org/sources/at-spi2-core/2.36/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.40.1
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1) >= 1.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.28
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xtst)
# dbus-daemon is needed to have this work fine
Requires:       dbus-1

%description
AT-SPI is a general interface for applications to make use of the
accessibility toolkit. This version is based on dbus.

This package contains the AT-SPI registry daemon. It provides a
mechanism for all assistive technologies to discover and interact
with applications running on the desktop.

%package -n libatspi0
Summary:        Assistive Technology Service Provider Interface

%description -n libatspi0
AT-SPI is a general interface for applications to make use of the
accessibility toolkit. This version is based on dbus.

%package -n typelib-1_0-Atspi-2_0
Summary:        Introspection bindings for the Assistive Technology Service Provider Interface

%description -n typelib-1_0-Atspi-2_0
AT-SPI is a general interface for applications to make use of the
accessibility toolkit. This version is based on dbus.

This package provides the GObject Introspection bindings for the
libatspi library.

%package devel
Summary:        Development files for the Assistive Technology Service Provider Interface
Requires:       at-spi2-core = %{version}
Requires:       libatspi0 = %{version}
Requires:       typelib-1_0-Atspi-2_0 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	--libexecdir="%{_libexecdir}/at-spi2" \
	-Ddocs=true \
	-Dintrospection=yes \
	-Dx11=yes \
	%{nil}
%meson_build

%install
%meson_install
%find_lang at-spi2-core

%post -n libatspi0 -p /sbin/ldconfig
%postun -n libatspi0 -p /sbin/ldconfig

%files
%license COPYING
%{_libexecdir}/at-spi2/
%{_sysconfdir}/xdg/autostart/at-spi-dbus-bus.desktop
%{_userunitdir}/at-spi-dbus-bus.service
%dir %{_datadir}/dbus-1/accessibility-services/
%{_datadir}/dbus-1/accessibility-services/org.a11y.atspi.Registry.service
%{_datadir}/dbus-1/services/org.a11y.Bus.service
%dir %{_datadir}/defaults
%{_datadir}/defaults/at-spi2/

%files -n libatspi0
%{_libdir}/libatspi.so.0*

%files -n typelib-1_0-Atspi-2_0
%{_libdir}/girepository-1.0/Atspi-2.0.typelib

%files devel
%doc AUTHORS README
%{_includedir}/at-spi-2.0/
%{_libdir}/libatspi.so
%{_libdir}/pkgconfig/atspi-2.pc
%{_datadir}/gir-1.0/*.gir
%doc %{_datadir}/gtk-doc/html/libatspi/

%files lang -f at-spi2-core.lang

%changelog
