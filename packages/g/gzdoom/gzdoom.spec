#
# spec file for package gzdoom
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


Name:           gzdoom
Version:        4.4.2
Release:        0
Summary:        A DOOM source port with graphic and modding extensions
License:        GPL-3.0-only
Group:          Amusements/Games/3D/Shoot
URL:            https://zdoom.org/

#Git-Clone:     https://github.com/coelckers/gzdoom
Source:         https://github.com/coelckers/gzdoom/archive/g%version.tar.gz
Patch1:         gzdoom-waddir.patch
Patch2:         gzdoom-lzma.patch
Patch3:         gzdoom-asmjit.patch
Patch4:         gzdoom-spirv.patch
Patch5:         gzdoom-sdlbug.patch
Patch6:         gzdoom-vulkan.patch
BuildRequires:  cmake >= 2.8.7
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  nasm
BuildRequires:  pkg-config
BuildRequires:  unzip
BuildRequires:  zmusic-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(clzma) >= 17.01
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
%if 0%{?sle_version} >= 150200
BuildRequires:  glslang-devel >= 6.3
BuildRequires:  pkgconfig(vulkan) >= 1.1.77
%else
Provides:       bundled(glslang) = 8.13.3559
Provides:       bundled(vulkan) = 1.1.114
%endif
Suggests:       freedoom
Provides:       qzdoom = 1.3.0
Provides:       zdoom = 2.8.1
# DUMB is modified to read OggVorbis samples
Provides:       bundled(gdtoa)
Provides:       bundled(re2c) = 0.16.0
Provides:       bundled(xbrz) = 1.7

%description
GZDoom is a port (a modification) of the original Doom source code, featuring:
* an OpenGL renderer, HQnX/xBRZ rescaling, 3D floor and model support
* Truecolor software rendering, extending the classic 8-bit palette
* a three-point projection software renderer, extending the classic
  2-point projection
* Heretic, Hexen and Strife game modes and support for a lot of
  additional IWADs.
* Boom and Hexen map extension support, scriptability with ACS and
  ZScript, and various modding features regarding actors and scenery.
* Demo record/playback of classic and Boom demos is not supported.

%prep
%setup -qn %name-g%version
%patch -P 1 -P 2 -P 3 -P 4 -P 5 -p1
%if 0%{?sle_version} >= 150200
%patch -P 6 -p1
rm -Rf glslang src/common/rendering/vulkan/thirdparty/vulkan
%endif
perl -i -pe 's{__DATE__}{""}g' src/posix/sdl/i_main.cpp

%build
# There is handcrafted assembler, which LTO does not play nice with.
%define _lto_cflags %nil

%ifarch %ix86
# Allow sw to use intrinsics (functions like _mm_set_sd).
# Guarded by cpuid calls by sw.
export CFLAGS="%optflags -msse -msse2"
export CXXFLAGS="%optflags -msse -msse2"
%endif
%cmake -DNO_STRIP=1 \
	-DCMAKE_SHARED_LINKER_FLAGS="" \
	-DCMAKE_EXE_LINKER_FLAGS="" -DCMAKE_MODULE_LINKER_FLAGS="" \
	-DINSTALL_DOCS_PATH="%_defaultdocdir/%name" \
	-DINSTALL_PK3_PATH="%_datadir/doom" \
	-DDYN_OPENAL=OFF
make %{?_smp_mflags}

%install
%cmake_install

%post
echo "INFO: %name: The global IWAD directory is %_datadir/doom."

%files
%_bindir/%name
%_defaultdocdir/%name
%_datadir/doom/

%changelog
