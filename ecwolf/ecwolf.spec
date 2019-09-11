#
# spec file for package ecwolf
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


Name:           ecwolf
Version:        1.3.3
Release:        0
Summary:        An opensource implementation of Wolfenstein3D engine
License:        GPL-2.0-only
Group:          Amusements/Games/3D/Shoot
URL:            http://maniacsvault.net/ecwolf
Source:         http://maniacsvault.net/ecwolf/files/ecwolf/1.x/%{name}-%{version}-src.tar.xz
Patch0:         ecwolf-static-libs.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libbz2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sdl)

%description
ECWolf is a port of the Wolfenstein 3D engine based of Wolf4SDL.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1

sed -e 's|OpenResourceFile(datawad|OpenResourceFile("%{_datadir}/ecwolf/ecwolf.pk3"|' \
  -e 's|Push(datawad|Push("%{_datadir}/ecwolf/ecwolf.pk3"|' \
  -e 's|%{_prefix}/local/share/games/wolf3d|%{_datadir}/wolf3d|' \
  -i src/wl_iwad.cpp

%build
%cmake \
    -DBUILD_PATCHUTIL=ON \
    -DGPL=ON
%make_jobs

%install
install -D -m 0755 build/ecwolf %{buildroot}%{_bindir}/ecwolf
install -m 0755 build/tools/patchutil/patchutil %{buildroot}%{_bindir}/ecwolf-patchutil
install -D -m 0644 build/ecwolf.pk3 %{buildroot}%{_datadir}/ecwolf/ecwolf.pk3

%files
%license docs/license-gpl.txt docs/license-id.txt
%doc README.md
%{_bindir}/ecwolf
%{_bindir}/ecwolf-patchutil
%{_datadir}/ecwolf
%{_datadir}/ecwolf/ecwolf.pk3

%changelog
