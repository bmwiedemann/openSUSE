#
# spec file for package sdrangel
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2026, Martin Hauke <mardnh@gmx.de>
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

# Don't build with LTO since it breaks sdrangel
%define _lto_cflags %{nil}
%ifarch %{ix86} %{arm}
%bcond_with    fec
%else
%bcond_without fec
%endif
%bcond_without freedv
%bcond_with qt6
Name:           sdrangel
Version:        8.2.0
Release:        0
Summary:        SDR/Analyzer frontend for Airspy, BladeRF, HackRF, RTL-SDR and FunCube
License:        GPL-3.0-or-later
URL:            https://github.com/f4exb/sdrangel
# Repacked tarball minus the four rebuilt ThirdParty wasm (all built from
# source in %%build; pristine at https://github.com/f4exb/sdrangel/archive/v8.2.0.tar.gz)
Source:         %{name}-%{version}.tar.gz
Source1:        https://github.com/CesiumGS/cesium-wasm-utils/archive/96a2fbae7ab1d117dd533fe558f0e061bed6762b.tar.gz#/cesium-wasm-utils-96a2fba.tar.gz
Source2:        wasm-splats-vendor.tar.xz
Source3:        https://static.crates.io/crates/wasm-bindgen-cli/wasm-bindgen-cli-0.2.100.crate
Source4:        rust-src-1.98.1.tar.xz
# Repacked upstream rust-src minus wit-bindgen's prebuilt WASI objects
# (only its sources are read; the wasm32 std is compiled from them)
Source5:        zlib-streams-ff804b0.tar.gz
Source6:        https://github.com/madler/zlib/archive/5a82f71ed1dfc0bec044d9702463dbdf84ea3b71.tar.gz#/zlib-5a82f71.tar.gz
Source7:        splats-check.mjs
Source8:        draco-1.5.7.tar.gz
# Repacked upstream draco minus its prebuilt wasm + nested Unity/Maya
# plugin archives (the Emscripten decoder build needs none of them)
Source9:        basis_universal-1.15_final.tar.gz
# Repacked upstream 1.15_final tag tarball minus its 3 prebuilt wasm
# (webgl encoder/transcoder/videotest builds; the transcoder is rebuilt below)
Source10:       basis-splice.py
# Swaps the source-built factory into the vendored worker bundle (the
# outer Cesium logic is untouched; restores the wasmBinaryFile contract)
Source11:       draco-check.mjs
Source12:       basis-e2e.cjs
# Worker end-to-end smoke test for the rebuilt basis factory + wasm.
Source13:       draco-relink.py
# Adapts the rebuilt draco_decoder.wasm to the linkage interface of the
# shipped Cesium glue (symbol/role-joined names; fails loudly on drift).
Source14:       basis-check-data.tar.xz
# Khronos KTX-Software sample transcode input for the %%check worker test.
# PATCH-FIX-UPSTREAM: draco-emscripten-python3.patch -- use FindPython3 module (cmake>=4 removed FindPythonInterp); backport of upstream 8b1f23e04391 + a4365c7935ca
Patch0:         draco-emscripten-python3.patch
# PATCH-FIX-OPENSUSE: basis-cxx17.patch -- embind needs C++17 (upstream pins C++11)
Patch1:         basis-cxx17.patch
# Repacked upstream archive minus its dist/ prebuilt blobs (rebuilt below)
# and the empty src/zlib submodule placeholder filled from Source6
# Source-Binary-Exception: wasm-splats-vendor.tar.xz:vendor-full/ring-*/pregenerated/* -- other-platform: Windows-only objects; Linux builds ring from its perlasm sources
# Source-Binary-Exception: wasm-splats-vendor.tar.xz:vendor-full/windows_* -- other-platform: Windows import libraries unused by the Linux build
# Source-Binary-Exception: wasm-splats-vendor.tar.xz:vendor-full/walrus-*/benches/fixtures/* -- test-data: benchmark input parsed by tests, never executed
# Source-Binary-Exception: */plugins/channelrx/demodacars/atn/asn1/*.obj -- other-platform: Windows MSVC objects committed upstream; the Linux build compiles only the *.c files
BuildRequires:  binaryen
BuildRequires:  cargo1.98
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  dsdcc-devel >= 1.9.3
BuildRequires:  emscripten
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_headers-devel
BuildRequires:  limesuite-devel
BuildRequires:  nodejs
BuildRequires:  patch
BuildRequires:  pkgconfig
BuildRequires:  python3-ply
BuildRequires:  serialdv-devel
BuildRequires:  pkgconfig(SoapySDR)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(codec2)
BuildRequires:  pkgconfig(faad2)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libacars-2)
BuildRequires:  pkgconfig(libairspy)
BuildRequires:  pkgconfig(libairspyhf)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libbladeRF)
BuildRequires:  pkgconfig(libhackrf)
BuildRequires:  pkgconfig(libiio)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(librtlsdr)
BuildRequires:  pkgconfig(libswscale)
# It does not build with libmirisdr from upstream
# https://github.com/f4exb/libmirisdr-4 is needed
#BuildRequires:  pkgconfig(libmirisdr)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxtrx)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(uhd)
Requires:       python3-requests
%if 0%{with qt6}
#BuildRequires:  libQt6Gui-private-headers-devel
#BuildRequires:  qt6-core-private-devel
%else
BuildRequires:  libQt5Gui-private-headers-devel
%endif
%if 0%{with qt6}
BuildRequires:  pkgconfig(Qt6Charts)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6MultimediaWidgets)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6Positioning)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6QuickWidgets)
BuildRequires:  pkgconfig(Qt6SerialPort)
BuildRequires:  pkgconfig(Qt6StateMachine)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6WebSockets)
BuildRequires:  pkgconfig(Qt6Widgets)
%else
BuildRequires:  pkgconfig(Qt5Charts)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gamepad)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Positioning)
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5TextToSpeech)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5WebSockets)
BuildRequires:  pkgconfig(Qt5Widgets)
%endif
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(opencv4)
%else
BuildRequires:  pkgconfig(opencv)
%endif
%if 0%{with fec}
BuildRequires:  pkgconfig(libcm256cc)
BuildRequires:  pkgconfig(nanomsg)
%endif
%if 0%{with freedv}
BuildRequires:  pkgconfig(codec2)
%endif

%description
SDRangel is an Open Source Qt5/OpenGL SDR and signal analyzer frontend
to various hardware.

%prep
%setup -q
sed -i 's/\r$//' Readme.md
sed -i 's|#!%{_bindir}/env python|#!%{_bindir}/python3|g' swagger/sdrangel/examples/*.py
# Stage the wasm sources (built in %%build to replace the dropped blobs)
mkdir wasm-src wasm-zlib wasm-vendor wasm-cli rust-src-full draco-1.5.7 basis-univ
tar -xzf %{SOURCE1} -C wasm-src --strip-components=1
tar -xzf %{SOURCE5} -C wasm-zlib --strip-components=1
mkdir -p wasm-zlib/src/zlib
tar -xzf %{SOURCE6} -C wasm-zlib/src/zlib --strip-components=1
tar -xJf %{SOURCE2} -C wasm-vendor --strip-components=1
tar -xzf %{SOURCE3} -C wasm-cli --strip-components=1
tar -xJf %{SOURCE4} -C rust-src-full
tar -xzf %{SOURCE8} -C draco-1.5.7 --strip-components=1
tar -xzf %{SOURCE9} -C basis-univ --strip-components=1
# Upstream backport: FindPythonInterp is gone in cmake>=4
patch -p1 -s --no-backup-if-mismatch < %PATCH0
# System emscripten embind needs C++17 (upstream pins C++11)
patch -d basis-univ -p1 -s --no-backup-if-mismatch < %PATCH1

%build
# Rebuild the four dropped ThirdParty wasm blobs from source in place
# of the prebuilt ones
cd %{_builddir}/%{name}-%{version}
export CARGO_NET_OFFLINE=true RUSTC_BOOTSTRAP=1
export CARGO_TARGET_DIR=$PWD/wasm-target
WASM_CFG1='source.crates-io.replace-with="vendored-sources"'
WASM_CFG2="source.vendored-sources.directory=\"$PWD/wasm-vendor\""
# wasm32 std for the pinned toolchain: system rustc ships host std only and
# /usr is read-only, so shadow its sysroot with the matching rust-src.
mkdir -p shadow-sysroot/lib/rustlib/src/rust
cp -r rust-src-full/rust-src-*/rust-src/lib/rustlib/src/rust/library shadow-sysroot/lib/rustlib/src/rust/
RUSTC_REAL=$(command -v rustc)
REAL_SYSROOT=$($RUSTC_REAL --print sysroot)
export RUSTC_REAL REAL_SYSROOT SHADOW_SYSROOT
SHADOW_SYSROOT=$PWD/shadow-sysroot
# Shadow answers rustc's sysroot probes (read-only /usr); the wrapper also
# adds the forgotten panic-runtime --extern to cdylib builds once built.
cat > rustc-wasm.sh <<'WRAPEOF'
#!/bin/bash
if [ " $* " = " --print sysroot " ] || [ " $* " = " --print=sysroot " ]; then
  echo "$SHADOW_SYSROOT"
  exit 0
fi
case " $* " in
  *" --print=sysroot "*|*" --print sysroot "*)
    set -o pipefail
    "$RUSTC_REAL" "$@" | sed "s|^${REAL_SYSROOT}\$|${SHADOW_SYSROOT}|"
    exit $?
    ;;
esac
case " $* " in
  *" --target wasm32-unknown-unknown "*)
    case " $* " in
      *" --crate-type cdylib "*)
        case " $* " in
          *" --print "*|*" --crate-name ___ "*) ;;
          *)
            ABORT=$(ls -t "$CARGO_TARGET_DIR"/wasm32-unknown-unknown/release/deps/libpanic_abort-*.rlib 2>/dev/null | head -1)
            [ -n "$ABORT" ] && set -- "$@" --extern "panic_abort=$ABORT"
            ;;
        esac
        ;;
    esac
    ;;
esac
exec "$RUSTC_REAL" "$@"
WRAPEOF
chmod +x rustc-wasm.sh
export RUSTC=$PWD/rustc-wasm.sh
# wasm_splats_bg.wasm (CesiumGS/cesium-wasm-utils, Apache-2.0): plain cargo
# build plus the era-matching wasm-bindgen CLI from the same vendor tree
cargo build --offline --release -Z build-std --target wasm32-unknown-unknown \
  --manifest-path wasm-src/wasm-splats/Cargo.toml \
  --config "$WASM_CFG1" --config "$WASM_CFG2"
rm -f wasm-cli/Cargo.lock
(cd wasm-cli && cargo build --offline --release \
  --config "$WASM_CFG1" --config "$WASM_CFG2")
wasm-target/release/wasm-bindgen --target web --no-typescript \
  --out-dir wasm-out \
  wasm-target/wasm32-unknown-unknown/release/wasm_splats.wasm
cp wasm-out/wasm_splats_bg.wasm \
  plugins/feature/map/Cesium/ThirdParty/wasm_splats_bg.wasm
# zip-module.wasm (gildas-lormeau/zlib-streams, BSD-3-Clause): upstream recipe
%make_build -C wasm-zlib zip_module EMCC=emcc WASM_OPT=wasm-opt
cp wasm-zlib/dist/zip-module.wasm \
  plugins/feature/map/Cesium/ThirdParty/zip-module.wasm
# draco_decoder.wasm (google/draco 1.5.7, Apache-2.0): upstream Emscripten
# decoder recipe; draco-relink.py adapts its linkage to the shipped glue.
export EMSCRIPTEN=%{_datadir}/emscripten
mkdir draco-build && cd draco-build
# FIXME: you should use the %%cmake macros
emcmake cmake ../draco-1.5.7 -DCMAKE_BUILD_TYPE=Release -DDRACO_WASM=ON
%make_build draco_decoder
cd ..
python3 %{SOURCE13} draco-1.5.7/javascript/npm/draco3d/draco_decoder_nodejs.js \
  draco-build/draco_decoder.js draco-build/draco_decoder.wasm \
  draco-build/draco_decoder.relinked.wasm "a:b,b:c,c:e,d:d,e:a"
# new->old runtime imports: throw->b, fd_write->c, resize_heap->e,
# fd_close->d (decoder opens no fds), abort->a; rest derived in script.
cp draco-build/draco_decoder.relinked.wasm \
  plugins/feature/map/Cesium/ThirdParty/draco_decoder.wasm
# basis (BinomialLLC/basis_universal 1.15_final): upstream webgl/transcoder
# recipe; basis-splice.py swaps the fresh factory into the worker bundle.
mkdir basis-build && cd basis-build
# Upstream declares cmake_minimum_required(VERSION 3.0), refused by cmake>=4
export CMAKE_POLICY_VERSION_MINIMUM=3.5
# FIXME: you should use the %%cmake macros
emcmake cmake ../basis-univ/webgl/transcoder -DCMAKE_BUILD_TYPE=Release
%make_build
# Link paths in objects1.rsp are relative to this dir (as in the recipe run)
mkdir -p ../basis-glue
%{_datadir}/emscripten/em++ --bind -s ALLOW_MEMORY_GROWTH=1 -O3 -s ASSERTIONS=0 \
  -s MODULARIZE=1 -s EXPORT_NAME=BASIS -sEXPORTED_RUNTIME_METHODS=HEAP8,HEAPU8 \
  -Wl,--export-all @CMakeFiles/basis_transcoder.js.dir/objects1.rsp \
  -o ../basis-glue/basis_transcoder.js
cd ..
python3 %{SOURCE10} basis-glue/basis_transcoder.js \
  plugins/feature/map/Cesium/Workers/transcodeKTX2.js \
  plugins/feature/map/Cesium/Workers/transcodeKTX2.js.new
mv plugins/feature/map/Cesium/Workers/transcodeKTX2.js.new \
  plugins/feature/map/Cesium/Workers/transcodeKTX2.js
cp basis-glue/basis_transcoder.wasm \
  plugins/feature/map/Cesium/ThirdParty/basis_transcoder.wasm
export CXXFLAGS="%{optflags} -Wno-return-type -fpermissive"
%cmake \
%if 0%{with qt6}
  -DENABLE_QT6=ON \
%endif
  -DCMAKE_SHARED_LINKER_FLAGS="" \
  -DCMAKE_SKIP_RPATH:BOOL=OFF \
  -DCMAKE_BUILD_TYPE=Release \
  -DENABLE_DISTRIBUTION=ON \
%ifarch i586 x86_64
  -DFORCE_SSE41=ON \
%endif
  -DRX_SAMPLE_24BIT=ON
%make_jobs

%check
cd %{_builddir}/%{name}-%{version}
# Upstream's own AES-HMAC suite for the rebuilt zip-module.wasm (needs node)
%make_build -C wasm-zlib test_zip_module
# Smoke-test the rebuilt wasm_splats_bg.wasm against verified outputs
node %{SOURCE7} wasm-out
# Draco decode tests with draco's own glue and test data (needs node)
mkdir -p draco-check
cp draco-1.5.7/javascript/npm/draco3d/draco_decoder_nodejs.js draco-1.5.7/javascript/npm/draco3d/bunny.drc draco-check/
cp draco-1.5.7/testdata/cube_pc.drc draco-1.5.7/testdata/cube_att.drc draco-check/
cp draco-build/draco_decoder.relinked.wasm draco-check/draco_decoder.wasm
node %{SOURCE11} draco-check
# Basis worker end-to-end: the spliced bundle + rebuilt wasm transcode
# kodim23.ktx2 through the real worker task path (needs node)
mkdir -p basis-check
tar -xf %{SOURCE14} -C basis-check
mv basis-check/test/kodim23.ktx2 basis-check/ && rmdir basis-check/test
cp plugins/feature/map/Cesium/ThirdParty/basis_transcoder.wasm basis-check/
node %{SOURCE12} plugins/feature/map/Cesium/Workers/transcodeKTX2.js basis-check

%install
%cmake_install
rm %{buildroot}%{_datadir}/sdrangel/Readme.md
rm %{buildroot}%{_bindir}/tools.json

%files
%license LICENSE
%doc Readme.md
%doc swagger/sdrangel/examples/
%{_bindir}/sdrangel
%{_bindir}/sdrangel-%{version}-linux.mcpb
%{_bindir}/sdrangelbench
%{_bindir}/sdrangelsrv
%{_bindir}/sdrangel-mcp-bridge

%dir %{_libdir}//sdrangel
%{_libdir}/sdrangel/lib*
%{_libdir}/sdrangel/plugins
%{_libdir}/sdrangel/pluginssrv
%{_datadir}/applications/sdrangel.desktop
%{_datadir}/icons/hicolor/scalable/apps/sdrangel_icon.svg
%{_datadir}/metainfo/org.sdrangel.SDRangel.metainfo.xml

%changelog
