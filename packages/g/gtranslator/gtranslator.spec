#
# spec file for package gtranslator
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


Name:           gtranslator
Version:        42.0
Release:        0
Summary:        A gettext po file editor for the GNOME desktop
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://wiki.gnome.org/Apps/Gtranslator
Source0:        https://download.gnome.org/sources/gtranslator/42/%{name}-%{version}.tar.xz
Source99:       gtranslator-rpmlintrc

BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  meson >= 0.46.0
BuildRequires:  pkgconfig
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
BuildRequires:  pkgconfig(libdazzle-1.0) >= 3.33.90
BuildRequires:  pkgconfig(libgda-6.0) >= 6.0.0
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.12
Requires:       gsettings-desktop-schemas
Requires:       iso-codes
Requires:       libgda-sqlite >= 6.0.0
Obsoletes:      gtranslator-devel <= 2.91.7

%description
Gtranslator is an enhanced gettext PO file editor for the GNOME desktop environment. It handles all forms of gettext PO files and features many comfortable everyday usage features like find and replace functions, auto translation, and translation learning.

%package doc
Summary:        Documentation for %{name}
Group:          Development/Tools/Other

%description doc
This package contains documentation for %{name}.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D gtk_doc=true
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "gtr-marshal.h" -delete -print
%find_lang %{name}
%fdupes %{buildroot}%{_prefix}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/gtksourceview-4/language-specs/*.lang
%{_datadir}/icons/hicolor/*/apps/org.gnome.Gtranslator*.svg
%{_datadir}/metainfo/org.gnome.Gtranslator.appdata.xml
%{_mandir}/man?/*

%files doc
%doc AUTHORS MAINTAINERS NEWS THANKS
%doc %{_datadir}/gtk-doc/html/%{name}/

%files lang -f %{name}.lang

%changelog
