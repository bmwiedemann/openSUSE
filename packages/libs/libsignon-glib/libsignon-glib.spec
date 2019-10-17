#
# spec file for package libsignon-glib
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


%define sover 2

Name:           libsignon-glib
Version:        2.1
Release:        0
Summary:        Library for signond
License:        LGPL-2.1-only
Group:          System/Libraries
URL:            https://gitlab.com/accounts-sso/libsignon-glib
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-gobject-devel
BuildRequires:  pkgconfig(gio-2.0) >= 2.36
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-2.0) >= 2.35.1
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(vapigen)

%description
GLib-based client library for applications handling account
authentication through the Online Accounts Single Sign-On service

%package -n libsignon-glib%{sover}
Summary:        Library for signond
Group:          System/Libraries

%description -n libsignon-glib%{sover}
GLib-based client library for applications handling account
authentication through the Online Accounts Single Sign-On service

This package provides shared libraries for libsignon-glib

%package devel
Summary:        Development headers for libsignon-glib
Group:          Development/Libraries/C and C++
Requires:       libsignon-glib%{sover} = %{version}

%description devel
GLib-based client library for applications handling account
authentication through the Online Accounts Single Sign-On service

This package provides development headers for libsignon-glib.

%package -n python3-libsignon-glib
Summary:        Python bindings for the libsignon-glib library
Group:          Development/Languages/Python

%description -n python3-libsignon-glib
This package contains the python bindings for the libsignon-glib
management library.

%package -n typelib-1_0-Signon-2_0
Summary:        Library for signond -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Signon-2_0
GLib-based client library for applications handling account
authentication through the Online Accounts Single Sign-On service

This package provides the GObject Introspection bindings for
libsignon-glib library.

%prep
%autosetup -p1

%build
%meson \
	-Dtests=false \
	%{nil}
%meson_build

%install
%meson_install

%post -n libsignon-glib%{sover} -p /sbin/ldconfig
%postun -n libsignon-glib%{sover} -p /sbin/ldconfig

%files -n libsignon-glib%{sover}
%license COPYING
%doc AUTHORS README.md NEWS
%{_libdir}/libsignon-glib.so.*

%files devel
%doc %{_datadir}/gtk-doc/html/
%{_includedir}/libsignon-glib
%{_libdir}/libsignon-glib.so
%{_libdir}/pkgconfig/libsignon-glib.pc
%{_datadir}/gir-1.0/Signon-2.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libsignon-glib.deps
%{_datadir}/vala/vapi/libsignon-glib.vapi

%files -n python3-libsignon-glib
%{python3_sitearch}/gi/overrides/

%files -n typelib-1_0-Signon-2_0
%{_libdir}/girepository-1.0/Signon-2.0.typelib

%changelog
