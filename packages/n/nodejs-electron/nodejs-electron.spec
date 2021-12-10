#
# spec file for package nodejs-electron
#
# Copyright (c) 2021 SUSE LLC
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


%define mod_name electron
ExcludeArch:    %{ix86}
%ifarch x86_64
%if 0%{?suse_version} > 1500 || 0%{?fedora_version}
%bcond_without lto
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
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200 || 0%{?fedora_version}
%bcond_without pipewire
%else
%bcond_with pipewire
%endif
%ifarch %{arm} aarch64
%bcond_with swiftshader
%else
%bcond_without swiftshader
%endif
%if 0%{?suse_version} >= 1550 || 0%{?fedora_version} > 34
%bcond_without systemicu
%else
%bcond_with systemicu
%endif
# vaapi still requires bundled libvpx
%bcond_with system_vpx
%ifarch aarch64
%bcond_without clang
%else
%bcond_with clang
%endif
Name:           nodejs-electron
Version:        13.6.2
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
Patch0:         chromium-91-compiler.patch
%if 0%{?sle_version} < 150300 || 0%{?fedora_version} < 34
# Fixed with ld.gold >= 2.36
# https://sourceware.org/bugzilla/show_bug.cgi?id=26200
Patch1:         chromium-disable-parallel-gold.patch
%endif
Patch2:         chromium-glibc-2.33.patch
Patch3:         chromium-lp152-missing-includes.patch
Patch4:         chromium-norar.patch
Patch5:         chromium-system-libusb.patch
Patch6:         gcc-enable-lto.patch
Patch7:         chromium-91-java-only-allowed-in-android-builds.patch
Patch8:         chromium-91-system-icu.patch
Patch9:         chromium-glibc-2.34.patch
Patch10:        chromium-88-gcc-fix-swiftshader-libEGL-visibility.patch
Patch11:        chromium-vaapi.patch
Patch12:        chromium-86-fix-vaapi-on-intel.patch
Patch13:        chromium-91-GCC_fix_vector_types_in_pcscan.patch
Patch14:        chromium-gcc11.patch
Patch15:        chromium-freetype-2.11.patch
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
# Mark [nodiscard] as unsupported
Patch23:        electron-13-gcc-fix-v8-nodiscard.patch
# Fix blink nodestructor
Patch24:        electron-13-blink-gcc-ambiguous-nodestructor.patch
Patch26:        a9831f1cbf93fb18dd951453635f488037454ce9.patch
# Fix missing harfbuzz symbols
Patch27:        skia_harfbuzz_roll.patch
Patch28:        skia_harfbuzz_api.patch
Patch29:        harfbuzz_roll.patch
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
%if 0%{?suse_version}
BuildRequires:  libgsm-devel
%else
BuildRequires:  gsm-devel
%endif
BuildRequires:  libpng-devel
BuildRequires:  memory-constraints
BuildRequires:  nasm
BuildRequires:  ncurses-devel
%if 0%{?suse_version}
# Required for /usr/bin/clang-format
BuildRequires:  clang >= 8.0.0
BuildRequires:  ninja >= 1.7.2
%endif
%if 0%{?fedora_version}
# Required for /usr/bin/clang-format
BuildRequires:  clang-tools-extra
BuildRequires:  libatomic
BuildRequires:  ninja-build >= 1.7.2
%endif
BuildRequires:  nodejs >= 8.0
BuildRequires:  npm
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
%if 0%{?fedora_version}
BuildRequires:  python2-devel
%endif
%if 0%{?suse_version}
BuildRequires:  python2
BuildRequires:  python2-xml
%endif
BuildRequires:  rsync
BuildRequires:  snappy-devel
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  util-linux
BuildRequires:  wdiff
BuildRequires:  perl(Switch)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo) >= 1.6
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(harfbuzz) > 2.3.0
BuildRequires:  pkgconfig(hunspell)
%if %{with systemicu}
BuildRequires:  pkgconfig(icu-i18n) >= 68.0
%else
Provides:       bundled(icu) = 68.0
%endif
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(kadm-client)
BuildRequires:  pkgconfig(kdb)
BuildRequires:  pkgconfig(krb5)
%if 0%{?suse_version}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat) >= 58
BuildRequires:  pkgconfig(libavutil)
%endif
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdc1394-2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libtcmalloc)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libwebp) >= 0.4.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.5
BuildRequires:  pkgconfig(libxslt)
%if 0%{?fedora_version}
BuildRequires:  minizip-compat-devel
%else
BuildRequires:  pkgconfig(minizip)
%endif
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
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
Requires:       hicolor-icon-theme
Recommends:     noto-coloremoji-fonts
Provides:       electron
Obsoletes:      nodejs-electron-prebuilt < %{version}
Provides:       nodejs-electron-prebuilt = %{version}
%if 0%{?suse_version}
BuildRequires:  libjpeg-devel >= 8.1
%else
BuildRequires:  libjpeg-turbo-devel
%endif
%if %{with system_vpx}
BuildRequires:  pkgconfig(vpx) >= 1.8.2
%endif
%if %{without clang}
%if 0%{?suse_version} >= 1550 || 0%{?fedora_version}
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

Recommends:     noto-coloremoji-fonts

Provides:       electron

Obsoletes:      nodejs-electron-prebuilt < %{version}
Provides:       nodejs-electron-prebuilt = %{version}

%description
Nodejs application: Build cross platform desktop apps with JavaScript, HTML, and CSS

%if 0%{?fedora}
%global debug_package %{nil}
%endif

%prep
%autosetup -n %{mod_name}-%{version} -p1

# Required for third_party/blink/renderer/bindings/scripts/generate_bindings.py
ln -sf %{_bindir}/clang-format buildtools/linux64/clang-format

# Fix the path to nodejs binary
mkdir -p third_party/node/linux/node-linux-x64/bin
ln -sf %{_bindir}/node third_party/node/linux/node-linux-x64/bin/node

# Fix shim header generation
sed -i 's/OFFICIAL_BUILD/GOOGLE_CHROME_BUILD/' \
      tools/generate_shim_headers/generate_shim_headers.py

%if %{with systemicu}
find third_party/icu -type f ! -name "*.gn" -a ! -name "*.gni" -delete
%endif

%build
# GN sets lto on its own and we need just ldflag options, not cflags
%define _lto_cflags %{nil}

# Make sure python is python2
install -d -m 0755 python2-path
ln -sf %{_bindir}/python2 "$(pwd)/python2-path/python"
export PATH="$(pwd)/python2-path:${PATH}"

# for wayland
export CXXFLAGS="${CXXFLAGS} -I/usr/include/wayland -I/usr/include/libxkbcommon"

%if %{with clang}
export CFLAGS="${CXXFLAGS}"

export CC=clang
export CXX=clang++

# else with clang
%else

# REDUCE DEBUG as it gets TOO large
ARCH_FLAGS="`echo %{optflags} | sed -e 's/^-g / /g' -e 's/ -g / /g' -e 's/ -g$//g'`"
%if 0%{?fedora_version}
# Fix base/allocator/allocator_shim.cc:408:2: error: #error This code cannot be
# used when exceptions are turned on.
ARCH_FLAGS="`echo $ARCH_FLAGS | sed -e 's/ -fexceptions / /g'`"
%endif

export CXXFLAGS="${CXXFLAGS} ${ARCH_FLAGS} -Wno-return-type"
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

%if 0%{?suse_version} >= 1550 || 0%{?fedora_version}
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
    flac
    fontconfig
    freetype
    harfbuzz-ng
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

%if %{with systemicu}
gn_system_libraries+=( icu )
%endif

%if 0%{?suse_version}
gn_system_libraries+=( ffmpeg )
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
myconf_gn+=" chrome_pgo_phase=0"
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
# Current tcmalloc does not support AArch64
myconf_gn+=" use_allocator=\"tcmalloc\""
myconf_gn+=" fieldtrial_testing_like_official_build=true"
myconf_gn+=" use_gold=true"
myconf_gn+=" use_gnome_keyring=false"
myconf_gn+=" use_unofficial_version_number=false"
myconf_gn+=" use_lld=false"
myconf_gn+=" use_vaapi=true"
myconf_gn+=" treat_warnings_as_errors=false"
myconf_gn+=" enable_widevine=true"
myconf_gn+=" use_dbus=true"
myconf_gn+=" enable_vulkan=true"
myconf_gn+=" icu_use_data_file=false"
myconf_gn+=" media_use_openh264=false"
myconf_gn+=" rtc_use_h264=false"

%if %{with clang}
myconf_gn+=" is_clang=true clang_base_path=\"/usr\" clang_use_chrome_plugins=false"
%else
myconf_gn+=" is_clang=false"
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
myconf_gn+=" rtc_pipewire_version=\"0.3\""
%endif

# The proprietary codecs just force the chromium to say they can use it and
# offload the actual computation to the ffmpeg, otherwise the chromium
# won't be able to load the codec even if the library can handle it
myconf_gn+=" proprietary_codecs=true"
myconf_gn+=" ffmpeg_branding=\"Chrome\""

# GN does not support passing cflags:
#  https://bugs.chromium.org/p/chromium/issues/detail?id=642016
gn gen out/Release --args="import(\"//electron/build/args/release.gn\") ${myconf_gn}"
ninja -v %{?_smp_mflags} -C out/Release electron

# strip the debugging and symbol information
electron/script/strip-binaries.py -d out/Release

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -d -m 0755 %{buildroot}%{_libdir}/electron
install -d -m 0755 %{buildroot}%{_libdir}/electron/swiftshader
install -d -m 0755 %{buildroot}%{_datadir}/applications
install -d -m 0755 %{buildroot}%{_datadir}/pixmaps/
install -d -m 0755 %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/

install -m 0755 %{SOURCE10} %{buildroot}%{_bindir}/%{mod_name}
install -m 0644 electron/default_app/icon.png %{buildroot}%{_datadir}/pixmaps/%{mod_name}.png
install -m 0644 %{SOURCE12} %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/electron-symbolic.svg

desktop-file-install --dir %{buildroot}%{_datadir}/applications/ %{SOURCE11}

pushd out/Release
rsync -av *.bin *.pak *.so resources %{buildroot}%{_libdir}/electron/

%if 0%{?fedora_version}
rm -f %{buildroot}%{_libdir}/electron/libffmpeg*
%endif

rsync -av --exclude '*.pak.info' locales %{buildroot}%{_libdir}/electron/

%if %{with swiftshader}
rsync -av --exclude '*.so.TOC' swiftshader %{buildroot}%{_libdir}/electron/
install -m 0644 vk_swiftshader_icd.json %{buildroot}%{_libdir}/electron/vk_swiftshader_icd.json
%else
rm -f  %{buildroot}/%{_libdir}/electron/libvk_swiftshader.so
%endif

install -m 0755 electron %{buildroot}%{_libdir}/electron/electron
popd

%if %{without systemicu}
rsync -av third_party/icu/common/icudtl.dat %{buildroot}%{_libdir}/electron/
%endif

echo -n "%{version}" > %{buildroot}%{_libdir}/electron/version

# Install folders required for webapps
mkdir -p "%{buildroot}%{_sysconfdir}/webapps"
mkdir -p "%{buildroot}%{_datadir}/webapps"

%files
%license electron/LICENSE
%doc electron/README.md
%{_bindir}/electron
%{_datadir}/pixmaps/electron.png
%{_datadir}/icons/hicolor/symbolic/apps/electron-symbolic.svg
%{_datadir}/applications/electron.desktop

%dir %{_libdir}/electron/

%{_libdir}/electron/electron

%{_libdir}/electron/*.bin
%{_libdir}/electron/*.pak

%{_libdir}/electron/libEGL.so
%{_libdir}/electron/libGLESv2.so
%{_libdir}/electron/libVkICD_mock_icd.so

%if %{without systemicu}
%{_libdir}/electron/icudtl.dat
%endif

%{_libdir}/electron/locales/
%{_libdir}/electron/resources/

%if %{with swiftshader}
%{_libdir}/electron/libvk_swiftshader.so
%{_libdir}/electron/vk_swiftshader_icd.json

%dir %{_libdir}/electron/swiftshader/
%{_libdir}/electron/swiftshader/libEGL.so
%{_libdir}/electron/swiftshader/libGLESv2.so
%endif

%{_libdir}/electron/version
%dir %{_sysconfdir}/webapps
%dir %{_datadir}/webapps

%changelog
