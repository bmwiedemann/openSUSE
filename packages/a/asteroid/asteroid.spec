#
# spec file for package asteroid
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global commit 64869dfe745800f34f1c68248ba2e350dc95a592
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           asteroid
Version:        1.2.1
Release:        0
Summary:        Modern version of the classic arcade Game
License:        GPL-3.0
Group:          Amusements/Games/Action/Arcade
Url:            https://chazomaticus.github.io/asteroid/
Source0:        %{name}-%{version}+git-64869df.tar.bz2
Source1:        generate-service-file.sh
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)

%description
Asteroid (just one!) is a modern version of the arcade classic Asteroids,
using OpenGL, GLUT, and optionally GTK and SDL_mixer.
It features a variety of powerups, taunting aliens, 3D textured asteroids,
face-melting sound effects, and infinite playability.

%prep
%setup -q -n %{name}-%{version}+git-%{shortcommit}

# fix include
sed -i -e 's|${OPENGL_LIBRARIES}|-lm ${OPENGL_LIBRARIES}|' \
     CMakeLists.txt

%build
# Not works build with %%cmake
cmake . -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix}
make %{?_smp_mflags}

%install
%make_install

%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}%{_prefix}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}

%changelog
