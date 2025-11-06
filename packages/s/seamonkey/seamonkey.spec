#
# spec file for package seamonkey
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#               2006-2018 Wolfgang Rosenauer
#               2018-2025 Tristan Miller
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

### build options

# Components to include/exclude
%bcond_without	dominspector
%bcond_without	irc
%bcond_without	localizations

# System vs. bundled libraries
%bcond_without	system_webp
%bcond_without	system_icu
%bcond_without	system_libvpx
%bcond_without	system_ffi
%bcond_without	system_nspr
%bcond_without	system_nss
%bcond_without	system_zlib
# Disable system AV1 on Leap; as of 15.6 dav1d is not yet packaged for it
%if 0%{?suse_version} > 1600
%bcond_without	system_av1
%endif
%bcond_with     system_jpeg
%bcond_with     system_png

# Compiler/linker options
%bcond_with     clang
%bcond_without  lto
%bcond_with     gold


%define progname       %{name}
%define sources_subdir %{name}-%{version}
%define progdir        %_libdir/%{progname}
%define gnome_dir      %{_prefix}
### build options end

%define releasedate 20251031000000

Name:           seamonkey
Summary:        An integrated web browser, composer, mail/news client, and IRC client
Version:        2.53.22
Release:        0
License:        MPL-2.0
Group:          Productivity/Networking/Web/Browsers
URL:            https://www.seamonkey-project.org/

Source0:        https://archive.mozilla.org/pub/seamonkey/releases/%{version}/source/seamonkey-%{version}.source.tar.xz
Source1:        https://archive.mozilla.org/pub/seamonkey/releases/%{version}/source/seamonkey-%{version}.source-l10n.tar.xz
Source2:        spellcheck.js
Source3:        mozilla.sh.in
Source4:        suse-default-prefs.js
Source5:        seamonkey-rpmlintrc
Source6:        seamonkey-appdata.tar.bz2
Source7:        seamonkey-GNUmakefile
Source8:        seamonkey.desktop.in
Source9:        seamonkey-composer.desktop.in
Source10:       seamonkey-mail.desktop.in
# Ready-made desktop files for products that don't support
# %%translate_suse_desktop.  You can be prompted for the update during the
# build.
Source11:       seamonkey.desktop
Source12:       seamonkey-composer.desktop
Source13:       seamonkey-mail.desktop

Patch1:         seamonkey-2.0.0-nongnome-proxies.patch
Patch2:         seamonkey-2.1.0-bmo634334.patch
Patch3:         seamonkey-2.53.3-lto.patch
Patch4:         seamonkey-2.53.7.1-man-page.patch
Patch5:         seamonkey-2.53.20-boo1237231.patch
Patch6:         seamonkey-2.53.17.1-bmo531915.patch
Patch7:         seamonkey-2.53.19-bmo1896958.patch
Patch8:         seamonkey-2.53.20-mach-use-python-311.patch
Patch9:         seamonkey-2.53.21-bmo1862601.patch
Patch10:        seamonkey-2.53.21-bmo1927380.patch
Patch11:	seamonkey-2.53.20-system-av1.patch
Patch12:        seamonkey-2.53.21-bmo1332139.patch
Patch13:        seamonkey-2.53.21-bmo1662867.patch

BuildRequires:  Mesa-devel
BuildRequires:  alsa-devel
BuildRequires:  autoconf213
BuildRequires:  dbus-1-glib-devel
BuildRequires:  fdupes
BuildRequires:  hunspell-devel
%if 0%{?suse_version} > 1600 && %{with system_av1}
BuildRequires:  libaom-devel
BuildRequires:  dav1d-devel
%endif
BuildRequires:  libiw-devel
BuildRequires:  libnotify-devel
BuildRequires:  libproxy-devel
%if %{with system_libvpx}
BuildRequires:  libvpx-devel
%endif
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200 && 0%{?is_opensuse}
BuildRequires:  libwebp-devel >= 1.0.0
%endif
%if %{with system_icu}
BuildRequires:  libicu-devel >= 67.1
%endif
BuildRequires:  makeinfo
BuildRequires:  memory-constraints
BuildRequires:  python311-base
BuildRequires:  startup-notification-devel
BuildRequires:  unzip
%if 0%{?suse_version} > 1560
BuildRequires:  translate-suse-desktop
%endif
BuildRequires:  xorg-x11-libXt-devel
BuildRequires:  yasm
BuildRequires:  zip
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.56
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.24
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.30
BuildRequires:  pkgconfig(gtk+-unix-print-2.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
%if %{with system_ffi}
BuildRequires:  pkgconfig(libffi) > 3.0.9
%endif
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(xcomposite)
%if 0%{?suse_version} > 1600
BuildRequires:  cargo1.84
BuildRequires:  rust1.84
%else
BuildRequires:  cargo
BuildRequires:  rust >= 1.76
%endif
BuildRequires:  rust-cbindgen
BuildRequires:  git
BuildRequires:  nasm >= 2.13
BuildRequires:  clang-devel
%if %{with clang}
BuildRequires:  clang
%else
# Use GCC 14 on Tumbleweed because builds of 2.53.21 fail with GCC 15
%if 0%{?suse_version} > 1600
%define gcc_version 14
%endif
BuildRequires:  gcc%{?gcc_version:%gcc_version}-c++
%if %{with gold}
BuildRequires:  binutils-gold
%endif
%endif

PreReq:         /bin/sh coreutils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Provides:       web_browser
Provides:       browser(npapi)
Provides:       seamonkey-mail = %{version}
Obsoletes:      seamonkey-mail <= 2.0
Provides:       seamonkey-spellchecker = %{version}
Obsoletes:      seamonkey-spellchecker <= 2.0
# venkman is discontinued and removed (not merged)
Provides:       seamonkey-venkman = %{version}
Obsoletes:      seamonkey-venkman <= 2.29
Recommends:     libcanberra0
Recommends:     libpulse0
# libavcodec is required for H.264 support but the
# openSUSE version is currently not able to play H.264
# therefore the Packman version is required
# minimum version of libavcodec is 53
Recommends:     libavcodec-full >= 0.10.16
# It no longer makes sense to include separate language packs because these
# apply only to the main SeaMonkey suite, but not to the integrated Chatzilla
# or Calendar
%if %{with localizations}
Provides:       seamonkey-translations-common = %{version}
Obsoletes:      seamonkey-translations-common < 2.53.6
Provides:       seamonkey-translations-other = %{version}
Obsoletes:      seamonkey-translations-other < 2.53.6
Provides:       locale(%{name}:cs;de;el;en_GB;es_AR;es_ES;fi;fr;hu;it;ja;ka;nb_NO;nl;pl;pt_BR;pt_PT;ru;sk;sv_SE;tr;zh_CN;zh_TW)
%endif
%if %{with irc}
Provides:       seamonkey-irc = %{version}
%endif
%if %{with dominspector}
Provides:       seamonkey-dom-inspector = %{version}
%endif
%define __provides_exclude ^lib.*\\.so.*$
%define __requires_exclude ^(libmoz.*|liblgpllibs.*|libxul.*|libld.*|libprldap.*)$
# the following conditions are always met in Factory by definition
%if %{with system_nspr}
BuildRequires:  mozilla-nspr-devel >= 4.13.1
PreReq:         mozilla-nspr >= %(rpm -q --queryformat '%%{VERSION}' mozilla-nspr)
%endif
%if %{with system_nss}
%if 0%{?sle_version} != 150500 && 0%{?is_opensuse}
BuildRequires:  mozilla-nss-devel >= 3.28.6
PreReq:         mozilla-nss >= %(rpm -q --queryformat '%%{VERSION}' mozilla-nss)
%endif
%endif

%description
SeaMonkey is an all-in-one Internet application suite containing a web
browser, an e-mail and newsgroup client with an included web feed
reader and calendar, an HTML editor and web development tools, and an
IRC client.  SeaMonkey is a successor to the popular Netscape
Communicator and Mozilla Application Suite, and (unlike its siblings,
Firefox and Thunderbird) retains Mozilla's more traditional-looking
interface.  Many Thunderbird and (legacy) Firefox extensions are
compatible with SeaMonkey.


%package irc
Summary:        IRC for SeaMonkey
Group:          Productivity/Networking/IRC
PreReq:         %{name} = %{version}

%description irc
An IRC client (Chatzilla) for SeaMonkey.

%package venkman
Summary:        The SeaMonkey JavaScript Debugger
Group:          Development/Tools/Debuggers
PreReq:         %{name} = %{version}

%description venkman
A JavaScript debugger for the SeaMonkey web browser.


%package dom-inspector
Summary:        The SeaMonkey DOM Inspector
Group:          Development/Tools/Navigators
PreReq:         %{name} = %{version}

%description dom-inspector
This is a tool that allows you to inspect the DOM for web pages in
SeaMonkey. This is of great use to people who are doing SeaMonkey
chrome development or web page development.


%if %{with localizations}
%package translations-common
Summary:        Common translations for SeaMonkey
Group:          System/Localization
Provides:       locale(%{name}:cs;de;el;en_GB;es_AR;es_ES;fi;fr;hu;it;ja;nb_NO;nl;pl;pt_BR;pt_PT;ru;sv_SE;zh_CN;zh_TW)
PreReq:         %{name} = %{version}

%description translations-common
This package contains several optional languages for the user interface
of SeaMonkey.


%package translations-other
Summary:        Extra translations for SeaMonkey
Group:          System/Localization
Provides:       locale(%{name}:ka;sk)
PreReq:         %{name} = %{version}

%description translations-other
This package contains several optional languages for the user interface
of SeaMonkey.
%endif


%prep
%setup -q -b 6 -c

mv %{sources_subdir} mozilla

%if %{with localizations}
%setup -q -T -D -c -n %{name}-%{version}/l10n -a 1
%setup -q -T -D
%endif

cd mozilla

cp %{SOURCE7} GNUmakefile

%patch -P 1 -p1
%patch -P 2 -p2
%patch -P 3 -p1
%patch -P 4 -p0
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1

%if %{with system_icu}
%if 0%{?suse_version} >= 1600
%patch -P 9 -p1
%patch -P 10 -p1
%endif
%endif

%if 0%{?suse_version} > 1600 && %{with system_av1}
%patch -P 11 -p1
%endif

%if %{with system_libvpx}
%patch -P 12 -p1
%endif

%patch -P 13 -p1

%define with_sys()   ac_add_options --with%%{!?with_system_%1:out}-system-%1
%define endis_sys()  ac_add_options --%%{?with_system_%1:enable}%%{!?with_system_%1:disable}-system-%1
%define endis()      ac_add_options --%%{?with_%1:enable}%%{!?with_%1:disable}-%1

cat << EOF > .mozconfig
### Various build options
mk_add_options MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZ_MILESTONE_RELEASE=1
mk_add_options MOZ_MAKE_FLAGS=%{?_smp_mflags}
#mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/../obj
ac_add_options --libdir=%{_libdir}
ac_add_options --prefix=%{_prefix}
ac_add_options --mandir=%{_mandir}
ac_add_options --disable-tests
ac_add_options --disable-install-strip
ac_add_options --enable-release
%if %{with localizations}
ac_add_options --with-l10n-base=$RPM_BUILD_DIR/seamonkey-%{version}/l10n
%endif

#ac_add_options --disable-elf-hack

%{expand:%endis  gold}

ac_add_options --disable-debug
ac_add_options --enable-alsa
ac_add_options --enable-default-toolkit=cairo-gtk3
ac_add_options --enable-libproxy


### Features

### Components to include
ac_add_options --enable-application=comm/suite
%{expand:%endis dominspector}
%{expand:%endis irc}
ac_add_options --disable-crashreporter
ac_add_options --disable-updater

# Calendar is always enabled as it's required to build various
# components and addons
ac_add_options --enable-calendar


### System vs. bundled libraries

%{expand:%with_sys   nspr}
%{expand:%with_sys   nss}
%{expand:%with_sys   zlib}
%{expand:%with_sys   icu}
%{expand:%with_sys   libvpx}
%{expand:%with_sys   webp}
%{expand:%endis_sys  ffi}
%if 0%{?suse_version} > 1600
%{expand:%with_sys   av1}
%endif

# Mozilla's internal JPEG library is used because of the "turbo" patches
# that make it more efficient than the stock system libjpeg:
# https://bugzilla.mozilla.org/show_bug.cgi?id=573948
%{expand:%with_sys  jpeg}

# The stock system libpng lacks support for APNG, whereas Mozilla's
# internal version suports APNG
%{expand:%with_sys  png}

EOF

# Prepare desktop files
%if 0%{?suse_version} > 1560
cp %{SOURCE8} seamonkey.desktop.in
cp %{SOURCE9} seamonkey-composer.desktop.in
cp %{SOURCE10} seamonkey-mail.desktop.in
%else
cp %{SOURCE11} seamonkey.desktop
cp %{SOURCE12} seamonkey-composer.desktop
cp %{SOURCE13} seamonkey-mail.desktop
%endif

%build

cd mozilla

# Build desktop files
%if 0%{?suse_version} > 1560
%translate_suse_desktop seamonkey.desktop
%translate_suse_desktop seamonkey-composer.desktop
%translate_suse_desktop seamonkey-mail.desktop
if ! (
      diff seamonkey.desktop %{SOURCE11} ||
      diff seamonkey-composer.desktop %{SOURCE12} ||
      diff seamonkey-mail.desktop %{SOURCE13}
    ); then
cat <<EOF
One or more desktop file translations have been changed.  Please
update the seamonkey*.desktop RPM source files to get translations for
older products.
EOF
  # Commenting out for now per https://build.opensuse.org/request/show/1306584#comment-2191023
  # exit 1
fi
%endif

export MOZ_BUILD_DATE=%{releasedate}
export MOZILLA_OFFICIAL=1
export BUILD_OFFICIAL=1

# no need to add build time to binaries
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -regex ".*\.c\|.*\.cpp\|.*\.h" \
    -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +

# Compiler settings

MOZ_OPT_FLAGS=$RPM_OPT_FLAGS

# Make compiler output less chatty
MOZ_OPT_FLAGS=$(echo $MOZ_OPT_FLAGS | sed -e 's/-Wall//g')

%if %{without clang}
export CC=gcc%{?gcc_version:-%gcc_version}
export CXX=g++%{?gcc_version:-%gcc_version}
%endif

# Linker settings

%define _lto_cflags %{nil}
MOZ_LD_FLAGS=$RPM_LD_FLAGS

# LTO settings
# TODO: Perhaps just let SeaMonkey do this via --enable-lto?
%if %{with lto}
MOZ_LD_FLAGS=$(echo $MOZ_LD_FLAGS | sed -e 's/-flto\b//g')
%if %{with clang}
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -flto=thin"
MOZ_LD_FLAGS="$MOZ_LD_FLAGS -flto=thin -fuse-ld=lld -Wl,-plugin-opt=-import-instr-limit=10"
export AR=llvm-ar
export RANLIB=llvm-ranlib
%else
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -flto=auto -flifetime-dse=1"
MOZ_LD_FLAGS="$MOZ_LD_FLAGS -flto=auto -flifetime-dse=1"
export AR=gcc-ar%{?gcc_version:-%gcc_version}
export RANLIB=gcc-ranlib%{?gcc_version:-%gcc_version}
%endif
%endif

export CFLAGS=$MOZ_OPT_FLAGS
export CXXFLAGS=$MOZ_OPT_FLAGS
export LDFLAGS=$MOZ_LD_FLAGS

%limit_build -m 2000
make %{?_smp_mflags}

%if %{with localizations}
make -j1 locales
%endif


%install

cd mozilla

make install DESTDIR=%{buildroot}

for ext in %{buildroot}/%{progdir}/extensions/langpack-*@seamonkey.mozilla.org.xpi
do
    lang=${ext##*langpack-}
    lang=${lang%@*}
    lang=${lang/-/_}
    echo "%%lang($lang) ${ext#%{buildroot}}"
done >../seamonkey.lang

# overwrite the mozilla start-script and link it to /usr/bin
mkdir --parents %{buildroot}%{_bindir}
sed "s:%%PREFIX:%{_prefix}:g
    s:%%PROGDIR:%{progdir}:g
    s:%%APPNAME:seamonkey:g" \
    %{SOURCE3} > %{buildroot}%{progdir}/%{progname}.sh
chmod 755 %{buildroot}%{progdir}/%{progname}.sh
ln -sf ../..%{progdir}/%{progname}.sh %{buildroot}%{_bindir}/%{progname}
# apply SUSE defaults
sed -e 's,RPM_VERSION,%{version}-%{release},g' \
    %{SOURCE4} > suse-default-prefs
install -D -m 0644 suse-default-prefs %{buildroot}%{progdir}/defaults/pref/all-openSUSE.js
rm suse-default-prefs
install -D -m 0644 %{SOURCE2} %{buildroot}%{progdir}/defaults/pref/spellcheck.js
# Desktop files and icons
install -D -m 0644 seamonkey.desktop %{buildroot}%{_datadir}/applications/seamonkey.desktop
install -D -m 0644 seamonkey-composer.desktop %{buildroot}%{_datadir}/applications/seamonkey-composer.desktop
install -D -m 0644 seamonkey-mail.desktop %{buildroot}%{_datadir}/applications/seamonkey-mail.desktop
for size in 16 22 24 32 48 64 128 256; do
    install -D -m 0644 comm/suite/branding/seamonkey/default${size}.png \
            %{buildroot}%{gnome_dir}/share/icons/hicolor/${size}x${size}/apps/seamonkey.png
done
install -D -m 0644 comm/suite/branding/seamonkey/icons/svg/seamonkey.svg \
        %{buildroot}%{gnome_dir}/share/icons/hicolor/scalable/apps/seamonkey.svg

# excludes
rm -f %{buildroot}%{progdir}/license.txt
rm -f %{buildroot}%{progdir}/README
rm -f %{buildroot}%{progdir}/removed-files
rm -f %{buildroot}%{progdir}/run-mozilla.sh
rm -f %{buildroot}%{progdir}/seamonkey
rm -f %{buildroot}%{progdir}/precomplete
rm -f %{buildroot}%{progdir}/updater
rm -f %{buildroot}%{progdir}/updater.ini
rm -f %{buildroot}%{progdir}/update.locale
rm -f %{buildroot}%{progdir}/update-settings.ini
rm -f %{buildroot}%{progdir}/icons/updater.png
rm -f %{buildroot}%{progdir}/dictionaries/*
# Some sites use different partitions for /usr/(lib|lib64) and /usr/share.  Since you
# can't create hardlinks across partitions, we'll do this more than once.
%fdupes %{buildroot}%{progdir}
%fdupes %{buildroot}%{_datadir}

#INSTALL APPDATA FILES
install -D -m 0644 $RPM_BUILD_DIR/seamonkey.appdata.xml %{buildroot}%{_datadir}/appdata/seamonkey.appdata.xml
install -D -m 0644 $RPM_BUILD_DIR/seamonkey-composer.appdata.xml %{buildroot}%{_datadir}/appdata/seamonkey-composer.appdata.xml
install -D -m 0644 $RPM_BUILD_DIR/seamonkey-mail.appdata.xml %{buildroot}%{_datadir}/appdata/seamonkey-mail.appdata.xml

%files -f seamonkey.lang
%defattr(-,root,root)
%{_bindir}/%{progname}
%dir %{progdir}
%{progdir}/defaults/
%dir %{progdir}/dictionaries/
%dir %{progdir}/extensions/
%dir %{progdir}/chrome/
%{progdir}/chrome/icons
%{progdir}/extensions/modern@themes.mozilla.org.xpi
%{progdir}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}.xpi
%{progdir}/extensions/{e2fda1a4-762b-4020-b5ad-a41df1933103}.xpi
%{progdir}/fonts/
%{progdir}/isp/
%{progdir}/application.ini
%{progdir}/blocklist.xml
%{progdir}/chrome.manifest
%{progdir}/dependentlibs.list
%{progdir}/*.so
%{progdir}/omni.ja
%{progdir}/platform.ini
%{progdir}/plugin-container
%{progdir}/%{progname}.sh
%{progdir}/seamonkey-bin
%{progdir}/libmozgtk.so
%{_datadir}/applications/*.desktop
%{gnome_dir}/share/icons/hicolor/
%dir %{_datadir}/appdata
%{_datadir}/appdata/*.appdata.xml
%{_mandir}/*/*

%if %{with irc}
%files irc
%defattr(-,root,root)
%{progdir}/extensions/{59c81df5-4b7a-477b-912d-4e0fdf64e5f2}.xpi
%endif

%if %{with dominspector}
%files dom-inspector
%defattr(-,root,root)
%{progdir}/extensions/inspector*.xpi
%endif

%changelog
