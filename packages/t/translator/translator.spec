#
# spec file for package translator
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


Name:           translator
Version:        1.4.1
Release:        0
Summary:        Translation program
License:        GPL-3.0-or-later
Group:          Productivity/Office/Dictionary
URL:            https://rapidfingers.github.io/Translator
Source:         https://github.com/RapidFingers/Translator/archive/%{version}.tar.gz#/Translator-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.28
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.3
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
Recommends:     %{name}-lang

%description
This is a translator. It is suited only for small messages, not
big text. Google Translate is used as a backend.

%lang_package

%prep
%setup -q -n Translator-%{version}

cp debian/copyright COPYING

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.rapidfingers.translator GTK Office Dictionary
%find_lang com.github.rapidfingers.translator %{name}.lang
%fdupes %{buildroot}%{_datadir}

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
%license COPYING
%doc README.md
%{_bindir}/com.github.rapidfingers.translator
%{_datadir}/applications/com.github.rapidfingers.translator.desktop
%{_datadir}/glib-2.0/schemas/com.github.rapidfingers.translator.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.rapidfingers.translator.??g
%{_datadir}/metainfo/com.github.rapidfingers.translator.appdata.xml

%files lang -f %{name}.lang

%changelog
