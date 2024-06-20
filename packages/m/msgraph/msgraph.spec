#
# spec file for package msgraph
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


Name:           msgraph
Version:        0.2.3
Release:        0
Summary:        Library for accessing online serive APIs using MS Graph protocol
License:        LGPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/msgraph
Source:         %{name}-%{version}.tar.zst
BuildRequires:  meson >= 0.63.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libuhttpmock-1.0) >= 0.11.0
BuildRequires:  pkgconfig(libxml-2.0)

%description
libmsgraph is a GLib-based library for accessing online serive APIs using MS Graph protocol.

%package -n libmsgraph-0-1
Summary:        Library for accessing online serive APIs using MS Graph protocol

%description -n libmsgraph-0-1
libmsgraph is a GLib-based library for accessing online serive APIs using MS Graph protocol.

%package -n typelib-1_0-Msg-0
Summary:        Library for accessing online serive APIs using MS Graph protocol

%description -n typelib-1_0-Msg-0
libmsgraph is a GLib-based library for accessing online serive APIs using MS Graph protocol.

%package devel
Summary:        Library for accessing online serive APIs using MS Graph protocol
Requires:       libmsgraph-0-1 = %{version}
Requires:       typelib-1_0-Msg-0 = %{version}

%description devel
libmsgraph is a GLib-based library for accessing online serive APIs using MS Graph protocol.

%prep
%autosetup
# the 'drive' test wats to connect to the actual drive / microsoft servers
sed -i '/drive/d' tests/meson.build

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n libmsgraph-0-1

%files -n libmsgraph-0-1
%license COPYING
%doc NEWS
%{_libdir}/libmsgraph-0.so.%{version}
%{_libdir}/libmsgraph-0.so.1

%files -n typelib-1_0-Msg-0
%{_libdir}/girepository-1.0/Msg-0.typelib

%files devel
%{_includedir}/msg/
%{_datadir}/doc/msgraph-0/
%{_libdir}/libmsgraph-0.so
%{_libdir}/pkgconfig/msgraph-0.1.pc
%{_datadir}/gir-1.0/Msg-0.gir

%changelog
