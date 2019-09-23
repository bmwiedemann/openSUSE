#
# spec file for package gssdp
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

Name:           gssdp
Version:        1.2.1
Release:        0
Summary:        Library for resource discovery and announcement over SSDP
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.gupnp.org/
Source0:        https://download.gnome.org/sources/gssdp/1.2/%{name}-%{version}.tar.xz
Source1:        baselibs.conf

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.26.1
BuildRequires:  pkgconfig(vapigen)

%description
gssdp offers a GObject-based API for handling resource discovery and
announcement over SSDP.

%package utils
Summary:        Utilities for resource discovery and announcement over SSDP
Group:          Productivity/Networking/Other

%description utils
gssdp offers a GObject-based API for handling resource discovery and
announcement over SSDP.

This package contains a device sniffer.

%package -n libgssdp-%{soname}
Summary:        Library for resource discovery and announcement over SSDP
Group:          Development/Libraries/C and C++

%description -n libgssdp-%{soname}
gssdp offers a GObject-based API for handling resource discovery and
announcement over SSDP.

%package -n typelib-1_0-GSSDP-1_0
Summary:        Lib for resource discovery and announcement over SSDP - Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GSSDP-1_0
gssdp offers a GObject-based API for handling resource discovery and
announcement over SSDP.

This package provides the GObject Introspection bindings for gssdp.

%package -n libgssdp-devel
Summary:        Library for resource discovery and announcement over SSDP - Development Files
Group:          Development/Libraries/C and C++
Requires:       libgssdp-%{soname} = %{version}
Requires:       typelib-1_0-GSSDP-1_0 = %{version}

%description -n libgssdp-devel
gssdp offers a GObject-based API for handling resource discovery and
announcement over SSDP.

%prep
%autosetup -p1

%build
%meson \
	-Dgtk_doc=true \
	-Dsniffer=true \
	-Dintrospection=true \
	-Dvapi=true \
	-Dexamples=false \
	%{nil}
%meson_build

%install
%meson_install

%check
### FIXME ###
#meson_test

%post -n libgssdp-%{soname} -p /sbin/ldconfig
%postun -n libgssdp-%{soname} -p /sbin/ldconfig

%files utils
%{_bindir}/*

%files -n libgssdp-%{soname}
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/*.so.*

%files -n typelib-1_0-GSSDP-1_0
%{_libdir}/girepository-1.0/GSSDP-%{sover}.typelib

%files -n libgssdp-devel
%{_includedir}/%{name}-%{sover}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/GSSDP-%{sover}.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/%{name}
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gssdp-%{sover}.deps
%{_datadir}/vala/vapi/gssdp-%{sover}.vapi

%changelog
