#
# spec file for package gnome-books
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


Name:           gnome-books
Version:        3.32.0
Release:        0
Summary:        An e-book manager application for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/Other
URL:            https://wiki.gnome.org/Apps/Books
Source0:        https://download.gnome.org/sources/%{name}/3.32/%{name}-%{version}.tar.xz

BuildRequires:  gnome-shell
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  meson >= 0.42.0
BuildRequires:  pkgconfig
BuildRequires:  poppler-tools
BuildRequires:  pkgconfig(evince-document-3.0) >= 3.13.3
BuildRequires:  pkgconfig(evince-view-3.0) >= 3.13.3
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.39.3
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.31.6
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.15
BuildRequires:  pkgconfig(libgepub-0.6)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(tracker-control-2.0) >= 0.17.3
BuildRequires:  pkgconfig(tracker-sparql-2.0) >= 0.17.3
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.6.0

%description
Books is an e-book manager application for GNOME.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc README
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/girepository-1.0
%{_libdir}/%{name}/girepository-1.0/Gd-1.0.typelib
%{_libdir}/%{name}/girepository-1.0/GdPrivate-1.0.typelib
%{_libdir}/%{name}/libgd.so
%{_libdir}/%{name}/libgdprivate-1.0.so
%{_datadir}/applications/org.gnome.Books.desktop
%{_datadir}/dbus-1/services/org.gnome.Books.service
%{_datadir}/glib-2.0/schemas/org.gnome.Books.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.books.gschema.xml
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/gir-1.0
%{_datadir}/%{name}/gir-1.0/Gd-1.0.gir
%{_datadir}/%{name}/gir-1.0/GdPrivate-1.0.gir
%{_datadir}/%{name}/org.gnome.Books
%{_datadir}/%{name}/org.gnome.Books.data.gresource
%{_datadir}/%{name}/org.gnome.Books.src.gresource
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Books.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Books-symbolic.svg
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/metainfo/org.gnome.Books.appdata.xml

%files lang -f %{name}.lang

%changelog
