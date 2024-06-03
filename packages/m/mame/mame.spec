#
# spec file for package mame
#
# Copyright (c) 2024 SUSE LLC
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


%define ver     266
Name:           mame
Version:        0.%{ver}
Release:        0
Summary:        Multiple Arcade Machine Emulator
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Emulators/Other
URL:            https://mamedev.org
Source0:        https://github.com/mamedev/%{name}/archive/%{name}0%{ver}.tar.gz#/%{name}-%{name}0%{ver}.tar.gz
Source1:        https://github.com/mamedev/%{name}/releases/download/%{name}0%{ver}/whatsnew_0%{ver}.txt
Source2:        %{name}.svg
Source3:        %{name}.ini.in
# PATCH-FIX-OPENSUSE use_thin_archives.patch -- use thin archives for static libraries
Patch0:         use_thin_archives.patch
# PATCH-FIX-UPSTREAM fix-922619.patch -- https://github.com/mamedev/mame/issues/3157
Patch1:         fix-922619.patch
# PATCH-FIX-OPENSUSE fix_lua_misspelling.patch -- introduced in mame 0.238
Patch2:         fix_lua_misspelling.patch
Patch3:         %{name}-fortify.patch
Patch4:         %{name}-bgfx.patch
Patch5:         reproducible.patch
BuildRequires:  asio-devel
BuildRequires:  binutils-gold
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  portmidi-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(glm)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(sdl2) >= 2.0.14
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-data = %{version}
Suggests:       %{name}-tools = %{version}
ExcludeArch:    i586 armv6hl armv7hl ppc
%if 0%{?sle_version} > 150000 && 0%{?sle_version} < 160000
BuildRequires:  gcc13
BuildRequires:  gcc13-c++
%endif

%description
MAME is an emulator designed to recreate the hardware of arcade game
systems in software on modern personal computers. The source code to
MAME serves as this hardware documentation. The fact that the
software is usable serves primarily to validate the accuracy of the
documentation.

%package tools
Summary:        MAME Tools
Group:          System/Emulators/Other

%description tools
Tools for use with MAME/MESS roms and images.

%package data
Summary:        Data files required by all builds of MAME
Group:          System/Emulators/Other
BuildArch:      noarch

%description data
This package contains all data files needed by the MAME binaries:
 * shaders
 * artwork
 * rom hashes
 * languages

%prep
%autosetup -p1 -n %{name}-%{name}0%{ver}
rm -r 3rdparty/{asio,compat,dxsdk,expat,flac,glm,libjpeg,portaudio,portmidi,pugixml,rapidjson,sqlite3,tap-windows6,utf8proc,zlib} docs/themes

%build
%define _lto_cflags %{nil}
MY_OPT_FLAGS=$(echo %{optflags} | sed -re 's@-g($|[0-9])@-g1@g; s@-g\s@-g1 @g')
MY_OPT_FLAGS=$(echo $MY_OPT_FLAGS | sed 's@ -Wp,-D_GLIBCXX_ASSERTIONS@@')
MY_LDFLAGS="${LDFLAGS} -Wl,-v -fuse-ld=gold -Wl,--no-map-whole-files -Wl,--no-keep-memory -Wl,--no-keep-files-mapped -Wl,--no-mmap-output-file"
sed -i "s@-Wall -Wextra -Os \$(MPARAM)@$MY_OPT_FLAGS@" 3rdparty/genie/build/gmake.linux/genie.make
sed -i "s@-s -rdynamic@$MY_LDFLAGS -rdynamic@" 3rdparty/genie/build/gmake.linux/genie.make

%make_build \
    NOWERROR=1 \
    OPTIMIZE=3 \
    PYTHON_EXECUTABLE=python3 \
    VERBOSE=1 \
    USE_SYSTEM_LIB_ASIO=1 \
    USE_SYSTEM_LIB_EXPAT=1 \
    USE_SYSTEM_LIB_FLAC=1 \
    USE_SYSTEM_LIB_GLM=1 \
    USE_SYSTEM_LIB_JPEG=1 \
    USE_SYSTEM_LIB_PORTAUDIO=1 \
    USE_SYSTEM_LIB_PORTMIDI=1 \
    USE_SYSTEM_LIB_PUGIXML=1 \
    USE_SYSTEM_LIB_RAPIDJSON=1 \
    USE_SYSTEM_LIB_SQLITE3=1 \
    USE_SYSTEM_LIB_UTF8PROC=1 \
    USE_SYSTEM_LIB_ZLIB=1 \
    SDL_INI_PATH="%{_sysconfdir}/%{name};" \
    TOOLS=1 \
%if 0%{?sle_version} > 150000 && 0%{?sle_version} < 160000
    CC="gcc-13" \
    CXX="g++-13" \
%endif
    OPT_FLAGS="$MY_OPT_FLAGS" \
    LDOPTS="$MY_LDFLAGS"

%install
install -pm0644 %{SOURCE1} whatsnew-%{version}.txt
sed -i 's/\r$//' COPYING README.md whatsnew-%{version}.txt

install -Dpm0644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%suse_update_desktop_file -c %{name} 'MAME' 'Multiple Arcade Machine Emulator' %{name} %{name} Game Emulator

sed -e 's|@DATADIR@|%{_datadir}|g; s|@SYSCONFDIR@|%{_sysconfdir}|g' %{SOURCE3} > %{name}.ini
install -Dpm0644 %{name}.ini %{buildroot}%{_sysconfdir}/%{name}/%{name}.ini

install -d %{buildroot}%{_bindir}
for dir in artwork bgfx chds cheats ctrlr effects fonts hash keymaps language plugins roms samples shader
do
    install -d %{buildroot}%{_datadir}/%{name}/$dir
done
install -d %{buildroot}%{_mandir}/man{1,6}

install -pm0755 %{name} %{buildroot}%{_bindir}/%{name}
install -pm0755 castool chdman floptool imgtool jedutil ldresample ldverify nltool nlwav pngcmp romcmp unidasm %{buildroot}%{_bindir}
for tool in regrep split srcclean
do
    install -pm0755 $tool %{buildroot}%{_bindir}/%{name}-$tool
done
pushd artwork
    find -type d -exec install -d %{buildroot}%{_datadir}/%{name}/artwork/{} \;
    find -type f -exec install -pm0644 {} %{buildroot}%{_datadir}/%{name}/artwork/{} \;
popd
pushd bgfx
    find -type d -a ! -wholename \*dx\* -a ! -wholename \*metal\* -exec install -d %{buildroot}%{_datadir}/%{name}/bgfx/{} \;
    find -type f -a ! -wholename \*dx\* -a ! -wholename \*metal\* -exec install -pm0644 {} %{buildroot}%{_datadir}/%{name}/bgfx/{} \;
popd
install -pm0644 hash/* %{buildroot}%{_datadir}/%{name}/hash
install -pm0644 keymaps/* %{buildroot}%{_datadir}/%{name}/keymaps
pushd language
    find -type d -exec install -d %{buildroot}%{_datadir}/%{name}/language/{} \;
    find -type f -name \*.mo -exec install -pm0644 {} %{buildroot}%{_datadir}/%{name}/language/{} \;
    grep -r --include=*.po \"Language: | sed -r 's@(.*)/strings\.po:"Language: ([[:alpha:]]{2}(_[[:alpha:]]{2})?)\\n"@%lang(\2) %{_datadir}/%{name}/language/\1@' > ../%{name}.lang
popd
pushd plugins
    find -type d -exec install -d %{buildroot}%{_datadir}/%{name}/plugins/{} \;
    find -type f -exec install -pm0644 {} %{buildroot}%{_datadir}/%{name}/plugins/{} \;
popd
pushd src/osd/modules/opengl
    install -pm0644 shader/*.?sh %{buildroot}%{_datadir}/%{name}/shader
popd
pushd docs/man
    install -pm0644 castool.1 chdman.1 imgtool.1 floptool.1 jedutil.1 ldresample.1 ldverify.1 romcmp.1 %{buildroot}%{_mandir}/man1
    install -pm0644 %{name}.6 %{buildroot}%{_mandir}/man6
popd

%fdupes -s %{buildroot}%{_datadir}/%{name}

%check
./%{name} -validate

%files
%doc README.md whatsnew-%{version}.txt
%license docs/LICENSE COPYING
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/%{name}.ini
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop

%files data -f %{name}.lang
%doc README.md
%license docs/LICENSE COPYING
%{_datadir}/%{name}

%files tools
%doc README.md
%license docs/LICENSE COPYING
%{_bindir}/castool
%{_bindir}/chdman
%{_bindir}/floptool
%{_bindir}/imgtool
%{_bindir}/jedutil
%{_bindir}/ldresample
%{_bindir}/ldverify
%{_bindir}/nltool
%{_bindir}/nlwav
%{_bindir}/pngcmp
%{_bindir}/%{name}-regrep
%{_bindir}/romcmp
%{_bindir}/%{name}-split
%{_bindir}/%{name}-srcclean
%{_bindir}/unidasm
%{_mandir}/man1/*.1%{?ext_man}

%changelog
