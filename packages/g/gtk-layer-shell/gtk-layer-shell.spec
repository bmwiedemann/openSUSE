#
# spec file for package gtk-layer-shell
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


Name:           gtk-layer-shell
Version:        0.4.0
Release:        0
Summary:        Library to create desktop components for Wayland
License:        MIT AND LGPL-3.0-or-later AND GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/wmww/gtk-layer-shell
Source:         %{url}/archive/v%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  meson >= 0.45.1
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-broadway-3.0)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-broadway-3.0)
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)

%description
A library to create panels and other desktop components for Wayland using the Layer Shell protocol.

%package -n gtk-layer-shell-devel
Summary:        Development files for gtk-layer-shell
Group:          Development/Libraries/C and C++
Requires:       libgtk-layer-shell0 = %{version}
Requires:       typelib-1_0-GtkLayerShell-0_1 = %{version}

%description -n gtk-layer-shell-devel
Development files and headers for gtk-layer-shell

%package -n libgtk-layer-shell0
Summary:        Library to create desktop components for Wayland
Group:          System/Libraries

%description -n libgtk-layer-shell0
A library to create panels and other desktop components for Wayland using the Layer Shell protocol

%package -n      typelib-1_0-GtkLayerShell-0_1
Summary:        Library to create desktop components for Wayland
Group:          System/Libraries

%description -n  typelib-1_0-GtkLayerShell-0_1
This library is a companion library to GObject and Gtk+.
It provides various features that are wished in the underlying
library but are not for various reasons. In most cases, they are
wildly out of scope for those libraries. In other cases, the design
isn't quite generic enough to work for everyone..

This package provides the GObject Introspection bindings for gtk-layer-shell.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%post -n libgtk-layer-shell0 -p /sbin/ldconfig
%postun -n libgtk-layer-shell0 -p /sbin/ldconfig

%files -n libgtk-layer-shell0
%license LICENSE_MIT.txt LICENSE_LGPL.txt
%doc README.md
%{_libdir}/libgtk-layer-shell.so.0
%{_libdir}/libgtk-layer-shell.so.0.?.0

%files -n gtk-layer-shell-devel
%{_libdir}/libgtk-layer-shell.so
%{_includedir}/gtk-layer-shell
%{_libdir}/pkgconfig/gtk-layer-shell-0.pc
%{_datadir}/gir-1.0/GtkLayerShell-0.1.gir

%files -n  typelib-1_0-GtkLayerShell-0_1
%{_libdir}/girepository-1.0/GtkLayerShell-0.1.typelib

%changelog
