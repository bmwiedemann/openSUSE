#
# spec file for package citra
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017–2019 Markus S. <kamikazow@opensuse.org>
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


Name:           citra
Version:        nightly1711
Release:        0
Summary:        Nintendo 3DS emulator
License:        GPL-2.0-or-later
URL:            https://citra-emu.org/
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM https://github.com/neobrain/nihstro/pull/62
Patch0:         gcc-enablement.patch
BuildRequires:  cmake >= 3.6
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_date_time-devel >= 1.70.0
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(sdl2)
ExclusiveArch:  x86_64

%description
Citra is an open-source Nintendo 3DS emulator and debugger, written with portability in mind.

%prep
%setup -q
%autopatch -p1

# Enforce package versioning in GUI
sed -i '$!N;s|#define GIT_REV.*"@GIT_REV@"\n#define GIT_BRANCH.*"@GIT_BRANCH@"|#define GIT_REV\t"%{release}"\n#define GIT_BRANCH\t"nightly"|g;P;D' src/common/scm_rev.cpp.in
sed -i 's|@GIT_DESC@|%{version}|g' src/common/scm_rev.cpp.in
sed -i 's|@BUILD_NAME@|%{name}|g' src/common/scm_rev.cpp.in

# Avoid submodule checks as OBS ensures source consistency
sed -i 's|check_submodules_present()||g' CMakeLists.txt

# Don't test during build phase
sed -i 's|enable_testing()||g' CMakeLists.txt

# do not use bundled libs
#sed -i -e 's|add_subdirectory(externals)||g' CMakeLists.txt

%build
# DYNARMIC_ENABLE_CPU_FEATURE_DETECTION - we can't rely on cpu detection
# CRYPTOPP_DISABLE_CXXFLAGS_OPTIMIZATIONS - use only system set optflags
# WEB_SERVICE/CUBEB/DISCORD_PRESENCE OFF because uses bundled libs and libressl, no-go for openSUSE integration
# SHARED/STATIC_LIBS - we don't do libs it is just bundled helpers we need to link into binaries
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
%cmake \
    -DBUILD_SHARED_LIBS=OFF \
    -DBUILD_STATIC_LIBS=ON \
    -DENABLE_WEB_SERVICE=OFF \
    -DENABLE_CUBEB=OFF \
    -DUSE_DISCORD_PRESENCE=OFF \
    -DDYNARMIC_ENABLE_CPU_FEATURE_DETECTION=OFF \
    -DCRYPTOPP_DISABLE_CXXFLAGS_OPTIMIZATIONS=OFF \
    -DENABLE_FFMPEG_AUDIO_DECODER=ON \
    -DENABLE_FFMPEG_VIDEO_DUMPER=ON \
    -DENABLE_FFMPEG_VIDEO_DUMPER=ON \
    -DCITRA_USE_BUNDLED_FFMPEG=OFF \
    -DENABLE_QT_TRANSLATION=ON \
    -DUSE_SYSTEM_BOOST=ON \
    -DZSTD_LZ4_SUPPORT=ON \
    -DZSTD_LZMA_SUPPORT=ON \
    -DZSTD_PROGRAMS_LINK_SHARED=ON \
    -DZSTD_ZLIB_SUPPORT=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README.md CONTRIBUTING.md
%license license.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-qt
%{_bindir}/%{name}-room
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
