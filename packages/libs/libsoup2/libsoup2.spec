#
# spec file for package libsoup2
#
# Copyright (c) 2026 SUSE LLC and contributors
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
# PATCH-FIX-UPSTREAM ef6c4bf6.patch boo#1240750 mgorse@suse.com -- fix a potential overflow.
Patch11:        https://gitlab.gnome.org/GNOME/libsoup/-/commit/ef6c4bf6.patch
# PATCH-FIX-UPSTREAM 96c22b67.patch boo#1240750 mgorse@suse.com -- add better coverage of skip_insignificant_space.
Patch12:        https://gitlab.gnome.org/GNOME/libsoup/-/commit/96c22b67.patch
# PATCH-FIX-UPSTREAM 19124679.patch boo#1240752 mgorse@suse.com -- Fix using int instead of size_t for strcspn return.
Patch13:        https://gitlab.gnome.org/GNOME/libsoup/-/commit/19124679.patch
# PATCH-FIX-UPSTREAM a5b86bfc.patch boo#1240756 mgorse@suse.com -- fix heap buffer overflow in soup_content_sniffer_sniff.
Patch14:        https://gitlab.gnome.org/GNOME/libsoup/-/commit/a5b86bfc.patch
# PATCH-FIX-UPSTREAM 5739a090.patch boo#1240757 mgorse@suse.com -- fix heap buffer overflow in soup_content_sniffer.c:sniff_feed_or_html
Patch15:        https://gitlab.gnome.org/GNOME/libsoup/-/commit/5739a090.patch
# PATCH-FIX-UPSTREAM c9083869.patch boo#1241686 mgorse@suse.com -- fix leak in soup_header_parse_quality_list.
Patch16:        https://gitlab.gnome.org/GNOME/libsoup/-/commit/c9083869.patch
# PATCH-FIX-UPSTREAM libsoup-CVE-2025-32914.patch boo#1241164 mgorse@suse.com -- fix read out of buffer bounds under soup_multipart_new_from_message.
Patch17:        libsoup-CVE-2025-32914.patch
# PATCH-FIX-UPSTREAM libsoup-CVE-2025-32907.patch boo#1241222 mgorse@suse.com -- correct merge of ranges.
Patch18:        libsoup-CVE-2025-32907.patch
# PATCH-FIX-UPSTREAM libsoup-CVE-2025-46421.patch boo#1241688 mgorse@suse.com -- strip authentication credentials on cross-origin redirect.
Patch19:        libsoup-CVE-2025-46421.patch
# PATCH-FIX-UPSTREAM libsoup-CVE-2025-32913.patch boo#1241162 mgorse@suse.com -- fix NULL deref in soup_message_headers_get_content_disposition.
Patch20:        libsoup-CVE-2025-32913.patch
# PATCH-FIX-UPSTREAM libsoup-CVE-2025-32910.patch boo#1241252 mgorse@suse.com -- fix NULL deref with missing realm in authenticate header.
Patch21:        libsoup-CVE-2025-32910.patch
# PATCH-FIX-UPSTREAM libsoup-CVE-2025-32912.patch boo#1241214 mgorse@suse.com -- fix NULL pointer deref in SoupAuthDigest.
Patch22:        libsoup-CVE-2025-32912.patch
# PATCH-FIX-UPSTREAM libsoup-CVE-2025-32906.patch boo#1241263 mgorse@suse.com -- fix an out-of-bounds read parsing headers.
Patch23:        libsoup-CVE-2025-32906.patch
# PATCH-FIX-UPSTREAM libsoup-CVE-2025-32909.patch boo#1241226 mgorse@suse.com -- handle sniffing resource shorter than 4 bytes.
Patch24:        libsoup-CVE-2025-32909.patch
# PATCH-FIX-UPSTREAM libsoup-CVE-2025-4948.patch boo#1243332 mgorse@suse.com -- verify boundary limits for multipart body.
Patch25:        libsoup-CVE-2025-4948.patch
# PATCH-FIX-UPSTREAM libsoup-CVE-2025-4969.patch boo#1243423 mgorse@suse.com -- soup-multipart: Verify array bounds before accessing its members.
Patch26:        libsoup-CVE-2025-4969.patch
# PATCH-FIX-UPSTREAM libsoup-CVE-2025-4945.patch boo#1243314 mgorse@suse.com -- add value checks for date/time parsing.
Patch27:        libsoup-CVE-2025-4945.patch
# PATCH-FIX-UPSTREAM libsoup2-CVE-2025-14523.patch bsc#1254876, CVE-2025-14523, glgo#GNOME/libsoup!491 alynx.zhou@suse.com -- Reject duplicated Host in headers
Patch28:        libsoup2-CVE-2025-14523.patch
# PATCH-FIX-UPSTREAM libsoup2-CVE-2026-0719.patch bsc#1256399, CVE-2026-0719, glgo#GNOME/libsoup!493 alynx.zhou@suse.com -- Fix overflow for password md4sum
Patch29:        libsoup2-CVE-2026-0719.patch
# PATCH-FIX-UPSTREAM libsoup2-CVE-2026-1761.patch bsc#1257598, CVE-2026-1761, glgo#GNOME/libsoup!496 sckang@suse.com -- multipart: check length of bytes read soup_filter_input_stream_read_until()
Patch30:        libsoup2-CVE-2026-1761.patch
# PATCH-FIX-UPSTREAM libsoup2-CVE-2026-0716.patch bsc#1256418, CVE-2026-0716, glgo#GNOME/libsoup!494 mgorse@suse.com -- Fix out-of-bounds read for websocket
Patch31:        libsoup2-CVE-2026-0716.patch
# PATCH-FIX-UPSTREAM libsoup2-CVE-2025-4476.patch boo#1243422 mgorse@suse.com -- fix crash in soup_auth_digest_get_protection_space.
Patch32:        libsoup2-CVE-2025-4476.patch
# PATCH-FIX-OPENSUSE libsoup2-CVE-2025-32049.patch bsc#1240751 mgorse@suse.com -- add size limit for total message size.
Patch33:        libsoup2-CVE-2025-32049.patch
# PATCH-FIX-UPSTREAM libsoup2-CVE-2026-2443.patch bsc#1243170 mgorse@suse.com -- fix out-of-bounds read when processing range headers.
Patch34:        libsoup2-CVE-2026-2443.patch
# PATCH-FIX-UPSTREAM libsoup2-CVE-2026-2369.patch bsc#1258120 mgorse@suse.com -- handle potential underflow in the content sniffer.
Patch35:        libsoup2-CVE-2026-2369.patch
# PATCH-FIX-UPSTREAM libsoup2-CVE-2026-2708.patch bsc#1258508 mgorse@suse.com -- do not allow adding multiple content length values to headers.
Patch36:        libsoup2-CVE-2026-2708.patch

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

%install
%meson_install
%find_lang %{_name} %{?no_lang_C}

%ldconfig_scriptlets -n %{_name}-2_4-1

%check
# Run the regression tests using GnuTLS NORMAL priority
export G_TLS_GNUTLS_PRIORITY=NORMAL
%ifnarch x86_64
%meson_test -t 5  || (%meson_test -t 5)
%else
%meson_test || (%meson_test)
%endif

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
