#
# spec file for package libhandy0
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


%define shlib %{_name}-0_0-0

Name:           libhandy0
%define _name   libhandy
Version:        0.0.13
Release:        0
Summary:        A GTK+ library to develop UI for mobile devices
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://source.puri.sm/Librem5/libhandy/
Source0:        %{_name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM libhandy-adapt-glade-3-36.patch -- Fix build with new glade 3.36
Patch0:         libhandy-adapt-glade-3-36.patch

BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.1

%description
libhandy is a library to help with developing UI for mobile devices
using GTK+/GNOME.

%package -n %{shlib}
Summary:        A GTK+ library to develop UI for mobile devices
Group:          System/Libraries

%description -n %{shlib}
This package provides the shared library for libhandy, a library to
help with developing mobile UI using GTK+/GNOME.

%package devel
Summary:        Source and header files for %{name}
Group:          Development/Libraries/GNOME
Requires:       %{shlib} = %{version}
Requires:       typelib-1_0-Handy-0_0 = %{version}
Conflicts:      %{_name}-devel

%description devel
This package provides the source and header files for writing
software using %{name}, a library to help with developing mobile UI
using GTK+/GNOME.

%package -n typelib-1_0-Handy-0_0
Summary:        Introspection bindings for libhandy
Group:          System/Libraries

%description -n typelib-1_0-Handy-0_0
This package provides the GObject Introspection bindings for
%{name}, a library to help with developing mobile UI using
GTK+/GNOME.

%package -n glade-catalog-libhandy0
Summary:        Glade catalog for libhandy
Group:          Development/Tools/GUI Builders
Requires:       glade
Supplements:    packageand(glade:%{name}-devel)
Conflicts:      glade-catalog-libhandy

%description -n glade-catalog-libhandy0
libhandy is a library to help with developing UI for mobile devices
using GTK+/GNOME.

This package provides a catalog for libhandy, to allow the use
libhandy widgets in Glade.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%meson \
	-Dprofiling=false \
	-Dstatic=false \
	-Dintrospection=enabled \
	-Dvapi=true \
	-Dgtk_doc=true \
	-Dtests=false \
	-Dexamples=false \
	-Dglade_catalog=enabled \
	%{nil}
%meson_build

%install
%meson_install

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%{_libdir}/libhandy-*.so.*

%files devel
%license COPYING
%doc AUTHORS README.md
%{_includedir}/libhandy-0.0/
%{_libdir}/libhandy-*.so
%{_datadir}/gir-1.0/*.gir
%{_libdir}/pkgconfig/libhandy-0.0.pc
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libhandy-*
%{_datadir}/gtk-doc/html/libhandy/

%files -n typelib-1_0-Handy-0_0
%{_libdir}/girepository-1.0/*.typelib

%files -n glade-catalog-libhandy0
%{_libdir}/glade/modules/*.so
%{_datadir}/glade/catalogs/*.xml

%changelog
