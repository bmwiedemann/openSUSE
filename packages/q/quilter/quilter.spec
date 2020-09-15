#
# spec file for package quilter
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


Name:           quilter
Version:        2.5.1
Release:        0
Summary:        Writing application
License:        GPL-3.0-only
Group:          Productivity/Office/Word Processor
URL:            https://github.com/lainsce/quilter
Source:         https://github.com/lainsce/quilter/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libmarkdown-devel
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 5.2.3
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
Recommends:     %{name}-lang

%description
A fullscreen word processor for Elementary OS.

%lang_package

%prep
%setup -q

# use default font
sed -i '/QuiltMono.ttf/d' $(grep -rl QuiltMono.ttf)
sed -i '/QuiltVier.ttf/d' $(grep -rl QuiltVier.ttf)

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.lainsce.quilter GTK Utility TimeUtility
%find_lang com.github.lainsce.quilter %{name}.lang
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
%{_bindir}/com.github.lainsce.quilter
%{_datadir}/com.github.lainsce.quilter/
%{_datadir}/applications/com.github.lainsce.quilter.desktop
%{_datadir}/glib-2.0/schemas/com.github.lainsce.quilter.gschema.xml
%{_datadir}/gtksourceview-3.0/styles/*.xml
%{_datadir}/icons/hicolor/*/apps/com.github.lainsce.quilter.??g
%{_datadir}/metainfo/com.github.lainsce.quilter.appdata.xml

%files lang -f %{name}.lang

%changelog
