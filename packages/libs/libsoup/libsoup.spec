#
# spec file for package libsoup
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


%define api_version 3.0
Name:           libsoup
### FIXME ### Run meson tests for all arches when stable branch!
Version:        3.4.0
Release:        0
Summary:        HTTP client/server library for GNOME
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Projects/libsoup
Source0:        https://download.gnome.org/sources/libsoup/3.4/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  glib-networking
BuildRequires:  meson >= 0.53
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= 2.69.1
BuildRequires:  pkgconfig(glib-2.0) >= 2.69.1
BuildRequires:  pkgconfig(gnutls) >= 3.6.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.69.1
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.5
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libpsl) >= 0.20
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

%package 3_0-0
Summary:        HTTP client/server library for GNOME
Group:          Development/Libraries/GNOME
Requires:       glib-networking >= 2.27.90
# For NTLM single sign on
Suggests:       samba-winbind
# Needed for smooth upgrades and to make the lang package installable
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description 3_0-0
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

%package -n typelib-1_0-Soup-3_0
Summary:        HTTP client/server library for GNOME -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Soup-3_0
Libsoup is an HTTP client/server library for GNOME. It uses GObjects
and the glib main loop, to integrate well with GNOME applications.

This package provides the GObject Introspection bindings for libsoup.

%package devel
Summary:        HTTP client/server library for GNOME - Development Files
Group:          Development/Libraries/GNOME
Requires:       %{name}-3_0-0 = %{version}
Requires:       typelib-1_0-Soup-3_0 = %{version}
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

%build
%meson \
	-D gssapi=enabled \
	-D krb5_config="$(which krb5-config)" \
	-D vapi=enabled \
	-D docs=enabled \
	-D ntlm=disabled \
	-D sysprof=disabled \
	-D autobahn=disabled \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}-3.0 %{?no_lang_C}
# Make default docdir ref openSUSE standard
mkdir -p %{buildroot}%{_docdir}/%{name}-%{api_version}
# Move docs from upstream docdir to openSUSE docdir standard
mv %{buildroot}%{_datadir}/doc/%{name}-%{api_version} %{buildroot}%{_docdir}

%check
# Temp fix for failing tests during unstable
%ifarch ix86 x86_64
# Run the regression tests using GnuTLS NORMAL priority
export G_TLS_GNUTLS_PRIORITY=NORMAL
%meson_test
%endif

%ldconfig_scriptlets 3_0-0

%files 3_0-0
%license COPYING
%doc NEWS
%{_libdir}/*.so.*

%files -n typelib-1_0-Soup-3_0
%{_libdir}/girepository-1.0/Soup-%{api_version}.typelib

%files devel
%doc AUTHORS README
%doc %{_docdir}/%{name}-%{api_version}
%{_includedir}/libsoup-%{api_version}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/Soup-%{api_version}.gir
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/libsoup-%{api_version}.vapi
%{_datadir}/vala/vapi/libsoup-%{api_version}.deps

%files lang -f %{name}-3.0.lang

%changelog
