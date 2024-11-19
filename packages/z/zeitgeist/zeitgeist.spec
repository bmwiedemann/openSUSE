#
# spec file for package zeitgeist
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2009 Dominique Leuenberger, Amsterdam, The Netherlands.
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


Name:           zeitgeist
Version:        1.0.4
Release:        0
Summary:        Zeitgeist Engine
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://gitlab.freedesktop.org/zeitgeist/zeitgeist
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-rdflib
BuildRequires:  python3-xml
BuildRequires:  raptor
BuildRequires:  vala
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(telepathy-glib)
BuildRequires:  pkgconfig(xapian-core)
Requires:       python3-xdg
Requires:       python3-xml

%description
Zeitgeist is a service that logs the users activity. The log can be
queried and managed in various ways over a DBus API.

This is the Zeitgeist backend engine.

%package -n libzeitgeist-2_0-0
Summary:        Client library for interacting with the Zeitgeist daemon
License:        LGPL-2.1-or-later

%description -n libzeitgeist-2_0-0
Libzeitgeist is a client library for interacting with the Zeitgeist
daemon.

This package provides the client library for Zeitgeist.

%package -n typelib-1_0-Zeitgeist-2_0
Summary:        Introspection bindings for Zeitgeist client library
License:        LGPL-2.1-or-later

%description -n typelib-1_0-Zeitgeist-2_0
Libzeitgeist is a client library for interacting with the Zeitgeist
daemon.

This package provides the Introspection bindings for Zeitgeist.

%package devel
Summary:        Development files for Zeitgeist client library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Requires:       libzeitgeist-2_0-0 = %{version}
Requires:       typelib-1_0-Zeitgeist-2_0 = %{version}

%description devel
Libzeitgeist is a client library for interacting with the Zeitgeist
daemon.

This package provides the necessary files for development with Zeitgeist.

%prep
%autosetup -n %{name}-v%{version}

%build
./autogen.sh
%configure \
  --enable-fts
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# We have the NEWS and AUTHORS in package doc
rm -rf %{buildroot}%{_datadir}/%{name}/doc
%fdupes %{buildroot}%{python3_sitelib}

%ldconfig_scriptlets -n libzeitgeist-2_0-0

%files
%doc AUTHORS NEWS
%{_bindir}/zeitgeist*
%{python3_sitelib}/zeitgeist/
%{_mandir}/man?/*%{ext_man}
%{_datadir}/zeitgeist/
%{_datadir}/dbus-1/services/org.gnome.zeitgeist.SimpleIndexer.service
%{_datadir}/dbus-1/services/org.gnome.zeitgeist.Engine.service
%{_userunitdir}/zeitgeist.service
%{_userunitdir}/zeitgeist-fts.service
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/zeitgeist-fts
%{_datadir}/bash-completion/completions/zeitgeist-daemon
%{_sysconfdir}/xdg/autostart/zeitgeist-datahub.desktop

%files -n libzeitgeist-2_0-0
%license COPYING
%{_libdir}/libzeitgeist-2.0.so.*

%files -n typelib-1_0-Zeitgeist-2_0
%{_libdir}/girepository-1.0/Zeitgeist-2.0.typelib

%files devel
%license COPYING.GPL
%{_includedir}/zeitgeist-2.0
%{_libdir}/libzeitgeist-2.0.so
%{_libdir}/pkgconfig/zeitgeist-2.0.pc
%{_datadir}/gir-1.0/Zeitgeist-2.0.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/zeitgeist*

%changelog
