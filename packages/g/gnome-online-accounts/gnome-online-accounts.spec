#
# spec file for package gnome-online-accounts
#
# Copyright (c) 2021 SUSE LLC
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


Name:           gnome-online-accounts
Version:        3.40.0
Release:        0
Summary:        GNOME service to access online accounts
License:        LGPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Projects/GnomeOnlineAccounts
Source0:        https://download.gnome.org/sources/gnome-online-accounts/3.40/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gio-2.0) >= 2.52
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.52
BuildRequires:  pkgconfig(glib-2.0) >= 2.52
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.6.2
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.19.12
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.42
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.26.0
# p11-kit is not 'strictly' seen a requirement, but without it none of the SSL/TLS
# Certificates are considered valid, which results in a really bad experience.
Requires:       p11-kit >= 0.16

%description
gnome-online-accounts provides interfaces so applications and
libraries in GNOME can access the user's online accounts.

%package -n libgoa-1_0-0
Summary:        GNOME service to access online accounts -- Client Library
Group:          System/Libraries
Recommends:     %{name}

%description -n libgoa-1_0-0
gnome-online-accounts provides interfaces so applications and
libraries in GNOME can access the user's online accounts.

%package -n typelib-1_0-Goa-1_0
Summary:        GNOME service to access online accounts -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Goa-1_0
gnome-online-accounts provides interfaces so applications and
libraries in GNOME can access the user's online accounts.

This package provides the GObject Introspection bindings for the libgoa
client library.

%package -n libgoa-backend-1_0-1
Summary:        GNOME service to access online accounts -- Backend Library
Group:          System/Libraries
Recommends:     %{name}

%description -n libgoa-backend-1_0-1
gnome-online-accounts provides interfaces so applications and
libraries in GNOME can access the user's online accounts.

%package devel
Summary:        GNOME service to access online accounts -- Development Files
Group:          Development/Libraries/GNOME
Requires:       libgoa-1_0-0 = %{version}
Requires:       libgoa-backend-1_0-1 = %{version}
Requires:       typelib-1_0-Goa-1_0 = %{version}

%description devel
gnome-online-accounts provides interfaces so applications and
libraries in GNOME can access the user's online accounts.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%configure \
        --disable-static \
        --enable-documentation \
        --enable-gtk-doc \
        --enable-exchange \
        --enable-facebook \
        --enable-flickr \
        --enable-foursquare \
        --enable-google \
        --enable-imap-smtp \
        --enable-kerberos \
        --disable-media-server \
        --enable-owncloud \
        --enable-windows-live \
        %{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}

%post -n libgoa-1_0-0 -p /sbin/ldconfig
%postun -n libgoa-1_0-0 -p /sbin/ldconfig
%post -n libgoa-backend-1_0-1 -p /sbin/ldconfig
%postun -n libgoa-backend-1_0-1 -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS
%{_libexecdir}/goa-daemon
%{_datadir}/dbus-1/services/org.gnome.OnlineAccounts.service
%{_datadir}/glib-2.0/schemas/org.gnome.online-accounts.gschema.xml
%{_datadir}/icons/hicolor/*/apps/goa-account*.svg
%{_mandir}/man8/goa-daemon.8%{?ext_man}
%dir %{_libdir}/goa-1.0
%dir %{_libdir}/goa-1.0/web-extensions
%{_libdir}/goa-1.0/web-extensions/libgoawebextension.so
%{_libexecdir}/goa-identity-service
%{_datadir}/dbus-1/services/org.gnome.Identity.service

%files -n libgoa-1_0-0
%{_libdir}/libgoa-1.0.so.*

%files -n typelib-1_0-Goa-1_0
%{_libdir}/girepository-1.0/Goa-1.0.typelib

%files -n libgoa-backend-1_0-1
%{_libdir}/libgoa-backend-1.0.so.*

%files devel
%doc %{_datadir}/gtk-doc/html/goa/
%{_includedir}/goa-1.0/
%dir %{_libdir}/goa-1.0
%{_libdir}/goa-1.0/include/
%{_libdir}/libgoa-1.0.so
%{_libdir}/libgoa-backend-1.0.so
%{_libdir}/pkgconfig/goa-1.0.pc
%{_libdir}/pkgconfig/goa-backend-1.0.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/goa-1.0.deps
%{_datadir}/vala/vapi/goa-1.0.vapi

%files lang -f %{name}.lang

%changelog
