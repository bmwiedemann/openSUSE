#
# spec file for package carla
#
# Copyright (c) 2026 SUSE LLC and contributors
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


#carla doesn't produce debug rpms unless a debugbuild is defined as 1
%define debugbuild 0
%define __provides_exclude_from ^%{_libdir}/carla/jack/.*.so.0$
%if 0%{?suse_version} >= 1550
%bcond_with liblo
%bcond_with vst
%else
%if 0%{?sle_version} >= 150500
%bcond_with liblo
%bcond_with vst
%else
%bcond_with vst
%bcond_with liblo
%endif
%endif
Name:           carla
#NOTE: to update this package please change these two version fields in "_service" <param name="revision">v2.1.1</param>
# to the version that you want and execute "osc service runall"
# It will even fill in the .changes file. Please don't touch the Version: in the spec file, it will be filled automaticaly.
Version:        2.5.10
Release:        0
Summary:        An audio plugin host
License:        BSD-2-Clause AND GPL-2.0-or-later AND BSD-3-Clause
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
BuildRequires:  freetype2-devel-32bit
BuildRequires:  gcc-32bit
BuildRequires:  gcc-c++-32bit
BuildRequires:  glibc-devel-32bit
BuildRequires:  hicolor-icon-theme
BuildRequires:  libX11-devel-32bit
BuildRequires:  libXcursor-devel-32bit
BuildRequires:  libXext-devel-32bit
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libstdc++-devel-32bit
# for extra native plugins
BuildRequires:  non-ntk-fluid
BuildRequires:  pkgconfig
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-rdflib
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(flac)
# for extra samplers support
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
# for plugin GUIs
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(mxml)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(python3-embed)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(zlib)
#Wine
#!BuildIgnore:  sane-backends-32bit
#End wine
Requires:       python3-base
Requires:       python3-qt5
Requires:       python3-rdflib
ExclusiveArch:  x86_64
%if %{with liblo}
BuildRequires:  pkgconfig(liblo)
%endif
%if %{with vst}
BuildRequires:  mingw32-cross-gcc
BuildRequires:  mingw32-cross-gcc-c++
BuildRequires:  mingw64-cross-gcc
BuildRequires:  mingw64-cross-gcc-c++
BuildRequires:  wine
BuildRequires:  wine-devel
BuildRequires:  wine-devel-32bit
Suggests:       %{name}-vst = %{version}
%endif
%if %{with liblo}
Requires:       python3-pyliblo
%endif

%description
Carla is an audio plugin host, with support for many audio drivers
and plugin formats. It features automation of parameters via MIDI CC
and full OSC control. It currently supports LADSPA, DSSI, LV2, VST2/3
and AU plugin formats, plus GIG, SF2 and SFZ sounds banks.
It futher supports bridging Window plugins using Wine.

%package devel
Summary:        Header files to access Carla's API
Requires:       carla = %{version}
Requires:       pkgconfig

%description devel
This package contains header files needed when writing software using
Carla's several APIs.

%package vst
Summary:        CarlaRack and CarlaPatchbay VST plugins
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
%if 0%{?debugbuild} == 1
export DEBUG=true
%endif
# list build configuration, no need for optflags or -j
%make_build features

%make_build \
%ifnarch %{ix86} x86_64
	BASE_OPTS= \
%endif
	--trace
#Makes 32bit plugin capabilities
%make_build posix32
#missing /usr/lib64/gcc/i686-w64-mingw32/9.2.0/libssp.a
%if %{with vst}
export CFLAGS=`echo $CFLAGS | sed s/\-flto=auto//`
export CXXFLAGS=`echo $CXXFLAGS | sed s/\-flto=auto//`
echo $CFLAGS
echo $CXXFLAGS
%make_build --trace win32 CC=i686-w64-mingw32-gcc CXX=i686-w64-mingw32-g++ LIBDIR=%{_libdir} CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="-Wl,--no-insert-timestamp"
%make_build --trace win64 CC=x86_64-w64-mingw32-gcc CXX=x86_64-w64-mingw32-g++ LIBDIR=%{_libdir} CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="-Wl,--no-insert-timestamp"
%make_build --trace wine32 LIBDIR=%{_libdir} CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="-L/usr/lib/wine"
%make_build --trace wine64 LIBDIR=%{_libdir} CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="-L%{_libdir}/wine"
%endif

%install
make install DESTDIR=%{buildroot} PREFIX="%{_prefix}" LIBDIR="%{_libdir}"

pushd %{buildroot}
for i in `grep -rl "%{_bindir}/env python"`;do $(sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i}; chmod +x ${i}) ;done
for i in `grep -rl "%{_bindir}/env python3"`;do $(sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i}; chmod +x ${i}) ;done
for i in `grep -rl "%{_bindir}/python3"`;do chmod +x ${i} ;done
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
cp %{SOURCE1}  %{buildroot}%{_localstatedir}/adm/update-messages/
cp %{SOURCE2} .

%files
%license doc/GPL.txt doc/LGPL.txt LICENSE.TurtleTests bsd-2-clause.txt
%doc README.md doc/Carla-TestCases
%{_bindir}/*
%{_libdir}/carla
%exclude %{_libdir}/carla/carla-bridge-posix32
%exclude %{_libdir}/carla/carla-discovery-posix32
%if %{with vst}
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
%if %{with vst}
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
