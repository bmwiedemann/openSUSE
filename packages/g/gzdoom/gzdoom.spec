#
# spec file for package gzdoom
#
# Copyright (c) 2022 SUSE LLC
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
Version:        4.10.0
Release:        0
Summary:        A DOOM source port with graphic and modding extensions
License:        GPL-3.0-only
Group:          Amusements/Games/3D/Shoot
URL:            https://zdoom.org/

#Git-Clone:     https://github.com/zdoom/gzdoom
Source:         https://github.com/zdoom/gzdoom/archive/g%version.tar.gz
Patch1:         gzdoom-waddir.patch
Patch2:         gzdoom-lzma.patch
Patch5:         gzdoom-vulkan.patch
Patch6:         gzdoom-discord.patch
Patch8:         0001-removed-some-32bit-only-CMake-code.patch
Patch9:         0001-Revert-use-static_assert-to-make-32-bit-builds-fail.patch
BuildRequires:  cmake >= 2.8.7
BuildRequires:  discord-rpc-devel
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  pkg-config
BuildRequires:  unzip
BuildRequires:  zmusic-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(clzma) >= 17.01
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2) >= 2.0.6
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} >= 1550
BuildRequires:  glslang-devel >= 11.10
BuildRequires:  pkgconfig(vulkan) >= 1.2.189
%else
Provides:       bundled(glslang) = 11.10.0
Provides:       bundled(vulkan) = 1.2.189.1
%endif
Suggests:       freedoom
Provides:       qzdoom = 1.3.0
Provides:       zdoom = 2.8.1
Provides:       bundled(gdtoa)
Provides:       bundled(re2c) = 0.16.0
Provides:       bundled(xbrz) = 1.8

%description
GZDoom is a port (a modification) of the original Doom source code, featuring:
* an OpenGL renderer, HQnX/xBRZ rescaling, 3D floor and model support
* Truecolor software rendering, extending the classic 8-bit palette
* Heretic, Hexen and Strife game modes and support for a lot of
  additional IWADs.
* Boom and Hexen map extension support, scriptability with ACS and
  ZScript, and various modding features regarding actors and scenery.
* Demo record/playback of classic and Boom demos is not supported.

The executables hard-require SSE2 on i686 currently.

%prep
%autosetup -n %name-g%version -p1
perl -i -pe 's{__DATE__}{"does not matter when"}g' src/common/platform/posix/sdl/i_main.cpp
perl -i -pe 's{<unknown version>}{%version}g' tools/updaterevision/UpdateRevision.cmake
mkdir -p extra_include/glslang
%if 0%{?suse_version} >= 1550
rm -Rf glslang src/common/rendering/vulkan/thirdparty/vulkan
%else
%patch -P 5 -R -p1
%endif

%build
# There is handcrafted assembler, which LTO does not play nice with.
%define _lto_cflags %nil

export CXXFLAGS="$CXXFLAGS -I$PWD/extra_include"
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
