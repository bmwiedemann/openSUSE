#
# spec file for package libsoup
#
# Copyright (c) 2020 SUSE LLC
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


Name:           libsoup
Version:        2.70.0
Release:        0
Summary:        HTTP client/server library for GNOME
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Projects/libsoup
Source0:        https://download.gnome.org/sources/libsoup/2.70/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

# PATCH-FIX-OPENSUSE libsoup-disable-hsts-tests.patch mgorse@suse.com -- disable hsts tests.
Patch0:         libsoup-disable-hsts-tests.patch
# PATCH-FIX-UPSTREAM libsoup-test-utils-fix.patch -- test-utils: Clarify meaning of an environment variable
Patch1:         libsoup-test-utils-fix.patch
# PATCH-FIX-OPENSUSE libsoup-disable-ssl-tests.patch glgo#GNOME/libsoup#188 -- Disable ssl tests
Patch2:         libsoup-disable-ssl-tests.patch

BuildRequires:  glib-networking
BuildRequires:  meson >= 0.50
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(gio-2.0) >= 2.58.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.58.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.58.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.5
BuildRequires:  pkgconfig(gtk-doc) >= 1.20
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libpsl) >= 0.20
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(vapigen)
# We do not need these dependencies needed only for tests.
#BuildRequires:  apache2-mod_php5 php5-xmlrpc

%description
Libsoup is an HTTP client/server library for GNOME. It uses GObjects
and the glib main loop, to integrate well with GNOME applications.

Features:
  * Both asynchronous (GMainLoop and callback-based) and synchronous APIs
  * Automatically caches connections
  * SSL Support using GnuTLS
  * Proxy support, including authentication and SSL tunneling
  * Client support for Digest, NTLM, and Basic authentication
  * Server support for Digest and Basic authentication
  * XML-RPC support

%package 2_4-1
Summary:        HTTP client/server library for GNOME
Group:          Development/Libraries/GNOME
Requires:       glib-networking >= 2.27.90
# For NTLM single sign on
Suggests:       samba-winbind
# Needed for smooth upgrades and to make the lang package installable
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description 2_4-1
Libsoup is an HTTP client/server library for GNOME. It uses GObjects
and the glib main loop, to integrate well with GNOME applications.

Features:
  * Both asynchronous (GMainLoop and callback-based) and synchronous APIs
  * Automatically caches connections
  * SSL Support using GnuTLS
  * Proxy support, including authentication and SSL tunneling
  * Client support for Digest, NTLM, and Basic authentication
  * Server support for Digest and Basic authentication
  * XML-RPC support

%package -n typelib-1_0-Soup-2_4
Summary:        HTTP client/server library for GNOME -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Soup-2_4
Libsoup is an HTTP client/server library for GNOME. It uses GObjects
and the glib main loop, to integrate well with GNOME applications.

This package provides the GObject Introspection bindings for libsoup.

%package devel
Summary:        HTTP client/server library for GNOME - Development Files
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Requires:       typelib-1_0-Soup-2_4 = %{version}
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}

%description devel
Libsoup is an HTTP client/server library for GNOME. It uses GObjects
and the glib main loop, to integrate well with GNOME applications.

Features:
  * Both asynchronous (GMainLoop and callback-based) and synchronous APIs
  * Automatically caches connections
  * SSL Support using GnuTLS
  * Proxy support, including authentication and SSL tunneling
  * Client support for Digest, NTLM, and Basic authentication
  * Server support for Digest and Basic authentication
  * XML-RPC support

%lang_package

%prep
%autosetup -p1
translation-update-upstream po libsoup

%build
%meson \
	-Dgssapi=enabled \
	-Dkrb5_config="$(which krb5-config)" \
	-Dvapi=enabled \
	-Dgtk_doc=true \
	-Dntlm=disabled \
	%{nil}
%meson_build

%check
%meson_test

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%post 2_4-1 -p /sbin/ldconfig
%postun 2_4-1 -p /sbin/ldconfig

%files 2_4-1
%license COPYING
%doc NEWS
%{_libdir}/*.so.*

%files -n typelib-1_0-Soup-2_4
%{_libdir}/girepository-1.0/Soup-2.4.typelib
%{_libdir}/girepository-1.0/SoupGNOME-2.4.typelib

%files devel
%doc AUTHORS README
%{_includedir}/libsoup-2.4
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libsoup-gnome-2.4
%doc %{_datadir}/gtk-doc/html/libsoup-2.4
%{_datadir}/gir-1.0/Soup-2.4.gir
%{_datadir}/gir-1.0/SoupGNOME-2.4.gir
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/libsoup-2.4.vapi
%{_datadir}/vala/vapi/libsoup-2.4.deps

%files lang -f %{name}.lang

%changelog
