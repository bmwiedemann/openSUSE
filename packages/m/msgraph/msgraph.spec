#
# spec file for package msgraph
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define apiver 1
%define sover 1

Name:           msgraph
Version:        0.3.4
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

%package -n libmsgraph%{apiver}-%{sover}
Summary:        Library for accessing online serive APIs using MS Graph protocol

%description -n libmsgraph%{apiver}-%{sover}
libmsgraph is a GLib-based library for accessing online serive APIs using MS Graph protocol.

%package -n typelib-1_0-Msg-%{apiver}
Summary:        Library for accessing online serive APIs using MS Graph protocol

%description -n typelib-1_0-Msg-%{apiver}
libmsgraph is a GLib-based library for accessing online serive APIs using MS Graph protocol.

%package devel
Summary:        Library for accessing online serive APIs using MS Graph protocol
Requires:       libmsgraph%{apiver}-%{sover} = %{version}
Requires:       typelib-1_0-Msg-%{apiver} = %{version}

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

%ldconfig_scriptlets -n libmsgraph%{apiver}-%{sover}

%files -n libmsgraph%{apiver}-%{sover}
%license COPYING
%doc NEWS
%{_libdir}/libmsgraph-%{apiver}.so.%{version}
%{_libdir}/libmsgraph-%{apiver}.so.%{sover}

%files -n typelib-1_0-Msg-%{apiver}
%{_libdir}/girepository-1.0/Msg-%{apiver}.typelib

%files devel
%{_includedir}/msg/
%{_datadir}/doc/msgraph-%{apiver}/
%{_libdir}/libmsgraph-%{apiver}.so
%{_libdir}/pkgconfig/msgraph-%{apiver}.pc
%{_datadir}/gir-1.0/Msg-%{apiver}.gir

%changelog
