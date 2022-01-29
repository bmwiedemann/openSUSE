#!/bin/bash

# Copyright (c) 2021 Andreas Schneider <asn@cryptomilk.org>
# License: GPLv3

ELECTRON_PKGVERSION=$(rpmspec -P *.spec | grep Version | sed -e 's/Version:[ ]*//g')
ELECTRON_PKGNAME="electron"
ELECTRON_PKGDIR="$(pwd)"
ELECTRON_TMPDIR=$(mktemp --tmpdir -d electron-XXXXXXXX)
ELECTRON_PATH="${ELECTRON_TMPDIR}/${ELECTRON_PKGNAME}-${ELECTRON_PKGVERSION}"

echo "NAME:    $ELECTRON_PKGNAME"
echo "VERSION: $ELECTRON_PKGVERSION"
echo "PATH:    $ELECTRON_PATH"

cleanup_tmpdir() {
    popd 2>/dev/null
    rm -rf $ELECTRON_TMPDIR
}
trap cleanup_tmpdir SIGINT

cleanup_and_exit() {
    cleanup_tmpdir
    if test "$1" = 0 -o -z "$1" ; then
        exit 0
    else
        exit $1
    fi
}

pushd "$ELECTRON_TMPDIR" || cleanup_and_exit 1

echo ">>>>>> Downloading depot tools"
git clone --depth=1 https://chromium.googlesource.com/chromium/tools/depot_tools.git
if [ $? -ne 0 ]; then
    echo "ERROR: git clone depot_tools failed"
    cleanup_and_exit 1
fi
PATH="$(pwd)/depot_tools:$PATH"
export PATH


echo ">>>>>> Create gclient config"
cat >.gclient <<EOF
solutions = [
  {
    "name"        : "src/electron",
    "url"         : "https://github.com/electron/electron",
    "deps_file"   : "DEPS",
    "managed"     : False,
  },
]
EOF

echo ">>>>>> Downloading electron-${ELECTRON_PKGVERSION}"
gclient sync --jobs 4 --nohooks --with_branch_heads --with_tags --revision=v${ELECTRON_PKGVERSION}
if [ $? -ne 0 ]; then
    echo "ERROR: gclient sync failed"
    cleanup_and_exit 1
fi

echo ">>>>>> Apply electron-${ELECTRON_PKGVERSION} patches"
python3 src/electron/script/apply_all_patches.py \
      src/electron/patches/config.json
if [ $? -ne 0 ]; then
    echo "ERROR: apply_all_patches.py failed"
    cleanup_and_exit 1
fi

echo ">>>>>> Generate GPU_LISTS_VERSION"
python3 src/build/util/lastchange.py -m GPU_LISTS_VERSION \
    --revision-id-only --header src/gpu/config/gpu_lists_version.h
if [ $? -ne 0 ]; then
    echo "ERROR: lastchange.py -m GPU_LISTS_VERSION failed"
    cleanup_and_exit 1
fi

echo ">>>>>> Generate SKIA_COMMIT_HASH"
python3 src/build/util/lastchange.py -m SKIA_COMMIT_HASH \
    -s src/third_party/skia --header src/skia/ext/skia_commit_hash.h
if [ $? -ne 0 ]; then
    echo "ERROR: lastchange.py -m SKIA_COMMIT_HASH failed"
    cleanup_and_exit 1
fi

echo ">>>>>> Download optimization profile"
python3 src/tools/download_optimization_profile.py \
    --newest_state=src/chrome/android/profiles/newest.txt \
    --local_state=src/chrome/android/profiles/local.txt \
    --output_name=src/chrome/android/profiles/afdo.prof \
    --gs_url_base=chromeos-prebuilt/afdo-job/llvm

echo ">>>>>> Download pgo profiles"
python3 src/tools/update_pgo_profiles.py \
    --target=linux \
    update \
    --gs-url-base=chromium-optimization-profiles/pgo_profiles

# Needed to get typescript compiler
echo ">>>>>> Get node modules for third_party/node"
bash src/third_party/node/update_npm_deps
if [ $? -ne 0 ]; then
    echo "ERROR: npm ci failed"
    cleanup_and_exit 1
fi

echo ">>>>>> Get node modules for electron"
pushd src/electron || cleanup_and_exit 1
yarn install --frozen-lockfile
if [ $? -ne 0 ]; then
    echo "ERROR: yarn install failed"
    cleanup_and_exit 1
fi
popd || cleanup_and_exit 1

mv src "${ELECTRON_PKGNAME}-${ELECTRON_PKGVERSION}"

pushd "${ELECTRON_PATH}" || cleanup_and_exit 1

echo ">>>>>> Create LASTCHANGE(.committime) file"
echo -n "LASTCHANGE=$(git log -1 --format=format:%H HEAD)" > build/util/LASTCHANGE
source build/util/LASTCHANGE
echo -n "$(git log -1 --date=unix --format=format:%cd $LASTCHANGE)" > build/util/LASTCHANGE.committime

echo ">>>>>> Remove bundled libs"
keeplibs=(
    base/third_party/cityhash
    base/third_party/double_conversion
    base/third_party/dynamic_annotations
    base/third_party/icu
    base/third_party/nspr
    base/third_party/superfasthash
    base/third_party/symbolize
    base/third_party/valgrind
    base/third_party/xdg_mime
    base/third_party/xdg_user_dirs
    buildtools/third_party/libc++
    buildtools/third_party/libc++abi
    buildtools/third_party/libunwind
    buildtools/third_party/eu-strip
    chrome/third_party/mozilla_security_manager
    courgette/third_party
    net/third_party/mozilla_security_manager
    net/third_party/nss
    net/third_party/quic
    net/third_party/uri_template
    third_party/abseil-cpp
    third_party/angle
    third_party/angle/src/common/third_party/base
    third_party/angle/src/common/third_party/smhasher
    third_party/angle/src/common/third_party/xxhash
    third_party/angle/src/third_party/libXNVCtrl
    third_party/angle/src/third_party/trace_event
    third_party/angle/src/third_party/volk
    third_party/apple_apsl
    third_party/axe-core
    third_party/blink
    third_party/boringssl
    third_party/boringssl/src/third_party/fiat
    third_party/breakpad
    third_party/breakpad/breakpad/src/third_party/curl
    third_party/brotli
    third_party/catapult
    third_party/catapult/common/py_vulcanize/third_party/rcssmin
    third_party/catapult/common/py_vulcanize/third_party/rjsmin
    third_party/catapult/third_party/beautifulsoup4
    third_party/catapult/third_party/html5lib-1.1/
    third_party/catapult/third_party/html5lib-python
    third_party/catapult/third_party/polymer
    third_party/catapult/third_party/six
    third_party/catapult/tracing/third_party/d3
    third_party/catapult/tracing/third_party/gl-matrix
    third_party/catapult/tracing/third_party/jpeg-js
    third_party/catapult/tracing/third_party/jszip
    third_party/catapult/tracing/third_party/mannwhitneyu
    third_party/catapult/tracing/third_party/oboe
    third_party/catapult/tracing/third_party/pako
    third_party/ced
    third_party/cld_3
    third_party/closure_compiler
    third_party/crashpad
    third_party/crashpad/crashpad/third_party/lss
    third_party/crashpad/crashpad/third_party/zlib
    third_party/crc32c
    third_party/cros_system_api
    third_party/dav1d
    third_party/dawn
    third_party/dawn/third_party
    third_party/dawn/third_party/tint/src/ast
    third_party/depot_tools
    third_party/depot_tools/third_party/six
    third_party/devscripts
    third_party/devtools-frontend
    third_party/devtools-frontend/src/front_end/third_party/acorn
    third_party/devtools-frontend/src/front_end/third_party/axe-core
    third_party/devtools-frontend/src/front_end/third_party/chromium
    third_party/devtools-frontend/src/front_end/third_party/codemirror
    third_party/devtools-frontend/src/front_end/third_party/diff
    third_party/devtools-frontend/src/front_end/third_party/i18n
    third_party/devtools-frontend/src/front_end/third_party/intl-messageformat
    third_party/devtools-frontend/src/front_end/third_party/lighthouse
    third_party/devtools-frontend/src/front_end/third_party/lit-html
    third_party/devtools-frontend/src/front_end/third_party/lodash-isequal
    third_party/devtools-frontend/src/front_end/third_party/marked
    third_party/devtools-frontend/src/front_end/third_party/puppeteer
    third_party/devtools-frontend/src/front_end/third_party/wasmparser
    third_party/devtools-frontend/src/third_party
    third_party/devtools-frontend/src/test/unittests/front_end/third_party/i18n
    third_party/distributed_point_functions
    third_party/dom_distiller_js
    third_party/eigen3
    third_party/electron_node
    third_party/emoji-segmenter
    third_party/farmhash
    third_party/fdlibm
    third_party/ffmpeg
    third_party/fft2d
    third_party/flatbuffers
    third_party/freetype
    third_party/fusejs/dist
    third_party/gemmlowp
    third_party/google_input_tools
    third_party/google_input_tools/third_party/closure_library
    third_party/google_input_tools/third_party/closure_library/third_party/closure
    third_party/googletest
    third_party/harfbuzz-ng
    third_party/harfbuzz-ng/utils
    third_party/highway
    third_party/hunspell
    third_party/iccjpeg
    third_party/icu
    third_party/inspector_protocol
    third_party/jinja2
    third_party/jsoncpp
    third_party/jstemplate
    third_party/khronos
    third_party/leveldatabase
    third_party/libaddressinput
    third_party/libaom
    third_party/libaom/source/libaom/third_party/fastfeat
    third_party/libaom/source/libaom/third_party/vector
    third_party/libaom/source/libaom/third_party/x86inc
    third_party/libavif
    third_party/libgav1
    third_party/libgifcodec
    third_party/libjingle
    third_party/libjxl
    third_party/libphonenumber
    third_party/libsecret
    third_party/libsrtp
    third_party/libsync
    third_party/libudev
    third_party/liburlpattern
    third_party/libva_protected_content
    third_party/libvpx
    third_party/libvpx/source/libvpx/third_party/x86inc
    third_party/libwebm
    third_party/libx11/src
    third_party/libxcb-keysyms/keysyms
    third_party/libxml/chromium
    third_party/libXNVCtrl
    third_party/libyuv
    third_party/libzip
    third_party/lottie
    third_party/lss
    third_party/lzma_sdk
    third_party/mako
    third_party/maldoca
    third_party/maldoca/src/third_party
    third_party/markupsafe
    third_party/mesa
    third_party/metrics_proto
    third_party/minigbm
    third_party/modp_b64
    third_party/nasm
    third_party/nearby
    third_party/node
    third_party/node/node_modules/polymer-bundler/lib/third_party/UglifyJS2
    third_party/one_euro_filter
    third_party/opencv
    third_party/openscreen
    third_party/openscreen/src/third_party/mozilla
    third_party/openscreen/src/third_party/tinycbor/src/src
    third_party/ots
    third_party/pdfium
    third_party/pdfium/third_party/agg23
    third_party/pdfium/third_party/base
    third_party/pdfium/third_party/bigint
    third_party/pdfium/third_party/freetype
    third_party/pdfium/third_party/lcms
    third_party/pdfium/third_party/libopenjpeg20
    third_party/pdfium/third_party/libpng16
    third_party/pdfium/third_party/libtiff
    third_party/pdfium/third_party/skia_shared
    third_party/perfetto
    third_party/perfetto/protos/third_party/chromium
    third_party/pffft
    third_party/ply
    third_party/polymer
    third_party/private-join-and-compute
    third_party/private_membership
    third_party/protobuf
    third_party/protobuf/third_party/six
    third_party/pyjson5
    third_party/qcms
    third_party/rnnoise
    third_party/ruy
    third_party/s2cellid
    third_party/securemessage
    third_party/shell-encryption
    third_party/simplejson
    third_party/skia
    third_party/skia/include/third_party/skcms/
    third_party/skia/include/third_party/vulkan/
    third_party/skia/third_party/skcms
    third_party/skia/third_party/vulkan
    third_party/smhasher
    third_party/speech-dispatcher
    third_party/sqlite
    third_party/swiftshader
    third_party/swiftshader/third_party/SPIRV-Headers/include/spirv/unified1
    third_party/swiftshader/third_party/astc-encoder
    third_party/swiftshader/third_party/llvm-10.0
    third_party/swiftshader/third_party/llvm-subzero
    third_party/swiftshader/third_party/marl
    third_party/swiftshader/third_party/subzero
    third_party/tcmalloc
    third_party/tensorflow-text
    third_party/tflite
    third_party/tflite/src/third_party/eigen3
    third_party/tflite/src/third_party/fft2d
    third_party/ukey2
    third_party/usb_ids
    third_party/usrsctp
    third_party/utf
    third_party/vulkan
    third_party/wayland
    third_party/web-animations-js
    third_party/webdriver
    third_party/webgpu-cts
    third_party/webrtc
    third_party/webrtc/common_audio/third_party/ooura
    third_party/webrtc/common_audio/third_party/spl_sqrt_floor
    third_party/webrtc/modules/third_party/fft
    third_party/webrtc/modules/third_party/g711
    third_party/webrtc/modules/third_party/g722
    third_party/webrtc/rtc_base/third_party/base64
    third_party/webrtc/rtc_base/third_party/sigslot
    third_party/widevine
    third_party/woff2
    third_party/wuffs
    third_party/x11proto
    third_party/xcbproto
    third_party/zlib/google
    third_party/zxcvbn-cpp
    url/third_party/mozilla
    v8/src/third_party/siphash
    v8/src/third_party/utf8-decoder
    v8/src/third_party/valgrind
    v8/third_party/inspector_protocol
    v8/third_party/v8/builtins
)
build/linux/unbundle/remove_bundled_libraries.py "${keeplibs[@]}" --do-remove
if [ $? -ne 0 ]; then
    echo "ERROR: remove_bundled_libraries.py failed"
    cleanup_and_exit 1
fi

rm -rf third_party/blink/web_tests # 1.6GB
rm -rf third_party/catapult/tracing/test_data # 200MB
find . -type d -name .git -print0 | xargs -0 rm -rf
popd || cleanup_and_exit 1

echo ">>>>>> Create tarball"
XZ_OPT="-T$(nproc)" tar cJf $ELECTRON_PKGDIR/$ELECTRON_PKGNAME-$ELECTRON_PKGVERSION.tar.xz $ELECTRON_PKGNAME-$ELECTRON_PKGVERSION
if [ $? -ne 0 ]; then
    echo "ERROR: tar cJf failed"
    cleanup_and_exit 1
fi

popd || cleanup_and_exit 1

cleanup_and_exit 0
