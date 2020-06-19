#
# spec file for package megaglest
#
# Copyright (c) 2020 SUSE LLC
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


Name:           megaglest
Version:        3.13.0
Release:        0
Summary:        Customizable 3D real-time strategy game
License:        GPL-3.0-or-later
Group:          Amusements/Games/Strategy/Real Time
URL:            https://megaglest.org/
Source:         https://github.com/MegaGlest/megaglest-source/releases/download/%{version}/%{name}-source-%{version}.tar.xz
# for grepping a constant build time to recieve reproducible builds
Source99:       %{name}.changes
# PATCH-FIX-UPSTREAM wxwidgets3.patch - https://github.com/MegaGlest/megaglest-source/pull/163
Patch0:         wxwidgets3.patch
BuildRequires:  ImageMagick
BuildRequires:  boost-jam
BuildRequires:  cmake
BuildRequires:  freealut-devel
BuildRequires:  freeglut-devel
BuildRequires:  fribidi-devel
BuildRequires:  ftgl-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  krb5-devel
BuildRequires:  libGLw-devel
BuildRequires:  libcares-devel
BuildRequires:  libcurl-devel >= 7.21
BuildRequires:  libdrm-devel
BuildRequires:  libidn-devel
BuildRequires:  libircclient-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libminiupnpc-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libssh2-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libxerces-c-devel
BuildRequires:  lua51-devel
BuildRequires:  openal-soft-devel
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel
BuildRequires:  xorg-x11-Mesa-devel
BuildRequires:  xorg-x11-libX11-devel
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sdl2)
Requires:       freefont
Requires:       gnu-free-fonts
Requires:       linux-libertine-fonts
Requires:       megaglest-data >= %{version}
Requires:       p7zip-full

%description
MegaGlest takes place in a context that could be compared to that of
pre-Renaissance Europe with the twist that magic forces exist in the
environment and can be controlled.

A game takes place on a map of varying size, such as large plains and
fields, with terrain features like rivers, mountains, seas, or
cliffs. Players must establish settlements to gain resources, defend
against other players, and train units to explore the map and attack
enemies.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags} -fcommon"
%cmake \
  -DWANT_SVN_STAMP=OFF
# unforce link against libcurl.a
find . -name link.txt -exec sed -ie 's!%{_libexecdir}/libcurl.a!-lcurl!g' {} \;
find . -name link.txt -exec sed -ie 's!%{_libdir}/libcurl.a!-lcurl!g' {} \;
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/%{name}/data
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,48x48}/apps

for image in megaglest g3dviewer editor; do
    convert "mk/shared/$image.ico[0]" -strip "%{buildroot}%{_datadir}/icons/hicolor/16x16/apps/megaglest_$image.png"
    convert "mk/shared/$image.ico[1]" -strip "%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/megaglest_$image.png"
    convert "mk/shared/$image.ico[2]" -strip "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/megaglest_$image.png"
done
%suse_update_desktop_file -c megaglest        "MegaGlest"        "Real-time strategy game"  megaglest           megaglest_megaglest Game StrategyGame
%suse_update_desktop_file -c megaglest_editor "MegaGlest Editor" "Gamedata editor"          megaglest_editor    megaglest_editor    Game StrategyGame
%suse_update_desktop_file -c g3dviewer        g3dviewer          "Glest 3D Graphics Viewer" megaglest_g3dviewer megaglest_g3dviewer Graphics Viewer

%files
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/megaglest_*.png
%{_datadir}/applications/*

%changelog
