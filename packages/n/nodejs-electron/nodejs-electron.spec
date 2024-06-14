#
# spec file for package nodejs-electron
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2021-2022 Andreas Schneider <asn@cryptomilk.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
# 
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# https://fedoraproject.org/wiki/Changes/SetBuildFlagsBuildCheck
%undefine _auto_set_build_flags

%define mod_name electron
# https://github.com/nodejs/node/blob/main/doc/abi_version_registry.json
%define abi_version 121

# Do not provide libEGL.so, etc…
%define __provides_exclude ^lib.*\\.so.*$

# Double DWZ memory limits
%define _dwz_low_mem_die_limit  20000000
%define _dwz_max_die_limit     100000000


#x86 requires SSE2
#see v8/src/codegen/ia32/assembler-ia32.cc
%ifarch %ix86
ExclusiveArch:  i586 i686
BuildArch:      i686
%{expand:%%global optflags %(echo "%optflags") -march=pentium4 -mtune=generic}
%endif


%bcond_without pipewire

%bcond_without swiftshader
%ifarch %ix86 x86_64 %x86_64 %arm
#Use subzero as swiftshader backend instead of LLVM
%bcond_without subzero
%else
%bcond_with subzero
%endif

#Not enabling this yet, as of electron 29 there are minor font rendering issues in menu, and the benefits are dubious
#(all the widgets use Gtk unconditionally — not sure which of the changed codepaths are used in Electron)
%bcond_with qt




%ifarch aarch64 riscv64
#Video acceleration API to support. Useful for e.g. signal messenger.
#One cannot enable both, unfortunately.
#Apparently more arm hardware supports v4l2 than vaapi,
#but that code does not build on armv{6,7}hl due to too high cpu requirements.
#bcond_without v4l2
#bcond_with vaapi
%else
#bcond_with v4l2
#bcond_without vaapi
%endif

#DISABLING THIS — cannot use video acceleration with system aom/vpx
%bcond_with v4l2
%bcond_with vaapi



%ifnarch %ix86 %arm

%if (0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700 || 0%{?fedora})
%bcond_without lto
%else
%bcond_with lto
%endif

%else
%bcond_with lto
%endif



%if 0%{?suse_version} || 0%{?fedora} < 40
%bcond_without system_minizip
%else
%bcond_with system_minizip
%endif


%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150600 || 0%{?fedora}
%bcond_without system_aom
%bcond_without system_spirv
%bcond_without harfbuzz_5
%bcond_without link_vulkan
%bcond_without wayland_32
%else
%bcond_with system_aom
%bcond_with system_spirv
%bcond_with harfbuzz_5
%bcond_with link_vulkan
%bcond_with wayland_32
%endif


%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150600
%bcond_without system_yuv
%else
%bcond_with system_yuv
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700 || 0%{?fedora}
%bcond_without ffmpeg_5
%bcond_without system_vpx
%else
%bcond_with ffmpeg_5
%bcond_with system_vpx
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700 || 0%{?fedora} >= 39
%bcond_without bro_11
%bcond_without ffmpeg_6
%else
%bcond_with bro_11
%bcond_with ffmpeg_6
%endif



%if 0%{?fedora}
%bcond_without system_llhttp
%bcond_without system_histogram
%bcond_without system_simdutf
%else
%bcond_with system_llhttp
%bcond_with system_histogram
%bcond_with system_simdutf
%endif


%if 0%{?fedora} >= 39
%bcond_without system_vma
%else
%bcond_with system_vma
%endif


#requires `imageSequenceTrackPresent` and `enableParsingGainMapMetadata` both of which are only in post-1.0.0 nightlies
%bcond_with system_avif

# Some chromium code assumes absl::string_view is a typedef for std::string_view. This is not true on GCC7 systems such as Leap.
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700 || 0%{?fedora} >= 39
%bcond_without system_abseil
%else
%bcond_with system_abseil
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700
#re2-11 has abseil as a public dependency. If you use system re2 you must use system abseil.
%bcond_without system_re2
%else
%bcond_with system_re2
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700 || 0%{?fedora}
%define PYVER 3
%else
%define PYVER 311
%endif

%if 0%{?fedora} >= 40
%define AVFORMAT_VER 6.0.1
%define RPMFUSION_VER 6.1-3
%endif
%if 0%{?fedora} >= 38 && 0%{?fedora} < 40
%define AVFORMAT_VER 6.0.1
%define RPMFUSION_VER 6.0.1-2
%endif


%if 0%{?suse_version}
%{expand:%%global NODEJS_DEFAULT_VER %(echo %{nodejs_version}|sed 's/\..*//')}
%else
%global NODEJS_DEFAULT_VER %nil
%endif

# We always ship the following bundled libraries as part of Electron despite a system version being available in either openSUSE or Fedora:
# Name         | Path in tarball                   | Reason
# -------------+-----------------------------------+---------------------------------------
# boringssl    | third_party/boringssl             | The openSUSE package is unmaintained.
# hunspell     | third_party/hunspell/src          | Fork.
# leveldb      | third_party/leveldatabase/src     | Internal api use.
# protobuf     | third_party/protobuf              | Fork.
# rnnoise      | third_party/rnnoise               | Internal api use.
# sqlite       | third_party/sqlite                | Fork.
# srtp / srtp2 | third_party/libsrtp               | Needs to be built against boringssl, not openssl
# uv           | third_party/electron_node/deps/uv | Heavily modified version which is exposed as part of Electron's public ABI.




Name:           nodejs-electron
Version:        29.4.2
%global tag_version %version
Release:        0
Summary:        Build cross platform desktop apps with JavaScript, HTML, and CSS
License:        Apache-2.0 AND blessing AND BSD-2-Clause AND BSD-3-Clause AND BSD-Source-Code AND bzip2-1.0.6 AND ISC AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND MIT-CMU AND MIT-open-group AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later) AND MPL-2.0 AND OpenSSL AND SGI-B-2.0 AND SUSE-Public-Domain AND X11%{!?with_system_minizip: AND Zlib}
Group:          Development/Languages/NodeJS
URL:            https://github.com/electron/electron
Source0:        %{mod_name}-%{tag_version}.tar.zst
Source1:        create_tarball.sh
Source10:       electron-launcher.sh
Source11:       electron.desktop


# Reverse upstream changes to be able to build against ffmpeg-4
Source400:      ffmpeg-new-channel-layout.patch
Source401:      audio_file_reader-ffmpeg-AVFrame-duration.patch
Source402:      Cr122-ffmpeg-new-channel-layout.patch
# and against harfbuzz 4
Source415:      harfbuzz-replace-chromium-scoped-type.patch
Source416:      harfbuzz-replace-HbScopedPointer.patch
# and wayland 1.31
Source450:      wayland-proto-31-cursor-shape.patch


# PATCHES for openSUSE-specific things (compiler flags, paths, etc.)
Patch0:         chromium-102-compiler.patch
Patch1:         fpic.patch
Patch2:         common.gypi-compiler.patch
Patch3:         gcc-enable-lto.patch
Patch7:         chromium-91-java-only-allowed-in-android-builds.patch
# Always disable use_thin_lto which is an lld feature
Patch21:        electron-13-fix-use-thin-lto.patch
# Fix common.gypi to include /usr/include/electron
Patch25:        electron-16-system-node-headers.patch
# https://sources.debian.org/patches/chromium/102.0.5005.115-1/debianization/support-i386.patch/
Patch39:        support-i386.patch
Patch69:        nasm-generate-debuginfo.patch
Patch74:        common.gypi-remove-fno-omit-frame-pointer.patch
Patch75:        gcc-asmflags.patch
Patch77:        angle_link_glx.patch
Patch78:        rdynamic.patch
Patch80:        icon.patch
Patch82:        node-compiler.patch
Patch84:        aarch64-Xclang.patch
Patch85:        devtools-frontend-compress_files-oom.patch


# PATCHES that remove code we don't want. Most of them can be reused verbatim by other distributors,
# and some of them probably should be submitted upstream (at least to Electron, not necessarily to Chromium)

# from https://sources.debian.org/patches/chromium/103.0.5060.53-1/disable/catapult.patch/
Patch567:       disable-catapult.patch
Patch570:       disable-fuses.patch
# https://code.qt.io/cgit/qt/qtwebengine-chromium.git/commit/?h=102-based&id=d617766b236a93749ddbb50b75573dd35238ffc9
Patch573:       disable-webspeech.patch
# https://sources.debian.org/patches/chromium/108.0.5359.124-1/disable/tests.patch/
Patch576:       disable-devtools-tests.patch
Patch581:       disable-tests.patch
Patch583:       remove-rust.patch
Patch585:       remove-dawn.patch
Patch586:       aom-vpx-no-thread-wrapper.patch
Patch587:       remove-openscreen.patch
Patch588:       remove-password-manager-and-policy.patch
Patch589:       remove-puffin.patch
Patch590:       remove-sync.patch




# PATCHES to use system libs
Patch1000:      do-not-build-libvulkan.so.patch
Patch1017:      system-libdrm.patch
# http://svnweb.mageia.org/packages/updates/7/chromium-browser-stable/current/SOURCES/chromium-74-pdfium-system-libopenjpeg2.patch?view=markup
Patch1038:      pdfium-fix-system-libs.patch
# https://sources.debian.org/patches/chromium/102.0.5005.115-1/system/zlib.patch/
Patch1041:      system-zlib.patch
Patch1045:      angle-system-xxhash.patch
Patch1047:      cares_public_headers.patch
Patch1048:      chromium-remove-bundled-roboto-font.patch
Patch1053:      swiftshader-use-system-llvm.patch
Patch1063:      system-libbsd.patch
Patch1065:      base-system-nspr.patch
Patch1066:      system-gtest.patch
Patch1068:      system-six.patch
Patch1069:      system-usb_ids.patch
Patch1070:      skia-system-vulkan-headers.patch
Patch1071:      system-pydeps.patch
Patch1072:      node-system-icu.patch
Patch1073:      system-nasm.patch
Patch1074:      no-zlib-headers.patch
Patch1076:      crashpad-use-system-abseil.patch
Patch1077:      system-wayland.patch
Patch1078:      system-simdutf.patch
Patch1079:      system-libm.patch
Patch1080:      system-yuv.patch
Patch1081:      chromium-122-abseil-shims.patch


# PATCHES to fix interaction with third-party software
Patch2004:      chromium-gcc11.patch
Patch2010:      chromium-93-ffmpeg-4.4.patch

#Since ffmpeg 5, there is no longer first_dts member in AVFormat. Chromium upstream (and Tumbleweed) patches ffmpeg to add a av_stream_get_first_dts function.
#Upstream ref: https://chromium-review.googlesource.com/c/chromium/src/+/3525614
#This patch is only for Leap which uses ffmpeg 4. It makes chromium use the old api and does not work with ffmpeg 5.
Patch2012:      chromium-94-ffmpeg-roll.patch

# Fixe builds with older clang versions that do not allow
# nomerge attributes on declaration. Otherwise, the following error
# is produced:
#     'nomerge' attribute cannot be applied to a declaration
# See https://reviews.llvm.org/D92800
Patch2022:      electron-13-fix-base-check-nomerge.patch
# Fix electron patched code
Patch2024:      electron-16-std-vector-non-const.patch
Patch2029:      electron-16-webpack-fix-openssl-3.patch
Patch2031:      partition_alloc-no-lto.patch
Patch2032:      seccomp_bpf-no-lto.patch
Patch2034:      swiftshader-LLVMJIT-AddressSanitizerPass-dead-code-remove.patch
Patch2035:      RenderFrameHostImpl-use-after-free.patch
# https://github.com/electron/electron/pull/40032
Patch2040:      build-without-extensions.patch
%if %{without bro_11}
Patch2042:      brotli-remove-shared-dictionary.patch
%else
Source2042:     brotli-remove-shared-dictionary.patch
%endif
Patch2045:      libxml-2.12-xmlCtxtGetLastError-const.patch
Patch2046:      chromium-118-sigtrap_system_ffmpeg.patch
%if %{with system_minizip}
Source2047:     bundled-minizip.patch
%else
Patch2047:      bundled-minizip.patch
%endif
Patch2048:      absl2023-encapsulated_web_transport-StrCat.patch

# PATCHES that should be submitted upstream verbatim or near-verbatim
Patch3016:      chromium-98-EnumTable-crash.patch
# Fix blink nodestructor
Patch3023:      electron-13-blink-gcc-ambiguous-nodestructor.patch
Patch3027:      electron-16-freetype-visibility-list.patch
Patch3028:      electron-16-third_party-symbolize-missing-include.patch
# From https://git.droidware.info/wchen342/ungoogled-chromium-fedora
Patch3033:      chromium-94.0.4606.71-InkDropHost-crash.patch
# https://salsa.debian.org/chromium-team/chromium/-/blob/456851fc808b2a5b5c762921699994e957645917/debian/patches/upstream/nested-nested-nested-nested-nested-nested-regex-patterns.patch
Patch3064:      nested-nested-nested-nested-nested-nested-regex-patterns.patch
Patch3080:      compact_enc_det_generated_tables-Wnarrowing.patch
Patch3096:      remove-date-reproducible-builds.patch
Patch3118:      material_color_utilities-tones-missing-round.patch
Patch3126:      perfetto-numeric_storage-double_t.patch
Patch3129:      text_break_iterator-icu74-breakAllLineBreakClassTable-should-be-consistent.patch
Patch3132:      v8-instance-type-inl-constexpr-used-before-its-definition.patch
Patch3133:      swiftshader-llvm18-LLVMReactor-getInt8PtrTy.patch
Patch3134:      swiftshader-llvm18-LLVMJIT-Host.patch
Patch3135:      swiftshader-llvm18-LLVMJIT-CodeGenOptLevel.patch
Patch3136:      CVE-2024-30260-undici-clear-proxy-authorization.patch
Patch3137:      CVE-2024-30261-undici-fetch-integrity.patch
Patch3138:      distributed_point_functions-aes_128_fixed_key_hash-missing-StrCat.patch
Patch3139:      chromium-122-avoid-SFINAE-TypeConverter.patch
Patch3140:      plus_address_types-missing-optional.patch
Patch3141:      chromium-122-BookmarkNode-missing-operator.patch
Patch3142:      search_engine_choice_service-missing-optional.patch
Patch3143:      race_network_request_write_buffer_manager-missing-optional.patch
Patch3144:      mt21_util-flax-vector-conversions.patch
Patch3145:      script_promise_resolver-explicit-specialization.patch
Patch3146:      hit_test_request-missing-optional.patch
Patch3147:      grid_sizing_tree-Wchanges-meaning.patch
Patch3148:      resolution_monitor-missing-bitset.patch
Patch3149:      boringssl-internal-addc-cxx.patch
Patch3150:      InternalAllocator-too-many-initializers.patch
Patch3151:      distributed_point_functions-evaluate_prg_hwy-signature.patch
Patch3152:      fake_ssl_socket_client-Wlto-type-mismatch.patch
Patch3153:      ElectronDesktopWindowTreeHostLinux-OnWindowTiledStateChanged-crash.patch

# Patches to re-enable upstream force disabled features.
# There's no sense in submitting them but they may be reused as-is by other packagers.
Patch5000:      more-locales.patch
Patch5006:      chromium-vaapi.patch

BuildRequires:  brotli
%if %{with system_cares}
BuildRequires:  c-ares-devel
%endif
BuildRequires:  cmake(Crc32c)
BuildRequires:  double-conversion-devel
BuildRequires:  desktop-file-utils
%if 0%{?fedora}
BuildRequires:  flatbuffers-compiler
%endif
BuildRequires:  flatbuffers-devel
BuildRequires:  gn >= 0.1807
BuildRequires:  gperf
%if %{with system_histogram}
BuildRequires:  HdrHistogram_c-devel
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  hwdata
BuildRequires:  ImageMagick
%if 0%{?fedora}
BuildRequires:  libatomic
%endif
%if %{with system_aom}
# requires AV1E_SET_QUANTIZER_ONE_PASS
BuildRequires:  libaom-devel >= 3.7~
%endif
BuildRequires:  libbsd-devel
BuildRequires:  libpng-devel
BuildRequires:  libXNVCtrl-devel
%if %{with system_llhttp}
BuildRequires:  llhttp-devel >= 8
%endif
%if %{with swiftshader} && %{without subzero}
BuildRequires:  llvm-devel >= 16
%endif
BuildRequires:  memory-constraints
%ifarch %ix86 x86_64 %x86_64
%if %{without system_aom} || %{without system_vpx}
BuildRequires:  nasm
%endif
%endif
%if 0%{?suse_version}
BuildRequires:  ninja >= 1.7.2
%else
BuildRequires:  ninja-build >= 1.7.2
%endif
%if 0%{?fedora} >= 37
BuildRequires:  nodejs-npm
%else
BuildRequires:  npm
%endif
%if 0%{?suse_version}
BuildRequires: nodejs-packaging
%endif
BuildRequires:  pkgconfig
BuildRequires:  plasma-wayland-protocols
BuildRequires:  python3-json5
BuildRequires:  python%{PYVER}-jinja2 >= 3.0.2
BuildRequires:  python3-mako
BuildRequires:  python%{PYVER}-ply
BuildRequires:  python%{PYVER}-PyYAML >= 6
%if 0%{?fedora}
BuildRequires:  (python3-setuptools if python3 >= 3.12)
%endif
BuildRequires:  python%{PYVER}-six
%if %{with system_simdutf}
BuildRequires:  simdutf-devel >= 3
%endif
BuildRequires:  snappy-devel
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  util-linux
BuildRequires:  vulkan-headers
%if %{with system_vma}
BuildRequires:  VulkanMemoryAllocator-devel >= 3
%endif
BuildRequires:  wayland-devel >= 1.20
BuildRequires:  zstd
%if %{with system_abseil}
BuildRequires:  pkgconfig(absl_absl_check)
BuildRequires:  pkgconfig(absl_algorithm_container)
BuildRequires:  pkgconfig(absl_any_invocable)
BuildRequires:  pkgconfig(absl_base)
BuildRequires:  pkgconfig(absl_bind_front)
BuildRequires:  pkgconfig(absl_bits)
BuildRequires:  pkgconfig(absl_btree)
BuildRequires:  pkgconfig(absl_cleanup)
BuildRequires:  pkgconfig(absl_config)
BuildRequires:  pkgconfig(absl_cord)
BuildRequires:  pkgconfig(absl_core_headers)
BuildRequires:  pkgconfig(absl_failure_signal_handler)
BuildRequires:  pkgconfig(absl_fixed_array)
BuildRequires:  pkgconfig(absl_flags)
BuildRequires:  pkgconfig(absl_flags_parse)
BuildRequires:  pkgconfig(absl_flags_usage)
BuildRequires:  pkgconfig(absl_flat_hash_map)
BuildRequires:  pkgconfig(absl_flat_hash_set)
BuildRequires:  pkgconfig(absl_hash)
BuildRequires:  pkgconfig(absl_inlined_vector)
BuildRequires:  pkgconfig(absl_int128)
BuildRequires:  pkgconfig(absl_memory)
BuildRequires:  pkgconfig(absl_node_hash_map)
BuildRequires:  pkgconfig(absl_node_hash_set)
BuildRequires:  pkgconfig(absl_optional)
BuildRequires:  pkgconfig(absl_random_random)
BuildRequires:  pkgconfig(absl_span)
BuildRequires:  pkgconfig(absl_stacktrace)
BuildRequires:  pkgconfig(absl_status)
BuildRequires:  pkgconfig(absl_statusor)
BuildRequires:  pkgconfig(absl_strings)
BuildRequires:  pkgconfig(absl_str_format)
BuildRequires:  pkgconfig(absl_symbolize)
BuildRequires:  pkgconfig(absl_synchronization)
BuildRequires:  pkgconfig(absl_time)
BuildRequires:  pkgconfig(absl_type_traits)
BuildRequires:  pkgconfig(absl_utility)
BuildRequires:  pkgconfig(absl_variant)
BuildRequires:  pkgconfig(absl_core_headers) >= 20230000
%endif
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo) >= 1.6
BuildRequires:  pkgconfig(dav1d) >= 1
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(harfbuzz) >= 3
%if %{with harfbuzz_5}
BuildRequires:  pkgconfig(harfbuzz) >= 5
%endif
BuildRequires:  pkgconfig(icu-i18n) >= 73
BuildRequires:  pkgconfig(jsoncpp)
%if 0%{?fedora}
Recommends: (ffmpeg-libs%{_isa} or libavcodec-freeworld%{_isa})
%endif
%if %{with ffmpeg_6}
BuildRequires:  pkgconfig(libavcodec) >= 60
%endif
%if %{with ffmpeg_5}
BuildRequires:  pkgconfig(libavcodec) >= 59
BuildRequires:  pkgconfig(libavformat) >= 59
BuildRequires:  pkgconfig(libavutil) >= 57
%if 0%{?fedora}
#requires av_stream_get_first_dts, see rhbz#2240127
BuildRequires:  libavformat-free-devel >= %AVFORMAT_VER
Requires: (ffmpeg-libs%{_isa} >= %RPMFUSION_VER or libavformat-free%{_isa} >= %AVFORMAT_VER)
# have choice for libvpl.so.2()(64bit) needed by libavcodec-free: libvpl oneVPL
%ifarch x86_64 %x86_64
BuildRequires:  oneVPL
%endif
%endif
%else
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat) >= 58
BuildRequires:  pkgconfig(libavutil)
%endif
%if %{with system_avif}
# Needs avifRGBImage::maxThreads
BuildRequires:  pkgconfig(libavif) >= 1
%endif
%if %{with bro_11}
BuildRequires:  pkgconfig(libbrotlicommon) >= 1.1~
%endif
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libhwy) >= 1
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsecret-1)
%if %{with vaapi}
BuildRequires:  pkgconfig(libva)
%endif
BuildRequires:  pkgconfig(libwebp) >= 0.4.0
BuildRequires:  pkgconfig(libwoff2dec)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.5
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(libxxhash)
%if %{with system_yuv}
# needs I410ToI420
BuildRequires:  pkgconfig(libyuv) >= 1855
%endif
%if %{with system_minizip}
%if 0%{?fedora}
BuildRequires:  minizip-compat-devel
%else
BuildRequires:  pkgconfig(minizip)
%endif
%endif
BuildRequires:  pkgconfig(nspr) >= 4.9.5
BuildRequires:  pkgconfig(nss) >= 3.26
BuildRequires:  pkgconfig(opus) >= 1.3.1
BuildRequires:  pkgconfig(pangocairo)
%if %{with qt}
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Widgets)
%endif
%if %{with system_abseil} && %{with system_re2}
#re2-11 has abseil as a public dependency. If you use system re2 you must use system abseil.
BuildRequires:  cmake(re2) >= 11
%endif
%if %{with system_spirv}
%if 0%{?suse_version}
BuildRequires:  spirv-headers
%else
BuildRequires:  spirv-headers-devel
%endif
BuildRequires:  pkgconfig(SPIRV-Tools) >= 2022.2
BuildRequires:  vulkan-headers >= 1.3
%endif
%if %{with link_vulkan}
BuildRequires:  pkgconfig(vulkan) >= 1.3
%endif
BuildRequires:  pkgconfig(wayland-protocols)
%if %{with wayland_32}
BuildRequires:  pkgconfig(wayland-protocols) >= 1.32
%endif
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version}
BuildRequires:  libjpeg-devel >= 8.1
%else
BuildRequires:  libjpeg-turbo-devel
%endif
%if %{with system_vpx}
# requires VP9E_SET_QUANTIZER_ONE_PASS
BuildRequires:  pkgconfig(vpx) >= 1.13~
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700 || 0%{?fedora}
BuildRequires:  gcc >= 13
BuildRequires:  gcc-c++ >= 13
%else
BuildRequires:  gcc13-PIE
BuildRequires:  gcc13-c++
%endif
%if %{with pipewire}
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libspa-0.2)
%endif

Requires:       hicolor-icon-theme
Requires:       google-roboto-fonts

# This required library is dlopened
%if %{without link_vulkan}
%ifarch %ix86 %arm
Requires:       libvulkan.so.1
%else
Requires:       libvulkan.so.1()(64bit)
%endif
%endif

%if %{with qt}
%if 0%{?fedora}
Requires: (nodejs-electron-qt5%{_isa} if qt5-qtbase-gui%{_isa})
Requires: (nodejs-electron-qt6%{_isa} if qt6-qtbase-gui%{_isa})
%else
Requires: (nodejs-electron-qt5%{_isa} if libQt5Gui5%{_isa})
Requires: (nodejs-electron-qt6%{_isa} if libQt6Gui6%{_isa})
%endif
%endif

Provides:       electron
Provides:       electron%{_isa}(abi) = %{abi_version}

Obsoletes:      nodejs-electron-prebuilt < %{version}
Provides:       nodejs-electron-prebuilt = %{version}

%description
Nodejs application: Build cross platform desktop apps with JavaScript, HTML, and CSS

%package devel
Summary:        Electron development headers
Group:          Development/Libraries/C and C++
Requires:       nodejs-electron%{_isa} = %{version}
Requires:       pkgconfig(zlib)
%if 0%{?suse_version}
Requires:       npm%{NODEJS_DEFAULT_VER}
%else
Requires:       nodejs-npm
%endif


%description devel
Development headers for Electron projects.

%package doc
Summary:        Electron API documentation
Group:          Documentation/Other
Enhances:       nodejs-electron-devel = %{version}
BuildArch:      noarch


%description doc
Development documentation for the Electron runtime.

%if %{with qt}
%package qt5
Summary:  Qt5 widgets for Electron
Group:    System/Libraries
Requires: nodejs-electron%{_isa} = %version

%description qt5
This is the Qt5-based UI backend for nodejs-electron,
providing better integration with desktop environments such as KDE.

%package qt6
Summary:  Qt6 widgets for Electron
Group:    System/Libraries
Requires: nodejs-electron%{_isa} = %version

%description qt6
This is the Qt6-based UI backend for nodejs-electron,
providing better integration with desktop environments such as KDE.
%endif

%prep
# Use stable path to source to make use of ccache
%autosetup -n src -p1




# Sanity check if macro corresponds to the actual ABI
test $(grep ^node_module_version electron/build/args/all.gn | sed 's/.* = //') = %abi_version

%if %{without system_abseil}
patch -R -p1 < %PATCH1076
%endif

%if %{without ffmpeg_6}
patch -R -p1 < %SOURCE402
%endif

%if %{with ffmpeg_5}
patch -R -p1 < %PATCH2012
%else
patch -R -p1 < %SOURCE400
%endif



%if %{without harfbuzz_5}
patch -R -p1 < %SOURCE415
patch -R -p1 < %SOURCE416
%endif


%if %{without wayland_32}
patch -R -p1 < %SOURCE450
%endif


# This one depends on an ffmpeg nightly, reverting unconditionally.
patch -R -p1 < %SOURCE401

# Link system wayland-protocols-devel into where chrome expects them
mkdir -p third_party/wayland/src
mkdir -p third_party/wayland-protocols/kde/src
ln -svfT %{_datadir}/wayland third_party/wayland/src/protocol
#mkdir -p third_party/wayland-protocols/mesa

ln -svfT %{_datadir}/wayland-protocols third_party/wayland-protocols/src
#ln -svfT %{_datadir}/wayland-eglstream third_party/wayland-protocols/mesa/wayland-drm
ln -svfT %{_datadir}/plasma-wayland-protocols third_party/wayland-protocols/kde/src/protocols

# Fix the path to nodejs binary
mkdir -p third_party/node/linux/node-linux-x64/bin
ln -sf %{_bindir}/node third_party/node/linux/node-linux-x64/bin/node

# Fix eu-strip
mkdir -p buildtools/third_party/eu-strip/bin
ln -sf %{_bindir}/eu-strip buildtools/third_party/eu-strip/bin/eu-strip

# Fix shim header generation
sed -i 's/OFFICIAL_BUILD/GOOGLE_CHROME_BUILD/' \
      tools/generate_shim_headers/generate_shim_headers.py


%build
pushd electron/shell/browser/resources/win
[ $(identify electron.ico | wc -l) = 4 ] #Sanity check
convert electron.ico -strip extracted.png
identify extracted-0.png | grep -F 16x16
identify extracted-1.png | grep -F 32x32
identify extracted-2.png | grep -F 48x48
identify extracted-3.png | grep -F 256x256
popd


# GN sets lto on its own and we need just ldflag options, not cflags
%define _lto_cflags %{nil}

# Make sure python is python3
install -d -m 0755 python3-path
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700 || 0%{?fedora}
ln -sf %{_bindir}/python3 "$(pwd)/python3-path/python"
%else
ln -sf %{_bindir}/python3.11 "$(pwd)/python3-path/python"
ln -sf %{_bindir}/python3.11 "$(pwd)/python3-path/python3"
%endif
export PATH="$(pwd)/python3-path:${PATH}"

#HACK: Those packages on Leap are available only in python3.6 versions.
%if 0%{?suse_version}  && 0%{?suse_version} < 1550
install -d -m 0755 python3-site
cp -pr %{python3_sitelib}/{json5,mako} -t "$(pwd)/python3-site"
export PYTHONPATH="$(pwd)/python3-site"
%endif

#some Fedora ports still try to build with LTO
ARCH_FLAGS=$(echo "%optflags"|sed 's/-f[^ ]*lto[^ ]*//g' )

#Work around an upstream ODR issue.
#Remove this once https://bugs.chromium.org/p/chromium/issues/detail?id=1375049 gets fixed.
ARCH_FLAGS="$ARCH_FLAGS -DIS_SERIAL_ENABLED_PLATFORM"




%if 0%{?fedora}
# Fix base/allocator/allocator_shim.cc:408:2: error: #error This code cannot be
# used when exceptions are turned on.
ARCH_FLAGS="$(echo $ARCH_FLAGS | sed -e 's/ -fexceptions / /g')"
%endif

# for wayland
export CXXFLAGS="${ARCH_FLAGS} -I/usr/include/wayland -I/usr/include/libxkbcommon"
export CFLAGS="${CXXFLAGS}"

# Google has a bad coding style, using a macro `NOTREACHED()` that is not properly detected by GCC
# multiple times throughout the codebase (including generated code). It is not possible to redefine the macro to __builtin_unreachable,
# as it has an astonishing syntax, behaving like an ostream (in debug builds it is supposed to trap and print an error message)
export CXXFLAGS="${CXXFLAGS} -Wno-error=return-type"
# [ 8947s] gen/third_party/blink/renderer/bindings/modules/v8/v8_gpu_sampler_descriptor.h:212:39: error: narrowing conversion of '4294967295' from 'unsigned int' to 'float' [-Wnarrowing]
# [ 8947s]   212 | float member_lod_max_clamp_{0xffffffff};
# I have no idea where this code is generated, and it is not something that needs a critical fix.
# Remove this once upstream issues a proper patch.
export CXXFLAGS="${CXXFLAGS} -Wno-error=narrowing"

# A bunch of memcpy'ing of JSObject in V8 runs us into “Logfile got too big, killed job.”
export CXXFLAGS="${CXXFLAGS} -Wno-class-memaccess"

# REDUCE DEBUG for C++ as it gets TOO large due to “heavy hemplate use in Blink”. See symbol_level below and chromium-102-compiler.patch
export CXXFLAGS="$(echo ${CXXFLAGS} | sed -e 's/-g / /g' -e 's/-g$//g')"

%ifnarch x86_64 %x86_64
export CFLAGS="$(echo ${CFLAGS} | sed -e 's/-g /-g1 /g' -e 's/-g$/-g1/g')"
%endif

#The chromium build process passes lots of .o files directly to the linker instead of using static libraries,
#and relies on the linker eliminating unused sections.
#Re-add these parameters from build/config/compiler/BUILD.gn.
export LDFLAGS="%{?build_ldflags} -Wl,-O2 -Wl,--gc-sections "



%ifarch %ix86 %arm
#try to reduce memory

export LDFLAGS="${LDFLAGS} -Wl,--no-keep-memory"
%endif #ifarch ix86 arm


%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700 || 0%{?fedora}
export CC=gcc
export CXX=g++
export AR=gcc-ar
export NM=gcc-nm
export RANLIB=gcc-ranlib
%else
export CC=gcc-13
export CXX=g++-13
export AR=gcc-ar-13
export NM=gcc-nm-13
export RANLIB=gcc-ranlib-13
%endif



# do not eat all memory
%ifarch %ix86 %arm
%limit_build -m 1200
%else
%limit_build -m 4000
%endif

%ifarch aarch64
#These settings make it use much more memory leading to OOM during linking
unset MALLOC_CHECK_
unset MALLOC_PERTURB_
%endif

%if %{with lto}
%ifarch aarch64
export LDFLAGS="$LDFLAGS -flto=auto --param ggc-min-expand=20 --param ggc-min-heapsize=32768 --param lto-max-streaming-parallelism=1 -Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
%else
# x64 is fine with the the default settings (the machines have 30GB+ ram)
export LDFLAGS="$LDFLAGS -flto=auto"
%endif
%endif

gn_system_libraries=(
    brotli
    crc32c
    dav1d
    double-conversion
    ffmpeg
    flac
    flatbuffers
    fontconfig
    freetype
    harfbuzz-ng
    highway
    icu
    jsoncpp
    libdrm
    libevent
    libjpeg
    libpng
    libsecret
    libusb
    libwebp
    libXNVCtrl
    libxml
    libxslt
    opus
    snappy
    woff2
    zlib
)

%if %{with system_abseil}
find third_party/abseil-cpp -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=(
   absl_algorithm
   absl_base
   absl_cleanup
   absl_crc
   absl_container
   absl_debugging
   absl_flags
   absl_functional
   absl_hash
   absl_log
   absl_log_internal
   absl_memory
   absl_meta
   absl_numeric
   absl_random
   absl_status
   absl_strings
   absl_synchronization
   absl_time
   absl_types
   absl_utility
)
%endif


%if %{with system_aom}
find third_party/libaom -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( libaom )
%endif

%if %{with system_avif}
find third_party/libavif -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( libavif )
%endif




%if %{with system_minizip}
find third_party/zlib/contrib -type f ! -name "*.gn" -a ! -name "*.gni" -delete
%endif


%if %{with system_re2}
find third_party/re2 -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( re2 )
%endif


%if %{with system_spirv}
find  third_party/swiftshader/third_party/SPIRV-Headers/ -type f ! -name "*.gn" -a ! -name "*.gni"  -delete
find  third_party/swiftshader/third_party/SPIRV-Tools/ -type f ! -name "*.gn" -a ! -name "*.gni"  -delete

find third_party/vulkan-deps/ -type f ! -name "*.gn" -a ! -name "*.gni"  -delete

gn_system_libraries+=(
   swiftshader-SPIRV-Headers
   swiftshader-SPIRV-Tools
#The following can only be unbundled if you don't build DAWN (WebGPU)
   vulkan-SPIRV-Headers
   vulkan-SPIRV-Tools
)
%endif

%if %{with system_vma}
find third_party/vulkan_memory_allocator -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( vulkan_memory_allocator )
%endif

%if %{with system_vpx}
find third_party/libvpx -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( libvpx )
%endif


%if %{with system_yuv}
find third_party/libyuv -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( libyuv )
%endif

build/linux/unbundle/replace_gn_files.py --system-libraries ${gn_system_libraries[@]}

%if %{with link_vulkan}
find third_party/angle/src/third_party/volk -type f ! -name "*.gn" -a ! -name "*.gni"  -delete
%endif

%if %{with system_llhttp}
find third_party/electron_node/deps/llhttp -type f ! -name "*.gn" -a ! -name "*.gni" -a ! -name "*.gyp" -a ! -name "*.gypi" -delete
%endif

%if %{with system_histogram}
find third_party/electron_node/deps/histogram -type f ! -name "*.gn" -a ! -name "*.gni" -a ! -name "*.gyp" -a ! -name "*.gypi" -delete
%endif

%if %{with system_simdutf}
find third_party/electron_node/deps/simdutf -type f ! -name "*.gn" -a ! -name "*.gni" -a ! -name "*.gyp" -a ! -name "*.gypi" -delete
%endif

# Create the configuration for GN
# Available options: out/Release/gn args --list out/Release/
myconf_gn=""
myconf_gn+=' override_electron_version="%{tag_version}"'
myconf_gn+=' electron_vendor_version="suse:Electron for openSUSE"'
myconf_gn+=" custom_toolchain=\"//build/toolchain/linux/unbundle:default\""
myconf_gn+=" host_toolchain=\"//build/toolchain/linux/unbundle:default\""
myconf_gn+=" use_custom_libcxx=false"
%ifarch %ix86
myconf_gn+=" host_cpu=\"x86\""
%endif
%ifarch x86_64 %x86_64
myconf_gn+=" host_cpu=\"x64\""
%endif
%ifarch aarch64
myconf_gn+=" host_cpu=\"arm64\""
#default is "standard" which does not work with gcc
#This does not raise the cpu requirements according to https://developer.arm.com/documentation/101754/0616/armclang-Reference/armclang-Command-line-Options/-mbranch-protection
myconf_gn+=" arm_control_flow_integrity=\"pac\""
%endif
%ifarch %arm
myconf_gn+=" host_cpu=\"arm\""
#openSUSE only supports armhf
%ifarch armv7hl armv7hnl
myconf_gn+=" arm_version=7"
%endif
%ifarch armv6hl
myconf_gn+=" arm_version=6"
%endif
myconf_gn+=" arm_float_abi=\"hard\""
# Disable requirement of neon instructions
%ifarch armv7hnl armv8hnl armv8hcnl
myconf_gn+=" arm_use_neon=true"
%else
myconf_gn+=" arm_use_neon=false"
%endif

%endif #ifarch arm



myconf_gn+=" host_os=\"linux\""
myconf_gn+=" is_debug=false"
myconf_gn+=" dcheck_always_on=false"
myconf_gn+=" enable_nacl=false"
%if %{with swiftshader}
myconf_gn+=" enable_swiftshader=true"
%if %{with subzero}
myconf_gn+=" use_swiftshader_with_subzero=true"
%else
myconf_gn+=" use_swiftshader_with_subzero=false"
%endif
%else
myconf_gn+=" enable_swiftshader=false"
%endif
myconf_gn+=" is_component_ffmpeg=true"
myconf_gn+=" use_cups=false"

# link libvulkan.so and libGLX.so instead of dlopening
myconf_gn+=" angle_use_custom_libvulkan=false"
%if %{with link_vulkan}
myconf_gn+=" angle_shared_libvulkan=false"
%endif
myconf_gn+=" angle_link_glx=true"

#Use faster flat_map instead of fallback std::unordered_map implementation in ANGLE.
#Upstream sets it by default to the value of is_clang with the comment “has trouble supporting MSVC”.
#This is supposed to be enabled in chromium and compiles fine with GCC.
myconf_gn+=' angle_enable_abseil=true'
#this is also mistakenly set to is_clang with the (untrue) comment “macros for determining endian type are currently clang specific”
#in fact, 1° clang copied those macros from gcc and 2° this should be unbundled.
myconf_gn+=' v8_use_libm_trig_functions=true'
#yet another is_clang
myconf_gn+=' rtc_enable_avx2=true'
myconf_gn+=' angle_enable_swiftshader=true'



# do not build PDF support
myconf_gn+=" enable_pdf=false"
myconf_gn+=" enable_pdf_viewer=false"
myconf_gn+=" enable_print_preview=false"
myconf_gn+=" enable_printing=false"
myconf_gn+=" enable_basic_printing=false"
myconf_gn+=' use_cups=false'
myconf_gn+=' enable_print_content_analysis=false'
#we don't build PDF support, so disabling the below:
#myconf_gn+=" use_system_lcms2=true"
#myconf_gn+=" use_system_libopenjpeg2=true"


#do not build chrome pepper plugins support
myconf_gn+=" enable_plugins=false"
myconf_gn+=" enable_ppapi=false"
#it is set by default to enable_ppapi but is required by electron_api_web_frame.cc
myconf_gn+=' content_enable_legacy_ipc=true'

#do not build webextensions support
myconf_gn+=' enable_electron_extensions=false'
myconf_gn+=' enable_extensions_legacy_ipc=false'

# The option below get overriden by whatever is in CFLAGS/CXXFLAGS, so they affect only C++ code.
# symbol_level=2 is full debug
# symbol_level=1 is enough info for stacktraces
# symbol_level=0 no debuginfo (only function names in private symbols)
# blink (HTML engine) and v8 (js engine) are template-heavy, trying to compile them with full debug leads to linker errors due to inherent limitations of the DWARF format.
%ifnarch %ix86 %arm aarch64
myconf_gn+=' symbol_level=2'
myconf_gn+=' blink_symbol_level=1'
myconf_gn+=' v8_symbol_level=1'
%endif
%ifarch %ix86 %arm
#Sorry, no debug on 32bit.
myconf_gn+=" symbol_level=1"
myconf_gn+=" blink_symbol_level=0"
myconf_gn+=" v8_symbol_level=0"
%endif
%ifarch aarch64
# linker OOM, sorry.
# we still seem to get some debug generated during linking when LTO is enabled
myconf_gn+=' symbol_level=0'
myconf_gn+=' blink_symbol_level=0'
myconf_gn+=' v8_symbol_level=0'
%endif


# do not build some chrome features not used by electron
# (some of these only go to buildflag_headers and are dead code rn, but disabling them preemptively as long as they're visible)
myconf_gn+=" enable_vr=false"
myconf_gn+=" enable_reading_list=false"
myconf_gn+=" enable_reporting=false"
myconf_gn+=" build_with_tflite_lib=false"
myconf_gn+=" build_tflite_with_xnnpack=false"
myconf_gn+=" build_webnn_with_xnnpack=false"
myconf_gn+=" safe_browsing_mode=0"
myconf_gn+=" enable_maldoca=false"
myconf_gn+=" enable_captive_portal_detection=false"
myconf_gn+=" enable_browser_speech_service=false"
myconf_gn+=" enable_speech_service=false"
myconf_gn+=" enable_screen_ai_service=false"
myconf_gn+=" include_transport_security_state_preload_list=false"
myconf_gn+=" enable_web_speech=false"
myconf_gn+=" chrome_wide_echo_cancellation_supported=false"
myconf_gn+=" enable_downgrade_processing=false"
myconf_gn+=" enable_click_to_call=false"
myconf_gn+=" enable_webui_tab_strip=false"
myconf_gn+=" enable_webui_certificate_viewer=false"
myconf_gn+=" enable_background_contents=false"
myconf_gn+=" enable_extractors=false"
myconf_gn+=" enable_feed_v2=false"
myconf_gn+=" ozone_platform_headless=false"
myconf_gn+=" angle_enable_gl_null=false"
myconf_gn+=" enable_paint_preview=false"
myconf_gn+=" use_bundled_weston=false"
myconf_gn+=" enable_component_updater=false"
myconf_gn+=" enable_lens_desktop=false"
myconf_gn+=' enable_bound_session_credentials=false'
myconf_gn+=' enable_chrome_notifications=false'
myconf_gn+=' enable_message_center=false'
myconf_gn+=' enable_system_notifications=false'
myconf_gn+=' enable_supervised_users=false'
myconf_gn+=' enable_compose=false'
myconf_gn+=' enterprise_cloud_content_analysis=false'
myconf_gn+=' enterprise_local_content_analysis=false'
myconf_gn+=' enterprise_data_controls=false'
myconf_gn+=' enterprise_client_certificates=false'
myconf_gn+=' enterprise_watermark=false'
myconf_gn+=' enterprise_content_analysis=false'


#FIXME: possibly enable this when skia gets built with rust code by default.
#Need to patch in optflags and possibly FFI LTO hacks (see signal-desktop package for how it's done)
myconf_gn+=' enable_rust=false'
myconf_gn+=' enable_chromium_prelude=false'

#See net/base/features.cc. It's not enabled yet.
#FIXME: enable this and add shims to build with system zstd when it's enabled
myconf_gn+=' disable_zstd_filter=true'

myconf_gn+=' chrome_certificate_policies_supported=false'
myconf_gn+=' use_kerberos=false'

myconf_gn+=' disable_histogram_support=true'



#Do not build Chromecast
myconf_gn+=" enable_remoting=false"
myconf_gn+=" enable_media_remoting=false"
myconf_gn+=" enable_service_discovery=false"

#disable some debug/tracing hooks, they increase size and we do not build chrome://tracing anyway (see disable-catapult.patch)
myconf_gn+=" enable_trace_logging=false"
myconf_gn+=" optional_trace_events_enabled=false"
myconf_gn+=" rtc_disable_logging=true"
myconf_gn+=" rtc_disable_metrics=true"
myconf_gn+=" rtc_disable_trace_events=true"
myconf_gn+=' enable_perfetto_system_consumer=false'
myconf_gn+=' enable_perfetto_trace_processor_json=false'
myconf_gn+=' enable_perfetto_trace_processor_httpd=false'
myconf_gn+=' enable_perfetto_zlib=false'



myconf_gn+=' dawn_complete_static_libs=true'
myconf_gn+=" enable_library_cdms=false"
myconf_gn+=" use_pulseaudio=true link_pulseaudio=true"
myconf_gn+=" is_component_build=false"
myconf_gn+=" use_sysroot=false"
myconf_gn+=" fatal_linker_warnings=false"



myconf_gn+=" disable_fieldtrial_testing_config=true"
myconf_gn+=" use_unofficial_version_number=false"
myconf_gn+=" use_lld=false"

%if %{with vaapi}
myconf_gn+=' use_vaapi=true use_vaapi_image_codecs=true'
%else
myconf_gn+=' use_vaapi=false use_vaapi_image_codecs=false'
%endif

%if %{with v4l2}
myconf_gn+=' use_v4l2_codec=true'
%else
myconf_gn+=' use_v4l2_codec=false'
%endif

myconf_gn+=" treat_warnings_as_errors=false"
myconf_gn+=" use_dbus=true"
myconf_gn+=" enable_vulkan=true"
myconf_gn+=" icu_use_data_file=false"
myconf_gn+=" media_use_openh264=false"
myconf_gn+=" rtc_use_h264=false"
myconf_gn+=" use_v8_context_snapshot=true"
myconf_gn+=" v8_use_external_startup_data=true"
myconf_gn+=" use_system_zlib=true"
myconf_gn+=" use_system_libjpeg=true"
myconf_gn+=" use_system_libpng=true"

#we don't build PDF support, so disabling the below:
#myconf_gn+=" use_system_lcms2=true"
#myconf_gn+=" use_system_libopenjpeg2=true"

myconf_gn+=" use_system_harfbuzz=true"
myconf_gn+=" use_system_freetype=true"
myconf_gn+=" use_system_cares=true"
myconf_gn+=" use_system_nghttp2=true"
%if %{with system_llhttp}
myconf_gn+=" use_system_llhttp=true"
%endif
%if %{with system_histogram}
myconf_gn+=" use_system_histogram=true"
%endif
%if %{with system_simdutf}
myconf_gn+=' use_system_simdutf=true'
%endif
myconf_gn+=" is_clang=false"
myconf_gn+=" use_gold=false"

%if %{with lto}
myconf_gn+=" gcc_lto=true"
# endif with lto
%endif


%if %{with pipewire}
myconf_gn+=" rtc_use_pipewire=true rtc_link_pipewire=true"
%endif

%if %{with qt}
myconf_gn+=' use_qt=true'
myconf_gn+=' moc_qt5_path="%{_libdir}/qt5/bin/"'
myconf_gn+=' use_qt6=true'
myconf_gn+=' moc_qt6_path="%{_qt6_libexecdir}"'
%endif


# Do not build WebGPU support. It is huge and not used by ANY known apps (we would know if it was — it's hidden behind an experimental flag).
myconf_gn+=" use_dawn=false"
myconf_gn+=' skia_use_dawn=false'

# The proprietary codecs just force the chromium to say they can use it and
# offload the actual computation to the ffmpeg, otherwise the chromium
# won't be able to load the codec even if the library can handle it
myconf_gn+=" proprietary_codecs=true"
myconf_gn+=" ffmpeg_branding=\"Chrome\""

# GN does not support passing cflags:
#  https://bugs.chromium.org/p/chromium/issues/detail?id=642016
gn gen out/Release --testonly=false --args="import(\"//electron/build/args/release.gn\") ${myconf_gn}"


# dump the linker command line (if any) in case of failure
ninja -v %{?_smp_mflags} -C out/Release chromium_licenses copy_node_headers version electron || (cat out/Release/*.rsp | sed 's/ /\n/g' && false)



%install
install -d -m 0755 %{buildroot}%{_bindir}
install -d -m 0755 %{buildroot}%{_includedir}/electron
install -d -m 0755 %{buildroot}%{_libdir}/electron
install -d -m 0755 %{buildroot}%{_datadir}/applications
install -d -m 0755 %{buildroot}%{_datadir}/pixmaps/
install -d -m 0755 %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/

install -pm 0755 %{SOURCE10} %{buildroot}%{_bindir}/%{mod_name}
sed -i 's[XXXLIBDIRXXX[%{_libdir}[g' %{buildroot}%{_bindir}/%{mod_name}
install -pvDm644 electron/default_app/icon.png %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/%{mod_name}.png

install -pvDm644 electron/shell/browser/resources/win/extracted-0.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{mod_name}.png
install -pvDm644 electron/shell/browser/resources/win/extracted-1.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{mod_name}.png
install -pvDm644 electron/shell/browser/resources/win/extracted-2.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{mod_name}.png
install -pvDm644 electron/shell/browser/resources/win/extracted-3.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{mod_name}.png


desktop-file-install --dir %{buildroot}%{_datadir}/applications/ %{SOURCE11}

pushd out/Release
install -pm 0644 version                 -t %{buildroot}%{_libdir}/electron/

gn desc . //electron:electron_app runtime_deps | grep -v ^gen/ | sort | uniq | xargs -t cp -l -v --parents -t %{buildroot}%{_libdir}/electron/ --


popd





cp -lrvT out/Release/gen/node_headers/include/node %{buildroot}%{_includedir}/electron

# Electron has a little known feature that make it work like a nodejs binary.
# We make use of it in the %%electron_rebuild macro which builds all dependencies in node_modules against Electron's headers.
# Not all scripts work when run under electron,
# but importantly npm/yarn and GYP do.
mkdir -pv %{buildroot}%{_libexecdir}/electron-node


cat <<EOF > %{buildroot}%{_libexecdir}/electron-node/node
#!/bin/sh
ELECTRON_RUN_AS_NODE=1 exec %{_libdir}/electron/electron "\$@"
EOF

# HACK: This will refer to /usr/bin/npm17 on openSUSE, /usr/bin/npm on Fedora which are Node scripts
cat <<EOF >%{buildroot}%{_libexecdir}/electron-node/npm
#!/bin/sh
exec %{_libexecdir}/electron-node/node %{_bindir}/npm%{NODEJS_DEFAULT_VER} "\$@"
EOF

cat <<EOF > %{buildroot}%{_libexecdir}/electron-node/npx
#!/bin/sh
exec %{_libexecdir}/electron-node/node %{_bindir}/npx%{NODEJS_DEFAULT_VER} "\$@"
EOF

# On Fedora, /usr/bin/yarn is a node script which means it needs to be wrapped too. On openSUSE, it is a shell script.
%if 0%{?fedora}
cat <<EOF > %{buildroot}%{_libexecdir}/electron-node/yarn
#!/bin/sh
exec %{_libexecdir}/electron-node/node %{_bindir}/yarn "\$@"
EOF
%endif
chmod -v 0755 %{buildroot}%{_libexecdir}/electron-node/*

# Install electron.macros
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
cp /dev/stdin %{buildroot}%{_rpmconfigdir}/macros.d/macros.electron <<"EOF"
# Ensure rebuilds when electron major changes.
%%electron_req Requires: electron%{_isa}(abi) = %{abi_version}

# Build native modules against Electron. This should be done as the first step in ‰build. You must set CFLAGS/LDFLAGS previously.
# You can call it multiple times in different directories and pass more parameters to it (seen in vscode)
%%electron_rebuild PATH="%{_libexecdir}/electron-node:$PATH" npm rebuild --verbose --foreground-scripts --nodedir=%{_includedir}/electron

# Sanity check that native modules load. You must include this in ‰check if the package includes native modules (possibly in addition to actual test suites)
# These do, in order:
# 1. Detect underlinking (missing dependencies)
# 2. Detect accidental linking to libuv which must not be used (Electron exports its own incompatible version)
# 3. Actually load each module

# This one should be paired with a simple `Requires: nodejs-electron%{_isa}` in requirements.
%%electron_check_native \
  find '%%{buildroot}' -type f -name '*.node' -print0 | xargs -0 -t -IXXX sh -c '! ldd -d -r XXX | \\\
    grep    '\\''^undefined symbol'\\'' | \\\
    grep -v '\\''^undefined symbol: napi_'\\'' | \\\
    grep -v '\\''^undefined symbol: uv_'\\'' ' \
  find '%%{buildroot}' -type f -name '*.node' -print0 | xargs -0 -t -IXXX sh -c '! objdump -p XXX | grep -F libuv.so.1' \
  find '%%{buildroot}' -type f -name '*.node' -print0 | xargs -0 -t -IXXX env ELECTRON_RUN_AS_NODE=1 %{_libdir}/electron/electron -e 'require("XXX")'

# This one allows use of unstable APIs and should be paired with the `‰electron_req` macro in requirements.
%%electron_check_native_unstable \
  find '%%{buildroot}' -type f -name '*.node' -print0 | xargs -0 -t -IXXX sh -c '! ldd -d -r XXX | \\\
    grep    '\\''^undefined symbol'\\'' | \\\
    grep -v '\\''^undefined symbol: node_'\\'' | \\\
    grep -v '\\''^undefined symbol: _ZN12v8_inspector'\\'' | \\\
    grep -v '\\''^undefined symbol: _ZN2v8'\\'' | \\\
    grep -v '\\''^undefined symbol: _ZN4node'\\'' | \\\
    grep -v '\\''^undefined symbol: _ZN5cppgc'\\'' | \\\
    grep -v '\\''^undefined symbol: _ZN8electron'\\'' | \\\
    grep -v '\\''^undefined symbol: _ZNK12v8_inspector'\\'' | \\\
    grep -v '\\''^undefined symbol: _ZNK2v8'\\'' | \\\
    grep -v '\\''^undefined symbol: _ZNK4node'\\'' | \\\
    grep -v '\\''^undefined symbol: _ZNK5cppgc'\\'' | \\\
    grep -v '\\''^undefined symbol: napi_'\\'' | \\\
    grep -v '\\''^undefined symbol: uv_'\\'' ' \
  find '%%{buildroot}' -type f -name '*.node' -print0 | xargs -0 -t -IXXX sh -c '! objdump -p XXX | grep -F libuv.so.1' \
  find '%%{buildroot}' -type f -name '*.node' -print0 | xargs -0 -t -IXXX env ELECTRON_RUN_AS_NODE=1 %{_libdir}/electron/electron -e 'require("XXX")'


EOF
chmod -v 644 %{buildroot}%{_rpmconfigdir}/macros.d/macros.electron

#help debugedit find the source files
ln -srv third_party/emoji-segmenter/src/emoji_presentation_scanner.c -t out/Release
ln -srv third_party/emoji-segmenter/src/emoji_presentation_scanner.rl -t out/Release
ln -srv third_party/angle/src/compiler/translator/glslang.l -t out/Release
ln -srv third_party/angle/src/compiler/preprocessor/preprocessor.l -t out/Release
ln -srv third_party -t out/Release

%files
%license electron/LICENSE out/Release/LICENSES.chromium.html
%{_bindir}/electron
%{_datadir}/applications/electron.desktop
%{_datadir}/icons/hicolor/16x16/apps/electron.png
%{_datadir}/icons/hicolor/32x32/apps/electron.png
%{_datadir}/icons/hicolor/48x48/apps/electron.png
%{_datadir}/icons/hicolor/256x256/apps/electron.png
%{_datadir}/icons/hicolor/1024x1024

%dir %{_libdir}/electron/
%{_libdir}/electron/chrome_100_percent.pak
%{_libdir}/electron/chrome_200_percent.pak
%{_libdir}/electron/chrome_crashpad_handler
%{_libdir}/electron/electron
%{_libdir}/electron/libEGL.so
%{_libdir}/electron/libGLESv2.so
%{_libdir}/electron/libvk_swiftshader.so
%{_libdir}/electron/resources.pak
%{_libdir}/electron/snapshot_blob.bin
%{_libdir}/electron/v8_context_snapshot.bin
%{_libdir}/electron/version
%{_libdir}/electron/vk_swiftshader_icd.json
%dir %{_libdir}/electron/locales
%{_libdir}/electron/locales/*.pak
%dir %{_libdir}/electron/resources
%{_libdir}/electron/resources/default_app.asar



%files devel
%{_includedir}/electron
%{_rpmconfigdir}/macros.d/macros.electron
%dir %{_libexecdir}/electron-node
%{_libexecdir}/electron-node/node
%{_libexecdir}/electron-node/npm
%{_libexecdir}/electron-node/npx
%if 0%{?fedora}
%{_libexecdir}/electron-node/yarn
%endif

%files doc
%doc electron/README.md
%doc electron/docs

%if %{with qt}
%files qt5
%{_libdir}/electron/libqt5_shim.so
%files qt6
%{_libdir}/electron/libqt6_shim.so
%endif

%changelog
