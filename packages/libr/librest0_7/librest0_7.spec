#
# spec file for package librest0_7
#
# Copyright (c) 2022 SUSE LLC
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
%define abi     0.7
%define abi_pkg 0_7
%define libname librest-%{abi_pkg}-%{sover}
Name:           librest0_7
Version:        0.8.1
Release:        0
Summary:        Library to access RESTful web services
License:        LGPL-2.1-only
Group:          Development/Libraries/GNOME
URL:            http://git.gnome.org/browse/librest/
Source0:        http://download.gnome.org/sources/rest/0.8/%{_name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.24
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libsoup-gnome-2.4)
BuildRequires:  pkgconfig(libxml-2.0)

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
%setup -q -n %{_name}-%{version}

%build
%configure \
	--disable-static \
	--with-ca-certificates=%{_sysconfdir}/ssl/ca-bundle.pem \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license COPYING
%doc AUTHORS README
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
%doc %{_datadir}/gtk-doc/html/rest-%{abi}/

%changelog
