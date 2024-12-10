#
# spec file for package playmymusic
#
# Copyright (c) 2024 SUSE LLC
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


%define         appid com.github.artemanufrij.playmymusic
Name:           playmymusic
Version:        2.2.1
Release:        0
Summary:        A music player for local files and remote streams
License:        GPL-3.0-or-later
URL:            https://github.com/artemanufrij/playmymusic
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gettext-runtime >= 0.19.7
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
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
Provides:       melody = %{version}
Obsoletes:      melody < %{version}

%description
A music player for listening local music files, online radios and Audio CDs.

%lang_package

%prep
%autosetup

cp --no-preserve='mode' debian/copyright COPYING

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}

%files
%license COPYING
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}*.svg
%{_datadir}/icons/hicolor/*/apps/playlist-queue-symbolic.svg
%{_datadir}/icons/hicolor/*/apps/playlist-symbolic.svg
%{_datadir}/metainfo/%{appid}.appdata.xml

%files lang -f %{appid}.lang

%changelog
