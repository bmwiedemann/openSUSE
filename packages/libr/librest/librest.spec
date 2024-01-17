#
# spec file for package librest
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


%define _name   rest
%define sover   0
%define abi     1.0
%define abi_pkg 1_0
%define libname librest-%{abi_pkg}-%{sover}
Name:           librest
Version:        0.9.1
Release:        0
Summary:        Library to access RESTful web services
License:        LGPL-2.1-only
Group:          Development/Libraries/GNOME
URL:            http://git.gnome.org/browse/librest/
Source0:        http://download.gnome.org/sources/rest/0.9/%{_name}-%{version}.tar.xz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM 0001-rest_proxy_call_sync-bail-out-if-no-payload.patch -- rest_proxy_call_sync: bail out if no payload
Patch0:         0001-rest_proxy_call_sync-bail-out-if-no-payload.patch
# PATCH-FIX-UPSTREAM 0002-Handle-some-potential-problems-in-parsing-oauth2-acc.patch -- Handle some potential problems in parsing oauth2 access tokens
Patch1:         0002-Handle-some-potential-problems-in-parsing-oauth2-acc.patch


BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(glib-2.0) >= 2.24
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(vapigen)

%description
This library was designed to make it easier to access web services that
claim to be "RESTful". A reasonable description is that a RESTful
service should have urls that represent remote objects, which methods
can then be called on.

It is comprised of two parts:

    * the first aims to make it easier to make requests by providing a
      wrapper around libsoup.
    * the second aids with XML parsing by wrapping libxml2.

%package -n %{libname}
Summary:        Library to access RESTful web services
Group:          System/Libraries
Recommends:     config(ca-certificates)
Obsoletes:      librest0 < %{version}-%{release}
Provides:       librest0 = %{version}-%{release}

%description -n %{libname}
This library was designed to make it easier to access web services that
claim to be "RESTful". A reasonable description is that a RESTful
service should have urls that represent remote objects, which methods
can then be called on.

It is comprised of two parts:

    * the first aims to make it easier to make requests by providing a
      wrapper around libsoup.
    * the second aids with XML parsing by wrapping libxml2.

%package -n typelib-1_0-Rest-%{abi_pkg}
Summary:        Library to access RESTful web services -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Rest-%{abi_pkg}
This library was designed to make it easier to access web services that
claim to be "RESTful". A reasonable description is that a RESTful
service should have urls that represent remote objects, which methods
can then be called on.

This package provides the GObject Introspection bindings for librest.

%package devel
Summary:        Library to access RESTful web services - Development Files
Group:          Development/Libraries/GNOME
Requires:       %{libname} = %{version}
Requires:       typelib-1_0-Rest-%{abi_pkg} = %{version}

%description devel
This library was designed to make it easier to access web services that
claim to be "RESTful". A reasonable description is that a RESTful
service should have urls that represent remote objects, which methods
can then be called on.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
# We should be able to pass both these (though just the first should be needed) - it fails the build however
#	-D ca_certificates=true \
#	-D ca_certificates_path=%%{_sysconfdir}/ssl/ca-bundle.pem \
%meson \
	-D ca_certificates=true \
	-D ca_certificates_path=%{_sysconfdir}/ssl/ca-bundle.pem \
	-D examples=false \
	-D vapi=true \
	%{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license COPYING
%doc AUTHORS README.md
%{_libdir}/librest-%{abi}.so.%{sover}
%{_libdir}/librest-%{abi}.so.%{sover}.*
%{_libdir}/librest-extras-%{abi}.so.%{sover}
%{_libdir}/librest-extras-%{abi}.so.%{sover}.*

%files -n typelib-1_0-Rest-%{abi_pkg}
%{_libdir}/girepository-1.0/Rest-%{abi}.typelib
%{_libdir}/girepository-1.0/RestExtras-%{abi}.typelib

%files devel
%{_libdir}/librest-%{abi}.so
%{_libdir}/librest-extras-%{abi}.so
%{_libdir}/pkgconfig/rest-%{abi}.pc
%{_libdir}/pkgconfig/rest-extras-%{abi}.pc
%{_datadir}/gir-1.0/*.gir
%{_includedir}/rest-%{abi}/
%doc %{_datadir}/doc/librest-%{abi}/
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/rest-1.0.deps
%{_datadir}/vala/vapi/rest-1.0.vapi
%{_datadir}/vala/vapi/rest-extras-1.0.deps
%{_datadir}/vala/vapi/rest-extras-1.0.vapi

%changelog
