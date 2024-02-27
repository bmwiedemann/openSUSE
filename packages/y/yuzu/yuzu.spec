#
# spec file for package yuzu
#
# Copyright (c) 2024 SUSE LLC
# Copyright © 2017–2020 Markus S. <kamikazow@opensuse.org>
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


%define __builder ninja
Name:           yuzu
Version:        0.1725
Release:        0
Summary:        Nintendo Switch emulator/debugger
License:        GPL-3.0-or-later
Group:          System/Emulators/Other
URL:            https://yuzu-emu.org/
Source0:        %{name}-%{version}.tar.xz
# wget https://api.yuzu-emu.org/gamedb/ -O compatibility_list.json
# It is dynamically changed so we should not use source URL in spec,
# otherwise it will fail source check when submitted to Factory...
Source1:        compatibility_list.json
Source2:        https://github.com/lat9nq/tzdb_to_nx/releases/download/221202/221202.zip

BuildRequires:  clang >= 14
BuildRequires:  clang-devel >= 14
BuildRequires:  cmake >= 3.15
BuildRequires:  discord-rpc-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glslang-devel
BuildRequires:  graphviz
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_context-devel-impl >= 1.75.0
BuildRequires:  libboost_filesystem-devel-impl >= 1.75.0
BuildRequires:  libzstd-devel-static
BuildRequires:  mold
BuildRequires:  ninja
BuildRequires:  shaderc
BuildRequires:  sndio-devel
BuildRequires:  unzip
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(catch2) >= 2.13.7
BuildRequires:  pkgconfig(cpp-httplib)
BuildRequires:  pkgconfig(fmt) >= 8.0.1
BuildRequires:  pkgconfig(inih)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(liblz4) >= 1.8
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(libzstd) >= 1.5
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(nlohmann_json) >= 3.8
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(sdl2) >= 2.0.18
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(tinfo)
BuildRequires:  pkgconfig(vulkan) >= 1.3.274

#Qt
BuildRequires:  libQt5PlatformSupport-private-headers-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5WebEngine)

# ffmpeg
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)

ExclusiveArch:  x86_64 aarch64

%description
yuzu is an open source Nintendo Switch emulator/debugger.

%prep
%autosetup
cp %{SOURCE1} dist/compatibility_list/
mkdir -p build/externals/nx_tzdb
unzip %{SOURCE2} -d build/externals/nx_tzdb/nx_tzdb/

# Enforce package versioning in GUI
sed -i \
-e 's|@GIT_BRANCH@|mainline|g' \
-e 's|@GIT_DESC@|%{version}|g' \
-e 's|@BUILD_NAME@|%{name}|g' \
src/common/scm_rev.cpp.in

%build
# Fix "too many open files" error
ulimit -n 2048

# Qt built with gles on aarch64, isn't compatible with opengl.
%cmake \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_C_COMPILER=clang \
        -DCMAKE_CXX_COMPILER=clang++ \
%ifarch x86_64
        -DCMAKE_CXX_FLAGS="-march=x86-64-v2" \
%endif
%ifarch aarch64
        -DCMAKE_CXX_FLAGS="-march=armv8-a" \
%endif
        -DENABLE_QT_TRANSLATION=ON \
        -DENABLE_COMPATIBILITY_LIST_DOWNLOAD=ON \
        -DUSE_DISCORD_PRESENCE=ON \
        -DYUZU_CHECK_SUBMODULES=OFF \
        -DYUZU_CRASH_DUMPS=OFF \
        -DYUZU_ENABLE_COMPATIBILITY_REPORTING=ON \
        -DYUZU_ENABLE_LTO=ON \
        -DYUZU_USE_EXTERNAL_SDL2=ON \
        -DYUZU_USE_EXTERNAL_FFMPEG=ON \
        -DYUZU_USE_EXTERNAL_VULKAN_HEADERS=ON \
        -DYUZU_USE_FASTER_LD=ON \
        -DYUZU_USE_QT_MULTIMEDIA=ON \
        -DYUZU_USE_QT_WEB_ENGINE=ON \
%ifarch aarch64
        -DENABLE_OPENGL=OFF \
%endif
        -DYUZU_TESTS=OFF

%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-cmd
%{_bindir}/%{name}-room
%{_datadir}/applications/org.yuzu_emu.yuzu.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.yuzu_emu.yuzu.svg
%{_datadir}/metainfo/org.yuzu_emu.yuzu.metainfo.xml
%{_datadir}/mime/packages/org.yuzu_emu.yuzu.xml

%changelog
