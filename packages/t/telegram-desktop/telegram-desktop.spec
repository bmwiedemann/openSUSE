#
# spec file for package telegram-desktop
#
# Copyright (c) 2025 SUSE LLC and contributors
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
# https://github.com/telegramdesktop/tdesktop/blob/8fab9167beb2407c1153930ed03a4badd0c2b59f/snap/snapcraft.yaml#L87-L88
%define api_id    611335
%define api_hash  d524b414d21f4d37f08684c1df41ac9c
%define ada_ver   3.3.0
%define h264_ver  2.6.0
%define owt_ver   git20250913
%define td_ver    git20250919
Name:           telegram-desktop
Version:        6.1.4
Release:        0
Summary:        Messaging application with a focus on speed and security
License:        GPL-3.0-only
URL:            https://github.com/telegramdesktop/tdesktop
Source0:        https://github.com/telegramdesktop/tdesktop/releases/download/v%{version}/tdesktop-%{version}-full.tar.gz
Source1:        https://github.com/ada-url/ada/archive/refs/tags/v%{ada_ver}.tar.gz#/ada-%{ada_ver}.tar.gz
# v=2.6.0 && n=openh264 && d=$n-headers-$v && f=$d.tar.xz && cd /tmp && git clone -bv$v --depth=1 https://github.com/cisco/$n.git && mkdir $d && mv $n/codec/api/wels/*.h $d && rm -rf $n && tar c --remove-files "$d" | xz -9e > "$f"
Source2:        openh264-headers-%{h264_ver}.tar.xz
# n=tg_owt && cd /tmp && git clone --depth=1 https://github.com/desktop-app/$n && pushd $n && v=git$(TZ=UTC date -d @`git log -1 --format=%at` +%Y%m%d) && d=$n-$v && f=$d.tar.xz && git submodule update --init --depth=1 && rm -rf .??* && popd && mv $n $d && tar c --remove-files "$d" | xz -9e > "$f"
Source3:        tg_owt-%{owt_ver}.tar.xz
# n=td && cd /tmp && git clone --depth=1 https://github.com/tdlib/$n && pushd $n && v=git$(TZ=UTC date -d @`git log -1 --format=%at` +%Y%m%d) && d=$n-$v && f=$d.tar.xz && rm -rf .??* && popd && mv $n $d && tar c --remove-files "$d" | xz -9e > "$f"
Source4:        td-%{td_ver}.tar.xz
Patch0:         %{name}-webrtc-link.patch
Patch1:         tg_owt-h264-dlopen.patch
BuildRequires:  QR-Code-generator-devel
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  gcc-c++
#?1
BuildRequires:  glibc-devel
BuildRequires:  gperf
BuildRequires:  kf6-kcoreaddons-devel
#?1
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libdispatch-devel
BuildRequires:  mold
BuildRequires:  ms-gsl-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-waylandclient-private-devel
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  range-v3-devel
BuildRequires:  xxhash-devel
#?1
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
#?1
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
#?1
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6QuickWidgets)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6WaylandCompositor)
#?1
BuildRequires:  pkgconfig(Qt6WaylandClient)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(alsa)
#?1
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fmt)
#?1
BuildRequires:  pkgconfig(fontconfig)
#?1
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
#?1
BuildRequires:  pkgconfig(glibmm-2.68)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
#?1
BuildRequires:  pkgconfig(gsl)
#?1
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(liblz4)
#?1
BuildRequires:  pkgconfig(liblzma)
#?1
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libpipewire-0.3)
#?1
BuildRequires:  pkgconfig(libpng)
#?1
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libpulse)
#?1
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
#?1
BuildRequires:  pkgconfig(libtiff-4)
#?1
BuildRequires:  pkgconfig(libva)
#?1
BuildRequires:  pkgconfig(libva-glx)
#?1
BuildRequires:  pkgconfig(libva-x11)
#?1
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(minizip)
#?1
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
#?1
BuildRequires:  pkgconfig(portaudio-2.0)
#?1
BuildRequires:  pkgconfig(portaudiocpp)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(rnnoise)
#?1
BuildRequires:  pkgconfig(tslib)
#?1
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(vpx)
#?1
BuildRequires:  pkgconfig(webkitgtk-6.0)
#?1
BuildRequires:  pkgconfig(webrtc-audio-processing-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
#?1
BuildRequires:  pkgconfig(xcb-ewmh)
#?1
BuildRequires:  pkgconfig(xcb-icccm)
#?1
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-record)
#?1
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-screensaver)
#?1
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
#?1
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
Requires:       icu
Requires:       kf6-kimageformats
Requires:       xdg-desktop-portal
ExclusiveArch:  x86_64 aarch64

%description
Telegram is a non-profit cloud-based instant messaging service.
Users can send messages and exchange photos, videos, stickers, audio and files of any type.
Its client-side code is open-source software but the source code for recent versions is not
always immediately published, whereas its server-side code is closed-source and proprietary.
The service also provides APIs to independent developers.

%prep
%setup -q -n tdesktop-%{version}-full -b1 -b2 -b3 -b4
%autopatch -p1 0

mv ../ada-%{ada_ver} Telegram/ThirdParty/ada

mkdir -p Telegram/ThirdParty/openh264/include
mv ../openh264-headers-%{h264_ver} Telegram/ThirdParty/openh264/include/wels

mv ../tg_owt-%{owt_ver} Telegram/ThirdParty/tg_owt
pushd Telegram/ThirdParty/tg_owt
%autopatch -p1 1
popd

mv ../td-%{td_ver} Telegram/ThirdParty/td

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
CFLAGS="%{optflags} -fPIC -g1 -Wl,-v -fuse-ld=mold"
export CMAKE_GENERATOR=Ninja
mkdir %{_builddir}/local

cd %{_builddir}/tdesktop-%{version}-full/Telegram/ThirdParty/ada
%cmake -LA \
      -DBUILD_SHARED_LIBS=OFF \
      -DCMAKE_BUILD_TYPE="Release" \
      -DCMAKE_C_FLAGS="$CFLAGS" \
      -DCMAKE_CXX_FLAGS="$CFLAGS" \
      -DCMAKE_INSTALL_PREFIX="%{_builddir}/local"
%cmake_build
ninja install

cd %{_builddir}/tdesktop-%{version}-full/Telegram/ThirdParty/expected
%cmake -LA \
      -DCMAKE_BUILD_TYPE="Release" \
      -DCMAKE_C_FLAGS="$CFLAGS" \
      -DCMAKE_CXX_FLAGS="$CFLAGS" \
      -DCMAKE_INSTALL_PREFIX="%{_builddir}/local" \
      -DEXPECTED_BUILD_PACKAGE=OFF \
      -DEXPECTED_BUILD_TESTS=OFF
%cmake_build
ninja install

cd %{_builddir}/tdesktop-%{version}-full/Telegram/ThirdParty/tg_owt
%cmake -LA \
      -DBUILD_SHARED_LIBS=OFF \
      -DCMAKE_BUILD_TYPE="Release" \
      -DCMAKE_C_FLAGS="$CFLAGS" \
      -DCMAKE_CXX_FLAGS="$CFLAGS" \
      -DCMAKE_INSTALL_PREFIX="%{_builddir}/local" \
      -DTG_OWT_DLOPEN_H264=ON \
      -DTG_OWT_FFMPEG_INCLUDE_PATH="%{_includedir}/ffmpeg" \
      -DTG_OWT_LIBJPEG_INCLUDE_PATH="%{_includedir}" \
      -DTG_OWT_LIBVPX_INCLUDE_PATH="%{_includedir}/vpx" \
      -DTG_OWT_OPENH264_INCLUDE_PATH="../openh264/include" \
      -DTG_OWT_OPENSSL_INCLUDE_PATH="%{_includedir}/openssl" \
      -DTG_OWT_OPUS_INCLUDE_PATH="%{_includedir}/opus" \
      -DTG_OWT_PACKAGED_BUILD=ON \
      -DTG_OWT_SPECIAL_TARGET="linux"
%cmake_build
ninja install

cd %{_builddir}/tdesktop-%{version}-full/Telegram/ThirdParty/td
%cmake -LA \
      -DBUILD_SHARED_LIBS=OFF \
      -DBUILD_TESTING=OFF \
      -DCMAKE_BUILD_TYPE="Release" \
      -DCMAKE_C_FLAGS="$CFLAGS" \
      -DCMAKE_CXX_FLAGS="$CFLAGS" \
      -DCMAKE_INSTALL_PREFIX="%{_builddir}/local" \
      -DTD_E2E_ONLY=ON
%cmake_build
ninja install

cd %{_builddir}/tdesktop-%{version}-full
%cmake -LA \
      -DCMAKE_BUILD_TYPE="Release" \
      -DCMAKE_C_FLAGS="$CFLAGS" \
      -DCMAKE_CXX_FLAGS="$CFLAGS" \
      -DCMAKE_PREFIX_PATH="%{_builddir}/local/lib64/cmake;%{_builddir}/local/share/cmake" \
      -DDESKTOP_APP_DISABLE_QT_PLUGINS=ON \
      -DDESKTOP_APP_USE_PACKAGED=ON \
      -DDESKTOP_APP_USE_PACKAGED_FONTS=ON \
      -DTDESKTOP_API_ID="%{api_id}" \
      -DTDESKTOP_API_HASH="%{api_hash}"
%cmake_build

%install
%cmake_install

%files
%license LICENSE LEGAL
%doc README.md changelog.txt
%{_bindir}/Telegram
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.telegram.desktop.service
%{_datadir}/icons/hicolor/*/apps/*.{png,svg}
%{_datadir}/metainfo/*.metainfo.xml

%changelog
