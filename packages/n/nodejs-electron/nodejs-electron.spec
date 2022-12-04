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


%undefine _package_note_file
# https://fedoraproject.org/wiki/Changes/SetBuildFlagsBuildCheck
%undefine _auto_set_build_flags

%define mod_name electron
# https://github.com/nodejs/node/blob/main/doc/abi_version_registry.json
%define abi_version 109

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

%ifarch %ix86 x86_64 %arm
#Use subzero as swiftshader backend instead of LLVM
%bcond_without subzero
%else
%bcond_with subzero
%endif



%ifarch x86_64 %ix86 aarch64
%bcond_without vaapi
%else
%bcond_with vaapi
%endif

%if %{with vaapi}
#vaapi still requires bundled libvpx
%bcond_with system_vpx
%else
%bcond_without system_vpx
%endif



%bcond_with clang



%if %{with clang}
%global toolchain clang
%else

# Linker selection. GCC only. Default is BFD.
# You can try different ones if it has problems.
# arm64 reports relocation errors with BFD.
%ifarch aarch64
%bcond_without gold
%else
%bcond_with gold
%endif

# Both BFD and Gold run out of memory on 32-bit.
%ifarch %ix86 %arm
%bcond_without lld
%else
%bcond_with lld
%endif

%endif #with clang

#Mold succeeds on ix86 but seems to produce corrupt binaries (no build-id)
%bcond_with mold

%ifnarch %ix86 %arm aarch64
# OBS does not have enough powerful machines to build with LTO on aarch64.

%if (0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150600 || 0%{?fedora})
%bcond_without lto
%else
%bcond_with lto
%endif

%else
%bcond_with lto
%endif


%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400 || 0%{?fedora}
%bcond_without system_harfbuzz
%else
%bcond_with system_harfbuzz
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500 || 0%{?fedora} >= 37
%bcond_without system_avif
%else
%bcond_with system_avif
%endif

%bcond_without system_freetype
%bcond_without system_nghttp2
%bcond_without system_double_conversion
%bcond_without system_woff2


%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150600 || 0%{?fedora} >= 37
%bcond_without system_aom
%bcond_without icu_71
%bcond_without ffmpeg_5
%bcond_without system_dav1d
%bcond_without system_spirv
%else
%bcond_with system_aom
%bcond_with icu_71
%bcond_with ffmpeg_5
%bcond_with system_dav1d
%bcond_with system_spirv
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500 || 0%{?fedora_version}
%bcond_without system_crc32c
%bcond_without system_nvctrl
%else
%bcond_with system_crc32c
%bcond_with system_nvctrl
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150600 || 0%{?fedora_version}
%bcond_without system_jxl
%else
%bcond_with system_jxl
%endif



%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
%bcond_without system_yuv
%else
%bcond_with system_yuv
%endif




%if 0%{?fedora}

%bcond_without system_llhttp
%bcond_without system_histogram
%else

%bcond_with system_llhttp
%bcond_with system_histogram
%endif

%if 0%{?fedora} >= 38
%bcond_without llhttp_8
%else
%bcond_with llhttp_8
%endif

# Abseil is broken in Leap
# enable this when boo#1203378 and boo#1203379 get fixed
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150600 || 0%{?fedora} >= 37
%if %{without clang}
%bcond_without system_abseil
%else
# Clang has several problems with std::optional used by system abseil
%bcond_with system_abseil
%endif
%else
%bcond_with system_abseil
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
# srtp / srtp2 | third_party/libsrtp               | Api matches neither version 1 nor 2 of this library.
# uv           | third_party/electron_node/deps/uv | Heavily modified version which is exposed as part of Electron's public ABI.




Name:           nodejs-electron
Version:        21.3.2
Release:        0
Summary:        Build cross platform desktop apps with JavaScript, HTML, and CSS
License:        AFL-2.0 AND Apache-2.0 AND blessing AND BSD-2-Clause AND BSD-3-Clause AND BSD-Protection AND BSD-Source-Code AND bzip2-1.0.6 AND IJG AND ISC AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND MIT-CMU AND MIT-open-group AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later) AND MPL-2.0 AND OpenSSL AND SGI-B-2.0 AND SUSE-Public-Domain AND X11
Group:          Development/Languages/NodeJS
URL:            https://github.com/electron/electron
Source0:        %{mod_name}-%{version}.tar.xz
Source1:        create_tarball.sh
Source10:       electron-launcher.sh
Source11:       electron.desktop
Source12:       electron-logo-symbolic.svg
# Shim generators for unbundling libraries
Source50:       flatbuffers.gn
Source51:       libsecret.gn


# Reverse upstream changes to be able to build against ffmpeg-4
Source400:      ffmpeg-new-channel-layout.patch
Source401:      audio_file_reader-ffmpeg-AVFrame-duration.patch
# …and against icu-69
Source410:      NumberFormat-icu71-incrementExact.patch
Source411:      intl-objects-icu71-UNUM_APPROXIMATELY_SIGN_FIELD.patch

#Reverse upstream changes to build against system libavif.
#All of this patch is dead code, so it can be reversed unconditionally.
Source420:      avif_image_decoder-AVIF_PIXEL_FORMAT_COUNT.patch


# PATCHES for openSUSE-specific things
Patch0:         chromium-102-compiler.patch
Patch1:         fpic.patch
Patch3:         gcc-enable-lto.patch
Patch5:         chromium-norar.patch
Patch6:         chromium-vaapi.patch
Patch7:         chromium-91-java-only-allowed-in-android-builds.patch
Patch9:         chromium-86-fix-vaapi-on-intel.patch
# Always disable use_thin_lto which is an lld feature
Patch21:        electron-13-fix-use-thin-lto.patch
# Fix common.gypi to include /usr/include/electron
Patch25:        electron-16-system-node-headers.patch
# https://sources.debian.org/patches/chromium/102.0.5005.115-1/debianization/support-i386.patch/
Patch39:        support-i386.patch
# from https://sources.debian.org/patches/chromium/103.0.5060.53-1/disable/catapult.patch/
Patch67:        disable-catapult.patch
Patch68:        do-not-build-libvulkan.so.patch
Patch69:        nasm-generate-debuginfo.patch
Patch70:        disable-fuses.patch
Patch71:        enable-jxl.patch
Patch72:        electron-version-from-env.patch
# https://code.qt.io/cgit/qt/qtwebengine-chromium.git/commit/?h=102-based&id=d617766b236a93749ddbb50b75573dd35238ffc9
Patch73:        disable-webspeech.patch
Patch74:        common.gypi-remove-fno-omit-frame-pointer.patch
Patch75:        gcc-asmflags.patch

# PATCHES to use system libs
Patch1002:      chromium-system-libusb.patch
Patch1017:      system-libdrm.patch
# http://svnweb.mageia.org/packages/updates/7/chromium-browser-stable/current/SOURCES/chromium-74-pdfium-system-libopenjpeg2.patch?view=markup
Patch1038:      pdfium-fix-system-libs.patch
# https://sources.debian.org/patches/chromium/102.0.5005.115-1/system/jsoncpp.patch/
Patch1040:      system-jsoncpp.patch
# https://sources.debian.org/patches/chromium/102.0.5005.115-1/system/zlib.patch/
Patch1041:      system-zlib.patch
Patch1043:      node-system-libs.patch
Patch1044:      replace_gn_files-system-libs.patch
Patch1045:      angle-system-xxhash.patch
# https://svnweb.mageia.org/packages/cauldron/chromium-browser-stable/current/SOURCES/chromium-99-pdfium-system-libtiff-libpng.patch
Patch1046:      chromium-99-pdfium-system-libtiff.patch
Patch1047:      cares_public_headers.patch
Patch1048:      chromium-remove-bundled-roboto-font.patch
Patch1053:      swiftshader-use-system-llvm.patch
Patch1054:      thread_annotations-fix-build-with-system-abseil.patch
Patch1063:      system-libbsd.patch
Patch1065:      base-system-nspr.patch
Patch1066:      system-gtest.patch
Patch1067:      breakpad-system-curl.patch
Patch1068:      system-six.patch
Patch1069:      system-usb_ids.patch
Patch1070:      skia-system-vulkan-headers.patch
Patch1071:      system-pydeps.patch
Patch1072:      node-system-icu.patch
Patch1073:      system-nasm.patch
Patch1074:      no-zlib-headers.patch
Patch1075:      system-abseil-missing-shims.patch
Patch1076:      crashpad-use-system-abseil.patch

# PATCHES to fix interaction with third-party software
Patch2004:      chromium-gcc11.patch
Patch2010:      chromium-93-ffmpeg-4.4.patch
Patch2011:      chromium-ffmpeg-first-dts.patch
# Fix building sql recover_module
Patch2020:      electron-13-fix-sql-virtualcursor-type.patch
# Fixe builds with older clang versions that do not allow
# nomerge attributes on declaration. Otherwise, the following error
# is produced:
#     'nomerge' attribute cannot be applied to a declaration
# See https://reviews.llvm.org/D92800
Patch2022:      electron-13-fix-base-check-nomerge.patch
# Fix electron patched code
Patch2024:      electron-16-std-vector-non-const.patch
Patch2029:      electron-16-webpack-fix-openssl-3.patch
Patch2030:      v8-icu69-FormattedNumberRange-no-default-constructible.patch
Patch2031:      partition_alloc-no-lto.patch
Patch2032:      seccomp_bpf-no-lto.patch
# adjust to llhttp 8 api changes
%if %{with llhttp_8}
Patch2033:       node-upgrade-llhttp-to-8.patch
%else
Source2033:      node-upgrade-llhttp-to-8.patch
%endif

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
# Fedora patch to fix build with python3.11
Patch3066:      chromium-103.0.5060.53-python3-do-not-use-deprecated-mode-U.patch
Patch3067:      reproducible-config.gypi.patch
Patch3068:      content_language_parser-missing-string.patch
Patch3069:      aggregatable_attribution_utils-do-not-assume-abseil-ABI.patch
Patch3072:      attribution_response_parsing-do-not-assume-abseil-ABI.patch
Patch3074:      pending_beacon_dispatcher-virtual-functions-cannot-be-constexpr.patch
Patch3075:      std_lib_extras-missing-intptr_t.patch
Patch3076:      gtk_ui_platform_stub-incomplete-type-LinuxInputMethodContext.patch
Patch3077:      argument_spec-missing-isnan-isinf.patch
Patch3078:      select_file_dialog_linux_kde-Wodr.patch
Patch3079:      web_contents_impl-Wsubobject-linkage.patch
Patch3080:      compact_enc_det_generated_tables-Wnarrowing.patch
Patch3081:      string_hasher-type-pun-UB-causes-heap-corruption.patch
Patch3082:      ipcz-buffer_id-Wnarrowing.patch
Patch3083:      swiftshader-Half-Wstrict-aliasing.patch
Patch3084:      swiftshader-Constants-Wstrict-aliasing.patch
Patch3085:      half_float-Wstrict-aliasing.patch
Patch3086:      unzip-Wsubobject-linkage.patch
Patch3087:      v8_initializer-PageAllocator-fpermissive.patch
Patch3089:      ipcz-safe_math-Wuninitialized.patch
Patch3090:      passwords_counter-Wsubobject-linkage.patch
Patch3091:      vector_math_impl-Wstrict-aliasing.patch
Patch3092:      webgl_image_conversion-Wstrict-aliasing.patch
Patch3093:      xr_cube_map-Wstrict-aliasing.patch
Patch3094:      static_constructors-Wstrict-aliasing.patch

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
%if %{with system_double_conversion}
BuildRequires:  double-conversion-devel
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
%if 0%{?fedora}
BuildRequires:  flatbuffers-compiler
%endif
BuildRequires:  flatbuffers-devel
BuildRequires:  git-core
BuildRequires:  gn >= 0.1807
BuildRequires:  gperf
%if %{with system_histogram}
BuildRequires:  HdrHistogram_c-devel
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  hwdata
%if 0%{?fedora}
BuildRequires:  libatomic
%endif
%if %{with system_aom}
BuildRequires:  libaom-devel >= 3.4
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
%if %{without subzero}
BuildRequires:  llvm-devel
%endif
BuildRequires:  memory-constraints
%if %{with mold}
BuildRequires:  mold
%endif
%ifarch %ix86 x86_64
BuildRequires:  nasm
%endif
%if 0%{?suse_version}
BuildRequires:  ninja >= 1.7.2
%else
BuildRequires:  ninja-build >= 1.7.2
%endif
%if 0%{?sle_version} == 150300
BuildRequires:  nodejs16
BuildRequires:  npm16
%else
BuildRequires:  nodejs >= 16
BuildRequires:  npm
%endif
BuildRequires:  pkgconfig
BuildRequires:  plasma-wayland-protocols
BuildRequires:  python3-json5
BuildRequires:  python3-mako
BuildRequires:  python3-ply
BuildRequires:  python3-six
BuildRequires:  rsync
BuildRequires:  snappy-devel
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  util-linux
BuildRequires:  vulkan-headers
%if %{with system_abseil}
BuildRequires:  pkgconfig(absl_algorithm_container) >= 20211000
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
%endif
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo) >= 1.6
%if %{with system_dav1d}
BuildRequires:  pkgconfig(dav1d) >= 1
%endif
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(expat)
%if %{with system_freetype}
BuildRequires:  pkgconfig(freetype2)
%endif
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gtk+-3.0)
%if %{with system_harfbuzz}
BuildRequires:  pkgconfig(harfbuzz) >= 3
%endif

%if %{with icu_71}
BuildRequires:  pkgconfig(icu-i18n) >= 71
%else

%if 0%{?fedora}
BuildRequires:  libicu-devel < 70
%else
BuildRequires:  icu.691-devel
%endif

%endif

BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(lcms2)
%if %{with ffmpeg_5}
BuildRequires:  pkgconfig(libavcodec) >= 59
BuildRequires:  pkgconfig(libavformat) >= 59
BuildRequires:  pkgconfig(libavutil) >= 57
%else
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat) >= 58
BuildRequires:  pkgconfig(libavutil)
%endif
%if %{with system_avif}
BuildRequires:  pkgconfig(libavif)
%endif
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevent)
%if %{with system_jxl}
BuildRequires:  pkgconfig(libjxl)
%endif
%if 0%{?fedora} >= 38
#Work around https://bugzilla.redhat.com/show_bug.cgi?id=2148612
BuildRequires:  pkgconfig(libmd)
%endif
%if %{with system_nghttp2}
BuildRequires:  pkgconfig(libnghttp2)
%endif
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libwebp) >= 0.4.0
%if %{with system_woff2}
BuildRequires:  pkgconfig(libwoff2dec)
%endif
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.5
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(libxxhash)
%if %{with system_yuv}
BuildRequires:  pkgconfig(libyuv)
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
BuildRequires:  pkgconfig(re2)
%if %{with system_spirv}
%if 0%{?suse_version}
BuildRequires:  spirv-headers
%else
BuildRequires:  spirv-headers-devel
%endif
BuildRequires:  pkgconfig(SPIRV-Tools) >= 2022.2
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
BuildRequires:  pkgconfig(vpx) >= 1.8.2
%endif
%if %{without clang}
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150600 || 0%{?fedora}
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
Recommends:     noto-coloremoji-fonts

# This required library is dlopened
%ifarch %ix86 %arm
Requires:       libvulkan.so.1
%else
Requires:       libvulkan.so.1()(64bit)
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

%if %{without icu_71}
#SUSE patched code includes icu headers
%if 0%{?fedora}
Requires:       libicu-devel%{?_isa}
%else
Requires:       icu.691-devel%{?_isa}
%endif
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

%if %{without ffmpeg_5}
patch -R -p1 < %SOURCE400
%endif

%if %{without icu_71}
patch -R -p1 < %SOURCE410
patch -R -p1 < %SOURCE411
%else
patch -R -p1 < %PATCH2030
%endif

# This one depends on an ffmpeg nightly, reverting unconditionally.
patch -R -p1 < %SOURCE401

# This one is dead code, we cen revert it even when using bundled avif.
patch -R -p1 < %SOURCE420

# Link system wayland-protocols-devel into where chrome expects them
mkdir -p third_party/wayland-protocols/kde/src
#ln -svfT %{_datadir}/wayland-protocols third_party/wayland-protocols/src
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
# GN sets lto on its own and we need just ldflag options, not cflags
%define _lto_cflags %{nil}

# see electron-version-from-env.patch
export SUSE_ELECTRON_VERSION=%{version}

# Make sure python is python3
install -d -m 0755 python3-path
ln -sf %{_bindir}/python3 "$(pwd)/python3-path/python"
export PATH="$(pwd)/python3-path:${PATH}"


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

%ifnarch x86_64
export CFLAGS="$(echo ${CFLAGS} | sed -e 's/-g /-g1 /g' -e 's/-g$/-g1/g')"
%endif


export LDFLAGS="%{?build_ldflags}"


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
export LDFLAGS="${LDFLAGS} -Wl,--no-keep-memory -Wl,--hash-size=30 -Wl,--reduce-memory-overheads"
%endif

%endif #without lld
%endif #ifarch ix86 arm




%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150600 || 0%{?fedora}
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
%limit_build -m 2600
%endif

%if %{with lto} && %{without clang}
# reduce the threads for linking even more due to LTO eating ton of memory
_link_threads=$(((%{jobs} - 2)))

%ifarch aarch64
_link_threads=1

%if %{without mold}
%if %{with gold}
export LDFLAGS="${LDFLAGS} -Wl,--no-map-whole-files -Wl,--no-keep-memory -Wl,--no-keep-files-mapped"
%else
export LDFLAGS="${LDFLAGS} -Wl,--no-keep-memory -Wl,--hash-size=30 -Wl,--reduce-memory-overheads"
%endif
%endif

%endif
test "$_link_threads" -le 0 && _link_threads=1
export LDFLAGS="$LDFLAGS -flto=$_link_threads --param lto-max-streaming-parallelism=1"
%endif

gn_system_libraries=(
    brotli
    ffmpeg
    flac
    flatbuffers
    fontconfig
    icu
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

%if %{with system_jxl}
find third_party/highway -type f ! -name "*.gn" -a ! -name "*.gni" -delete
find third_party/libjxl -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( libjxl )
%endif


%if %{with system_dav1d}
find third_party/dav1d -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( dav1d )
%endif

%if %{with system_double_conversion}
find base/third_party/double_conversion -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( double-conversion )
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

%if %{with system_harfbuzz}
find third_party/harfbuzz-ng -type f ! -name "*.gn" -a ! -name "*.gni" -a ! -path "third_party/harfbuzz-ng/utils/hb_scoped.h" -delete
gn_system_libraries+=( harfbuzz-ng )
%endif

%if %{with system_freetype}
find third_party/freetype -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( freetype )
%endif

%if %{with system_vpx}
find third_party/libvpx -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( libvpx )
%endif

%if %{with system_woff2}
find third_party/woff2 -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( woff2 )
%endif

%if %{with system_yuv}
find third_party/libyuv -type f ! -name "*.gn" -a ! -name "*.gni" -delete
gn_system_libraries+=( libyuv )
%endif

build/linux/unbundle/replace_gn_files.py --system-libraries ${gn_system_libraries[@]}



%if %{with system_nghttp2}
find third_party/electron_node/deps/nghttp2 -type f ! -name "*.gn" -a ! -name "*.gni" -a ! -name "*.gyp" -a ! -name "*.gypi" -delete
%endif

%if %{with system_llhttp}
find third_party/electron_node/deps/llhttp -type f ! -name "*.gn" -a ! -name "*.gni" -a ! -name "*.gyp" -a ! -name "*.gypi" -delete
%endif

%if %{with system_histogram}
find third_party/electron_node/deps/histogram -type f ! -name "*.gn" -a ! -name "*.gni" -a ! -name "*.gyp" -a ! -name "*.gypi" -delete
%endif


# Create the configuration for GN
# Available options: out/Release/gn args --list out/Release/
myconf_gn=""
myconf_gn+=" custom_toolchain=\"//build/toolchain/linux/unbundle:default\""
myconf_gn+=" host_toolchain=\"//build/toolchain/linux/unbundle:default\""
myconf_gn+=" use_custom_libcxx=false"
%ifarch %ix86
myconf_gn+=" host_cpu=\"x86\""
%endif
%ifarch x86_64
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
%if %{with subzero}
myconf_gn+=" use_swiftshader_with_subzero=true"
%else
myconf_gn+=" use_swiftshader_with_subzero=false"
%endif
myconf_gn+=" is_component_ffmpeg=true"
myconf_gn+=" use_cups=true"
myconf_gn+=" use_aura=true"

# always load system libvulkan.so
myconf_gn+=" angle_use_custom_libvulkan=false"

# do not build PDF support
myconf_gn+=" enable_pdf=false"
myconf_gn+=" enable_pdf_viewer=false"
myconf_gn+=" enable_print_preview=false"
myconf_gn+=" enable_basic_printing=false"

#do not build chrome pepper plugins support
myconf_gn+=" enable_plugins=false"
myconf_gn+=" enable_ppapi=false"

# This requires the non-free closure_compiler.jar. If we ever need to build chrome with JS typecheck,
# we would need to package it separately and compile it from sources, since the chrome git repo
# provides only a compiled binary.
myconf_gn+=" enable_js_type_check=false"

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
myconf_gn+=" symbol_level=0" 
myconf_gn+=" blink_symbol_level=0"
myconf_gn+=" v8_symbol_level=0"
%endif
%ifarch aarch64 #“No space left on device” with symbol level 2
myconf_gn+=" symbol_level=1"
myconf_gn+=" blink_symbol_level=1"
myconf_gn+=" v8_symbol_level=1"
%endif

myconf_gn+=" use_kerberos=true"

# do not build some chrome features not used by electron
myconf_gn+=" enable_vr=false"
myconf_gn+=" enable_reading_list=false"
myconf_gn+=" enable_reporting=false"
myconf_gn+=" build_with_tflite_lib=false"
myconf_gn+=" build_tflite_with_xnnpack=false"
myconf_gn+=" safe_browsing_mode=0"
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
myconf_gn+=" enable_xz_extractor=false"
myconf_gn+=" enable_feed_v2=false"


#Do not build Chromecast
myconf_gn+=" enable_remoting=false"
myconf_gn+=" enable_media_remoting=false"
myconf_gn+=" enable_service_discovery=false"



myconf_gn+=" enable_library_cdms=false"
myconf_gn+=" use_pulseaudio=true link_pulseaudio=true"
myconf_gn+=" is_component_build=false"
myconf_gn+=" use_sysroot=false"
myconf_gn+=" fatal_linker_warnings=false"
myconf_gn+=" use_allocator=\"partition\""
myconf_gn+=" use_allocator_shim=true"
myconf_gn+=" use_partition_alloc=true"


myconf_gn+=" disable_fieldtrial_testing_config=true"
myconf_gn+=" use_gnome_keyring=false"
myconf_gn+=" use_unofficial_version_number=false"
myconf_gn+=" use_lld=false"
%if %{with vaapi}
myconf_gn+=" use_vaapi=true"
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
myconf_gn+=" use_system_lcms2=true"
myconf_gn+=" use_system_libopenjpeg2=true"
myconf_gn+=" use_system_wayland_scanner=true"
%if %{with system_harfbuzz}
myconf_gn+=" use_system_harfbuzz=true"
%endif
%if %{with system_freetype}
myconf_gn+=" use_system_freetype=true"
%endif
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

#Build the supplementary stuff first to notice errors earlier bc building electron itself takes several hours.
ninja -v %{?_smp_mflags} -C out/Release chromium_licenses
ninja -v %{?_smp_mflags} -C out/Release copy_headers
ninja -v %{?_smp_mflags} -C out/Release version

# dump the linker command line (if any) in case of failure
ninja -v %{?_smp_mflags} -C out/Release electron || (cat out/Release/*.rsp | sed 's/ /\n/g' && false)



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
install -pm 0644 electron/default_app/icon.png %{buildroot}%{_datadir}/pixmaps/%{mod_name}.png
install -pm 0644 %{SOURCE12} %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/electron-symbolic.svg

desktop-file-install --dir %{buildroot}%{_datadir}/applications/ %{SOURCE11}

pushd out/Release
rsync -av *.bin *.pak %{buildroot}%{_libdir}/electron/
install -pm 0644 resources/default_app.asar -t %{buildroot}%{_libdir}/electron/resources/

rsync -av --exclude '*.pak.info' locales %{buildroot}%{_libdir}/electron/


install -pm 0755 electron                -t %{buildroot}%{_libdir}/electron/
install -pm 0755 chrome_crashpad_handler -t %{buildroot}%{_libdir}/electron/
install -pm 0755 libEGL.so               -t %{buildroot}%{_libdir}/electron/
install -pm 0755 libGLESv2.so            -t %{buildroot}%{_libdir}/electron/
install -pm 0755 libvk_swiftshader.so    -t %{buildroot}%{_libdir}/electron/
install -pm 0644 vk_swiftshader_icd.json -t %{buildroot}%{_libdir}/electron/
install -pm 0644 version                 -t %{buildroot}%{_libdir}/electron/
popd




# Install folders required for webapps
mkdir -p "%{buildroot}%{_sysconfdir}/webapps"
mkdir -p "%{buildroot}%{_datadir}/webapps"

rsync -av out/Release/gen/node_headers/include/node/* %{buildroot}%{_includedir}/electron

# Install electron.macros
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
cp /dev/stdin %{buildroot}%{_rpmconfigdir}/macros.d/macros.electron <<"EOF"
%%electron_req Requires: electron%{_isa}(abi) = %{abi_version}
EOF
chmod -v 644 %{buildroot}%{_rpmconfigdir}/macros.d/macros.electron

%files
%license electron/LICENSE out/Release/LICENSES.chromium.html
%{_bindir}/electron
%{_datadir}/pixmaps/electron.png
%{_datadir}/icons/hicolor/symbolic/apps/electron-symbolic.svg
%{_datadir}/applications/electron.desktop


%{_libdir}/electron/

%dir %{_sysconfdir}/webapps
%dir %{_datadir}/webapps

%files devel
%{_includedir}/electron
%{_rpmconfigdir}/macros.d/macros.electron

%files doc
%doc electron/README.md
%doc electron/docs

%changelog
