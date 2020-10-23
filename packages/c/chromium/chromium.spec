#
# spec file for package chromium
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


%define rname chromium
# bsc#1108175
%define __provides_exclude ^lib.*\\.so.*$
%if 0%{?suse_version} > 1500
%bcond_without system_icu
%bcond_with system_vpx
%bcond_with wayland
%else
%bcond_with system_icu
%bcond_with system_vpx
%bcond_with wayland
%endif
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
%bcond_without system_harfbuzz
%bcond_without pipewire
%else
%bcond_with system_harfbuzz
%bcond_with pipewire
%endif
%ifarch %{arm} aarch64
%bcond_with swiftshader
%else
%bcond_without swiftshader
%endif
%ifarch x86_64
%if %{?suse_version} > 1500
%bcond_without lto
%else
%bcond_with lto
%endif
%else
%bcond_with lto
%endif
%bcond_with clang
Name:           chromium
Version:        86.0.4240.111
Release:        0
Summary:        Google's open source browser project
License:        BSD-3-Clause AND LGPL-2.1-or-later
URL:            https://www.chromium.org/
Source0:        https://commondatastorage.googleapis.com/chromium-browser-official/%{rname}-%{version}.tar.xz
# Toolchain definitions
Source30:       master_preferences
Source100:      chromium-browser.sh
Source101:      chromium-browser.desktop
Source102:      chromium-browser.xml
Source103:      chromium.default
Source104:      chromium-symbolic.svg
Patch0:         chromium-libusb_interrupt_event_handler.patch
# PATCH-FIX-OPENSUSE Make the 1-click-install ymp file always download [bnc#836059]
Patch1:         exclude_ymp.patch
# PATCH-FIX-OPENSUSE enables reading of the master preference
Patch2:         chromium-master-prefs-path.patch
# PATCH-FIX-OPENSUSE fix_building_widevinecdm_with_chromium.patch - Enable WideVine plugin
Patch3:         fix_building_widevinecdm_with_chromium.patch
Patch4:         chromium-buildname.patch
Patch5:         chromium-system-libusb.patch
Patch6:         gcc-enable-lto.patch
Patch7:         chromium-fix-char_traits.patch
Patch8:         gpu-timeout.patch
Patch9:         build-with-pipewire-0.3.patch
# Do not use unrar code, it is non-free
Patch10:        chromium-norar.patch
# revert location on old GCC on 15.1, 15.2 gets it right tho
Patch11:        no-location-leap151.patch
Patch12:        system-libdrm.patch
Patch13:        chromium-disable-parallel-gold.patch
Patch14:        chromium-lp151-old-drm.patch
Patch15:        fix-invalid-end-iterator-usage-in-CookieMonster.patch
# gentoo patchset
Patch50:        chromium-78-protobuf-RepeatedPtrField-export.patch
Patch51:        chromium-79-gcc-protobuf-alignas.patch
Patch52:        chromium-80-QuicStreamSendBuffer-deleted-move-constructor.patch
Patch53:        chromium-84-blink-disable-clang-format.patch
Patch54:        chromium-86-compiler.patch
Patch55:        chromium-86-ConsumeDurationNumber-constexpr.patch
Patch56:        chromium-86-ImageMemoryBarrierData-init.patch
Patch57:        chromium-86-nearby-explicit.patch
Patch58:        chromium-86-nearby-include.patch
Patch59:        chromium-86-ServiceWorkerRunningInfo-noexcept.patch
Patch60:        chromium-86-f_seal.patch
# Google seem not too keen on merging this but GPU accel is quite important
#  https://chromium-review.googlesource.com/c/chromium/src/+/532294
#  https://github.com/saiarcot895/chromium-ubuntu-build/tree/master/debian/patches
#  Recreated from scratch to be smaller and use system the orginal switches
#  (default on) compared to the PR
Patch100:       chromium-vaapi.patch
Patch101:       old-libva.patch
# PATCH-FIX-SUSE: allow prop codecs to be set with chromium branding
Patch200:       chromium-prop-codecs.patch
BuildRequires:  SDL-devel
BuildRequires:  binutils-gold
BuildRequires:  bison
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gn >= 0.1807
BuildRequires:  gperf
BuildRequires:  hicolor-icon-theme
# Java used during build
BuildRequires:  java-openjdk-headless
BuildRequires:  libcap-devel
BuildRequires:  libdc1394
BuildRequires:  libgcrypt-devel
BuildRequires:  libgsm-devel
BuildRequires:  libjpeg-devel >= 8.1
BuildRequires:  libpng-devel
BuildRequires:  memory-constraints
BuildRequires:  nasm
BuildRequires:  ncurses-devel
BuildRequires:  ninja >= 1.7.2
BuildRequires:  nodejs >= 8.0
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  python-xml
BuildRequires:  python2-setuptools
BuildRequires:  snappy-devel
BuildRequires:  update-desktop-files
BuildRequires:  util-linux
BuildRequires:  wdiff
BuildRequires:  perl(Switch)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo) >= 1.6
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dirac) >= 1.0.0
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(kadm-client)
BuildRequires:  pkgconfig(kdb)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat) >= 58
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libdc1394-2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libwebp) >= 0.4.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.5
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(nspr) >= 4.9.5
BuildRequires:  pkgconfig(nss) >= 3.26
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus) >= 1.3.1
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(schroedinger-1.0)
BuildRequires:  pkgconfig(slang)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(theora) >= 1.1
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
Requires:       hicolor-icon-theme
Requires:       xdg-utils
Requires(pre):  permissions
Recommends:     noto-coloremoji-fonts
Conflicts:      chromium-browser
Provides:       chromium-based-browser = %{version}
Provides:       chromium-browser = %{version}
Provides:       web_browser
Obsoletes:      %{name}-suid-helper < %{version}
Obsoletes:      chromium-browser < %{version}
Provides:       %{name}-suid-helper = %{version}
Obsoletes:      chromium-beta-desktop-gnome
Obsoletes:      chromium-beta-desktop-kde
Obsoletes:      chromium-desktop-gnome
Obsoletes:      chromium-desktop-kde
Obsoletes:      chromium-dev-desktop-gnome
Obsoletes:      chromium-dev-desktop-kde
Obsoletes:      chromium-ffmpeg
Obsoletes:      chromium-ffmpegsumo
# no 32bit supported and it takes ages to build
ExcludeArch:    %{ix86} %{arm} ppc ppc64 ppc64le s390 s390x
%if %{with pipewire}
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libspa-0.2)
%endif
%if %{with wayland}
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)
%endif
%ifnarch aarch64
# Current tcmalloc does not support AArch64
BuildRequires:  pkgconfig(libtcmalloc)
%endif
%if %{with system_harfbuzz}
BuildRequires:  pkgconfig(harfbuzz) > 2.3.0
%endif
%if %{with system_icu}
BuildRequires:  pkgconfig(icu-i18n) >= 67.0
%endif
%if %{with system_vpx}
BuildRequires:  pkgconfig(vpx) >= 1.8.2
%endif
%if %{with clang}
BuildRequires:  clang >= 5.0.0
%else
%if %{?suse_version} > 1500
BuildRequires:  gcc >= 10
BuildRequires:  gcc-c++ >= 10
%else
BuildRequires:  gcc10
BuildRequires:  gcc10-c++
%endif
%endif

%description
Chromium is the open-source project behind Google Chrome. We invite you to join us in our effort to help build a safer, faster, and more stable way for all Internet users to experience the web, and to create a powerful platform for developing a new generation of web applications.

%package -n chromedriver
Summary:        WebDriver for Google Chrome/Chromium
License:        BSD-3-Clause
Requires:       %{name} = %{version}

%description -n chromedriver
WebDriver is an open source tool for automated testing of webapps across many browsers. It provides capabilities for navigating to web pages, user input, JavaScript execution, and more. ChromeDriver is a standalone server which implements WebDriver's wire protocol for Chromium. It is being developed by members of the Chromium and WebDriver teams.

%prep
%setup -q -n %{rname}-%{version}
%autopatch -p1

# Fix the path to nodejs binary
mkdir -p third_party/node/linux/node-linux-x64/bin
ln -s %{_bindir}/node third_party/node/linux/node-linux-x64/bin/node

# Remove bundled libs
keeplibs=(
    base/third_party/cityhash
    base/third_party/double_conversion
    base/third_party/dynamic_annotations
    base/third_party/nspr
    base/third_party/icu
    base/third_party/superfasthash
    base/third_party/symbolize
    base/third_party/valgrind
    base/third_party/xdg_mime
    base/third_party/xdg_user_dirs
    buildtools/third_party/libc++
    buildtools/third_party/libc++abi
    buildtools/third_party/libunwind
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
    third_party/angle/src/third_party/compiler
    third_party/angle/src/third_party/libXNVCtrl
    third_party/angle/src/third_party/trace_event
    third_party/angle/src/third_party/volk
    third_party/angle/third_party/glslang
    third_party/angle/third_party/spirv-headers
    third_party/angle/third_party/spirv-tools
    third_party/angle/third_party/vulkan-headers
    third_party/angle/third_party/vulkan-loader
    third_party/angle/third_party/vulkan-tools
    third_party/angle/third_party/vulkan-validation-layers
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
    third_party/crashpad
    third_party/closure_compiler
    third_party/crashpad/crashpad/third_party/lss
    third_party/crashpad/crashpad/third_party/zlib
    third_party/crc32c
    third_party/cros_system_api
    third_party/dav1d
    third_party/dawn
    third_party/depot_tools
    third_party/depot_tools/third_party/six
    third_party/devscripts
    third_party/devtools-frontend
    third_party/devtools-frontend/src/front_end/third_party/acorn
    third_party/devtools-frontend/src/front_end/third_party/chromium
    third_party/devtools-frontend/src/front_end/third_party/codemirror
    third_party/devtools-frontend/src/front_end/third_party/fabricjs
    third_party/devtools-frontend/src/front_end/third_party/i18n
    third_party/devtools-frontend/src/front_end/third_party/intl-messageformat
    third_party/devtools-frontend/src/front_end/third_party/lighthouse
    third_party/devtools-frontend/src/front_end/third_party/lit-html
    third_party/devtools-frontend/src/front_end/third_party/lodash-isequal
    third_party/devtools-frontend/src/front_end/third_party/marked
    third_party/devtools-frontend/src/front_end/third_party/wasmparser
    third_party/devtools-frontend/src/third_party
    third_party/dom_distiller_js
    third_party/emoji-segmenter
    third_party/flatbuffers
    third_party/libgifcodec
    third_party/glslang
    third_party/google_input_tools
    third_party/google_input_tools/third_party/closure_library
    third_party/google_input_tools/third_party/closure_library/third_party/closure
    third_party/googletest
    third_party/harfbuzz-ng/utils
    third_party/hunspell
    third_party/iccjpeg
    third_party/inspector_protocol
    third_party/jinja2
    third_party/jsoncpp
    third_party/jstemplate
    third_party/khronos
    third_party/leveldatabase
    third_party/libXNVCtrl
    third_party/libaddressinput
    third_party/libaom
    third_party/libaom/source/libaom/third_party/vector
    third_party/libaom/source/libaom/third_party/x86inc
    third_party/libavif
    third_party/libjingle
    third_party/libphonenumber
    third_party/libsecret
    third_party/libsrtp
    third_party/libsync
    third_party/libudev
    third_party/libwebm
    third_party/libxml/chromium
    third_party/libyuv
    third_party/lottie
    third_party/lss
    third_party/lzma_sdk
    third_party/mako
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
    third_party/pdfium/third_party/eu-strip
    third_party/pdfium/third_party/freetype
    third_party/pdfium/third_party/lcms
    third_party/pdfium/third_party/libopenjpeg20
    third_party/pdfium/third_party/libpng16
    third_party/pdfium/third_party/libtiff
    third_party/pdfium/third_party/skia_shared
    third_party/perfetto
    third_party/pffft
    third_party/ply
    third_party/polymer
    third_party/private-join-and-compute
    third_party/protobuf
    third_party/protobuf/third_party/six
    third_party/pyjson5
    third_party/qcms
    third_party/rnnoise
    third_party/s2cellid
    third_party/schema_org
    third_party/securemessage
    third_party/simplejson
    third_party/skia
    third_party/skia/third_party/skcms
    third_party/skia/third_party/vulkan
    third_party/skia/include/third_party/vulkan/
    third_party/skia/include/third_party/skcms/
    third_party/smhasher
    third_party/spirv-headers
    third_party/SPIRV-Tools
    third_party/sqlite
    third_party/swiftshader
    third_party/swiftshader/third_party/astc-encoder
    third_party/swiftshader/third_party/llvm-10.0
    third_party/swiftshader/third_party/llvm-subzero
    third_party/swiftshader/third_party/marl
    third_party/swiftshader/third_party/subzero
    third_party/swiftshader/third_party/SPIRV-Headers/include/spirv/unified1
    third_party/tcmalloc
    third_party/ukey2
    third_party/usrsctp
    third_party/vulkan
    third_party/web-animations-js
    third_party/webdriver
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
    third_party/xcbproto
    third_party/zxcvbn-cpp
    third_party/zlib/google
    tools/grit/third_party/six
    url/third_party/mozilla
    v8/src/third_party/siphash
    v8/src/third_party/valgrind
    v8/src/third_party/utf8-decoder
    v8/third_party/inspector_protocol
    v8/third_party/v8/builtins
)
%if %{with wayland}
keeplibs+=(
    third_party/v4l-utils
    third_party/wayland
    third_party/wayland-protocols
)
%endif
%if !%{with system_harfbuzz}
keeplibs+=(
    third_party/freetype
    third_party/harfbuzz-ng
)
%endif
%if !%{with system_icu}
keeplibs+=( third_party/icu )
%endif
%if !%{with system_vpx}
keeplibs+=(
    third_party/libvpx
    third_party/libvpx/source/libvpx/third_party/x86inc
)
%endif
# needed due to bugs in GN
keeplibs+=(
    third_party/adobe
    third_party/speech-dispatcher
    third_party/usb_ids
    third_party/xdg-utils
)
build/linux/unbundle/remove_bundled_libraries.py "${keeplibs[@]}" --do-remove

%build
# GN sets lto on its own and we need just ldflag options, not cflags
%define _lto_cflags %{nil}
%if %{with clang}
export CC=clang
export CXX=clang++
%else
# REDUCE DEBUG as it gets TOO large
ARCH_FLAGS="`echo %{optflags} | sed -e 's/^-g / /g' -e 's/ -g / /g' -e 's/ -g$//g'`"
export CXXFLAGS="${ARCH_FLAGS} -fpermissive -Wno-return-type"
# extra flags to reduce warnings that aren't very useful
export CXXFLAGS="${CXXFLAGS} -Wno-pedantic -Wno-unused-result -Wno-unused-function -Wno-unused-variable -Wno-unused-but-set-variable -Wno-deprecated-declarations"
# ignore warnings for minor mistakes that are too common
export CXXFLAGS="${CXXFLAGS} -Wno-return-type -Wno-parentheses -Wno-misleading-indentation"
# ignore warnings that are not supported well until gcc 8
export CXXFLAGS="${CXXFLAGS} -Wno-attributes -Wno-subobject-linkage"
# ignore warnings due to gcc bug (https://gcc.gnu.org/bugzilla/show_bug.cgi?id=84055)
export CXXFLAGS="${CXXFLAGS} -Wno-ignored-attributes"
# ingore new gcc 8 warnings that aren't yet handled upstream
export CXXFLAGS="${CXXFLAGS} -Wno-address -Wno-dangling-else -Wno-class-memaccess -Wno-invalid-offsetof -Wno-packed-not-aligned"
%if %{with wayland}
# for wayland
export CXXFLAGS="${CXXFLAGS} -I/usr/include/libxkbcommon"
%endif
export CFLAGS="${CXXFLAGS}"
export CC=gcc
export CXX=g++
export AR=ar
export NM=nm
%if 0%{?suse_version} <= 1500
export CC=gcc-10
export CXX=g++-10
# some still call gcc/g++
mkdir -p "$HOME/bin/"
ln -sfn %{_bindir}/$CC $HOME/bin/gcc
ln -sfn %{_bindir}/$CXX $HOME/bin/g++
export PATH="$HOME/bin/:$PATH"
%endif
%endif
# do not eat all memory
%limit_build -m 2600
%if %{with lto}
# reduce the threads for linking even more due to LTO eating ton of memory
_link_threads=$(((%{jobs} - 2)))
test "$_link_threads" -le 0 && _link_threads=1
export LDFLAGS="-flto=$_link_threads --param lto-max-streaming-parallelism=1"
%endif

# Set system libraries to be used
gn_system_libraries=(
    ffmpeg
    flac
    fontconfig
    libdrm
    libevent
    libjpeg
    libpng
    libxslt
    libusb
    libwebp
    libxml
    opus
    re2
    snappy
    zlib
)
%if %{with system_harfbuzz}
gn_system_libraries+=(
    harfbuzz-ng
    freetype
)
%endif
%if %{with system_icu}
gn_system_libraries+=( icu )
%endif
%if %{with system_vpx}
gn_system_libraries+=( libvpx )
%endif
build/linux/unbundle/replace_gn_files.py --system-libraries ${gn_system_libraries[@]}

# Create the configuration for GN
# Available options: out/Release/gn args --list out/Release/
myconf_gn=""
myconf_gn+=" custom_toolchain=\"//build/toolchain/linux/unbundle:default\""
myconf_gn+=" host_toolchain=\"//build/toolchain/linux/unbundle:default\""
myconf_gn+=" use_custom_libcxx=false"
myconf_gn+=" is_debug=false"
myconf_gn+=" enable_nacl=false"
%if %{with swiftshader}
myconf_gn+=" use_swiftshader_with_subzero=true"
%endif
myconf_gn+=" is_component_ffmpeg=true"
myconf_gn+=" use_cups=true"
myconf_gn+=" use_aura=true"
myconf_gn+=" concurrent_links=1"
myconf_gn+=" symbol_level=1"
myconf_gn+=" blink_symbol_level=0"
myconf_gn+=" use_kerberos=true"
myconf_gn+=" enable_vr=false"
myconf_gn+=" optimize_webui=false"
myconf_gn+=" enable_reading_list=false"
myconf_gn+=" use_pulseaudio=true link_pulseaudio=true"
myconf_gn+=" is_component_build=false"
myconf_gn+=" use_sysroot=false"
myconf_gn+=" fatal_linker_warnings=false"
%ifnarch aarch64
# Current tcmalloc does not support AArch64
myconf_gn+=" use_allocator=\"tcmalloc\""
%endif
myconf_gn+=" fieldtrial_testing_like_official_build=true"
myconf_gn+=" use_gold=true"
myconf_gn+=" use_gnome_keyring=false"
myconf_gn+=" use_unofficial_version_number=false"
myconf_gn+=" use_lld=false"
myconf_gn+=" use_vaapi=true"
myconf_gn+=" use_sysroot=false"
myconf_gn+=" treat_warnings_as_errors=false"
myconf_gn+=" enable_widevine=true"
myconf_gn+=" use_dbus=true"
# See dependency logic in third_party/BUILD.gn
%if %{with system_harfbuzz}
myconf_gn+=" use_system_harfbuzz=true"
myconf_gn+=" use_system_freetype=true"
%endif
myconf_gn+=" enable_hangout_services_extension=true"
myconf_gn+=" enable_vulkan=true"
%if %{with pipewire}
myconf_gn+=" rtc_use_pipewire=true rtc_link_pipewire=true"
myconf_gn+=" rtc_use_pipewire_version=\"0.3\""
%endif
# ozone stuff
%if %{with wayland}
myconf_gn+=" use_system_libdrm=true"
myconf_gn+=" use_system_minigbm=true use_xkbcommon=true"
myconf_gn+=" use_ozone=true ozone_auto_platforms=false"
myconf_gn+=" ozone_platform=\"x11\" ozone_platform_x11=true ozone_platform_gbm=true"
myconf_gn+=" ozone_platform_wayland=true ozone_platform_headless=true"
# use_v4l2_codec - uses patches in kernel-headers present on chromeos only
myconf_gn+=" use_v4lplugin=true use_v4l2_codec=false"
%endif
%if %{with clang}
myconf_gn+=" is_clang=true clang_base_path=\"/usr\" clang_use_chrome_plugins=false"
%else
myconf_gn+=" is_clang=false"
%endif
%if %{with lto}
myconf_gn+=" gcc_lto=true"
%endif
%if %{with system_icu}
myconf_gn+=" icu_use_data_file=false"
%endif

# The proprietary codecs just force the chromium to say they can use it and
# offload the actual computation to the ffmpeg, otherwise the chromium
# won't be able to load the codec even if the library can handle it
myconf_gn+=" proprietary_codecs=true"
myconf_gn+=" ffmpeg_branding=\"Chrome\""

%ifarch %{arm}
myconf_gn+=" target_cpu=\"arm\""
myconf_gn+=" arm_float_abi=\"hard\""
%ifarch armv6l armv6hl
myconf_gn+=" arm_version=6"
%else
myconf_gn+=" arm_version=7"
# Setting arm_use_neon to false breaks build
myconf_gn+=" arm_use_neon=true"
myconf_gn+=" arm_optionally_use_neon=true"
%endif
myconf_gn+=" arm_use_thumb=true"
%endif

%ifarch %{arm}
# We don't need to cross compile while building on an arm system.
sed -i 's|arm-linux-gnu-||g' build/toolchain/linux/BUILD.gn
sed -i 's|arm-linux-gnueabihf-||g' build/toolchain/linux/BUILD.gn
%endif

%ifarch aarch64
myconf_gn+=" target_cpu=\"arm64\""
%endif

%ifarch aarch64
# We don't need to cross compile while building on an aarch64 system.
sed -i 's|aarch64-linux-gnu-||g' build/toolchain/linux/BUILD.gn
%endif

# Set up Google API keys, see http://www.chromium.org/developers/how-tos/api-keys
# Note: these are for the openSUSE Chromium builds ONLY. For your own distribution,
# please get your own set of keys.
google_api_key="AIzaSyD1hTe85_a14kr1Ks8T3Ce75rvbR1_Dx7Q"
google_default_client_id="4139804441.apps.googleusercontent.com"
google_default_client_secret="KDTRKEZk2jwT_7CDpcmMA--P"

myconf_gn+=" google_api_key=\"${google_api_key}\""
myconf_gn+=" google_default_client_id=\"${google_default_client_id}\""
myconf_gn+=" google_default_client_secret=\"${google_default_client_secret}\""

# GN does not support passing cflags:
#  https://bugs.chromium.org/p/chromium/issues/detail?id=642016
gn gen --args="${myconf_gn}" out/Release

# bundled xcb proto for python2
export PYTHONPATH="$PWD/xcb-proto-1.14${PYTHONPATH+:}${PYTHONPATH}"

ninja -v %{?_smp_mflags} -C out/Release chrome chromedriver

%install
mkdir -p %{buildroot}%{_libdir}/chromium
mkdir -p %{buildroot}%{_prefix}/lib/
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{SOURCE100} %{buildroot}%{_bindir}/chromium

# x86_64 capable systems need this
sed -i "s|%{_prefix}/lib/chromium|%{_libdir}/chromium|g" %{buildroot}%{_bindir}/chromium

mkdir -p %{buildroot}%{_mandir}/man1/
pushd out/Release

# Install the file %{_sysconfdir}/default/chromium which defines the chromium flags
mkdir -p %{buildroot}%{_sysconfdir}/default
install -m 644 %{SOURCE103} %{buildroot}%{_sysconfdir}/default/chromium

cp -a *.bin *.pak locales %{buildroot}%{_libdir}/chromium/

# This is ANGLE, not to be confused with the similarly named files under swiftshader/
cp -a libEGL.so* libGLESv2.so* %{buildroot}%{_libdir}/chromium/
rm %{buildroot}%{_libdir}/chromium/*.so.TOC

%if !%{with system_icu}
cp -a icudtl.dat %{buildroot}%{_libdir}/chromium/
%endif

%if %{with swiftshader}
# general folder for these is swiftshader bsc#1176450
mkdir -p %{buildroot}%{_libdir}/chromium/swiftshader
cp -a swiftshader/*.so %{buildroot}%{_libdir}/chromium/swiftshader/
%endif

# chromedriver
cp -a chromedriver %{buildroot}%{_libdir}/chromium/
ln -s %{_libdir}/chromium/chromedriver %{buildroot}%{_bindir}/chromedriver

cp -a resources.pak %{buildroot}%{_libdir}/chromium/
cp -a chrome %{buildroot}%{_libdir}/chromium/chromium
popd

install -Dm 0644 chrome/app/theme/chromium/product_logo_256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/chromium-browser.png
install -Dm 0644 chrome/app/theme/chromium/product_logo_128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/chromium-browser.png
install -Dm 0644 chrome/app/theme/chromium/product_logo_64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/chromium-browser.png
install -Dm 0644 chrome/app/theme/chromium/product_logo_48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/chromium-browser.png
install -Dm 0644 chrome/app/theme/chromium/product_logo_24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/chromium-browser.png
install -Dm 0644 %{SOURCE104} %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/chromium-browser-symbolic.svg

mkdir -p %{buildroot}%{_datadir}/applications/
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE101}

install -D -m0644 chrome/installer/linux/common/chromium-browser/chromium-browser.appdata.xml %{buildroot}%{_datadir}/metainfo/chromium-browser.appdata.xml

mkdir -p %{buildroot}%{_datadir}/gnome-control-center/default-apps/
cp -a %{SOURCE102} %{buildroot}%{_datadir}/gnome-control-center/default-apps/

# link to browser plugin path.  Plugin patch doesn't work. Why?
mkdir -p %{buildroot}%{_libdir}/browser-plugins
pushd %{buildroot}%{_libdir}/chromium
ln -s ../browser-plugins plugins
popd

# Install the master_preferences file
mkdir -p %{buildroot}%{_sysconfdir}/chromium
install -m 0644 %{SOURCE30} %{buildroot}%{_sysconfdir}/chromium

# install manpages
mkdir -p %{buildroot}%{_mandir}/man1/
cp -a chrome/app/resources/manpage.1.in %{buildroot}%{_mandir}/man1/chromium.1
sed -i "s|@@PACKAGE@@|chromium|g" %{buildroot}%{_mandir}/man1/chromium.1
sed -i "s|@@MENUNAME@@|Chromium|g" %{buildroot}%{_mandir}/man1/chromium.1

%fdupes %{buildroot}

%post
%icon_theme_cache_post
%desktop_database_post
/sbin/ldconfig %{_libdir}/chromium

%postun
%icon_theme_cache_postun
%desktop_database_postun
/sbin/ldconfig %{_libdir}/chromium

%files
%license LICENSE
%doc AUTHORS
%config %{_sysconfdir}/chromium
%config(noreplace) %{_sysconfdir}/default/chromium
%dir %{_datadir}/gnome-control-center
%dir %{_datadir}/gnome-control-center/default-apps
%{_libdir}/chromium/
%if %{with swiftshader}
%dir %{_libdir}/chromium/swiftshader/
%{_libdir}/chromium/swiftshader/*.so
%endif
%{_libdir}/chromium/*.so
%{_datadir}/applications/*.desktop
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/chromium-browser.appdata.xml
%{_datadir}/gnome-control-center/default-apps/chromium-browser.xml
%{_datadir}/icons/hicolor/
%exclude %{_libdir}/chromium/chromedriver
%{_bindir}/chromium
%{_mandir}/man1/chromium.1%{?ext_man}

%files -n chromedriver
%{_libdir}/chromium/chromedriver
%{_bindir}/chromedriver

%changelog
