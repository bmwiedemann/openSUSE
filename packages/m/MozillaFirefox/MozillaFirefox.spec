#
# spec file for package MozillaFirefox
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2006-2022 Wolfgang Rosenauer <wr@rosenauer.org>
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


%define _dwz_low_mem_die_limit  40000000
%define _dwz_max_die_limit     200000000

# changed with every update
# orig_version vs. mainver: To have beta-builds
# FF70beta3 would be released as FF69.99
# orig_version would be the upstream tar ball
# orig_version 70.0
# orig_suffix b3
# major 69
# mainver %major.99
%define major          107
%define mainver        %major.0.1
%define orig_version   107.0.1
%define orig_suffix    %{nil}
%define update_channel release
%define branding       1
%define devpkg         1

# PGO builds do not work in TW currently (bmo#1680306)
%define do_profiling   0

# upstream default is clang (to use gcc for large parts set to 0)
%define clang_build    0

%bcond_with only_print_mozconfig

# define if ccache should be used or not
%define useccache     0

# SLE-12 doesn't have this macro
%{!?_rpmmacrodir: %global _rpmmacrodir %{_rpmconfigdir}/macros.d}

# Firefox only supports i686
%ifarch %ix86
ExclusiveArch:  i586 i686
BuildArch:      i686
%{expand:%%global optflags %(echo "%optflags"|sed -e s/i586/i686/) -march=i686 -mtune=generic -msse2}
%endif
%{expand:%%global optflags %(echo "%optflags"|sed -e s/-Werror=return-type//) }
%{expand:%%global optflags %(echo "%optflags"|sed -e s/-flto=auto//) }

# general build definitions
%define progname firefox
%define appname  Firefox
%define pkgname  MozillaFirefox
%define srcname  firefox
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
%define with_pipewire0_3  1
%define wayland_supported 1
%if 0%{?sle_version} > 0 && 0%{?sle_version} < 150200
# pipewire is too old on Leap <=15.1
%define with_pipewire0_3 0
# Wayland is too old on Leap <=15.1 as well
%define wayland_supported 0
%endif

Name:           %{pkgname}
BuildRequires:  Mesa-devel
BuildRequires:  alsa-devel
BuildRequires:  autoconf213
BuildRequires:  dbus-1-glib-devel
BuildRequires:  dejavu-fonts
BuildRequires:  fdupes
BuildRequires:  memory-constraints
%if 0%{?suse_version} < 1550 && 0%{?sle_version} <= 150400
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++
%endif
%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150300
BuildRequires:  cargo >= 1.61
BuildRequires:  rust >= 1.61
%else
# Newer sle/leap/tw use parallel versioned rust releases which have
# a different method for provides that we can use to request a
# specific version
# minimal requirement:
BuildRequires:  rust+cargo >= 1.61
# actually used upstream:
BuildRequires:  cargo1.64
BuildRequires:  rust1.64
%endif
%if 0%{useccache} != 0
BuildRequires:  ccache
%endif
BuildRequires:  libXcomposite-devel
BuildRequires:  libcurl-devel
BuildRequires:  libiw-devel
BuildRequires:  libproxy-devel
BuildRequires:  makeinfo
BuildRequires:  mozilla-nspr-devel >= 4.35
BuildRequires:  mozilla-nss-devel >= 3.84
BuildRequires:  nasm >= 2.14
BuildRequires:  nodejs >= 10.22.1
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} < 150000
BuildRequires:  python-libxml2
BuildRequires:  python36
%else
BuildRequires:  python3 >= 3.5
BuildRequires:  python3-devel
%endif
BuildRequires:  rust-cbindgen >= 0.24.3
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
BuildRequires:  pkgconfig(glib-2.0) >= 2.22
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
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
%if %{localize}
Source7:        l10n-%{orig_version}%{orig_suffix}.tar.xz
%endif
Source8:        firefox-mimeinfo.xml
Source9:        firefox.js
Source11:       firefox.1
Source12:       mozilla-get-app-id
Source13:       spellcheck.js
Source14:       https://github.com/openSUSE/firefox-scripts/raw/4503820/create-tar.sh
Source15:       firefox-appdata.xml
Source16:       %{name}.changes
Source17:       firefox-search-provider.ini
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
Patch5:         mozilla-fix-aarch64-libopus.patch
Patch6:         mozilla-s390-context.patch
Patch7:         mozilla-pgo.patch
Patch8:         mozilla-reduce-rust-debuginfo.patch
Patch9:         mozilla-bmo1005535.patch
Patch10:        mozilla-bmo1568145.patch
Patch11:        mozilla-bmo1504834-part1.patch
Patch13:        mozilla-bmo1504834-part3.patch
Patch14:        mozilla-bmo1512162.patch
Patch15:        mozilla-fix-top-level-asm.patch
Patch17:        mozilla-bmo849632.patch
Patch18:        mozilla-bmo998749.patch
Patch20:        mozilla-s390x-skia-gradient.patch
Patch21:        mozilla-libavcodec58_91.patch
Patch22:        mozilla-silence-no-return-type.patch
Patch23:        mozilla-bmo531915.patch
Patch25:        one_swizzle_to_rule_them_all.patch
Patch26:        svg-rendering.patch
Patch27:        mozilla-buildfixes.patch
# Firefox/browser
Patch101:       firefox-kde.patch
Patch102:       firefox-branded-icons.patch
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(post): coreutils shared-mime-info desktop-file-utils
Requires(postun):shared-mime-info desktop-file-utils
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
%autopatch -p1
%endif

%build
%if !%{with only_print_mozconfig}
# no need to add build time to binaries
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{pkgname}.changes")"
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
# When doing only_print_mozconfig, this file isn't necessarily available, so skip it
cp %{SOURCE4} .obsenv.sh
%else
# We need to make sure its empty
echo "" > .obsenv.sh
%endif

cat >> .obsenv.sh <<EOF
export CARGO_HOME=${RPM_BUILD_DIR}/%{srcname}-%{orig_version}/.cargo
export MOZ_SOURCE_CHANGESET=\$RELEASE_TAG
export SOURCE_REPO=\$RELEASE_REPO
export source_repo=\$RELEASE_REPO
export MOZ_SOURCE_REPO=\$RELEASE_REPO
export MOZ_BUILD_DATE=\$RELEASE_TIMESTAMP
export MOZILLA_OFFICIAL=1
export BUILD_OFFICIAL=1
export MOZ_TELEMETRY_REPORTING=1
export MACH_USE_SYSTEM_PYTHON=1
export CFLAGS="%{optflags}"
%if 0%{?suse_version} < 1550 && 0%{?sle_version} <= 150400
export CC=gcc-11
%else
%if 0%{?clang_build} == 0
export CC=gcc
export CXX=g++
%if 0%{?gcc_version:%{gcc_version}} >= 12
export CFLAGS="\$CFLAGS -fimplicit-constexpr"
%endif
%endif
%endif
%ifarch %arm %ix86
# Limit RAM usage during link
export LDFLAGS="\$LDFLAGS -Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
# A lie to prevent -Wl,--gc-sections being set which requires more memory than 32bit can offer
export GC_SECTIONS_BREAKS_DEBUG_RANGES=yes
%endif
export LDFLAGS="\$LDFLAGS -fPIC -Wl,-z,relro,-z,now"
%ifarch ppc64 ppc64le
%if 0%{?clang_build} == 0
export CFLAGS="\$CFLAGS -mminimal-toc"
%endif
%endif
export CXXFLAGS="\$CFLAGS"
export MOZCONFIG=$RPM_BUILD_DIR/mozconfig
EOF
# Done with env-variables.
source ./.obsenv.sh

%ifarch aarch64 %arm ppc64 ppc64le
%limit_build -m 2500
%endif

# Generating mozconfig
cat << EOF > $MOZCONFIG
mk_add_options MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZ_MAKE_FLAGS=%{?jobs:-j%jobs}
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/../obj
. \$topsrcdir/browser/config/mozconfig
ac_add_options --disable-bootstrap
ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}
ac_add_options --includedir=%{_includedir}
ac_add_options --enable-release
%if 0%{wayland_supported}
ac_add_options --enable-default-toolkit=cairo-gtk3-wayland
%else
ac_add_options --enable-default-toolkit=cairo-gtk3
%endif
# bmo#1441155 - Disable the generation of Rust debug symbols on Linux32
%ifarch %ix86 %arm
ac_add_options --disable-debug-symbols
%else
ac_add_options --enable-debug-symbols=-g1
%endif
ac_add_options --disable-install-strip
# building with elf-hack started to fail everywhere with FF73
#%if 0%{?suse_version} > 1549
%ifarch %arm %ix86 x86_64
ac_add_options --disable-elf-hack
%endif
#%endif
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
%if 0%{useccache} != 0
ac_add_options --with-ccache
%endif
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
ac_add_options --enable-update-channel=%{update_channel}
ac_add_options --with-mozilla-api-keyfile=%{SOURCE18}
# Google-service currently not available for free anymore
#ac_add_options --with-google-location-service-api-keyfile=%{SOURCE19}
ac_add_options --with-google-safebrowsing-api-keyfile=%{SOURCE19}
ac_add_options --with-unsigned-addon-scopes=app
ac_add_options --allow-addon-sideload
# at least temporary until the "wasi-sysroot" issue is solved
ac_add_options --without-wasm-sandboxed-libraries
%ifarch x86_64 aarch64
ac_add_options --enable-rust-simd
%endif
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

%if %{with only_print_mozconfig}
cat ./.obsenv.sh
cat $MOZCONFIG
%else

%if 0%{useccache} != 0
ccache -s
%endif
%if 0%{?do_profiling}
xvfb-run --server-args="-screen 0 1920x1080x24" \
%endif
./mach build -v

# build additional locales
%if %localize
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
ac_add_options --without-wasm-sandboxed-libraries
%if %branding
ac_add_options --enable-official-branding
%endif
EOF

%ifarch %ix86
%define njobs 1
%else
%define njobs 0%{?jobs:%jobs}
%endif
mkdir -p $RPM_BUILD_DIR/langpacks_artifacts/
sed -r '/^(ja-JP-mac|ga-IE|en-US|)$/d;s/ .*$//' $RPM_BUILD_DIR/%{srcname}-%{orig_version}/browser/locales/shipped-locales \
    | xargs -n 1 %{?njobs:-P %njobs} -I {} /bin/sh -c '
        locale=$1
        cp ${MOZCONFIG}_LANG ${MOZCONFIG}_$locale
        sed -i "s|obj_LANG|obj_$locale|" ${MOZCONFIG}_$locale
        export MOZCONFIG=${MOZCONFIG}_$locale
        # nsinstall is needed for langpack-build. It is already built by `./mach build`, but building it again is very fast
        ./mach build config/nsinstall langpack-$locale
        cp -L ../obj_$locale/dist/linux-*/xpi/firefox-%{orig_version}.$locale.langpack.xpi \
            $RPM_BUILD_DIR/langpacks_artifacts/langpack-$locale@firefox.mozilla.org.xpi
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

%if 0%{useccache} != 0
ccache -s
%endif
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
mkdir -p %{buildroot}%{progdir}/browser/extensions
cp -rf $RPM_BUILD_DIR/langpacks_artifacts/* %{buildroot}%{progdir}/browser/extensions/
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
s:%%WAYLAND_SUPPORTED:%{wayland_supported}:g
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
# install GNOME Shell search provider
mkdir -p %{buildroot}%{_datadir}/gnome-shell/search-providers
cp %{SOURCE17} %{buildroot}%{_datadir}/gnome-shell/search-providers
##########
# ADDONS
#
mkdir -p %{buildroot}%{_datadir}/mozilla/extensions/%{firefox_appid}
mkdir -p %{buildroot}%{_libdir}/mozilla/extensions/%{firefox_appid}
# Install symbolic icon for GNOME
%if %branding
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
mkdir -p %{buildroot}%{_rpmmacrodir}
cat <<'FIN' >%{buildroot}%{_rpmmacrodir}/macros.%{progname}
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
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/*.ini
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
%{_rpmmacrodir}/macros.%{progname}
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

%changelog
