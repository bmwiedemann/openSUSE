#
# spec file for package chromium
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2024 Callum Farmer <gmbr3@opensuse.org>
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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
%define outputdir out
# bsc#1108175
%define __provides_exclude ^lib.*\\.so.*$
%define __requires_exclude ^libffmpeg\\.so.*$
# suse_version 1500 all of sle code 15, all of leap15
# suse_version 1600 all of alp, slfo
# suse_version 1699 tw
%if 0%{?suse_version} >= 1600 || 0%{?sle_version} >= 150400
%bcond_without gtk4
%else
%bcond_with gtk4
%endif
%ifarch aarch64 ppc64le riscv64
# ERROR Unresolved dependencies.
# //third_party/swiftshader/src/Reactor:swiftshader_reactor(//build/toolchain/linux/unbundle:default)
#   needs //third_party/swiftshader/src/Reactor:swiftshader_subzero_reactor(//build/toolchain/linux/unbundle:default)
%bcond_with swiftshader
%else
%bcond_without swiftshader
%endif
%if 0%{?suse_version} >= 1600
%bcond_with system_harfbuzz
%bcond_without system_freetype
%bcond_without arm_bti
# ERROR Unresolved dependencies.
# //chrome/browser/ui/lens:unit_tests(//build/toolchain/linux/unbundle:default)
#   needs //third_party/icu:icuuc_public(//build/toolchain/linux/unbundle:default)
%bcond_with system_icu
%bcond_without qt6
%bcond_without system_ffmpeg
%else
%bcond_with system_harfbuzz
%bcond_with system_freetype
%bcond_with arm_bti
%bcond_with system_icu
%bcond_without qt6
%bcond_with system_ffmpeg
%endif
%bcond_without noopenh264
%define ffmpeg_version 59
%bcond_with system_zstd
%if 0%{?suse_version} > 1600
# LLVM version
%define llvm_version 21
%define llvm_version_long 21.1.8
# RUST version
%define rust_version 1.93
%else
# LLVM version
%define llvm_version 19
%define llvm_version_long 19.1.7
# RUST version
%define rust_version 1.92
%endif
# GCC version
%define gcc_version 14
# minimal esbuild version
%define esbuild_version 0.25.1
# minimal gn version
%define gn_version 0.20251217
# local rollup override to run without binaries
%define rollup_version 3.29.5
%if 0%{?suse_version} <= 1699
%bcond_with system_webp
%bcond_with system_re2
%else
%bcond_without system_webp
%bcond_without system_re2
%endif
%bcond_with is_beta # CHANNEL SWITCH
%bcond_with system_avif
# Compiler
%bcond_without clang
# libstdc++ or libc++
%bcond_with libstdcpp
# Chromium built with GCC 11 and LTO enabled crashes (boo#1194055)
%bcond_without lto
%bcond_without pipewire
%bcond_with system_zlib
%bcond_with system_vpx
%if %{pkg_vcmp libxml2-devel >= 2.12}
%bcond_without libxml2_2_12
%else
%bcond_with libxml2_2_12
%endif
%if %{pkg_vcmp libxml2-devel >= 2.13}
%bcond_without libxml2_2_13
%else
%bcond_with libxml2_2_13
%endif
%if %{pkg_vcmp gtk4-devel >= 4.19}
%bcond_without gtk4_4_19
%else
%bcond_with gtk4_4_19
%endif
%if %{pkg_vcmp flac-devel >= 1.5.0}
%bcond_without flac_1_5
%else
%bcond_with flac_1_5
%endif
# Package names
%if %{with is_beta}
%define chromedriver_name %{name}-chromedriver
%define n_suffix -beta
%else
%define chromedriver_name chromedriver
%define n_suffix %{nil}
%endif
# official builds have less debugging and go faster... but we have to shut some things off.
%global official_build 1

Name:           chromium%{n_suffix}
Version:        145.0.7632.116
Release:        0
Summary:        Google's open source browser project
License:        BSD-3-Clause AND LGPL-2.1-or-later
URL:            https://www.chromium.org/
Source0:        https://github.com/chromium-linux-tarballs/chromium-tarballs/releases/download/%{version}/chromium-%{version}-linux.tar.xz
NoSource:       0
# https://github.com/evanw/esbuild/archive/refs/tags/v%%{esbuild_version}.tar.gz
Source1:        esbuild-%{esbuild_version}.tar.gz
Source2:        esbuild-%{esbuild_version}-vendor.tar.gz
Source3:        README.openSUSE
# upstream only contains x86 binary of 4.x, other archs do not work reliably
# try to use an old version like in debian package
Source4:        https://registry.npmjs.org/rollup/-/rollup-%{rollup_version}.tgz
# Toolchain definitions
Source30:       master_preferences
Source104:      chromium-symbolic.svg
# https://source.chromium.org/chromium/chromium/src/+/refs/tags/%%{version}:chrome/installer/linux/common/installer.include
Source105:      INSTALL.sh
#
Source106:      chrome-wrapper
# global patches
Patch0:         chromium-libusb_interrupt_event_handler.patch
# PATCH-FIX-OPENSUSE Make the 1-click-install ymp file always download [bnc#836059]
Patch1:         exclude_ymp.patch
# PATCH-FIX-OPENSUSE enables reading of the master preference
Patch2:         chromium-master-prefs-path.patch
# PATCH-FIX-OPENSUSE fix_building_widevinecdm_with_chromium.patch - Enable WideVine plugin
Patch3:         fix_building_widevinecdm_with_chromium.patch
Patch4:         chromium-buildname.patch
Patch6:         gcc-enable-lto.patch
# Do not use unrar code, it is non-free
Patch7:         chromium-norar.patch
Patch9:         system-libdrm.patch
# gentoo/fedora/arch patchset
Patch15:        chromium-125-compiler.patch
Patch98:        chromium-102-regex_pattern-array.patch
# PATCH-FIX-SUSE: allow prop codecs to be set with chromium branding
Patch202:       chromium-prop-codecs.patch
Patch240:       chromium-117-string-convert.patch
Patch261:       chromium-121-rust-clang_lib.patch
Patch337:       chromium-123-missing-QtGui.patch
Patch359:       chromium-126-quiche-interator.patch
Patch360:       chromium-127-bindgen.patch
Patch361:       chromium-127-rust-clanglib.patch
Patch363:       chromium-127-constexpr.patch
Patch364:       chromium-129-revert-AVFMT_FLAG_NOH264PARSE.patch
Patch368:       chromium-131-clang-stack-protector.patch
Patch369:       chromium-132-pdfium-explicit-template.patch
Patch371:       chromium-133-bring_back_and_disable_allowlist.patch
Patch373:       chromium-134-type-mismatch-error.patch
Patch375:       chromium-131-fix-qt-ui.pach
Patch377:       chromium-139-deterministic.patch
Patch380:       chromium-141-use_libcxx_modules.patch
Patch381:       chromium-141-csss_style_sheet.patch
Patch382:       chromium-141-no_cxx_modules.patch
Patch385:       chromium-142-rust_no_sanitize.patch
Patch386:       chromium-143-libpng-unbundle.patch
Patch387:       chromium-143-cookie_string_view.patch
Patch389:       chromium-143-revert_rust_is_multiple_of.patch
Patch390:       chromium-144-revert_gfx_value_or.patch
Patch391:       chromium-145-blink_missing_include.patch
Patch392:       chromium-145-use_unrar.patch
Patch393:       force-rust-nightly.patch
Patch394:       chromium-145-swiftshader-missing-include.patch
# conditionally applied patches ppc64le only
# where applicable patch numbers from fedora specfile + 100
Patch400:       chromium-141-glibc-2.42-SYS_SECCOMP.patch
Patch402:       ppc-fedora-memory-allocator-dcheck-assert-fix.patch
# similar to patch 483 but in llvm-10 tree
# so we do not use chromium-143-swiftshader-llvm-16.0.patch
Patch403:       0001-swiftshader-fix-build-llvm10.patch
#
Patch459:       ppc-fedora-add-ppc64-architecture-string.patch
Patch461:       ppc-fedora-0001-sandbox-Enable-seccomp_bpf-for-ppc64.patch
#
Patch476:       ppc-fedora-0001-third_party-angle-Include-missing-header-cstddef-in-.patch
Patch477:       ppc-fedora-0001-Add-PPC64-support-for-boringssl.patch
Patch478:       ppc-fedora-0001-third_party-libvpx-Properly-generate-gni-on-ppc64.patch
Patch480:       ppc-fedora-0001-third_party-pffft-Include-altivec.h-on-ppc64-with-SI.patch
Patch481:       ppc-fedora-0002-Add-PPC64-generated-files-for-boringssl.patch
Patch482:       ppc-fedora-0002-third_party-lss-kernel-structs.patch
#
Patch483:       ppc-fedora-0001-swiftshader-fix-build.patch
#
Patch484:       ppc-fedora-Rtc_base-system-arch.h-PPC.patch
#
Patch486:       ppc-fedora-0004-third_party-crashpad-port-curl-transport-ppc64.patch
#
Patch487:       ppc-fedora-HACK-third_party-libvpx-use-generic-gnu.patch
Patch489:       ppc-fedora-HACK-debian-clang-disable-base-musttail.patch
Patch490:       ppc-fedora-HACK-debian-clang-disable-pa-musttail.patch
Patch491:       ppc-fedora-0001-Add-ppc64-target-to-libaom.patch
Patch492:       ppc-fedora-0001-Add-pregenerated-config-for-libaom-on-ppc64.patch
#
Patch493:       ppc-fedora-0002-third_party-libvpx-Remove-bad-ppc64-config.patch
Patch494:       ppc-fedora-0003-third_party-libvpx-Add-ppc64-generated-config.patch
#
Patch495:       ppc-fedora-0004-third_party-libvpx-work-around-ambiguous-vsx.patch
#
Patch496:       ppc-fedora-skia-vsx-instructions.patch
#
Patch497:       ppc-fedora-0001-Implement-support-for-ppc64-on-Linux.patch
Patch498:       ppc-fedora-0001-Implement-support-for-PPC64-on-Linux.patch
Patch499:       ppc-fedora-0001-Force-baseline-POWER8-AltiVec-VSX-CPU-features-when-.patch
Patch501:       ppc-fedora-fix-rustc.patch
Patch502:       ppc-fedora-fix-rust-linking.patch
Patch503:       ppc-fedora-fix-breakpad-compile.patch
Patch504:       ppc-fedora-fix-partition-alloc-compile.patch
Patch505:       ppc-fedora-fix-study-crash.patch
Patch507:       ppc-fedora-fix-different-data-layouts.patch
Patch508:       ppc-fedora-0002-Add-ppc64-trap-instructions.patch
#
Patch509:       ppc-fedora-fix-page-allocator-overflow.patch
Patch510:       ppc-fedora-0001-Enable-ppc64-pointer-compression.patch
#
Patch511:       ppc-fedora-dawn-fix-ppc64le-detection.patch
Patch512:       ppc-fedora-add-ppc64-architecture-to-extensions.diff
#
Patch513:       ppc-fedora-fix-unknown-warning-option-messages.diff
Patch515:       ppc-fedora-add-ppc64-pthread-stack-size.patch
#
Patch517:       ppc-fedora-0001-add-xnn-ppc64el-support.patch
# https://src.fedoraproject.org/rpms/chromium/blob/rawhide/f/0002-regenerate-xnn-buildgn.patch
Patch518:       ppc-fedora-0002-regenerate-xnn-buildgn.patch
Patch519:       ppc-fedora-0009-sandbox-ignore-byte-span-error.patch
# fedora does this in chromium-144-rust-clanglib.patch
# while we do this without ppc in chromium-121-rust-clang_lib.patch
Patch550:       ppc-chromium-136-clang-config.patch
# from debian
Patch551:       ppc-debian-0003-third_party-ffmpeg-Add-ppc64-generated-config.patch
# conditionally applied patches
# patch where libxml < 2.12
Patch1010:      chromium-124-system-libxml.patch
# patch where libxml < 2.13
Patch1011:      chromium-144-revert-libxml-2.13.patch
# gtk4 is too old
Patch1040:      gtk-414.patch
Patch1041:      gtk-414-2.patch
# flac is too old
Patch1050:      chromium-140-old-flac.patch
# revert upstream patch ending in compile error
# error: static assertion expression is not an integral constant expression
Patch1060:       chromium-24264eefbfd3464161764f31a2752c5327719452.patch
Patch1061:       chromium-4f46f03a6c6d4c6efc1ad5d0d78030d02326f967.patch
Patch1080:       rollup.patch

# end conditionally applied patches
BuildRequires:  SDL-devel
BuildRequires:  bison
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  elfutils
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  git
BuildRequires:  gn >= %{gn_version}
BuildRequires:  gperf
BuildRequires:  hicolor-icon-theme
BuildRequires:  golang(API)
# Java used during build
BuildRequires:  java-openjdk-headless
BuildRequires:  libdc1394
BuildRequires:  libgcrypt-devel
BuildRequires:  libgsm-devel
BuildRequires:  libjpeg-devel >= 8.1
BuildRequires:  libpng-devel
BuildRequires:  memory-constraints
BuildRequires:  nasm
BuildRequires:  ninja >= 1.7.2
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
%if 0%{?suse_version} >= 1600 || 0%{?sle_version} >= 150700
BuildRequires:  nodejs-default
%else
BuildRequires:  nodejs22
%endif
%if 0%{?suse_version} >= 1600
BuildRequires:  python3
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
%else
BuildRequires:  python311
BuildRequires:  python311-setuptools
BuildRequires:  python311-six
%endif
BuildRequires:  snappy-devel
BuildRequires:  util-linux
BuildRequires:  wdiff
BuildRequires:  perl(Switch)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo) >= 1.6
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dirac) >= 1.0.0
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(form)
BuildRequires:  pkgconfig(formw)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(kadm-client)
BuildRequires:  pkgconfig(kdb)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdc1394-2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.5
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(menu)
BuildRequires:  pkgconfig(menuw)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(ncurses++)
BuildRequires:  pkgconfig(ncurses++w)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(nspr) >= 4.9.5
BuildRequires:  pkgconfig(nss) >= 3.26
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus) >= 1.3.1
BuildRequires:  pkgconfig(panel)
BuildRequires:  pkgconfig(panelw)
BuildRequires:  pkgconfig(schroedinger-1.0)
BuildRequires:  pkgconfig(slang)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(theora) >= 1.1
BuildRequires:  pkgconfig(tic)
BuildRequires:  pkgconfig(tinfo)
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbcommon) >= 1.0.0
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
# BEG add rust BR
BuildRequires:  cargo%{rust_version}
BuildRequires:  rust%{rust_version}
# END add rust BR
BuildRequires:  rust-bindgen >= 0.71
Requires:       xdg-utils
Requires(pre):  permissions
Recommends:     noto-coloremoji-fonts
Conflicts:      chromium-browser
Provides:       %{name}-suid-helper = %{version}
Provides:       chromium-based-browser = %{version}
Provides:       chromium-browser = %{version}
Provides:       web_browser
Obsoletes:      %{name}-suid-helper < %{version}
Obsoletes:      chromium-beta-desktop-gnome < %{version}
Obsoletes:      chromium-beta-desktop-kde < %{version}
Obsoletes:      chromium-browser < %{version}
Obsoletes:      chromium-desktop-gnome < %{version}
Obsoletes:      chromium-desktop-kde < %{version}
Obsoletes:      chromium-dev-desktop-gnome < %{version}
Obsoletes:      chromium-dev-desktop-kde < %{version}
Obsoletes:      chromium-ffmpeg < %{version}
Obsoletes:      chromium-ffmpegsumo < %{version}
# no 32bit supported and it takes ages to build
ExclusiveArch:  x86_64 aarch64 riscv64 ppc64le
%if 0%{?suse_version} <= 1500
BuildRequires:  pkgconfig(glproto)
%endif
%if %{with pipewire}
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libspa-0.2)
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
%if %{with system_freetype}
BuildRequires:  pkgconfig(freetype2)
%endif
%if %{with system_zlib}
BuildRequires:  pkgconfig(zlib)
%endif
%if %{with noopenh264}
BuildRequires: pkgconfig(openh264)
%endif
%if %{with gtk4}
BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(gtk4)
%else
BuildRequires:  pkgconfig(gtk+-3.0)
%endif
%if %{with system_ffmpeg}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat) >= %{ffmpeg_version}
BuildRequires:  pkgconfig(libavutil)
%endif
%if %{with system_avif}
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libyuv)
%endif
%if %{with qt6}
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
%endif
%if %{with system_re2}
BuildRequires:  pkgconfig(re2) >= 11
%endif
%if %{with system_webp}
BuildRequires:  pkgconfig(libwebp) >= 0.4.0
%endif
%if %{with system_zstd}
BuildRequires:  pkgconfig(libzstd) >= 1.5.5
%endif
# compiler selection
%if %{with clang}
# clang/llvm case
BuildRequires:  clang%{llvm_version}
%if %{with libstdcpp}
BuildRequires:  libstdc++6-devel-gcc%{gcc_version}
%else
BuildRequires:  clang%{llvm_version}-devel
BuildRequires:  libc++.so = %{llvm_version_long}
BuildRequires:  libc++1 = %{llvm_version_long}
BuildRequires:  libc++abi.so = %{llvm_version_long}
BuildRequires:  libc++abi1 = %{llvm_version_long}
%endif
BuildRequires:  lld%{llvm_version}
BuildRequires:  llvm%{llvm_version}
#!BuildIgnore:  gcc
%else
# gcc case
BuildRequires:  binutils-gold
BuildRequires:  gcc%{gcc_version}
BuildRequires:  gcc%{gcc_version}-c++
%endif
%if 0%{?suse_version} >= 1699
#!BuildIgnore:  rpmlint rpmlint-Factory rpmlint-mini
%endif

%description
Chromium is the open-source project behind Google Chrome. We invite you to join us in our effort to help build a safer, faster, and more stable way for all Internet users to experience the web, and to create a powerful platform for developing a new generation of web applications.

%package -n %{chromedriver_name}
Summary:        WebDriver for Google Chrome/Chromium
License:        BSD-3-Clause
Requires:       %{name} = %{version}
%if %{with is_beta}
Conflicts:      chromedriver
Provides:       chromedriver = %{version}-%{release}
%endif

%description -n %{chromedriver_name}
WebDriver is an open source tool for automated testing of webapps across many browsers. It provides capabilities for navigating to web pages, user input, JavaScript execution, and more. ChromeDriver is a standalone server which implements WebDriver's wire protocol for Chromium. It is being developed by members of the Chromium and WebDriver teams.

%prep
%setup -q -n %{rname}-%{version}
# apply all patches up to 399
%autopatch -p1 -M 399

%ifarch ppc64le
%autopatch -p1 -m 400 -M 599
%endif

%if %{without libxml2_2_12}
%patch -p1 -P 1010
%endif

%if %{without libxml2_2_13}
%patch -p1 -P 1011
%endif

%if %{without gtk4_4_19}
%patch -p1 -R -P 1041
%patch -p1 -R -P 1040
%endif

%if %{without flac_1_5}
%patch -p1 -P 1050
%endif

clang_version="$(clang --version | sed -n 's/clang version //p')"
if [[ $(echo ${clang_version} | cut -d. -f1) -lt 21 ]]; then
%patch -p1 -R -P 1060
%patch -p1 -R -P 1061
fi

## ROLLUP_HACK
rm -rf third_party/devtools-frontend/src/node_modules/rollup
rm -rf third_party/devtools-frontend/src/node_modules/@rollup/rollup-linux-*
tar xf %{SOURCE4} && mv package third_party/devtools-frontend/src/node_modules/rollup
rm -rf third_party/node/node_modules/rollup
tar xf %{SOURCE4} && mv package third_party/node/node_modules/rollup
%patch -p1 -P 1080

%build
# esbuild
rm third_party/devtools-frontend/src/third_party/esbuild/esbuild
tar -xf %{SOURCE1}
tar -xf %{SOURCE2}
ln -sf esbuild-%{esbuild_version} esbuild
pushd esbuild
gflags="-mod=vendor"
%if 0%{?suse_version} >= 1600
gflags+=" -buildvcs=false"
%endif
GO_FLAGS="${gflags}" make
cp -a esbuild ../third_party/devtools-frontend/src/third_party/esbuild/esbuild
popd

# Fix the path to nodejs binary
mkdir -p third_party/node/linux/node-linux-x64/bin
rm -f third_party/node/linux/node-linux-x64/bin/node
ln -s %{_bindir}/node third_party/node/linux/node-linux-x64/bin/node
node_version=$(/usr/bin/node --version)
sed -i -e "s@^NODE_VERSION=.*@NODE_VERSION=\"${node_version}\"@" third_party/node/update_node_binaries

# python3
mkdir -p $HOME/bin
%if 0%{?suse_version} >= 1600
export PYTHON=python3
%else
export PYTHON=python3.11
%endif
ln -sfn %{_bindir}/$PYTHON $HOME/bin/python
ln -sfn %{_bindir}/$PYTHON $HOME/bin/python3
export PATH="$HOME/bin:$PATH"

# use our wrapper
rm chrome/installer/linux/common/wrapper
cp %{SOURCE106} chrome/installer/linux/common/wrapper

# from our Fedora friends
export RUSTC_BOOTSTRAP=1
rustc_version="$(rustc --version | cut -d' ' -f2)"
clang_version="$(clang --version | sed -n 's/clang version //p')"
if [[ $(echo ${clang_version} | cut -d. -f1) -ge 16 ]]; then
  clang_version="$(echo ${clang_version} | cut -d. -f1)"
fi
clang_base_path="$(clang --version | grep InstalledDir | cut -d' ' -f2 | sed 's#/bin##')"

# Remove bundled libs
keeplibs=(
    base/third_party/cityhash
    base/third_party/double_conversion
    base/third_party/icu
    base/third_party/nspr
    base/third_party/superfasthash
    base/third_party/symbolize
    base/third_party/xdg_user_dirs
    buildtools/third_party/libc++
    buildtools/third_party/libc++abi
    buildtools/third_party/libunwind
    net/third_party/mozilla_security_manager
    net/third_party/quic
    net/third_party/uri_template
    third_party/abseil-cpp
    third_party/abseil-cpp/absl
    third_party/abseil-cpp/absl/algorithm
    third_party/abseil-cpp/absl/base
    third_party/abseil-cpp/absl/flags
    third_party/abseil-cpp/absl/functional
    third_party/abseil-cpp/absl/strings
    third_party/abseil-cpp/absl/types
    third_party/angle
    third_party/angle/src/common/third_party/xxhash
    third_party/angle/src/third_party/ceval
    third_party/angle/src/third_party/libXNVCtrl
    third_party/angle/src/third_party/volk
    third_party/anonymous_tokens
    third_party/apple_apsl
    third_party/axe-core
    third_party/bidimapper
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
    third_party/compiler-rt
    third_party/content_analysis_sdk
    third_party/cpuinfo
    third_party/crashpad
    third_party/crashpad/crashpad/third_party/lss
    third_party/crashpad/crashpad/third_party/zlib
    third_party/crabbyavif
    third_party/crc32c
    third_party/cros_system_api
    third_party/d3
    third_party/dav1d
    third_party/dawn
    third_party/dawn/third_party
    third_party/depot_tools
    third_party/devscripts
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
    third_party/devtools-frontend/src/front_end/third_party/marked
    third_party/devtools-frontend/src/front_end/third_party/puppeteer
    third_party/devtools-frontend/src/front_end/third_party/puppeteer/package/lib/esm/third_party/mitt
    third_party/devtools-frontend/src/front_end/third_party/puppeteer/package/lib/esm/third_party/parsel-js
    third_party/devtools-frontend/src/front_end/third_party/puppeteer/package/lib/esm/third_party/rxjs
    third_party/devtools-frontend/src/front_end/third_party/wasmparser
    third_party/devtools-frontend/src/node_modules/fast-glob
    third_party/devtools-frontend/src/third_party
    third_party/dom_distiller_js
    third_party/dragonbox
    third_party/eigen3
    third_party/emoji-segmenter
    third_party/farmhash
    third_party/fast_float
    third_party/fdlibm
    third_party/federated_compute
    third_party/fft2d
    third_party/flatbuffers
    third_party/fp16
    third_party/fusejs/dist
    third_party/fxdiv
    third_party/gemmlowp
    third_party/google_input_tools
    third_party/google_input_tools/third_party/closure_library
    third_party/google_input_tools/third_party/closure_library/third_party/closure
    third_party/googletest
    third_party/highway
    third_party/hunspell
    third_party/ink
    third_party/inspector_protocol
    third_party/ipcz
    third_party/jinja2
    third_party/jsoncpp
    third_party/khronos
    third_party/lens_server_proto
    third_party/leveldatabase
    third_party/libaddressinput
    third_party/libaom
    third_party/libaom/source/libaom/third_party/fastfeat
    third_party/libaom/source/libaom/third_party/SVT-AV1
    third_party/libaom/source/libaom/third_party/vector
    third_party/libaom/source/libaom/third_party/x86inc
    third_party/libc++
    third_party/libgav1
    third_party/libjingle
    third_party/libphonenumber
    third_party/libsecret
    third_party/libsrtp
    third_party/libsync
    third_party/libtess2
    third_party/liburlpattern
    third_party/libva_protected_content
    third_party/libwebm
    third_party/libx11/src
    third_party/libxcb-keysyms/keysyms
    third_party/libxml/chromium
    third_party/libzip
    third_party/lit
    third_party/lottie
    third_party/lss
    third_party/lzma_sdk
    third_party/mako
    third_party/markupsafe
    third_party/material_color_utilities
    third_party/metrics_proto
    third_party/minigbm
    third_party/ml_dtypes
    third_party/modp_b64
    third_party/nasm
    third_party/nearby
    third_party/node
    third_party/oak
    third_party/omnibox_proto
    third_party/one_euro_filter
    third_party/openscreen
    third_party/openscreen/src/third_party/tinycbor/src/src
    third_party/ots
    third_party/pdfium
    third_party/pdfium/third_party/agg23
    third_party/pdfium/third_party/bigint
    third_party/pdfium/third_party/freetype
    third_party/pdfium/third_party/lcms
    third_party/pdfium/third_party/libopenjpeg
    third_party/pdfium/third_party/libtiff
    third_party/perfetto
    third_party/perfetto/protos/third_party/chromium
    third_party/perfetto/protos/third_party/pprof
    third_party/perfetto/protos/third_party/simpleperf
    third_party/pffft
    third_party/ply
    third_party/polymer
    third_party/private-join-and-compute
    third_party/private_membership
    third_party/protobuf
    third_party/protobuf/third_party/utf8_range
    third_party/pthreadpool
    third_party/puffin
    third_party/pyjson5
    third_party/pyyaml
    third_party/rapidhash
    third_party/readability
    third_party/rnnoise
    third_party/rust
    third_party/ruy
    third_party/s2cellid
    third_party/search_engines_data
    third_party/securemessage
    third_party/selenium-atoms
    third_party/sentencepiece
    third_party/sentencepiece/src/third_party/darts_clone
    third_party/shell-encryption
    third_party/simdutf
    third_party/simplejson
    third_party/skia
    third_party/skia/include/third_party/vulkan/
    third_party/skia/third_party/vulkan
    third_party/smhasher
    third_party/spirv-headers
    third_party/spirv-tools
    third_party/sqlite
    third_party/swiftshader
    third_party/swiftshader/third_party/astc-encoder
    third_party/swiftshader/third_party/llvm-10.0
    third_party/swiftshader/third_party/llvm-subzero
    third_party/swiftshader/third_party/marl
    third_party/swiftshader/third_party/SPIRV-Headers
    third_party/swiftshader/third_party/SPIRV-Tools
    third_party/swiftshader/third_party/subzero
    third_party/tensorflow_models
    third_party/tensorflow-text
    third_party/tflite
    third_party/tflite/src/third_party/fft2d
    third_party/tflite/src/third_party/xla/third_party/tsl
    third_party/tflite/src/third_party/xla/xla/tsl
    third_party/ukey2
    third_party/utf
    third_party/vulkan
    third_party/wayland
    third_party/webdriver
    third_party/webgpu-cts
    third_party/webrtc
    third_party/webrtc/common_audio/third_party/ooura
    third_party/webrtc/common_audio/third_party/spl_sqrt_floor
    third_party/webrtc/modules/third_party/fft
    third_party/webrtc/modules/third_party/g711
    third_party/webrtc/modules/third_party/g722
    third_party/webrtc/rtc_tools
    third_party/widevine
    third_party/woff2
    third_party/wuffs
    third_party/x11proto
    third_party/xcbproto
    third_party/xnnpack
    third_party/zlib/google
    third_party/zxcvbn-cpp
    url/third_party/mozilla
    v8/third_party/glibc
    v8/third_party/inspector_protocol
    v8/third_party/rapidhash-v8
    v8/third_party/siphash
    v8/third_party/utf8-decoder
    v8/third_party/valgrind
    v8/third_party/v8/builtins
    v8/third_party/v8/codegen
)
%if !%{with system_harfbuzz}
keeplibs+=(
    third_party/harfbuzz-ng
)
%endif
%if !%{with system_freetype}
keeplibs+=(
    third_party/freetype
)
%endif
%if !%{with system_icu}
keeplibs+=( third_party/icu )
%endif
%if !%{with system_ffmpeg}
keeplibs+=( third_party/ffmpeg )
%endif
%if !%{with system_zlib}
keeplibs+=( third_party/zlib )
%endif
%if !%{with system_vpx}
keeplibs+=(
    third_party/libvpx
    third_party/libvpx/source/libvpx/third_party/x86inc
)
%endif
%if !%{with system_avif}
keeplibs+=( third_party/libyuv )
%endif
%if !%{with system_webp} || !%{with system_avif}
keeplibs+=( third_party/libwebp )
%endif
# needed due to bugs in GN
keeplibs+=(
    third_party/speech-dispatcher
    third_party/usb_ids
    third_party/xdg-utils
)
# really if not with system_re2 but googletest needs it
keeplibs+=( third_party/re2 )
#endif
%if !%{with system_zstd}
keeplibs+=( third_party/zstd )
%endif
# needed ...
keeplibs+=( third_party/lit )
keeplibs+=( third_party/rust/chromium_crates_io )
keeplibs+=( third_party/rust/cxx )

%if %{without libstdcpp}
keeplibs+=( third_party/snappy )
%endif
build/linux/unbundle/remove_bundled_libraries.py "${keeplibs[@]}" --do-remove

# GN sets lto on its own and we need just ldflag options, not cflags
%define _lto_cflags %{nil}
%if %{with clang}
export CC=clang
export CXX=clang++
export AR=llvm-ar
export NM=llvm-nm
export RANLIB=llvm-ranlib
%else
%if 0%{?suse_version} <= 1500
export CC=gcc-%{gcc_version}
export CXX=g++-%{gcc_version}
# some still call gcc/g++
ln -sfn %{_bindir}/$CC $HOME/bin/gcc
ln -sfn %{_bindir}/$CXX $HOME/bin/g++
export PATH="$HOME/bin/:$PATH"
%else
export CC=gcc
export CXX=g++
%endif
export AR=ar
export NM=nm
export RANLIB=ranlib
%endif
# REDUCE DEBUG as it gets TOO large
ARCH_FLAGS="`echo %{optflags} | sed -e 's/^-g / /g' -e 's/ -g / /g' -e 's/ -g$//g'`"
export CXXFLAGS="${ARCH_FLAGS} -Wno-return-type"
# extra flags to reduce warnings that aren't very useful
export CXXFLAGS="${CXXFLAGS} -Wno-pedantic -Wno-unused-result -Wno-unused-function -Wno-unused-variable -Wno-deprecated-declarations"
# ignore warnings for minor mistakes that are too common
export CXXFLAGS="${CXXFLAGS} -Wno-return-type -Wno-parentheses -Wno-misleading-indentation"
# ignore warnings that are not supported well until gcc 8
export CXXFLAGS="${CXXFLAGS} -Wno-attributes"
# ignore warnings due to gcc bug (https://gcc.gnu.org/bugzilla/show_bug.cgi?id=84055)
export CXXFLAGS="${CXXFLAGS} -Wno-ignored-attributes"
# ingore new gcc 8 warnings that aren't yet handled upstream
export CXXFLAGS="${CXXFLAGS} -Wno-address -Wno-dangling-else -D_GNU_SOURCE"
# for wayland
export CXXFLAGS="${CXXFLAGS} -I/usr/include/wayland -I/usr/include/libxkbcommon -I/usr/include/opus"
%if %{with clang}
export LDFLAGS="${LDFLAGS} -Wl,--build-id=sha1"
export CXXFLAGS="${CXXFLAGS} -Wno-unused-command-line-argument -Wno-unknown-warning-option"
%endif
%if %{without libstdcpp}
export LDFLAGS="${LDFLAGS} -stdlib=libc++"
export CXXFLAGS="${CXXFLAGS} -stdlib=libc++ -I/usr/include/c++/v1"
%endif

%ifarch aarch64
%if %{without clang}
export CXXFLAGS="${CXXFLAGS} -flax-vector-conversions -fno-omit-frame-pointer"
%else
%if 0%{?sle_version} == 150200
export CXXFLAGS="${CXXFLAGS} -flax-vector-conversions"
%else
export CXXFLAGS="${CXXFLAGS} -flax-vector-conversions=all"
%endif
%endif
%endif
export CXXFLAGS="${CXXFLAGS} -Wno-unused-but-set-variable -Wno-missing-braces -Wno-unused-private-field -Wno-absolute-value"
%if %{without clang}
export CXXFLAGS="${CXXFLAGS} -Wno-packed-not-aligned"
%endif
export CFLAGS="${CXXFLAGS}"
%if %{without clang}
export CXXFLAGS="${CXXFLAGS} -Wno-subobject-linkage -Wno-class-memaccess"
%endif
export CXXFLAGS="${CXXFLAGS} -Wno-invalid-offsetof -U_GLIBCXX_ASSERTIONS -fpermissive"
export RUSTFLAGS

# do not eat all memory
%limit_build -m 2600
%if %{with lto} && %{without clang}
# reduce the threads for linking even more due to LTO eating ton of memory
_link_threads=$((($(echo %{?_smp_mflags} | cut -c 3-) - 2)))
test "$_link_threads" -le 0 && _link_threads=1
export LDFLAGS="-flto=$_link_threads --param lto-max-streaming-parallelism=1"
%endif

# need for error: the option `Z` is only accepted on the nightly compiler
export RUSTC_BOOTSTRAP=1

# Set system libraries to be used
gn_system_libraries=(
    flac
    fontconfig
    libdrm
    libjpeg
    libpng
    libusb
    libxml
    libxslt
    opus
)
%if %{with libstdcpp}
gn_system_libraries+=(
    snappy
)
%endif
%if %{with system_harfbuzz}
gn_system_libraries+=(
    harfbuzz-ng
)
%endif
%if %{with system_freetype}
gn_system_libraries+=(
    freetype
)
%endif
%if %{with system_icu}
gn_system_libraries+=( icu )
%endif
%if %{with system_vpx}
gn_system_libraries+=( libvpx )
%endif
%if %{with system_ffmpeg}
gn_system_libraries+=( ffmpeg )
%endif
%if %{with system_avif}
gn_system_libraries+=( libyuv )
gn_system_libraries+=( libavif )
%endif
%if %{with system_re2}
gn_system_libraries+=( re2 )
%endif
%if %{with system_webp}
gn_system_libraries+=( libwebp )
%endif
%if %{with system_zstd}
gn_system_libraries+=( zstd )
%endif
%if %{with system_zlib}
gn_system_libraries+=( zlib )
%endif
%if %{with noopenh264}
gn_system_libraries+=( openh264 )
%endif

build/linux/unbundle/replace_gn_files.py --system-libraries ${gn_system_libraries[@]}

# Create the configuration for GN
# Available options: out/Release/gn args --list out/Release/
myconf_gn=""
myconf_gn+=" custom_toolchain=\"//build/toolchain/linux/unbundle:default\""
myconf_gn+=" host_toolchain=\"//build/toolchain/linux/unbundle:default\""
myconf_gn+=" use_custom_libcxx=false"
%ifarch x86_64
myconf_gn+=" host_cpu=\"x64\""
%endif
%ifarch riscv64
myconf_gn+=" host_cpu=\"riscv64\""
%endif
%ifarch aarch64
myconf_gn+=" host_cpu=\"arm64\""
%if %{with arm_bti}
myconf_gn+=" arm_control_flow_integrity=\"standard\""
%else
myconf_gn+=" arm_control_flow_integrity=\"none\""
%endif
%endif
%ifarch ppc64le
myconf_gn+=" host_cpu=\"ppc64\""
%endif
myconf_gn+=" host_os=\"linux\""
%if %{official_build}
myconf_gn+=" is_official_build=true"
sed -i 's|OFFICIAL_BUILD|GOOGLE_CHROME_BUILD|g' tools/generate_shim_headers/generate_shim_headers.py
%endif
myconf_gn+=" is_debug=false"
myconf_gn+=" dcheck_always_on=false"
%if %{with swiftshader}
myconf_gn+=" use_swiftshader_with_subzero=true"
%endif
myconf_gn+=" is_component_ffmpeg=true"
myconf_gn+=" use_cups=true"
myconf_gn+=" use_aura=true"
myconf_gn+=" symbol_level=1"
myconf_gn+=" blink_symbol_level=0"
myconf_gn+=" use_kerberos=true"
myconf_gn+=" enable_vr=false"
myconf_gn+=" optimize_webui=false"
myconf_gn+=" use_pulseaudio=true link_pulseaudio=true"
myconf_gn+=" is_component_build=false"
myconf_gn+=" use_sysroot=false"
myconf_gn+=" fatal_linker_warnings=false"
myconf_gn+=" use_allocator_shim=true"
myconf_gn+=" use_partition_alloc=true"
myconf_gn+=" disable_fieldtrial_testing_config=true"
myconf_gn+=" use_unofficial_version_number=false"
myconf_gn+=" use_vaapi=true"
myconf_gn+=" treat_warnings_as_errors=false"
myconf_gn+=" enable_widevine=true"
myconf_gn+=" use_dbus=true"
%if %{with noopenh264}
myconf_gn+=" media_use_openh264=true"
myconf_gn+=" rtc_use_h264=true"
%else
myconf_gn+=" media_use_openh264=false"
myconf_gn+=" rtc_use_h264=false"
%endif
myconf_gn+=" use_v8_context_snapshot=true"
myconf_gn+=" v8_use_external_startup_data=true"
myconf_gn+=" rust_sysroot_absolute=\"%{_prefix}\""
myconf_gn+=" rust_bindgen_root=\"%{_prefix}\""
myconf_gn+=" rustc_version=\"$rustc_version\""
myconf_gn+=" clang_base_path=\"$clang_base_path\""
myconf_gn+=" clang_version=\"$clang_version\""
myconf_gn+=" safe_browsing_use_unrar=false"
%if %{with gtk4}
myconf_gn+=" gtk_version=4"
%endif
myconf_gn+=" use_qt5=false"
%if %{with qt6}
myconf_gn+=" use_qt6=true"
myconf_gn+=" moc_qt6_path=\"%{?_qt6_libexecdir}\""
%endif
# See dependency logic in third_party/BUILD.gn
%if %{with system_harfbuzz}
myconf_gn+=" use_system_harfbuzz=true"
%endif
%if %{with system_freetype}
myconf_gn+=" use_system_freetype=true"
%endif
myconf_gn+=" use_system_libffi=true"
myconf_gn+=" enable_hangout_services_extension=true"
myconf_gn+=" enable_vulkan=true"
%if %{with pipewire}
myconf_gn+=" rtc_use_pipewire=true rtc_link_pipewire=true"
%endif
%if %{with clang}
myconf_gn+=" is_clang=true clang_use_chrome_plugins=false"
%if %{with lto} && %{with clang}
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 150300
myconf_gn+=" use_thin_lto=true"
%endif
%endif
myconf_gn+=" use_lld=true"
%else
myconf_gn+=" is_clang=false"
myconf_gn+=" use_gold=true"
%endif
%if %{with lto} && %{without clang}
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

# Set up Google API keys, see http://www.chromium.org/developers/how-tos/api-keys
# Note: these are for the openSUSE Chromium builds ONLY. For your own distribution,
# please get your own set of keys.
google_api_key="AIzaSyD1hTe85_a14kr1Ks8T3Ce75rvbR1_Dx7Q"
myconf_gn+=" google_api_key=\"${google_api_key}\""

if [ "$clang_version" -lt 20 ] ; then
myconf_gn+=" clang_warning_suppression_file=\"\""
fi
if [ "$clang_version" -lt 21 ] ; then
myconf_gn+=" toolchain_supports_rust_thin_lto=false"
fi
myconf_gn+=" chrome_pgo_phase=0"

# GN does not support passing cflags:
#  https://bugs.chromium.org/p/chromium/issues/detail?id=642016
gn gen --args="${myconf_gn}" %{outputdir}

ninja -v %{?_smp_mflags} -C %{outputdir} \
	chrome \
	chromedriver \
	%{nil}

%install
bash %{SOURCE105} -s %{buildroot} -l %{_libdir} %{!?with_system_icu:-i true} -o %{outputdir}
# chromedriver
cp -a %{outputdir}/chromedriver.unstripped %{buildroot}%{_libdir}/chromium/chromedriver
ln -s %{_libdir}/chromium/chromedriver %{buildroot}%{_bindir}/chromedriver
# link to browser plugin path.  Plugin patch doesn't work. Why?
mkdir -p %{buildroot}%{_libdir}/browser-plugins
ln -s %{_libdir}/browser-plugins %{buildroot}%{_libdir}/chromium/plugins
# Install the master_preferences file
mkdir -p %{buildroot}%{_sysconfdir}/chromium
install -m 0644 %{SOURCE30} %{buildroot}%{_sysconfdir}/chromium
# Compat link
ln -s %{_bindir}/chromium-browser %{buildroot}%{_bindir}/chromium
# Policy dirs
mkdir -p %{buildroot}%{_sysconfdir}/chromium/policies
mkdir %{buildroot}%{_sysconfdir}/chromium/policies/managed
mkdir %{buildroot}%{_sysconfdir}/chromium/policies/recommended
chmod -w %{buildroot}%{_sysconfdir}/chromium/policies/managed
mkdir -p %{buildroot}%{_datadir}/chromium/extensions
mkdir -p %{buildroot}%{_sysconfdir}/chromium/native-messaging-hosts
# SVG
install -Dm 0644 %{SOURCE104} %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/chromium-browser.svg
# link for the manpage
ln -sf chromium-browser.1%{?ext_man} %{buildroot}%{_mandir}/man1/chromium.1%{?ext_man}

%fdupes -s %{buildroot}

%files
%license LICENSE
%doc AUTHORS
%{_datadir}/chromium
%dir %{_sysconfdir}/chromium
%dir %{_sysconfdir}/chromium/policies
%dir %{_sysconfdir}/chromium/policies/managed
%dir %{_sysconfdir}/chromium/policies/recommended
%dir %{_sysconfdir}/chromium/native-messaging-hosts
%config %{_sysconfdir}/chromium/master_preferences
%{_libdir}/chromium
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/chromium-browser.appdata.xml
%{_datadir}/icons/hicolor
%exclude %{_libdir}/chromium/chromedriver
%{_bindir}/chromium-browser
%{_bindir}/chromium
%{_mandir}/man1/chromium.1%{?ext_man}
%{_mandir}/man1/chromium-browser.1%{?ext_man}

%files -n %{chromedriver_name}
%license LICENSE
%{_libdir}/chromium/chromedriver
%{_bindir}/chromedriver

%changelog
