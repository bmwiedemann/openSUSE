#
# spec file for package MozillaThunderbird
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


# changed with every update
# orig_version vs. mainver: To have beta-builds
# FF70beta3 would be released as FF69.99
# orig_version would be the upstream tar ball
# orig_version 70.0
# orig_suffix b3
# major 69
# mainver %major.99
%define major           68
%define mainver         %major.12.0
%define orig_version    68.12.0
%define orig_suffix     %{nil}
%define update_channel  release
%define source_prefix   thunderbird-%{mainver}

# always build with GCC as SUSE Security Team requires that
%define clang_build 0

# PIE, full relro
%define build_hardened 1

%bcond_with only_print_mozconfig

%bcond_without mozilla_tb_kde4
%bcond_with    mozilla_tb_valgrind
%bcond_without mozilla_tb_optimize_for_size

# general build definitions
%define progname thunderbird
%define pkgname  MozillaThunderbird
%define appname  Thunderbird
%define progdir %{_prefix}/%_lib/%{progname}
%define gnome_dir     %{_prefix}
%define desktop_file_name %{progname}
%define __provides_exclude ^lib.*\\.so.*$
%define __requires_exclude ^(libmoz.*|liblgpllibs.*|libxul.*|libldap.*|libldif.*|libprldap.*)$
%define localize 1
%define crashreporter 0

%define has_system_cairo 0

Name:           %{pkgname}
BuildRequires:  Mesa-devel
BuildRequires:  alsa-devel
BuildRequires:  autoconf213
BuildRequires:  dbus-1-glib-devel
BuildRequires:  fdupes
%if 0%{?suse_version} <= 1320
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  cargo >= 1.34
#BuildRequires:  hunspell-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libcurl-devel
BuildRequires:  libidl-devel
BuildRequires:  libnotify-devel
BuildRequires:  memory-constraints
BuildRequires:  mozilla-nspr-devel >= 4.21
BuildRequires:  mozilla-nss-devel >= 3.44.4
BuildRequires:  nasm >= 2.13
BuildRequires:  nodejs10 >= 10.19.0
BuildRequires:  python-devel
BuildRequires:  python2-xml
BuildRequires:  python3 >= 3.5
BuildRequires:  rust >= 1.34
BuildRequires:  rust-cbindgen >= 0.8.7
BuildRequires:  startup-notification-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-libXt-devel
BuildRequires:  xz
BuildRequires:  yasm
BuildRequires:  zip
%if 0%{?suse_version} < 1550
BuildRequires:  pkgconfig(gconf-2.0) >= 1.2.1
%endif
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.22
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.18.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:  pkgconfig(gtk+-unix-print-2.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libpulse)
%if %{with mozilla_tb_valgrind}
BuildRequires:  pkgconfig(valgrind)
%endif
%if 0%{?suse_version} > 1320
BuildRequires:  llvm-clang-devel >= 3.9.0
%else
# this covers the workaround to compile on Leap 42 in OBS
BuildRequires:  clang4-devel
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
Source:         http://ftp.mozilla.org/pub/%{progname}/releases/%{orig_version}%{orig_suffix}/source/%{progname}-%{orig_version}%{orig_suffix}.source.tar.xz
Source1:        thunderbird.desktop
Source2:        thunderbird-rpmlintrc
Source3:        mozilla.sh.in
Source4:        tar_stamps
Source6:        suse-default-prefs.js
Source7:        l10n-%{version}.tar.xz
Source9:        thunderbird.appdata.xml
Source14:       https://github.com/openSUSE/firefox-scripts/raw/5e54f4a/create-tar.sh
Source20:       https://ftp.mozilla.org/pub/%{progname}/releases/%{orig_version}%{orig_suffix}/source/%{progname}-%{orig_version}%{orig_suffix}.source.tar.xz.asc
Source21:       https://ftp.mozilla.org/pub/%{progname}/releases/%{orig_version}/KEY#/mozilla.keyring
# Gecko/Toolkit
Patch1:         mozilla-nongnome-proxies.patch
Patch2:         mozilla-kde.patch
Patch3:         mozilla-ntlm-full-path.patch
Patch4:         mozilla-openaes-decl.patch
Patch5:         mozilla-aarch64-startup-crash.patch
Patch6:         mozilla-bmo1463035.patch
Patch7:         mozilla-cubeb-noreturn.patch
Patch8:         mozilla-fix-aarch64-libopus.patch
Patch9:         mozilla-disable-wasm-emulate-arm-unaligned-fp-access.patch
Patch10:        mozilla-s390-context.patch
Patch11:        mozilla-s390-bigendian.patch
Patch12:        mozilla-reduce-rust-debuginfo.patch
Patch13:        mozilla-ppc-altivec_static_inline.patch
Patch14:        mozilla-bmo1005535.patch
Patch15:        mozilla-bmo1568145.patch
Patch16:        mozilla-bmo849632.patch
Patch17:        mozilla-bmo1504834-part1.patch
Patch18:        mozilla-bmo1504834-part2.patch
Patch19:        mozilla-bmo1504834-part3.patch
Patch20:        mozilla-bmo1602730.patch
Patch21:        mozilla-bmo1554971.patch
Patch22:        mozilla-nestegg-big-endian.patch
Patch24:        mozilla-fix-top-level-asm.patch
Patch25:        mozilla-bmo1504834-part4.patch
%endif # only_print_mozconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         coreutils fileutils textutils /bin/sh
Recommends:     libcanberra0
Recommends:     libpulse0
### build options
%define has_system_cairo 0
### build options end
Requires:       mozilla-nspr >= %(rpm -q --queryformat '%%{VERSION}' mozilla-nspr)
Requires:       mozilla-nss >= %(rpm -q --queryformat '%%{VERSION}' mozilla-nss)
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
%define libgssapi libgssapi_krb5.so.2

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
Provides:       locale(%{name}:ast;be;bg;br;cak;cy;dsb;et;eu;fy_NL;ga_IE;gd;gl;he;hr;hsb;hy_AM;id;is;ka;kab;kk;lt;ms;nn_NO;rm;ro;si;sk;sl;sq;sr;tr;uk;uz;vi)
Requires:       %{name} = %{version}
Obsoletes:      %{name}-translations < %{version}-%{release}

%description translations-other
This package contains rarely used languages for the user interface
of %{appname}.
%endif

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
%setup -q -n %{source_prefix} -b 7
%else
%setup -q -n %{source_prefix}
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
%ifarch s390x ppc64
%patch11 -p1
%endif
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
%patch24 -p1
%patch25 -p1
%endif # only_print_mozconfig

%build
%if !%{with only_print_mozconfig}
%define _lto_cflags %{nil}
# no need to add build time to binaries
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +
#
%if %{with mozilla_tb_kde4}
kdehelperversion=$(cat toolkit/xre/nsKDEUtils.cpp | grep '#define KMOZILLAHELPER_VERSION' | cut -d ' ' -f 3)
if test "$kdehelperversion" != %{kde_helper_version}; then
  echo fix kde helper version in the .spec file
  exit 1
fi
%endif
%endif # only_print_mozconfig

source %{SOURCE4}

export SUSE_ASNEEDED=0
export MOZ_BUILD_DATE=$RELEASE_TIMESTAMP
export MOZILLA_OFFICIAL=1
export BUILD_OFFICIAL=1
export MOZ_TELEMETRY_REPORTING=1
%if 0%{?suse_version} <= 1320
export CC=gcc-7
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
echo "export LDFLAGS=\"$LDFLAGS\""
echo "export RUSTFLAGS=\"$RUSTFLAGS\""
echo ""
cat << EOF
%else
%limit_build -m 2000
export MOZ_DEBUG_FLAGS="-pipe"
cat << EOF > $MOZCONFIG
%endif
mk_add_options MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZ_MILESTONE_RELEASE=1
%if 0%{?suse_version} > 1320
%ifarch i586
mk_add_options MOZ_MAKE_FLAGS=-j1
%else
mk_add_options MOZ_MAKE_FLAGS=%{?jobs:-j%jobs}
%endif
%endif
mk_add_options MOZ_OBJDIR=$RPM_BUILD_DIR/obj
ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{progdir}
ac_add_options --includedir=%{_includedir}
ac_add_options --enable-application=comm/mail
ac_add_options --enable-calendar
ac_add_options --disable-tests
ac_add_options --disable-debug
ac_add_options --enable-alsa
ac_add_options --enable-default-toolkit=cairo-gtk3
%if 0%{?suse_version} >= 1550
ac_add_options --disable-gconf
%endif
# bmo#1441155 - Disable the generation of Rust debug symbols on Linux32
%ifarch %ix86 %arm
ac_add_options --disable-debug-symbols
%else
ac_add_options --enable-debug-symbols
%endif
%if 0%{?suse_version} > 1549
%ifnarch aarch64 ppc64 ppc64le s390x
ac_add_options --disable-elf-hack
%endif
%endif
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-zlib
%if 0%{?localize}
ac_add_options --with-l10n-base=$RPM_BUILD_DIR/l10n
%endif
ac_add_options --disable-updater
#ac_add_options --with-system-png # no apng support
#ac_add_options --enable-system-hunspell
ac_add_options --enable-startup-notification
ac_add_options --disable-necko-wifi
ac_add_options --enable-update-channel=%{update_channel}
%if %has_system_cairo
ac_add_options --enable-system-cairo
%endif
ac_add_options --with-unsigned-addon-scopes=app
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
%endif
%endif
%if %{with mozilla_tb_valgrind}
ac_add_options --disable-jemalloc
ac_add_options --enable-valgrind
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
./mach build

# build additional locales
%if %localize
mkdir -p %{buildroot}%{progdir}/extensions/
truncate -s 0 %{_tmppath}/translations.{common,other}
sed -r '/^(ja-JP-mac|en-US|$)/d;s/ .*$//' $RPM_BUILD_DIR/%{source_prefix}/comm/mail/locales/shipped-locales \
    | xargs -n 1 -I {} /bin/sh -c '
        locale=$1
        ./mach build langpack-$locale
        cp -rL ../obj/dist/xpi-stage/locale-$locale \
           %{buildroot}%{progdir}/extensions/langpack-$locale@thunderbird.mozilla.org
        # remove prefs and profile defaults from langpack
        rm -rf %{buildroot}%{progdir}/extensions/langpack-$locale@thunderbird.mozilla.org/defaults
        # check against the fixed common list and sort into the right filelist
        _matched=0
        for _match in ar ca cs da de el en-GB es-AR es-CL es-ES fi fr hu it ja ko nb-NO nl pl pt-BR pt-PT ru sv-SE zh-CN zh-TW; do
            [ "$_match" = "$locale" ] && _matched=1
        done
        [ $_matched -eq 1 ] && _l10ntarget=common || _l10ntarget=other
        echo %{progdir}/extensions/langpack-$locale@thunderbird.mozilla.org \
          >> %{_tmppath}/translations.$_l10ntarget
' -- {}
%endif
%endif # only_print_mozconfig

%install
cd $RPM_BUILD_DIR/obj
make -C comm/mail/installer STRIP=/bin/true MOZ_PKG_FATAL_WARNINGS=0
# copy tree into RPM_BUILD_ROOT
mkdir -p %{buildroot}%{progdir}
cp -rf $RPM_BUILD_DIR/obj/dist/%{progname}/* %{buildroot}%{progdir}

%if %localize
# repack the lightning xpi with all available locales (boo#939153) (lp#545778)
_extid="{e2fda1a4-762b-4020-b5ad-a41df1933103}"
rm -rf _lightning
mkdir -p _lightning
unzip -q -d _lightning "%{buildroot}%{progdir}/distribution/extensions/${_extid}.xpi"
_langpacks=$(cd "%{buildroot}%{progdir}/extensions/" && find langpack-* -type d -prune -print|cut -d'-' -f2-|cut -d'@' -f1)
for _loc in $_langpacks ; do
    _dir="%{buildroot}%{progdir}/extensions/langpack-${_loc}@thunderbird.mozilla.org"
    _dir="${_dir}/distribution/extensions/${_extid}"
    test -d "_lightning/chrome/calendar-${_loc}" && continue
    test -d "_lightning/chrome/lightning-${_loc}" && continue
    test -f "${_dir}/chrome.manifest" || continue
    cp -rL "${_dir}"/chrome/{calendar,lightning}-"${_loc}" _lightning/chrome/
    cat "${_dir}/chrome.manifest" >> _lightning/chrome.manifest
done
(cd _lightning && zip -q9r ../"${_extid}.xpi" *)
cp -p "${_extid}.xpi" %{buildroot}%{progdir}/distribution/extensions/
%endif
# remove some executable permissions
find %{buildroot}%{_libdir}/%{progname}  \
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
s:%%APPNAME:thunderbird:g
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
# create breakpad debugsymbols
%if %crashreporter
SYMBOLS_NAME="thunderbird-%{version}-%{release}.%{_arch}-%{suse_version}-symbols"
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
%{progdir}/blocklist.xml
%{progdir}/chrome.manifest
%{progdir}/dependentlibs.list
%{progdir}/fonts/
%dir %{progdir}/gtk2
%{progdir}/gtk2/libmozgtk.so
%{progdir}/*.so
%{progdir}/omni.ja
%{progdir}/pingsender
%{progdir}/platform.ini
%{progdir}/plugin-container
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
%{progdir}/distribution/
%{progdir}/defaults/
%{progdir}/features/
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

%if %crashreporter
%files buildsymbols
%defattr(-,root,root)
%{_datadir}/mozilla/
%endif

%changelog
