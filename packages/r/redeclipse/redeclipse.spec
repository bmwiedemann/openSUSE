#
# spec file for package redeclipse
#
# Copyright (c) 2022 SUSE LLC
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


Name:           redeclipse
Version:        2.0.0
Release:        0
Summary:        Fast-paced first person ego shooter
License:        CC-BY-SA-3.0 AND Zlib
Group:          Amusements/Games/3D/Shoot
URL:            http://www.redeclipse.net/
Source:         https://github.com/redeclipse/base/releases/download/v%{version}/%{name}_%{version}_nix.tar.bz2

Patch0:         windowed-by-default.patch
Patch1:         system_sqlite.patch

BuildRequires:  discord-rpc-devel
BuildRequires:  ed
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)

Requires:       %{name}-data >= %{version}

%description
Red Eclipse 2 is a first-person shooter based on the tesseract engine.
Parkour gameplay, different game modes, and several mutators to make the game very flexible.
A map editor is included.

%package data
Summary:        Data files for the Red Eclipse game
Group:          Amusements/Games/3D/Shoot
BuildArch:      noarch

%description data
This package contains the data files (maps, models, textures, sounds, etc.) for the Red Eclipse game.

%package server
Summary:        The Red Eclipse server binary
Group:          Amusements/Games/3D/Shoot
Requires:       %{name}-data >= %{version}

%description server
This package contains the server binary for the Red Eclipse game.

%prep
%autosetup -p1
# Make sure we use no externally-provided blobs
rm -rf bin/x86 bin/amd64
# Use the system discord headers
rm -rf src/shared/discord_rpc.h src/shared/discord_register.h

rm -r src/enet/
rm -r src/include/
rm -r src/lib/
mkdir -p src/enet/include

find . -name ".git*" -exec rm -rf \{\} +

iconv -f iso8859-1 -t utf-8 readme.txt > readme.txt.conv \
      && mv -f readme.txt.conv readme.txt

sed -i 's/mapeditor/mapeditor;/g' src/install/nix/redeclipse.desktop.am

%build
%make_build \
  CXXFLAGS='%{optflags}' \
%ifarch %{ix86} x86_64
  WANT_DISCORD=1 \
%endif
  LIBENET="" -C src/

%install
%make_build CXXFLAGS="%{optflags}" -C src/ \
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
%license doc/license.txt
%doc readme.txt doc/*.txt
%doc %{_defaultdocdir}/%{name}/examples/
%{_bindir}/%{name}

%{_libexecdir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/*
%dir %{_datadir}/appdata
%{_datadir}/appdata/*.appdata.xml
%{_mandir}/man6/%{name}.6.*

%files data
%license doc/license.txt
%{_datadir}/%{name}

%files server
%license doc/license.txt
%{_bindir}/%{name}-server
%{_mandir}/man6/%{name}-server.6.*
%{_libexecdir}/%{name}/config
%{_libexecdir}/%{name}/data
%{_libexecdir}/%{name}/config

%changelog
