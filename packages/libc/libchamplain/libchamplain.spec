#
# spec file for package libchamplain
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


Name:           libchamplain
Version:        0.12.21
Release:        0
Summary:        Library to display maps
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Projects/libchamplain
Source0:        https://download.gnome.org/sources/libchamplain/0.12/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo) >= 1.4
BuildRequires:  pkgconfig(clutter-1.0) >= 1.12
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 0.90
BuildRequires:  pkgconfig(gdk-3.0) >= 2.90
BuildRequires:  pkgconfig(gio-2.0) >= 2.68
BuildRequires:  pkgconfig(glib-2.0) >= 2.68
BuildRequires:  pkgconfig(gobject-2.0) >= 2.68
BuildRequires:  pkgconfig(gtk+-3.0) >= 2.90
BuildRequires:  pkgconfig(libsoup-3.0) >= 3.0
BuildRequires:  pkgconfig(sqlite3) >= 3.0
BuildRequires:  pkgconfig(vapigen)

%description
Libchamplain is a C library providing a ClutterActor to display maps. It
also provides a Gtk+ widget to display maps in Gtk+ applications.

It supports numerous free map sources such as OpenStreetMap,
OpenAerialMap and Maps for free.

%package -n libchamplain-0_12-0
Summary:        Library to display maps
Group:          Development/Libraries/GNOME

%description -n libchamplain-0_12-0
Libchamplain is a C library providing a ClutterActor to display maps. It
also provides a Gtk+ widget to display maps in Gtk+ applications.

It supports numerous free map sources such as OpenStreetMap,
OpenAerialMap and Maps for free.

%package -n typelib-1_0-Champlain-0_12
Summary:        Library to display maps -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Champlain-0_12
Libchamplain is a C library providing a ClutterActor to display maps. It
also provides a Gtk+ widget to display maps in Gtk+ applications.

This package provides the GObject Introspection bindings for
libchamplain.

%package devel
Summary:        Library to dusplay maps - Development Files
Group:          Development/Libraries/GNOME
Requires:       libchamplain-0_12-0 = %{version}
Requires:       typelib-1_0-Champlain-0_12 = %{version}

%description devel
Libchamplain is a C library providing a ClutterActor to display maps. It
also provides a Gtk+ widget to display maps in Gtk+ applications.

It supports numerous free map sources such as OpenStreetMap,
OpenAerialMap and Maps for free.

%prep
%autosetup -p1

%build
%meson \
	-Dmemphis=false \
	-Dintrospection=true \
	-Dvapi=true \
	-Dwidgetry=true \
	-Dgtk_doc=true \
	-Ddemos=false \
	%{nil}
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_datadir}/gtk-doc

%post -n libchamplain-0_12-0 -p /sbin/ldconfig
%postun -n libchamplain-0_12-0 -p /sbin/ldconfig

%files -n libchamplain-0_12-0
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libchamplain-0.12.so.*
%{_libdir}/libchamplain-gtk-0.12.so.*

%files -n typelib-1_0-Champlain-0_12
%{_libdir}/girepository-1.0/Champlain-0.12.typelib
%{_libdir}/girepository-1.0/GtkChamplain-0.12.typelib

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/champlain-0.12.pc
%{_libdir}/pkgconfig/champlain-gtk-0.12.pc
%{_includedir}/champlain-0.12/
%doc %{_datadir}/gtk-doc/html/champlain-0.12/
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/champlain-0.12.*
%{_datadir}/vala/vapi/champlain-gtk-0.12.*

%changelog
