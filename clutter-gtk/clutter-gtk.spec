#
# spec file for package clutter-gtk
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           clutter-gtk
Version:        1.8.4
Release:        0
Summary:        GTK+ integration for Clutter
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Url:            http://clutter-project.org/
Source0:        https://download.gnome.org/sources/clutter-gtk/1.8/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM clutter-gtk-Add-private-header.patch -- Add private header for GtkClutterEmbed
Patch0:         clutter-gtk-Add-private-header.patch
# PATCH-FIX-UPSTREAM clutter-gtk-Declare-private-callbacks-static.patch -- Declare private callbacks as static
Patch1:         clutter-gtk-Declare-private-callbacks-static.patch

BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(clutter-1.0) >= 1.23.7
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.21.4
BuildRequires:  pkgconfig(gtk+-x11-3.0) >= 3.6.0

%description
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces.

Clutter GTK+ enables the use of GTK+ with Clutter.

%package -n libclutter-gtk-1_0-0
Summary:        GTK+ integration for Clutter
Group:          System/Libraries
Recommends:     %{name}-lang
# To make lang package installable
Provides:       %{name} = %{version}

%description -n libclutter-gtk-1_0-0
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces.

Clutter GTK+ enables the use of GTK+ with Clutter.

%package -n typelib-1_0-GtkClutter-1_0
Summary:        Introspection bindings for the GTK+ Clutter integration
Group:          System/Libraries

%description -n typelib-1_0-GtkClutter-1_0
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces.

Clutter GTK+ enables the use of GTK+ with Clutter.

This package provides the GObject Introspection bindings for Clutter
GTK+.

%package devel
Summary:        Development files for the GTK+ Clutter integration
Group:          Development/Libraries/GNOME
Requires:       libclutter-gtk-1_0-0 = %{version}
Requires:       typelib-1_0-GtkClutter-1_0 = %{version}
Provides:       clutter-gtk-doc = %{version}
Obsoletes:      clutter-gtk-doc < %{version}

%description  devel
Clutter is an open source software library for creating fast, visually
rich and animated graphical user interfaces.

Clutter GTK+ enables the use of GTK+ with Clutter.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Denable_docs=true \
	%{nil}
%meson_build

# Check disabled as it seems to be missing from meson build for now
#%%check
#%%{meson_test}

%install
%meson_install
%find_lang cluttergtk-1.0 %{?no_lang_C}

%post -n libclutter-gtk-1_0-0 -p /sbin/ldconfig
%postun -n libclutter-gtk-1_0-0 -p /sbin/ldconfig

%files -n libclutter-gtk-1_0-0
%license COPYING
%doc README
%{_libdir}/*.so.*

%files -n typelib-1_0-GtkClutter-1_0
%{_libdir}/girepository-1.0/GtkClutter-1.0.typelib

%files devel
%{_libdir}/*.so
%{_includedir}/clutter-gtk-1.0/
%{_libdir}/pkgconfig/clutter-gtk-1.0.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/clutter-gtk-1.0/

%files lang -f cluttergtk-1.0.lang

%changelog
