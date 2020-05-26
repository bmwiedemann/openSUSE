#
# spec file for package yishu
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


Name:           yishu
Version:        1.2.3
Release:        0
Summary:        A bespoke and simple Todo.txt client
License:        GPL-3.0-or-later
Group:          Productivity/Office/Organizers
URL:            https://github.com/lainsce
Source:         https://github.com/lainsce/yishu/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxml2-tools
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0)
Recommends:     %{name}-lang

%description
Write a to-do list that will be easy to sync with most known Todo.txt clients.

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.lainsce.yishu GTK Utility DesktopUtility
%find_lang com.github.lainsce.yishu %{name}.lang
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
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/com.github.lainsce.yishu
%{_datadir}/applications/com.github.lainsce.yishu.desktop
%{_datadir}/glib-2.0/schemas/com.github.lainsce.yishu.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.lainsce.yishu.??g
%{_datadir}/metainfo/com.github.lainsce.yishu.appdata.xml

%files lang -f %{name}.lang

%changelog
