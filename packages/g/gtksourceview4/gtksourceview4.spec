#
# spec file for package gtksourceview4
#
# Copyright (c) 2021 SUSE LLC
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


%define _name   gtksourceview
Name:           gtksourceview4
Version:        4.8.1
Release:        0
Summary:        GTK+ Source Editing Widget
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Projects/GtkSourceView
Source0:        https://download.gnome.org/sources/gtksourceview/4.8/%{_name}-%{version}.tar.xz
Source1:        changes.lang
# PATCH-FIX-UPSTREAM d1ed58b2ab82bd5be55881088fc17ff1527511db.patch dimstar@opensuse.org -- build: disable -Werror for incompatible-pointer-types
Patch0:         https://gitlab.gnome.org/GNOME/gtksourceview/-/commit/d1ed58b2ab82bd5be55881088fc17ff1527511db.patch

BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  valgrind
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gio-2.0) >= 2.48
BuildRequires:  pkgconfig(gladeui-2.0) >= 3.9
BuildRequires:  pkgconfig(glib-2.0) >= 2.48
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6

%description
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

%package -n libgtksourceview-4-0
Summary:        GTK+ Source Editing Widget
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n libgtksourceview-4-0
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

%package -n typelib-1_0-GtkSource-4
Summary:        GTK+ Source Editing Widget -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GtkSource-4
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

This package provides the GObject Introspection bindings for
GtkSourceView.

%package -n glade-catalog-gtksourceview4
Summary:        GTK+ Source Editing Widget -- Catalog for Glade
Group:          Development/Tools/GUI Builders
Requires:       glade
Requires:       libgtksourceview-4-0 = %{version}
Supplements:    packageand(glade:%{name}-devel)
Obsoletes:      glade-catalog-gtksourceview <= %{version}
Provides:       glade-catalog-gtksourceview = %{version}

%description -n glade-catalog-gtksourceview4
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

This package provides a catalog for Glade, to allow the use the
GtkSourceView widget in Glade.

%package devel
Summary:        GTK+ Source Editing Widget
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
Requires:       typelib-1_0-GtkSource-4 = %{version}

%description devel
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

%lang_package

%prep
%autosetup -n %{_name}-%{version} -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%meson \
    -Dglade_catalog=true \
    -Dgtk_doc=true \
    %{nil}
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{_name}-4
# Install language definition for *.changes files:
install -m 644 %{S:1} %{buildroot}%{_datadir}/gtksourceview-4/language-specs/

%post -n libgtksourceview-4-0 -p /sbin/ldconfig
%postun -n libgtksourceview-4-0 -p /sbin/ldconfig

%files -n libgtksourceview-4-0
%license COPYING
%doc AUTHORS
%{_libdir}/libgtksourceview-4.so.*
%{_datadir}/gtksourceview-4/

%files -n typelib-1_0-GtkSource-4
%{_libdir}/girepository-1.0/GtkSource-4.typelib

%files -n glade-catalog-gtksourceview4
%{_datadir}/glade/catalogs/gtksourceview.xml

%files devel
%{_includedir}/gtksourceview-4/
%{_libdir}/libgtksourceview-4.so
%{_libdir}/pkgconfig/gtksourceview-4.pc
%{_datadir}/gir-1.0/GtkSource-4.gir
%{_datadir}/gtk-doc/html/gtksourceview-4.0/
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gtksourceview-4.*

%files lang -f %{_name}-4.lang

%changelog
