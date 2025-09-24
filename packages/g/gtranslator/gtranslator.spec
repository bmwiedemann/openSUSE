#
# spec file for package gtranslator
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        49.0
Release:        0
Summary:        A gettext po file editor for the GNOME desktop
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://wiki.gnome.org/Apps/Gtranslator
Source0:        %{name}-%{version}.tar.zst
Source99:       gtranslator-rpmlintrc

BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  meson >= 0.46.0
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-2.0) >= 2.36.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.76
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gthread-2.0) >= 2.13.0
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(gtk4) >= 4.12.0
BuildRequires:  pkgconfig(gtksourceview-5) >= 5.4.0
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.8.alpha
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.12
BuildRequires:  pkgconfig(sqlite3)
Requires:       gsettings-desktop-schemas
Requires:       iso-codes
Requires:       libadwaita-1-0 >= 1.5.0
Requires:       libgda-sqlite >= 6.0.0
Obsoletes:      gtranslator-devel <= 2.91.7

%description
Gtranslator is an enhanced gettext PO file editor for the GNOME desktop environment. It handles all forms of gettext PO files and features many comfortable everyday usage features like find and replace functions, auto translation, and translation learning.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "gtr-marshal.h" -delete -print
%find_lang %{name}
%fdupes %{buildroot}%{_prefix}

%check
%meson_test

%files
%license COPYING
%doc README.md
%doc AUTHORS MAINTAINERS NEWS THANKS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gnome.Gtranslator.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/gtksourceview-5/language-specs/*.lang
%{_datadir}/icons/hicolor/*/apps/org.gnome.Gtranslator*.svg
%{_datadir}/metainfo/org.gnome.Gtranslator.appdata.xml
%{_mandir}/man?/*

%files lang -f %{name}.lang

%changelog
