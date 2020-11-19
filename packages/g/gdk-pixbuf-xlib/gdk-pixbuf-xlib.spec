#
# spec file for package gdk-pixbuf-xlib
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gdk-pixbuf-xlib
Version:        2.40.1
Release:        0
Summary:        An GdkPixbuf compat library
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/Archive/gdk-pixbuf-xlib
Source:         %{name}-%{version}.tar.xz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM 1.patch dimstar@opensuse.org -- Headers are installed to the gdk-pixbuf-2.0 for compat reasons
Patch1:         https://gitlab.gnome.org/Archive/gdk-pixbuf-xlib/-/merge_requests/1.patch
# PATCH-FIX-UPSTREAM 2.patch dimstar@opensuse.org -- build: Declare public dependencies in pkg-config
Patch2:         https://gitlab.gnome.org/Archive/gdk-pixbuf-xlib/-/merge_requests/2.patch
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.39.2
BuildRequires:  pkgconfig(x11)

%description
gdk-pixbuf-xlib is an image loading library that can be extended by
loadable modules for new image formats. It is used by toolkits such
as GTK+ or Clutter.

This package is a compat package providing various functions to
integrate GdkPixbuf with Xlib data types

%package -n libgdk_pixbuf_xlib-2_0-0
Summary:        An GdkPixbuf compat library

%description -n libgdk_pixbuf_xlib-2_0-0
gdk-pixbuf-xlib is an image loading library that can be extended by
loadable modules for new image formats. It is used by toolkits such
as GTK+ or Clutter.

This package is a compat package providing various functions to
integrate GdkPixbuf with Xlib data types

%package devel
Summary:        Development files for gdk-pixbuf-xlib
Requires:       libgdk_pixbuf_xlib-2_0-0 = %{version}

%description devel
This package contains the development files for gdk-pixbuf-xlib.

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%post -n libgdk_pixbuf_xlib-2_0-0 -p /sbin/ldconfig
%postun -n libgdk_pixbuf_xlib-2_0-0 -p /sbin/ldconfig

%files -n libgdk_pixbuf_xlib-2_0-0
%license COPYING
%doc README.md
%{_libdir}/libgdk_pixbuf_xlib-2.0.so.*

%files devel
%{_includedir}/gdk-pixbuf-2.0/gdk-pixbuf-xlib/
%{_libdir}/libgdk_pixbuf_xlib-2.0.so
%{_libdir}/pkgconfig/gdk-pixbuf-xlib-2.0.pc

%changelog

