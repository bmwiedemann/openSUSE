#
# spec file for package libshumate
#
# Copyright (c) 2022 SUSE LLC
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


%define somajor 1
%define sominor 0
%define soname libshumate-%{somajor}_%{sominor}-1

Name:           libshumate
Version:        1.0.3
Release:        0
Summary:        C library providing a GtkWidget to display maps
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/libshumate
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gtk-doc >= 1.9
BuildRequires:  meson >= 0.53.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo) >= 1.4
BuildRequires:  pkgconfig(gi-docgen) >= 2021.1
BuildRequires:  pkgconfig(gio-2.0) >= 2.16.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.16.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.16.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.6.3
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libsoup-3.0) >= 3.0
BuildRequires:  pkgconfig(sqlite3) >= 1.12.0
BuildRequires:  pkgconfig(vapigen) >= 0.11.0

%description
libshumate is a C library providing a GtkWidget to display maps.
It supports numerous free map sources such as OpenStreetMap,
OpenCycleMap, OpenAerialMap and Maps for free.

libshumate is named after Jessamine Shumate, an American artist,
historian, and cartographer (Wikipedia). libshumate is forked from,
and tries to follow similar principles in the API as libchamplain.

%package -n %{soname}
Summary:        Shared library for %{name}
Provides:       %{name} = %{version}

%description -n %{soname}
C library providing a GtkWidget to display maps.
This package contains the shared library files.

%package -n typelib-1_0-Shumate-%{somajor}_%{sominor}
Summary:        Introspection file for %{name}

%description -n typelib-1_0-Shumate-%{somajor}_%{sominor}
C library providing a GtkWidget to display maps.
This package contains introspection file for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{soname} = %{version}
Requires:       typelib-1_0-Shumate-%{somajor}_%{sominor} = %{version}

%description devel
C library providing a GtkWidget to display maps.
This package contains development files for %{name}.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D libsoup3=true \
	-D vector_renderer=true \
	-D gtk_doc=true \
	%{nil}
%meson_build

%install
%meson_install
%find_lang shumate%{somajor} %{?no_lang_C}

%ldconfig_scriptlets -n %{soname}

%files -n %{soname}
%license COPYING
%{_libdir}/libshumate-%{somajor}.%{sominor}.so.*

%files -n typelib-1_0-Shumate-%{somajor}_%{sominor}
%{_libdir}/girepository-1.0/Shumate-%{somajor}.%{sominor}.typelib

%files devel
%doc AUTHORS README.md
%{_datadir}/doc/libshumate-%{somajor}.%{sominor}/
%{_includedir}/shumate-%{somajor}.%{sominor}/
%{_libdir}/pkgconfig/shumate-%{somajor}.%{sominor}.pc
%{_libdir}/libshumate-%{somajor}.%{sominor}.so
%{_datadir}/gir-1.0/Shumate-%{somajor}.%{sominor}.gir
%{_datadir}/vala/vapi/shumate-%{somajor}.%{sominor}.deps
%{_datadir}/vala/vapi/shumate-%{somajor}.%{sominor}.vapi

%files lang -f shumate%{somajor}.lang

%changelog
