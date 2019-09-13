#
# spec file for package transporter
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


Name:           transporter
Version:        1.3.3
Release:        0
Summary:        Program for sharing files between computers
License:        GPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/bleakgrey
Source:         https://github.com/bleakgrey/Transporter/archive/%{version}.tar.gz#/Transporter-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gettext-runtime >= 0.19.7
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
Requires:       contractor
Requires:       python3-magic-wormhole
Recommends:     %{name}-lang
# SECTION test requirements
BuildRequires:  python3-magic-wormhole
# /SECTION

%description
A magic-wormhole client designed for Elementary OS.

%lang_package

%prep
%setup -q -n Transporter-%{version}

sed -i 's/\bmetainfo\b/appdata/' $(grep -rwl 'metainfo')

# Add path to the wormhole executable file
ls %{_bindir}/wormhole || %{_bindir}/wormhole
sed -e '/WORMHOLE_LOCATIONS\ \?=/s|{\(.*\)}|{\"%{_bindir}/wormhole\"\, \1}|' \
    -i $(grep -rl 'WORMHOLE_LOCATIONS\ \?=')

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.bleakgrey.transporter GTK Network FileTransfer
%find_lang com.github.bleakgrey.transporter %{name}.lang
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
%license LICENSE*
%doc README.md
%{_bindir}/com.github.bleakgrey.transporter
%{_datadir}/appdata/com.github.bleakgrey.transporter.appdata.xml
%{_datadir}/applications/com.github.bleakgrey.transporter.desktop
%dir %{_datadir}/contractor
%{_datadir}/contractor/com.github.bleakgrey.transporter.contract
%{_datadir}/glib-2.0/schemas/com.github.bleakgrey.transporter.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.bleakgrey.transporter.??g

%files lang -f %{name}.lang

%changelog
