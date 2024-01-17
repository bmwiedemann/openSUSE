#
# spec file for package efl
#
# Copyright (c) 2022 SUSE LLC
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


%define sover 1
# build doc is disabled due to #897122 once the bug is resolved it can be re enabled
%define build_doc 0
# Build doc needs to be defined for build doc man to work
%define build_doc_man 0
%define gstreamer1_present 1
%define build_examples 1
%if !0%{?suse_version} || 0%{?is_opensuse}
%define physics_present 1
%endif
# Currently we don't need to build any  plugins and theres none that make
# sense to build
%define generic_players_present 0
%define xinput22_present 1
# fedora SLEs 12 don't support xine
%if !0%{?suse_version}
%define xine_present 0
%else
%define xine_present 1
%endif
%ifarch %ix86 x86_64 aarch64 %{arml} ppc
%if !0%{?suse_version} || 0%{?is_opensuse}
%define luajit_present 1
%endif
%endif
%if 0%{?is_opensuse}
%define poppler_present 1
%else
%define poppler_present 0
%endif
%if 0%{?is_opensuse}
%ifarch !aarch64
%define vlc_present 1
%else
%define vlc_present 0
%endif
%else
%define vlc_present 0
%endif
%if 0%{?suse_version} > 1500 || 0%{?fedora_version} > 27 || 0%{?mageia} > 6
%define enable_wayland 1
%endif
# Build with an alternate package names for Mageia
%if 0%{?mageia}
%ifarch x86_64
%define _bit %(getconf LONG_BIT)
%endif
%endif
# If packages are targeted for anything other than openSUSE
%{?!icon_theme_cache_create_ghost:%define icon_theme_cache_create_ghost() touch %{buildroot}%{_datadir}/icons/%{1}/icon-theme.cache}
%{?!icon_theme_cache_post:%define icon_theme_cache_post() gtk-update-icon-cache %{_datadir}/icons/$1 &> /dev/null || :}
Name:           efl
Version:        1.26.3
Release:        0
# TODO: split package to separate packages and specify licenses correctly
Summary:        Enlightenment Foundation Libraries - set of libraries used (not only) by E17
License:        BSD-2-Clause AND LGPL-2.1-only AND Zlib
URL:            https://git.enlightenment.org/core/efl.git
Source:         https://download.enlightenment.org/rel/libs/efl/%{name}-%{version}.tar.xz
Patch1:         efl-no-neon.patch
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  giflib-devel
BuildRequires:  glibc-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  libraw-devel
BuildRequires:  libspectre-devel
BuildRequires:  meson >= 0.47
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libinput) >= 0.6.0
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng) >= 1.2.10
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scim)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tslib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xp)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
Recommends:     %{name}-lang
Provides:       ecore = %{version}
Obsoletes:      ecore < %{version}
Provides:       edje = %{version}
Obsoletes:      edje < %{version}
Provides:       edje-utils = %{version}
Obsoletes:      edje-utils < %{version}
Provides:       eet = %{version}
Obsoletes:      eet < %{version}
Provides:       eeze = %{version}
Obsoletes:      eeze < %{version}
Provides:       efreet = %{version}
Obsoletes:      efreet < %{version}
Provides:       eina = %{version}
Obsoletes:      eina < %{version}
Provides:       elementary = %{version}
Obsoletes:      elementary < %{version}
Provides:       embryo = %{version}
Obsoletes:      embryo < %{version}
Provides:       emotion = %{version}
Obsoletes:      emotion < %{version}
Provides:       ethumb = %{version}
Obsoletes:      ethumb < %{version}
Provides:       evas = %{version}
Obsoletes:      evas < %{version}
Provides:       libecore%{sover} = %{version}
Obsoletes:      libecore%{sover} < %{version}
Provides:       libector%{sover} = %{version}
Obsoletes:      libector%{sover} < %{version}
Provides:       libedje%{sover} = %{version}
Obsoletes:      libedje%{sover} < %{version}
Provides:       libeet%{sover} = %{version}
Obsoletes:      libeet%{sover} < %{version}
Provides:       libeeze%{sover} = %{version}
Obsoletes:      libeeze%{sover} < %{version}
Provides:       libefl%{sover} = %{version}
Obsoletes:      libefl%{sover} < %{version}
Provides:       libefreet%{sover} = %{version}
Obsoletes:      libefreet%{sover} < %{version}
Provides:       libefreet_mime%{sover} = %{version}
Obsoletes:      libefreet_mime%{sover} < %{version}
Provides:       libefreet_trash%{sover} = %{version}
Obsoletes:      libefreet_trash%{sover} < %{version}
Provides:       libeina%{sover} = %{version}
Obsoletes:      libeina%{sover} < %{version}
Provides:       libeio%{sover} = %{version}
Obsoletes:      libeio%{sover} < %{version}
Provides:       libeldbus%{sover} = %{version}
Obsoletes:      libeldbus%{sover} < %{version}
Provides:       libelementary%{sover} = %{version}
Obsoletes:      libelementary%{sover} < %{version}
Provides:       libelput%{sover} = %{version}
Obsoletes:      libelput%{sover} < %{version}
Provides:       libelua%{sover} = %{version}
Obsoletes:      libelua%{sover} < %{version}
Provides:       libembryo%{sover} = %{version}
Obsoletes:      libembryo%{sover} < %{version}
Provides:       libemile%{sover} = %{version}
Obsoletes:      libemile%{sover} < %{version}
Provides:       libemotion%{sover} = %{version}
Obsoletes:      libemotion%{sover} < %{version}
Provides:       libeo%{sover} = %{version}
Obsoletes:      libeo%{sover} < %{version}
Provides:       libeolian%{sover} = %{version}
Obsoletes:      libeolian%{sover} < %{version}
Provides:       libephysics%{sover} = %{version}
Obsoletes:      libephysics%{sover} < %{version}
Provides:       libethumb%{sover} = %{version}
Obsoletes:      libethumb%{sover} < %{version}
Provides:       libethumb_client%{sover} = %{version}
Obsoletes:      libethumb_client%{sover} < %{version}
Provides:       libevas%{sover} = %{version}
Obsoletes:      libevas%{sover} < %{version}
%{?systemd_requires}
%if 0%{?luajit_present}
BuildRequires:  pkgconfig(luajit)
%else
BuildRequires:  pkgconfig(lua5.1)
%endif
%if 0%{?luajit_present}
Recommends:     elua = %{version}
%endif
%if %{build_doc}
BuildRequires:  doxygen
%endif
%if %{poppler_present}
# boo#864299 need libpoppler-cpp0 for Leap / SLE
BuildRequires:  libpoppler-cpp0
BuildRequires:  libpoppler-devel
%endif
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le s390x %{arm} aarch64
BuildRequires:  valgrind
%endif
%if 0%{?physics_present}
BuildRequires:  pkgconfig(bullet) >= 2.80
%endif
%if %{vlc_present}
BuildRequires:  pkgconfig(libvlc)
%endif
%if %{xine_present}
BuildRequires:  pkgconfig(libxine)
%endif
%if 0%{?enable_wayland}
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm) >= 2.4
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client) >= 1.11.0
BuildRequires:  pkgconfig(wayland-cursor) >= 1.11.0
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.10
BuildRequires:  pkgconfig(wayland-scanner) >= 1.11.0
BuildRequires:  pkgconfig(wayland-server) >= 1.11.0
BuildRequires:  pkgconfig(xkbcommon)
%endif
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif

%description
EFL is library collection providing various functionality used (not only)
by Enlightenment 17, Terminology, Tizen mobile platform and much more.

%lang_package

%package %{?mageia:-n %{_lib}%{name}-}devel
Summary:        Headers, pkgconfig files and other files for development with EFL
License:        BSD-2-Clause AND LGPL-2.1-only AND Zlib
Requires:       %{name} = %{version}
Requires:       gettext-devel
Requires:       giflib-devel
Requires:       glibc-devel
Requires:       pkgconfig(dbus-1)
Requires:       pkgconfig(dri)
Requires:       pkgconfig(egl)
Requires:       pkgconfig(fontconfig)
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(fribidi)
Requires:       pkgconfig(glesv2)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(harfbuzz)
Requires:       pkgconfig(libcurl)
Requires:       pkgconfig(libexif)
Requires:       pkgconfig(libpng) >= 1.2.10
Requires:       pkgconfig(libpulse)
Requires:       pkgconfig(librsvg-2.0)
Requires:       pkgconfig(libtiff-4)
Requires:       pkgconfig(libudev)
Requires:       pkgconfig(openssl)
Requires:       pkgconfig(pixman-1)
Requires:       pkgconfig(sdl)
Requires:       pkgconfig(sndfile)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xcomposite)
Requires:       pkgconfig(xcursor)
Requires:       pkgconfig(xdmcp)
Requires:       pkgconfig(xext)
Requires:       pkgconfig(xi)
Requires:       pkgconfig(xinerama)
Requires:       pkgconfig(xp)
Requires:       pkgconfig(xproto)
Requires:       pkgconfig(xrandr)
Requires:       pkgconfig(xscrnsaver)
Requires:       pkgconfig(xtst)
Requires:       pkgconfig(zlib)
Provides:       %{?mageia:%{_lib}}ecore-devel = %{version}
Provides:       %{?mageia:%{_lib}}edbus-devel = %{version}
Provides:       %{?mageia:%{_lib}}edje-devel = %{version}
Provides:       %{?mageia:%{_lib}}eet-devel = %{version}
Provides:       %{?mageia:%{_lib}}eeze-devel = %{version}
Provides:       %{?mageia:%{_lib}}efreet-devel = %{version}
Provides:       %{?mageia:%{_lib}}eina-devel = %{version}
Provides:       %{?mageia:%{_lib}}eio-devel = %{version}
Provides:       %{?mageia:%{_lib}}elementary-devel = %{version}
Provides:       %{?mageia:%{_lib}}embryo-devel = %{version}
Provides:       %{?mageia:%{_lib}}emotion-devel = %{version}
Provides:       %{?mageia:%{_lib}}emotion-generic-players-devel = %{version}
Provides:       %{?mageia:%{_lib}}eo-devel = %{version}
Provides:       %{?mageia:%{_lib}}ethumb-devel = %{version}
Provides:       %{?mageia:%{_lib}}evas-devel = %{version}
Provides:       %{?mageia:%{_lib}}evas-generic-loaders-devel = %{version}
Obsoletes:      %{?mageia:%{_lib}}ecore-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}edbus-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}edje-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}eet-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}eeze-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}efreet-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}eina-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}eio-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}elementary-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}embryo-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}emotion-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}emotion-generic-players-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}eo-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}ethumb-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}evas-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}evas-generic-loaders-devel < %{version}
%if 0%{?luajit_present}
Requires:       pkgconfig(luajit)
%else
Requires:       pkgconfig(lua5.1)
%endif
%if %{xine_present}
Requires:       pkgconfig(libxine)
%endif
%if %{gstreamer1_present}
Requires:       pkgconfig(gstreamer-1.0)
Requires:       pkgconfig(gstreamer-plugins-base-1.0)
%endif
%if 0%{?physics_present}
Requires:       pkgconfig(bullet)
%endif
%if 0%{?physics_present}
Provides:       %{?mageia:%{_lib}}ephysics-devel = %{version}
Obsoletes:      %{?mageia:%{_lib}}ephysics-devel < %{version}
%endif

%description %{?mageia:-n %{_lib}%{name}-}devel
Headers, pkgconfig files and other files needed for development with EFL.

%if %{build_examples}
%package -n elementary-examples
Summary:        Elementary examples
License:        LGPL-2.1-only

%description -n elementary-examples
Examples of usage of Elementary library.
%endif

%package -n elua
Summary:        LuaJIT bindings for the efl
License:        LGPL-2.1-only
Requires:       efl = %{version}

%description -n elua
A set of efl bindings for the LuaJIT environment.

%package -n ecore_imf-module-scim
Summary:        SCIM module for Ecore
License:        BSD-2-Clause

%description -n ecore_imf-module-scim
SCIM input method module for Ecore.

%package -n evas-generic-loaders
Summary:        Set of generic loaders for Evas
License:        GPL-2.0-or-later

%description -n evas-generic-loaders
Set of generic loaders allowing to open XCF, PDF, PS, RAW,
MPG/AVI/OGV/MOV/MKV/WMV.

Useful only for evas library.

This part of the Enlightenment Foundation Libraries.

%if %{generic_players_present}
%package -n emotion-generic-players
Summary:        Set of generic players for Emotion
License:        GPL-2.0-or-later

%description -n emotion-generic-players
Set of generic players (currently VLC is supported) allowing to open video
files through emotion.

Useful only for emotion library.

This part of the Enlightenment Foundation Libraries.
%endif

%if %{build_doc}
%if %{build_doc_man}
%package doc-man
Summary:        EFL reference man pages
License:        BSD-2-Clause

%description doc-man
Documentation in form of man pages describing EFL API.
%endif #build_doc_man

%package doc-html
Summary:        EFL reference man pages
License:        BSD-2-Clause

%description doc-html
Documentation in form of HTML pages describing EFL API.
%endif #build_doc

%if %{build_examples}
%package examples
Summary:        Examples of EFL usage
License:        BSD-2-Clause AND LGPL-2.1-only AND Zlib

%description examples
Examples usage of the EFL library.
%endif

%package testsuite
Summary:        EFL testsuite
License:        BSD-2-Clause AND LGPL-2.1-only AND Zlib
Requires:       lib%{?mageia:%{?_bit}}efreet%{sover} = %{version}

%description testsuite
Testsuite of EFL package.

%package -n enlightenment-theme-upstream
Version:        0.21.0
Release:        0
Summary:        Default Enlightenment theme
License:        BSD-2-Clause AND LGPL-2.1-only
Conflicts:      enlightenment-theme-dft
Provides:       enlightenment-theme = 0.1
Provides:       enlightenment-theme-dft

%description  -n enlightenment-theme-upstream
For use with upstream branding, when using openSUSE themes, when using
openSUSE themes Use the Flat theme instead.

%package -n enlightenment-theme-Flat
Version:        0.21.0
Release:        0
Summary:        Default Enlightenment theme(Flat)
License:        BSD-2-Clause AND LGPL-2.1-only
Provides:       enlightenment-theme
Recommends:     enlightenment-x-Flat-icon-theme

%description  -n enlightenment-theme-Flat
The default theme for enlightenment install when using openSUSE branding.

%package -n enlightenment-x-Flat-icon-theme
Version:        0.21.0
Release:        0
Summary:        A freedesktop.org compatible icon theme
License:        GPL-3.0-only

%description -n enlightenment-x-Flat-icon-theme
Setting this icon theme as your application icon theme in enlightenment will
make all your applications use the same icon set as the enlightenment
Flat (upstream) theme.

Icon themes to match the openSUSE Enlightenment themes are also available.

%prep
%setup -q
%autopatch -p1
# remove __DATE__ and __TIME__
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M')
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
FAKE_DOCDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%a %%b %%d %%Y')
sed -e "s/__TIME__/$FAKE_BUILDTIME/g" \
    -e "s/__DATE__/$FAKE_BUILDDATE/g" \
    -i $(grep -rl '__TIME__\|__DATE__') || :

%build
%if 0%{?enable_wayland}
INCLUDEDIR="-I$(pkg-config --variable=includedir wayland-server)"
INCLUDEDIR+=" -I$(pkg-config --variable=includedir xkbcommon)"
INCLUDEDIR+=" -I$(pkg-config --variable=includedir libinput)"
%endif

# efl intentionally compares string pointers in alot of places rather then strings this stops obs complaining
export CFLAGS="%{optflags}%{?mageia: -g} -Wno-address %{?enable_wayland:$INCLUDEDIR}"

%meson \
%if 0%{?physics_present}
    -Dphysics=true \
%endif
%if !0%{?poppler_present}
    -Devas-loaders-disabler=pdf,webp \
%endif
    -Dharfbuzz=true \
%if 0%{?xinput22_present}
    -Dxinput22=true \
%endif
    -Dsystemd=true \
    -Dfb=true \
%if 0%{?enable_wayland}
    -Ddrm=true \
    -Dwl=true \
    -Dopengl=es-egl \
%endif
%if !0%{?luajit_present}
    -Delua=false \
    -Dlua-interpreter=lua \
%endif
%if %{build_examples}
    -Dbuild-examples=true \
%else
    -Dbuild-examples=false \
%endif
    -Dbuild-tests=true

%meson_build

%install
%meson_install

# delete binary with suid bit set :D
rm -f "%{buildroot}/%{_bindir}/eeze_scanner"

%if %{build_doc}
%if %{build_doc_man}
# copy documentation manually
echo "Copying MAN pages"
/bin/cp -vr doc/man %{buildroot}%{_datadir}/
%endif #build_doc_man

# fix line endings
find doc/html -name '*.eps' | xargs sed -i 's@\r@\n@g'
# remove duplicates
%if 0%{?suse_version}
%fdupes -s doc/html
%if %{build_doc_man}
%fdupes -s %{buildroot}%{_mandir}/
%endif #build_doc_man
%endif
%endif #build_doc

# fix permissions
#%if %{build_examples} || %{build_doc_man}
#find \
#%if %{build_doc_man}
#     %{buildroot}%{_mandir} \
#     doc \
#%endif
#%if %{build_examples}
#     %{buildroot}%{_datadir}/*/examples \
#%endif
#     -type d -exec chmod 0755 {} \;
#find \
#%if %{build_doc_man}
#     %{buildroot}%{_mandir} \
#     doc \
#%endif
#%if %{build_examples}
#     %{buildroot}%{_datadir}/*/examples \
#%endif
#    -type f -exec chmod 0644 {} \;
#%endif

# python gdb pretty printers shouldn't have execute permissions.
chmod 0644 %{buildroot}%{_datadir}/eo/gdb/eo_gdb.py

# create theme version for Flat package
cp %{buildroot}%{_datadir}/elementary/themes/default.edj %{buildroot}%{_datadir}/elementary/themes/Flat.edj

# move icons as openSUSE also ships
mv %{buildroot}/%{_datadir}/icons/Enlightenment-X %{buildroot}/%{_datadir}/icons/Enlightenment-X-Flat
touch %{buildroot}%{_datadir}/icons/Enlightenment-X-Flat/icon-theme.cache

find %{buildroot} -type f -name "*.la" -delete -print

%if 0%{?suse_version}
%{suse_update_desktop_file \
    -N "Elementary Configuration" -G "Elementary Configuration" -r elementary_config Enlightenment Settings DesktopSettings}
%{suse_update_desktop_file \
  -N "Elementary Performance" -G "Elementary Performance" -r elementary_perf Enlightenment Development IDE}
%{suse_update_desktop_file \
  -N "Elementary Test" -G "Elementary Test" -r elementary_test Enlightenment Development IDE}
%fdupes -s %{buildroot}%{_datadir}/icons/Enlightenment-X-Flat
%fdupes -s %{buildroot}%{_datadir}/%{name}/examples
%endif

%find_lang %{name}

%post
/sbin/ldconfig
%if !0%{?mageia}
%systemd_user_post ethumb.service
%endif

%if !0%{?mageia}
%preun
%systemd_user_preun ethumb.service
%endif

%postun
/sbin/ldconfig
%if !0%{?mageia}
%systemd_user_postun ethumb.service
%endif

%{?suse_version:%files}
%{!?suse_version:%files -f %{name}.lang}
%exclude %{_bindir}/elementary_codegen
%exclude %{_bindir}/elementary_test
# evas generic loaders
%exclude %{_libdir}/evas/utils/
%exclude %{_libdir}/libeo_dbg.so.*
%exclude %{_datadir}/ecore_x/checkme
%exclude %{_datadir}/evas/checkme
%exclude %{_datadir}/elementary/themes/*

#%if %{build_examples}
#%exclude %{_datadir}/*/examples
#%endif

%if %{generic_players_present}
%exclude %{_libdir}/emotion/generic_players/
%endif
# separated SCIM dependencies from the main package
%exclude %{_libdir}/ecore_imf/modules/scim

%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_libdir}/ecore
%{_libdir}/ecore_con
%{_libdir}/ecore_evas
%{_libdir}/ecore_imf
%{_libdir}/edje
%{_libdir}/eeze
%{_libdir}/efreet
%{_libdir}/elementary
%{_libdir}/emotion
%{_libdir}/ethumb
%{_libdir}/ethumb_client
%{_libdir}/evas
%{_libdir}/lib*.so.*
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1
%{_datadir}/ecore
%{_datadir}/ecore_x
%{_datadir}/edje
%{_datadir}/elementary
%{_datadir}/embryo
%{_datadir}/emotion
%{_datadir}/eo
%{_datadir}/eolian
%{_datadir}/ethumb
%{_datadir}/evas
%{_datadir}/exactness
%{_datadir}/icons/hicolor/*
%{_datadir}/mime/packages/edje.xml
%{_userunitdir}/ethumb.service

%if 0%{?enable_wayland}
%{_libdir}/ecore_wl2
%endif

%if 0%{?suse_version}
%files lang -f %{name}.lang
%endif

%files %{?mageia:-n %{_lib}%{name}-}devel
%{_bindir}/elementary_codegen
%{_bindir}/elementary_test
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.so
%{_libdir}/libeo_dbg.so.*
%{_libdir}/cmake/
%{_includedir}/efl-1/
%if 0%{?enable_wayland}
%{_includedir}/efl-canvas-wl-1/
%endif
%{_includedir}/ecore-1/
%{_includedir}/ecore-audio-1/
%{_includedir}/ecore-con-1/
%{_includedir}/ecore-evas-1/
%{_includedir}/ecore-fb-1/
%{_includedir}/ecore-file-1/
%{_includedir}/ecore-imf-1/
%{_includedir}/ecore-imf-evas-1/
%{_includedir}/ecore-input-1/
%{_includedir}/ecore-input-evas-1/
%{_includedir}/ecore-ipc-1/
%{_includedir}/ecore-x-1/
%{_includedir}/eldbus-1/
%{_includedir}/elementary-1
%{_includedir}/edje-1/
%{_includedir}/eet-1/
%{_includedir}/eeze-1/
%{_includedir}/efreet-1/
%{_includedir}/eina-1/
%{_includedir}/eio-1/
%{_includedir}/embryo-1/
%{_includedir}/emile-1/
%{_includedir}/emotion-1/
%{_includedir}/eo-1/
%{_includedir}/eolian-1/
# C++ headers
%{_includedir}/ecore-cxx-1/
%{_includedir}/edje-cxx-1/
%{_includedir}/eet-cxx-1/
%{_includedir}/efl-cxx-1/
%{_includedir}/eina-cxx-1/
%{_includedir}/eio-cxx-1/
%{_includedir}/eldbus-cxx-1/
%{_includedir}/elementary-cxx-1/
%{_includedir}/eo-cxx-1/
%{_includedir}/eolian-cxx-1/
%{_includedir}/evas-cxx-1/

%if 0%{?physics_present}
%{_includedir}/ephysics-1/
%endif
%{_includedir}/ethumb-1/
%{_includedir}/ethumb-client-1/
%{_includedir}/evas-1/
%if 0%{?enable_wayland}
%{_includedir}/ecore-drm2-1/
%{_includedir}/ecore-wl2-1/
%endif
%{_includedir}/elput-1/
%{_datadir}/ecore_x/checkme
%{_datadir}/gdb/
%{_datadir}/mime/packages/evas.xml

%files -n elua
%{_datadir}/elua

%files -n ecore_imf-module-scim
%{_libdir}/ecore_imf/modules/scim

%files -n enlightenment-theme-upstream
%{_datadir}/elementary/themes/default.edj

%files -n enlightenment-theme-Flat
%{_datadir}/elementary/themes/Flat.edj

%files -n enlightenment-x-Flat-icon-theme
%{_datadir}/icons/Enlightenment-X-Flat
%ghost %{_datadir}/icons/Enlightenment-X-Flat/icon-theme.cache

%files -n evas-generic-loaders
%{_libdir}/evas/utils/

%if %{generic_players_present}
%files -n emotion-generic-players
%{_libdir}/emotion/generic_players/
%endif

%if %{build_doc}
%if %{build_doc_man}
%files doc-man
%{_mandir}/*/*
%endif #build_doc

%files doc-html
%doc doc/html/*

%endif #build_doc

%if %{build_examples}
%files examples
#%{_datadir}/*/examples
#%exclude %{_datadir}/elementary/examples
%endif

%files testsuite
%{_datadir}/ecore_imf/
%{_datadir}/eeze/
%{_datadir}/efreet/
%{_datadir}/ethumb_client/
%if %{build_examples}
%endif

%changelog
