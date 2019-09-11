#
# spec file for package telegram-desktop
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.8.4
Release:        0
Summary:        Messaging application with a focus on speed and security
License:        GPL-3.0-only
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/telegramdesktop/tdesktop
Source0:        https://github.com/telegramdesktop/tdesktop/archive/v%{version}.tar.gz
# curl https://chromium.googlesource.com/breakpad/breakpad/+archive/refs/heads/master.tar.gz -o breakpad-master.tar.gz
Source1:        breakpad-master.tar.gz
# curl https://chromium.googlesource.com/linux-syscall-support/+archive/master.tar.gz -o linux-syscall-support-refs-heads-master.tar.gz
Source2:        linux-syscall-support-refs-heads-master.tar.gz
# curl https://chromium.googlesource.com/external/gyp/+archive/master.tar.gz -o gyp-master.tar.gz
Source3:        gyp-master.tar.gz
Source4:        patch.py
# curl https://codeload.github.com/Microsoft/GSL/zip/master -o GSL-master.zip
Source5:        GSL-master.zip
# curl https://codeload.github.com/mapbox/variant/zip/master -o variant-master.zip
Source6:        variant-master.zip
# curl https://codeload.github.com/grishka/libtgvoip/zip/public -o libtgvoip.zip
Source7:        libtgvoip.zip
# curl https://raw.githubusercontent.com/philsquared/Catch/master/single_include/catch.hpp -o catch.hpp
Source8:        catch.hpp
# curl https://codeload.github.com/ericniebler/range-v3/zip/master -o range-v3-master.zip
Source9:        range-v3-master.zip
# curl https://codeload.github.com/telegramdesktop/crl/zip/master -o crl-master.zip
Source10:       crl-master.zip
# curl https://codeload.github.com/Cyan4973/xxHash/zip/master -o xxHash-master.zip
Source11:       xxHash-master.zip
# curl https://codeload.github.com/lz4/lz4/zip/dev -o lz4-dev.zip
Source12:       lz4-dev.zip
# curl https://codeload.github.com/john-preston/rlottie/zip/master -o rlottie-master.zip
Source13:       rlottie-master.zip

Patch0:         tdesktop.patch
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
BuildRequires:  glibc-devel
BuildRequires:  libQt5Core-private-headers-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libqt5-qtimageformats-devel
BuildRequires:  pkgconfig
# python2-base is required for gyp, Auto pulled in for Tumbleweed, but need for Leap 15.
BuildRequires:  python2-base
BuildRequires:  python3
BuildRequires:  unzip
BuildRequires:  xorg-x11-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)
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
Conflicts:      libqt5-qtstyleplugins-platformtheme-gtk2
ExclusiveArch:  x86_64

%description
Telegram is a non-profit cloud-based instant messaging service.
Users can send messages and exchange photos, videos, stickers, audio and files of any type.
Its client-side code is open-source software but the source code for recent versions is not
always immediately published, whereas its server-side code is closed-source and proprietary.
The service also provides APIs to independent developers.

%prep
%setup -q -n tdesktop-%{version}
cp %{SOURCE8} Telegram/SourceFiles/base

# Already included in %{S:8}
sed -i "/catch_reporter_compact.hpp/d" Telegram/SourceFiles/base/tests_main.cpp

cp %{_sourcedir}/GSL-master.zip . && unzip GSL-master.zip
mv GSL-master GSL
mv GSL %{_builddir}/tdesktop-%{version}/Telegram/ThirdParty/

cp %{_sourcedir}/variant-master.zip . && unzip variant-master.zip
mv variant-master variant
mv variant %{_builddir}/tdesktop-%{version}/Telegram/ThirdParty/

cp %{_sourcedir}/libtgvoip.zip . && unzip libtgvoip.zip
mv libtgvoip-public libtgvoip
mv libtgvoip %{_builddir}/tdesktop-%{version}/Telegram/ThirdParty/

cp %{_sourcedir}/range-v3-master.zip . && unzip range-v3-master.zip
mv range-v3-master range-v3
mkdir -p %{_builddir}/Libraries
mv range-v3 %{_builddir}/Libraries/

cp %{_sourcedir}/crl-master.zip . && unzip crl-master.zip
mv crl-master crl
mv crl %{_builddir}/tdesktop-%{version}/Telegram/ThirdParty/

cp %{_sourcedir}/rlottie-master.zip . && unzip rlottie-master.zip
mv rlottie-master rlottie
mv rlottie %{_builddir}/tdesktop-%{version}/Telegram/ThirdParty/

cp %{_sourcedir}/lz4-dev.zip . && unzip lz4-dev.zip
mv lz4-dev lz4
mv lz4 %{_builddir}/tdesktop-%{version}/Telegram/ThirdParty/

cp %{_sourcedir}/xxHash-master.zip . && unzip xxHash-master.zip
mv xxHash-master xxHash
mv xxHash %{_builddir}/tdesktop-%{version}/Telegram/ThirdParty/

cp %{_sourcedir}/tdesktop.patch %{_builddir}/tdesktop-%{version}
cd %{_builddir}/tdesktop-%{version}

%patch0 -p1

cp %{_sourcedir}/patch.py . && python3 ./patch.py
cp %{_sourcedir}/catch.hpp ./Telegram/SourceFiles/

%setup -q -T -c -n breakpad -a 1
%setup -q -T -c -n breakpad-lss -a 2
%setup -q -T -c -n gyp -a 3

%build
%if %{with gcc8}
export CC=/usr/bin/gcc-8
export CXX=/usr/bin/g++-8
%endif

mv %{_builddir}/tdesktop-%{version} %{_builddir}/tdesktop

# patch gyp
cd %{_builddir}/Libraries
ln -s %{_builddir}/gyp
cp %{_builddir}/tdesktop/Telegram/Patches/gyp.diff gyp
cd gyp
patch -p1 < gyp.diff

# Build breakpad
cd %{_builddir}/breakpad
ln -s %{_builddir}/breakpad-lss src/third_party/lss
%configure
%make_build
make %{?_smp_mflags} install DESTDIR=%{_builddir}/Libraries/breakpad

cd %{_builddir}/tdesktop/Telegram/gyp
# patch qt.gypi to change libxkbcommon path
%{_builddir}/Libraries/gyp/gyp \
    -Dapi_id=340630 \
    -Dapi_hash=98a22f733eac40f1bd187a30d19271de \
    -Dlinux_lib_ssl=-lssl \
    -Dlinux_lib_crypto=-lcrypto \
    -Dlinux_lib_icu="-licuuc -licutu -licui18n" \
    -Dlinux_path_opus_include="%{_includedir}/opus" \
    -Dlinux_path_breakpad="%{_builddir}/Libraries/breakpad%{_prefix}" \
    -Gconfig=Release \
    --depth=. --generator-output="%{_builddir}/tdesktop" -Goutput_dir=out Telegram.gyp --format=cmake

# build Telegram
cd %{_builddir}/tdesktop/out/Release
%cmake ..
sed -i 's,breakpad/usr/lib,breakpad%{_libdir},' ./CMakeFiles/Telegram.dir/link.txt
%make_build
chrpath --delete Telegram

%install
# Install binary
install -dm755 %{buildroot}%{_bindir}
install -m755 %{_builddir}/tdesktop/out/Release/build/Telegram %{buildroot}%{_bindir}/%{name}

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    --add-category InstantMessaging \
    %{_builddir}/tdesktop/lib/xdg/telegramdesktop.desktop

# Install protocol
install -d %{buildroot}%{_datadir}/kservices5
install -m644 %{_builddir}/tdesktop/lib/xdg/tg.protocol \
    %{buildroot}%{_datadir}/kservices5/tg.protocol

# Install icons
for icon_size in 16 32 48 64 128 256 512; do
    icon_dir="%{buildroot}%{_datadir}/icons/hicolor/${icon_size}x${icon_size}/apps"
    install -d "${icon_dir}"
    install -m644 "%{_builddir}/tdesktop/Telegram/Resources/art/icon${icon_size}.png" \
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
