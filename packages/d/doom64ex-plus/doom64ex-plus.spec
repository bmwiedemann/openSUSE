#
# spec file for package doom64ex-plus
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


Name:           doom64ex-plus
Summary:        An improved modern version of Doom64EX
Version:        4.0.0.3
Release:        0
Group:          Amusements/Games/3D/Shoot
License:        GPL-2.0-or-later
URL:            https://github.com/atsb/Doom64EX-Plus
Source0:        %{name}-%{version}.tar.gz
Patch:          fix-user-dir.patch
BuildRequires:  gcc
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sdl3) >= 3.1.3
BuildRequires:  pkgconfig(zlib)
Requires(post): hicolor-icon-theme
Requires(postun): hicolor-icon-theme

%define           datafilesdir  %{_datadir}/games/%{name}
%define           gameexefile DOOM64EX-Plus

%description
Doom 64 EX+ is a continuation project of Samuel "Kaiser" Villarreal's
Doom 64 EX aimed to recreate DOOM 64 as closely as possible with
additional modding features.

Doom64EX is a reverse-engineering project aimed to recreate
Doom64 as close as possible with additional modding features.

You must place file DOOM.WAD (case-sensitive) from the Steam or GOG version
of Doom 64 into either folder %datafilesdir or ~/.local/share/doom64ex-plus

%prep
%setup -q -n Doom64EX-Plus-%{version}.SDL.3.1.3
%patch -P 0 -p 1
sed -i 's/__DATE__/"unset"/' src/engine/i_main.c

%build
export CFLAGS="-Wno-pointer-sign %{optflags} -DDOOM_UNIX_INSTALL -DDOOM_UNIX_SYSTEM_DATADIR=\\\"%{datafilesdir}\\\""
%make_build

%install
install -D -t "%{buildroot}%{_bindir}" %{gameexefile}
install -Dm 644 -t "%{buildroot}%{datafilesdir}" %{name}.wad doomsnd.sf2
install -Dm 644 src/engine/%{name}.png "%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png"

mkdir "%{buildroot}%{_datadir}/applications"
cat > "%{buildroot}%{_datadir}/applications/%{name}.desktop" <<EOF
[Desktop Entry]
Name=Doom 64 EX+
Exec=%{gameexefile}
Icon=doom64ex-plus
Type=Application
Comment=A Doom64 game engine
Categories=Game;ActionGame;
EOF

%suse_update_desktop_file %{name}

%post
if [ $1 -eq 1 ]; then
    # shown on installs only
    echo "INFO: %name: The global IWAD directory is %{datafilesdir}"
    echo "You must place file DOOM.WAD (case-sensitive) from the Steam or GOG version
    	 of Doom64 into that folder or in ~/.local/share/doom64ex-plus"
fi

%files
%doc AUTHORS README.md
%license COPYING
%{_bindir}/%{gameexefile}
%{datafilesdir}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%changelog
