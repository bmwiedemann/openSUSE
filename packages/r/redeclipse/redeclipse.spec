#
# spec file for package redeclipse
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           redeclipse
Version:        1.5.6
Release:        0
Summary:        Fast-paced first person ego shooter
License:        Zlib and CC-BY-SA-3.0
Group:          Amusements/Games/3D/Shoot
Url:            http://www.redeclipse.net/
# Sadly not source URL compatible http://www.indiedb.com/games/red-eclipse/downloads/red-eclipse-v155-elysium-edition-for-linux
Source:         %{name}_%{version}_nix.tar.bz2
# Patches from PlayDeb
Patch1:         windowed-by-default.patch
Patch2:         system_sqlite.patch
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
# This is needed by the Makefile
BuildRequires:  ed
Requires:       %{name}-data >= %{version}

%description
The game is a new take on the first person arena shooter, built as a
total conversion of Cube Engine 2 (Sauerbraten), which lends itself
toward a balanced gameplay, with a general theme of agility in a
variety of environments.
The game is centered on multiplayer based action, but can also be 
played offline against bots.

%package data
Summary:        Data files for the Red Eclipse game
Group:          Amusements/Games/3D/Shoot
Requires:       %{name} >= %{version}
BuildArch:      noarch

%description data
The game is a new take on the first person arena shooter, built as a
total conversion of Cube Engine 2 (Sauerbraten), which lends itself
toward a balanced gameplay, with a general theme of agility in a
variety of environments.

This package contains the data files (maps, models, textures, sounds, etc.)
for the Red Eclipse game.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

rm -r src/enet/
rm -r src/include/
rm -r src/lib/
mkdir -p src/enet/include

find . -name ".git*" -exec rm -rf \{\} +

iconv -f iso8859-1 -t utf-8 readme.txt > readme.txt.conv \
      && mv -f readme.txt.conv readme.txt

sed -i 's/mapeditor/mapeditor;/g' src/install/nix/redeclipse.desktop.am

%build
make %{?_smp_mflags} CXXFLAGS='%{optflags}' LIBENET="" -C src/

%install
make %{?_smp_mflags} CXXFLAGS="%{optflags}" -C src/ \
        DESTDIR=%{buildroot} prefix=%{_prefix}      \
        libexecdir=%{buildroot}%{_libexecdir}       \
        docdir=%{buildroot}%{_docdir}               \
        LIBENET=""                                  \
        system-install

rm -r %{buildroot}%{_datadir}/pixmaps/
sed -i 's/"redeclipse"/redeclipse/g' %{buildroot}%{_datadir}/applications/%{name}.desktop

%fdupes %{buildroot}%{_datadir}/%{name}

%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc readme.txt doc/*.txt
%doc %{_defaultdocdir}/%{name}/examples/
%{_bindir}/%{name}
%{_bindir}/%{name}-server
%{_libexecdir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/*
%dir %{_datadir}/appdata
%{_datadir}/appdata/*.appdata.xml
%{_mandir}/man6/%{name}-server.6.*
%{_mandir}/man6/%{name}.6.*

%files data
%defattr(-,root,root)
%{_datadir}/%{name}

%changelog
