#
# spec file for package openomf
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2019-2025, Martin Hauke <mardnh@gmx.de>
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


Name:           openomf
Version:        0.8.6
Release:        0
Summary:        Open Source remake of "One Must Fall 2097"
License:        MIT
URL:            https://www.openomf.org
#Git-Clone:     https://github.com/omf2097/openomf.git
Source:         %{name}-%{version}.tar.xz
Source2:        %{name}.README.SUSE
# PATCH-FIX-OPENSUSE null-audio-relwithdebinfo.patch mpluskal@suse.com -- build null audio backend/sources in RelWithDebInfo so unit tests link (upstream enables them only in Debug, but test_sound_tracker.c needs them unconditionally)
Patch0:         null-audio-relwithdebinfo.patch
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(argtable3)
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxmp)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)

%description
OpenOMF is a open source remake of "One Must Fall 2097".

OMF is a fighting game featuring two robot fighters who fight in a
single arena. Eleven robots and ten customizable pilots are available
for play, along with five arenas and four tournaments. The pilots
vary in strength, speed and endurance.

NOTE:
To play One Must Fall 2097 with openomf you need the original game
files.  See %{_docdir}/openomf/README.SUSE

%prep
%autosetup -p1

%build
%cmake \
    -DUSE_MINIUPNPC=OFF \
    -DUSE_NATPMP=OFF \
    -DUSE_TESTS=ON
%cmake_build

%install
%cmake_install

# Install icons and desktop file
for size in 256 128 96 64 48 32 16; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$size"x$size/apps"
    magick convert -strip resources/icons/openomf.png -resize "$size"x"$size" %{buildroot}%{_datadir}/icons/hicolor/$size"x$size/apps/%{name}.png"
done
%suse_update_desktop_file -c %{name} 'Remake of "One Must Fall 2097"' "A fighting video game" %{name} %{name} Game ArcadeGame

install -m0644 %{SOURCE2} README.SUSE

rm %{buildroot}%{_datadir}/games/openomf/resources/{LICENSE*,README.md}
# Flatpak desktop file is not usable in an RPM (wrong Icon name); we ship our own below
rm %{buildroot}%{_datadir}/games/openomf/resources/org.openomf.OpenOMF.desktop

%check
./build/openomf_test_main

%files
%doc DEBUG-KEYS.md NETWORKING.md README.md README.SUSE
%license LICENSE resources/gamecontrollerdb/LICENSE.gamecontrollerdb src/vendored/argtable/LICENSE.argtable3 src/vendored/zip/LICENSE.zip
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/resources
%{_datadir}/games/openomf/resources/openomf.bk
%{_datadir}/games/openomf/resources/gamecontrollerdb.txt
%{_datadir}/games/openomf/resources/openomf.png
%{_datadir}/games/openomf/resources/DANISH.LNG
%{_datadir}/games/openomf/resources/DANISH.LNG2
%{_datadir}/games/openomf/resources/ENGLISH.DAT2
%{_datadir}/games/openomf/resources/GERMAN.DAT2
%dir %{_datadir}/games/openomf/shaders
%{_datadir}/games/openomf/shaders/debug_atlas.frag
%{_datadir}/games/openomf/shaders/palette.*
%{_datadir}/games/openomf/shaders/rgba.*
%{_datadir}/games/openomf/shaders/scalers/

%changelog
