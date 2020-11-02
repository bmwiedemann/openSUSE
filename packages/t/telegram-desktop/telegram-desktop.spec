#
# spec file for package telegram-desktop
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


# Disable LTO on TW due to build failures
%if 0%{?suse_version} > 01500
%define _lto_cflags %{nil}
%endif

# We need at least gcc8 or higher to build
%if 0%{?suse_version} < 01550 && 0%{?is_opensuse}
%bcond_without  fixed_gcc
%else
%bcond_with     fixed_gcc
%endif

%define __builder ninja

Name:           telegram-desktop
Version:        2.4.5
Release:        0
Summary:        Messaging application with a focus on speed and security
License:        GPL-3.0-only
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/telegramdesktop/tdesktop
Source0:        https://github.com/telegramdesktop/tdesktop/releases/download/v%{version}/tdesktop-%{version}-full.tar.gz
# tg_owt: https://github.com/desktop-app/tg_owt/archive/master.zip
Source1:        tg_owt-master.zip
# PATCH-FIX-OPENSUSE
Patch0:         0000-gtk2-default.patch
# PATCH-FIX-OPENSUSE
Patch1:         0001-use-bundled-ranged-exptected-gsl.patch
# PATCH-FIX-OPENSUSE
Patch2:         0002-tg_owt-fix-name-confliction.patch
BuildRequires:  appstream-glib
BuildRequires:  chrpath
BuildRequires:  cmake >= 3.16
BuildRequires:  desktop-file-utils
BuildRequires:  enchant-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  freetype-devel
%if %{with fixed_gcc}
BuildRequires:  gcc9-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  glibc-devel
BuildRequires:  libQt5Core-private-headers-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblz4-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libqt5-qtimageformats-devel
BuildRequires:  libqt5-qtwayland-private-headers-devel
BuildRequires:  libwebrtc_audio_processing-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  xorg-x11-devel
BuildRequires:  xxhash-devel
BuildRequires:  xz
BuildRequires:  yasm
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbusmenu-qt5)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(hunspell)
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
BuildRequires:  pkgconfig(tslib)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(zlib)
# Runtime requirements
Requires:       ffmpeg
Requires:       hicolor-icon-theme
Requires:       icu
Requires:       openssl
# TDesktop can fall back to a simple GTK file picker but prefers the portal
Recommends:     xdg-desktop-portal
Recommends:     libqt5-qtwayland

%description
Telegram is a non-profit cloud-based instant messaging service.
Users can send messages and exchange photos, videos, stickers, audio and files of any type.
Its client-side code is open-source software but the source code for recent versions is not
always immediately published, whereas its server-side code is closed-source and proprietary.
The service also provides APIs to independent developers.

%prep
%setup -q -n tdesktop-%{version}-full
%patch0 -p1
%patch1 -p2

cd ../
unzip %{S:1}
mkdir Libraries
mv tg_owt-master Libraries/tg_owt
%patch2 -p2 -d Libraries/tg_owt

%build
%if %{with fixed_gcc}
export CC=/usr/bin/gcc-9
export CXX=/usr/bin/g++-9
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

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files
%license LICENSE LEGAL
%doc README.md changelog.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/metainfo/*.appdata.xml

%changelog
