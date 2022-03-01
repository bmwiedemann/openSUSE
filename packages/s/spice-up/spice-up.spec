#
# spec file for package spice-up
#
# Copyright (c) 2022 SUSE LLC
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


Name:           spice-up
Version:        1.9.1
Release:        0
Summary:        Desktop presentation application
License:        GPL-3.0-only
Group:          Productivity/Office/Other
URL:            https://github.com/Philip-Scott/Spice-up
Source:         https://github.com/Philip-Scott/Spice-up/archive/%{version}.tar.gz#/Spice-up-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  vala > 0.48.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libsoup-2.4)
Recommends:     %{name}-lang

%description
Spice-up is a desktop presentation application
based upon SpiceOfDesign's presentation concept.

%lang_package

%prep
%setup -q -n Spice-up-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang com.github.philip_scott.spice-up %{name}.lang
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
%{_bindir}/com.github.philip_scott.spice-up
%{_datadir}/applications/com.github.philip_scott.spice-up.desktop
%{_datadir}/glib-2.0/schemas/com.github.philip_scott.spice-up.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.??g
%{_datadir}/metainfo/com.github.philip_scott.spice-up.appdata.xml
%{_datadir}/mime/packages/com.github.philip_scott.spice-up.mime.xml

%files lang -f %{name}.lang

%changelog
