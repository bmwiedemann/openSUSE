#
# spec file for package ciano
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ciano
Version:        0.2.1
Release:        0
Summary:        A multimedia file converter
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://robertsanseries.github.io/ciano
Source:         https://github.com/robertsanseries/ciano/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gettext-runtime >= 0.19.7
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
Requires:       ImageMagick
Requires:       ffmpeg
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
A program to convert your multimedia files to contemporary formats.

%lang_package

%prep
%setup -q

sed -i 's/\bmetainfo\b/appdata/' $(grep -rwl 'metainfo')

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.robertsanseries.ciano GTK AudioVideo Video AudioVideoEditing
%find_lang com.github.robertsanseries.ciano %{name}.lang
%fdupes %{buildroot}/%{_datadir}

%files
%doc AUTHORS LICENSE* README.md
%{_bindir}/com.github.robertsanseries.ciano
%dir %{_datadir}/appdata
%{_datadir}/appdata/com.github.robertsanseries.ciano.appdata.xml
%{_datadir}/applications/com.github.robertsanseries.ciano.desktop
%{_datadir}/ciano/
%{_datadir}/glib-2.0/schemas/com.github.robertsanseries.ciano.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.robertsanseries.ciano.??g
%{_datadir}/pixmaps/com.github.robertsanseries.ciano.??g

%files lang -f %{name}.lang

%changelog
