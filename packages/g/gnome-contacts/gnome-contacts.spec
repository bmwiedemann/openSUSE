#
# spec file for package gnome-contacts
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


Name:           gnome-contacts
Version:        3.36.2
Release:        0
Summary:        Contacts Manager for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Office/Other
URL:            https://wiki.gnome.org/Apps/Contacts
Source0:        https://download.gnome.org/sources/gnome-contacts/3.36/%{name}-%{version}.tar.xz

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook_4
BuildRequires:  meson >= 0.50
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  vala
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(cheese)
BuildRequires:  pkgconfig(cheese-gtk) >= 3.3.91
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(folks) >= 0.11.4
BuildRequires:  pkgconfig(folks-eds) >= 0.11.4
# Disable telepathy by default
#BuildRequires:  pkgconfig(folks-telepathy) >= 0.11.4
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(geocode-glib-1.0) >= 3.15.3
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.44.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gmodule-export-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libebook-1.2) >= 3.13.90
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.13.90
BuildRequires:  pkgconfig(libedataserverui-1.2) >= 3.13.90
BuildRequires:  pkgconfig(libhandy-0.0) >= 0.0.9
# Disable telepathy by default, following upstream, NOTE pass -Dtelepathy=true to meson if you reenable this.
#BuildRequires:  pkgconfig(telepathy-glib) >= 0.22.0

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
Supplements:    packageand(%{name}:gnome-shell)

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
# t-u-u disabled since 3.35.x - execution failure
#translation-update-upstream

%build
%meson \
	-Dwith-cheese=yes \
	-Dwith-manpage=true \
	-Dmaps=true \
	-Dtelepathy=false \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_mandir}/man1/gnome-contacts.1%{ext_man}
%{_bindir}/gnome-contacts
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.Contacts.appdata.xml
%{_datadir}/applications/org.gnome.Contacts.desktop
%{_datadir}/dbus-1/services/org.gnome.Contacts.service
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
%{_datadir}/icons/hicolor/*/*/org.gnome.Contacts*

%files -n gnome-shell-search-provider-contacts
%{_datadir}/dbus-1/services/org.gnome.Contacts.SearchProvider.service
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Contacts.search-provider.ini
%{_libexecdir}/gnome-contacts-search-provider

%files lang -f %{name}.lang

%changelog
