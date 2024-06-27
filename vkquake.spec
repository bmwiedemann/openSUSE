#
# spec file for package vkquake
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2017 Luke Jones <luke.nukem.jones@gmail.com>
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


Name:           vkquake
Version:        1.31.0
Release:        0
Summary:        Quake 1 port using Vulkan instead of OpenGL for rendering
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            https://github.com/Novum/vkQuake
Source:         https://github.com/Novum/vkQuake/archive/refs/tags/%{version}.tar.gz#/vkQuake-%{version}.tar.gz
Source99:       %{name}.changes
Source100:      appdata.xml
Source101:      %{name}.desktop
BuildRequires:  cmake
BuildRequires:  glslang-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  spirv-tools
# from quakedef.h "Vulkan is too old" preprocessor check
BuildRequires:  vulkan-devel >= 1.2.162
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libmikmod)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
BuildRequires:  gcc11
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++
%endif

%description
vkQuake is a Quake 1 port using Vulkan instead of OpenGL for rendering. It is based on the popular QuakeSpasm port and runs all mods compatible with it like Arcane Dimensions or In The Shadows.
Game data must be placed in ~/.vkquake/id1 .

%prep
%autosetup -n vkQuake-%{version}

# Drop pre-compiled Windows stuff
rm Windows -fr

# Fix usage of __DATE__ and __TIME__ macros to prevent build in excess
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE99}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" Quake/host.c

%build
%meson -Ddo_userdirs=enabled
%meson_build

%install
install -Dm755 %{_vpath_builddir}/vkquake %{buildroot}%{_bindir}/%{name}
install -D -p -m 644 Misc/vkQuake_512.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -p -m 644 %{SOURCE100} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
install -D -p -m 644 %{SOURCE101} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE.txt
%doc readme.md Misc/fitzquake080.txt Misc/fitzquake080sdl.txt Misc/fitzquake085.txt
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
