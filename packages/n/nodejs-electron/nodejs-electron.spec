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

# Do not provide libEGL.so, etc…
%define __provides_exclude ^lib.*\\.so.*$


# These ports now assemble correctly as of 19.0.5,
# but the linker gets out of memory (32-bit)
# causing build failure near the end
# Remove this block if you wish to fix it
ExcludeArch: %ix86 %arm

#x86 requires SSE2
%ifarch %ix86
ExclusiveArch:  i586 i686
BuildArch:      i686
%{expand:%%global optflags %(echo "%optflags") -march=pentium4 -mtune=generic}
%endif

%ifarch x86_64
%if 0%{?suse_version} > 1500 || 0%{?fedora}
# DISABLE LTO AS IT IS BROKEN RIGHT NOW
#%%bcond_without lto
%bcond_with lto
# else suse_version
%else
%bcond_with lto
# endif suse_version
%endif
# else arch x86_64
%else
%bcond_with lto
# endif arch x86_64
%endif

%bcond_without pipewire

%ifarch x86_64 %ix86 %arm
#Use subzero as swiftshader backend instead of LLVM
%bcond_without subzero
%else
%bcond_with subzero
%endif


%bcond_without systemicu


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


%bcond_without gold

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400 || 0%{?fedora}
%bcond_without system_harfbuzz
%else
%bcond_with system_harfbuzz
%endif

%bcond_without system_freetype

# requires 3.4 (not in factory yet)
%bcond_with system_aom

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500 || 0%{?fedora_version}
%bcond_without system_crc32c
%else
%bcond_with system_crc32c
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500 || 0%{?fedora} >= 37
%bcond_without system_dav1d
%else
%bcond_with system_dav1d
%endif

%bcond_without system_double_conversion
%bcond_without system_jsoncpp
%bcond_without system_cares
%bcond_without system_woff2

%if 0%{?fedora}
%bcond_without system_nvctrl
%else
%bcond_with system_nvctrl
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
%bcond_without system_spirv
%else
%bcond_with system_spirv
%endif

%if %{without subzero}
%bcond_without system_llvm
%else
%bcond_with system_llvm
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500 || 0%{?fedora_version}
%bcond_without system_nghttp2
%else
%bcond_with system_nghttp2
%endif

%bcond_without system_tiff

%if 0%{?fedora}
%bcond_without system_jxl
%else
%bcond_with system_jxl
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400 || 0%{?fedora}
%bcond_without system_avif
%else
%bcond_with system_avif
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500 || 0%{?fedora} >= 37
%if %{without clang}
# Clang has several problems with std::optional used by system abseil
%bcond_without system_abseil
%else
%bcond_with system_abseil
%endif
%else
%bcond_with system_abseil
%endif




Name:           nodejs-electron
Version:        19.0.7
Release:        0
Summary:        Build cross platform desktop apps with JavaScript, HTML, and CSS
License:        MIT
Group:          Productivity/Networking/Web/Browsers
URL:            https://github.com/electron/electron
Source0:        %{mod_name}-%{version}.tar.xz
Source1:        create_tarball.sh
Source10:       electron-launcher.sh
Source11:       electron.desktop
Source12:       electron-logo-symbolic.svg
# Shim generators for unbundling libraries
Source20:       absl_algorithm.gn
Source21:       absl_base.gn
Source22:       absl_cleanup.gn
Source23:       absl_container.gn
Source24:       absl_debugging.gn
Source25:       absl_flags.gn
Source26:       absl_functional.gn
Source27:       absl_hash.gn
Source28:       absl_memory.gn
Source29:       absl_meta.gn
Source30:       absl_numeric.gn
Source31:       absl_random.gn
Source32:       absl_status.gn
Source33:       absl_strings.gn
Source34:       absl_synchronization.gn
Source35:       absl_time.gn
Source36:       absl_types.gn
Source37:       brotli.gn
Source38:       crc32c.gn
# https://svnweb.mageia.org/packages/cauldron/chromium-browser-stable/current/SOURCES/chromium-79-system-dav1d.patch
Source39:       dav1d.gn
Source40:       double-conversion.gn
# https://svnweb.mageia.org/packages/cauldron/chromium-browser-stable/current/SOURCES/chromium-79-system-libaom.patch
Source41:       libaom.gn
Source42:       libavif.gn
Source43:       libjxl.gn
Source44:       libXNVCtrl.gn
Source45:       swiftshader-SPIRV-Headers.gn
Source46:       swiftshader-SPIRV-Tools.gn
Source47:       vulkan-SPIRV-Headers.gn
Source48:       vulkan-SPIRV-Tools.gn
Source49:       woff2.gn


# Reverse upstream changes to be able to build against system ffmpeg
Source400:      ffmpeg-new-channel-layout.patch
Patch0:         chromium-102-compiler.patch
Patch2:         chromium-system-libusb.patch
Patch3:         gcc-enable-lto.patch
Patch4:         chromium-gcc11.patch
Patch5:         chromium-norar.patch
Patch6:         chromium-vaapi.patch
Patch7:         chromium-91-java-only-allowed-in-android-builds.patch
Patch9:         chromium-86-fix-vaapi-on-intel.patch
Patch10:        chromium-93-ffmpeg-4.4.patch
Patch11:        chromium-ffmpeg-first-dts.patch
Patch13:        chromium-96-CouponDB-include.patch
Patch16:        chromium-98-EnumTable-crash.patch
Patch17:        system-libdrm.patch
# Fix building sql recover_module
Patch20:        electron-13-fix-sql-virtualcursor-type.patch
# Always disable use_thin_lto which is an lld feature
Patch21:        electron-13-fix-use-thin-lto.patch
# Fixe builds with older clang versions that do not allow
# nomerge attributes on declaration. Otherwise, the following error
# is produced:
#     'nomerge' attribute cannot be applied to a declaration
# See https://reviews.llvm.org/D92800
Patch22:        electron-13-fix-base-check-nomerge.patch
# Fix blink nodestructor
Patch23:        electron-13-blink-gcc-ambiguous-nodestructor.patch
# Fix electron patched code
Patch24:        electron-16-std-vector-non-const.patch
# Fix common.gypi to include /usr/include/electron
Patch25:        electron-16-system-node-headers.patch
Patch27:        electron-16-freetype-visibility-list.patch
Patch28:        electron-16-third_party-symbolize-missing-include.patch
Patch29:        electron-16-webpack-fix-openssl-3.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2052228
Patch30:        electron-16-fix-swiftshader-template.patch
# From https://git.droidware.info/wchen342/ungoogled-chromium-fedora
Patch33:        chromium-94.0.4606.71-InkDropHost-crash.patch
# https://sources.debian.org/patches/chromium/102.0.5005.115-1/upstream/byteswap-constexpr.patch/
Patch34:        byteswap-constexpr.patch
# https://sources.debian.org/patches/chromium/102.0.5005.115-1/bullseye/byteswap-constexpr2.patch/
Patch35:        byteswap-constexpr2.patch
Patch36:        chromium-101-libxml-unbundle.patch
Patch37:        chromium-102-fenced_frame_utils-include.patch
# http://svnweb.mageia.org/packages/updates/7/chromium-browser-stable/current/SOURCES/chromium-74-pdfium-system-libopenjpeg2.patch?view=markup
Patch38:        pdfium-fix-system-libs.patch
# https://sources.debian.org/patches/chromium/102.0.5005.115-1/debianization/support-i386.patch/
Patch39:        support-i386.patch
%if %{with system_jsoncpp}
# https://sources.debian.org/patches/chromium/102.0.5005.115-1/system/jsoncpp.patch/
Patch40:        system-jsoncpp.patch
%endif
# https://sources.debian.org/patches/chromium/102.0.5005.115-1/system/zlib.patch/
Patch41:        system-zlib.patch
Patch42:        chromium-fix-pac-with-gcc.patch
Patch43:        node-system-libs.patch
Patch44:        replace_gn_files-system-libs.patch
Patch45:        angle-system-xxhash.patch
%if %{with system_tiff}
# https://svnweb.mageia.org/packages/cauldron/chromium-browser-stable/current/SOURCES/chromium-99-pdfium-system-libtiff-libpng.patch
Patch46:        chromium-99-pdfium-system-libtiff.patch
%endif
Patch47:        cares_public_headers.patch
Patch48:        chromium-remove-bundled-roboto-font.patch
Patch49:        abseil-remove-unused-targets.patch
# PATCH-FIX-UPSTREAM
Patch50:        abseil_string_number_conversions-do-not-assume-ABI.patch
# PATCH-FIX-UPSTREAM
Patch51:        multi_channel_content_detector-missing-unique_ptr.patch
# PATCH-FIX-UPSTREAM
Patch52:        process_doc_wrapper-do-not-assume-ABI.patch
%if %{with system_llvm}
Patch53:        swiftshader-use-system-llvm.patch
%endif
%if %{with system_abseil}
Patch54:        thread_annotations-fix-build-with-system-abseil.patch
%endif
#PATCH-FIX-UPSTREAM
Patch55:        json_generation-missing-unique_ptr.patch
#PATCH-FIX-UPSTREAM
Patch56:        async_shared_storage_database_impl-missing-absl-WrapUnique.patch
#PATCH-FIX-UPSTREAM
Patch57:        metrics_recorder-missing-string.patch
#PATCH-FIX-UPSTREAM
Patch58:        skia_utils-missing-uint64_t.patch
#PATCH-FIX-UPSTREAM
Patch59:        device_perf_info-missing-uint32_t.patch
# PATCH-FIX-UPSTREAM
Patch60:        dark_mode_types-uint8_t.patch
# PATCH-FIX-UPSTREAM
Patch61:        ax_property_node-missing-unique_ptr-forward.patch
# PATCH-FIX-UPSTREAM
Patch62:        attribution_manager_impl-missing-absl-WrapUnique.patch
Patch63:        system-libbsd.patch
# https://salsa.debian.org/chromium-team/chromium/-/blob/456851fc808b2a5b5c762921699994e957645917/debian/patches/upstream/nested-nested-nested-nested-nested-nested-regex-patterns.patch
Patch64:        nested-nested-nested-nested-nested-nested-regex-patterns.patch
Patch65:        base-system-nspr.patch
%if %{with clang}
BuildRequires:  clang
BuildRequires:  lld
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
BuildRequires:  cups-devel
%if %{with system_double_conversion}
BuildRequires:  double-conversion-devel
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  gn >= 0.1807
BuildRequires:  gperf
BuildRequires:  hicolor-icon-theme
# Java used during build
BuildRequires:  java-openjdk-headless
%if 0%{?fedora}
BuildRequires:  libatomic
%endif
BuildRequires:  libbsd-devel
BuildRequires:  libpng-devel
%if %{with system_tiff}
BuildRequires:  libtiff-devel
%endif
%if %{with system_nvctrl}
BuildRequires:  libXNVCtrl-devel
%endif
%if %{with system_llvm}
BuildRequires:  llvm-devel
%endif
BuildRequires:  memory-constraints
%if 0%{?suse_version}
BuildRequires:  ninja >= 1.7.2
%else
BuildRequires:  ninja-build >= 1.7.2
%endif
%if 0%{?suse_version}
BuildRequires:  nodejs16
BuildRequires:  npm16
%else
BuildRequires:  nodejs >= 16.5.0
BuildRequires:  npm
%endif
BuildRequires:  pkgconfig
BuildRequires:  python3-html5lib
BuildRequires:  rsync
BuildRequires:  snappy-devel
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  util-linux
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
BuildRequires:  pkgconfig(absl_variant)
%endif
BuildRequires:  pkgconfig(alsa)
%if %{with system_aom}
BuildRequires:  pkgconfig(aom) >= 3.4
%endif
BuildRequires:  pkgconfig(cairo) >= 1.6
%if %{with system_dav1d}
BuildRequires:  pkgconfig(dav1d) >= 1
%endif
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(flac++)
%if %{with system_freetype}
BuildRequires:  pkgconfig(freetype2)
%endif
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(gtk+-3.0)
%if %{with system_harfbuzz}
BuildRequires:  pkgconfig(harfbuzz) >= 3
%endif
%if %{with systemicu}
BuildRequires:  pkgconfig(icu-i18n) >= 68.0
%else
Provides:       bundled(icu) = 68.0
%endif
%if %{with system_jsoncpp}
BuildRequires:  pkgconfig(jsoncpp)
%endif
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat) >= 58
BuildRequires:  pkgconfig(libavutil)
%if %{with system_avif}
BuildRequires:  pkgconfig(libavif)
%endif
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
%if %{with system_cares}
BuildRequires:  pkgconfig(libcares)
%endif
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libffi)
%if %{with system_jxl}
BuildRequires:  pkgconfig(libjxl)
%endif
%if %{with system_nghttp2}
BuildRequires:  pkgconfig(libnghttp2)
%endif
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libwebp) >= 0.4.0
%if %{with system_woff2}
BuildRequires:  pkgconfig(libwoff2dec)
%endif
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.5
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(libxxhash)
%if 0%{?fedora}
BuildRequires:  minizip-compat-devel
# help decide for dependency
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  nodejs-devel >= 17
%else
BuildRequires:  pkgconfig(minizip)
%endif
BuildRequires:  pkgconfig(nspr) >= 4.9.5
BuildRequires:  pkgconfig(nss) >= 3.26
BuildRequires:  pkgconfig(ogg)
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
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500 || 0%{?fedora}
BuildRequires:  gcc >= 10
BuildRequires:  gcc-c++ >= 10
%else
BuildRequires:  gcc10
BuildRequires:  gcc10-c++
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

Obsoletes:      nodejs-electron-prebuilt < %{version}
Provides:       nodejs-electron-prebuilt = %{version}

%description
Nodejs application: Build cross platform desktop apps with JavaScript, HTML, and CSS

%package devel
Summary:        Electron development headers
Group:          Development/Libraries/C and C++
Requires:       nodejs-electron = %{version}

%description devel
Development headers for Electron projects.

%prep

# Use stable path to source to make use of ccache
%autosetup -n src -p1

patch -R -p1 < %{SOURCE400}



# Shim generators for replace_gn_files.py
cp -lv %{_sourcedir}/*.gn build/linux/unbundle/

# Fix the path to nodejs binary
mkdir -p third_party/node/linux/node-linux-x64/bin
ln -sf %{_bindir}/node third_party/node/linux/node-linux-x64/bin/node

# Fix eu-strip
rm buildtools/third_party/eu-strip/bin/eu-strip
ln -s %{_bindir}/eu-strip buildtools/third_party/eu-strip/bin/eu-strip

# Fix shim header generation
sed -i 's/OFFICIAL_BUILD/GOOGLE_CHROME_BUILD/' \
      tools/generate_shim_headers/generate_shim_headers.py

%if %{with systemicu}
find third_party/icu -type f ! -name "*.gn" -a ! -name "*.gni" -delete
%endif

%build
# GN sets lto on its own and we need just ldflag options, not cflags
%define _lto_cflags %{nil}

# Make sure python is python3
install -d -m 0755 python3-path
ln -sf %{_bindir}/python3 "$(pwd)/python3-path/python"
export PATH="$(pwd)/python3-path:${PATH}"

# Make sure node is node16 on suse
export NODE_VERSION=16



# REDUCE DEBUG as it gets TOO large
ARCH_FLAGS="$(echo %{optflags} | sed -e 's/-g /-g1 /g' -e 's/-g$/-g1/g')"


%if 0%{?fedora}
# Fix base/allocator/allocator_shim.cc:408:2: error: #error This code cannot be
# used when exceptions are turned on.
ARCH_FLAGS="$(echo $ARCH_FLAGS | sed -e 's/ -fexceptions / /g')"
%endif




# for wayland
export CXXFLAGS="${ARCH_FLAGS} -I/usr/include/wayland -I/usr/include/libxkbcommon"

export LDFLAGS="%{?build_ldflags}"



%if %{with clang}

export CFLAGS="${CXXFLAGS}"
export CC=clang
export CXX=clang++

# else with clang
%else


%ifarch %ix86 %arm
#try to reduce memory
#%%if %{with gold}
#export LDFLAGS="${LDFLAGS} -Wl,--no-map-whole-files -Wl,--no-keep-memory -Wl,--no-keep-files-mapped"
#%%else
#export LDFLAGS="${LDFLAGS} -Wl,--no-keep-memory -Wl,--hash-size=30 -Wl,--reduce-memory-overheads"
#%%endif
%endif


export CXXFLAGS="${CXXFLAGS} -Wno-return-type"
# extra flags to reduce warnings that aren't very useful
export CXXFLAGS="${CXXFLAGS} -Wno-pedantic -Wno-unused-result -Wno-unused-function -Wno-unused-variable -Wno-unused-but-set-variable -Wno-deprecated-declarations"
# ignore warnings for minor mistakes that are too common
export CXXFLAGS="${CXXFLAGS} -Wno-return-type -Wno-parentheses -Wno-misleading-indentation"
# ignore warnings that are not supported well until gcc 8
export CXXFLAGS="${CXXFLAGS} -Wno-attributes"
# ignore warnings due to gcc bug (https://gcc.gnu.org/bugzilla/show_bug.cgi?id=84055)
export CXXFLAGS="${CXXFLAGS} -Wno-ignored-attributes"
# ingore new gcc 8 warnings that aren't yet handled upstream
export CXXFLAGS="${CXXFLAGS} -Wno-address -Wno-dangling-else -Wno-packed-not-aligned"

export CFLAGS="${CXXFLAGS}"
export CXXFLAGS="${CXXFLAGS} -Wno-subobject-linkage -Wno-class-memaccess -Wno-invalid-offsetof -fpermissive"

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500 || 0%{?fedora}
export CC=gcc
export CXX=g++
%else
export CC=gcc-10
export CXX=g++-10
%endif

# endif with clang
%endif

# Needed e.g. for static library creation by base/third_party/dynamic_annotations/
export AR=ar
export NM=nm
export RANLIB=ranlib

# do not eat all memory
%limit_build -m 2600

gn_system_libraries=(
    brotli
    ffmpeg
    flac
    fontconfig
    libdrm
    libevent
    libjpeg
    libpng
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
find third_party/abseil-cpp -name *.[ch] -delete
find third_party/abseil-cpp -name *.cc -delete
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
)
rm third_party/abseil-cpp/absl/utility/BUILD.gn
%endif


%if %{with system_aom}
find third_party/libaom -name *.[ch] -delete
find third_party/libaom -name *.cc -delete
gn_system_libraries+=( libaom )
%endif

%if %{with system_avif}
find third_party/libavif -name *.[ch] -delete
gn_system_libraries+=( libavif )
%endif

%if %{with system_crc32c}
find third_party/libavif -name *.[ch] -delete
gn_system_libraries+=( crc32c )
%endif

%if %{with system_jxl}
find third_party/libjxl -name *.[ch] -delete
gn_system_libraries+=( libjxl )
%endif


%if %{with system_dav1d}
find third_party/dav1d -name *.[ch] -delete
gn_system_libraries+=( dav1d )
%endif

%if %{with system_double_conversion}
find base/third_party/double_conversion -name *.[ch] -delete
gn_system_libraries+=( double-conversion )
%endif

%if %{with system_nvctrl}
find third_party/angle/src/third_party/libXNVCtrl/ -name *.[ch] -delete
gn_system_libraries+=( libXNVCtrl )
%endif

%if %{with system_spirv}
rm -rv third_party/swiftshader/third_party/SPIRV-Headers/include
find  third_party/swiftshader/third_party/SPIRV-Tools/ -name *.[ch] -delete
find  third_party/swiftshader/third_party/SPIRV-Tools/ -name *.[ch]pp -delete
rm -rv third_party/vulkan-deps/spirv-headers/src/include
find third_party/vulkan-deps/spirv-tools/ -name *.[ch] -delete
find third_party/vulkan-deps/spirv-tools/ -name *.[ch]pp -delete

gn_system_libraries+=( 
   swiftshader-SPIRV-Headers
   swiftshader-SPIRV-Tools
#The following can only be unbundled if you don't build DAWN (WebGPU)
   vulkan-SPIRV-Headers
   vulkan-SPIRV-Tools
)
%endif

%if %{with system_harfbuzz}
find third_party/harfbuzz-ng -name *.[ch] \! -path "third_party/harfbuzz-ng/utils/hb_scoped.h" -delete
find third_party/harfbuzz-ng -name *.cc -delete
find third_party/harfbuzz-ng -name *.hh -delete
gn_system_libraries+=( harfbuzz-ng )
%endif

%if %{with system_freetype}
find third_party/freetype -name *.[ch] -delete
gn_system_libraries+=( freetype )
%endif

%if %{with systemicu}
gn_system_libraries+=( icu )
%endif

%if %{with system_vpx}
find third_party/libvpx -name *.[ch] -delete
gn_system_libraries+=( libvpx )
%endif

%if %{with system_woff2}
find third_party/woff2 -name *.[ch] -delete
find third_party/woff2 -name *.cc -delete
gn_system_libraries+=( woff2 )
%endif

build/linux/unbundle/replace_gn_files.py --system-libraries ${gn_system_libraries[@]}

%if %{with system_cares}
find third_party/electron_node/deps/cares -name *.[ch] -delete
%endif

%if %{with system_nghttp2}
find third_party/electron_node/deps/nghttp2 -name *.[ch] -delete
%endif

%if %{with system_llvm}
rm -rf third_party/swiftshader/third_party/llvm-10.0
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
%endif
%ifarch %arm
myconf_gn+=" host_cpu=\"arm\""
# Disable requirement of neon instructions
myconf_gn+="  arm_use_neon=false"
%endif
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
# symbol_level=2 is full debug
# symbol_level=1 is enough info for stacktraces
# symbol_level=0 disable debug
myconf_gn+=" symbol_level=1"
myconf_gn+=" blink_symbol_level=0"
myconf_gn+=" use_kerberos=true"
myconf_gn+=" enable_vr=false"
myconf_gn+=" optimize_webui=false"
myconf_gn+=" enable_reading_list=false"
myconf_gn+=" enable_reporting=false"
myconf_gn+=" build_with_tflite_lib=false"
myconf_gn+=" safe_browsing_mode=0"

#Do not build Chromecast
myconf_gn+=" enable_openscreen=false"
myconf_gn+=" enable_media_remoting=false"


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
%if %{with system_harfbuzz}
myconf_gn+=" use_system_harfbuzz=true"
%endif
%if %{with system_freetype}
myconf_gn+=" use_system_freetype=true"
%endif
%if %{with system_cares}
myconf_gn+=" use_system_cares=true"
%endif
%if %{with system_nghttp2}
myconf_gn+=" use_system_nghttp2=true"
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
myconf_gn+=" use_thin_lto=false"

%if %{without clang}
myconf_gn+=" gcc_lto=true"
%endif

# endif with lto
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
ninja -v %{?_smp_mflags} -C out/Release electron
ninja -v %{?_smp_mflags} -C out/Release copy_headers


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
popd

%if %{without systemicu}
rsync -av third_party/icu/common/icudtl.dat %{buildroot}%{_libdir}/electron/
%endif

echo -n "%{version}" > %{buildroot}%{_libdir}/electron/version

# Install folders required for webapps
mkdir -p "%{buildroot}%{_sysconfdir}/webapps"
mkdir -p "%{buildroot}%{_datadir}/webapps"

rsync -av out/Release/gen/node_headers/include/node/* %{buildroot}%{_includedir}/electron

%files
%license electron/LICENSE
%doc electron/README.md
%{_bindir}/electron
%{_datadir}/pixmaps/electron.png
%{_datadir}/icons/hicolor/symbolic/apps/electron-symbolic.svg
%{_datadir}/applications/electron.desktop


%{_libdir}/electron/

%dir %{_sysconfdir}/webapps
%dir %{_datadir}/webapps

%files devel
%{_includedir}/electron

%changelog
