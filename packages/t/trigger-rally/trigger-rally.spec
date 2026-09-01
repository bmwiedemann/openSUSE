#
# spec file for package trigger-rally
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           trigger-rally
Version:        0.6.7
Release:        0
Summary:        Fast-paced single-player rally racing game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Race
URL:            https://trigger-rally.sourceforge.io/
Source0:        https://downloads.sourceforge.net/project/trigger-rally/trigger-%{version}/trigger-rally-%{version}.tar.gz
# Manpage from Debian
Source1:        trigger-rally.6
Source99:       trigger-rally.changes
# PATCH-FIX-UPSTREAM trigger-rally-libs.patch - fix linking libs
Patch1:         trigger-rally-libs.patch
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(freealut)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(physfs)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(tinyxml2)
Requires:       %{name}-data = %{version}

%description
A 3D rally simulation with a physics engine for drifting, over 100 maps,
different terrain materials like dirt, asphalt, sand, ice etc. and various
weather, light and fog conditions. Most maps are equipped with spoken co-driver
notes and co-driver icons.

%package data
Summary:        Data files for trigger-rally
Group:          Amusements/Games/Action/Race
Requires:       trigger-rally = %{version}
BuildArch:      noarch

%description data
This package provides the data files for trigger-rally, a 3D rally simulation
with a physics engine for drifting, over 100 maps, different terrain materials
like dirt, asphalt, sand, ice etc. and various weather, light and fog conditions.
Most maps are equipped with spoken co-driver notes and co-driver icons.

%prep
%autosetup -p1

dos2unix doc/*.txt bin/*.defs
chmod 644 doc/*
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE99}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" src/PEngine/app.cpp src/Trigger/menu.cpp

%build
%make_build -C src

%install
install -D -m755 bin/%{name} %{buildroot}%{_bindir}/%{name}
install -D -m644 bin/trigger-rally.config.defs %{buildroot}%{_bindir}/trigger-rally.config.defs

# game data
mkdir -p %{buildroot}%{_datadir}/games/%{name}
cp -a data/data.{md5,zip} %{buildroot}%{_datadir}/games/%{name}

# icons
for size in 16 22 24 32 36 48 64 72 96 128 192 256; do
  install -D -m644 data/icon/trigger-${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done
install -D -m644 data/icon/%{name}-icons.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# desktop file
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Trigger Rally
GenericName=Racing game
GenericName[de_DE]=Autorennen
GenericName[fr_FR]=Jeu de course
GenericName[ro_RO]=Joc cu curse
Comment=3D rally racing game
Comment[de_DE]=3D Rally-Autorennen
Comment[fr_FR]=un jeu de rally en 3D
Comment[ro_RO]=Un joc în 3D cu curse de raliu
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;SportsGame;
EOF

# metainfo
install -D -m644 data/metainfo/%{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

# man page
install -D -m644 %{_sourcedir}/%{name}.6 %{buildroot}%{_mandir}/man6/%{name}.6

rm -f %{buildroot}%{_datadir}/doc/trigger-rally/COPYING.txt

%fdupes %{buildroot}%{_datadir}

%files
%doc doc/DATA_AUTHORS.txt doc/README.txt doc/README-stereo.txt
%license doc/COPYING.txt
%{_bindir}/*
%{_datadir}/applications/trigger-rally.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/scalable/apps/trigger-rally.svg
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man6/%{name}.6*

%files data
%license doc/COPYING.txt
%dir %{_datadir}/games/trigger-rally/
%{_datadir}/games/trigger-rally/data.*

%changelog
