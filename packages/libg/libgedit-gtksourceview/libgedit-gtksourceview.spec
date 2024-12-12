#
# spec file for package libgedit-gtksourceview
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


%define sover 3

Name:           libgedit-gtksourceview
Version:        299.4.0
Release:        0
Summary:        Source code editing widget
License:        LGPL-2.1-or-later
URL:            https://gedit-technology.net/
Source:         %{name}-%{version}.tar.zst
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.74
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(libxml-2.0)

%description
libgedit-gtksourceview is a library that extends GtkTextView, the standard GTK
widget for multiline text editing. This library adds support for syntax
highlighting, undo/redo, file loading and saving, search and replace, a
completion system, printing, displaying line numbers, and other features typical
of a source code editor.

%lang_package

%package -n typelib-1_0-GtkSource-300
Summary:        libgedit-gtksourceview's GObject introspection bindings

%description -n typelib-1_0-GtkSource-300
The GObject introspection bindings for libgedit-gtksourceview library.

%package -n libgedit-gtksourceview-300-%{sover}
Summary:        libgedit-gtksourceview shared library
Requires:       %{name} >= %{version}

%description -n libgedit-gtksourceview-300-%{sover}
The libgedit-gtksourceview shared library.

%package devel
Summary:        Source code editing widget development headers
Requires:       libgedit-gtksourceview-300-%{sover} = %{version}
Requires:       typelib-1_0-GtkSource-300 = %{version}

%description devel
Development files related to libgedit-gtksourceview.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang libgedit-gtksourceview-300

%ldconfig_scriptlets -n libgedit-gtksourceview-300-%{sover}

%files
%license COPYING
%{_datadir}/libgedit-gtksourceview-300/

%files -n typelib-1_0-GtkSource-300
%{_libdir}/girepository-1.0/GtkSource-300.typelib

%files -n libgedit-gtksourceview-300-%{sover}
%{_libdir}/libgedit-gtksourceview-300.so.*

%files devel
%{_libdir}/libgedit-gtksourceview-300.so
%{_includedir}/libgedit-gtksourceview-300
%{_libdir}/pkgconfig/libgedit-gtksourceview-300.pc
%{_datadir}/gir-1.0/GtkSource-300.gir
%{_datadir}/gtk-doc/html/libgedit-gtksourceview-300

%files lang -f libgedit-gtksourceview-300.lang

%changelog
