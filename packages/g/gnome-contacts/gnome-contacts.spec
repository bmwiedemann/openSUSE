#
# spec file for package gnome-contacts
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


%define eds_version 3.42
%define folks_version 0.14
%define glib_version 2.64

Name:           gnome-contacts
Version:        47.1.1
Release:        0
Summary:        Contacts Manager for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Office/Other
URL:            https://wiki.gnome.org/Apps/Contacts
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  desktop-file-utils
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook_4
BuildRequires:  meson >= 0.50
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.56.11
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(folks) >= %{folks_version}
BuildRequires:  pkgconfig(folks-eds) >= %{folks_version}
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(geocode-glib-1.0) >= 3.15.3
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gmodule-export-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.12
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4.alpha
BuildRequires:  pkgconfig(libebook-1.2) >= %{eds_version}
BuildRequires:  pkgconfig(libedataserver-1.2) >= %{eds_version}
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk4) >= 0.6
BuildRequires:  pkgconfig(libqrencode) >= 4.1.1

%description
The integraded address book for GNOME.

Among its features are:

 * Search for and view contacts;
 * Edit contact details and make new contacts;
 * Integration with online address books;
 * Automatic linking of contacts from different online sources.

%package -n gnome-shell-search-provider-contacts
Summary:        Contacts Manager for GNOME -- Search Provider for GNOME Shell
Group:          Productivity/Office/Other
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    (%{name} and gnome-shell)

%description -n gnome-shell-search-provider-contacts
The integraded address book for GNOME.

Among its features are:

 * Search for and view contacts;
 * Edit contact details and make new contacts;
 * Integration with online address books;
 * Automatic linking of contacts from different online sources.

This package contains a search provider to enable GNOME Shell to get
search results from contacts.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dmanpage=true \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_mandir}/man1/gnome-contacts.1%{ext_man}
%{_bindir}/gnome-contacts
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.Contacts.appdata.xml
%{_datadir}/applications/org.gnome.Contacts.desktop
%{_datadir}/dbus-1/services/org.gnome.Contacts.service
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
%{_datadir}/icons/hicolor/*/*/org.gnome.Contacts*
%dir %{_libexecdir}/gnome-contacts
%{_libexecdir}/gnome-contacts/gnome-contacts-parser

%files -n gnome-shell-search-provider-contacts
%{_datadir}/dbus-1/services/org.gnome.Contacts.SearchProvider.service
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Contacts.search-provider.ini
%{_libexecdir}/gnome-contacts-search-provider

%files lang -f %{name}.lang

%changelog
