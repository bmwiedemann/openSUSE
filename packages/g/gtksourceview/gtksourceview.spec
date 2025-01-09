#
# spec file for package gtksourceview
#
# Copyright (c) 2025 SUSE LLC
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


Name:           gtksourceview
Version:        3.24.11
Release:        0
Summary:        GTK+ Source Editing Widget
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Projects/GtkSourceView
Source0:        http://download.gnome.org/sources/gtksourceview/3.24/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM gtksourceview-gcc14.patch mgorse@suse.com -- fix assignment from incompatible pointer type.
Patch0:         gtksourceview-gcc14.patch

BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel >= 1.42.0
BuildRequires:  itstool
BuildRequires:  libxml2-devel >= 2.6
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0) >= 2.48
BuildRequires:  pkgconfig(gladeui-2.0) >= 3.9
BuildRequires:  pkgconfig(glib-2.0) >= 2.48
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(valgrind)

%description
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

%package -n libgtksourceview-3_0-1
Summary:        GTK+ Source Editing Widget
Group:          System/Libraries
Provides:       gtksourceview = %{version}
Provides:       libgtksourceview3 = %{version}
Obsoletes:      gtksourceview < %{version}

%description -n libgtksourceview-3_0-1
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

%package -n typelib-1_0-GtkSource-3_0
Summary:        Introspection bindings for the GTK+ source editing widget
Group:          System/Libraries

%description -n typelib-1_0-GtkSource-3_0
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

This package provides the GObject Introspection bindings for
GtkSourceView.

%package -n glade-catalog-gtksourceview
Summary:        Glade catalog for the GTK+ source editing widget
Group:          Development/Tools/GUI Builders
Requires:       glade
Requires:       libgtksourceview-3_0-1 = %{version}
Supplements:    (glade and %{name}-devel)

%description -n glade-catalog-gtksourceview
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

This package provides a catalog for Glade, to allow the use the
GtkSourceView widget in Glade.

%package devel
Summary:        Development files for the GTK+ source editing widget
Group:          Development/Languages/C and C++
Requires:       libgtksourceview-3_0-1 = %{version}
Requires:       libgtksourceview3 = %{version}
Requires:       typelib-1_0-GtkSource-3_0 = %{version}

%description devel
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

%lang_package

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--enable-glade-catalog \
	--disable-gtk-doc \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}-3.0
%fdupes %{buildroot}%{_datadir}

%ldconfig_scriptlets -n libgtksourceview-3_0-1

%files -n libgtksourceview-3_0-1
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/libgtksourceview-3.0.so.*
%{_datadir}/gtksourceview-3.0/

%files -n typelib-1_0-GtkSource-3_0
%{_libdir}/girepository-1.0/GtkSource-3.0.typelib

%files -n glade-catalog-gtksourceview
%{_datadir}/glade/catalogs/gtksourceview.xml

%files devel
%doc ChangeLog MAINTAINERS
%{_includedir}/gtksourceview-3.0/
%{_libdir}/libgtksourceview-3.0.so
%{_libdir}/pkgconfig/gtksourceview-3.0.pc
%{_datadir}/gir-1.0/GtkSource-3.0.gir
%{_datadir}/gtk-doc/
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gtksourceview-3.0.*

%files lang -f %{name}-3.0.lang

%changelog
