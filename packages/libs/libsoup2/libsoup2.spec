#
# spec file for package libsoup2
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


Name:           libsoup2
%define _name libsoup
Version:        2.74.3
Release:        0
Summary:        HTTP client/server library for GNOME
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Projects/libsoup
Source0:        https://download.gnome.org/sources/libsoup/2.74/%{_name}-%{version}.tar.xz
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE disable tls_interaction-test https://gitlab.gnome.org/GNOME/libsoup/issues/120
Patch1:         libsoup-skip-tls_interaction-test.patch
# PATCH-FIX-UPSTREAM libsoup2-extend-test-cert.patch boo#1102840 -- Fix tests after 2027
Patch2:         libsoup2-extend-test-cert.patch
# PATCH-FIX-UPSTREAM 4d12c3e5.patch -- lib: Add g_task_set_source_tag() everywhere
Patch3:         https://gitlab.gnome.org/GNOME/libsoup/-/commit/4d12c3e5.patch
# PATCH-FIX-UPSTREAM 48b3b611.patch -- lib: Add names to various GSources
Patch4:         https://gitlab.gnome.org/GNOME/libsoup/-/commit/48b3b611.patch
# PATCH-FIX-UPSTREAM ced3c5d8.patch -- Fix build with libxml2-2.12.0 and clang-17
Patch5:         https://gitlab.gnome.org/GNOME/libsoup/-/commit/ced3c5d8.patch
# PATCH-FIX-UPSTREAM 04df03bc.patch boo#1233285 mgorse@suse.com -- strictly don't allow NUL bytes in headers.
Patch6:         https://gitlab.gnome.org/GNOME/libsoup/-/commit/04df03bc.patch
# PATCH-FIX-UPSTREAM libsoup-CVE-2024-52532.patch boo#1233287 mgorse@suse.com -- process the frame as soon as we read data.
Patch7:         libsoup-CVE-2024-52532.patch
# PATCH-FIX-UPSTREAM 29b96fab.patch boo#1233287 mgorse@suse.com -- websocket-test: disconnect error copy after the test ends.
Patch8:         https://gitlab.gnome.org/GNOME/libsoup/-/commit/29b96fab.patch
# PATCH-FIX-UPSTREAM a35222dd.patch boo#1233292 mgorse@suse.com -- be more robust against invalid input when parsing params.
Patch9:         https://gitlab.gnome.org/GNOME/libsoup/-/commit/a35222dd.patch
# PATCH-FIX-UPSTREAM 4c9e75c6.patch boo#1233287 mgorse@suse.com -- fix an intermittent test failure.
Patch10:        https://gitlab.gnome.org/GNOME/libsoup/-/commit/4c9e75c6.patch

BuildRequires:  glib-networking
BuildRequires:  meson >= 0.50
BuildRequires:  pkgconfig
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

%package -n %{_name}-2_4-1
Summary:        HTTP client/server library for GNOME
Group:          Development/Libraries/GNOME
Requires:       glib-networking >= 2.27.90
# For NTLM single sign on
Suggests:       samba-winbind
# Needed to make the lang package installable
Provides:       %{name} = %{version}

%description -n %{_name}-2_4-1
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
Requires:       libsoup-2_4-1 = %{version}
Requires:       typelib-1_0-Soup-2_4 = %{version}
Provides:       %{_name}-doc = %{version}
Obsoletes:      %{_name}-doc < %{version}

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
%autosetup -p1 -n %{_name}-%{version}

%build
%meson \
    -Dgssapi=enabled \
    -Dkrb5_config="$(which krb5-config)" \
    -Dvapi=enabled \
    -Dgtk_doc=true \
    -Dntlm=disabled \
    -Dsysprof=disabled \
    %{nil}
%meson_build

%check
# Run the regression tests using GnuTLS NORMAL priority
export G_TLS_GNUTLS_PRIORITY=NORMAL
%meson_test

%install
%meson_install
%find_lang %{_name} %{?no_lang_C}

%ldconfig_scriptlets -n %{_name}-2_4-1

%files -n %{_name}-2_4-1
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

%files lang -f %{_name}.lang

%changelog
