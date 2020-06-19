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
Version:        2.1.12
Release:        0
Summary:        Messaging application with a focus on speed and security
License:        GPL-3.0-only
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/telegramdesktop/tdesktop
Source0:        https://github.com/telegramdesktop/tdesktop/releases/download/v%{version}/tdesktop-%{version}-full.tar.gz
# PATCH-FIX-OPENSUSE
Patch0:         0000-gtk2-default.patch
# PATCH-FIX-OPENSUSE
Patch1:         0001-use-bundled-range.patch
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
BuildRequires:  memory-constraints
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-devel
BuildRequires:  xxhash-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
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
ExclusiveArch:  x86_64

%description
Telegram is a non-profit cloud-based instant messaging service.
Users can send messages and exchange photos, videos, stickers, audio and files of any type.
Its client-side code is open-source software but the source code for recent versions is not
always immediately published, whereas its server-side code is closed-source and proprietary.
The service also provides APIs to independent developers.

%prep
%setup -q -n tdesktop-%{version}-full

%patch0 -p1
%patch1 -p1

%build
%limit_build -m 2048
%if %{with fixed_gcc}
export CC=/usr/bin/gcc-9
export CXX=/usr/bin/g++-9
%endif

%cmake \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_BUILD_TYPE=Release \
      -DTDESKTOP_API_ID=340630 \
      -DTDESKTOP_API_HASH=98a22f733eac40f1bd187a30d19271de \
      -DDESKTOP_APP_USE_GLIBC_WRAPS=OFF \
      -DDESKTOP_APP_USE_PACKAGED=ON \
      -DDESKTOP_APP_USE_PACKAGED_GSL=OFF \
      -DDESKTOP_APP_USE_PACKAGED_EXPECTED=OFF \
      -DDESKTOP_APP_USE_PACKAGED_RLOTTIE=OFF \
      -DDESKTOP_APP_USE_PACKAGED_VARIANT=OFF \
      -DTDESKTOP_USE_PACKAGED_TGVOIP=OFF \
      -DDESKTOP_APP_USE_PACKAGED_FONTS=ON \
      -DDESKTOP_APP_DISABLE_CRASH_REPORTS=ON \
      -DTDESKTOP_DISABLE_AUTOUPDATE=ON \
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
