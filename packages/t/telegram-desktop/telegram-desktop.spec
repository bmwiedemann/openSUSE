#
# spec file for package telegram-desktop
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%define ada_ver   4.1.1
%define owt_ver   git20261122
%define td_ver    git20261123
%define tlottie_ver 1.0.6
%define wallet_engine_ver 0.0.7
Name:           telegram-desktop
Version:        7.4.6
Release:        0
Summary:        Messaging application with a focus on speed and security
License:        GPL-3.0-only
URL:            https://github.com/telegramdesktop/tdesktop
Source0:        https://github.com/telegramdesktop/tdesktop/releases/download/v%{version}/tdesktop-%{version}-full.tar.gz
# n=twidget-vendor && v=7.4.6 && d=$n-$v && f=$d.tar.xz && dt=tdesktop-$v-full && cd /tmp && curl -fsSL https://github.com/telegramdesktop/tdesktop/releases/download/v$v/$dt.tar.gz | tar -xz && pushd $dt/Telegram/ThirdParty/twidget/rust && mkdir .cargo && cargo vendor vendor > .cargo/config.toml && mkdir "$d" && mv .cargo vendor "$d" && tar c --remove-files "$d" | xz -9e > "../../../../../$f" && popd && rm -r "$dt"
Source1:        twidget-vendor-%{version}.tar.xz
Source2:        https://github.com/ada-url/ada/archive/refs/tags/v%{ada_ver}.tar.gz#/ada-%{ada_ver}.tar.gz
# n=tg_owt && cd /tmp && git clone --depth=1 https://github.com/desktop-app/$n && pushd $n && v=git$(TZ=UTC date -d @`git log -1 --format=%at` +%Y%m%d) && d=$n-$v && f=$d.tar.xz && git -c gc.autoDetach=false -c maintenance.autoDetach=false submodule update --init --depth=1 && rm -rf .??* && popd && mv "$n" "$d" && tar c --remove-files "$d" | xz -9e > "$f"
Source3:        tg_owt-%{owt_ver}.tar.xz
# n=td && cd /tmp && git clone --depth=1 https://github.com/tdlib/$n && pushd $n && v=git$(TZ=UTC date -d @`git log -1 --format=%at` +%Y%m%d) && d=$n-$v && f=$d.tar.xz && rm -rf .??* && popd && mv "$n" "$d" && tar c --remove-files "$d" | xz -9e > "$f"
Source4:        td-%{td_ver}.tar.xz
Source5:        https://github.com/dkaraush/tlottie/archive/refs/tags/v%{tlottie_ver}.tar.gz#/tlottie-%{tlottie_ver}.tar.gz
Source6:        tlottie-cargo.toml
# n=wallet-engine && v=0.0.7 && d=$n-$v && f=$d-full.tar.xz && cd /tmp && curl -fsSL https://github.com/i582/wallet-engine/archive/refs/tags/v$v.tar.gz | tar -xz && pushd $d && curl -fsSL https://github.com/desktop-app/patches/raw/refs/heads/master/wallet-engine.patch | patch -p1 --no-backup-if-mismatch && cargo xtask bindings cpp && rm -r .??* target && mkdir .cargo && cargo vendor vendor > .cargo/config.toml && for vd in vendor/*/; do if [ -d "$vd" ] && [ ! -f "$vd/.cargo-checksum.json" ]; then echo '{"files":{}}' > "$vd/.cargo-checksum.json"; fi; done && popd && tar c --remove-files "$d" | xz -9e > "$f"
Source7:        wallet-engine-%{wallet_engine_ver}-full.tar.xz
BuildRequires:  cargo
BuildRequires:  cmake >= 4
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  gperf
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  mold
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  qt6-shadertools
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(Microsoft.GSL)
BuildRequires:  cmake(OpenAL)
BuildRequires:  cmake(Qt6Core) >= 6.12
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  cmake(Qt6WaylandCompositor)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WidgetsPrivate)
BuildRequires:  cmake(libavif)
BuildRequires:  cmake(libheif)
BuildRequires:  cmake(lz4)
BuildRequires:  cmake(protobuf)
BuildRequires:  cmake(qrcodegen)
BuildRequires:  cmake(range-v3)
BuildRequires:  cmake(tiff)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glibmm-2.68)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libfido2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(openh264)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(protobuf-lite)
BuildRequires:  pkgconfig(rnnoise)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-screensaver)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
Requires:       icu
Requires:       kf6-kimageformats
Requires:       xdg-desktop-portal
Recommends:     WebKitGTK-6.0
ExclusiveArch:  x86_64 aarch64

%description
Telegram is a non-profit cloud-based instant messaging service.
Users can send messages and exchange photos, videos, stickers, audio and files of any type.
Its client-side code is open-source software but the source code for recent versions is not
always immediately published, whereas its server-side code is closed-source and proprietary.
The service also provides APIs to independent developers.

%prep
%setup -q -n tdesktop-%{version}-full -b1 -b2 -b3 -b4 -b5 -b7
mkdir -p build/widget_helper_rust
mv ../twidget-vendor-%{version}/{.cargo,vendor} build/widget_helper_rust
mv ../ada-%{ada_ver} Telegram/ThirdParty/ada
mv ../tg_owt-%{owt_ver} Telegram/ThirdParty/tg_owt
mv ../td-%{td_ver} Telegram/ThirdParty/td
mv ../tlottie-%{tlottie_ver} Telegram/ThirdParty/tlottie
install -pm0644 %{SOURCE6} Telegram/ThirdParty/tlottie/Cargo.toml
sed -i 's/TLOTTIE_VER/%{tlottie_ver}/' Telegram/ThirdParty/tlottie/Cargo.toml

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags} -fPIC -g1 -Wl,-v -fuse-ld=mold"
export CXXFLAGS="$CFLAGS"
export CMAKE_GENERATOR="Ninja"
mkdir %{_builddir}/local

cd %{_builddir}/tdesktop-%{version}-full/Telegram/ThirdParty/ada
%cmake -LA \
      -DBUILD_SHARED_LIBS=OFF \
      -DCMAKE_BUILD_TYPE="Release" \
      -DCMAKE_INSTALL_PREFIX="%{_builddir}/local"
%cmake_build
ninja install

cd %{_builddir}/tdesktop-%{version}-full/Telegram/ThirdParty/expected
%cmake -LA \
      -DCMAKE_BUILD_TYPE="Release" \
      -DCMAKE_INSTALL_PREFIX="%{_builddir}/local" \
      -DEXPECTED_BUILD_PACKAGE=OFF \
      -DEXPECTED_BUILD_TESTS=OFF
%cmake_build
ninja install

cd %{_builddir}/tdesktop-%{version}-full/Telegram/ThirdParty/tg_owt
%cmake -LA \
      -DBUILD_SHARED_LIBS=OFF \
      -DCMAKE_BUILD_TYPE="Release" \
      -DCMAKE_INSTALL_PREFIX="%{_builddir}/local" \
      -DTG_OWT_PACKAGED_BUILD=ON
%cmake_build
ninja install

cd %{_builddir}/tdesktop-%{version}-full/Telegram/ThirdParty/td
%cmake -LA \
      -DBUILD_SHARED_LIBS=OFF \
      -DBUILD_TESTING=OFF \
      -DCMAKE_BUILD_TYPE="Release" \
%ifarch aarch64
      -DCMAKE_C_FLAGS="%{optflags} -fPIC -g1 -Wl,-v" \
      -DCMAKE_CXX_FLAGS="%{optflags} -fPIC -g1 -Wl,-v" \
%endif
      -DCMAKE_INSTALL_PREFIX="%{_builddir}/local" \
      -DTD_E2E_ONLY=ON
%cmake_build
ninja install

cd %{_builddir}/tdesktop-%{version}-full/Telegram/ThirdParty/tlottie
cargo build --release --offline --features c-api
install -Dpm0644 target/release/libtlottie.a %{_builddir}/local/lib64/libtlottie.a
install -Dpm0644 include/tlottie.h %{_builddir}/local/include/tlottie/tlottie.h

cd %{_builddir}/wallet-engine-%{wallet_engine_ver}
cargo build --release --offline
install -Dpm0644 target/release/libwallet_engine.a %{_builddir}/local/lib64/libwallet_engine.a
mkdir -p %{_builddir}/local/include/wallet_engine
install -pm0644 bindings/cpp-experimental/* %{_builddir}/local/include/wallet_engine

cd %{_builddir}/tdesktop-%{version}-full
%cmake -LA \
      -DCMAKE_PREFIX_PATH="%{_builddir}/local" \
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
%dir %{_libexecdir}/TelegramDesktop
%{_libexecdir}/TelegramDesktop/TelegramWidgetHelper
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.telegram.desktop.service
%{_datadir}/icons/hicolor/*/apps/*.{png,svg}
%{_datadir}/metainfo/*.metainfo.xml

%changelog
