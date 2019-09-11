#
# spec file for package meteo
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           meteo
Version:        0.9.7
Release:        0
Summary:        Program to show the weather forecast of the next hours and days
License:        GPL-3.0-or-later
Group:          Productivity/Other
URL:            https://gitlab.com/bitseater
Source:         https://gitlab.com/bitseater/meteo/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxml2-tools
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(champlain-0.12)
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4) > 2.54.1
BuildRequires:  pkgconfig(webkit2gtk-4.0)
Recommends:     %{name}-lang
Provides:       weather = %{version}
Obsoletes:      weather < %{version}

%description
A program which displays current weather, with information about temperature,
pressure, wind speed and direction, as well as sunrise and sunset times.

%lang_package

%prep
%setup -q -n meteo-%{version}

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.gitlab.bitseater.meteo GTK Utility DesktopUtility
%find_lang com.gitlab.bitseater.meteo %{name}.lang
%fdupes %{buildroot}%{_datadir}

# dirlist HiDPI icons (see: hicolor/index.theme)
_dirlist=$PWD/dir.lst
pushd %{buildroot}
find ./ | while read _list; do
    echo $_list | grep '[0-9]\@[0-9]' || continue
    _path=$(echo $_list | sed 's/[^/]//')
    if ! ls ${_path%/*}; then
        grep -xqs "\%dir\ ${_path%/*}" $_dirlist || echo "%dir ${_path%/*}" >> $_dirlist
    fi
done
popd

%files -f dir.lst
%license COPYING
%doc AUTHORS README.md
%{_bindir}/com.gitlab.bitseater.meteo
%{_datadir}/applications/com.gitlab.bitseater.meteo.desktop
%{_datadir}/glib-2.0/schemas/com.gitlab.bitseater.meteo.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.gitlab.bitseater.meteo.??g
%{_datadir}/metainfo/com.gitlab.bitseater.meteo.appdata.xml

%files lang -f %{name}.lang

%changelog
