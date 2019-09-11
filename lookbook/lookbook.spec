#
# spec file for package lookbook
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


Name:           lookbook
Version:        1.1.0
Release:        0
Summary:        Navigator for finding and browsing system icons
License:        GPL-3.0-or-later
Group:          Development/Tools/Navigators
URL:            http://danielfore.com
Source:         https://github.com/danrabbit/lookbook/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.40.4
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)

%description
Lookbook is a browser for system icons. Icons can be grouped by
category or be searched by icon name. Icons are shown in different
sizes. A code snippet to use in programs can be displayed.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.danrabbit.lookbook GTK Development X-SuSE-Core-Development
%fdupes %{buildroot}/%{_datadir}

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
%doc README.md
%{_bindir}/com.github.danrabbit.lookbook
%{_datadir}/applications/com.github.danrabbit.lookbook.desktop
%{_datadir}/glib-2.0/schemas/com.github.danrabbit.lookbook.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.danrabbit.lookbook.??g
%{_datadir}/metainfo/com.github.danrabbit.lookbook.appdata.xml

%changelog
