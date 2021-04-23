#
# spec file for package jsonrpc-glib
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


%define sover 1_0-1
Name:           jsonrpc-glib
Version:        3.38.0
Release:        0
Summary:        Library to communicate with JSON-RPC based peers
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://gitlab.gnome.org/GNOME/jsonrpc-glib
Source0:        https://download.gnome.org/sources/jsonrpc-glib/3.38/%{name}-%{version}.tar.xz

BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.49.2
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(vapigen)

%description
This is a library to communicate with JSON-RPC based peers in
either a synchronous or an asynchronous fashion. It also allows
communicating using the GVariant serialization format instead
of JSON when both peers support it.

%package -n     libjsonrpc-glib-%{sover}
Summary:        Library to communicate with JSON-RPC based peers
Group:          System/Libraries

%description -n libjsonrpc-glib-%{sover}
This is a library to communicate with JSON-RPC based peers in
either a synchronous or an asynchronous fashion. It also allows
communicating using the GVariant serialization format instead
of JSON when both peers support it.

This package contains the Jsonrpc-GLib shared library.

%package -n     typelib-1_0-Jsonrpc-1_0
Summary:        JSON-RPC based peers lib -- Introspection bindings
# typelib-1_0-Jsonrpc-1.0 has been renamed to typelib-1_0-Jsonrpc-1_0 to match packaging guideline
Group:          System/Libraries
Obsoletes:      typelib-1_0-Jsonrpc-1.0 <= %{version}

%description -n typelib-1_0-Jsonrpc-1_0
This is a library to communicate with JSON-RPC based peers in
either a synchronous or an asynchronous fashion. It also allows
communicating using the GVariant serialization format instead
of JSON when both peers support it.

This package contains the Jsonrpc-GLib introspection bindings.

%package        devel
Summary:        Development environment for jsonrpc-glib
Group:          Development/Languages/C and C++
Requires:       libjsonrpc-glib-%{sover} = %{version}
Requires:       typelib-1_0-Jsonrpc-1_0 = %{version}

%description devel
This is a library to communicate with JSON-RPC based peers in
either a synchronous or an asynchronous fashion. It also allows
communicating using the GVariant serialization format instead
of JSON when both peers support it.

This package contains all files necessary for development using
Jsonrpc-GLib.

%prep
%autosetup

%build
%meson \
	-Denable_profiling=false \
	-Dwith_introspection=true \
	-Dwith_vapi=true \
	-Denable_gtk_doc=true \
	-Denable_tests=false \
	%{nil}
%meson_build

%install
%meson_install

%post -n libjsonrpc-glib-%{sover} -p /sbin/ldconfig
%postun -n libjsonrpc-glib-%{sover} -p /sbin/ldconfig

%files -n libjsonrpc-glib-%{sover}
%license COPYING
%doc NEWS
%{_libdir}/libjsonrpc-glib-1.0.so.*

%files -n typelib-1_0-Jsonrpc-1_0
%{_libdir}/girepository-1.0/Jsonrpc-1.0.typelib

%files devel
%doc AUTHORS CONTRIBUTING.md README.md
%doc %{_datadir}/gtk-doc/html/jsonrpc-glib/
%dir %{_includedir}/jsonrpc-glib-1.0
%{_includedir}/jsonrpc-glib-1.0/jsonrpc-*.h
%{_libdir}/libjsonrpc-glib-1.0.so
%{_datadir}/gir-1.0/Jsonrpc-1.0.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/jsonrpc-glib-1.0.deps
%{_datadir}/vala/vapi/jsonrpc-glib-1.0.vapi
%{_libdir}/pkgconfig/jsonrpc-glib-1.0.pc

%changelog
