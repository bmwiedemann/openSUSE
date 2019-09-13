#
# spec file for package dippi
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


Name:           dippi
Version:        2.7.3
Release:        0
Summary:        Tool for calculating display info like DPI and aspect ratio
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://cassidyjames.com/dippi
Source:         https://github.com/cassidyjames/dippi/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  AppStream
BuildRequires:  fdupes
BuildRequires:  gettext-runtime >= 0.19.7
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxml2-tools
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
Recommends:     %{name}-lang

%description
A tool to analyze displays and to input a few details and figure out the aspect
ratio, DPI, and other details of a particular display. Can be used to decide
which laptop or external monitor to purchase, and if it would be considered
HiDPI.

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.cassidyjames.dippi GTK Utility DesktopSettings
%find_lang com.github.cassidyjames.dippi %{name}.lang
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
%doc AUTHORS COPYING README.md
%{_bindir}/com.github.cassidyjames.dippi
%{_datadir}/applications/com.github.cassidyjames.dippi.desktop
%{_datadir}/icons/hicolor/*/apps/com.github.cassidyjames.dippi.??g
%{_datadir}/metainfo/com.github.cassidyjames.dippi.appdata.xml

%files lang -f %{name}.lang

%changelog
