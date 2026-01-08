#
# spec file for package grafx2
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


%define recoilver 6.4.2
%define sixfivezerotwover 0.1

Name:           grafx2
Version:        2.9
Release:        0
Summary:        Pixel Art editor
License:        GPL-2.0-only
Group:          Productivity/Graphics/Bitmap Editors
URL:            http://grafx2.tk
Source:         https://gitlab.com/GrafX2/grafX2/-/archive/v%{version}/grafX2-v%{version}.tar.bz2
Source1:        https://sourceforge.net/projects/recoil/files/recoil/%{recoilver}/recoil-%{recoilver}.tar.gz
Source2:        https://github.com/redcode/6502/releases/download/v%{sixfivezerotwover}/6502-v%{sixfivezerotwover}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpng16-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
Provides:       bundled(6502) = %{sixfivezerotwover}
Provides:       bundled(recoil) = %{recoilver}

%description
GrafX2 is a bitmap paint program inspired by the Amiga programs Deluxe Paint and Brilliance.

%prep
%autosetup -n grafX2-v%{version}
mkdir -p 3rdparty/archives/
cp -a %{SOURCE1} %{SOURCE2} 3rdparty/archives/

%build
cd src
make %{?_smp_mflags} API=sdl2

%install
cd src
make install PREFIX=%{_prefix} DESTDIR=%{buildroot} API=sdl2

%suse_update_desktop_file grafx2 -r Graphics 2DGraphics

mkdir -p %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/grafx2.xpm %{buildroot}%{_datadir}/pixmaps/grafx2.xpm
mv %{buildroot}%{_bindir}/grafx2-sdl2 %{buildroot}%{_bindir}/grafx2

%files
%doc doc/README.txt doc/quickstart.rtf
%{_bindir}/grafx2
%{_datadir}/grafx2
%{_datadir}/applications/grafx2.desktop
%{_datadir}/metainfo/eu.grafx2.grafx2.metainfo.xml
%{_datadir}/pixmaps/grafx2.xpm
%{_datadir}/icons/hicolor/scalable/apps/grafx2.svg

%changelog
