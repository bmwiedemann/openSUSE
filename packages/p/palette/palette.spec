#
# spec file for package palette
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


Name:           palette
Version:        3.2.1
Release:        0
Summary:        Color palette viewer
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Visualization/Other
URL:            https://github.com/cassidyjames/palette
Source:         https://github.com/cassidyjames/palette/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  AppStream
BuildRequires:  fdupes
BuildRequires:  gettext-runtime >= 0.19.7
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxml2-tools
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 5.1.0
BuildRequires:  pkgconfig(gtk+-3.0)
Recommends:     %{name}-lang

%description
A program for viewing and copying colors from Elementary OS.

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.cassidyjames.palette Graphics GTK Viewer
%find_lang com.github.cassidyjames.palette %{name}.lang
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
%{_bindir}/com.github.cassidyjames.palette
%{_datadir}/applications/com.github.cassidyjames.palette.desktop
%{_datadir}/glib-2.0/schemas/com.github.cassidyjames.palette.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.cassidyjames.palette.??g
%{_datadir}/metainfo/com.github.cassidyjames.palette.appdata.xml

%files lang -f %{name}.lang

%changelog
