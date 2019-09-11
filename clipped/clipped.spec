#
# spec file for package clipped
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


Name:           clipped
Version:        1.1.1
Release:        0
Summary:        Clipboard Manager
License:        GPL-2.0-only
Group:          System/GUI/Other
URL:            https://github.com/davidmhewitt/clipped
Source:         https://github.com/davidmhewitt/clipped/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.28.0
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
Recommends:     %{name}-lang

%description
Clipboard history manager for Elementary OS.

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.davidmhewitt.clipped Utility DesktopUtility
%find_lang com.github.davidmhewitt.clipped %{name}.lang
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
%doc AUTHORS README*
%{_bindir}/com.github.davidmhewitt.clipped
%{_datadir}/applications/com.github.davidmhewitt.clipped.desktop
%{_datadir}/glib-2.0/schemas/com.github.davidmhewitt.clipped.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.davidmhewitt.clipped.??g
%{_datadir}/metainfo/com.github.davidmhewitt.clipped.appdata.xml

%files lang -f %{name}.lang

%changelog
