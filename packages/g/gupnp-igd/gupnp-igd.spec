#
# spec file for package gupnp-igd
#
# Copyright (c) 2023 SUSE LLC
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


Name:           gupnp-igd
Version:        1.6.0
Release:        0
Summary:        Library to handle UPnP IGD port mapping
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://wiki.gnome.org/Projects/GUPnP
Source:         https://download.gnome.org/sources/gupnp-igd/1.6/%{name}-%{version}.tar.xz
Source1:        baselibs.conf

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.26
BuildRequires:  pkgconfig(gobject-2.0) >= 2.26
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gssdp-1.6)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(gupnp-1.6)

%description
GUPnP-IGD is a library to handle UPnP IGD port mapping. It is supposed
to have a very simple API.

%package -n libgupnp-igd-1_6-0
Summary:        Library to handle UPnP IGD port mapping
# Obsoletes may be removed when Leap 42.3 is out of support.
Group:          Development/Libraries/C and C++
Obsoletes:      python-gupnp-igd

%description -n libgupnp-igd-1_6-0
GUPnP-IGD is a library to handle UPnP IGD port mapping. It is supposed
to have a very simple API.

%package -n typelib-1_0-GUPnPIgd-1_6
Summary:        Library to handle UPnP IGD port mapping -- Introspection bindings
Group:          Development/Libraries/C and C++

%description -n typelib-1_0-GUPnPIgd-1_6
GUPnP-IGD is a library to handle UPnP IGD port mapping. It is supposed
to have a very simple API.

This package provides the GObject Introspection bindings for GUPnP-IGD.

%package -n libgupnp-igd-devel
Summary:        Library to handle UPnP IGD port mapping - Development Files
Group:          Development/Libraries/C and C++
Requires:       libgupnp-igd-1_6-0 = %{version}
Requires:       typelib-1_0-GUPnPIgd-1_6 = %{version}

%description -n libgupnp-igd-devel
GUPnP-IGD is a library to handle UPnP IGD port mapping. It is supposed
to have a very simple API.

%prep
%autosetup -p1

%build
%meson \
	-Dgtk_doc=true \
	%{nil}
%meson_build

%install
%meson_install

# Test is to flaky - disable 28-04-2023
# https://gitlab.gnome.org/GNOME/gupnp-igd/-/issues/3
#%%check
#%%meson_test

%ldconfig_scriptlets -n libgupnp-igd-1_6-0

%files -n libgupnp-igd-1_6-0
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/*.so.*

%files -n typelib-1_0-GUPnPIgd-1_6
%{_libdir}/girepository-1.0/GUPnPIgd-1.6.typelib

%files -n libgupnp-igd-devel
%{_includedir}/%{name}-1.6
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/GUPnPIgd-1.6.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/%{name}

%changelog
