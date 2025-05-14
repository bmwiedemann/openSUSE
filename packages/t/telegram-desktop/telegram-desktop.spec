#
# spec file for package telegram-desktop
#
# Copyright (c) 2025 SUSE LLC
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
%define ada_ver   3.2.4
%define exp_ver   1.1.0
%define h264_ver  2.6.0
%define owt_ver   git20250501
Name:           telegram-desktop
Version:        5.13.1
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
Patch0:         dynamic-link-x.patch
Patch1:         tg_owt-h264-dlopen.patch
Patch2:         Qt-6.9.patch
BuildRequires:  appstream-glib
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libdispatch-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblz4-devel
BuildRequires:  mold
BuildRequires:  ms-gsl-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-waylandclient-private-devel
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  range-v3-devel
BuildRequires:  unzip
BuildRequires:  xxhash-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6WaylandClient)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glibmm-2.68)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
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
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(portaudiocpp)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(rnnoise)
BuildRequires:  pkgconfig(tslib)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(webrtc-audio-processing-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
Requires:       icu
Requires:       qt6-imageformats
Requires:       xdg-desktop-portal
ExclusiveArch:  x86_64 aarch64

%description
Telegram is a non-profit cloud-based instant messaging service.
Users can send messages and exchange photos, videos, stickers, audio and files of any type.
Its client-side code is open-source software but the source code for recent versions is not
always immediately published, whereas its server-side code is closed-source and proprietary.
The service also provides APIs to independent developers.

%prep
%setup -q -n tdesktop-%{version}-full -b1 -b2 -b3
%autopatch -p1 0 2

mkdir -p ../Libraries/ada
mv ../ada-%{ada_ver}/* ../Libraries/ada

mv Telegram/ThirdParty/expected ../Libraries

mkdir -p ../Libraries/openh264/include/wels
mv ../openh264-headers-%{h264_ver}/* ../Libraries/openh264/include/wels

mkdir -p ../Libraries/tg_owt
mv ../tg_owt-%{owt_ver}/* ../Libraries/tg_owt
pushd ../Libraries/tg_owt
%autopatch -p1 1
popd

%build
CFLAGS="%{optflags} -g1 -Wl,-v -fuse-ld=mold"
export CMAKE_GENERATOR=Ninja
mkdir -p %{_builddir}/Libraries/install

cd %{_builddir}/Libraries/ada
%cmake -LA \
      -DBUILD_SHARED_LIBS=OFF \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_C_FLAGS="$CFLAGS" \
      -DCMAKE_CXX_FLAGS="$CFLAGS" \
      -DCMAKE_INSTALL_PREFIX=%{_builddir}/Libraries/install
%cmake_build
ninja install

cd %{_builddir}/Libraries/expected
%cmake -LA \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_C_FLAGS="$CFLAGS" \
      -DCMAKE_CXX_FLAGS="$CFLAGS" \
      -DCMAKE_INSTALL_PREFIX=%{_builddir}/Libraries/install \
      -DEXPECTED_BUILD_PACKAGE=OFF \
      -DEXPECTED_BUILD_TESTS=OFF
%cmake_build
ninja install

cd %{_builddir}/Libraries/tg_owt
%cmake -LA \
      -DBUILD_SHARED_LIBS=OFF \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_C_FLAGS="$CFLAGS" \
      -DCMAKE_CXX_FLAGS="$CFLAGS" \
      -DCMAKE_INSTALL_PREFIX=%{_builddir}/Libraries/install \
      -DTG_OWT_DLOPEN_H264=ON \
      -DTG_OWT_SPECIAL_TARGET=linux \
      -DTG_OWT_LIBJPEG_INCLUDE_PATH=%{_includedir} \
      -DTG_OWT_OPENH264_INCLUDE_PATH=%{_builddir}/Libraries/openh264/include \
      -DTG_OWT_OPENSSL_INCLUDE_PATH=%{_includedir}/openssl \
      -DTG_OWT_OPUS_INCLUDE_PATH=%{_includedir}/opus \
      -DTG_OWT_FFMPEG_INCLUDE_PATH=%{_includedir}/ffmpeg \
      -DTG_OWT_LIBVPX_INCLUDE_PATH=%{_includedir}/vpx
%cmake_build
ninja install

cd %{_builddir}/tdesktop-%{version}-full
%cmake -LA \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_C_FLAGS="$CFLAGS" \
      -DCMAKE_CXX_FLAGS="$CFLAGS" \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_PREFIX_PATH="%{_builddir}/Libraries/install/lib64/cmake;%{_builddir}/Libraries/install/share/cmake/tl-expected" \
      -DDESKTOP_APP_QT6=ON \
      -DQT_VERSION_MAJOR=6 \
      -DTDESKTOP_API_ID=%{api_id} \
      -DTDESKTOP_API_HASH=%{api_hash} \
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

%files
%license LICENSE LEGAL
%doc README.md changelog.txt
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.telegram.desktop.service
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/metainfo/*.metainfo.xml

%changelog
