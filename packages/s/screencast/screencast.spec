#
# spec file for package screencast
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


Name:           screencast
Version:        1.0.0
Release:        0
Summary:        A screencasting application
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://github.com/artemanufrij/screencast
Source:         https://github.com/artemanufrij/screencast/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
Recommends:     %{name}-lang
Provides:       eidete = %{version}
Obsoletes:      eidete < %{version}

%description
A screencasting application for Elementary OS.

Current features:
  * encoding to WebM
  * selection of the area to be recorded
  * display of the pressed keys
  * audio recording

%lang_package

%prep
%setup -q

install -m0644 debian/copyright COPYING

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.artemanufrij.screencast GTK AudioVideo Video Recorder
%find_lang com.github.artemanufrij.screencast %{name}.lang
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
%{_bindir}/com.github.artemanufrij.screencast
%{_datadir}/applications/com.github.artemanufrij.screencast.desktop
%{_datadir}/glib-2.0/schemas/com.github.artemanufrij.screencast.gschema.xml
%{_datadir}/icons/hicolor/*/*/com.github.artemanufrij.screencast.??g
%{_datadir}/metainfo/com.github.artemanufrij.screencast.appdata.xml

%files lang -f %{name}.lang

%changelog
