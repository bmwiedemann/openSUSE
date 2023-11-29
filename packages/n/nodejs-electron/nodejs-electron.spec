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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# https://fedoraproject.org/wiki/Changes/SetBuildFlagsBuildCheck
%undefine _auto_set_build_flags

%define mod_name electron
# https://github.com/nodejs/node/blob/main/doc/abi_version_registry.json
%define abi_version 118

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

#the QT ui is currently borderline unusable (too small fonts in menu and wrong colors)
%bcond_with qt

%bcond_with vaapi





%bcond_with clang



%if %{with clang}
%global toolchain clang
%else

# Linker selection. GCC only. Default is BFD.
# You can try different ones if it has problems.
# arm64 reports relocation errors with BFD.
# obj/third_party/electron_node/deps/uv/uv/threadpool.o: in function `init_once':
# /home/abuild/rpmbuild/BUILD/src/out/Release/../../third_party/electron_node/deps/uv/src/threadpool.c:254:(.text+0x2bc): relocation truncated to fit: R_AARCH64_CALL26 against symbol `pthread_atfork' defined in .text section in /usr/lib64/libc_nonshared.a(pthread_atfork.oS)
# obj/third_party/electron_node/node_lib/embed_helpers.o: in function `std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > node::SPrintFImpl<char const*>(char const*, char const*&&)':
# /home/abuild/rpmbuild/BUILD/src/out/Release/../../third_party/electron_node/src/debug_utils-inl.h:76:(.text.unlikely._ZN4node11SPrintFImplIPKcJEEENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES2_OT_DpOT0_[_ZN4node11SPrintFImplIPKcJEEENSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEES2_OT_DpOT0_]+0x50): relocation truncated to fit: R_AARCH64_CALL26 against symbol `node::Assert(node::AssertionInfo const&)' defined in .text section in obj/third_party/electron_node/node_lib/node_errors.o

%if 0%{?suse_version}
%ifarch aarch64
%bcond_without gold
%else
%bcond_with gold
%endif
%else
%bcond_with gold
%endif

%endif #with clang

#Mold succeeds on ix86 but seems to produce corrupt binaries (no build-id)
%bcond_with mold

%ifnarch %ix86 %arm aarch64
# OBS does not have enough powerful machines to build with LTO on aarch64.

%if (0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700 || 0%{?fedora})
%bcond_without lto
%else
%bcond_with lto
%endif

%else
%bcond_with lto
%endif


%bcond_without system_nghttp2


%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700
%bcond_without system_avif
%else
%bcond_with system_avif
%endif


%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500 || 0%{?fedora}
%bcond_without system_crc32c
%bcond_without system_dav1d
%bcond_without system_highway
%bcond_without system_nvctrl
%else
%bcond_with system_crc32c
%bcond_with system_dav1d
%bcond_with system_highway
%bcond_with system_nvctrl
%endif


%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700 || 0%{?fedora}
%bcond_without harfbuzz_5
%bcond_without link_vulkan
%bcond_without ffmpeg_5
%bcond_without system_spirv
%else
%bcond_with harfbuzz_5
%bcond_with link_vulkan
%bcond_with ffmpeg_5
%bcond_with system_spirv
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700 || 0%{?fedora} >= 38
%bcond_without system_aom
%bcond_without system_vpx
%else
%bcond_with system_aom
%bcond_with system_vpx
%endif

%if 0%{?suse_version} || 0%{?fedora} >= 39
%bcond_without icu_73
%else
%bcond_with icu_73
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150600
%bcond_without system_yuv
%else
%bcond_with system_yuv
%endif


%if 0%{?fedora}
%bcond_without system_llhttp
%bcond_without llhttp_8
%bcond_without system_histogram
%else
%bcond_with system_llhttp
%bcond_with llhttp_8
%bcond_with system_histogram
%endif

%if 0%{?fedora} >= 38
%bcond_without system_simdutf
%else
%bcond_with system_simdutf
%endif

%if 0%{?fedora} >= 40
%bcond_without system_vma
%else
%bcond_with system_vma
%endif


# Abseil is broken in Leap
# enable this when boo#1203378 and boo#1203379 get fixed
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700 || 0%{?fedora} >= 37
%bcond_without system_abseil

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700 || 0%{?fedora} >= 39
%bcond_without abseil_2023
%else
%bcond_with abseil_2023
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700
%bcond_without re2_11
%else
%bcond_with re2_11
%endif

%else
%bcond_with system_abseil
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
%if 0%{?fedora} >= 37 && 0%{?fedora} < 38
%define AVFORMAT_VER 5.1.4
%define RPMFUSION_VER 5.1.4-1
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
Version:        27.1.2
Release:        0
Summary:        Build cross platform desktop apps with JavaScript, HTML, and CSS
License:        AFL-2.0 AND Apache-2.0 AND blessing AND BSD-2-Clause AND BSD-3-Clause AND BSD-Protection AND BSD-Source-Code AND bzip2-1.0.6 AND IJG AND ISC AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND MIT-CMU AND MIT-open-group AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later) AND MPL-2.0 AND OpenSSL AND SGI-B-2.0 AND SUSE-Public-Domain AND X11
Group:          Development/Languages/NodeJS
URL:            https://github.com/electron/electron
Source0:        %{mod_name}-%{version}.tar.zst
Source1:        create_tarball.sh
Source10:       electron-launcher.sh
Source11:       electron.desktop
# Shim generators for unbundling libraries
Source50:       flatbuffers.gn
Source51:       libsecret.gn
Source52:       highway.gn
Source53:       vulkan_memory_allocator.gn


# Reverse upstream changes to be able to build against ffmpeg-4
Source400:      ffmpeg-new-channel-layout.patch
Source401:      audio_file_reader-ffmpeg-AVFrame-duration.patch
# and against harfbuzz 4
Source415:      harfbuzz-replace-chromium-scoped-type.patch
Source416:      harfbuzz-replace-HbScopedPointer.patch
# and icu 71
Source417:      v8-icu73-alt_calendar.patch
Source418:      v8-icu73-simple-case-folding.patch
# and re2 10
Source430:      replace-StringPiece-with-string_view.patch


# PATCHES for openSUSE-specific things
Patch0:         chromium-102-compiler.patch
Patch1:         fpic.patch
Patch3:         gcc-enable-lto.patch
Patch6:         chromium-vaapi.patch
Patch7:         chromium-91-java-only-allowed-in-android-builds.patch
# Always disable use_thin_lto which is an lld feature
Patch21:        electron-13-fix-use-thin-lto.patch
# Fix common.gypi to include /usr/include/electron
Patch25:        electron-16-system-node-headers.patch
# https://sources.debian.org/patches/chromium/102.0.5005.115-1/debianization/support-i386.patch/
Patch39:        support-i386.patch
# from https://sources.debian.org/patches/chromium/103.0.5060.53-1/disable/catapult.patch/
Patch67:        disable-catapult.patch
Patch69:        nasm-generate-debuginfo.patch
Patch70:        disable-fuses.patch
# https://code.qt.io/cgit/qt/qtwebengine-chromium.git/commit/?h=102-based&id=d617766b236a93749ddbb50b75573dd35238ffc9
Patch73:        disable-webspeech.patch
Patch74:        common.gypi-remove-fno-omit-frame-pointer.patch
Patch75:        gcc-asmflags.patch
# https://sources.debian.org/patches/chromium/108.0.5359.124-1/disable/tests.patch/
Patch76:        disable-devtools-tests.patch
Patch77:        angle_link_glx.patch
Patch78:        rdynamic.patch
Patch79:        v8-hide-private-symbols.patch
Patch80:        icon.patch
Patch81:        disable-tests.patch

# PATCHES to use system libs
Patch1000:      do-not-build-libvulkan.so.patch
Patch1002:      chromium-system-libusb.patch
Patch1017:      system-libdrm.patch
# http://svnweb.mageia.org/packages/updates/7/chromium-browser-stable/current/SOURCES/chromium-74-pdfium-system-libopenjpeg2.patch?view=markup
Patch1038:      pdfium-fix-system-libs.patch
# https://sources.debian.org/patches/chromium/102.0.5005.115-1/system/zlib.patch/
Patch1041:      system-zlib.patch
Patch1044:      replace_gn_files-system-libs.patch
Patch1045:      angle-system-xxhash.patch
Patch1047:      cares_public_headers.patch
Patch1048:      chromium-remove-bundled-roboto-font.patch
Patch1053:      swiftshader-use-system-llvm.patch
Patch1054:      thread_annotations-fix-build-with-system-abseil.patch
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
# adjust to llhttp 8 api changes
%if %{with llhttp_8}
Patch2033:       node-upgrade-llhttp-to-8.patch
%else
Source2033:      node-upgrade-llhttp-to-8.patch
%endif
Patch2034:      swiftshader-LLVMJIT-AddressSanitizerPass-dead-code-remove.patch
Patch2035:      RenderFrameHostImpl-use-after-free.patch
Patch2037:      abseil-remove-unused-targets.patch
Patch2039:      vulkan_memory_allocator-upgrade.patch
# https://github.com/electron/electron/pull/40032
Patch2040:      build-without-extensions.patch
Patch2041:      chromium-117-blink-BUILD-mnemonic.patch
Patch2042:      brotli-remove-shared-dictionary.patch
Patch2043:      keyboard_util-gcc12-invalid-constexpr.patch
Patch2044:      computed_style_base-nbsp.patch
Patch2045:      libxml-2.12-xmlCtxtGetLastError-const.patch

# PATCHES that should be submitted upstream verbatim or near-verbatim
Patch3016:      chromium-98-EnumTable-crash.patch
# Fix blink nodestructor
Patch3023:      electron-13-blink-gcc-ambiguous-nodestructor.patch
Patch3027:      electron-16-freetype-visibility-list.patch
Patch3028:      electron-16-third_party-symbolize-missing-include.patch
# From https://git.droidware.info/wchen342/ungoogled-chromium-fedora
Patch3033:      chromium-94.0.4606.71-InkDropHost-crash.patch
Patch3056:      async_shared_storage_database_impl-missing-absl-WrapUnique.patch
# https://salsa.debian.org/chromium-team/chromium/-/blob/456851fc808b2a5b5c762921699994e957645917/debian/patches/upstream/nested-nested-nested-nested-nested-nested-regex-patterns.patch
Patch3064:      nested-nested-nested-nested-nested-nested-regex-patterns.patch
Patch3080:      compact_enc_det_generated_tables-Wnarrowing.patch
Patch3096:      remove-date-reproducible-builds.patch
Patch3106:      vulkan_memory_allocator-vk_mem_alloc-missing-snprintf.patch
Patch3121:      services-network-optional-explicit-constructor.patch
# https://src.fedoraproject.org/rpms/qt6-qtwebengine/blob/rawhide/f/Partial-migration-from-imp-to-importlib.patch
Patch3203:      Partial-migration-from-imp-to-importlib.patch
Patch3208:      mojo_ukm_recorder-missing-WrapUnique.patch
Patch3209:      electron_browser_context-missing-variant.patch
Patch3210:      electron_api_app-GetPathConstant-non-constexpr.patch
Patch3213:      CVE-2023-38552-node-integrity-checks-according-to-policies.patch
Patch3214:      CVE-2023-39333-node-create_dynamic_module-code-injection.patch
Patch3215:      CVE-2023-45143-undici-cookie-leakage.patch
Patch3216:      partition_root-attribute.patch
Patch3217:      sensor_reading-missing-int64_t-size_t.patch
Patch3218:      material_color_utilities-tones-missing-round.patch
Patch3219:      utf_string_conversion_utils-missing-numeric_limits.patch
Patch3220:      kwallet_dbus-missing-uint8_t.patch
Patch3221:      page_content_annotations_common-remove-tflite.patch
Patch3222:      decoder_buffer_side_data-missing-uint8_t.patch
Patch3223:      absl-make_unique-missing-include.patch
Patch3224:      autofill_i18n_parsing_expressions-constexpr.patch
Patch3225:      simple_font_data-freetype-include.patch
Patch3226:      perfetto-numeric_storage-double_t.patch
Patch3227:      policy_templates-deterministic.patch


%if %{with clang}
BuildRequires:  clang
BuildRequires:  lld
BuildRequires:  llvm
%if 0%{?suse_version} && 0%{?suse_version} < 1550
BuildRequires:  gcc11
BuildRequires:  libstdc++6-devel-gcc11
%endif
%endif
%if %{with gold}
BuildRequires:  binutils-gold
%endif
BuildRequires:  brotli
%if %{with system_cares}
BuildRequires:  c-ares-devel
%endif
%if %{with system_crc32c}
BuildRequires:  cmake(Crc32c)
%endif
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
%if %{with system_nvctrl}
BuildRequires:  libXNVCtrl-devel
%endif
%if %{with system_llhttp}
%if %{with llhttp_8}
BuildRequires:  llhttp-devel >= 8
%else
BuildRequires:  llhttp-devel < 8
%endif
%endif
%if %{with lld}
BuildRequires:  lld
%endif
%if %{with swiftshader} && %{without subzero}
BuildRequires:  llvm-devel >= 16
%endif
BuildRequires:  memory-constraints
%if %{with mold}
BuildRequires:  mold
%endif
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
BuildRequires:  pkgconfig
BuildRequires:  plasma-wayland-protocols
BuildRequires:  python3-json5
BuildRequires:  python%{PYVER}-jinja2 >= 3.0.2
BuildRequires:  python3-mako
BuildRequires:  python3-ply
BuildRequires:  python%{PYVER}-PyYAML >= 6
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
%if %{with abseil_2023}
BuildRequires:  pkgconfig(absl_core_headers) >= 20230000
%endif
%endif
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo) >= 1.6
%if %{with system_dav1d}
BuildRequires:  pkgconfig(dav1d) >= 1
%endif
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
BuildRequires:  pkgconfig(icu-i18n) >= 71
%if %{with icu_73}
BuildRequires:  pkgconfig(icu-i18n) >= 73
%else
BuildRequires:  pkgconfig(icu-i18n) >= 71
%endif
BuildRequires:  pkgconfig(jsoncpp)
%if 0%{?fedora}
Recommends: (ffmpeg-libs%{_isa} or libavcodec-freeworld%{_isa})
%endif
%if %{with ffmpeg_5}
BuildRequires:  pkgconfig(libavcodec) >= 59
BuildRequires:  pkgconfig(libavformat) >= 59
BuildRequires:  pkgconfig(libavutil) >= 57
%if 0%{?fedora}
#requires av_stream_get_first_dts, see rhbz#2240127
BuildRequires:  libavformat-free-devel >= %AVFORMAT_VER
Requires: (ffmpeg-libs%{_isa} >= %RPMFUSION_VER or libavformat-free%{_isa} >= %AVFORMAT_VER)
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
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevent)
%if %{with system_highway}
BuildRequires:  pkgconfig(libhwy) >= 1
%endif
%if 0%{?fedora} >= 38
#Work around https://bugzilla.redhat.com/show_bug.cgi?id=2148612
BuildRequires:  pkgconfig(libmd)
%endif
%if %{with system_nghttp2}
BuildRequires:  pkgconfig(libnghttp2)
%endif
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
%if 0%{?fedora}
BuildRequires:  minizip-compat-devel
%else
BuildRequires:  pkgconfig(minizip)
%endif
BuildRequires:  pkgconfig(nspr) >= 4.9.5
BuildRequires:  pkgconfig(nss) >= 3.26
BuildRequires:  pkgconfig(opus) >= 1.3.1
BuildRequires:  pkgconfig(pangocairo)
%if %{with qt}
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
%endif
BuildRequires:  pkgconfig(re2)
%if %{without system_abseil}
#re2-11 has abseil as a public dependency. The headers collide with the bundled ones, causing linker errors.
BuildRequires:  cmake(re2) < 11
%endif
%if %{with system_abseil} && %{with re2_11}
BuildRequires:  cmake(re2) >= 11
%endif
%if %{with system_spirv}
%if 0%{?suse_version}
BuildRequires:  spirv-headers
%else
BuildRequires:  spirv-headers-devel
%endif
BuildRequires:  pkgconfig(SPIRV-Tools) >= 2022.2
%endif
%if %{with link_vulkan}
BuildRequires:  pkgconfig(vulkan) >= 1.3
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
%if %{without clang}
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700 || 0%{?fedora}
BuildRequires:  gcc >= 12
BuildRequires:  gcc-c++ >= 12
%else
BuildRequires:  gcc12-PIE
BuildRequires:  gcc12-c++
%endif
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

Provides:       electron
Provides:       electron%{_isa}(abi) = %{abi_version}

Obsoletes:      nodejs-electron-prebuilt < %{version}
Provides:       nodejs-electron-prebuilt = %{version}

%description
Nodejs application: Build cross platform desktop apps with JavaScript, HTML, and CSS

%package devel
Summary:        Electron development headers
Group:          Development/Libraries/C and C++
Requires:       nodejs-electron%{?_isa} = %{version}
Requires:       pkgconfig(zlib)


%description devel
Development headers for Electron projects.

%package doc
Summary:        Electron API documentation
Group:          Documentation/Other
Enhances:       nodejs-electron-devel = %{version}
BuildArch:      noarch


%description doc
Development documentation for the Electron runtime.

%prep
%if %{with clang}
clang -v
%endif

# Use stable path to source to make use of ccache
%autosetup -n src -p1


# Sanity check if macro corresponds to the actual ABI
test $(grep ^node_module_version electron/build/args/all.gn | sed 's/.* = //') = %abi_version

%if %{without system_abseil}
patch -R -p1 < %PATCH1054
patch -R -p1 < %PATCH1076
%endif

%if %{with system_abseil} && %{with abseil_2023}
patch -R -p1 < %PATCH1054
%endif

%if %{with ffmpeg_5}
patch -R -p1 < %PATCH2012
%else
patch -R -p1 < %SOURCE400
%endif



%if %{without system_vma}
patch -R -p1 < %PATCH2039
%endif

%if %{without harfbuzz_5}
patch -R -p1 < %SOURCE415
patch -R -p1 < %SOURCE416
%endif

%if %{without icu_73}
patch -R -p1 < %SOURCE417
patch -R -p1 < %SOURCE418
%endif


# This one depends on an ffmpeg nightly, reverting unconditionally.
patch -R -p1 < %SOURCE401

%if %{without system_abseil} || (%{with system_abseil} || %{without re2_11})
patch -R -p1 < %SOURCE430
%endif

# Link system wayland-protocols-devel into where chrome expects them
mkdir -p third_party/wayland/src
mkdir -p third_party/wayland-protocols/kde/src
ln -svfT %{_datadir}/wayland third_party/wayland/src/protocol
#mkdir -p third_party/wayland-protocols/mesa

#ln -svfT %{_datadir}/wayland-protocols third_party/wayland-protocols/src
#ln -svfT %{_datadir}/wayland-eglstream third_party/wayland-protocols/mesa/wayland-drm
ln -svfT %{_datadir}/plasma-wayland-protocols third_party/wayland-protocols/kde/src/protocols

# Shim generators for replace_gn_files.py
cp -lv %{_sourcedir}/*.gn build/linux/unbundle/

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
cp -pr %{python3_sitelib}/{json5,mako,ply} -t "$(pwd)/python3-site"
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

%if %{with clang}
#RPM debugedit cannot handle clang's default dwarf-5
ARCH_FLAGS="$ARCH_FLAGS -fdebug-default-version=4"
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
%if %{without lld} && %{without gold}
export LDFLAGS="$LDFLAGS -Wl,--gc-keep-exported"
%endif


%if %{with clang}


export CC=clang
export CXX=clang++
export AR=llvm-ar
export NM=llvm-nm
export RANLIB=llvm-ranlib

# else with clang
%else


%ifarch %ix86 %arm
#try to reduce memory
%if %{without lld} && %{without mold}

%if %{with gold}
export LDFLAGS="${LDFLAGS} -Wl,--no-map-whole-files -Wl,--no-keep-memory -Wl,--no-keep-files-mapped"
%else
export LDFLAGS="${LDFLAGS} -Wl,--no-keep-memory"
%endif

%endif #without lld
%endif #ifarch ix86 arm


%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700 || 0%{?fedora}
export CC=gcc
export CXX=g++
export AR=gcc-ar
export NM=gcc-nm
export RANLIB=gcc-ranlib
%else
export CC=gcc-12
export CXX=g++-12
export AR=gcc-ar-12
export NM=gcc-nm-12
export RANLIB=gcc-ranlib-12
%endif

# endif with clang
%endif


%if %{with lld}
export LDFLAGS="${LDFLAGS} -Wl,--as-needed -fuse-ld=lld"
%endif
%if %{with mold}
export LDFLAGS="${LDFLAGS} -Wl,--as-needed -fuse-ld=mold"
%endif

# do not eat all memory
%ifarch %ix86 %arm
%limit_build -m 1200
%else
%limit_build -m 3500
%endif


%if %{with lto} && %{without clang}
%ifarch aarch64
# reduce the threads for linking even more due to LTO eating ton of memory
# [This is not used currently — these settings still get us OOM on 20GB memory]
_link_threads=$(((%{jobs} - 6)))

test "$_link_threads" -le 0 && _link_threads=1
export LDFLAGS="$LDFLAGS -flto=$_link_threads --param lto-max-streaming-parallelism=1 -Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
%else
# x64 is fine with the the default settings (the machines have 30GB+ ram)
export LDFLAGS="$LDFLAGS -flto=auto"
%endif
%endif

gn_system_libraries=(
    brotli
    double-conversion
    ffmpeg
    flac
    flatbuffers
    fontconfig
    freetype
    harfbuzz-ng
    icu
    jsoncpp
    libdrm
    libevent
    libjpeg
    libpng
    libsecret
    libusb
    libwebp
    libxml
    libxslt
    opus
    re2
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

%if %{with system_crc32c}
find third_party/crc32c -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( crc32c )
%endif



%if %{with system_dav1d}
find third_party/dav1d -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( dav1d )
%endif

%if %{with system_highway}
find third_party/highway -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( highway )
%endif


%if %{with system_nvctrl}
find third_party/angle/src/third_party/libXNVCtrl/ -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( libXNVCtrl )
%endif

%if %{with system_spirv}
rm -rf third_party/swiftshader/third_party/SPIRV-Headers/include
find  third_party/swiftshader/third_party/SPIRV-Tools/ -type f ! -name "*.gn" -a ! -name "*.gni"  -delete

rm -rf third_party/vulkan-deps/spirv-headers/src/include
find third_party/vulkan-deps/spirv-tools/ -type f ! -name "*.gn" -a ! -name "*.gni"  -delete

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

%if %{with system_nghttp2}
find third_party/electron_node/deps/nghttp2 -type f ! -name "*.gn" -a ! -name "*.gni" -a ! -name "*.gyp" -a ! -name "*.gypi" -delete
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
myconf_gn+=' override_electron_version="%{version}"'
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



# do not build PDF support
myconf_gn+=" enable_pdf=false"
myconf_gn+=" enable_pdf_viewer=false"
myconf_gn+=" enable_print_preview=false"
myconf_gn+=" enable_printing=false"
myconf_gn+=" enable_basic_printing=false"
myconf_gn+=' use_cups=false'
#we don't build PDF support, so disabling the below:
#myconf_gn+=" use_system_lcms2=true"
#myconf_gn+=" use_system_libopenjpeg2=true"


#do not build chrome pepper plugins support
myconf_gn+=" enable_plugins=false"
myconf_gn+=" enable_ppapi=false"

#do not build webextensions support
myconf_gn+=' enable_electron_extensions=false'

# The option below get overriden by whatever is in CFLAGS/CXXFLAGS, so they affect only C++ code.
# symbol_level=2 is full debug
# symbol_level=1 is enough info for stacktraces
# symbol_level=0 no debuginfo (only function names in private symbols)
# blink (HTML engine) and v8 (js engine) are template-heavy, trying to compile them with full debug leads to linker errors
%ifnarch %ix86 %arm aarch64
%if %{without lto}
myconf_gn+=" symbol_level=2"
%else
myconf_gn+=" symbol_level=1"
%endif
myconf_gn+=" blink_symbol_level=1"
myconf_gn+=" v8_symbol_level=1"
%endif
%ifarch %ix86 %arm
#Sorry, no debug on 32bit.
myconf_gn+=" symbol_level=1"
myconf_gn+=" blink_symbol_level=0"
myconf_gn+=" v8_symbol_level=0"
%endif
%ifarch aarch64 #“No space left on device” with symbol level 2
myconf_gn+=" symbol_level=1"
myconf_gn+=" blink_symbol_level=1"
myconf_gn+=" v8_symbol_level=1"
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



#FIXME: possibly enable this when skia gets built with rust code by default.
#Need to patch in optflags and possibly FFI LTO hacks (see signal-desktop package for how it's done)
myconf_gn+=' enable_rust=false'

#See net/base/features.cc. It's not enabled yet.
#FIXME: enable this and add shims to build with system zstd when it's enabled
myconf_gn+=' disable_zstd_filter=true'

myconf_gn+=' chrome_root_store_supported=false'
myconf_gn+=' chrome_root_store_optional=false'
myconf_gn+=' chrome_root_store_policy_supported=false'
myconf_gn+=' trial_comparison_cert_verifier_supported=false'
myconf_gn+=' use_kerberos=false'
myconf_gt+=' is_ct_supported=false'

myconf_gn+=' disable_histogram_support=true'



#Do not build Chromecast
myconf_gn+=" enable_remoting=false"
myconf_gn+=" enable_media_remoting=false"
myconf_gn+=" enable_service_discovery=false"

#disable some debug/tracing hooks, they increase size and we do not build chrome://tracing anyway (see disable-catapult.patch)
myconf_gn+=" enable_trace_logging=false"
myconf_gn+=" optional_trace_events_enabled=false"
myconf_gn+=" use_runtime_vlog=false"
myconf_gn+=" rtc_disable_logging=true"
myconf_gn+=" rtc_disable_metrics=true"
myconf_gn+=" rtc_disable_trace_events=true"
myconf_gn+=' enable_perfetto_system_consumer=false'
myconf_gn+=' enable_perfetto_trace_processor_json=false'
myconf_gn+=' enable_perfetto_trace_processor_httpd=false'
myconf_gn+=' enable_perfetto_zlib=false'



myconf_gn+=" enable_library_cdms=false"
myconf_gn+=" use_pulseaudio=true link_pulseaudio=true"
myconf_gn+=" is_component_build=false"
myconf_gn+=" use_sysroot=false"
myconf_gn+=" fatal_linker_warnings=false"
myconf_gn+=" use_allocator_shim=true"
myconf_gn+=" use_partition_alloc=true"


myconf_gn+=" disable_fieldtrial_testing_config=true"
myconf_gn+=" use_unofficial_version_number=false"
myconf_gn+=" use_lld=false"

%if %{with vaapi}
myconf_gn+=' use_vaapi=true'
myconf_gn+=' use_vaapi_x11=true'
myconf_gn+=' use_libgav1_parser=true'
%else
myconf_gn+=' use_vaapi=false'
myconf_gn+=' use_vaapi_x11=false'
myconf_gn+=' use_libgav1_parser=false'
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
%if %{with system_nghttp2}
myconf_gn+=" use_system_nghttp2=true"
%endif
%if %{with system_llhttp}
myconf_gn+=" use_system_llhttp=true"
%endif
%if %{with system_histogram}
myconf_gn+=" use_system_histogram=true"
%endif
%if %{with system_simdutf}
myconf_gn+=' use_system_simdutf=true'
%endif
%if %{with clang}
myconf_gn+=" is_clang=true clang_base_path=\"/usr\" clang_use_chrome_plugins=false"
myconf_gn+=" use_lld=true"
# PGO is broken rn
myconf_gn+=" chrome_pgo_phase=0"
%else
myconf_gn+=" is_clang=false"
%if %{with gold}
myconf_gn+=" use_gold=true"
%else
myconf_gn+=" use_gold=false"
%endif
%endif

%if %{with lto}


%if %{without clang}
myconf_gn+=" gcc_lto=true"
%else
myconf_gn+=" use_thin_lto=true"
%endif

# endif with lto
%endif

%ifarch %arm
# Bundled libaom is broken on ARMv7
%if %{without system_aom}
# [74796s] FAILED: v8_context_snapshot_generator
# [74796s] python3 "../../build/toolchain/gcc_link_wrapper.py" --output="./v8_context_snapshot_generator" -- g++ -Wl,--build-id=sha1 -fPIC -Wl,-z,noexecstack -Wl,-z,relro -Wl,-z,now -rdynamic -Wl,-z,defs -Wl,--as-needed -pie -Wl,--disable-new-dtags -Wl,-rpath=\$ORIGIN  -Wl,--as-needed -fuse-ld=lld -o "./v8_context_snapshot_generator" -Wl,--start-group @"./v8_context_snapshot_generator.rsp"  -Wl,--end-group  -latomic -ldl -lpthread -lrt -lgmodule-2.0 -lglib-2.0 -lgobject-2.0 -lgthread-2.0 -ljsoncpp -labsl_base -labsl_raw_logging_internal -labsl_log_severity -labsl_spinlock_wait -labsl_cord -labsl_cordz_info -labsl_cord_internal -labsl_cordz_functions -labsl_exponential_biased -labsl_cordz_handle -labsl_synchronization -labsl_graphcycles_internal -labsl_stacktrace -labsl_symbolize -labsl_debugging_internal -labsl_demangle_internal -labsl_malloc_internal -labsl_time -labsl_civil_time -labsl_time_zone -labsl_bad_optional_access -labsl_strings -labsl_strings_internal -labsl_int128 -labsl_throw_delegate -labsl_hash -labsl_city -labsl_bad_variant_access -labsl_low_level_hash -labsl_raw_hash_set -labsl_hashtablez_sampler -labsl_failure_signal_handler -labsl_examine_stack -labsl_random_distributions -labsl_random_seed_sequences -labsl_random_internal_pool_urbg -labsl_random_internal_randen -labsl_random_internal_randen_hwaes -labsl_random_internal_randen_hwaes_impl -labsl_random_internal_randen_slow -labsl_random_internal_platform -labsl_random_internal_seed_material -labsl_random_seed_gen_exception -labsl_status -labsl_str_format_internal -labsl_strerror -labsl_statusor -licui18n -licuuc -licudata -lsmime3 -lnss3 -lnssutil3 -lplds4 -lplc4 -lnspr4 -ldouble-conversion -levent -lz -ljpeg -lpng16 -lxml2 -lxslt -lresolv -lgio-2.0 -lbrotlidec -lwebpdemux -lwebpmux -lwebp -lfreetype -lexpat -lfontconfig -lharfbuzz-subset -lharfbuzz -lyuv -lopus -lvpx -lm -ldav1d -lX11 -lXcomposite -lXdamage -lXext -lXfixes -lXrender -lXrandr -lXtst -lpipewire-0.3 -lgbm -lEGL -ldrm -lcrc32c -lbsd -lxcb -lxkbcommon -lwayland-client -ldbus-1 -lre2 -lpangocairo-1.0 -lpango-1.0 -lcairo -latk-1.0 -latk-bridge-2.0 -lasound -lpulse -lavcodec -lavformat -lavutil -lXi -lpci -lxxhash -lXNVCtrl -lsnappy -lavif -ljxl -lwoff2dec -latspi
# [74796s] ld.lld: error: undefined symbol: aom_arm_cpu_caps
# [74796s] >>> referenced by av1_rtcd.h:1079 (../../third_party/libaom/source/config/linux/arm/config/av1_rtcd.h:1079)
# [74796s] >>>               libaom/av1_rtcd.o:(setup_rtcd_internal) in archive obj/third_party/libaom/libaom.a
# [74796s] >>> referenced by aom_dsp_rtcd.h:3560 (../../third_party/libaom/source/config/linux/arm/config/aom_dsp_rtcd.h:3560)
# [74796s] >>>               libaom/aom_dsp_rtcd.o:(setup_rtcd_internal) in archive obj/third_party/libaom/libaom.a
# [74796s] >>> referenced by aom_scale_rtcd.h:162 (../../third_party/libaom/source/config/linux/arm/config/aom_scale_rtcd.h:162)
# [74796s] >>>               libaom/aom_scale_rtcd.o:(setup_rtcd_internal) in archive obj/third_party/libaom/libaom.a
myconf_gn+=" enable_libaom=false"
%endif
%endif

%if %{with pipewire}
myconf_gn+=" rtc_use_pipewire=true rtc_link_pipewire=true"
%endif

%if %{with qt}
myconf_gn+=" use_qt=true"
%endif


# Do not build WebGPU support. It is huge and not used by ANY known apps (we would know if it was — it's hidden behind an experimental flag).
myconf_gn+=" use_dawn=false"

# The proprietary codecs just force the chromium to say they can use it and
# offload the actual computation to the ffmpeg, otherwise the chromium
# won't be able to load the codec even if the library can handle it
myconf_gn+=" proprietary_codecs=true"
myconf_gn+=" ffmpeg_branding=\"Chrome\""

# GN does not support passing cflags:
#  https://bugs.chromium.org/p/chromium/issues/detail?id=642016
gn gen out/Release --args="import(\"//electron/build/args/release.gn\") ${myconf_gn}"


# dump the linker command line (if any) in case of failure
ninja -v %{?_smp_mflags} -C out/Release chromium_licenses copy_headers version electron || (cat out/Release/*.rsp | sed 's/ /\n/g' && false)



%install
install -d -m 0755 %{buildroot}%{_bindir}
install -d -m 0755 %{buildroot}%{_includedir}/electron
install -d -m 0755 %{buildroot}%{_libdir}/electron
install -d -m 0755 %{buildroot}%{_libdir}/electron/resources
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
cp -lv *.bin *.pak -t %{buildroot}%{_libdir}/electron/
install -pm 0644 resources/default_app.asar -t %{buildroot}%{_libdir}/electron/resources/

cp -lrv locales -t %{buildroot}%{_libdir}/electron/
rm -v %{buildroot}%{_libdir}/electron/locales/*.pak.info


install -pm 0755 electron                -t %{buildroot}%{_libdir}/electron/
install -pm 0755 chrome_crashpad_handler -t %{buildroot}%{_libdir}/electron/ ||true
install -pm 0755 libEGL.so               -t %{buildroot}%{_libdir}/electron/
install -pm 0755 libGLESv2.so            -t %{buildroot}%{_libdir}/electron/
install -pm 0755 libqt5_shim.so          -t %{buildroot}%{_libdir}/electron/ ||true
install -pm 0755 libvk_swiftshader.so    -t %{buildroot}%{_libdir}/electron/ ||true
install -pm 0644 vk_swiftshader_icd.json -t %{buildroot}%{_libdir}/electron/ ||true
install -pm 0644 version                 -t %{buildroot}%{_libdir}/electron/
popd





cp -lrvT out/Release/gen/node_headers/include/node %{buildroot}%{_includedir}/electron

# Install electron.macros
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
cp /dev/stdin %{buildroot}%{_rpmconfigdir}/macros.d/macros.electron <<"EOF"
%%electron_req Requires: electron%{_isa}(abi) = %{abi_version}
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

%{_libdir}/electron/

%files devel
%{_includedir}/electron
%{_rpmconfigdir}/macros.d/macros.electron

%files doc
%doc electron/README.md
%doc electron/docs

%changelog
