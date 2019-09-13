#
# spec file for package vkquake
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.02.1
Release:        0
Summary:        Quake 1 port using Vulkan instead of OpenGL for rendering
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
License:        GPL-2.0-only
Group:          Amusements/Games/3D/Shoot
Url:            https://github.com/Novum/vkQuake
Source:         https://github.com/Novum/vkQuake/archive/%{version}/vkQuake-%{version}.tar.gz
Source99:       %{name}.changes
Source100:      appdata.xml
Source101:      %{name}.desktop
BuildRequires:  vulkan-devel
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libmikmod)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
vkQuake is a Quake 1 port using Vulkan instead of OpenGL for rendering. It is based on the popular QuakeSpasm port and runs all mods compatible with it like Arcane Dimensions or In The Shadows.
Game data must be placed in ~/.vkquake/id1 .

%prep
%setup -q -n vkQuake-%{version}
# Fix usage of __DATE__ and __TIME__ macros to prevent build in excess
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE99}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" Quake/host.c

%build
make %{?_smp_mflags} -C Quake \
    STRIP=": do not strip:" \
    DO_USERDIRS=1 \
    USE_SDL2=1 \
    USE_CODEC_FLAC=1 \
    USE_CODEC_OPUS=1 \
    USE_CODEC_MIKMOD=1 \
    USE_CODEC_UMX=1 \
    USE_CODEC_MP3=0
make -C Misc/vq_pak

%install
install -Dm755 Quake/vkquake %{buildroot}%{_bindir}/%{name}
install -Dm644 Misc/vq_pak/vkquake.pak %{buildroot}%{_datadir}/games/%{name}/%{name}.pak
install -D -p -m 644 Misc/vkQuake_512.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -p -m 644 %{SOURCE100}  %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
install -D -p -m 644 %{SOURCE101}  %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%defattr(-,root,root)
%doc readme.md LICENSE.txt Misc/fitzquake080.txt Misc/fitzquake080sdl.txt Misc/fitzquake085.txt
%{_bindir}/%{name}
%dir %{_datadir}/games/%{name}/
%{_datadir}/games/%{name}/%{name}.pak
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%if ( 0%{?suse_version} == 1315 && 0%{?sle_version} == 120100 ) || ! 0%{?is_opensuse}
# Leap 42.1 or SLE
%dir %{_datadir}/appdata
%endif
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
