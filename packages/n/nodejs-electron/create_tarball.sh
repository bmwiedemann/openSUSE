#!/bin/bash
# shellcheck disable=2181
#
# Copyright (c) 2021 Andreas Schneider <asn@cryptomilk.org>
# License: GPLv3
#
# dnf install python3-base git-core npm16 yarn python2-base

ELECTRON_PKGVERSION="$(rpmspec -P ./*.spec | grep ^\s*Version | sed -e 's/Version:[ ]*//g')"
ELECTRON_PKGNAME="electron"
ELECTRON_PKGDIR="$(pwd)"
ELECTRON_TMPDIR="$(mktemp --tmpdir -d electron-XXXXXXXX)"
ELECTRON_PATH="${ELECTRON_TMPDIR}/src"

echo "NAME:    $ELECTRON_PKGNAME"
echo "VERSION: $ELECTRON_PKGVERSION"
echo "PATH:    $ELECTRON_PATH"

echo -n "This script will download about 60G to $ELECTRON_TMPDIR, continue? "
read $ans

cleanup_tmpdir() {
    popd 2>/dev/null || true
    rm -rf "$ELECTRON_TMPDIR"
}
trap cleanup_tmpdir SIGINT

cleanup_and_exit() {
    cleanup_tmpdir
    if test "$1" = 0 -o -z "$1" ; then
        exit 0
    else
        exit "$1"
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

# HACK to make gclient much faster, do not download entire history
sed -i 's/remote or self.remote,$/remote or self.remote, "--depth=1"/' depot_tools/gclient_scm.py


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
gclient sync -v --jobs $(nproc) --nohooks --no-history --shallow --revision=v"${ELECTRON_PKGVERSION}"
if [ $? -ne 0 ]; then
    echo "ERROR: gclient sync failed"
    cleanup_and_exit 1
fi

pushd src || cleanup_and_exit 1

echo ">>>>>> Create LASTCHANGE(.committime) file"
echo -n "LASTCHANGE=$(git log -1 --format=format:%H HEAD)" > build/util/LASTCHANGE
# shellcheck disable=1091
source build/util/LASTCHANGE
echo -n "$(git log -1 --date=unix --format=format:%cd "$LASTCHANGE")" > build/util/LASTCHANGE.committime

popd

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

echo ">>>>>> Apply electron-${ELECTRON_PKGVERSION} patches"
python3 src/electron/script/apply_all_patches.py \
      src/electron/patches/config.json
if [ $? -ne 0 ]; then
    echo "ERROR: apply_all_patches.py failed"
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


#The following commands overwrite this file which is needed during build.
#The precise content is unimportant, but we cache the original one for reproducibility.
mv -v src/third_party/node/node_modules.tar.gz.sha1{,.bak}
# Needed to get typescript compiler
echo ">>>>>> Get node modules for third_party/node"
bash src/third_party/node/update_npm_deps
if [ $? -ne 0 ]; then
    echo "ERROR: npm ci failed"
    cleanup_and_exit 1
fi
mv -v src/third_party/node/node_modules.tar.gz.sha1{.bak,}
# Remove unnecessary repack of node_modules
rm -v src/third_party/node/node_modules.tar.gz

echo ">>>>>> Get node modules for electron"
pushd src/electron || cleanup_and_exit 1
yarn install --frozen-lockfile
if [ $? -ne 0 ]; then
    echo "ERROR: yarn install failed"
    cleanup_and_exit 1
fi
popd || cleanup_and_exit 1


pushd "${ELECTRON_PATH}" || cleanup_and_exit 1


# TODO: Go through every entry on this list and either remove it, or add an explanation why it's needed.
echo ">>>>>> Remove bundled libs"
keeplibs=(
    base/third_party/cityhash #Derived code, not vendored dependency.
    base/third_party/dynamic_annotations #Derived code, not vendored dependency.
    base/third_party/icu #Derived code, not vendored dependency.
    base/third_party/superfasthash #Not a shared library.
    base/third_party/symbolize #Derived code, not vendored dependency.
    base/third_party/valgrind #Copy of a private header.
    base/third_party/xdg_mime #Seems not to be available as a shared library.
    base/third_party/xdg_user_dirs #Derived code, not vendored dependency.
    chrome/third_party/mozilla_security_manager #Derived code, not vendored dependency.
    courgette/third_party #Derived code, not vendored dependency.
    net/third_party/mozilla_security_manager #Derived code, not vendored dependency.
    net/third_party/nss #Derived code, not vendored dependency.
    net/third_party/quic #Not available as a shared library yet. An old version is in Factory (google-quiche-source)
    net/third_party/uri_template #Derived code, not vendored dependency.
    third_party/abseil-cpp #15.4 and fc36 too old.
    # ANGLE is an integral part of chrome and is not available as a shared library.
    third_party/angle
    third_party/angle/src/common/third_party/base
    third_party/angle/src/common/third_party/smhasher
    #
    third_party/angle/src/third_party/libXNVCtrl #Not in Factory yet
    third_party/angle/src/third_party/trace_event #Does not seem to be a separate library.
    third_party/angle/src/third_party/volk #Not in Factory or Rawhide. Debian has it as vulkan-volk
    third_party/axe-core
    third_party/blink #Integral part of chrome
    third_party/boringssl #Factory has an ancient version, but upstream seems to have gave up on making it a shared library
    third_party/boringssl/src/third_party/fiat
    third_party/breakpad #Integral part of chrome
    # We don't need it (disable-catapult.patch)
    #third_party/catapult
    #third_party/catapult/common/py_vulcanize/third_party/rcssmin
    #third_party/catapult/common/py_vulcanize/third_party/rjsmin
    #third_party/catapult/third_party/beautifulsoup4
    #third_party/catapult/third_party/html5lib-1.1/
    #third_party/catapult/third_party/html5lib-python
    #third_party/catapult/third_party/polymer
    #third_party/catapult/third_party/six
    #third_party/catapult/tracing/third_party/d3
    #third_party/catapult/tracing/third_party/gl-matrix
    #third_party/catapult/tracing/third_party/jpeg-js
    #third_party/catapult/tracing/third_party/jszip
    #third_party/catapult/tracing/third_party/mannwhitneyu
    #third_party/catapult/tracing/third_party/oboe
    #third_party/catapult/tracing/third_party/pako
    third_party/ced
    third_party/cld_3
    third_party/closure_compiler
    third_party/crashpad #Integral part of chrome
    third_party/crashpad/crashpad/third_party/lss #Derived code, not vendored dependency.
    third_party/crashpad/crashpad/third_party/zlib #Derived code, not vendored dependency.
    third_party/crc32c #Not in Leap
    third_party/cros_system_api #Integral part of Chrome. Needed.
    third_party/dav1d #Leap and fc36 too old
    third_party/dawn #Integral part of chrome
    third_party/dawn/third_party
    third_party/depot_tools #Integral part of chrome
    third_party/depot_tools/third_party/six
    third_party/devscripts
    #Javascript code, integral part of chrome
    third_party/devtools-frontend
    third_party/devtools-frontend/src/front_end/third_party
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
    #
    third_party/distributed_point_functions
    third_party/dom_distiller_js
    #third_party/eigen3 #Used only by tflite which is not used in electron
    third_party/electron_node #Integral part of electron
    third_party/emoji-segmenter
    third_party/farmhash
    third_party/fdlibm
    third_party/fft2d
    third_party/flatbuffers #TODO: Consider unbundling this
    third_party/fusejs/dist
    third_party/gemmlowp
    third_party/harfbuzz-ng #There are new google files within this directory.
    third_party/harfbuzz-ng/utils
    third_party/highway #Used only by libjxl. Consider unbundling this.
    third_party/hunspell #heavily forked version
    third_party/iccjpeg
    third_party/inspector_protocol
    third_party/jinja2
    third_party/jstemplate
    third_party/khronos
    third_party/leveldatabase #use of private headers
    third_party/libaddressinput
    third_party/libaom #version in Factory is too old
    third_party/libaom/source/libaom/third_party/fastfeat
    third_party/libaom/source/libaom/third_party/vector
    third_party/libaom/source/libaom/third_party/x86inc
    third_party/libavif #not availabe on 15.3
    third_party/libgav1 #not in Factory yet
    third_party/libgifcodec
    third_party/libjxl #not in Factory yet
    third_party/libphonenumber #depends on protobuf
    third_party/libsecret #TODO: Consider unbundling this
    third_party/libsrtp #Use of private headers
    third_party/libsync/src
    third_party/libudev
    third_party/liburlpattern
    third_party/libva_protected_content
    third_party/libvpx #Use of private headers
    third_party/libvpx/source/libvpx/third_party/x86inc
    third_party/libwebm
    third_party/libx11/src
    third_party/libxcb-keysyms/keysyms
    third_party/libxml/chromium
    third_party/libyuv #The version in Fedora is too old
    third_party/libzip
    third_party/lottie
    third_party/lss
    third_party/mako
    #third_party/maldoca #integral part of chrome, but not used in electron.
    #third_party/maldoca/src/third_party
    third_party/markupsafe
    third_party/mesa
    third_party/metrics_proto
    third_party/modp_b64
    third_party/nasm #TODO: Check how forked is this and if we can use the system version
    third_party/node #javascript code
    third_party/node/node_modules/polymer-bundler/lib/third_party/UglifyJS2
    third_party/one_euro_filter
    third_party/openscreen
    third_party/openscreen/src/third_party/mozilla
    third_party/openscreen/src/third_party/tinycbor/src/src
    third_party/ots
    third_party/pdfium
    third_party/pdfium/third_party/agg23
    third_party/pdfium/third_party/base
    third_party/pdfium/third_party/bigint
    third_party/pdfium/third_party/freetype
    third_party/pdfium/third_party/skia_shared
    third_party/perfetto
    third_party/perfetto/protos/third_party/chromium
    third_party/pffft
    third_party/ply
    third_party/polymer
    third_party/private-join-and-compute
    third_party/private_membership
    third_party/protobuf #Heavily forked.
    third_party/protobuf/third_party/six
    third_party/pyjson5
    third_party/qcms
    third_party/rnnoise #use of private headers
    third_party/ruy
    third_party/s2cellid
    third_party/securemessage
    third_party/shell-encryption
    third_party/simplejson
    third_party/skia #integral part of chrome
    third_party/skia/include/third_party/skcms/
    third_party/skia/include/third_party/vulkan/
    third_party/skia/third_party/skcms
    third_party/skia/third_party/vulkan
    third_party/smhasher
    third_party/speech-dispatcher #stub header for a dlopened library
    third_party/sqlite #heavily forked version
    third_party/swiftshader
    third_party/swiftshader/third_party/SPIRV-Headers/include/spirv/unified1 #FC36 too old
    third_party/swiftshader/third_party/SPIRV-Tools #FC36 too old
    third_party/swiftshader/third_party/astc-encoder
    third_party/swiftshader/third_party/llvm-subzero
    third_party/swiftshader/third_party/marl
    third_party/swiftshader/third_party/subzero
    #third_party/tflite #Not used by electron, but chrome needs it.
    #third_party/tflite/src/third_party/eigen3
    #third_party/tflite/src/third_party/fft2d
    third_party/ukey2
    third_party/usb_ids #TODO: Consider unbundling this, the version in chrome is ancient
    third_party/utf
    third_party/vulkan
    third_party/wayland
    third_party/web-animations-js
    third_party/webdriver
    third_party/webgpu-cts
    third_party/webrtc #Integral part of chrome
    third_party/webrtc/common_audio/third_party/ooura
    third_party/webrtc/common_audio/third_party/spl_sqrt_floor
    third_party/webrtc/modules/third_party/fft
    third_party/webrtc/modules/third_party/g711
    third_party/webrtc/modules/third_party/g722
    third_party/webrtc/rtc_base/third_party/base64
    third_party/webrtc/rtc_base/third_party/sigslot
    third_party/widevine #Integral part of chrome. Needed.
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
# Remove generatted python bytecode
find . -type d -name __pycache__ -print0 | xargs -0 rm -rvf
find . -type f -name '*.pyc' -print -delete

echo ">>>>>> Remove non-free binaries"
find . -type f -name "*.node" -print -delete
find . -type f -name "*.dll" -print -delete
find . -type f -name "*.dylib" -print -delete
find . -type f -name "*.so" -print -delete
find . -type f -name "*.o" -print -delete
find . -type f -name "*.a" -print -delete

find -type f | xargs -P$(nproc) -- sh -c 'file "$@" | grep -v '\'' .*script'\'' | grep '\'' .*executable'\'' | tee /dev/stderr | sed '\''s/: .*//'\'' | xargs rm -fv'


# Remove empty directories
find . -type d -empty -print -delete
popd || cleanup_and_exit 1

echo ">>>>>> Create tarball"
XZ_OPT="-T$(nproc) -e9 -vv" tar -vvcJf "${ELECTRON_PKGDIR}/${ELECTRON_PKGNAME}-${ELECTRON_PKGVERSION}.tar.xz" src
if [ $? -ne 0 ]; then
    echo "ERROR: tar cJf failed"
    cleanup_and_exit 1
fi

popd || cleanup_and_exit 1

cleanup_and_exit 0
