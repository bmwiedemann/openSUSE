#
# spec file for package gtranslator
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


Name:           gtranslator
Version:        3.32.1
Release:        0
Summary:        A gettext po file editor for the GNOME desktop
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://wiki.gnome.org/Apps/Gtranslator
Source:         https://download.gnome.org/sources/gtranslator/3.32/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  meson >= 0.46.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-2.0) >= 2.36.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gspell-1) >= 1.2.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.20
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(gtksourceview-4) >= 4.0.2
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.0
BuildRequires:  pkgconfig(libgda-5.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.12
Requires:       gsettings-desktop-schemas
Requires:       iso-codes
Requires:       libgda-5_0-sqlite
Recommends:     %{name}-lang
Obsoletes:      gtranslator-devel <= 2.91.7

%description
Gtranslator is a ".po" file editor with many bells and whistles.
It features many functions which aid in the work of translators of po
files imminently.

%lang_package

%prep
%setup -q

%build
%meson \
	-D gtk_doc=true
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "gtr-marshal.h" -delete -print
%suse_update_desktop_file -r org.gnome.Gtranslator GNOME GTK Development Translation
%find_lang %{name}

%files
%license COPYING
%doc AUTHORS MAINTAINERS NEWS README.md THANKS
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_mandir}/man?/*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Gtranslator*.svg
%{_datadir}/metainfo/org.gnome.Gtranslator.appdata.xml
%{_datadir}/pixmaps/gtranslator-*.png

%files lang -f %{name}.lang

%changelog
