#
# spec file for package ecwolf
#
# Copyright (c) 2023 SUSE LLC
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


Name:           ecwolf
Version:        1.4.1
Release:        0
Summary:        An opensource implementation of Wolfenstein3D engine
License:        GPL-2.0-only
Group:          Amusements/Games/3D/Shoot
URL:            https://maniacsvault.net/ecwolf
#Git-Clone:     https://bitbucket.org/ecwolf/ecwolf.git
Source:         https://maniacsvault.net/ecwolf/files/ecwolf/1.x/%{name}-%{version}-src.tar.xz
Patch1:         ecwolf-no-rpath.patch
Patch2:         ecwolf-fix-path.patch
BuildRequires:  cmake
BuildRequires:  fluidsynth-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(sdl2)
Provides:       bundled(gdtoa)
Provides:       bundled(lzma)

%description
ECWolf is a port of the Wolfenstein 3D engine based of Wolf4SDL.

%prep
%setup -q -n %{name}-%{version}-src
%patch1 -p1
%patch2 -p1
# remove bundled libs
rm -Rf deps/{bzip2,zlib,jpeg-6b,SDL,SDL_mixer,SDL_net,textscreen}
sed -e 's|/usr/local/share/games/wolf3d|%{_datadir}/wolf3d|g' -i docs/ecwolf.6

%build
%cmake \
    -DINTERNAL_ZLIB=OFF \
    -DINTERNAL_BZIP2=OFF \
    -DINTERNAL_JPEG=OFF \
    -DUSE_LIBTEXTSCREEN=OFF \
    -DGPL=ON
%cmake_build

%install
install -D -m 0755 build/ecwolf %{buildroot}%{_bindir}/ecwolf
install -D -m 0644 build/ecwolf.pk3 %{buildroot}%{_datadir}/ecwolf/ecwolf.pk3
install -D -m 0644 docs/ecwolf.6 %{buildroot}%{_mandir}/man6/ecwolf.6

%files
%license docs/license-gpl.txt docs/license-id.txt
%doc README.md PHILOSOPHY.md docs/changelog
%{_bindir}/ecwolf
%dir %{_datadir}/ecwolf
%{_datadir}/ecwolf/ecwolf.pk3
%{_mandir}/man6/ecwolf.6%{?ext_man}

%changelog
