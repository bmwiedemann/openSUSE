#
# spec file for package at-spi2-core
#
# Copyright (c) 2023 SUSE LLC
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
Version:        2.48.0
Release:        0
Summary:        Assistive Technology Service Provider Interface - D-Bus based implementation
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://www.gnome.org/
Source0:        https://download.gnome.org/sources/at-spi2-core/2.48/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  fdupes
BuildRequires:  meson >= 0.63.0
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  pkgconfig(dbus-1) >= 1.5
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= 2.28.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.62.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xtst)
# dbus-daemon is needed to have this work fine
Requires:       dbus-1
Provides:       at-spi2-atk-gtk2 = %{version}
Obsoletes:      at-spi2-atk-gtk2 < %{version}
# xprop is needed when using XWayland
Requires:       (xprop if xwayland)

%description
AT-SPI is a general interface for applications to make use of the
accessibility toolkit. This version is based on dbus.

This package contains the AT-SPI registry daemon. It provides a
mechanism for all assistive technologies to discover and interact
with applications running on the desktop.

%package -n libatspi0
Summary:        Assistive Technology Service Provider Interface
Group:          System/Libraries

%description -n libatspi0
AT-SPI is a general interface for applications to make use of the
accessibility toolkit. This version is based on dbus.

%package -n typelib-1_0-Atspi-2_0
Summary:        Introspection bindings for the Assistive Technology Service Provider Interface
Group:          System/Libraries

%description -n typelib-1_0-Atspi-2_0
AT-SPI is a general interface for applications to make use of the
accessibility toolkit. This version is based on dbus.

This package provides the GObject Introspection bindings for the
libatspi library.

%package devel
Summary:        Development files for the Assistive Technology Service Provider Interface
Group:          Development/Libraries/GNOME
Requires:       at-spi2-core = %{version}
Requires:       libatk-1_0-0 = %{version}
Requires:       libatk-bridge-2_0-0 = %{version}
Requires:       libatspi0 = %{version}
Requires:       typelib-1_0-Atk-1_0 = %{version}
Requires:       typelib-1_0-Atspi-2_0 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package -n libatk-1_0-0
Summary:        An Accessibility Toolkit
Group:          System/Libraries
Provides:       atk = %{version}
Obsoletes:      atk < %{version}

%description -n libatk-1_0-0
The ATK library provides a set of accessibility interfaces. By
supporting the ATK interfaces, an application or toolkit can be used
with screen readers, magnifiers, and alternate input devices.

%package -n typelib-1_0-Atk-1_0
Summary:        Introspection bindings for the ATK accessibility toolkit
Group:          System/Libraries

%description -n typelib-1_0-Atk-1_0
The ATK library provides a set of accessibility interfaces. By
supporting the ATK interfaces, an application or toolkit can be used
with screen readers, magnifiers, and alternate input devices.

This package provides the GObject Introspection bindings for ATK.

%package -n libatk-bridge-2_0-0
Summary:        ATK/D-Bus bridging library
Group:          System/Libraries

%description -n libatk-bridge-2_0-0
AT-SPI is a general interface for applications to make use of the
accessibility toolkit. This version is based on dbus.

The package contains a ATK/D-Bus bridge library.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	--libexecdir="%{_libexecdir}/at-spi2" \
	-Ddbus_broker=/usr/bin/dbus-broker-launch \
	-Ddefault_bus=dbus-broker \
	-Ddocs=true \
	-Dintrospection=enabled \
	-Dx11=enabled \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}/gtk-doc/html/
# Move autostart file to /usr/etc
mkdir -p %{buildroot}%{_distconfdir}/xdg/autostart
mkdir -p %{buildroot}%{_distconfdir}/xdg/Xwayland-session.d
mv %{buildroot}%{_sysconfdir}/xdg/autostart/* %{buildroot}%{_distconfdir}/xdg/autostart/
mv %{buildroot}%{_sysconfdir}/xdg/Xwayland-session.d/* %{buildroot}%{_distconfdir}/xdg/Xwayland-session.d/

%ldconfig_scriptlets -n libatspi0
%ldconfig_scriptlets -n libatk-1_0-0
%ldconfig_scriptlets -n libatk-bridge-2_0-0

%files
%license COPYING
%{_libexecdir}/at-spi2/
%dir %{_distconfdir}/xdg/Xwayland-session.d
%{_distconfdir}/xdg/Xwayland-session.d/00-at-spi
%{_distconfdir}/xdg/autostart/at-spi-dbus-bus.desktop
%{_userunitdir}/at-spi-dbus-bus.service
%dir %{_datadir}/dbus-1/accessibility-services/
%{_datadir}/dbus-1/accessibility-services/org.a11y.atspi.Registry.service
%{_datadir}/dbus-1/services/org.a11y.Bus.service
%dir %{_datadir}/defaults
%{_datadir}/defaults/at-spi2/
%dir %{_libdir}/gnome-settings-daemon-3.0
%dir %{_libdir}/gnome-settings-daemon-3.0/gtk-modules
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop
%dir %{_libdir}/gtk-2.0
%dir %{_libdir}/gtk-2.0/modules
%{_libdir}/gtk-2.0/modules/libatk-bridge.so

%files -n libatspi0
%{_libdir}/libatspi.so.0*

%files -n libatk-1_0-0
%{_libdir}/libatk-1.0.so.0*

%files -n libatk-bridge-2_0-0
%{_libdir}/libatk-bridge-2.0.so.0*

%files -n typelib-1_0-Atspi-2_0
%{_libdir}/girepository-1.0/Atspi-2.0.typelib

%files -n typelib-1_0-Atk-1_0
%{_libdir}/girepository-1.0/Atk-1.0.typelib

%files devel
%doc NEWS README.md
%{_includedir}/at-spi-2.0/
%{_includedir}/at-spi2-atk/
%{_includedir}/atk-1.0/
%{_libdir}/libatspi.so
%{_libdir}/libatk-1.0.so
%{_libdir}/libatk-bridge-2.0.so
%{_libdir}/pkgconfig/atspi-2.pc
%{_libdir}/pkgconfig/atk-bridge-2.0.pc
%{_libdir}/pkgconfig/atk.pc
%{_datadir}/gir-1.0/*.gir
%doc %{_datadir}/doc/atk/
%doc %{_datadir}/doc/libatspi/

%files lang -f at-spi2-core.lang

%changelog
