#
# spec file for package gupnp
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


# When bumping soname, do not forget to bump in baselibs.conf too.
%define soname 1_2-0
%define sover 1.2

Name:           gupnp
Version:        1.2.1
Release:        0
Summary:        Implementation of the UPnP specification
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.gupnp.org/
Source0:        https://download.gnome.org/sources/gupnp/1.2/%{name}-%{version}.tar.xz
Source1:        baselibs.conf

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.44
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.6.4
BuildRequires:  pkgconfig(gssdp-1.2) >= 1.1.3
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.48.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vapigen)

%description
GUPnP implements the UPnP specification: resource announcement and
discovery, description, control, event notification, and presentation
(GUPnP includes basic web server functionality through libsoup). GUPnP
does not include helpers for construction or control of specific
standardized resources (e.g. MediaServer); this is left for higher level
libraries utilizing the GUPnP framework.

%package -n libgupnp-%{soname}
Summary:        Implementation of the UPnP specification
Group:          Development/Libraries/C and C++

%description -n libgupnp-%{soname}
GUPnP implements the UPnP specification: resource announcement and
discovery, description, control, event notification, and presentation
(GUPnP includes basic web server functionality through libsoup). GUPnP
does not include helpers for construction or control of specific
standardized resources (e.g. MediaServer); this is left for higher level
libraries utilizing the GUPnP framework.

%package -n typelib-1_0-GUPnP-1_0
Summary:        Implementation of the UPnP specification -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GUPnP-1_0
GUPnP implements the UPnP specification: resource announcement and
discovery, description, control, event notification, and presentation
(GUPnP includes basic web server functionality through libsoup). GUPnP
does not include helpers for construction or control of specific
standardized resources (e.g. MediaServer); this is left for higher level
libraries utilizing the GUPnP framework.

This package provides the GObject Introspection bindings for GUPnP.

%package -n libgupnp-devel
Summary:        Implementation of the UPnP specification - Development Files
Group:          Development/Libraries/C and C++
Requires:       libgupnp-%{soname} = %{version}
Requires:       typelib-1_0-GUPnP-1_0 = %{version}

%description -n libgupnp-devel
GUPnP implements the UPnP specification: resource announcement and
discovery, description, control, event notification, and presentation
(GUPnP includes basic web server functionality through libsoup). GUPnP
does not include helpers for construction or control of specific
standardized resources (e.g. MediaServer); this is left for higher level
libraries utilizing the GUPnP framework.

%prep
%autosetup -p1

%build
%meson \
	-Dcontext_manager=network-manager \
	-Dintrospection=true \
	-Dvapi=true \
	-Dgtk_doc=true \
	-Dexamples=false \
	%{nil}
%meson_build

%install
%meson_install

%post -n libgupnp-%{soname} -p /sbin/ldconfig
%postun -n libgupnp-%{soname} -p /sbin/ldconfig

%files -n libgupnp-%{soname}
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/*.so.*

%files -n typelib-1_0-GUPnP-1_0
%{_libdir}/girepository-1.0/GUPnP-%{sover}.typelib

%files -n libgupnp-devel
%{_bindir}/gupnp-binding-tool-%{sover}
%{_includedir}/%{name}-%{sover}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/GUPnP-%{sover}.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/%{name}
%{_datadir}/vala/vapi/gupnp-%{sover}.deps
%{_datadir}/vala/vapi/gupnp-%{sover}.vapi

%changelog
