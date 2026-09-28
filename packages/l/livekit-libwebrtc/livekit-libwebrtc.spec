#
# spec file for package livekit-libwebrtc
#
# Copyright (c) 2026 SUSE LLC
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


%global commit_short 0001d84
%global lkdir        %{_libdir}/livekit-webrtc
%global outdir       out/Release
%global sover        137
%global soname       libwebrtc-suse.so.%{sover}
%global libpkg       libwebrtc-suse%{sover}
%global vernode      LIVEKIT_WEBRTC_%{sover}_%{commit_short}
%ifarch x86_64
%global gn_target_cpu x64
%endif
%ifarch aarch64
%global gn_target_cpu arm64
%endif
Name:           livekit-libwebrtc
Version:        137.0+git20251012.0001d84
Release:        0
Summary:        LiveKit's build of WebRTC (M137) as a shared library
# Everything statically linked is permissive; the per-component breakdown, and
# why generate_licenses.py still lists the unbundled and host-only ones, is in
# README.SUSE-maint.
# Legal-Review-Notice: dav1d, ffmpeg, libaom, libjpeg-turbo, libvpx, openh264,
# opus and zlib come from the distribution and carry no source in the tarball,
# so none of their licences - ffmpeg's LGPL/GPL included - applies here.
# protobuf builds host code generators only (rtc_enable_protobuf=false, no
# google::protobuf symbol is exported).
License:        Apache-2.0 AND BSD-3-Clause AND HPND AND SUSE-Public-Domain
URL:            https://github.com/webrtc-sdk/webrtc
# No upstream tarball exists for a gclient checkout; Source1 regenerates it.
Source0:        webrtc-m137-%{commit_short}.tar.zst
Source1:        make-source.sh
# From livekit/rust-sdks webrtc-sys/libwebrtc/boringssl_prefix_symbols.txt.
Source2:        boringssl_prefix_symbols.txt
Source3:        README.SUSE-maint
Source4:        libwebrtc.version
# PATCH-FIX-OPENSUSE add_licenses.patch -- from livekit/rust-sdks webrtc-sys/libwebrtc/patches: entries generate_licenses.py needs for deps it does not know
Patch0:         add_licenses.patch
# PATCH-FIX-OPENSUSE ssl_verify_callback_with_native_handle.patch -- from livekit/rust-sdks webrtc-sys/libwebrtc/patches: hand the native SSL* to a custom certificate verifier
Patch1:         ssl_verify_callback_with_native_handle.patch
# PATCH-FIX-OPENSUSE add_deps.patch -- from livekit/rust-sdks webrtc-sys/libwebrtc/patches: add zlib, log sinks, the simulcast encoder adapter and the frame crypto transformer to :default
Patch2:         add_deps.patch
# PATCH-FIX-OPENSUSE disable_crel.patch -- from livekit/rust-sdks webrtc-sys/libwebrtc/patches: CREL relocations segfault on aarch64, crbug.com/376278218
Patch3:         disable_crel.patch
# PATCH-FIX-OPENSUSE david_disable_gun_source_macro.patch -- from livekit/rust-sdks webrtc-sys/libwebrtc/patches: dav1d defines _GNU_SOURCE only for gcc on x86/x64
Patch4:         david_disable_gun_source_macro.patch
# PATCH-FIX-OPENSUSE force_gcc.patch -- from livekit/rust-sdks webrtc-sys/libwebrtc/patches, extended here with the distribution hardening flags
Patch5:         force_gcc.patch
# PATCH-FIX-OPENSUSE chromium-129-rust.patch -- from nixpkgs pkgs/by-name/li/livekit-libwebrtc: drop the clang compiler_builtins config, no compiler-rt available
Patch6:         chromium-129-rust.patch
# PATCH-FIX-OPENSUSE pipewire-1.5-rebased.patch -- from nixpkgs pkgs/by-name/li/livekit-libwebrtc, rebased: spa/pod/iter.h include for PipeWire >= 1.5.81
Patch7:         pipewire-1.5-rebased.patch
# PATCH-FIX-OPENSUSE native-gcc-toolchain.patch -- as nixpkgs does: the arm64 gcc toolchain hard-codes a cross tool prefix
Patch8:         native-gcc-toolchain.patch
# PATCH-FIX-OPENSUSE generate-licenses-system-gn.patch -- depot_tools is not packaged and not in the tarball
Patch9:         generate-licenses-system-gn.patch
# PATCH-FIX-OPENSUSE shared-library.patch -- after nixpkgs 0001-shared-libraries.patch: build one shared library instead of a static archive
Patch10:        shared-library.patch
# PATCH-FIX-OPENSUSE system-openh264-shim.patch -- rtc_system_openh264=true leaves h264_encoder_impl.h including the in-tree header path, which needs the unbundle shim as a dependency
Patch11:        system-openh264-shim.patch
# PATCH-FIX-OPENSUSE h265-optional-in-frame-cryptor.patch -- livekit's frame cryptor calls the H.265 parsers unguarded, so rtc_use_h265=false does not link
Patch12:        h265-optional-in-frame-cryptor.patch
BuildRequires:  cpio
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gn
BuildRequires:  memory-constraints
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  zstd
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(openh264)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
# The gn graph and the header set were verified for these two only.
ExclusiveArch:  x86_64 aarch64

%description
WebRTC (milestone 137) from the webrtc-sdk fork, built the way the LiveKit
Rust SDK builds it: one shared library plus the matching header tree.

%package -n %{libpkg}
Summary:        LiveKit's build of WebRTC (M137) as a shared library
# Statically linked into the library; revisions from gclient_entries.txt and
# the per-component README.chromium.
Provides:       bundled(abseil-cpp) = e5e2a9d
Provides:       bundled(boringssl) = 34492c8
Provides:       bundled(crc32c) = d3d60ac
Provides:       bundled(libsrtp) = fd08747
Provides:       bundled(libyuv) = 1908
Provides:       bundled(perfetto) = a54dd38
Provides:       bundled(pffft) = 483453d
Provides:       bundled(rnnoise) = 91ef401
Provides:       bundled(sigslot)

%description -n %{libpkg}
WebRTC (milestone 137) from the webrtc-sdk fork, built the way the LiveKit
Rust SDK builds it.

The BoringSSL linked into this library carries an LK_ symbol prefix so that it
can neither interpose nor be interposed by the system OpenSSL in a process that
loads both. The bundled abseil needs no such treatment: Chromium builds it
without upstream's lts_ inline namespace, so its symbols cannot collide with
the distribution's.

The soname is SUSE-specific because upstream publishes no shared library and
no soname; its number follows the WebRTC milestone. The C++ ABI changes with
every snapshot inside a milestone, which the LIVEKIT_WEBRTC_<milestone>_<commit>
symbol version node makes explicit, so a consumer only loads against the
snapshot it was built with.

%package devel
Summary:        Development files for LiveKit's build of WebRTC (M137)
Requires:       %{libpkg} = %{version}-%{release}
# webrtc-sys' build.rs pkg-config-probes these; everything else WebRTC uses is
# reached through dlopen stubs.
Requires:       pkgconfig(gio-2.0)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gobject-2.0)

%description devel
The header tree and link symlink consumed by the LiveKit Rust SDK's webrtc-sys
crate, which the Zed editor uses for its calls feature.

Point webrtc-sys at it with

    LK_CUSTOM_WEBRTC=%{lkdir}

That directory holds lib/libwebrtc.so, include/, webrtc.ninja,
desktop_capture.ninja and args.gn; webrtc-sys reads the first line of the two
.ninja files to re-apply this build's preprocessor defines to its own C++ shim.
It also has to be told to link the library dynamically, which it does not do by
itself:

    cargo:rustc-link-lib=static=webrtc -> cargo:rustc-link-lib=dylib=webrtc

Because the API and ABI change with every WebRTC snapshot, a consumer has to
require this exact version at build time and be rebuilt on every bump.

%prep
%autosetup -p1 -n webrtc-m137-%{commit_short}
cp -a %{SOURCE1} %{SOURCE3} .
chmod 0644 make-source.sh
cp -a %{SOURCE4} src/libwebrtc.version
sed -i 's/@SHORT@/%{commit_short}/' src/libwebrtc.version
sed -i 's/@SONAME@/%{soname}/' src/BUILD.gn
# vpython3 is not packaged and the gn scripts run under plain python3.
sed -i 's/script_executable = "vpython3"/script_executable = "python3"/' src/.gn
python3 src/build/linux/unbundle/replace_gn_files.py --system-libraries \
    dav1d ffmpeg libaom libjpeg libvpx openh264 opus zlib
# The zlib shim also declares Chromium's minizip and zip wrappers; zip pulls in
# //base, which is not part of a WebRTC checkout, and nothing here uses either.
sed -i '/^shim_headers("minizip_shim")/,$d' src/third_party/zlib/BUILD.gn

%build
%limit_build -m 1200
# The gn arg list and why each non-default one is set: README.SUSE-maint.
gn gen %{outdir} --root=src --args='
  is_debug=false
  target_os="linux"
  target_cpu="%{gn_target_cpu}"
  rtc_enable_protobuf=false
  treat_warnings_as_errors=false
  use_custom_libcxx=false
  use_llvm_libatomic=false
  use_libcxx_modules=false
  use_custom_libcxx_for_host=false
  rtc_include_tests=false
  rtc_build_tools=false
  rtc_build_examples=false
  rtc_libvpx_build_vp9=true
  enable_libaom=true
  is_component_build=true
  rtc_enable_symbol_export=true
  rtc_use_h264=true
  rtc_system_openh264=true
  rtc_use_h265=false
  rtc_use_pipewire=true
  symbol_level=1
  enable_iterator_debugging=false
  use_rtti=true
  rtc_use_x11=true
  use_sysroot=false
  is_clang=false
  use_dummy_lastchange=true'

ninja -C %{outdir} -t commands :default 2>/dev/null | grep -m1 'rtc_base.*\.cc' || :
ninja %{?_smp_mflags} -C %{outdir} :default

# livekit's list stops at BoringSSL as of m114; extend it with the other C
# symbols the objects define.  Mangled names are left alone: those objects also
# carry libstdc++ vague-linkage symbols, which need one address per process.
syms=$(pwd)/%{outdir}/boringssl_syms.txt
awk '!/^#/ && NF == 2' %{SOURCE2} > "$syms"
nm -g --defined-only $(find %{outdir}/obj/third_party/boringssl -name '*.o') |
    awk 'NF == 3 && $3 ~ /^[A-Za-z][A-Za-z0-9_]*$/ && $3 !~ /^LK_/ { print $3 }' |
    sort -u |
    awk 'NR == FNR { known[$1]; next } !($1 in known) { print $1, "LK_" $1 }' "$syms" - \
    >> "$syms"
echo "BoringSSL symbols to rename: $(wc -l < "$syms")"

# objcopy cannot rename dynamic symbols, so the renaming happens on the objects
# and the library is linked again.  Restoring each mtime keeps ninja from
# deciding the objects are stale and recompiling them over the renamed ones.
find %{outdir}/obj -name '*.o' -print0 |
    xargs -0 -r -n 1 -P %{?jobs}%{!?jobs:1} sh -c '
        touch -r "$1" "$1.mt" &&
        objcopy --redefine-syms="$0" "$1" &&
        touch -r "$1.mt" "$1"
        rm -f "$1.mt"' "$syms"
find %{outdir} -name '*.a' -delete
rm -f %{outdir}/libwebrtc.so
ninja %{?_smp_mflags} -C %{outdir} :default

python3 src/tools_webrtc/libs/generate_licenses.py --target :default %{outdir} %{outdir}

%install
install -D -m 0755 %{outdir}/libwebrtc.so %{buildroot}%{_libdir}/%{soname}
install -d %{buildroot}%{lkdir}/lib %{buildroot}%{lkdir}/include
ln -s ../../%{soname} %{buildroot}%{lkdir}/lib/libwebrtc.so
install -m 0644 %{outdir}/obj/webrtc.ninja %{buildroot}%{lkdir}/
install -m 0644 %{outdir}/obj/modules/desktop_capture/desktop_capture.ninja %{buildroot}%{lkdir}/
install -m 0644 %{outdir}/args.gn %{buildroot}%{lkdir}/
# The include closure of webrtc-sys' C++ shim, verified by preprocessing it
# against exactly this set; the rest of the tree is not compiled against.
cd src
for d in api audio call common_audio common_video logging media modules net \
         p2p pc rtc_base sdk stats system_wrappers video \
         third_party/abseil-cpp third_party/libyuv/include \
         third_party/boringssl/src/include third_party/perfetto/include; do
    find "$d" \( -name '*.h' -o -name '*.inc' \) -print
done | grep -vE '^(modules/third_party/portaudio|rtc_base/third_party/base64)/' |
    cpio -pd --quiet %{buildroot}%{lkdir}/include
cd ..
find %{buildroot}%{lkdir}/include -type f -exec chmod 0644 {} +
find %{buildroot}%{lkdir}/include -type d -exec chmod 0755 {} +
%fdupes %{buildroot}%{lkdir}/include

%check
cd %{outdir}
nm -D --defined-only libwebrtc.so | awk 'NF == 3 { print $3 }' > exported.txt
echo "exported symbols:           $(wc -l < exported.txt)"
echo "webrtc:: symbols:           $(grep -c 6webrtc exported.txt)"
echo "LK_-prefixed BoringSSL:     $(grep -c '^LK_' exported.txt)"
echo "unprefixed SSL_ EVP_ CRYPTO_ X509_: $(grep -cE '^(SSL|EVP|CRYPTO|X509)_' exported.txt)"
echo "exported main():            $(grep -cx main exported.txt)"
echo "exported pw_ spa_:          $(grep -cE '^(pw|spa)_' exported.txt)"
echo "openh264 Wels symbols:      $(grep -c '^Wels' exported.txt)"
echo "absl-owned exports:         $(grep -cE '^(_Z[A-Z]*N4absl|_ZGVZN4absl|_ZZN4absl|Absl)' exported.txt)"
echo "absl LTS-namespaced:        $(grep -c 'lts_20' exported.txt)"
echo "perfetto-owned exports:     $(grep -cE '^(_Z[A-Z]*N8perfetto|_ZGVZN8perfetto|_ZZN8perfetto)' exported.txt)"
echo "ffmpeg ff_ symbols:         $(grep -c '^ff_' exported.txt)"
test "$(grep -c 6webrtc exported.txt)" -gt 1000
test "$(grep -c '^LK_' exported.txt)" -gt 1000
test "$(grep -cE '^(SSL|EVP|CRYPTO|X509)_' exported.txt)" -eq 0
test "$(grep -cx main exported.txt)" -eq 0
test "$(grep -cE '^(pw|spa)_' exported.txt)" -eq 0
test "$(grep -c '^Wels' exported.txt)" -eq 0
# Chromium builds abseil with ABSL_OPTION_USE_INLINE_NAMESPACE 0 while the
# distribution keeps upstream's lts_ namespace, so the two symbol sets cannot
# collide and ours must carry no lts_ name.
test "$(grep -c 'lts_20' exported.txt)" -eq 0
test "$(grep -cE '^(_Z[A-Z]*N8perfetto|_ZGVZN8perfetto|_ZZN8perfetto)' exported.txt)" -eq 0
test "$(grep -c '^ff_' exported.txt)" -eq 0
rm exported.txt
readelf -d libwebrtc.so | grep -E 'SONAME|NEEDED'
readelf -d libwebrtc.so | grep -q 'SONAME.*%{soname}'
for l in libavcodec libavutil libopenh264 libvpx libaom libdav1d libopus libjpeg; do
    readelf -d libwebrtc.so | grep -q "NEEDED.*$l"
done
! ldd libwebrtc.so | grep -q 'not found'
! readelf -d libwebrtc.so | grep -qE 'RPATH|RUNPATH'
# The version node is what makes a snapshot mismatch a load-time error.
readelf -V libwebrtc.so | grep -q '%{vernode}'
# webrtc-sys re-applies the defines on the first line of these two files;
# WEBRTC_USE_X11 only ever appears in desktop_capture.ninja.
grep -q WEBRTC_USE_PIPEWIRE obj/webrtc.ninja
grep -q WEBRTC_USE_X11 obj/modules/desktop_capture/desktop_capture.ninja
# Nothing copyleft may reach the licence file.
! grep -q 'GNU GENERAL PUBLIC LICENSE' LICENSE.md
! grep -q 'GNU LESSER GENERAL PUBLIC LICENSE' LICENSE.md

%ldconfig_scriptlets -n %{libpkg}

%files -n %{libpkg}
%license src/LICENSE src/PATENTS %{outdir}/LICENSE.md
%{_libdir}/%{soname}

%files devel
%license src/LICENSE src/PATENTS
%doc README.SUSE-maint make-source.sh gclient_entries.txt
%dir %{lkdir}
%dir %{lkdir}/lib
%{lkdir}/lib/libwebrtc.so
%{lkdir}/include
%{lkdir}/webrtc.ninja
%{lkdir}/desktop_capture.ninja
%{lkdir}/args.gn

%changelog
