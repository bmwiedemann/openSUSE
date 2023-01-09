#
# spec file for package carla
#
# Copyright (c) 2023 SUSE LLC
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


%if 0%{?suse_version} > 1501
%bcond_without liblo
%else
%bcond_with liblo
%endif

%define __provides_exclude_from ^%{_libdir}/carla/jack/.*.so.0$
Name:           carla
#NOTE: to update this package please change these two version fields in "_service" <param name="revision">v2.1.1</param>
# to the version that you want and execute "osc service runall"
# It will even fill in the .changes file. Please don't touch the Version: in the spec file, it will be filled automaticaly.
Version:        2.5.2
Release:        0
Summary:        An audio plugin host
License:        BSD-2-Clause AND GPL-2.0-or-later AND BSD-3-Clause
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://kx.studio/Applications:Carla
Source0:        %{name}-%{version}.tar.xz
Source1:        carla-warning
Source2:        bsd-2-clause.txt
# PATCH-FIX-OPENSUSE -- Use system flac/vorbis/ogg
Patch0:         0001-Use-system-flac-vorbis-ogg.patch
# PATCH-FIX-OPENSUSE -- Remove rpath from .pc files davejplater@gmail.com
Patch1:         0002-Remove-rpath-from-.pc-files.patch
# PATCH-FIX-OPENSUSE -- Use the correct plugin paths for openSUSE sflees@suse.de
Patch2:         0003-Use-correct-plugin-paths-for-openSUSE.patch
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-qtbase-devel
# for extra native plugins
BuildRequires:  non-ntk-fluid
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-rdflib
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(freetype2)
# for extra samplers support
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(gl)
# for plugin GUIs
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
%if %{with liblo}
BuildRequires:  pkgconfig(liblo)
%endif
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(mxml)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(zlib)
#Wine
#!BuildIgnore:  sane-backends-32bit
BuildRequires:  freetype2-devel-32bit
BuildRequires:  gcc-32bit
BuildRequires:  gcc-c++-32bit
BuildRequires:  glibc-devel-32bit
BuildRequires:  libX11-devel-32bit
BuildRequires:  libXcursor-devel-32bit
BuildRequires:  libXext-devel-32bit
BuildRequires:  libstdc++-devel-32bit
%if 0%{?suse_version} >= 1550
BuildRequires:  mingw32-cross-gcc
BuildRequires:  mingw32-cross-gcc-c++
BuildRequires:  mingw64-cross-gcc
BuildRequires:  mingw64-cross-gcc-c++
BuildRequires:  wine
BuildRequires:  wine-devel
BuildRequires:  wine-devel-32bit
Suggests:       %{name}-vst = %{version}
%endif
#End wine
Requires:       python3-base
Requires:       python3-qt5
Requires:       python3-rdflib
%if %{with liblo}
Requires:       python3-pyliblo
%endif
ExclusiveArch:  x86_64

%description
Carla is an audio plugin host, with support for many audio drivers
and plugin formats. It features automation of parameters via MIDI CC
and full OSC control. It currently supports LADSPA, DSSI, LV2, VST2/3
and AU plugin formats, plus GIG, SF2 and SFZ sounds banks.
It futher supports bridging Window plugins using Wine.

%package devel
Summary:        Header files to access Carla's API
Group:          Development/Libraries/C and C++
Requires:       carla = %{version}
Requires:       pkgconfig

%description devel
This package contains header files needed when writing software using
Carla's several APIs.

%package vst
Summary:        CarlaRack and CarlaPatchbay VST plugins
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name} = %{version}

%description vst
This package contanis Carla VST plugins, including CarlaPatchbayFX,
CarlaPatchbay, CarlaRackFX, and CarlaRack. It also contains the
win32 and wine32 binaries for handling ms win32 vst plugins

%prep
%autosetup -p1
#for i in `grep -rl "/usr/bin/env python3"`;do $(sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i}; chmod +x ${i}) ;done

%build
#remove -m64 from the build
%define optflags -O2 -Wall -D_FORTIFY_SOURCE=2 -funwind-tables -fasynchronous-unwind-tables -Werror=return-type -flto=auto
export CXXFLAGS="%{optflags}"
export CFLAGS="%{optflags}"

# list build configuration, no need for optflags or -j
make features

make %{_smp_mflags} \
%ifnarch %{ix86} x86_64
	BASE_OPTS= \
%endif
	--trace
#Makes 32bit plugin capabilities
make posix32
#missing /usr/lib64/gcc/i686-w64-mingw32/9.2.0/libssp.a
%if 0%{?suse_version} >= 1550
export CFLAGS=`echo $CFLAGS | sed s/\-flto=auto//`
export CXXFLAGS=`echo $CXXFLAGS | sed s/\-flto=auto//`
echo $CFLAGS
echo $CXXFLAGS
make --trace win32 CC=i686-w64-mingw32-gcc CXX=i686-w64-mingw32-g++ LIBDIR=%{_libdir} CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="-Wl,--no-insert-timestamp"
make --trace win64 CC=x86_64-w64-mingw32-gcc CXX=x86_64-w64-mingw32-g++ LIBDIR=%{_libdir} CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="-Wl,--no-insert-timestamp"
make --trace wine32 LIBDIR=%{_libdir} CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="-L/usr/lib/wine"
make --trace wine64 LIBDIR=%{_libdir} CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="-L%{_libdir}/wine"
%endif

%install
make install DESTDIR=%{buildroot} PREFIX="%{_prefix}" LIBDIR="%{_libdir}"

pushd %{buildroot}
for i in `grep -rl "/usr/bin/env python"`;do $(sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i}; chmod +x ${i}) ;done
for i in `grep -rl "/usr/bin/env python3"`;do $(sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i}; chmod +x ${i}) ;done
for i in `grep -rl "/usr/bin/python3"`;do chmod +x ${i} ;done
popd

cp -v source/modules/lilv/serd-0.24.0/tests/TurtleTests/LICENSE LICENSE.TurtleTests

# Cadence uses carla_util.py which also uses carla_backend.py so they need to be in pythonsitelib
mkdir -p %{buildroot}/%{python3_sitelib}
pushd %{buildroot}/%{python3_sitelib}
ln -rs %{buildroot}%{_datadir}/carla/carla_backend.py .
ln -rs %{buildroot}%{_datadir}/carla/carla_utils.py .
popd

# SUSE specific
%if 0%{?suse_version}
 %suse_update_desktop_file -r carla AudioVideo Music
 %if %{with liblo}
 %suse_update_desktop_file -r carla-control AudioVideo Music
 %endif
 %fdupes -s %{buildroot}%{_datadir}
 %fdupes -s %{buildroot}%{_includedir}
%endif
mkdir -p %{buildroot}%{_localstatedir}/adm/update-messages/
#%%{name}-warning
cp %{S:1}  %{buildroot}%{_localstatedir}/adm/update-messages/
cp %{S:2} .

%files
%license doc/GPL.txt doc/LGPL.txt LICENSE.TurtleTests bsd-2-clause.txt
%doc README.md doc/Carla-TestCases
%{_bindir}/*
%{_libdir}/carla
%exclude %{_libdir}/carla/carla-bridge-posix32
%exclude %{_libdir}/carla/carla-discovery-posix32
%if 0%{?suse_version} >= 1550
%exclude %{_libdir}/carla/carla-bridge-win32.exe
%exclude %{_libdir}/carla/carla-bridge-win64.exe
%exclude %{_libdir}/carla/carla-discovery-win32.exe
%exclude %{_libdir}/carla/carla-discovery-win64.exe
%exclude %{_libdir}/carla/jackbridge-wine32.dll
%exclude %{_libdir}/carla/jackbridge-wine64.dll
%endif
%dir %{_libdir}/lv2
%{_libdir}/lv2/carla.lv2
%{_datadir}/carla
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/carla.xml
%{_datadir}/appdata/studio.kx.carla.appdata.xml
%{python3_sitelib}/carla*.py
%{_localstatedir}/adm/update-messages/%{name}-warning

%post
cat %{_localstatedir}/adm/update-messages/%{name}-warning

%files vst
%dir %{_libdir}/vst
%{_libdir}/vst/carla.vst
%{_libdir}/carla/carla-bridge-posix32
%{_libdir}/carla/carla-discovery-posix32
%if 0%{?suse_version} >= 1550
%{_libdir}/carla/carla-bridge-win32.exe
%{_libdir}/carla/carla-bridge-win64.exe
%{_libdir}/carla/carla-discovery-win32.exe
%{_libdir}/carla/carla-discovery-win64.exe
%{_libdir}/carla/jackbridge-wine32.dll
%{_libdir}/carla/jackbridge-wine64.dll
%endif

%files devel
%{_includedir}/carla
%{_libdir}/pkgconfig/*

%changelog
