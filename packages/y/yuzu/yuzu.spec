#
# spec file for package yuzu
#
# Copyright © 2017–2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright © 2017–2020 Markus S. <kamikazow@opensuse.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#


%define __builder ninja
# For strip binaries
%global cmake_install \
    DESTDIR=%{buildroot} %__builder install/strip -C %__builddir

Name:               yuzu
Version:            01290
Release:            0
Summary:            Nintendo Switch emulator/debugger
License:            GPL-3.0-or-later
Group:              System/Emulators/Other
Url:                https://yuzu-emu.org/
Source0:            %{name}-%{version}.tar.xz
# wget https://api.yuzu-emu.org/gamedb/ -O compatibility_list.json
# It is dynamically changed so we should not use source URL in spec,
# otherwise it will fail source check when submitted to Factory...
Source1:            compatibility_list.json
ExclusiveArch:      x86_64
BuildRequires:      cmake >= 3.15
BuildRequires:      binutils binutils-gold
BuildRequires:      gcc >= 12
BuildRequires:      gcc-c++ >= 12
BuildRequires:      pkgconfig(sdl2) >= 2.0.18
BuildRequires:      libboost_filesystem-devel-impl >= 1.75.0
BuildRequires:      libboost_context-devel-impl >= 1.75.0
BuildRequires:      nasm autoconf
BuildRequires:      pkgconfig(vulkan)
BuildRequires:      glslang-devel
BuildRequires:      sndio-devel
BuildRequires:      pkgconfig(libcurl)
BuildRequires:      pkgconfig(nettle)
BuildRequires:      pkgconfig(openssl)
BuildRequires:      pkgconfig(gnutls)
BuildRequires:      pkgconfig(libpng)
BuildRequires:      pkgconfig(libva)
BuildRequires:      pkgconfig(libpulse)
BuildRequires:      pkgconfig(alsa)
BuildRequires:      pkgconfig(opus)
BuildRequires:      pkgconfig(speexdsp)
BuildRequires:      pkgconfig(jack)

BuildRequires:      pkgconfig(Qt5Core) >= 5.15
BuildRequires:      pkgconfig(Qt5Widgets)
BuildRequires:      pkgconfig(Qt5OpenGL)
BuildRequires:      pkgconfig(Qt5Multimedia)

# ffmpeg
BuildRequires:      pkgconfig(libavcodec)
BuildRequires:      pkgconfig(libavutil)
BuildRequires:      pkgconfig(libswscale)

BuildRequires:      pkgconfig(catch2) >= 2.13.7
BuildRequires:      pkgconfig(fmt) >= 8.0.1
BuildRequires:      pkgconfig(nlohmann_json) >= 3.8
BuildRequires:      pkgconfig(libusb-1.0)
BuildRequires:      pkgconfig(liblz4) >= 1.8
BuildRequires:      pkgconfig(libzstd) >= 1.5
BuildRequires:      pkgconfig(libzip) libzip-tools

BuildRequires:      libqt5-linguist-devel

%if 0%{?fedora} || 0%{?centos_version} || 0%{?rhel_version}
BuildRequires:      ninja-build
%endif
%if 0%{?suse_version}
BuildRequires:      libQt5PlatformSupport-private-headers-devel
BuildRequires:      ninja
%endif

BuildRequires:      hicolor-icon-theme
%if 0%{?suse_version}
BuildRequires:      libQt5Concurrent-devel
BuildRequires:      update-desktop-files
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
