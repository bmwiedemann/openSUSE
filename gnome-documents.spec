#
# spec file for package gnome-documents
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


%ifnarch x86_64 %{ix86} aarch64
# Remove reference to libreofficekit
%global __requires_exclude typelib\\(LOKDocView\\)
%endif
Name:           gnome-documents
Version:        3.33.90
Release:        0
Summary:        Document Manager for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Office/Other
URL:            https://wiki.gnome.org/Apps/Documents
Source0:        http://download.gnome.org/sources/gnome-documents/3.33/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gnome-shell
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(evince-document-3.0) >= 3.13.3
BuildRequires:  pkgconfig(evince-view-3.0) >= 3.13.3
BuildRequires:  pkgconfig(gjs-1.0) >= 1.48.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.39.3
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(goa-1.0) >= 3.2.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.31.6
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.15
BuildRequires:  pkgconfig(libgdata) >= 0.13.3
BuildRequires:  pkgconfig(libgepub-0.6) >= 0.6
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.41.3
BuildRequires:  pkgconfig(tracker-control-2.0) >= 0.17.3
BuildRequires:  pkgconfig(tracker-sparql-2.0) >= 0.17.3
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.6.0
BuildRequires:  pkgconfig(zapojit-0.0) >= 0.0.2
# This is a gjs application
Requires:       gjs
# If available, we query the Online Miners via dbus.
Recommends:     dbus(org.gnome.OnlineMiners.GData)
Provides:       gnome-documents_books-common = %{version}
Obsoletes:      gnome-documents_books-common < %{version}

%description
Documents is a document manager application for GNOME.

%package -n gnome-shell-search-provider-documents
Summary:        Document Manager for GNOME -- Search Provider for GNOME Shell
Group:          Productivity/Office/Other
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    packageand(%{name}:gnome-shell)

%description -n gnome-shell-search-provider-documents
Documents is a document manager application for GNOME.

This package contains a search provider to enable GNOME Shell to get
search results from documents.

%lang_package

%prep
%autosetup -p1
translation-update-upstream po %{name}

%build
%meson \
	-Ddocumentation=true \
	-Dgetting_started=false \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc AUTHORS NEWS README.md TODO
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/gnome-documents
%{_datadir}/gnome-documents/
%{_libdir}/gnome-documents/
%{_datadir}/applications/org.gnome.Documents.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.documents.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Documents.enums.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Documents*
%{_datadir}/metainfo/org.gnome.Documents.appdata.xml
%{_mandir}/man1/gnome-documents.1%{?ext_man}

%files -n gnome-shell-search-provider-documents
%{_datadir}/dbus-1/services/org.gnome.Documents.service
%{_datadir}/gnome-shell/search-providers/org.gnome.Documents.search-provider.ini

%files lang -f %{name}.lang

%changelog
