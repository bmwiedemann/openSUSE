#
# spec file for package vido
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


Name:           vido
Version:        1.3.0
Release:        0
Summary:        Online Video Downloader
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Utilities
URL:            https://github.com/bernardodsanderson/vido
Source:         https://github.com/bernardodsanderson/vido/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gettext-runtime >= 0.19.7
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxml2-tools
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.3
BuildRequires:  pkgconfig(gtk+-3.0)
Requires:       youtube-dl
Recommends:     %{name}-lang

%description
This tool downloads online videos from various sources including
archive.org and others.

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.bernardodsanderson.vido GTK Network FileTransfer
%find_lang com.github.bernardodsanderson.vido %{name}.lang
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
%{_bindir}/com.github.bernardodsanderson.vido
%{_datadir}/applications/com.github.bernardodsanderson.vido.desktop
%{_datadir}/icons/hicolor/*/apps/com.github.bernardodsanderson.vido.??g
%{_datadir}/metainfo/com.github.bernardodsanderson.vido.appdata.xml

%files lang -f %{name}.lang

%changelog
