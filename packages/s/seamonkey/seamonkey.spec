#
# spec file for package seamonkey
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#               2006-2018 Wolfgang Rosenauer
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


%define _use_rust 0
%if 0%{?suse_version} > 1320
%ifarch x86_64
%define _use_rust 1
%endif
%endif

Name:           seamonkey
BuildRequires:  Mesa-devel
BuildRequires:  alsa-devel
BuildRequires:  autoconf213
BuildRequires:  dbus-1-glib-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
BuildRequires:  libidl-devel
BuildRequires:  libiw-devel
BuildRequires:  libnotify-devel
BuildRequires:  libproxy-devel
BuildRequires:  makeinfo
BuildRequires:  memory-constraints
BuildRequires:  python-devel
BuildRequires:  python2-xml
BuildRequires:  startup-notification-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-libXt-devel
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
BuildRequires:  pkgconfig(libffi) > 3.0.9
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(xcomposite)
%if 0%{?_use_rust}
BuildRequires:  cargo
BuildRequires:  rust >= 1.10
BuildRequires:  rust-std
%endif
Provides:       web_browser
Provides:       browser(npapi)
Version:        2.49.4
Release:        0
%define releasedate 20180215000000
Summary:        An integrated web browser, composer, mail/news client, and IRC client
License:        MPL-2.0
Group:          Productivity/Networking/Web/Browsers
Url:            https://www.seamonkey-project.org/
Source:         seamonkey-%{version}-source.tar.xz
Source1:        seamonkey-desktop.tar.bz2
Source2:        spellcheck.js
Source3:        mozilla.sh.in
Source4:        suse-default-prefs.js
Source5:        l10n-%{version}.tar.xz
Source6:        search-addons.tar.bz2
Source7:        seamonkey-rpmlintrc
Source9:        create-tar.sh
Source10:       compare-locales.tar.xz
Source11:       seamonkey-appdata.tar.bz2
Patch1:         mozilla-nongnome-proxies.patch
Patch3:         mozilla-language.patch
Patch4:         mozilla-ntlm-full-path.patch
Patch5:         mozilla-ua-locale.patch
Patch6:         mozilla-no-stdcxx-check.patch
Patch7:         mozilla-reduce-files-per-UnifiedBindings.patch
Patch8:         mozilla-bmo1338655.patch
Patch100:       seamonkey-ua-locale.patch
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
%define prefix /usr
%define progdir %_libdir/%{progname}
%define libgssapi libgssapi_krb5.so.2
### build options
%define has_system_cairo 0
%define localize 1
%define with_chatzilla 0
%define with_domi 0
### build options end
%if 0%{?with_chatzilla} == 0
Obsoletes:      seamonkey-irc < %{version}
%endif
%if 0%{?with_domi} == 0
Obsoletes:      seamonkey-dom-inspector < %{version}
%endif
%define __provides_exclude ^lib.*\\.so.*$
%define __requires_exclude ^(libmoz.*|liblgpllibs.*|libxul.*|libld.*|libprldap.*)$
# the following conditions are always met in Factory by definition
BuildRequires:  mozilla-nspr-devel >= 4.13.1
PreReq:         mozilla-nspr >= %(rpm -q --queryformat '%%{VERSION}' mozilla-nspr)
BuildRequires:  mozilla-nss-devel >= 3.28.6
PreReq:         mozilla-nss >= %(rpm -q --queryformat '%%{VERSION}' mozilla-nss)

%description
SeaMonkey is an all-in-one Internet application suite containing a
web browser, an e-mail and newsgroup client with an included web feed
reader, an HTML editor and web development tools, and an IRC client.
SeaMonkey is a successor to the popular Netscape Communicator and
Mozilla Application Suite, and (unlike its siblings, Firefox and
Thunderbird) retains Mozilla's more traditional-looking interface.
Many Firefox and Thunderbird extensions are compatible with SeaMonkey.

%package irc
Summary:        IRC for SeaMonkey
Group:          Productivity/Networking/IRC
PreReq:         %{name} = %{version}

%description irc
An IRC Client (Chatzilla) for SeaMonkey.

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
Provides:       locale(%{name}:cs;de;en_GB;es_AR;es_ES;fr;hu;it;ja;nl;pl;pt_PT;ru;sv_SE;zh_CN)
PreReq:         %{name} = %{version}

%description translations-common
This package contains several optional languages for the user interface
of SeaMonkey.


%package translations-other
Summary:        Extra translations for SeaMonkey
Group:          System/Localization
Provides:       locale(%{name}:lt;sk)
PreReq:         %{name} = %{version}

%description translations-other
This package contains several optional languages for the user interface
of SeaMonkey.
%endif

%prep
%if %localize
%setup -n seamonkey -b 1 -b 5 -b 10 -b 11 -q
%else
%setup -n seamonkey -b 1 -b11 -q
%endif
# mozilla patches
pushd mozilla
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
popd
# comm patches
%patch100 -p1

%build
%limit_build -m 800
# no need to add build time to binaries
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -regex ".*\.c\|.*\.cpp\|.*\.h" \
    -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +

#
export SUSE_ASNEEDED=0
export MOZ_BUILD_DATE=%{releasedate}
export MOZILLA_OFFICIAL=1
export BUILD_OFFICIAL=1
export CFLAGS="%{optflags} -fno-strict-aliasing"
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
export CFLAGS="$CFLAGS -mminimal-toc"
%endif
export CXXFLAGS="$CFLAGS"
export MOZCONFIG=$RPM_BUILD_DIR/mozconfig

#
cat << EOF > $MOZCONFIG
mk_add_options MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZ_MILESTONE_RELEASE=1
mk_add_options MOZ_MAKE_FLAGS=%{?jobs:-j%jobs}
#mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/../obj
ac_add_options --enable-application=suite
ac_add_options --libdir=%{progdir}
ac_add_options --prefix=%{prefix}
%if %localize
ac_add_options --with-l10n-base=$RPM_BUILD_DIR/l10n
%endif
ac_add_options --disable-tests
ac_add_options --enable-release
%if 0%{?suse_version} > 1320
ac_add_options --enable-default-toolkit=cairo-gtk3
%else
ac_add_options --enable-default-toolkit=cairo-gtk2
%endif
%if 0%{?suse_version} >= 1550
ac_add_options --disable-gconf
%endif
%ifarch %ix86 %arm
%if 0%{?suse_version} > 1230
ac_add_options --disable-optimize
%endif
%endif
%ifarch ppc ppc64 ppc64le aarch64 %arm
ac_add_options --disable-elf-hack
%endif
ac_add_options --disable-debug
#ac_add_options --enable-libxul # removed
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-zlib
#ac_add_options --with-system-jpeg
# ac_add_options--with-system-png # no apng support
#ac_add_options --enable-ldap-experimental # removed
#ac_add_options --disable-installer # removed
#ac_add_options --disable-mochitest # removed
ac_add_options --disable-crashreporter
ac_add_options --disable-updater
ac_add_options --enable-startup-notification
ac_add_options --enable-system-hunspell
ac_add_options --enable-alsa
%if 0%{?_use_rust}
ac_add_options --enable-rust
%endif
#ac_add_options --enable-system-mozldap
%if %has_system_cairo
ac_add_options --enable-system-cairo
%endif
ac_add_options --enable-libproxy
EOF

make -f client.mk build
#

%install
cd obj*
make -C suite/installer STRIP=/bin/true MOZ_PKG_FATAL_WARNINGS=0
# copy tree into RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{progdir}
cp -rf $RPM_BUILD_DIR/seamonkey/obj*/dist/seamonkey/* $RPM_BUILD_ROOT%{progdir}
# remove some executable permissions
find $RPM_BUILD_ROOT%{progdir} \
    -name "*.js" -o \
    -name "*.jsm" -o \
    -name "*.rdf" -o \
    -name "*.properties" -o \
    -name "*.dtd" -o \
    -name "*.txt" -o \
    -name "*.xml" -o \
    -name "*.css" \
    | xargs chmod a-x
# remove mkdir.done files from installed base
find $RPM_BUILD_ROOT%{progdir} -name ".mkdir.done" | xargs rm -f

%if %localize
rm -f %{_tmppath}/translations.*
touch %{_tmppath}/translations.{common,other}
for locale in $(awk '{ print $1; }' ../suite/locales/shipped-locales); do
    case $locale in
        ja-JP-mac|en-US|gl)
        ;;
        *)
            pushd $RPM_BUILD_DIR/compare-locales
            PYTHONPATH=lib \
	        scripts/compare-locales \
                -m ../l10n-merged/$locale \
	            ../seamonkey/suite/locales/l10n.ini ../l10n $locale
	        popd

            LOCALE_MERGEDIR=$RPM_BUILD_DIR/l10n-merged/$locale \
            make -C suite/locales langpack-$locale || continue

            cp -rL dist/xpi-stage/locale-$locale \
                $RPM_BUILD_ROOT%{progdir}/extensions/langpack-$locale@seamonkey.mozilla.org
            rm $RPM_BUILD_ROOT%{progdir}/extensions/langpack-$locale@seamonkey.mozilla.org/chrome/.mkdir.done

            # remove prefs and profile defaults from langpack
            rm -rf $RPM_BUILD_ROOT%{progdir}/extensions/langpack-$locale@seamonkey.mozilla.org/defaults

            # check against the fixed common list and sort into the right filelist
            _matched=0
            for _match in \
                ar ca cs da de en-GB es-AR es-CL es-ES fi fr hu it ja ko nb-NO nl pl pt-BR pt-PT ru sv-SE zh-CN zh-TW;
                do
                [ "$_match" = "$locale" ] && _matched=1
            done

            [ $_matched -eq 1 ] && _l10ntarget=common || _l10ntarget=other
	        echo %{progdir}/extensions/langpack-$locale@seamonkey.mozilla.org \
	            >> %{_tmppath}/translations.$_l10ntarget
    ;;
  esac
done
%endif

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

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_tmppath}/translations.*

%files
%defattr(-,root,root)
%{_bindir}/%{progname}
%dir %{progdir}
%{progdir}/components/
%{progdir}/defaults/
%dir %{progdir}/dictionaries/
%dir %{progdir}/extensions/
%dir %{progdir}/chrome/
#%dir %{progdir}/distribution/
#%dir %{progdir}/distribution/extensions/
#%exclude %{progdir}/distribution/extensions/debugQA@mozilla.org.xpi
%{progdir}/chrome/icons
%{progdir}/extensions/modern@themes.mozilla.org.xpi
%{progdir}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}.xpi
%{progdir}/fonts/
%{progdir}/isp/
%{progdir}/searchplugins/
%{progdir}/application.ini
%{progdir}/blocklist.xml
%{progdir}/chrome.manifest
%{progdir}/dependentlibs.list
%{progdir}/icudt58l.dat
%{progdir}/*.so
#%{progdir}/mozilla-xremote-client
%{progdir}/omni.ja
%{progdir}/platform.ini
%{progdir}/plugin-container
%{progdir}/%{progname}.sh
%{progdir}/seamonkey-bin
%if 0%{?suse_version} > 1320
%dir %{progdir}/gtk2
%{progdir}/gtk2/libmozgtk.so
%endif
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%dir %{_datadir}/appdata
%{_datadir}/appdata/*.appdata.xml

%if 0%{?with_chatzilla}
%files irc
%defattr(-,root,root)
%{progdir}/distribution/extensions/{59c81df5-4b7a-477b-912d-4e0fdf64e5f2}.xpi
%endif

%if 0%{?with_domi}
%files dom-inspector
%defattr(-,root,root)
%{progdir}/distribution/extensions/inspector*.xpi
%endif

%if %localize
%files translations-common -f %{_tmppath}/translations.common
%defattr(-,root,root)

%files translations-other -f %{_tmppath}/translations.other
%defattr(-,root,root)
%endif

%changelog
