#
# spec file for package telepathy-glib
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


Name:           telepathy-glib
Version:        0.24.2
Release:        0
Summary:        GObject-based library for the Telepathy D-Bus API
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++
URL:            http://telepathy.freedesktop.org/
Source:         http://telepathy.freedesktop.org/releases/telepathy-glib/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM telepathy-glib-function-type-cast.patch boo#1221707 mgorse@suse.com -- fix an invalid cast.
Patch0:         telepathy-glib-function-type-cast.patch

BuildRequires:  gtk-doc >= 1.17
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.16.0
BuildRequires:  pkgconfig(dbus-1) >= 0.95
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.90
BuildRequires:  pkgconfig(gio-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.30

%description
The telepathy-glib library is a GObject-based C binding for the
Telepathy D-Bus API.

%package -n libtelepathy-glib0
Summary:        GObject-based library for the Telepathy D-Bus API
Group:          Development/Languages/C and C++

%description -n libtelepathy-glib0
The telepathy-glib library is a GObject-based C binding for the
Telepathy D-Bus API.

%package -n typelib-1_0-TelepathyGlib-0_12
Summary:        GObject-based library for the Telepathy D-Bus API -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-TelepathyGlib-0_12
The telepathy-glib library is a GObject-based C binding for the
Telepathy D-Bus API.

This package provides the GObject Introspection bindings for the
telepathy-glib library.

%package devel
Summary:        GObject-based library for the Telepathy D-Bus API -- Development Files
Group:          Development/Languages/C and C++
Requires:       glibc-devel
Requires:       libtelepathy-glib0 = %{version}
Requires:       typelib-1_0-TelepathyGlib-0_12 = %{version}

%description devel
The telepathy-glib library is a GObject-based C binding for the
Telepathy D-Bus API.

%package doc
Summary:        GObject-based library for the Telepathy D-Bus API -- Developer documentation
Group:          Development/Languages/C and C++
Requires:       libtelepathy-glib0 = %{version}

%description doc
The telepathy-glib library is a GObject-based C binding for the
Telepathy D-Bus API.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--enable-vala-bindings \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libtelepathy-glib0 -p /sbin/ldconfig
%postun -n libtelepathy-glib0  -p /sbin/ldconfig

%files -n libtelepathy-glib0
%license COPYING
%{_libdir}/libtelepathy-glib*.so.0*

%files -n typelib-1_0-TelepathyGlib-0_12
%{_libdir}/girepository-1.0/TelepathyGLib-0.12.typelib

%files devel
%dir %{_includedir}/telepathy-1.0
%{_includedir}/telepathy-1.0/telepathy-glib/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/telepathy-glib.*

%files doc
%{_datadir}/gtk-doc/html/telepathy-glib

%changelog
