#!/bin/bash
# shellcheck disable=2181
#
# Copyright (c) 2021 Andreas Schneider <asn@cryptomilk.org>
# License: GPLv3
#
# dnf install python3-base git-core npm16 yarn python2-base moreutils

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
sed -i "s/, '--progress']$/, '--progress', '--filter=tree:0']/" depot_tools/gclient_scm.py
sed -i 's/remote or self.remote,$/remote or self.remote, "--depth=1", "--filter=tree:0"/' depot_tools/gclient_scm.py

# HACK I want to see progress from git checkout to ensure it does not hang
sed -i 's/if quiet is None:$/if True:/' depot_tools/gclient_scm.py


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



echo ">>>>>> Generate GPU_LISTS_VERSION"
python3 build/util/lastchange.py -m GPU_LISTS_VERSION \
    --revision-id-only --header gpu/config/gpu_lists_version.h
if [ $? -ne 0 ]; then
    echo "ERROR: lastchange.py -m GPU_LISTS_VERSION failed"
    cleanup_and_exit 1
fi

echo ">>>>>> Generate SKIA_COMMIT_HASH"
python3 build/util/lastchange.py -m SKIA_COMMIT_HASH \
    -s third_party/skia --header skia/ext/skia_commit_hash.h
if [ $? -ne 0 ]; then
    echo "ERROR: lastchange.py -m SKIA_COMMIT_HASH failed"
    cleanup_and_exit 1
fi

popd

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


# Needed to get typescript compiler
echo ">>>>>> Download and unpack webui-node-modules tarball for third_party/node"
python3 src/third_party/depot_tools/download_from_google_storage.py \
    --no_resume --extract --no_auth --bucket chromium-nodejs \
    -s src/third_party/node/node_modules.tar.gz.sha1
if [ $? -ne 0 ]; then
    echo "ERROR: download_from_google_storage failed"
    cleanup_and_exit 1
fi
# we don't need the orig tarball
rm -v src/third_party/node/node_modules.tar.gz

echo ">>>>>> Get node modules for electron"
pushd src/electron || cleanup_and_exit 1
yarn install --frozen-lockfile --ignore-engines --ignore-scripts --link-duplicates
if [ $? -ne 0 ]; then
    echo "ERROR: yarn install failed"
    cleanup_and_exit 1
fi
popd || cleanup_and_exit 1


pushd "${ELECTRON_PATH}" || cleanup_and_exit 1


# For every entry on this list either remove it, or add an explanation why it's needed.
echo ">>>>>> Remove bundled libs"
keeplibs=(
    base/third_party/cityhash #Derived code, not vendored dependency.
    base/third_party/cityhash_v103 #Derived code, not vendored dep
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
    net/third_party/quiche #Not available as a shared library yet. An old version is in Factory (google-quiche-source)
    net/third_party/uri_template #Derived code, not vendored dependency.
    third_party/abseil-cpp #15.4 and fc36 too old.
    third_party/angle  # ANGLE is an integral part of chrome and is not available as a shared library.
    third_party/angle/src/common/third_party/base #Derived code, not vendored dependency.
    third_party/angle/src/common/third_party/smhasher ##Derived code, not vendored dependency.
    third_party/angle/src/third_party/libXNVCtrl #Not in Factory yet
    third_party/angle/src/third_party/trace_event #Does not seem to be a separate library.
    third_party/angle/src/third_party/volk #Not in Factory or Rawhide. Debian has it as vulkan-volk, CONSIDER UNBUNDLING when we have it
    third_party/blink #Integral part of chrome
    third_party/boringssl #Factory has an ancient version, but upstream seems to have gave up on making it a shared library
    third_party/boringssl/src/third_party/fiat #Not in any distro
    third_party/breakpad #Integral part of chrome
    # We don't need it (disable-catapult.patch)
    #third_party/catapult
    #third_party/catapult/common/py_vulcanize/third_party/rcssmin
    #third_party/catapult/common/py_vulcanize/third_party/rjsmin
    #third_party/catapult/third_party/beautifulsoup4
    #third_party/catapult/third_party/html5lib-1.1
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
    third_party/ced #not in any distro
    third_party/cld_3 #not in any distro. We have cld2 but not cld3
    third_party/closure_compiler #the python scripts are not available separately
    third_party/crashpad #Integral part of chrome
    third_party/crashpad/crashpad/third_party/lss #Derived code, not vendored dependency.
    third_party/crashpad/crashpad/third_party/zlib #Derived code, not vendored dependency.
    third_party/crc32c #Not in Leap
    third_party/cros_system_api #Integral part of Chrome. Needed.
    third_party/dav1d #Leap and fc36 too old
    third_party/dawn #Integral part of chrome, Needed even if you're building chrome without webgpu
    third_party/dawn/third_party/gn/webgpu-cts #Integral part of chrome, Needed even if you're building chrome without webgpu
    third_party/devtools-frontend #Javascript code, integral part of chrome
    third_party/devtools-frontend/src/front_end/third_party #various javascript code compiled into chrome, see README.md
    third_party/devtools-frontend/src/test/unittests/front_end/third_party/i18n # javascript
    third_party/devtools-frontend/src/third_party/typescript #Chromium added code
    third_party/distributed_point_functions #not in any distro
    third_party/dom_distiller_js #javascript
    #third_party/eigen3 #Used only by tflite which is not used in electron
    third_party/electron_node #Integral part of electron
    third_party/emoji-segmenter #not available as a shared library
    third_party/fdlibm #derived code, not vendored dep
    third_party/harfbuzz-ng #There are new google files within this directory.
    third_party/harfbuzz-ng/utils
    third_party/highway #Not in Leap
    third_party/hunspell #heavily forked version
    third_party/iccjpeg #not in any distro
    third_party/inspector_protocol #integral part of chrome
    third_party/ipcz #not in any distro
    third_party/jinja2 #Patch for deterministic builds. CONSIDER UNBUNDLING this when chrome switches to jinja 3.x
    third_party/jstemplate #javascript
    third_party/khronos #Modified to add ANGLE definitions
    third_party/leveldatabase #use of private headers
    third_party/libaddressinput #seems not to be available as a separate library
    third_party/libaom #version in Factory is too old
    third_party/libaom/source/libaom/third_party/fastfeat
    third_party/libaom/source/libaom/third_party/vector
    third_party/libaom/source/libaom/third_party/x86inc
    third_party/libavif #not availabe on 15.3
    third_party/libgav1 #not in Factory yet, but available in unofficial repos. CONSIDER UNBUNDLING when any distro has it.
    third_party/libjxl #not in Leap
    third_party/libphonenumber #Depends on protobuf which cannot be unbundled
    third_party/libsrtp #Use of private headers. they were public in libsrtp1
    third_party/libsync #not yet in any distro
    third_party/libudev #Headers for a optional delay-loaded dependency
    third_party/liburlpattern #Derived code, not vendored dep.
    third_party/libva_protected_content #ChromeOS header not available separately. needed for build.
    third_party/libvpx #Use of private headers in VAAPI code only.
    third_party/libvpx/source/libvpx/third_party/x86inc
    third_party/libwebm #Usage of private headers (mkvparser/mkvmuxer)
    third_party/libx11 #Derived code, not vendored dep
    third_party/libxcb-keysyms #Derived code, not vendored dep
    third_party/libxml/chromium #added chromium code
    third_party/libyuv #The version in Fedora is too old
    third_party/lottie #javascript
    third_party/lss #Wrapper for linux ABI
    #third_party/maldoca #integral part of chrome, but not used in electron.
    #third_party/maldoca/src/third_party
    third_party/markupsafe #ImportError: cannot import name 'soft_unicode' from 'markupsafe' (/usr/lib64/python3.10/site-packages/markupsafe/__init__.py). CONSIDER UNBUNDLING when jinja is fixed
    third_party/mesa_headers #ui/gl/gl_bindings.cc depends on GL_KHR_robustness not being defined.
    third_party/metrics_proto #integral part of chrome
    third_party/modp_b64 #not in any distro
    third_party/node #javascript code
    third_party/node/node_modules/polymer-bundler/lib/third_party/UglifyJS2/
    third_party/one_euro_filter #not in any distro
    third_party/openscreen #Integral part of chrome, needed even if you're building without.
    third_party/openscreen/src/third_party/mozilla #derived code, not vendored dependency
    third_party/openscreen/src/third_party/tinycbor/src/src #not in any distro
    third_party/ots #not available as a shared library. Fedora has the cli version as opentype-sanitizer
    third_party/pdfium #Integral part of chrome
    third_party/pdfium/third_party/agg23 #Heavily patched version. Fedora has it as agg
    third_party/pdfium/third_party/base #derived code, not vendored dependency
    third_party/pdfium/third_party/bigint #not on any distro
    third_party/pdfium/third_party/freetype #Copy of private headers
    third_party/pdfium/third_party/skia_shared #Skia is not available as a shared library yet.
    third_party/perfetto #Seems not to be available as a shared library, despite the presence of a `debian` directory.
    third_party/perfetto/protos/third_party/chromium #derived code, not vendored dep
    third_party/pffft #not in any distro, also heavily patched
    third_party/polymer #javascript
    third_party/private-join-and-compute #not in any distro, also heavily patched
    third_party/private_membership #derived code, not vendored dep
    third_party/protobuf #Heavily forked. Apparently was officially unbundlable back in the GYP days, and may be again in the future.
    third_party/rnnoise #use of private headers
    third_party/shell-encryption #not available on any distro, also heavily patched
    third_party/skia #integral part of chrome
    third_party/skia/include/third_party/skcms #part of skia, not available as a separate library
    third_party/skia/third_party/skcms #part of skia, not available as a separate library
    third_party/smhasher #not in Rawhide or Factory. AltLinux has it (libsmhasher) CONSIDER UNBUNDLING if we have it
    third_party/speech-dispatcher #Headers for a delay-loaded optional dependency
    third_party/sqlite #heavily forked version
    third_party/swiftshader #not available as a shared library
    third_party/swiftshader/third_party/astc-encoder #not in rawhide or factory. Debian has it (astc-encoder)
    third_party/swiftshader/third_party/llvm-subzero #heavily forked version of libLLVM for use in subzero
    third_party/swiftshader/third_party/marl #not on any distro
    third_party/swiftshader/third_party/SPIRV-Headers #FC36 too old
    third_party/swiftshader/third_party/SPIRV-Tools #FC36 too old
    third_party/swiftshader/third_party/subzero #integral part of swiftshader
    #third_party/tflite #Not used by electron, but chrome needs it.
    #third_party/tflite/src/third_party/eigen3
    #third_party/tflite/src/third_party/fft2d
    third_party/vulkan-deps/spirv-headers #FC36 too old
    third_party/vulkan-deps/spirv-tools #FC36 too old
    third_party/vulkan-deps/vulkan-headers #FC36 too old. CONSIDER UNBUNDLING when all distros have new enough vulkan sdk
    third_party/vulkan-deps/vulkan-tools #The mock ICD seems to be used during build, but is not shipped (see https://github.com/electron/electron/pull/18596)
    third_party/vulkan_memory_allocator #not in any distro
    third_party/webgpu-cts #Javascript code. Needed even if you're building chrome without webgpu
    third_party/webrtc #Integral part of chrome
    third_party/webrtc/common_audio/third_party/ooura #derived code, not vendored dep
    third_party/webrtc/common_audio/third_party/spl_sqrt_floor #derived code, not vendored dep
    third_party/webrtc/modules/third_party/fft #derived code, not vendored dep
    third_party/webrtc/modules/third_party/g711 #derived code, not vendored dep
    third_party/webrtc/modules/third_party/g722 #derived code, not vendored dep
    third_party/webrtc/rtc_base/third_party/base64 #derived code, not vendored dep
    third_party/webrtc/rtc_base/third_party/sigslot #derived code, not vendored dep
    third_party/webrtc_overrides #Integral part of chrome
    third_party/widevine #Integral part of chrome. Needed.
    third_party/wayland/protocol #added chromium code
    third_party/wayland/stubs #added chromium code
    third_party/wayland/wayland_scanner_wrapper.py #wrapper script
    third_party/wayland-protocols/gtk/gdk/wayland/protocol #Imagine downloading 100MB of gtk source just to get one file.
    third_party/wayland-protocols/mesa #egl-wayland-devel (Fedora) / libnvidia-egl-wayland1 (SUSE). Not in 15.3 CONSIDER UNBUNDLING when all distros have this
    third_party/wayland-protocols/src #pkgconfig(wayland-protocols) — 15.3 too old CONSIDER UNBUNDLING once we drop it
    third_party/wayland-protocols/unstable #unknown origin. not in wayland-protocol-devel or elsewhere
    third_party/wuffs #not in any distro
    third_party/x11proto #derived code, not vendored dep
    third_party/zlib/google #derived code, not vendored dep
    third_party/zxcvbn-cpp #not in any distro, also heavily patched
    url/third_party/mozilla #derived code, not vendored dep
    v8/src/third_party/siphash #derived code, not vendored dep
    v8/src/third_party/utf8-decoder #derived code, not vendored dep
    v8/src/third_party/valgrind #incompatible definition of VALGRIND_DISCARD_TRANSLATIONS
    v8/third_party/inspector_protocol #integral part of chrome
    v8/third_party/v8 #derived code, not vendored dep
)
build/linux/unbundle/remove_bundled_libraries.py "${keeplibs[@]}" --do-remove
if [ $? -ne 0 ]; then
    echo "ERROR: remove_bundled_libraries.py failed"
    cleanup_and_exit 1
fi
# Now remove additional bundled/duplicate libraries in node/deps
rm -rf third_party/electron_node/deps/{googletest/{include,src},icu-small} #292MB and vendored
find third_party/electron_node/deps/brotli -type f ! -name "*.gn" -a ! -name "*.gni" -a ! -name "*.gyp" -a ! -name "*.gypi" -delete
find third_party/electron_node/deps/cares -type f ! -name "*.gn" -a ! -name "*.gni" -a ! -name "*.gyp" -a ! -name "*.gypi" -delete
find third_party/electron_node/deps/nghttp2 -type f ! -name "*.gn" -a ! -name "*.gni" -a ! -name "*.gyp" -a ! -name "*.gypi" -delete
find third_party/electron_node/deps/openssl -type f ! -name "*.gn" -a ! -name "*.gni" -a ! -name "*.gyp" -a ! -name "*.gypi" -delete
find third_party/electron_node/deps/v8 -type f ! -name "*.gn" -a ! -name "*.gni" -a ! -name "*.gyp" -a ! -name "*.gypi" -delete
find third_party/electron_node/deps/zlib -type f ! -name "*.gn" -a ! -name "*.gni" -a ! -name "*.gyp" -a ! -name "*.gypi" -delete


#Some more chonkers
rm -rf components/test/data #21MB
rm -rf docs #30MB
rm -rf media/test/data #62MB
rm -rf native_client_sdk/doc_generated #21MB
rm -rf third_party/blink/{manual,perf}_tests #70MB
rm -rf third_party/electron_node/{doc,test} #42MB
rm -rf third_party/libaom/fuzz #44MB
rm -rf third_party/perfetto/docs #11MB
rm -rf third_party/protobuf/{csharp,java,js,objectivec,php,ruby} #22MB
rm -rf third_party/skia/{bench,docs,gm,platform_tools,resources,site,test,tools} #67MB
rm -rf third_party/sqlite/fuzz #61MB
rm -rf third_party/swiftshader/tests/regres #381MB
rm -rf third_party/webrtc/data #27MB
rm -rf tools/disable_tests #6MB
rm -rf tools/perf/{page_sets,testdata} #55MB
rm -rf third_party/blink/web_tests # 1.6GB
rm -rf third_party/catapult/tracing/test_data # 200MB
rm -rf third_party/sqlite/src/test #86MB
find chrome/test/data -type f ! -name "*.gn" -a ! -name "*.gni" -delete #249MB, thanks Mageia

#see electron/.circleci/config/base.yml
rm -rf android_webview
rm -rf ios/chrome

find . -type d -name .git -print0 | xargs -0 rm -rf
# Remove generatted python bytecode
find . -type d -name __pycache__ -print0 | xargs -0 rm -rvf
find . -type f -name '*.pyc' -print -delete

echo ">>>>>> Remove non-free binaries"
find . -type f -name "*.jar" -print -delete
find . -type f -name "*.exe" -print -delete
find . -type f -name "*.node" -print -delete
find . -type f -name "*.dll" -print -delete
find . -type f -name "*.dylib" -print -delete
find . -type f -name "*.so" -print -delete
find . -type f -name "*.o" -print -delete
find . -type f -name "*.a" -print -delete

#We use sponge to avoid a race condition between find and rm
find -type f | sponge | xargs -P$(nproc) -- sh -c 'file "$@" | grep -v '\'' .*script'\'' | grep '\'' .*executable'\'' | tee /dev/stderr | sed '\''s/: .*//'\'' | xargs rm -fv'


# Remove empty directories
echo ">>>>>> Remove empty directories"
find . -type d -empty -print -delete
popd || cleanup_and_exit 1

echo ">>>>>> Hardlink duplicate files to reduce extraction time"

fdupes -Sr src

echo ">>>>>> Create tarball"
#I would like to use zst, as it decompresses MUCH faster, but unfortunately it is not supported by OBS diff view yet
XZ_OPT="-T$(nproc) -e9 -vv" tar -vvcJf "${ELECTRON_PKGDIR}/${ELECTRON_PKGNAME}-${ELECTRON_PKGVERSION}.tar.xz" src
if [ $? -ne 0 ]; then
    echo "ERROR: tar cf failed"
    cleanup_and_exit 1
fi

popd || cleanup_and_exit 1

cleanup_and_exit 0
