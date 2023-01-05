#
# spec file for package warzone2100
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

# Linking is broken with LTO at the moment
%define _lto_cflags %{nil}
# NOTE Vulkan is disabled for Leap 15 due to older VK Headers
%if 0%{?suse_version} > 1500
%bcond_without vulkan
%else
%bcond_with vulkan
%endif
Name:           warzone2100
Version:        4.3.3
Release:        0
Summary:        Innovative 3D real-time strategy
License:        BSD-3-Clause AND CC-BY-SA-3.0 AND GPL-3.0-or-later AND CC0-1.0 AND LGPL-2.1-only
Group:          Amusements/Games/Strategy/Real Time
URL:            http://wz2100.net/
Source:         https://github.com/Warzone2100/warzone2100/releases/download/%{version}/warzone2100_src.tar.xz
Source99:       %{name}.changes
BuildRequires:  asciidoc
BuildRequires:  cmake >= 3.5
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  libminiupnpc-devel
BuildRequires:  libpng-devel
BuildRequires:  physfs-devel
BuildRequires:  pkg-config
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  zip
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sqlite3) >= 3.14
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  rubygem(asciidoctor)
%if %{with vulkan}
BuildRequires:  shaderc
BuildRequires:  vulkan-headers >= 1.2.148
BuildRequires:  pkgconfig(vulkan)
%endif
Requires:       %{name}-data = %{version}
Recommends:     %{name}-movies

%description
You command the forces of "The Project" in a battle to rebuild
the world after mankind has almost been destroyed by nuclear
missiles.

The game offers campaign, multi-player and single-player skirmish
modes. An extensive tech tree with over 400 different
technologies, combined with the unit design system, allows for
a wide variety of possible units and tactics.

Warzone 2100 was originally developed as a commercial game by
Pumpkin Studios and published in 1999, and was released as
open source by them in 2004, for the community to continue
working on it.

This package provides the binaries for Warzone 2100.

%package data
Summary:        Data files for Warzone 2100
Group:          Amusements/Games/Strategy/Real Time
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
You command the forces of "The Project" in a battle to rebuild
the world after mankind has almost been destroyed by nuclear
missiles.

The game offers campaign, multi-player and single-player skirmish
modes. An extensive tech tree with over 400 different
technologies, combined with the unit design system, allows for
a wide variety of possible units and tactics.

Warzone 2100 was originally developed as a commercial game by
Pumpkin Studios and published in 1999, and was released as
open source by them in 2004, for the community to continue
working on it.

This package provides the game data for Warzone 2100.

%prep
%setup -q -n %{name}

# constant timestamp for reproducible builds
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE99}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%T")\""
find .  -name '*.cpp' | xargs sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g"

%build
%cmake .. \
%if %{without vulkan}
        -DWZ_ENABLE_BACKEND_VULKAN=Off \
%endif
        -DBUILD_SHARED_LIBS:BOOL=OFF \
        -DWZ_APPSTREAM_ID=warzone2100
%cmake_build

%install
%cmake_install
%find_lang %{name}
%suse_update_desktop_file -i %{name}

mkdir -p %{buildroot}%{_datadir}/appdata/
mv %{buildroot}%{_datadir}/metainfo/warzone2100.appdata.xml %{buildroot}%{_datadir}/appdata/warzone2100.appdata.xml

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
mv %{buildroot}%{_datadir}/icons/warzone2100.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/warzone2100.png

# remove redundant files
rm %{buildroot}%{_datadir}/doc/%{name}/AUTHORS
rm %{buildroot}%{_datadir}/doc/%{name}/ChangeLog
rm %{buildroot}%{_datadir}/doc/%{name}/COPYING
rm %{buildroot}%{_datadir}/doc/%{name}/COPYING.NONGPL
rm %{buildroot}%{_datadir}/doc/%{name}/COPYING.README
rm %{buildroot}%{_datadir}/doc/%{name}/README.md

%fdupes %{buildroot}%{_datadir}

%files -f %{name}.lang
%license COPYING COPYING.NONGPL COPYING.README
%doc AUTHORS ChangeLog README.md
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/appdata/warzone2100.appdata.xml
%{_datadir}/icons/hicolor/*/apps/warzone2100.png
%{_datadir}/doc/%{name}
%{_mandir}/man6/%{name}.6.*

%files data
%{_datadir}/warzone2100/

%changelog
