#
# spec file for package evolution-data-server
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


%global with_docs 0

# Shared Library soNUMs, to make it easier for updates
%define so_camel 64
%define so_ebackend 11
%define so_edataserver 27
%define so_edataserverui 4
%define so_edataserverui4 0
%define so_ebook 21
%define so_ebook_contacts 4
%define so_edata_book 27
%define so_ecal 2
%define so_edata_cal 2
%bcond_without introspection

Name:           evolution-data-server
Version:        3.46.2
Release:        0
Summary:        Evolution Data Server
License:        LGPL-2.0-only
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Apps/Evolution
Source0:        https://download.gnome.org/sources/evolution-data-server/3.46/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  db-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gperf
BuildRequires:  gtk-doc >= 1.9
BuildRequires:  intltool
BuildRequires:  krb5-devel
BuildRequires:  mozilla-nss-devel
BuildRequires:  nss-shared-helper-devel
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libical) >= 3.0.5
BuildRequires:  pkgconfig(libical-glib) >= 3.0.7
# For adressbook data generating
BuildRequires:  python3-base
BuildRequires:  libboost_thread-devel
BuildRequires:  libphonenumber-devel
BuildRequires:  sqlite3-devel >= 3.7.17
BuildRequires:  vala >= 0.22.0
BuildRequires:  pkgconfig(goa-1.0) >= 3.8
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16
BuildRequires:  pkgconfig(gweather4) >= 3.91
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.0.4
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.25
BuildRequires:  pkgconfig(libnotify) >= 0.7
BuildRequires:  pkgconfig(libsecret-unstable) >= 0.5
BuildRequires:  pkgconfig(libsoup-3.0) >= 2.58
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(protobuf) >= 2.4
BuildRequires:  pkgconfig(webkit2gtk-4.1) >= 2.34.0
BuildRequires:  pkgconfig(webkit2gtk-5.0) >= 2.36.0
Requires:       mozilla-nss
# typelib-1_0-ECalendar-1_2 was dropped with e-d-s 3.7.3 due to libical not being introspecatble.
Obsoletes:      typelib-1_0-ECalendar-1_2 <= %{version}

%description
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

%package -n libcamel-1_2-%{so_camel}
Summary:        Evolution Data Server's Messaging Library
Group:          System/Libraries

%description -n libcamel-1_2-%{so_camel}
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package contains a shared system library for messaging.

%package -n libebackend-1_2-%{so_ebackend}
Summary:        Evolution Data Server's Backend Utilities Library
Group:          System/Libraries

%description -n libebackend-1_2-%{so_ebackend}
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package contains a shared system library for backends.

%package -n libebook-1_2-%{so_ebook}
Summary:        Evolution Data Server's Address Book Client Library
Group:          System/Libraries

%description -n libebook-1_2-%{so_ebook}
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package contains a shared system library to access address books.

%package -n libebook-contacts-1_2-%{so_ebook_contacts}
Summary:        Evolution Data Server's Address Book Client Library
Group:          System/Libraries

%description -n libebook-contacts-1_2-%{so_ebook_contacts}
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package contains a shared system library to access address books.

%package -n libecal-2_0-%{so_ecal}
Summary:        Evolution Data Server's Calendar Client Library
Group:          System/Libraries

%description -n libecal-2_0-%{so_ecal}
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package contains a shared system library to access calendars.

%package -n libedata-book-1_2-%{so_edata_book}
Summary:        Evolution Data Server's Address Book Backend Library
Group:          System/Libraries

%description -n libedata-book-1_2-%{so_edata_book}
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package contains a shared system library for address book backends.

%package -n typelib-1_0-Camel-1_2
Summary:        Introspection bindings for Evolution Data Server's Messaging Library
Group:          System/Libraries

%description -n typelib-1_0-Camel-1_2
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package provides the GObject Introspection bindings for library for messaging.

%package -n typelib-1_0-EBook-1_2
Summary:        Introspection bindings for Evolution Data Server's Address Book Backend Library
Group:          System/Libraries

%description -n typelib-1_0-EBook-1_2
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package provides the GObject Introspection bindings for the library
for address book backends.

%package -n typelib-1_0-EBookContacts-1_2
Summary:        Introspection bindings for Evolution Data Server's Address Book Backend Library
Group:          System/Libraries

%description -n typelib-1_0-EBookContacts-1_2
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package provides the GObject Introspection bindings for the library
for address book backends.

%package -n libedata-cal-2_0-%{so_edata_cal}
Summary:        Evolution Data Server's Calendar Backend Library
Group:          System/Libraries

%description -n libedata-cal-2_0-%{so_edata_cal}
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package contains a shared system library for calendar backends.

%package -n libedataserver-1_2-%{so_edataserver}
Summary:        Evolution Data Server's Utilities Library
# libedataserver references the gsettings schemas, which live in e-d-s package
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libedataserver-1_2-%{so_edataserver}
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package contains a shared system library.

%package -n libedataserverui-1_2-%{so_edataserverui}
Summary:        Evolution Data Server's Utilities Library
Group:          System/Libraries

%description -n libedataserverui-1_2-%{so_edataserverui}
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package contains a shared system library.

%package -n libedataserverui4-1_0-%{so_edataserverui4}
Summary:        Evolution Data Server's Utilities Library
Group:          System/Libraries

%description -n libedataserverui4-1_0-%{so_edataserverui4}
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package contains a shared system library.

%package -n typelib-1_0-EBackend-1_2
Summary:        Introspection bindings for Evolution Data Server's Utilities Library
Group:          System/Libraries

%description -n typelib-1_0-EBackend-1_2
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

%package -n typelib-1_0-ECal-2_0
Summary:        Introspection bindings for Evolution Data Server's Utilities Library
Group:          System/Libraries

%description -n typelib-1_0-ECal-2_0
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

%package -n typelib-1_0-EDataBook-1_2
Summary:        Introspection bindings for Evolution Data Server's Utilities Library
Group:          System/Libraries

%description -n typelib-1_0-EDataBook-1_2
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

%package -n typelib-1_0-EDataCal-2_0
Summary:        Introspection bindings for Evolution Data Server's Utilities Library
Group:          System/Libraries

%description -n typelib-1_0-EDataCal-2_0
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

%package -n typelib-1_0-EDataServer-1_2
Summary:        Introspection bindings for Evolution Data Server's Utilities Library
Group:          System/Libraries

%description -n typelib-1_0-EDataServer-1_2
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package provides the GObject Introspection bindings for the
libedataserver library.

%package -n typelib-1_0-EDataServerUI-1_2
Summary:        Introspection bindings for Evolution Data Server's Utilities Library
Group:          System/Libraries

%description -n typelib-1_0-EDataServerUI-1_2
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package provides the GObject Introspection bindings for the
libedataserver library.

%package -n typelib-1_0-EDataServerUI4-1_0
Summary:        Introspection bindings for Evolution Data Server's Utilities Library
Group:          System/Libraries

%description -n typelib-1_0-EDataServerUI4-1_0
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package provides the GObject Introspection bindings for the
libedataserver library.

%package devel
Summary:        Development files for Evolution Data Server
Group:          Development/Libraries/GNOME
Requires:       evolution-data-server = %{?epoch:}%{version}
Requires:       libcamel-1_2-%{so_camel} = %{version}
Requires:       libebackend-1_2-%{so_ebackend} = %{version}
Requires:       libebook-1_2-%{so_ebook} = %{version}
Requires:       libebook-contacts-1_2-%{so_ebook_contacts} = %{version}
Requires:       libecal-2_0-%{so_ecal} = %{version}
Requires:       libedata-book-1_2-%{so_edata_book} = %{version}
Requires:       libedata-cal-2_0-%{so_edata_cal} = %{version}
Requires:       libedataserver-1_2-%{so_edataserver} = %{version}
Requires:       libedataserverui-1_2-%{so_edataserverui} = %{version}
Requires:       libedataserverui4-1_0-%{so_edataserverui4} = %{version}
Requires:       openldap2-devel
%if %{?with_introspection}
Requires:       typelib-1_0-Camel-1_2 = %{version}
Requires:       typelib-1_0-EBook-1_2 = %{version}
Requires:       typelib-1_0-EBookContacts-1_2 = %{version}
Requires:       typelib-1_0-EDataServer-1_2 = %{version}
Requires:       typelib-1_0-EDataServerUI-1_2 = %{version}
Requires:       typelib-1_0-EDataServerUI4-1_0 = %{version}
%endif

%description devel
The Evolution Data Server development files provide the necessary
libraries, headers, and other files for developing applications which
use the Evolution Data Server for storing contact and calendar
information.

%if %{with_docs}
%package doc
Summary:        Developer documentation for Evolution Data Server
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}

%description doc
Evolution Data Server provides a central location for your address book
and calendar in the GNOME Desktop.

This package contains developer documentation.
%endif

%lang_package

%prep
%autosetup -p1

%build
%if %{with_docs}
%define gtkdoc_flags -DENABLE_GTK_DOC=ON
%else
%define gtkdoc_flags -DENABLE_GTK_DOC=OFF
%endif

%cmake -G "Unix Makefiles" \
    -DLIBEXEC_INSTALL_DIR=%{_libexecdir}/evolution-data-server \
    -DENABLE_MAINTAINER_MODE=OFF \
    -DENABLE_GTK_DOC=ON \
    -DENABLE_IPV6=ON \
    -DENABLE_SMIME=ON \
    -DENABLE_UOA=OFF \
    -DCMAKE_SKIP_INSTALL_RPATH=OFF \
    %{?with_introspection:\
    -DENABLE_VALA_BINDINGS=ON \
    -DENABLE_INTROSPECTION=ON} \
    -DWITH_PHONENUMBER=ON \
    -DENABLE_DBUS_SESSION_TOOL=OFF \
    %gtkdoc_flags \
    %{nil}
%cmake_build

%install
%cmake_install
%find_lang evolution-data-server
%fdupes %{buildroot}/%{_prefix}

%ldconfig_scriptlets -n libcamel-1_2-%{so_camel}
%ldconfig_scriptlets -n libebackend-1_2-%{so_ebackend}
%ldconfig_scriptlets -n libebook-1_2-%{so_ebook}
%ldconfig_scriptlets -n libebook-contacts-1_2-%{so_ebook_contacts}
%ldconfig_scriptlets -n libecal-2_0-%{so_ecal}
%ldconfig_scriptlets -n libedata-book-1_2-%{so_edata_book}
%ldconfig_scriptlets -n libedata-cal-2_0-%{so_edata_cal}
%ldconfig_scriptlets -n libedataserver-1_2-%{so_edataserver}
%ldconfig_scriptlets -n libedataserverui-1_2-%{so_edataserverui}
%ldconfig_scriptlets -n libedataserverui4-1_0-%{so_edataserverui4}

%files
%license COPYING
%doc NEWS README
%{_datadir}/evolution-data-server/
%{_datadir}/GConf/gsettings/evolution-data-server.convert
%{_datadir}/glib-2.0/schemas/org.gnome.Evolution.DefaultSources.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.eds-shell.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.shell.network-config.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution-data-server.addressbook.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution-data-server.calendar.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution-data-server.gschema.xml
# Category icons that are used by libedataserver
%{_datadir}/pixmaps/evolution-data-server/
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.*.service
%{_libdir}/evolution-data-server/
%if "%{_libdir}" != "%{_libexecdir}"
%{_libexecdir}/evolution-data-server/
%endif
%{_userunitdir}/evolution-addressbook-factory.service
%{_userunitdir}/evolution-calendar-factory.service
%{_userunitdir}/evolution-source-registry.service
%{_userunitdir}/evolution-user-prompter.service
%{_sysconfdir}/xdg/autostart/org.gnome.Evolution-alarm-notify.desktop
%{_datadir}/applications/org.gnome.Evolution-alarm-notify.desktop

%files -n libcamel-1_2-%{so_camel}
%{_libdir}/libcamel-1.2.so.%{so_camel}*

%files -n libebackend-1_2-%{so_ebackend}
%{_libdir}/libebackend-1.2.so.%{so_ebackend}*

%files -n libebook-1_2-%{so_ebook}
%{_libdir}/libebook-1.2.so.%{so_ebook}*

%files -n libebook-contacts-1_2-%{so_ebook_contacts}
%{_libdir}/libebook-contacts-1.2.so.%{so_ebook_contacts}*

%files -n libecal-2_0-%{so_ecal}
%{_libdir}/libecal-2.0.so.%{so_ecal}*

%files -n libedata-book-1_2-%{so_edata_book}
%{_libdir}/libedata-book-1.2.so.%{so_edata_book}*

%if %{with introspection}
%files -n typelib-1_0-Camel-1_2
%{_libdir}/girepository-1.0/Camel-1.2.typelib

%files -n typelib-1_0-EBackend-1_2
%{_libdir}/girepository-1.0/EBackend-1.2.typelib

%files -n typelib-1_0-EBook-1_2
%{_libdir}/girepository-1.0/EBook-1.2.typelib

%files -n typelib-1_0-EBookContacts-1_2
%{_libdir}/girepository-1.0/EBookContacts-1.2.typelib

%files -n typelib-1_0-ECal-2_0
%{_libdir}/girepository-1.0/ECal-2.0.typelib

%files -n typelib-1_0-EDataBook-1_2
%{_libdir}/girepository-1.0/EDataBook-1.2.typelib

%files -n typelib-1_0-EDataCal-2_0
%{_libdir}/girepository-1.0/EDataCal-2.0.typelib

%files -n typelib-1_0-EDataServer-1_2
%{_libdir}/girepository-1.0/EDataServer-1.2.typelib

%files -n typelib-1_0-EDataServerUI-1_2
%{_libdir}/girepository-1.0/EDataServerUI-1.2.typelib

%files -n typelib-1_0-EDataServerUI4-1_0
%{_libdir}/girepository-1.0/EDataServerUI4-1.0.typelib

%endif

%files -n libedata-cal-2_0-%{so_edata_cal}
%{_libdir}/libedata-cal-2.0.so.%{so_edata_cal}*

%files -n libedataserver-1_2-%{so_edataserver}
%{_libdir}/libedataserver-1.2.so.%{so_edataserver}*

%files -n libedataserverui-1_2-%{so_edataserverui}
%{_libdir}/libedataserverui-1.2.so.%{so_edataserverui}*

%files -n libedataserverui4-1_0-%{so_edataserverui4}
%{_libdir}/libedataserverui4-1.0.so.%{so_edataserverui4}*

%files devel
%doc ChangeLog MAINTAINERS
%{_includedir}/evolution-data-server/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%if %{with introspection}
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi
%endif

%if %{with_docs}
%files doc
%{_datadir}/gtk-doc/html/*
%endif

%files lang -f evolution-data-server.lang

%changelog
