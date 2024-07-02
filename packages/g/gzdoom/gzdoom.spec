#
# spec file for package gzdoom
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gzdoom
Version:        4.12.2
Release:        0
Summary:        A DOOM source port with graphic and modding extensions
License:        GPL-3.0-only
Group:          Amusements/Games/3D/Shoot
URL:            https://zdoom.org/

#Git-Clone:     https://github.com/zdoom/gzdoom
Source:         https://github.com/zdoom/gzdoom/archive/g%version.tar.gz
Patch2:         gzdoom-discord.patch
Patch3:         0001-Revert-Switch-to-miniz-from-zlib.patch
Patch4:         gzdoom-lzma-simd.patch
Patch5:         gzdoom-lzma.patch
Patch8:         more-32bit.patch
BuildRequires:  cmake >= 2.8.7
BuildRequires:  discord-rpc-devel
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  pkg-config
BuildRequires:  unzip
BuildRequires:  zmusic-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2) >= 2.0.6
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} >= 1599
BuildRequires:  pkgconfig(clzma) >= 23.01
%else
Provides:       bundled(clzma) = 23.01
%endif
Provides:       qzdoom = 1.3.0
Provides:       zdoom = 2.8.1
Provides:       bundled(gdtoa)
Provides:       bundled(glslang) = 11.10.0
Provides:       bundled(re2c) = 0.16.0
Provides:       bundled(vulkan) = 1.2.189.1
Provides:       bundled(xbrz) = 1.8
Suggests:       freedoom

%description
GZDoom is a port (a modification) of the original Doom source code, featuring:
* an OpenGL renderer, HQnX/xBRZ rescaling, 3D floor and model support
* Truecolor software rendering, extending the classic 8-bit palette
* Heretic, Hexen and Strife game modes and support for a lot of
  additional IWADs.
* Boom and Hexen map extension support, scriptability with ACS and
  ZScript, and various modding features regarding actors and scenery.
* Demo record/playback of classic and Boom demos is not supported.

%ifarch %ix86
SSE2 is a hard requirement even on 32-bit x86.
%endif

%prep
%autosetup -n %name-g%version -p1
%if 0%{?suse_version} < 1599
# system lzma-sdk too old, use bundled copy
%patch -P 5 -R -p1
%endif
# osc/rpm always has the version identifier (only has an effect when snapshots are used via _service files)
perl -i -pe "s{<unknown version>}{%version}g" tools/updaterevision/UpdateRevision.cmake
# https://en.opensuse.org/openSUSE:Reproducible_Builds
perl -i -pe 's{__DATE__}{"'"$SOURCE_DATE_EPOCH"'"}g' src/common/platform/posix/sdl/i_main.cpp

%build
# Disable LTO, which does not like seeing handcrafted assembler
%define _lto_cflags %nil

export CXXFLAGS="$CXXFLAGS -DSHARE_DIR=\\\"%_datadir/doom\\\""
%cmake -DNO_STRIP=1 \
	-DCMAKE_SHARED_LINKER_FLAGS="" \
	-DCMAKE_EXE_LINKER_FLAGS="" -DCMAKE_MODULE_LINKER_FLAGS="" \
	-DINSTALL_DOCS_PATH="%_defaultdocdir/%name" \
	-DINSTALL_PK3_PATH="%_datadir/doom" \
	-DINSTALL_SOUNDFONT_PATH="%_datadir/doom" \
	-DDYN_OPENAL=OFF -DINSTALL_RPATH:STRING="NO"
%cmake_build

%install
%cmake_install

%post
echo "INFO: %name: The global IWAD directory is %_datadir/doom."

%files
%_bindir/%name
%_defaultdocdir/%name
%_datadir/doom/

%changelog
