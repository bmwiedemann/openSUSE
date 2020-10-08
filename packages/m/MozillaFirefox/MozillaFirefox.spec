#
# spec file for package MozillaFirefox
#
# Copyright (c) 2020 SUSE LLC
#               2006-2020 Wolfgang Rosenauer <wr@rosenauer.org>
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


%if 0%{?suse_version} < 1550 && 0%{?sle_version} <= 150100
#!BuildIgnore: post-build-checks
%endif

# changed with every update
# orig_version vs. mainver: To have beta-builds
# FF70beta3 would be released as FF69.99
# orig_version would be the upstream tar ball
# orig_version 70.0
# orig_suffix b3
# major 69
# mainver %major.99
%define major          81
%define mainver        %major.0.1
%define orig_version   81.0.1
%define orig_suffix    %{nil}
%define update_channel release
%define branding       1
%define devpkg         1

# PGO builds do not work in TW currently (bmo#1642410)
%define do_profiling   0

# upstream default is clang (to use gcc for large parts set to 0)
%define clang_build 0

# PIE, full relro
%define build_hardened 1

%bcond_with only_print_mozconfig

# Firefox only supports i686
%ifarch %ix86
ExclusiveArch:  i586 i686
BuildArch:      i686
%{expand:%%global optflags %(echo "%optflags"|sed -e s/i586/i686/) -march=i686 -mtune=generic}
%endif

# general build definitions
%define progname firefox
%define pkgname  MozillaFirefox
%define srcname  firefox
%define appname  Firefox
%define progdir %{_prefix}/%_lib/%{progname}
%define gnome_dir     %{_prefix}
%define desktop_file_name %{progname}
%define firefox_appid \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%define __provides_exclude ^lib.*\\.so.*$
%define __requires_exclude ^(libmoz.*|liblgpllibs.*|libxul.*)$
%define localize 1
%ifarch %ix86 x86_64
%define crashreporter 1
%else
%define crashreporter 0
%endif
%if 0%{?suse_version} < 1550 && 0%{?sle_version} <= 150100
# pipewire is too old on Leap <15.1
%define with_pipewire0_3 0
%else
%define with_pipewire0_3 1
%endif

Name:           %{pkgname}
BuildRequires:  Mesa-devel
BuildRequires:  alsa-devel
BuildRequires:  autoconf213
BuildRequires:  dbus-1-glib-devel
BuildRequires:  dejavu-fonts
BuildRequires:  fdupes
BuildRequires:  memory-constraints
%if 0%{?suse_version} <= 1320
BuildRequires:  gcc9-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  cargo >= 1.43
BuildRequires:  ccache
BuildRequires:  libXcomposite-devel
BuildRequires:  libcurl-devel
BuildRequires:  libidl-devel
BuildRequires:  libiw-devel
BuildRequires:  libproxy-devel
BuildRequires:  makeinfo
BuildRequires:  mozilla-nspr-devel >= 4.28
BuildRequires:  mozilla-nss-devel >= 3.56
BuildRequires:  nasm >= 2.14
BuildRequires:  nodejs10 >= 10.21.0
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} < 150000
BuildRequires:  python-libxml2
BuildRequires:  python36
%else
BuildRequires:  python3 >= 3.5
BuildRequires:  python3-curses
BuildRequires:  python3-devel
%endif
BuildRequires:  rust >= 1.43
BuildRequires:  rust-cbindgen >= 0.14.3
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-libXt-devel
%if 0%{?do_profiling}
BuildRequires:  xvfb-run
%endif
BuildRequires:  yasm
BuildRequires:  zip
%if 0%{?suse_version} < 1550
BuildRequires:  pkgconfig(gconf-2.0) >= 1.2.1
%endif
%if (0%{?sle_version} >= 120000 && 0%{?sle_version} < 150000)
BuildRequires:  clang6-devel
%else
BuildRequires:  clang-devel >= 5
%endif
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.22
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.18.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
BuildRequires:  pkgconfig(gtk+-unix-print-2.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libpulse)
%if %{with_pipewire0_3}
BuildRequires:  pkgconfig(libpipewire-0.3)
%endif
# libavcodec is required for H.264 support but the
# openSUSE version is currently not able to play H.264
# therefore the Packman version is required
# minimum version of libavcodec is 53
Recommends:     libavcodec-full >= 0.10.16
Version:        %{mainver}
Release:        0
%if "%{name}" == "MozillaFirefox"
Provides:       firefox = %{mainver}
Provides:       firefox = %{version}-%{release}
%endif
Provides:       web_browser
Provides:       appdata()
Provides:       appdata(firefox.appdata.xml)
# this is needed to match this package with the kde4 helper package without the main package
# having a hard requirement on the kde4 package
%define kde_helper_version 6
Provides:       mozilla-kde4-version = %{kde_helper_version}
Summary:        Mozilla %{appname} Web Browser
License:        MPL-2.0
Group:          Productivity/Networking/Web/Browsers
URL:            http://www.mozilla.org/
%if !%{with only_print_mozconfig}
Source:         http://ftp.mozilla.org/pub/%{srcname}/releases/%{version}%{orig_suffix}/source/%{srcname}-%{orig_version}%{orig_suffix}.source.tar.xz
Source1:        MozillaFirefox.desktop
Source2:        MozillaFirefox-rpmlintrc
Source3:        mozilla.sh.in
Source4:        tar_stamps
Source7:        l10n-%{orig_version}%{orig_suffix}.tar.xz
Source8:        firefox-mimeinfo.xml
Source9:        firefox.js
Source11:       firefox.1
Source12:       mozilla-get-app-id
Source13:       spellcheck.js
Source14:       https://github.com/openSUSE/firefox-scripts/raw/5e54f4a/create-tar.sh
Source15:       firefox-appdata.xml
Source16:       %{name}.changes
# Set up API keys, see http://www.chromium.org/developers/how-tos/api-keys
# Note: these are for the openSUSE Firefox builds ONLY. For your own distribution,
# please get your own set of keys.
Source18:       mozilla-api-key
Source19:       google-api-key
Source20:       https://ftp.mozilla.org/pub/%{srcname}/releases/%{version}%{orig_suffix}/source/%{srcname}-%{orig_version}%{orig_suffix}.source.tar.xz.asc
Source21:       https://ftp.mozilla.org/pub/%{srcname}/releases/%{version}%{orig_suffix}/KEY#/mozilla.keyring
# Gecko/Toolkit
Patch1:         mozilla-nongnome-proxies.patch
Patch2:         mozilla-kde.patch
Patch3:         mozilla-ntlm-full-path.patch
Patch4:         mozilla-aarch64-startup-crash.patch
Patch6:         mozilla-sandbox-fips.patch
Patch7:         mozilla-fix-aarch64-libopus.patch
Patch8:         mozilla-disable-wasm-emulate-arm-unaligned-fp-access.patch
Patch9:         mozilla-s390-context.patch
Patch11:        mozilla-reduce-rust-debuginfo.patch
Patch12:        mozilla-ppc-altivec_static_inline.patch
Patch13:        mozilla-bmo1005535.patch
Patch14:        mozilla-bmo1568145.patch
Patch15:        mozilla-bmo1504834-part1.patch
Patch16:        mozilla-bmo1504834-part2.patch
Patch17:        mozilla-bmo1504834-part3.patch
Patch18:        mozilla-bmo1554971.patch
Patch19:        mozilla-bmo1512162.patch
Patch20:        mozilla-fix-top-level-asm.patch
Patch21:        mozilla-bmo1504834-part4.patch
Patch22:        mozilla-bmo849632.patch
Patch23:        mozilla-pipewire-0-3.patch
Patch24:        mozilla-bmo1602730.patch
Patch25:        mozilla-bmo998749.patch
Patch26:        mozilla-bmo1626236.patch
Patch27:        mozilla-s390x-skia-gradient.patch
Patch28:        mozilla-libavcodec58_91.patch
Patch29:        revert-795c8762b16b.patch
# Firefox/browser
Patch101:       firefox-kde.patch
Patch102:       firefox-branded-icons.patch
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(post):   coreutils shared-mime-info desktop-file-utils
Requires(postun): shared-mime-info desktop-file-utils
Requires:       %{name}-branding >= 68
%requires_ge    mozilla-nspr
%requires_ge    mozilla-nss
%requires_ge    libfreetype6
Recommends:     libcanberra0
Recommends:     libpulse0
# addon leads to startup crash (bnc#908892)
Obsoletes:      tracker-miner-firefox < 0.15
%if 0%{?devpkg} == 0
Obsoletes:      %{name}-devel < %{version}
%endif
# libproxy's mozjs pacrunner crashes FF (bnc#759123)
%if 0%{?suse_version} < 1220
Obsoletes:      libproxy1-pacrunner-mozjs <= 0.4.7
%endif
ExcludeArch:    armv6l armv6hl

%description
Mozilla Firefox is a standalone web browser, designed for standards
compliance and performance.  Its functionality can be enhanced via a
plethora of extensions.

%if 0%{?devpkg}
%package devel
Summary:        Devel package for %{appname}
Group:          Development/Tools/Other
Provides:       firefox-devel = %{version}-%{release}
Requires:       %{name} = %{version}
Requires:       perl(Archive::Zip)
Requires:       perl(XML::Simple)

%description devel
Development files for %{appname} to make packaging of addons easier.
%endif

%if %localize
%package translations-common
Summary:        Common translations for %{appname}
Group:          System/Localization
Provides:       locale(%{name}:ar;ca;cs;da;de;el;en_GB;es_AR;es_CL;es_ES;fi;fr;hu;it;ja;ko;nb_NO;nl;pl;pt_BR;pt_PT;ru;sv_SE;zh_CN;zh_TW)
# This is there for updates from Firefox before the translations-package was split up into 2 packages
Provides:       %{name}-translations
Requires:       %{name} = %{version}
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-common
This package contains several common languages for the user interface
of %{appname}.

%package translations-other
Summary:        Extra translations for %{appname}
Group:          System/Localization
Provides:       locale(%{name}:ach;af;an;ast;az;be;bg;bn;br;bs;cak;cy;dsb;en_CA;eo;es_MX;et;eu;fa;ff;fy_NL;ga_IE;gd;gl;gn;gu_IN;he;hi_IN;hr;hsb;hy_AM;ia;id;is;ka;kab;kk;km;kn;lij;lt;lv;mk;mr;ms;my;ne_NP;nn_NO;oc;pa_IN;rm;ro;si;sk;sl;son;sq;sr;ta;te;th;tr;uk;ur;uz;vi;xh)
Requires:       %{name} = %{version}
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-other
This package contains rarely used languages for the user interface
of %{appname}.
%endif

%package branding-upstream
Summary:        Upstream branding for %{appname}
Group:          Productivity/Networking/Web/Browsers
Provides:       %{name}-branding = %{version}
Conflicts:      otherproviders(%{name}-branding)
Supplements:    packageand(%{name}:branding-upstream)
#BRAND: Provide three files -
#BRAND: /usr/lib/firefox/browserconfig.properties that contains the
#BRAND: default homepage and some other default configuration options
#BRAND: /usr/lib/firefox/defaults/profile/bookmarks.html that contains
#BRAND: the list of default bookmarks
#BRAND: It's also possible to create a file
#BRAND: /usr/lib/firefox/defaults/preferences/firefox-$vendor.js to set
#BRAND: custom preference overrides.
#BRAND: It's also possible to drop files in /usr/lib/firefox/distribution/searchplugins/common/

%description branding-upstream
This package provides upstream look and feel for %{appname}.

%if %crashreporter
%package buildsymbols
Summary:        Breakpad buildsymbols for %{appname}
Group:          Development/Debug

%description buildsymbols
This subpackage contains the Breakpad created and compatible debugging
symbols meant for upload to Mozilla's crash collector database.
%endif

%if !%{with only_print_mozconfig}
%prep
%if %localize

# If generated incorrectly, the tarball will be ~270B in
# size, so 1MB seems like good enough limit to check.
MINSIZE=1048576
if (( $(stat -Lc%s "%{SOURCE7}") < MINSIZE)); then
    echo "Translations tarball %{SOURCE7} not generated properly."
    exit 1
fi

%setup -q -n %{srcname}-%{orig_version} -b 7
%else
%setup -q -n %{srcname}-%{orig_version}
%endif
cd $RPM_BUILD_DIR/%{srcname}-%{orig_version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%if %{with_pipewire0_3}
%patch23 -p1
%endif
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1 -R
# Firefox
%patch101 -p1
%patch102 -p1
%endif

%build
%if !%{with only_print_mozconfig}
# no need to add build time to binaries
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +

# SLE-12 provides python36, but that package does not provide a python3 binary
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} < 150000
sed -i "s/python3/python36/g" configure.in
sed -i "s/python3/python36/g" mach
export PYTHON3=/usr/bin/python36
%endif

#
kdehelperversion=$(cat toolkit/xre/nsKDEUtils.cpp | grep '#define KMOZILLAHELPER_VERSION' | cut -d ' ' -f 3)
if test "$kdehelperversion" != %{kde_helper_version}; then
  echo fix kde helper version in the .spec file
  exit 1
fi

source %{SOURCE4}
%endif

export CARGO_HOME=${RPM_BUILD_DIR}/%{srcname}-%{orig_version}/.cargo
export MOZ_SOURCE_CHANGESET=$RELEASE_TAG
export SOURCE_REPO=$RELEASE_REPO
export source_repo=$RELEASE_REPO
export MOZ_SOURCE_REPO=$RELEASE_REPO
export MOZ_BUILD_DATE=$RELEASE_TIMESTAMP
export MOZILLA_OFFICIAL=1
export BUILD_OFFICIAL=1
export MOZ_TELEMETRY_REPORTING=1
export MACH_USE_SYSTEM_PYTHON=1
%if 0%{?suse_version} <= 1320
export CC=gcc-9
%else
%if 0%{?clang_build} == 0
export CC=gcc
export CXX=g++
%endif
%endif
%ifarch %arm %ix86
# Limit RAM usage during link
export LDFLAGS="${LDFLAGS} -Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
%endif
%if 0%{?build_hardened}
export LDFLAGS="${LDFLAGS} -fPIC -Wl,-z,relro,-z,now"
%endif
%ifarch ppc64 ppc64le
%if 0%{?clang_build} == 0
export CFLAGS="$CFLAGS -mminimal-toc"
%endif
%endif
export CXXFLAGS="$CFLAGS"
export MOZCONFIG=$RPM_BUILD_DIR/mozconfig
%if %{with only_print_mozconfig}
echo "export CC=$CC"
echo "export CXX=$CXX"
echo "export CFLAGS=\"$CFLAGS\""
echo "export CXXFLAGS=\"$CXXFLAGS\""
echo "export LDFLAGS=\"$LDFLAGS\""
echo "export RUSTFLAGS=\"$RUSTFLAGS\""
echo "export CARGO_HOME=\"$CARGO_HOME\""
echo "export PATH=\"$PATH\""
echo "export LD_LIBRARY_PATH=\"$LD_LIBRARY_PATH\""
echo "export PKG_CONFIG_PATH=\"$PKG_CONFIG_PATH\""
echo "export MOZCONFIG=\"$MOZCONFIG\""
echo "export MOZILLA_OFFICIAL=1"
echo "export BUILD_OFFICIAL=1"
echo "export MOZ_TELEMETRY_REPORTING=1"
echo ""
cat << EOF
%else
%ifarch aarch64 %arm
%limit_build -m 2000
%endif
cat << EOF > $MOZCONFIG
%endif
mk_add_options MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZ_MAKE_FLAGS=%{?jobs:-j%jobs}
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/../obj
. \$topsrcdir/browser/config/mozconfig
ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}
ac_add_options --includedir=%{_includedir}
ac_add_options --enable-release
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} < 150000
ac_add_options --enable-default-toolkit=cairo-gtk3
%else
ac_add_options --enable-default-toolkit=cairo-gtk3-wayland
%endif
# bmo#1441155 - Disable the generation of Rust debug symbols on Linux32
%ifarch %ix86 %arm
ac_add_options --disable-debug-symbols
%else
ac_add_options --enable-debug-symbols
%endif
# building with elf-hack started to fail everywhere with FF73
#%if 0%{?suse_version} > 1549
%ifnarch aarch64 ppc64 ppc64le s390x
ac_add_options --disable-elf-hack
%endif
#%endif
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-ccache
%if %{localize}
ac_add_options --with-l10n-base=$RPM_BUILD_DIR/l10n
%endif
#ac_add_options --with-system-jpeg    # libjpeg-turbo is used internally
#ac_add_options --with-system-png     # doesn't work because of missing APNG support
ac_add_options --with-system-zlib
ac_add_options --disable-updater
ac_add_options --disable-tests
ac_add_options --enable-alsa
ac_add_options --disable-debug
#ac_add_options --enable-chrome-format=jar
ac_add_options --enable-update-channel=%{update_channel}
ac_add_options --with-mozilla-api-keyfile=%{SOURCE18}
# Google-service currently not available for free anymore
#ac_add_options --with-google-location-service-api-keyfile=%{SOURCE19}
ac_add_options --with-google-safebrowsing-api-keyfile=%{SOURCE19}
ac_add_options --with-unsigned-addon-scopes=app
ac_add_options --allow-addon-sideload
%if %branding
ac_add_options --enable-official-branding
%endif
ac_add_options --enable-libproxy
%if ! %crashreporter
ac_add_options --disable-crashreporter
%endif
%ifarch %arm
ac_add_options --with-fpu=vfpv3-d16
ac_add_options --with-float-abi=hard
%ifarch armv6l armv6hl
ac_add_options --with-arch=armv6
%else
ac_add_options --with-arch=armv7-a
%endif
%endif
# mitigation/workaround for bmo#1512162
%ifarch s390x
ac_add_options --enable-optimize="-O1"
%endif
%ifarch x86_64
# LTO needs newer toolchain stack only (at least GCC 8.2.1 (r268506)
%if 0%{?suse_version} > 1500
ac_add_options --enable-lto
%if 0%{?do_profiling}
ac_add_options MOZ_PGO=1
%endif
%endif
%endif
EOF
%if !%{with only_print_mozconfig}
%ifarch ppc64 s390x s390
# NOTE: Currently, system-icu is too old, so we can't build with that,
#       but have to generate the .dat-file freshly. This seems to be a
#       less fragile approach anyways.
# ac_add_options --with-system-icu
echo "Generate big endian version of config/external/icu/data/icud58l.dat"
./mach python intl/icu_sources_data.py .
ls -l config/external/icu/data
rm -f config/external/icu/data/icudt*l.dat
%endif
ccache -s
%if 0%{?do_profiling}
xvfb-run --server-args="-screen 0 1920x1080x24" \
%endif
./mach build -v

# build additional locales
%if %localize
mkdir -p %{buildroot}%{progdir}/browser/extensions
truncate -s 0 %{_tmppath}/translations.{common,other}
# langpack-build can not be done in parallel easily (see https://bugzilla.mozilla.org/show_bug.cgi?id=1660943)
# Therefore, we have to have a separate obj-dir for each language
# We do this, by creating a mozconfig-template with the necessary switches
# and a placeholder obj-dir, which gets copied and modified for each language

# Create mozconfig-template for langbuild
cat << EOF > ${MOZCONFIG}_LANG
mk_add_options MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/../obj_LANG
. \$topsrcdir/browser/config/mozconfig
ac_add_options --prefix=%{_prefix}
ac_add_options --with-l10n-base=$RPM_BUILD_DIR/l10n
ac_add_options --disable-updater
%if %branding
ac_add_options --enable-official-branding
%endif
EOF

sed -r '/^(ja-JP-mac|ga-IE|en-US|)$/d;s/ .*$//' $RPM_BUILD_DIR/%{srcname}-%{orig_version}/browser/locales/shipped-locales \
    | xargs -n 1 %{?jobs:-P %jobs} -I {} /bin/sh -c '
        locale=$1
        cp ${MOZCONFIG}_LANG ${MOZCONFIG}_$locale
        sed -i "s|obj_LANG|obj_$locale|" ${MOZCONFIG}_$locale
        export MOZCONFIG=${MOZCONFIG}_$locale
        # nsinstall is needed for langpack-build. It is already built by `./mach build`, but building it again is very fast
        ./mach build config/nsinstall langpack-$locale
        cp -L ../obj_$locale/dist/linux-*/xpi/firefox-%{orig_version}.$locale.langpack.xpi \
            %{buildroot}%{progdir}/browser/extensions/langpack-$locale@firefox.mozilla.org.xpi
        # remove prefs, profile defaults, and hyphenation from langpack
        #rm -rf %{buildroot}%{progdir}/browser/extensions/langpack-$locale@firefox.mozilla.org/defaults
        #rm -rf %{buildroot}%{progdir}/browser/extensions/langpack-$locale@firefox.mozilla.org/hyphenation
        # check against the fixed common list and sort into the right filelist
        _matched=0
        for _match in ar ca cs da de el en-GB es-AR es-CL es-ES fi fr hu it ja ko nb-NO nl pl pt-BR pt-PT ru sv-SE zh-CN zh-TW; do
            [ "$_match" = "$locale" ] && _matched=1
        done
        [ $_matched -eq 1 ] && _l10ntarget=common || _l10ntarget=other
        echo %{progdir}/browser/extensions/langpack-$locale@firefox.mozilla.org.xpi \
            >> %{_tmppath}/translations.$_l10ntarget
' -- {}
%endif

ccache -s
%endif

%install
cd $RPM_BUILD_DIR/obj
source %{SOURCE4}
export MOZ_SOURCE_STAMP=$RELEASE_TAG
export MOZ_SOURCE_REPO=$RELEASE_REPO
# need to remove default en-US firefox-l10n.js before it gets
# populated into browser's omni.ja; it only contains general.useragent.locale
# which should be loaded from each language pack (set in firefox.js)
rm dist/bin/browser/defaults/preferences/firefox-l10n.js
make -C browser/installer STRIP=/bin/true MOZ_PKG_FATAL_WARNINGS=0
#DEBUG (break the build if searchplugins are missing / temporary)
grep amazondotcom dist/firefox/browser/omni.ja
# copy tree into RPM_BUILD_ROOT
mkdir -p %{buildroot}%{progdir}
cp -rf $RPM_BUILD_DIR/obj/dist/%{srcname}/* %{buildroot}%{progdir}
mkdir -p %{buildroot}%{progdir}/distribution/extensions
mkdir -p %{buildroot}%{progdir}/browser/defaults/preferences/
# renaming executables (for regular vs. ESR)
%if "%{srcname}" != "%{progname}"
mv %{buildroot}%{progdir}/%{srcname} %{buildroot}%{progdir}/%{progname}
mv %{buildroot}%{progdir}/%{srcname}-bin %{buildroot}%{progdir}/%{progname}-bin
%endif
# install gre prefs
install -m 644 %{SOURCE13} %{buildroot}%{progdir}/defaults/pref/
# install browser prefs
install -m 644 %{SOURCE9} %{buildroot}%{progdir}/browser/defaults/preferences/firefox.js

# remove some executable permissions
find %{buildroot}%{progdir} \
     -name "*.js" -o \
     -name "*.jsm" -o \
     -name "*.rdf" -o \
     -name "*.properties" -o \
     -name "*.dtd" -o \
     -name "*.txt" -o \
     -name "*.xml" -o \
     -name "*.css" \
     -exec chmod a-x {} +
# remove mkdir.done files from installed base
find %{buildroot}%{progdir} -type f -name ".mkdir.done" -delete
# overwrite the mozilla start-script and link it to /usr/bin
mkdir --parents %{buildroot}/usr/bin
sed "s:%%PREFIX:%{_prefix}:g
s:%%PROGDIR:%{progdir}:g
s:%%APPNAME:%{progname}:g
s:%%PROFILE:.mozilla/firefox:g" \
  %{SOURCE3} > %{buildroot}%{progdir}/%{progname}.sh
chmod 755 %{buildroot}%{progdir}/%{progname}.sh
ln -sf ../..%{progdir}/%{progname}.sh %{buildroot}%{_bindir}/%{progname}
# desktop file
mkdir -p %{buildroot}%{_datadir}/applications
sed "s:%%NAME:%{appname}:g
s:%%EXEC:%{progname}:g
s:%%ICON:%{progname}:g" \
  %{SOURCE1} > %{buildroot}%{_datadir}/applications/%{desktop_file_name}.desktop
%suse_update_desktop_file %{desktop_file_name} Network WebBrowser GTK
# additional mime-types
mkdir -p %{buildroot}%{_datadir}/mime/packages
cp %{SOURCE8} %{buildroot}%{_datadir}/mime/packages/%{progname}.xml
# appdata
mkdir -p %{buildroot}%{_datadir}/metainfo
sed "s:firefox.desktop:%{desktop_file_name}:g" \
  %{SOURCE15} > %{buildroot}%{_datadir}/metainfo/%{desktop_file_name}.appdata.xml
# install man-page
mkdir -p %{buildroot}%{_mandir}/man1/
cp %{SOURCE11} %{buildroot}%{_mandir}/man1/%{progname}.1
##########
# ADDONS
#
mkdir -p %{buildroot}%{_datadir}/mozilla/extensions/%{firefox_appid}
mkdir -p %{buildroot}%{_libdir}/mozilla/extensions/%{firefox_appid}
%if %branding
# Install symbolic icon for GNOME
mkdir -p %{buildroot}%{gnome_dir}/share/icons/hicolor/symbolic/apps/
cp %{_builddir}/%{srcname}-%{orig_version}/browser/branding/official/content/identity-icons-brand.svg \
   %{buildroot}%{gnome_dir}/share/icons/hicolor/symbolic/apps/%{progname}-symbolic.svg
for size in 16 22 24 32 48 64 128 256; do
%else
for size in 16 32 48; do
%endif
  mkdir -p %{buildroot}%{gnome_dir}/share/icons/hicolor/${size}x${size}/apps/
  cp %{buildroot}%{progdir}/browser/chrome/icons/default/default$size.png \
         %{buildroot}%{gnome_dir}/share/icons/hicolor/${size}x${size}/apps/%{progname}.png
done
# excludes
rm -f %{buildroot}%{progdir}/updater.ini
rm -f %{buildroot}%{progdir}/removed-files
rm -f %{buildroot}%{progdir}/README.txt
rm -f %{buildroot}%{progdir}/old-homepage-default.properties
rm -f %{buildroot}%{progdir}/run-mozilla.sh
rm -f %{buildroot}%{progdir}/LICENSE
rm -f %{buildroot}%{progdir}/precomplete
rm -f %{buildroot}%{progdir}/update-settings.ini
%if 0%{?devpkg}
# devel
mkdir -p %{buildroot}%{_bindir}
install -m 755 %SOURCE12 %{buildroot}%{_bindir}
# inspired by mandriva
mkdir -p %{buildroot}%{_sysconfdir}/rpm
cat <<'FIN' >%{buildroot}%{_sysconfdir}/rpm/macros.%{progname}
# Macros from %{name} package
%%firefox_major              %{major}
%%firefox_version            %{version}
%%firefox_mainver            %{mainver}
%%firefox_mozillapath        %%{_libdir}/%{progname}
%%firefox_pluginsdir         %%{_libdir}/mozilla/plugins
%%firefox_appid              \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%%firefox_extdir             %%(if [ "%%_target_cpu" = "noarch" ]; then echo %%{_datadir}/mozilla/extensions/%%{firefox_appid}; else echo %%{_libdir}/mozilla/extensions/%%{firefox_appid}; fi)

%%firefox_ext_install() \
   extdir="%%{buildroot}%%{firefox_extdir}/`mozilla-get-app-id '%%1'`" \
   mkdir -p "$extdir" \
   %%{__unzip} -q -d "$extdir" "%%1" \
   %%{nil}
FIN
%endif
# fdupes
%fdupes %{buildroot}%{progdir}
%fdupes %{buildroot}%{_datadir}
# create breakpad debugsymbols
%if %crashreporter
SYMBOLS_NAME="firefox-%{version}-` echo '%{release}' | sed 's@\.[^\.]\+$@@' `.%{_arch}-%{suse_version}-symbols"
make buildsymbols \
  SYMBOL_INDEX_NAME="$SYMBOLS_NAME.txt" \
  SYMBOL_FULL_ARCHIVE_BASENAME="$SYMBOLS_NAME-full" \
  SYMBOL_ARCHIVE_BASENAME="$SYMBOLS_NAME"
if [ -e dist/*symbols.zip ]; then
  mkdir -p %{buildroot}%{_datadir}/mozilla/
  cp dist/*symbols.zip %{buildroot}%{_datadir}/mozilla/
fi
%endif

%clean
rm -rf %{buildroot}
%if %localize
rm -rf %{_tmppath}/translations.*
%endif

%post
# update mime and desktop database
%mime_database_post
%desktop_database_post
%icon_theme_cache_post
exit 0

%postun
%icon_theme_cache_postun
%desktop_database_postun
%mime_database_postun
exit 0

%files
%defattr(-,root,root)
%dir %{progdir}
%dir %{progdir}/browser/
%dir %{progdir}/browser/chrome/
%{progdir}/browser/defaults
%{progdir}/browser/features/
%{progdir}/browser/chrome/icons
%{progdir}/browser/omni.ja
%dir %{progdir}/distribution/
%{progdir}/distribution/extensions/
%{progdir}/defaults/
%dir %{progdir}/gtk2
%{progdir}/gtk2/libmozgtk.so
%{progdir}/gmp-clearkey/
%attr(755,root,root) %{progdir}/%{progname}.sh
%{progdir}/%{progname}
%{progdir}/%{progname}-bin
%{progdir}/application.ini
%{progdir}/dependentlibs.list
%{progdir}/*.so
%{progdir}/omni.ja
%{progdir}/fonts/
%{progdir}/pingsender
%{progdir}/platform.ini
%{progdir}/plugin-container
%if %crashreporter
%{progdir}/crashreporter
%{progdir}/crashreporter.ini
%{progdir}/Throbber-small.gif
%{progdir}/minidump-analyzer
%{progdir}/browser/crashreporter-override.ini
%endif
%{_datadir}/applications/%{desktop_file_name}.desktop
%{_datadir}/mime/packages/%{progname}.xml
%dir %{_datadir}/mozilla
%dir %{_datadir}/mozilla/extensions
%dir %{_datadir}/mozilla/extensions/%{firefox_appid}
%dir %{_libdir}/mozilla
%dir %{_libdir}/mozilla/extensions
%dir %{_libdir}/mozilla/extensions/%{firefox_appid}
%{gnome_dir}/share/icons/hicolor/
%{_bindir}/%{progname}
%doc %{_mandir}/man1/%{progname}.1.gz
%{_datadir}/metainfo/

%if 0%{?devpkg}
%files devel
%defattr(-,root,root)
%{_bindir}/mozilla-get-app-id
%config %{_sysconfdir}/rpm/macros.%{progname}
%endif

%if %localize
%files translations-common -f %{_tmppath}/translations.common
%defattr(-,root,root)
%dir %{progdir}
%dir %{progdir}/browser/extensions/

%files translations-other -f %{_tmppath}/translations.other
%defattr(-,root,root)
%dir %{progdir}
%dir %{progdir}/browser/extensions/
%endif

# this package does not need to provide files but is needed to fulfill
# requirements if no other branding package is to be installed
%files branding-upstream
%defattr(-,root,root)
%dir %{progdir}

%if %crashreporter
%files buildsymbols
%defattr(-,root,root)
%{_datadir}/mozilla/*.zip
%endif

%changelog
