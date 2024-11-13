#
# spec file for package ironwail
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


Name:           ironwail
Version:        0.8.0
Release:        0
Summary:        High-performance QuakeSpasm fork
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            https://github.com/andrei-drexler/ironwail
Source:         %{name}-%{version}.tar.gz
Source1:        ironwail-rpmlintrc
Patch0:         enginepak.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmikmod)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
Requires(post): hicolor-icon-theme
Requires(postun): hicolor-icon-theme

%description
A fork of the popular GLQuake descendant QuakeSpasm with a focus
on high performance instead of maximum compatibility,
with a few extra features sprinkled on top.
Quake game files (id1 directory containing pak files) must be found
for ironquake to start:
- automatically found if the Quake Steam remaster is installed
- id1 directory can be copied into ~/.ironwail
- start ironwail with option -basedir <install_dir>, where <install_dir>
  is the directory containing the id1 folder

%prep
%autosetup -p0

%build
export CFLAGS="%{optflags}"
# LDFLAGS needed for link to not fail on Leap 15.5
export LDFLAGS="-ldl"
%make_build -C Quake\
	    DO_USERDIRS=1 \
	    USE_CODEC_FLAC=1 \
	    USE_CODEC_OPUS=1 \
	    USE_CODEC_MIKMOD=1 \
	    USE_CODEC_UMX=1

%install
install -D -m 755 Quake/ironwail %{buildroot}%{_bindir}/ironwail
install -Dm 644 -t %{buildroot}%{_datadir}/games/ironwail Quake/ironwail.pak
install -Dm 644 Misc/QuakeSpasm_512.png "%{buildroot}%{_datadir}/icons/hicolor/512x512/apps/ironwail.png"

mkdir "%{buildroot}%{_datadir}/applications"
cat > "%{buildroot}%{_datadir}/applications/ironwail.desktop" <<EOF
[Desktop Entry]
Name=Ironwail
Exec=ironwail
Icon=ironwail
Type=Application
Comment=A Quake game engine
Categories=Game;ActionGame;
EOF

%post
if [ $1 -eq 1 ]; then
    # shown on installs only
    echo "Quake game files (id1 directory containing pak files) must be found for ironquake to start:"
    echo "  - automatically found if the Quake Steam remaster is installed"
    echo "  - id1 directory can be copied into ~/.ironwail"
    echo "  - start ironwail with option -basedir <install_dir>, where <install_dir> is the directory containing the id1 folder"
fi

%files
%license LICENSE.txt
%doc README.md Quakespasm.txt Quakespasm-Music.txt Misc/fitzquake080.txt Misc/fitzquake080sdl.txt Misc/fitzquake085.txt
%{_bindir}/ironwail
%dir %{_datadir}/games/ironwail
%{_datadir}/games/ironwail/ironwail.pak
%{_datadir}/applications/ironwail.desktop
%{_datadir}/icons/hicolor/512x512/apps/ironwail.png

%changelog
