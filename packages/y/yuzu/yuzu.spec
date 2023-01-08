#
# spec file for package yuzu
#
# Copyright (c) 2023 SUSE LLC
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
# For strip binaries
%global cmake_install \
    DESTDIR=%{buildroot} %__builder install/strip -C %__builddir

Name:           yuzu
Version:        01299
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
ExclusiveArch:  x86_64
BuildRequires:  autoconf
BuildRequires:  binutils
BuildRequires:  binutils-gold
BuildRequires:  cmake >= 3.15
BuildRequires:  gcc >= 12
BuildRequires:  gcc-c++ >= 12
BuildRequires:  glslang-devel
BuildRequires:  libboost_context-devel-impl >= 1.75.0
BuildRequires:  libboost_filesystem-devel-impl >= 1.75.0
BuildRequires:  nasm
BuildRequires:  sndio-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(sdl2) >= 2.0.18
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(vulkan)

BuildRequires:  pkgconfig(Qt5Core) >= 5.15
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)

# ffmpeg
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)

BuildRequires:  libzip-tools
BuildRequires:  pkgconfig(catch2) >= 2.13.7
BuildRequires:  pkgconfig(fmt) >= 8.0.1
BuildRequires:  pkgconfig(liblz4) >= 1.8
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(libzstd) >= 1.5
BuildRequires:  pkgconfig(nlohmann_json) >= 3.8

BuildRequires:  libqt5-linguist-devel

%if 0%{?fedora} || 0%{?centos_version} || 0%{?rhel_version}
BuildRequires:  ninja-build
%endif
%if 0%{?suse_version}
BuildRequires:  libQt5PlatformSupport-private-headers-devel
BuildRequires:  ninja
%endif

BuildRequires:  hicolor-icon-theme
%if 0%{?suse_version}
BuildRequires:  libQt5Concurrent-devel
BuildRequires:  update-desktop-files
%endif

%description
yuzu is an open source Nintendo Switch emulator/debugger.

%prep
%autosetup -p1
cp %{SOURCE1} dist/compatibility_list/

# Enforce package versioning in GUI
sed -i \
-e 's|@GIT_REV@|%{release}|g' \
-e 's|@GIT_BRANCH@|master|g' \
-e 's|@GIT_DESC@|%{version}|g' \
-e 's|@BUILD_NAME@|%{name}|g' \
src/common/scm_rev.cpp.in

# Avoid submodule checks as OBS ensures source consistency
sed -i 's|check_submodules_present()||g' CMakeLists.txt

%build
%cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
        -DYUZU_USE_QT_WEB_ENGINE=OFF \
        -DENABLE_QT_TRANSLATION=ON \
        -DBUILD_SHARED_LIBS=OFF \
        -DYUZU_USE_EXTERNAL_SDL2=OFF \
        -DYUZU_USE_BUNDLED_SDL2=OFF \
        -DYUZU_TESTS=OFF

%cmake_build

%install
%cmake_install

# Delete leftover development files
rm -rf %{?buildroot}%{_includedir}
rm -fr %{buildroot}%{_datadir}/cmake
rm -fr %{buildroot}%{_libdir}/cmake

%if 0%{?suse_version}
%suse_update_desktop_file org.yuzu_emu.yuzu
%endif

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
