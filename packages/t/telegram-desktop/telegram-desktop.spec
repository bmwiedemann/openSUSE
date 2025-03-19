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
%define ada_ver   3.2.1
%define owt_ver   git20241202
Name:           telegram-desktop
Version:        5.12.5
Release:        0
Summary:        Messaging application with a focus on speed and security
License:        GPL-3.0-only
URL:            https://github.com/telegramdesktop/tdesktop
Source0:        https://github.com/telegramdesktop/tdesktop/releases/download/v%{version}/tdesktop-%{version}-full.tar.gz
Source1:        https://github.com/ada-url/ada/archive/refs/tags/v%{ada_ver}.tar.gz#/ada-%{ada_ver}.tar.gz
# n=tg_owt && cd /tmp && git clone https://github.com/desktop-app/$n && pushd $n && v=git$(TZ=UTC date -d @`git log -1 --format=%at` +%Y%m%d) && d=$n-$v && f=$d.tar.xz && git submodule update --init && rm -rf .??* && popd && mv $n $d && tar c --remove-files "$d" | xz -9e > "$f"
Source2:        tg_owt-%{owt_ver}.tar.xz
Source3:        tg_owt-dlopen-headers.tar.gz
Patch1:         0001-dynamic-link-x.patch
Patch2:         0002-tg_owt-h264-dlopen.patch
Patch3:         0003-tg_owt-pipewire-1.4.patch
BuildRequires:  appstream-glib
BuildRequires:  chrpath
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  enchant-devel
BuildRequires:  expect-devel
BuildRequires:  ffmpeg-7-libavcodec-devel
BuildRequires:  ffmpeg-7-libavdevice-devel
BuildRequires:  ffmpeg-7-libavfilter-devel
BuildRequires:  ffmpeg-7-libavformat-devel
BuildRequires:  ffmpeg-7-libavutil-devel
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblz4-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3 >= 3.7
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-waylandclient-private-devel
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  range-v3-devel
BuildRequires:  unzip
BuildRequires:  wayland-devel
BuildRequires:  xxhash-devel
BuildRequires:  xz
BuildRequires:  yasm
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6Widgets)
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
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmng)
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
Recommends:     google-opensans-fonts
Recommends:     qt6-wayland
ExclusiveArch:  x86_64 aarch64

%description
Telegram is a non-profit cloud-based instant messaging service.
Users can send messages and exchange photos, videos, stickers, audio and files of any type.
Its client-side code is open-source software but the source code for recent versions is not
always immediately published, whereas its server-side code is closed-source and proprietary.
The service also provides APIs to independent developers.

%prep
%setup -q -n tdesktop-%{version}-full -b1 -b2 -b3
%autopatch -p1 1

mkdir -p %{_builddir}/Libraries/ada
mkdir -p %{_builddir}/Libraries/tg_owt
mkdir -p %{_builddir}/Libraries/openh264/include
mv ../ada-%{ada_ver}/* %{_builddir}/Libraries/ada
mv ../tg_owt-%{owt_ver}/* %{_builddir}/Libraries/tg_owt
mv ../wels %{_builddir}/Libraries/openh264/include

pushd %{_builddir}/Libraries/tg_owt
%autopatch -p1 2 3
popd

%build
mkdir -p %{_builddir}/Libraries/install

pushd %{_builddir}/Libraries/ada
%cmake -LA \
      -G Ninja \
      -B build \
      -DBUILD_SHARED_LIBS=OFF \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX=%{_builddir}/Libraries/install
%cmake_build -C build
ninja install -C build

cd %{_builddir}/Libraries/tg_owt
%cmake -LA \
      -G Ninja \
      -B out/Release \
      -DBUILD_SHARED_LIBS=OFF \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX=%{_builddir}/Libraries/install \
      -DTG_OWT_DLOPEN_H264=ON \
      -DTG_OWT_SPECIAL_TARGET=linux \
      -DTG_OWT_LIBJPEG_INCLUDE_PATH=%{_includedir} \
      -DTG_OWT_OPENH264_INCLUDE_PATH=%{_builddir}/Libraries/openh264/include \
      -DTG_OWT_OPENSSL_INCLUDE_PATH=%{_includedir}/openssl \
      -DTG_OWT_OPUS_INCLUDE_PATH=%{_includedir}/opus \
      -DTG_OWT_FFMPEG_INCLUDE_PATH=%{_includedir}/ffmpeg \
      -DTG_OWT_LIBVPX_INCLUDE_PATH=%{_includedir}/vpx
%cmake_build -C out/Release
ninja install -C out/Release

pushd %{_builddir}/tdesktop-%{version}-full
%cmake -LA \
      -G Ninja \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_C_FLAGS="%{optflags} -g1" \
      -DCMAKE_CXX_FLAGS="%{optflags} -g1" \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_PREFIX_PATH=%{_builddir}/Libraries/install/lib64/cmake \
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
