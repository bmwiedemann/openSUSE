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


# We need at least gcc8 or higher to build
%if 0%{?suse_version} < 01550 && 0%{?is_opensuse}
%bcond_without  gcc8
%else
%bcond_with     gcc8
%endif

# Disable LTO on TW due to build failures
%if 0%{?suse_version} > 01500
%define _lto_cflags %{nil}
%endif

Name:           telegram-desktop
Version:        1.9.3
Release:        0
Summary:        Messaging application with a focus on speed and security
License:        GPL-3.0-only
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/telegramdesktop/tdesktop
Source0:        https://github.com/telegramdesktop/tdesktop/releases/download/v%{version}/tdesktop-%{version}-full.tar.gz
# curl https://codeload.github.com/ericniebler/range-v3/zip/master -o range-v3-master.zip
Source1:        range-v3-master.zip
Patch0:         0000-gtk2-default.patch 
Patch1:         0001-Dynamic-linking-system-libs.patch 
Patch2:         0002-Dynamic-linking-system-qt.patch 
Patch3:         0004-gtk3.patch 
Patch4:         0005-Use-system-wide-fonts.patch 
Patch5:         0006-Revert-Disable-DemiBold-fallback-for-Semibold.patch
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  ffmpeg-devel
BuildRequires:  freetype-devel
%if %{with gcc8}
BuildRequires:  gcc8-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  enchant-devel
BuildRequires:  glibc-devel
BuildRequires:  libQt5Core-private-headers-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblz4-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libqt5-qtimageformats-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  xorg-x11-devel
BuildRequires:  xxhash-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:  pkgconfig(dee-1.0)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(harfbuzz)
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
Requires:       libappindicator1
Requires:       openssl
ExclusiveArch:  x86_64

%description
Telegram is a non-profit cloud-based instant messaging service.
Users can send messages and exchange photos, videos, stickers, audio and files of any type.
Its client-side code is open-source software but the source code for recent versions is not
always immediately published, whereas its server-side code is closed-source and proprietary.
The service also provides APIs to independent developers.

%prep
%setup -q -n tdesktop-%{version}-full

unzip %{_sourcedir}/range-v3-master.zip -d %{_builddir}/Libraries/
mv %{_builddir}/Libraries/range-v3-master %{_builddir}/Libraries/range-v3

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%if %{with gcc8}
export CC=/usr/bin/gcc-8
export CXX=/usr/bin/g++-8
%endif

cmake -B build -G Ninja . \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DCMAKE_BUILD_TYPE=Release \
      -DTDESKTOP_API_ID=340630 \
      -DTDESKTOP_API_HASH=98a22f733eac40f1bd187a30d19271de \
      -DDESKTOP_APP_USE_GLIBC_WRAPS=OFF \
      -DDESKTOP_APP_USE_SYSTEM_LIBS=ON \
      -DDESKTOP_APP_DISABLE_CRASH_REPORTS=ON \
      -DTDESKTOP_DISABLE_AUTOUPDATE=ON \
      -DTDESKTOP_DISABLE_REGISTER_CUSTOM_SCHEME=ON \
      -DTDESKTOP_DISABLE_DESKTOP_FILE_GENERATION=ON \
      -DDESKTOP_APP_SPECIAL_TARGET=""

ninja -C build

%install
# Install binary
install -dm755 %{buildroot}%{_bindir}
install -m755 build/bin/Telegram %{buildroot}%{_bindir}/%{name}

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    --add-category InstantMessaging \
    lib/xdg/telegramdesktop.desktop

# Install protocol
install -d %{buildroot}%{_datadir}/kservices5
install -m644 lib/xdg/tg.protocol \
        %{buildroot}%{_datadir}/kservices5/tg.protocol

# Install icons
for icon_size in 16 32 48 64 128 256 512; do
    icon_dir="%{buildroot}%{_datadir}/icons/hicolor/${icon_size}x${icon_size}/apps"
    install -d "${icon_dir}"
    install -m644 "Telegram/Resources/art/icon${icon_size}.png" \
            "${icon_dir}/telegram.png"
done

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/telegramdesktop.desktop
%dir %{_datadir}/kservices5
%{_datadir}/kservices5/tg.protocol
%{_datadir}/icons/hicolor/*/apps/telegram.png

%changelog
