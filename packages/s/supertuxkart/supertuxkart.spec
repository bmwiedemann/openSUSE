#
# spec file for package supertuxkart
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


#
Name:           supertuxkart
Version:        1.4
Release:        0
Summary:        A 3D kart racing game
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Amusements/Games/3D/Race
URL:            https://supertuxkart.net/
Source:         https://github.com/supertuxkart/stk-code/releases/download/%{version}/supertuxkart-%{version}-src.tar.xz
# Geeko kart add-on (CC-BY 3.0)
Source1:        14e6ba25b17f0d.zip
Source9:        supertuxkart.6
Patch0:         gcc13.patch
BuildRequires:  cmake >= 3
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libraqm-devel
%if 0%{?suse_version} && 0%{?is_opensuse}
BuildRequires:  mcpp-devel
%endif
%ifnarch %ix86 x86_64
BuildRequires:  Mesa-libEGL-devel
BuildRequires:  Mesa-libGLESv2-devel
BuildRequires:  Mesa-libGLESv3-devel
%endif
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  wiiuse-devel
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(xrandr)
Requires:       %{name}-data = %{version}
Requires(post): hicolor-icon-theme
Requires(postun):hicolor-icon-theme

%description
SuperTuxKart is a Free 3d kart racing game.

The focus of the game is more to be fun than it is to be realistic.
You can play with up to 4 friends on one PC, racing against each other or just try to beat the computer.

See the great lighthouse or drive through the sand and visit the pyramids. Race underground or in space,
watching the stars passing by. Have some rest under the palms on the beach (watching the other karts
overtaking you :) ). But don't eat the bananas! Watch for bowling balls, plungers, bubble gum and cakes thrown by opponents.

You can do a single race against other karts, compete in one of several Grand Prix, try to beat the high score in time trials
on your own, play battle mode against your friends, and more!

%package data
Summary:        Data files for SuperTuxKart
Group:          Amusements/Games/3D/Race
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Data files for SuperTuxKart a Free 3d kart racing game.

%prep
%autosetup -p1 -n SuperTuxKart-%{version}-src
find -name '*~' -delete -print
find -name '.git*' -type f -delete -print
rm -rfv ./.github

# fix W: non-executable-script
rm data/optimize_data.sh
rm data/po/pull_from_transifex.sh
rm data/po/update_po_authors.py

%build
mkdir build && cd build
# NOTE that %%cmake macro breaks linking.
cmake .. \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_C_FLAGS="%{optflags} -fno-strict-aliasing" \
        -DCMAKE_CXX_FLAGS="%{optflags} -fno-strict-aliasing" \
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
        -DBUILD_RECORDER=0 \
        -DOpenGL_GL_PREFERENCE=GLVND \
        -DUSE_SYSTEM_WIIUSE:BOOL=ON \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo
make V=1 %{?_smp_mflags}

%install
%cmake_install

mkdir -p %{buildroot}%{_datadir}/supertuxkart/data/karts/geeko/
cd %{buildroot}%{_datadir}/supertuxkart/data/karts/geeko/
unzip %{SOURCE1}
%fdupes  %{buildroot}%{_datadir}
%suse_update_desktop_file supertuxkart
# Man page:
mkdir -p %{buildroot}%{_mandir}/man6
cp %{SOURCE9} %{buildroot}%{_mandir}/man6

# libangelscript does not need to be provided
for file in /usr/include/angelscript.h \
   /usr/lib/cmake/Angelscript/AngelscriptConfig.cmake \
   /usr/lib/cmake/Angelscript/AngelscriptConfigVersion.cmake \
   /usr/lib/cmake/Angelscript/AngelscriptTargets-relwithdebinfo.cmake \
   /usr/lib/cmake/Angelscript/AngelscriptTargets.cmake \
   /usr/lib/libangelscript.a; do
   rm %{buildroot}/$file
done

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%defattr(-,root,root)
%license COPYING
%doc README.md CHANGELOG.md
%{_bindir}/supertuxkart
%{_mandir}/man?/%{name}.?.*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/supertuxkart.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/

%files data
%defattr(-,root,root)
%{_datadir}/supertuxkart/

%changelog
