#
# spec file for package mame
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define fver    211

# Build mame-mess by default, and use system libraries
%bcond_without  mess
%bcond_without  systemlibs

Name:           mame
Version:        0.%fver
Release:        0
Summary:        Multiple Arcade Machine Emulator
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause
Group:          System/Emulators/Other
Url:            http://mamedev.org/
Source0:        https://github.com/mamedev/mame/archive/mame0%{fver}.tar.gz
Source1:        https://github.com/mamedev/mame/releases/download/mame0%{fver}/whatsnew_0%{fver}.txt
Source2:        mame.png
Source3:        mess.png
Source100:      mame-rpmlintrc
Source101:      mame.ini.in
Source102:      mame.appdata.xml
Source104:      mame-mess.appdata.xml
# PATCH-FIX-UPSTREAM stefan.bruens@rwth-aachen.de gh#mamedev/mame#4771 -- Add a messing dependency on generated file
Patch0:         add_tms57002_hxx_dependecy.patch
Patch1:         fix_mkdir_order.patch
BuildRequires:  binutils-gold
BuildRequires:  fdupes
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  python-xml
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:  gcc-c++
%if %{with systemlibs}
BuildRequires:  libexpat-devel
BuildRequires:  libjpeg8-devel
BuildRequires:  portmidi-devel
BuildRequires:  utf8proc-devel
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
%endif
Suggests:       %{name}-tools = %{version}
# sdlmame was last used at version 0.142
Obsoletes:      sdlmame < %{version}
# ume was last used at version 0.159
Obsoletes:      mame-arcade < %{version}
Obsoletes:      ume < %{version}
Requires:       %{name}-data = %{version}-%{release}
# s390x does not have currently a worker strong enough to satisfy the build constraints
ExcludeArch:    s390x

%description
MAME is an emulator designed to recreate the hardware of arcade game
systems in software on modern personal computers. The source code to
MAME serves as this hardware documentation. The fact that the
software is usable serves primarily to validate the accuracy of the
documentation.

%package tools
Summary:        MAME Tools
Group:          System/Emulators/Other
Requires:       %{name}-data = %{version}-%{release}
# mess-tools was last used at version 0.159
Provides:       mess-tools = %{version}
Obsoletes:      mess-tools < %{version}

%description tools
Tools for use with MAME/MESS roms and images.

%package mess
Summary:        Multi Emulator Super System
Group:          System/Emulators/Other
Requires:       %{name}-data = %{version}-%{release}
# mess was last used at version 0.159
Provides:       mess = %{version}
Obsoletes:      mess < %{version}
# sdlmess was last used at version 0.142
Provides:       sdlmess = %{version}
Obsoletes:      sdlmess < %{version}

%description mess
This is the MESS only build of MAME; it has been compiled without Arcade built in.

MESS is an emulator for many game consoles and computer systems, based on
the MAME core and now a part of MAME. MESS emulates portable and console
gaming systems, computer platforms, and calculators.

%package data
Summary:        Data files required by all builds of MAME
Group:          System/Emulators/Other
BuildArch:      noarch

%description data
This package contains all data files needed by the MAME binaries;
 * shaders
 * artwork
 * rom hashes
 * languages

%prep
%setup -q -n mame-mame0%fver
%patch0 -p0
%patch1 -p0

cp %{SOURCE1} whatsnew-%{version}.txt
# Fix rpmlint warning "wrong-file-end-of-line-encoding"
sed -i 's/\r$//' LICENSE.md README.md whatsnew-%{version}.txt

# Set DATADIR and SYSCONFDIR in ini files
sed -e "s,@DATADIR@,%{_datadir},g"\
    -e "s,@SYSCONFDIR@,%{_sysconfdir},g" %{SOURCE101} > mame.ini

# limit 32bit archs to debug level 1, the linker exhausts the address space otherwise
%ifarch %ix86 %arm
%define myoptflags %(echo %{optflags} | sed -E 's@(-g\\\b)|(-g[0-9])@-g1@g')
%else
%define myoptflags %{optflags}
%endif

#ensure genie uses %optflags
sed -i "s@-Wall -Wextra -Os@%{myoptflags}@" 3rdparty/genie/build/gmake.linux/genie.make
sed -i "s@\. -s@\. %{myoptflags}@" 3rdparty/genie/build/gmake.linux/genie.make

%build
%limit_build -m 1800
# Memory mapped files occupy the limited 32bit address space
%ifarch %ix86 %arm
export LDFLAGS="${LDFLAGS} -Wl,-v -fuse-ld=gold -Wl,--no-keep-files-mapped -Wl,--no-map-whole-files -Wl,--no-mmap-output-file %{?_lto_cflags}"
%else
export LDFLAGS="${LDFLAGS} -Wl,-v -fuse-ld=gold %{?_lto_cflags}"
%endif

export CFLAGS=$(pkg-config --cflags lua)

COMMON_FLAGS="\
    NOWERROR=1 \
    VERBOSE=1 \
    OPTIMIZE=3 \
    %if %{with systemlibs}
    USE_SYSTEM_LIB_EXPAT=1 \
    USE_SYSTEM_LIB_ZLIB=1 \
    USE_SYSTEM_LIB_JPEG=1 \
    USE_SYSTEM_LIB_FLAC=1 \
    USE_SYSTEM_LIB_LUA=1 \
    USE_SYSTEM_LIB_UV=1 \
    USE_SYSTEM_LIB_SQLITE3=1 \
    USE_SYSTEM_LIB_PORTMIDI=1 \
    USE_SYSTEM_LIB_PORTAUDIO=1 \
    USE_SYSTEM_LIB_UTF8PROC=1 \
    %endif
    "
# Bootstrap genie, scripts file has been patched
make %{?_smp_mflags} OPT_FLAGS="%{myoptflags}" $COMMON_FLAGS genie
(cd 3rdparty/genie/; bin/linux/genie embed)
make %{?_smp_mflags} OPT_FLAGS="%{myoptflags}" $COMMON_FLAGS genie

make %{?_smp_mflags} OPT_FLAGS="%{myoptflags}" $COMMON_FLAGS SUBTARGET=arcade TOOLS=1
# Remove static libraries after linking, to save some disk space
find build/ -ipath '*mame_arcade/lib*a' -delete

%if %{with mess}
make %{?_smp_mflags} OPT_FLAGS="%{myoptflags}" $COMMON_FLAGS SUBTARGET=mess
# Remove static libraries after linking, to save some disk space
find build/ -ipath '*mame_mess/lib*a' -delete
%endif

%install
# Rename binaries
%define emu_bin_dir  %{buildroot}%{_bindir}
%define emu_data_dir %{buildroot}%{_datadir}/mame
# Install binaries
%ifarch x86_64
install -Dpm 0755 mamearcade64 %{emu_bin_dir}/mame
%if %{with mess}
install -pm 0755 mess64 %{emu_bin_dir}/mame-mess
%endif
%else
install -Dpm 0755 mamearcade %{emu_bin_dir}/mame
%if %{with mess}
install -pm 0755 mess %{emu_bin_dir}/mame-mess
%endif
%endif
# Tool binaries
install -pm 0755 castool chdman floptool imgtool jedutil ldresample \
                 ldverify romcmp unidasm %{emu_bin_dir}/
for mame_tool in nltool nlwav pngcmp regrep split src2html srcclean
do
  install -pm 0755 $mame_tool %{emu_bin_dir}/mame-$mame_tool
done

# Install manpages
install -dm 0755 %{buildroot}%{_mandir}/{man1,man6}
pushd docs/man/
install -pm 0644 castool.1 chdman.1 floptool.1 imgtool.1 jedutil.1 \
                 ldresample.1 ldverify.1 romcmp.1 %{buildroot}%{_mandir}/man1/
install -pm 0644 mame.6 mess.6 %{buildroot}%{_mandir}/man6/
popd

# Install data required by mame
for dir in artwork chds bgfx cheats crosshair ctrlr fonts hash \
           keymaps language plugins roms samples opengl_shaders
do
  install -dm 0755 %{emu_data_dir}/$dir
done
install -dm 0755 %{emu_data_dir}/bgfx/shaders
install -dm 0755 %{buildroot}%{_datadir}/pixmaps

install -pm 0644 hash/*      %{emu_data_dir}/hash/
install -pm 0644 uismall.bdf %{emu_data_dir}/uismall.bdf
install -pm 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/mame.png
install -pm 0644 keymaps/{LICENSE,README.md}    %{emu_data_dir}/keymaps/
install -pm 0644 keymaps/*LINUX.map             %{emu_data_dir}/keymaps/
cp -ar language %{emu_data_dir}/
find %{emu_data_dir}/language/ -name "*.po" | xargs rm -rf
cp -ar artwork              %{emu_data_dir}/
cp -ar plugins              %{emu_data_dir}/
cp -ar samples              %{emu_data_dir}/
cp -ar bgfx/chains          %{emu_data_dir}/bgfx/
cp -ar bgfx/effects         %{emu_data_dir}/bgfx/
cp -ar bgfx/layouts         %{emu_data_dir}/bgfx/
cp -ar bgfx/shaders/glsl    %{emu_data_dir}/bgfx/shaders/
install -pm 0644 src/osd/modules/opengl/shader/*.{fsh,vsh} %{emu_data_dir}/opengl_shaders/

# Install config file
mkdir -p %{buildroot}%{_sysconfdir}/skel/.%{name}
install -Dpm 0644 mame.ini %{buildroot}%{_sysconfdir}/skel/.%{name}/mame.ini

%suse_update_desktop_file -c mame 'MAME' 'Multiple Arcade Machine Emulator' mame mame Game Emulator
install -Dpm 0644 %{SOURCE102}  %{buildroot}%{_datadir}/appdata/mame.appdata.xml

%if %{with mess}
mkdir -p %{buildroot}%{_sysconfdir}/skel/.mess
install -Dpm 0644 mame.ini   %{buildroot}%{_sysconfdir}/skel/.mess/mess.ini
sed -i -- 's/.mame;/.mess;/g'   %{buildroot}%{_sysconfdir}/skel/.mess/mess.ini
mv %{buildroot}%{_mandir}/man6/mess.6 %{buildroot}%{_mandir}/man6/mame-mess.6
install -Dpm 0644 %{SOURCE3}  %{buildroot}%{_datadir}/pixmaps/mame-mess.png
%suse_update_desktop_file -c mame-mess 'MESS' 'Multi Emulator Super System' mame-mess mame-mess Game Emulator
install -Dpm 0644 %{SOURCE104}  %{buildroot}%{_datadir}/appdata/mame-mess.appdata.xml
%endif

%fdupes -s %{buildroot}/%{_datadir}/mame/bgfx

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%doc README.md whatsnew-%{version}.txt
%license docs/LICENSE LICENSE.md
%{_bindir}/mame
%{_datadir}/pixmaps/mame.png
%{_datadir}/applications/mame.desktop
%dir %{_datadir}/appdata
%{_datadir}/appdata/mame.appdata.xml
%{_mandir}/man6/mame.6%{ext_man}
%if %{without mess}
%{_mandir}/man6/mess.6%{ext_man}
%endif

%files data
%doc README.md
%license docs/LICENSE LICENSE.md
%{_datadir}/mame/
%dir %{_sysconfdir}/skel/.mame
%dir %{_sysconfdir}/skel/.mess
%config(noreplace) %{_sysconfdir}/skel/.mame/mame.ini
%config(noreplace) %{_sysconfdir}/skel/.mess/mess.ini

%files tools
%license docs/LICENSE LICENSE.md
%{_bindir}/castool
%{_bindir}/chdman
%{_bindir}/floptool
%{_bindir}/imgtool
%{_bindir}/jedutil
%{_bindir}/ldresample
%{_bindir}/ldverify
%{_bindir}/mame-nltool
%{_bindir}/mame-nlwav
%{_bindir}/mame-pngcmp
%{_bindir}/mame-regrep
%{_bindir}/mame-split
%{_bindir}/mame-src2html
%{_bindir}/mame-srcclean
%{_bindir}/romcmp
%{_bindir}/unidasm
%{_mandir}/man1/castool.1%{ext_man}
%{_mandir}/man1/chdman.1%{ext_man}
%{_mandir}/man1/floptool.1%{ext_man}
%{_mandir}/man1/imgtool.1%{ext_man}
%{_mandir}/man1/jedutil.1%{ext_man}
%{_mandir}/man1/ldresample.1%{ext_man}
%{_mandir}/man1/ldverify.1%{ext_man}
%{_mandir}/man1/romcmp.1%{ext_man}

%files mess
%if %{with mess}
%doc README.md whatsnew-%{version}.txt
%license docs/LICENSE LICENSE.md
%{_bindir}/mame-mess
%{_datadir}/pixmaps/mame-mess.png
%{_datadir}/applications/mame-mess.desktop
%dir %{_datadir}/appdata
%{_datadir}/appdata/mame-mess.appdata.xml
%{_mandir}/man6/mame-mess.6%{ext_man}
%endif

%changelog
