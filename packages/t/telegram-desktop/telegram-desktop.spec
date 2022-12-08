#
# spec file for package telegram-desktop
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


# Disable LTO on TW due to build failures
%if 0%{?suse_version} > 01500
%define _lto_cflags %{nil}
%endif

%define __builder ninja

# gcc10 or higher is required
%if 0%{?suse_version} && ( 0%{?suse_version} < 1500 || ( 0%{?is_opensuse} && 0%{?suse_version} == 1500 && 0%{?sle_version} && 0%{?sle_version} <= 150400 ) )
%bcond_without  compiler_upgrade
%else
%bcond_with     compiler_upgrade
%endif

%define _dwz_low_mem_die_limit  40000000
%define _dwz_max_die_limit     200000000

%define qt_major_version 6

Name:           telegram-desktop
Version:        4.4.1
Release:        0
Summary:        Messaging application with a focus on speed and security
License:        GPL-3.0-only
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/telegramdesktop/tdesktop
Source0:        https://github.com/telegramdesktop/tdesktop/releases/download/v%{version}/tdesktop-%{version}-full.tar.gz
# Use tg_owt-packager.py to prepare tg_owt-master.zip
# Usage: python tg_owt-packager.py --repo-dir $PWD/tg_owt-master
Source1:        tg_owt-packager.py
Source2:        tg_owt-master.zip
%if 0%{?suse_version} > 01500
# PATCH-FIX-OPENSUSE
Patch1:         0001-use-bundled-webrtc.patch
%else
Source3:        rnnoise-git20210122.tar.gz
# PATCH-FIX-OPENSUSE
Patch1:         0002-use-bundled-rnnoise-expected-gsl-ranges-webrtc.patch
%endif
# PATCH-FIX-OPENSUSE
Patch3:         0003-revert-webrtc-cmake-target-file.patch
# PATCH-FIX-OPENSUSE
Patch4:         0004-use-dynamic-x-libraries.patch
# There is an (incomplete) patch available for part of the source:
# https://github.com/desktop-app/lib_base.git 3582bca53a1e195a31760978dc41f67ce44fc7e4
# but tdesktop itself still falls short, and it looks to be something
# that would affect all ILP32 platforms.
# PATCH-FIX-OPENSUSE
Patch5:         0005-qt6-fixes.patch
ExcludeArch:    %ix86 aarch64_ilp32 ppc riscv32
BuildRequires:  appstream-glib
BuildRequires:  chrpath
BuildRequires:  clang
BuildRequires:  cmake >= 3.16
BuildRequires:  desktop-file-utils
BuildRequires:  enchant-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  freetype-devel
%if %{with compiler_upgrade}
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  glibc-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblz4-devel
BuildRequires:  libwebrtc_audio_processing-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  wayland-devel
BuildRequires:  webkit2gtk3-devel
BuildRequires:  xorg-x11-devel
BuildRequires:  xxhash-devel
BuildRequires:  xz
BuildRequires:  yasm
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(Qt%{qt_major_version}Concurrent)
BuildRequires:  cmake(Qt%{qt_major_version}Core)
BuildRequires:  cmake(Qt%{qt_major_version}DBus)
BuildRequires:  cmake(Qt%{qt_major_version}Network)
BuildRequires:  cmake(Qt%{qt_major_version}OpenGL)
BuildRequires:  cmake(Qt%{qt_major_version}Qml)
BuildRequires:  cmake(Qt%{qt_major_version}Quick)
BuildRequires:  cmake(Qt%{qt_major_version}QuickWidgets)
BuildRequires:  cmake(Qt%{qt_major_version}Svg)
BuildRequires:  cmake(Qt%{qt_major_version}WaylandClient)
BuildRequires:  cmake(Qt%{qt_major_version}WaylandCompositor)
BuildRequires:  cmake(Qt%{qt_major_version}Widgets)
%if %{qt_major_version} >= 6
BuildRequires:  qt%{qt_major_version}-gui-private-devel
BuildRequires:  qt%{qt_major_version}-waylandclient-private-devel
BuildRequires:  qt%{qt_major_version}-widgets-private-devel
BuildRequires:  cmake(Qt%{qt_major_version}Core5Compat)
BuildRequires:  cmake(Qt%{qt_major_version}OpenGLWidgets)
%else
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-qtwayland-private-headers-devel
BuildRequires:  pkgconfig(dbusmenu-qt%{qt_major_version})
%endif
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glibmm-2.68)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libpcre16)
BuildRequires:  pkgconfig(libpcrecpp)
BuildRequires:  pkgconfig(libpcreposix)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-glx)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(opusurl)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(portaudiocpp)
BuildRequires:  pkgconfig(protobuf)
# Use system rnnoise on TW, self-build on others
%if 0%{?suse_version} > 01500
BuildRequires:  expect-devel
BuildRequires:  range-v3-devel
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(rnnoise)
%else
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif
BuildRequires:  pkgconfig(tslib)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(zlib)
# Runtime requirements
Requires:       hicolor-icon-theme
Requires:       icu
%if %{qt_major_version} >= 6
Requires:       qt%{qt_major_version}-imageformats
Recommends:     qt%{qt_major_version}-wayland
%else
Requires:       libqt%{qt_major_version}-qtimageformats
Recommends:     libqt%{qt_major_version}-qtwayland
%endif
# TDesktop can fall back to a simple GTK file picker but prefers the portal
Recommends:     xdg-desktop-portal
Recommends:     google-opensans-fonts

%description
Telegram is a non-profit cloud-based instant messaging service.
Users can send messages and exchange photos, videos, stickers, audio and files of any type.
Its client-side code is open-source software but the source code for recent versions is not
always immediately published, whereas its server-side code is closed-source and proprietary.
The service also provides APIs to independent developers.

%prep
%setup -q -n tdesktop-%{version}-full
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0
mkdir ../Libraries

# If not TW, unpack rnnoise source
%if 0%{?suse_version} <= 01500
%setup -q -T -D -b 3 -n tdesktop-%{version}-full
mv ../rnnoise-git20210122 ../Libraries/rnnoise
%endif

cd ../
unzip -q %{SOURCE2}
mv tg_owt-master Libraries/tg_owt

%build
%if %{with compiler_upgrade}
export CC=gcc-10
export CXX=g++-10
%endif

# Fix build failures due to not finding installed headers for xkbcommon and wayland-client
export CXXFLAGS+="`pkg-config --cflags xkbcommon wayland-client`"

# If not TW, build rnnoise
%if 0%{?suse_version} <= 01500
pushd %{_builddir}/Libraries/rnnoise
./autogen.sh
%configure
%make_build
popd
%endif

cd %{_builddir}/Libraries/tg_owt
mkdir -p out/Release
cd out/Release
cmake -G Ninja \
       -DCMAKE_BUILD_TYPE=Release \
       -DTG_OWT_SPECIAL_TARGET=linux \
       -DTG_OWT_LIBJPEG_INCLUDE_PATH=/usr/include \
       -DTG_OWT_OPENSSL_INCLUDE_PATH=/usr/include/openssl \
       -DTG_OWT_OPUS_INCLUDE_PATH=/usr/include/opus \
       -DTG_OWT_FFMPEG_INCLUDE_PATH=/usr/include/ffmpeg \
       -DTG_OWT_LIBVPX_INCLUDE_PATH=/usr/include/vpx \
       ../..
sed -i 's,gnu++2a,gnu++17,g' build.ninja
ninja

cd %{_builddir}/tdesktop-%{version}-full
# Use the official API key that telegram uses for their snap builds:
# https://github.com/telegramdesktop/tdesktop/blob/8fab9167beb2407c1153930ed03a4badd0c2b59f/snap/snapcraft.yaml#L87-L88
# Thanks to @primeos on Github.
%cmake \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_BUILD_TYPE=Release \
%if %{qt_major_version} == 6
      -DDESKTOP_APP_QT6=ON \
      -DQT_VERSION_MAJOR=6 \
%else
      -DDESKTOP_APP_QT6=OFF \
      -DDESKTOP_APP_DISABLE_WAYLAND_INTEGRATION=ON \
      -DDESKTOP_APP_USE_ENCHANT=ON \
%endif
      -DTDESKTOP_API_ID=611335 \
      -DTDESKTOP_API_HASH=d524b414d21f4d37f08684c1df41ac9c \
      -DDESKTOP_APP_USE_GLIBC_WRAPS=OFF \
      -DDESKTOP_APP_USE_PACKAGED=ON \
      -DDESKTOP_APP_QTWAYLANDCLIENT_PRIVATE_HEADERS=OFF \
      -DDESKTOP_APP_USE_PACKAGED_FONTS=ON \
      -DDESKTOP_APP_DISABLE_CRASH_REPORTS=ON \
      -DTDESKTOP_LAUNCHER_BASENAME=%{name} \
      -DDESKTOP_APP_SPECIAL_TARGET=""

%cmake_build

%install
%cmake_install

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%files
%license LICENSE LEGAL
%doc README.md changelog.txt
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/metainfo/*.metainfo.xml

%changelog
