#
# spec file for package melody
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


Name:           melody
Version:        2.2.1
Release:        0
Summary:        A music player for local files and remote streams
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://artemanufrij.github.io
Source:         https://github.com/artemanufrij/playmymusic/archive/%{version}.tar.gz#/playmymusic-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gettext-runtime >= 0.19.7
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.42.0
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(taglib_c)
Recommends:     %{name}-lang

%description
A music player for listening local music files, online radios and Audio CDs.

%lang_package

%prep
%setup -q -n playmymusic-%{version}

cp --no-preserve='mode' debian/copyright COPYING

%build
%meson
%meson_build

%install
%meson_install
%find_lang com.github.artemanufrij.playmymusic %{name}.lang
%fdupes %{buildroot}/%{_datadir}

%files
%license COPYING
%doc README.md
%{_bindir}/com.github.artemanufrij.playmymusic
%{_datadir}/applications/com.github.artemanufrij.playmymusic.desktop
%{_datadir}/glib-2.0/schemas/com.github.artemanufrij.playmymusic.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.artemanufrij.playmymusic*.??g
%{_datadir}/icons/hicolor/*/apps/playlist-queue-symbolic.??g
%{_datadir}/icons/hicolor/*/apps/playlist-symbolic.??g
%{_datadir}/metainfo/com.github.artemanufrij.playmymusic.appdata.xml

%files lang -f %{name}.lang

%changelog
