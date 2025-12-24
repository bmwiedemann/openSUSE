#
# spec file for package eartag
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define         appid app.drey.EarTag
Name:           eartag
Version:        1.0.2
Release:        0
Summary:        Edit audio file tags
License:        MIT
URL:            https://gitlab.gnome.org/World/eartag
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  blueprint-compiler
BuildRequires:  meson
BuildRequires:  python3-Pillow
BuildRequires:  python3-base >= 3.11
BuildRequires:  python3-gobject >= 3.49.0
BuildRequires:  python3-mutagen
BuildRequires:  python3-pyacoustid
BuildRequires:  pkgconfig(gtk4) >= 4.16
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5
Requires:       chromaprint-fpcalc
Requires:       python3-Pillow
Requires:       python3-aiofiles
Requires:       python3-aiohttp
Requires:       python3-aiohttp-retry
Requires:       python3-filetype
Requires:       python3-gobject
Requires:       python3-mutagen
Requires:       python3-pyacoustid
Requires:       python3-xxhash

%description
Ear Tag is a simple audio file tag editor. It is primarily geared towards making quick edits or bulk-editing tracks in albums/EPs.
Unlike other tagging programs, Ear Tag does not require the user to set up a music library folder.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{appid}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/dbus-1/services/%{appid}.service
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files lang -f app.drey.EarTag.lang

%changelog
