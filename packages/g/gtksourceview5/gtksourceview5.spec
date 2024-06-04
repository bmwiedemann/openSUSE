#
# spec file for package gtksourceview5
#
# Copyright (c) 2024 SUSE LLC
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
Name:           gtksourceview5
Version:        5.12.1
Release:        0
Summary:        GTK+ Source Editing Widget
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Projects/GtkSourceView
Source0:        %{_name}-%{version}.tar.zst
Source1:        changes.lang

BuildRequires:  gobject-introspection-devel >= 1.70
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  valgrind
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fribidi) >= 0.19.7
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= 2.72
BuildRequires:  pkgconfig(glib-2.0) >= 2.72
BuildRequires:  pkgconfig(gtk4) >= 4.6
BuildRequires:  pkgconfig(libpcre2-8) >= 10.21
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6
BuildRequires:  pkgconfig(pangoft2)

%description
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

%package -n libgtksourceview-5-0
Summary:        GTK+ Source Editing Widget
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n libgtksourceview-5-0
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

%package -n typelib-1_0-GtkSource-5
Summary:        GTK+ Source Editing Widget -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GtkSource-5
GtkSourceView is a text widget that extends GtkTextView, the standard
GTK+ text widget.

It improves GtkTextView by implementing syntax highlighting and other
features typical of a source editor.

This package provides the GObject Introspection bindings for
GtkSourceView.

%package devel
Summary:        GTK+ Source Editing Widget
Group:          Development/Languages/C and C++
Requires:       libgtksourceview-5-0 = %{version}
Requires:       typelib-1_0-GtkSource-5 = %{version}

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
    %{nil}
%meson_build

%install
%meson_install
%find_lang %{_name}-5
# Install language definition for *.changes files:
install -m 644 %{S:1} %{buildroot}%{_datadir}/gtksourceview-5/language-specs/

%ldconfig_scriptlets -n libgtksourceview-5-0

%files -n libgtksourceview-5-0
%license COPYING
%doc AUTHORS
%{_libdir}/libgtksourceview-5.so.*
%{_datadir}/gtksourceview-5/
%{_datadir}/icons/*/*/*/*.svg

%files -n typelib-1_0-GtkSource-5
%{_libdir}/girepository-1.0/GtkSource-5.typelib

%files devel
%{_includedir}/gtksourceview-5/
%{_libdir}/libgtksourceview-5.so
%{_libdir}/pkgconfig/gtksourceview-5.pc
%{_datadir}/gir-1.0/GtkSource-5.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gtksourceview-5.*

%files lang -f %{_name}-5.lang

%changelog
