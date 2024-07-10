#
# spec file for package json-glib
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2009 Dominique Leuenberger, Almere, The Netherlands.
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


Name:           json-glib
Version:        1.8.0
Release:        0
Summary:        Library for JavaScript Object Notation format
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://live.gnome.org/JsonGlib

Source0:        https://download.gnome.org/sources/json-glib/1.8/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  glib2-devel >= 2.54
BuildRequires:  gobject-introspection-devel
BuildRequires:  libxslt-tools
BuildRequires:  meson
BuildRequires:  pkgconfig

%description
JSON-GLib provides a parser and a generator GObject classes and various
wrappers for the complex data types employed by JSON, such as arrays
and objects.

JSON-GLib uses GLib native data types and the generic value container
GValue for ease of development. It also provides integration with the
GObject classes for direct serialization into, and deserialization from,
JSON data streams.

%package -n libjson-glib-1_0-0
Summary:        Library for JavaScript Object Notation format
# To make lang subpackage installable
Group:          Development/Libraries/C and C++
Provides:       %{name} = %{version}

%description -n libjson-glib-1_0-0
JSON is a lightweight data-interchange format. It is comparatively
easy for humans to read and write, and for machines to parse and generate.

JSON-GLib provides a parser and a generator GObject classes and various
wrappers for the complex data types employed by JSON, such as arrays
and objects.

JSON-GLib uses GLib native data types and the generic value container
GValue for ease of development. It also provides integration with the
GObject classes for direct serialization into, and deserialization from,
JSON data streams.

%package -n typelib-1_0-Json-1_0
Summary:        Introspection bindings for libjson-glib
Group:          System/Libraries

%description -n typelib-1_0-Json-1_0
JSON-GLib provides a parser and a generator GObject classes and various
wrappers for the complex data types employed by JSON, such as arrays
and objects.

This package provides the GObject Introspection bindings for JSON-GLib.

%package devel
Summary:        Development files for libjson-glib
Group:          Development/Libraries/C and C++
Requires:       libjson-glib-1_0-0 = %{version}
Requires:       typelib-1_0-Json-1_0 = %{version}

%description devel
JSON-GLib provides a parser and a generator GObject classes and various
wrappers for the complex data types employed by JSON, such as arrays
and objects.

This package contains development files needed to develop with the
json-glib library.

%lang_package

%prep
%setup -q

%build
%meson \
	-Dman=true \
	-Dgtk_doc=disabled \
	%{nil}
%meson_build

%check
%meson_test

%install
%meson_install
%find_lang %{name}-1.0

%post -n libjson-glib-1_0-0 -p /sbin/ldconfig
%postun -n libjson-glib-1_0-0 -p /sbin/ldconfig

%files -n libjson-glib-1_0-0
%license COPYING

%{_libdir}/*.so.*

%files -n typelib-1_0-Json-1_0
%{_libdir}/girepository-1.0/Json-1.0.typelib

%files devel
%doc NEWS README.md
# These could potentially be split in a -tools package, but are never used by non-devs.
%{_bindir}/json-glib-format
%{_bindir}/json-glib-validate
%{_mandir}/man1/json-glib-format.1%{ext_man}
%{_mandir}/man1/json-glib-validate.1%{ext_man}
#
%{_includedir}/%{name}-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/installed-tests
%dir %{_libexecdir}/installed-tests
%{_datadir}/installed-tests/json-glib-1.0/
%{_libexecdir}/installed-tests/json-glib-1.0/

%files lang -f %{name}-1.0.lang

%changelog
