#
# spec file for package trigger-rally
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


Name:           trigger-rally
Version:        0.6.6.1
Release:        0
Summary:        Fast-paced single-player rally racing game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Race
URL:            http://trigger-rally.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/trigger-rally/trigger-%{version}/trigger-rally-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM https://sourceforge.net/p/trigger-rally/patches/14/
Source1:        %{name}.desktop
# PATCH-FEATURE-UPSTREAM https://sourceforge.net/p/trigger-rally/patches/15/
Source2:        %{name}.appdata.xml
Source99:       %{name}.changes
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(freealut)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(physfs) >= 2.1
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(tinyxml2) >= 6
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
%setup -q
sed -i 's#-lSDL2main##' src/GNUmakefile*

dos2unix doc/*.txt bin/*.defs
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE99}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" src/PEngine/app.cpp src/Trigger/menu.cpp
sed -i "s|-march=native||; s|-mtune=native||" src/GNUmakefile*

%build
make --directory=src prefix=%{_prefix} exec_prefix=%{_prefix} bindir=%{_bindir}
# NOTE: don't use datadir=...: program currently (v0.6.6.1) uses hardcoded search paths

%install
%make_install --directory=src prefix=%{_prefix} exec_prefix=%{_prefix} bindir=%{_bindir}
# NOTE: don't use datadir=...: program currently (v0.6.6.1) uses hardcoded search paths

rm -f %{buildroot}%{_datadir}/doc/trigger-rally/COPYING.txt

%suse_update_desktop_file -i %{name}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
ln -sf %{_datadir}/games/trigger-rally/icon/trigger-rally-icons.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/trigger-rally.svg

mkdir -p %{buildroot}%{_datadir}/appdata
install -Dm0644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%fdupes %{buildroot}%{_datadir}

%files
%license doc/COPYING.txt
%{_bindir}/*
%{_datadir}/games/trigger-rally/icon
%{_datadir}/applications/trigger-rally.desktop
%{_datadir}/icons/hicolor/scalable/apps/trigger-rally.svg
%{_datadir}/doc/trigger-rally/
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml

%files data
%license doc/COPYING.txt
%dir %{_datadir}/games/trigger-rally/
%{_datadir}/games/trigger-rally/data.*

%changelog
