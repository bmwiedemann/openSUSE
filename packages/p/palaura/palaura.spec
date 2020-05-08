#
# spec file for package palaura
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


Name:           palaura
Version:        1.2.2
Release:        0
Summary:        A dictionary with word definitions
License:        GPL-3.0-or-later
Group:          Productivity/Office/Other
URL:            https://lainsce.us/
Source:         https://github.com/lainsce/palaura/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 5.1.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)

%description
palaura is a dictionary application featuring word definitions.
It uses the Oxford Dictionaries API for lookups.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.lainsce.palaura GTK Office Dictionary
%fdupes %{buildroot}/%{_datadir}

# dirlist HiDPI icons (see: hicolor/index.theme)
touch $PWD/dir.lst
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
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/com.github.lainsce.palaura
%{_datadir}/applications/com.github.lainsce.palaura.desktop
%{_datadir}/glib-2.0/schemas/com.github.lainsce.palaura.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.lainsce.palaura.??g
%{_datadir}/metainfo/com.github.lainsce.palaura.appdata.xml

%changelog
