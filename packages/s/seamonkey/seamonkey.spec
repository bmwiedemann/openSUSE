#
# spec file for package seamonkey
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#               2006-2018 Wolfgang Rosenauer
#               2018-2024 Tristan Miller
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

# upstream default is clang (to use gcc for large parts set to 0)
%define clang_build    0

Name:           seamonkey
BuildRequires:  Mesa-devel
BuildRequires:  alsa-devel
BuildRequires:  autoconf213
BuildRequires:  dbus-1-glib-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
# Using system AV1 decoder depends on pending patch from
# https://bugzilla.mozilla.org/show_bug.cgi?id=1559213
#BuildRequires:  dav1d5-devel
BuildRequires:  libiw-devel
BuildRequires:  libnotify-devel
BuildRequires:  libproxy-devel
#BuildRequires:  libvpx-devel # Compile errors with 1.10.0
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200 && 0%{?is_opensuse}
BuildRequires:  libwebp-devel >= 1.0.0
#BuildRequires:  libicu-devel >= 63.1
%endif
BuildRequires:  makeinfo
BuildRequires:  memory-constraints
BuildRequires:  python3-base
BuildRequires:  startup-notification-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-libXt-devel
BuildRequires:  yasm
BuildRequires:  zip
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.18.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:  pkgconfig(gtk+-unix-print-2.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(libffi) > 3.0.9
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  cargo
BuildRequires:  rust >= 1.47
BuildRequires:  rust-cbindgen
BuildRequires:  git
BuildRequires:  nasm >= 2.13
#BuildRequires:  llvm-devel
%if (0%{?sle_version} >= 120000 && 0%{?sle_version} < 150000)
BuildRequires:  clang6-devel
%else
BuildRequires:  clang-devel >= 5
%endif
Provides:       web_browser
Provides:       browser(npapi)
Version:        2.53.18.2
Release:        0
%define releasedate 20240328000000
Summary:        An integrated web browser, composer, mail/news client, and IRC client
License:        MPL-2.0
Group:          Productivity/Networking/Web/Browsers
Url:            https://www.seamonkey-project.org/
Source:         https://archive.mozilla.org/pub/seamonkey/releases/%{version}/source/seamonkey-%{version}.source.tar.xz
Source1:        seamonkey-desktop.tar.bz2
Source2:        spellcheck.js
Source3:        mozilla.sh.in
Source4:        suse-default-prefs.js
Source5:        https://archive.mozilla.org/pub/seamonkey/releases/%{version}/source/seamonkey-%{version}.source-l10n.tar.xz
Source7:        seamonkey-rpmlintrc
Source11:       seamonkey-appdata.tar.bz2
Source12:       seamonkey-GNUmakefile
Patch1:         mozilla-nongnome-proxies.patch
Patch2:         mozilla-ntlm-full-path.patch
Patch3:         seamonkey-lto.patch
Patch4:         seamonkey-man-page.patch
Patch5:         reproducible.patch
Patch6:         mozilla-bmo531915.patch
Patch7:         mozilla-bmo1896958.patch
Patch8:         mozilla-bmo1862601.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         /bin/sh coreutils
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
%define progname %{name}
%define sources_subdir %{name}-%{version}
%define prefix /usr
%define progdir %_libdir/%{progname}
%define libgssapi libgssapi_krb5.so.2
### build options
%define has_system_cairo 0
%define localize 1
%define with_chatzilla 1
%define with_domi 1
### build options end
# It no longer makes sense to include separate language packs because these
# apply only to the main SeaMonkey suite, but not to the integrated Chatzilla
# or Calendar
%if %localize
Provides:       seamonkey-translations-common = %{version}
Obsoletes:      seamonkey-translations-common < 2.53.6
Provides:       seamonkey-translations-other = %{version}
Obsoletes:      seamonkey-translations-other < 2.53.6
Provides:       locale(%{name}:cs;de;el;en_GB;es_AR;es_ES;fi;fr;hu;it;ja;ka;nb_NO;nl;pl;pt_BR;pt_PT;ru;sk;sv_SE;zh_CN;zh_TW)
%endif
%if 0%{?with_chatzilla} == 0
Provides:       seamonkey-irc = %{version}
%endif
%if 0%{?with_domi} == 0
Provides:       seamonkey-dom-inspector = %{version}
%endif
%define __provides_exclude ^lib.*\\.so.*$
%define __requires_exclude ^(libmoz.*|liblgpllibs.*|libxul.*|libld.*|libprldap.*)$
# the following conditions are always met in Factory by definition
BuildRequires:  mozilla-nspr-devel >= 4.13.1
PreReq:         mozilla-nspr >= %(rpm -q --queryformat '%%{VERSION}' mozilla-nspr)
%if 0%{?sle_version} != 150500 && 0%{?is_opensuse}
BuildRequires:  mozilla-nss-devel >= 3.28.6
PreReq:         mozilla-nss >= %(rpm -q --queryformat '%%{VERSION}' mozilla-nss)
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

%if %localize

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

%setup -q -b 1 -b 11 -c

mv %{sources_subdir} mozilla

%if %localize
%setup -q -T -D -c -n %{name}-%{version}/l10n -a 5
%setup -q -T -D
%endif

cd mozilla

cp %{SOURCE12} GNUmakefile

%patch -P 1 -p1
%patch -P 2 -p2
%patch -P 3 -p1
%patch -P 4 -p0
%patch -P 5 -p1
%patch -P 6 -p1

# Fix Rust builds on Tumbleweed; see https://bugzilla.mozilla.org/show_bug.cgi?id=1896958
%if 0%{?suse_version} > 1600
%patch -P 7 -p1
%endif

# Fix --system-icu builds on Tumbleweed; see https://bugzilla.mozilla.org/show_bug.cgi?id=1862601
%if 0%{?suse_version} > 1600
%patch -P 8 -p1
%endif

cat << EOF > .mozconfig
mk_add_options MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZ_MILESTONE_RELEASE=1
mk_add_options MOZ_MAKE_FLAGS=%{?jobs:-j%jobs}
#mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/../obj
ac_add_options --enable-application=comm/suite
ac_add_options --libdir=%{_libdir}
ac_add_options --prefix=%{_prefix}
ac_add_options --mandir=%{_mandir}
%if %localize
ac_add_options --with-l10n-base=$RPM_BUILD_DIR/seamonkey-%{version}/l10n
%endif
ac_add_options --disable-tests
ac_add_options --disable-install-strip
ac_add_options --enable-release
ac_add_options --enable-default-toolkit=cairo-gtk3
ac_add_options --disable-gconf

# Elfhack fails on ix86: https://bugzilla.mozilla.org/show_bug.cgi?id=1706264
%ifarch aarch64 ppc %arm %ix86
ac_add_options --disable-elf-hack
%endif

ac_add_options --disable-debug

ac_add_options --with-system-nspr
%if 0%{?sle_version} != 150500 && 0%{?is_opensuse}
ac_add_options --with-system-nss
%endif
ac_add_options --with-system-zlib
ac_add_options --with-system-bz2
%if 0%{?suse_version} > 1600 || 0%{?sle_version} >= 150200 && 0%{?is_opensuse}
ac_add_options --with-system-webp
ac_add_options --with-system-icu
%endif

# Compile errors with system libvpx-1.10.0
#ac_add_options --with-system-libvpx

# Using system AV1 decoder depends on pending patch from
# https://bugzilla.mozilla.org/show_bug.cgi?id=1559213
# ac_add_options --with-system-av1

# Mozilla's internal JPEG library is used because of the "turbo" patches
# that make it more efficient than the stock system libjpeg:
#  https://bugzilla.mozilla.org/show_bug.cgi?id=573948
#ac_add_options --with-system-jpeg

# The stock system libpng lacks support for APNG, whereas Mozilla's
# internal version suports APNG
#ac_add_options--with-system-png

ac_add_options --disable-crashreporter
ac_add_options --disable-updater
ac_add_options --enable-startup-notification
ac_add_options --enable-alsa
%if %has_system_cairo
ac_add_options --enable-system-cairo
%endif
ac_add_options --enable-libproxy
%if 0%{?with_chatzilla}
ac_add_options --with-irc
%endif
%if %with_domi
ac_add_options --with-dominspector
%endif
ac_add_options --enable-calendar
EOF


%build
# no need to add build time to binaries
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -regex ".*\.c\|.*\.cpp\|.*\.h" \
    -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +

# As of 2.53.3, i586 builds are failing due to out-of-memory issues,
# so we disable LTO.  (This workaround is still necessary as of
# 2.53.7.1.)
%ifarch %ix86
%define _lto_cflags %{nil}
%endif
#
# As of 2.53.13, Tumbleweed builds are failing due to the linker
# issue <https://bugzilla.mozilla.org/show_bug.cgi?id=1778981>
# so we disable LTO.
%if 0%{?suse_version} > 1600
%define _lto_cflags %{nil}
%endif
export SUSE_ASNEEDED=0
export MOZ_BUILD_DATE=%{releasedate}
export MOZILLA_OFFICIAL=1
export BUILD_OFFICIAL=1

export CFLAGS="%{optflags} -fno-strict-aliasing"
%if 0%{?clang_build} == 0
export CC=gcc
export CXX=g++
%if 0%{?gcc_version:%{gcc_version}} >= 12
export CFLAGS="$CFLAGS -fimplicit-constexpr"
%endif
%endif

if [ $(gcc -dumpversion | awk -F. '{print $1}') -ge 6 ]; then
export CFLAGS+=" -fno-delete-null-pointer-checks -fno-lifetime-dse -fno-schedule-insns2"
fi
%ifarch %arm
export CFLAGS="${CFLAGS/-g / }"
%endif
%ifarch %arm %ix86
# Limit RAM usage during link
export LDFLAGS="${LDFLAGS} -Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
%endif
%ifarch ppc64 ppc64le
%if 0%{?clang_build} == 0
export CFLAGS="$CFLAGS -mminimal-toc"
%endif
%endif
export CXXFLAGS="$CFLAGS"

#
%limit_build -m 2000
cd mozilla
make %{?_smp_mflags}

%if %localize
make -j1 locales
%endif
#

%install

cd mozilla

make install DESTDIR=$RPM_BUILD_ROOT

for ext in $RPM_BUILD_ROOT/%{progdir}/extensions/langpack-*@seamonkey.mozilla.org.xpi
do
    lang=${ext##*langpack-}
    lang=${lang%@*}
    lang=${lang/-/_}
    echo "%%lang($lang) ${ext#$RPM_BUILD_ROOT}"
done >../seamonkey.lang

# overwrite the mozilla start-script and link it to /usr/bin
mkdir --parents $RPM_BUILD_ROOT%{_bindir}
sed "s:%%PREFIX:%{prefix}:g
s:%%PROGDIR:%{progdir}:g
s:%%APPNAME:seamonkey:g" \
   %{SOURCE3} > $RPM_BUILD_ROOT%{progdir}/%{progname}.sh
chmod 755 $RPM_BUILD_ROOT%{progdir}/%{progname}.sh
ln -sf ../..%{progdir}/%{progname}.sh $RPM_BUILD_ROOT%{_bindir}/%{progname}
# apply SUSE defaults
sed -e 's,RPM_VERSION,%{version}-%{release},g
#s,GSSAPI,%{libgssapi},g' \
   %{SOURCE4} > suse-default-prefs
cp suse-default-prefs $RPM_BUILD_ROOT%{progdir}/defaults/pref/all-openSUSE.js
rm suse-default-prefs
install -m 644 %{SOURCE2} %{buildroot}%{progdir}/defaults/pref/
# Desktop definition
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -m 644 $RPM_BUILD_DIR/*.desktop \
               $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps/
install -m 644 $RPM_BUILD_DIR/*.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/
#
%suse_update_desktop_file seamonkey          Network WebBrowser GTK
%suse_update_desktop_file seamonkey-mail     Network Email GTK
%suse_update_desktop_file seamonkey-composer Network WebDevelopment GTK
# excludes
rm -f $RPM_BUILD_ROOT%{progdir}/license.txt
rm -f $RPM_BUILD_ROOT%{progdir}/README
rm -f $RPM_BUILD_ROOT%{progdir}/removed-files
rm -f $RPM_BUILD_ROOT%{progdir}/run-mozilla.sh
rm -f $RPM_BUILD_ROOT%{progdir}/seamonkey
rm -f $RPM_BUILD_ROOT%{progdir}/precomplete
rm -f $RPM_BUILD_ROOT%{progdir}/updater
rm -f $RPM_BUILD_ROOT%{progdir}/updater.ini
rm -f $RPM_BUILD_ROOT%{progdir}/update.locale
rm -f $RPM_BUILD_ROOT%{progdir}/update-settings.ini
rm -f $RPM_BUILD_ROOT%{progdir}/icons/updater.png
rm -f $RPM_BUILD_ROOT%{progdir}/dictionaries/*
# Some sites use different partitions for /usr/(lib|lib64) and /usr/share.  Since you
# can't create hardlinks across partitions, we'll do this more than once.
%fdupes $RPM_BUILD_ROOT%{progdir}
%fdupes $RPM_BUILD_ROOT%{_datadir}

#INSTALL APPDATA FILES
mkdir -p %{buildroot}%{_datadir}/appdata
install -m0644 -t %{buildroot}%{_datadir}/appdata/ $RPM_BUILD_DIR/*.appdata.xml

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
%{_datadir}/pixmaps/*.png
%dir %{_datadir}/appdata
%{_datadir}/appdata/*.appdata.xml
%{_mandir}/*/*

%if 0%{?with_chatzilla}
%files irc
%defattr(-,root,root)
%{progdir}/extensions/{59c81df5-4b7a-477b-912d-4e0fdf64e5f2}.xpi
%endif

%if 0%{?with_domi}
%files dom-inspector
%defattr(-,root,root)
%{progdir}/extensions/inspector*.xpi
%endif

%changelog
