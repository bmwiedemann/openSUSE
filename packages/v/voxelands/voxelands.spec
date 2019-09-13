#
# spec file for package voxelands
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


%define hash bd31b6d6d0808aa64b6985da99d3d1f7b414b17d

Name:           voxelands
Version:        1709.00
Release:        0
Summary:        An InfiniMiner/Minecraft inspired game
License:        GPL-3.0-or-later AND CC-BY-SA-3.0
Group:          Amusements/Games/3D/Simulation
Url:            http://www.voxelands.com/
Source:         https://gitlab.com/voxelands/voxelands/repository/archive.tar.bz2?ref=v%{version}#/%{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  gmp-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  irrlicht-devel
BuildRequires:  libjpeg-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Voxelands is a sandbox construction game inspired by earlier "voxel world" style
games such as Minetest, Minecraft, and Infiniminer. Gameplay puts players in a
fully destructible 3D game world where they can place and dig numerous types of
blocks, items and creatures using a variety of tools.

Inside the game world players can build structures, artworks and anything else
their creativity can think of on multiplayer servers and singleplayer worlds
across multiple game modes.

%prep
%setup -q -n %{name}-v%{version}-%hash

%build
# cmake macro does not work
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_C_FLAGS_RELEASE=-DNDEBUG -DCMAKE_CXX_FLAGS_RELEASE=-DNDEBUG \
	-DPNG_PNG_INCLUDE_DIR=$(pkg-config libpng --variable=includedir)
make

%install
make DESTDIR=%{buildroot} install
%suse_update_desktop_file -r %{name} Game Simulation
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/%{name}-server
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6*
%{_mandir}/man6/voxelands-server.6.gz
%{_datadir}/%{name}/
%{_datadir}/doc/voxelands/
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
