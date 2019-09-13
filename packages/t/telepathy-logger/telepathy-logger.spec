#
# spec file for package telepathy-logger
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


Name:           telepathy-logger
Version:        0.8.2
Release:        0
Summary:        Centralized Logging for the Telepathy Framework
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
Url:            http://telepathy.freedesktop.org/wiki/Logger
Source:         http://telepathy.freedesktop.org/releases/telepathy-logger/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM telepathy-logger-tests-Rename-function.patch zaitor@opensuse.org -- Fix build
Patch0:         telepathy-logger-tests-Rename-function.patch
# PATCH-FIx-UPSTREAM libtpl-extensions-dependencies.patch gh#TelepathyIM/telepathy-logger#2 dimstar@opensuse.org -- Fix dependencies of tpl-extensions
Patch1:         libtpl-extensions-dependencies.patch
BuildRequires:  gnome-doc-utils-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  python2-devel
BuildRequires:  python2-xml
BuildRequires:  pkgconfig(dbus-1) >= 1.1.0
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.82
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(telepathy-glib) >= 0.19.2
%glib2_gsettings_schema_requires

%description
tp-logger is a headless Observer client that logs information received by the
Telepathy framework. It features pluggable backends to log different sorts of
messages, in different formats.

tp-logger features a Telepathy-style D-Bus API to expose logs and interesting
information related to logging (most frequent contacts, etc.). It also provides
a GLib-compatible client API for making bulk log requests (e.g. for display
logs in applications without having to provide lots of information over D-Bus).

%package devel
Summary:        Development files for the Telepathy Framework Centralized Logging
Group:          Development/Languages/C and C++
Requires:       libtelepathy-logger3 = %{version}
Requires:       libtpl-extensions3 = %{version}
Requires:       typelib-1_0-TelepathyLogger-0_2 = %{version}

%description devel
tp-logger is a headless Observer client that logs information received by the
Telepathy framework. It features pluggable backends to log different sorts of
messages, in different formats.

tp-logger features a Telepathy-style D-Bus API to expose logs and interesting
information related to logging (most frequent contacts, etc.). It also provides
a GLib-compatible client API for making bulk log requests (e.g. for display
logs in applications without having to provide lots of information over D-Bus).

%package -n libtelepathy-logger3
Summary:        Centralized Logging for the Telepathy Framework
Group:          System/Libraries

%description -n libtelepathy-logger3
tp-logger is a headless Observer client that logs information received by the
Telepathy framework. It features pluggable backends to log different sorts of
messages, in different formats.

tp-logger features a Telepathy-style D-Bus API to expose logs and interesting
information related to logging (most frequent contacts, etc.). It also provides
a GLib-compatible client API for making bulk log requests (e.g. for display
logs in applications without having to provide lots of information over D-Bus).

%package -n typelib-1_0-TelepathyLogger-0_2
Summary:        Introspection bindings for the Telepathy Framework Centralized Logging
Group:          System/Libraries

%description -n typelib-1_0-TelepathyLogger-0_2
tp-logger is a headless Observer client that logs information received by the
Telepathy framework. It features pluggable backends to log different sorts of
messages, in different formats.

tp-logger features a Telepathy-style D-Bus API to expose logs and interesting
information related to logging (most frequent contacts, etc.). It also provides
a GLib-compatible client API for making bulk log requests (e.g. for display
logs in applications without having to provide lots of information over D-Bus).

This package provides the GObject Introspection bindings for Telepathy Logger.

%package -n libtpl-extensions3
Summary:        Extensions for the Telepathy Framework Centralized Logging
Group:          System/Libraries

%description -n libtpl-extensions3
tp-logger is a headless Observer client that logs information received by the
Telepathy framework. It features pluggable backends to log different sorts of
messages, in different formats.

tp-logger features a Telepathy-style D-Bus API to expose logs and interesting
information related to logging (most frequent contacts, etc.). It also provides
a GLib-compatible client API for making bulk log requests (e.g. for display
logs in applications without having to provide lots of information over D-Bus).

%prep
%autosetup -p1

%build
%configure \
  --disable-static \
  --enable-public-extensions
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post
%glib2_gsettings_schema_post

%postun
%glib2_gsettings_schema_postun

%post -n libtelepathy-logger3 -p /sbin/ldconfig
%postun -n libtelepathy-logger3 -p /sbin/ldconfig
%post -n libtpl-extensions3 -p /sbin/ldconfig
%postun -n libtpl-extensions3 -p /sbin/ldconfig

%files
%{_libexecdir}/telepathy-logger
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Logger.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Logger.service
%{_datadir}/glib-2.0/schemas/org.freedesktop.Telepathy.Logger.gschema.xml
%dir %{_datadir}/telepathy
%dir %{_datadir}/telepathy/clients
%{_datadir}/telepathy/clients/Logger.client

%files -n libtelepathy-logger3
%{_libdir}/libtelepathy-logger.so.*

%files -n typelib-1_0-TelepathyLogger-0_2
%{_libdir}/girepository-1.0/TelepathyLogger-0.2.typelib

%files -n libtpl-extensions3
%{_libdir}/libtpl-extensions.so.*

%files devel
%{_includedir}/telepathy-logger-0.2/
%{_includedir}/tpl-extensions/
%{_libdir}/pkgconfig/telepathy-logger-0.2.pc
%{_libdir}/libtelepathy-logger.so
%{_libdir}/libtpl-extensions.so
%{_libdir}/pkgconfig/tpl-extensions.pc
%{_datadir}/gtk-doc/html/telepathy-logger/
%{_datadir}/gir-1.0/TelepathyLogger-0.2.gir

%changelog
