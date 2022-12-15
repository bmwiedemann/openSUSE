#
# spec file
#
# Copyright (c) 2022 SUSE LLC
#               2006-2022 Wolfgang Rosenauer <wr@rosenauer.org>
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
%define major          102
%define mainver        %major.6.0
%define orig_version   102.6.0
%define orig_suffix    %{nil}
%define update_channel release
%define source_prefix  thunderbird-%{orig_version}

# PGO builds do not work in TW currently (bmo#1680306)
%define do_profiling   0

# upstream default is clang (to use gcc for large parts set to 0)
%define clang_build    0

%bcond_with only_print_mozconfig

%bcond_without mozilla_tb_kde4
%bcond_with    mozilla_tb_valgrind
%bcond_without mozilla_tb_optimize_for_size

# define if ccache should be used or not
%define useccache     0

# Firefox only supports i686
%ifarch %ix86
ExclusiveArch:  i586 i686
BuildArch:      i686
%{expand:%%global optflags %(echo "%optflags"|sed -e s/i586/i686/) -march=i686 -mtune=generic}
%endif

# general build definitions
%define progname thunderbird
%define pkgname  MozillaThunderbird
%define srcname  thunderbird
%define appname  Thunderbird
%define progdir %{_prefix}/%_lib/%{progname}
%define gnome_dir     %{_prefix}
%define desktop_file_name %{progname}
%define __provides_exclude ^lib.*\\.so.*$
%define __requires_exclude ^(libmoz.*|liblgpllibs.*|libxul.*|libldap.*|libldif.*|libprldap.*|librnp.*)$
%define localize 1
%define crashreporter 0
%define with_pipewire0_3 1
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
BuildRequires:  fdupes
BuildRequires:  memory-constraints
%if 0%{?suse_version} < 1550 && 0%{?sle_version} <= 150400
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++
%endif
%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150300
BuildRequires:  cargo >= 1.59
BuildRequires:  rust >= 1.59
%else
# Newer sle/leap/tw use parallel versioned rust releases which have
# a different method for provides that we can use to request a
# specific version
# minimal requirement:
BuildRequires:  rust+cargo >= 1.59
# actually used upstream:
BuildRequires:  cargo1.63
BuildRequires:  rust1.63
%endif
%if 0%{useccache} != 0
BuildRequires:  ccache
%endif
BuildRequires:  libXcomposite-devel
BuildRequires:  libcurl-devel
BuildRequires:  mozilla-nspr-devel >= 4.34
BuildRequires:  mozilla-nss-devel >= 3.79
BuildRequires:  nasm >= 2.14
BuildRequires:  nodejs >= 10.22.1
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} < 150000
BuildRequires:  python-libxml2
BuildRequires:  python36
%else
BuildRequires:  python3 >= 3.5
BuildRequires:  python3-devel
%endif
BuildRequires:  rust-cbindgen >= 0.24.0
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
%if %{with mozilla_tb_valgrind}
BuildRequires:  pkgconfig(valgrind)
%endif
# libavcodec is required for H.264 support but the
# openSUSE version is currently not able to play H.264
# therefore the Packman version is required
# minimum version of libavcodec is 53
Recommends:     libavcodec-full >= 0.10.16
Version:        %{mainver}
Release:        0
Provides:       MozillaThunderbird-devel = %{version}
Provides:       thunderbird = %{version}
Obsoletes:      MozillaThunderbird-devel < %{version}
Provides:       appdata()
Provides:       appdata(thunderbird.appdata.xml)
%if %{with mozilla_tb_kde4}
# this is needed to match this package with the kde4 helper package without the main package
# having a hard requirement on the kde4 package
%define kde_helper_version 6
Provides:       mozilla-kde4-version = %{kde_helper_version}
%endif
Summary:        An integrated email, news feeds, chat, and newsgroups client
License:        MPL-2.0
Group:          Productivity/Networking/Email/Clients
URL:            https://www.thunderbird.net/
%if !%{with only_print_mozconfig}
Source:         http://ftp.mozilla.org/pub/%{srcname}/releases/%{version}%{orig_suffix}/source/%{srcname}-%{orig_version}%{orig_suffix}.source.tar.xz
Source1:        thunderbird.desktop
Source2:        thunderbird-rpmlintrc
Source3:        mozilla.sh.in
Source4:        tar_stamps
Source6:        suse-default-prefs.js
Source7:        l10n-%{orig_version}%{orig_suffix}.tar.xz
Source9:        thunderbird.appdata.xml
Source13:       spellcheck.js
Source14:       https://github.com/openSUSE/firefox-scripts/raw/4503820/create-tar.sh
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
Patch12:        mozilla-bmo1504834-part3.patch
Patch13:        mozilla-bmo1512162.patch
Patch14:        mozilla-fix-top-level-asm.patch
Patch15:        mozilla-bmo849632.patch
Patch16:        mozilla-bmo998749.patch
Patch17:        mozilla-s390x-skia-gradient.patch
Patch18:        mozilla-libavcodec58_91.patch
Patch19:        mozilla-silence-no-return-type.patch
Patch20:        mozilla-bmo531915.patch
Patch21:        one_swizzle_to_rule_them_all.patch
Patch22:        svg-rendering.patch
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         /bin/sh
PreReq:         coreutils
PreReq:         fileutils
PreReq:         textutils
### build options end
%requires_ge    mozilla-nspr
%requires_ge    mozilla-nss
%requires_ge    libfreetype6
Recommends:     libcanberra0
Recommends:     libotr5
Recommends:     libpulse0
Requires(post): desktop-file-utils
Requires(postun):desktop-file-utils
%define libgssapi libgssapi_krb5.so.2
ExcludeArch:    armv6l armv6hl

%description
Thunderbird is a free, open-source, cross-platform application for
managing email, news feeds, chat, and news groups. It is a local
(rather than browser- or web-based) email application that is powerful
yet easy to use.

%if %localize
%package translations-common
Summary:        Common translations for %{appname}
Group:          System/Localization
Provides:       locale(%{name}:ar;ca;cs;da;de;el;en_GB;es_AR;es_CL;es_ES;fi;fr;hu;it;ja;ko;nb_NO;nl;pl;pt_BR;pt_PT;ru;sv_SE;zh_CN;zh_TW)
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
%patch1 -p1
%if %{with mozilla_tb_kde4}
%patch2 -p1
%endif
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
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
%if %{with mozilla_tb_kde4}
kdehelperversion=$(cat toolkit/xre/nsKDEUtils.cpp | grep '#define KMOZILLAHELPER_VERSION' | cut -d ' ' -f 3)
if test "$kdehelperversion" != %{kde_helper_version}; then
  echo fix kde helper version in the .spec file
  exit 1
fi
%endif

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
export MOZ_REQUIRE_SIGNING=
export MACH_USE_SYSTEM_PYTHON=1
%if 0%{?suse_version} < 1550 && 0%{?sle_version} <= 150400
export CC=gcc-11
%else
%if 0%{?clang_build} == 0
export CC=gcc
export CXX=g++
%if 0%{?gcc_version:%{gcc_version}} >= 12
export CFLAGS="$CFLAGS -fimplicit-constexpr"
%endif
%endif
%endif
%ifarch %arm %ix86
# Limit RAM usage during link
export LDFLAGS="${LDFLAGS} -Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
# A lie to prevent -Wl,--gc-sections being set which requires more memory than 32bit can offer
export GC_SECTIONS_BREAKS_DEBUG_RANGES=yes
%endif
export LDFLAGS="${LDFLAGS} -fPIC -Wl,-z,relro,-z,now"
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
echo "export MOZ_REQUIRE_SIGNING="
echo ""
cat << EOF
%else
%ifarch aarch64 ppc64 ppc64le
%limit_build -m 2500
%else
%limit_build -m 2000
%endif
# TODO: Check if this can be removed
#export MOZ_DEBUG_FLAGS="-pipe"
cat << EOF > $MOZCONFIG
%endif
mk_add_options MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZ_MAKE_FLAGS=%{?jobs:-j%jobs}
mk_add_options MOZ_OBJDIR=$RPM_BUILD_DIR/obj
ac_add_options --disable-bootstrap
ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}
ac_add_options --includedir=%{_includedir}
ac_add_options --enable-application=comm/mail
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
%ifnarch aarch64 ppc64 ppc64le s390x
ac_add_options --disable-elf-hack
%endif
#%endif
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
%if 0%{useccache} != 0
ac_add_options --with-ccache
%endif
ac_add_options --with-system-zlib
ac_add_options --disable-updater
ac_add_options --disable-tests
ac_add_options --enable-alsa
ac_add_options --disable-debug
ac_add_options --disable-necko-wifi
ac_add_options --enable-update-channel=%{update_channel}
ac_add_options --with-unsigned-addon-scopes=app
ac_add_options --allow-addon-sideload
# at least temporary until the "wasi-sysroot" issue is solved
ac_add_options --without-wasm-sandboxed-libraries
%ifarch x86_64 aarch64
ac_add_options --enable-rust-simd
%endif
ac_add_options --enable-official-branding
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
%if %{with mozilla_tb_valgrind}
ac_add_options --disable-jemalloc
ac_add_options --enable-valgrind
%endif
%endif
EOF
%if !%{with only_print_mozconfig}
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
ac_add_options --enable-application=comm/mail
ac_add_options --prefix=%{_prefix}
ac_add_options --with-l10n-base=$RPM_BUILD_DIR/l10n
ac_add_options --disable-updater
ac_add_options --without-wasm-sandboxed-libraries
ac_add_options --enable-official-branding
EOF
mkdir -p $RPM_BUILD_DIR/langpacks_artifacts/

sed -r '/^(ja-JP-mac|en-US|$)/d;s/ .*$//' $RPM_BUILD_DIR/%{source_prefix}/comm/mail/locales/shipped-locales \
    | xargs -n 1 %{?jobs:-P %jobs} -I {} /bin/sh -c '
        locale=$1
        cp ${MOZCONFIG}_LANG ${MOZCONFIG}_$locale
        sed -i "s|obj_LANG|obj_$locale|" ${MOZCONFIG}_$locale
        export MOZCONFIG=${MOZCONFIG}_$locale
        # nsinstall is needed for langpack-build. It is already built by `./mach build`, but building it again is very fast
        ./mach build config/nsinstall langpack-$locale
        cp -L ../obj_$locale/dist/linux-*/xpi/thunderbird-%{orig_version}.$locale.langpack.xpi \
            $RPM_BUILD_DIR/langpacks_artifacts/langpack-$locale@thunderbird.mozilla.org.xpi
        # check against the fixed common list and sort into the right filelist
        _matched=0
        for _match in ar ca cs da de el en-GB es-AR es-CL es-ES fi fr hu it ja ko nb-NO nl pl pt-BR pt-PT ru sv-SE zh-CN zh-TW; do
            [ "$_match" = "$locale" ] && _matched=1
        done
        [ $_matched -eq 1 ] && _l10ntarget=common || _l10ntarget=other
        echo %{progdir}/extensions/langpack-$locale@thunderbird.mozilla.org.xpi \
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
make -C comm/mail/installer STRIP=/bin/true MOZ_PKG_FATAL_WARNINGS=0
# copy tree into RPM_BUILD_ROOT
mkdir -p %{buildroot}%{progdir}
cp -rf $RPM_BUILD_DIR/obj/dist/%{progname}/* %{buildroot}%{progdir}
mkdir -p %{buildroot}%{progdir}/extensions
cp -rf $RPM_BUILD_DIR/langpacks_artifacts/* %{buildroot}%{progdir}/extensions/

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
mkdir --parents %{buildroot}%{_bindir}/
sed "s:%%PREFIX:%{_prefix}:g
s:%%PROGDIR:%{progdir}:g
s:%%APPNAME:%{progname}:g
s:%%WAYLAND_SUPPORTED:%{wayland_supported}:g
s:%%PROFILE:.thunderbird:g" \
  %{SOURCE3} > %{buildroot}%{progdir}/%{progname}.sh
chmod 755 %{buildroot}%{progdir}/%{progname}.sh
ln -sf ../..%{progdir}/%{progname}.sh %{buildroot}%{_bindir}/%{progname}
# desktop file
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE1} \
               %{buildroot}%{_datadir}/applications/%{desktop_file_name}.desktop
%suse_update_desktop_file %{desktop_file_name} Network Email GTK
# appdata
mkdir -p %{buildroot}%{_datadir}/appdata
cp %{SOURCE9} %{buildroot}%{_datadir}/appdata/%{desktop_file_name}.appdata.xml
# apply SUSE defaults
sed -e 's,RPM_VERSION,%{mainversion},g
s,GSSAPI,%{libgssapi},g' \
   %{SOURCE6} > suse-default-prefs
cp suse-default-prefs %{buildroot}%{progdir}/defaults/pref/all-opensuse.js
rm suse-default-prefs
# use correct locale for useragent
cat > %{buildroot}%{progdir}/defaults/pref/all-l10n.js << EOF
pref("general.useragent.locale", "chrome://global/locale/intl.properties");
EOF
#
# Install symbolic icon for GNOME
mkdir -p %{buildroot}%{gnome_dir}/share/icons/hicolor/symbolic/apps/
cp %{_builddir}/%{source_prefix}/comm/mail/branding/thunderbird/TB-symbolic.svg \
   %{buildroot}%{gnome_dir}/share/icons/hicolor/symbolic/apps/%{progname}-symbolic.svg
for size in 16 22 24 32 48 64 128; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/
  cp %{buildroot}%{progdir}/chrome/icons/default/default$size.png \
    %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{progname}.png
done
# excluded files
rm -f %{buildroot}%{progdir}/thunderbird
rm -f %{buildroot}%{progdir}/removed-files
rm -f %{buildroot}%{progdir}/precomplete
rm -f %{buildroot}%{progdir}/updater
rm -f %{buildroot}%{progdir}/updater.ini
rm -f %{buildroot}%{progdir}/update.locale
rm -f %{buildroot}%{progdir}/dictionaries/en-US*
rm -f %{buildroot}%{progdir}/nspr-config
# Some sites use different partitions for /usr/(lib|lib64) and /usr/share.  Since you
# can't create hardlinks across partitions, we'll do this more than once.
%fdupes %{buildroot}%{progdir}
%fdupes %{buildroot}%{_libdir}/mozilla
%fdupes %{buildroot}%{_datadir}

%post
%desktop_database_post
%icon_theme_cache_post
exit 0

%postun
%desktop_database_postun
%icon_theme_cache_postun
exit 0

%files
%defattr(-,root,root)
%attr(755,root,root) %{progdir}/%{progname}.sh
%dir %{progdir}
%{progdir}/application.ini
%{progdir}/dependentlibs.list
%{progdir}/fonts/
%{progdir}/*.so
%{progdir}/omni.ja
%{progdir}/pingsender
%{progdir}/platform.ini
%{progdir}/plugin-container
%{progdir}/rnp-cli
%{progdir}/rnpkeys
%{progdir}/thunderbird-bin
# crashreporter files
%if %crashreporter
%{progdir}/crashreporter
%{progdir}/crashreporter.ini
%{progdir}/minidump-analyzer
%{progdir}/Throbber-small.gif
%endif
%dir %{progdir}/chrome/
%{progdir}/chrome/icons/
%{progdir}/defaults/
%{progdir}/isp/
%{_datadir}/appdata/
%{_datadir}/applications/%{desktop_file_name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{progname}.png
%{_datadir}/icons/hicolor/symbolic/apps/%{progname}-symbolic.svg
%{_bindir}/%{progname}

%if %localize
%files translations-common -f %{_tmppath}/translations.common
%defattr(-,root,root)
%dir %{progdir}/extensions/

%files translations-other -f %{_tmppath}/translations.other
%defattr(-,root,root)
%dir %{progdir}/extensions/
%endif

%changelog
