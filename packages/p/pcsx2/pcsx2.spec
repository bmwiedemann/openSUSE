#
# spec file for package pcsx2
#
# Copyright (c) 2020 SUSE LLC
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


Name:           pcsx2
Version:        1.6.0
Release:        0
Summary:        Sony PlayStation 2 Emulator
License:        LGPL-3.0-only
Group:          System/Emulators/Other
URL:            http://pcsx2.net/
Source:         %{name}-%{version}.tar.gz

ExclusiveArch:  i586

#Build Dependencies:
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++

#Misc
BuildRequires:  libaio-devel
BuildRequires:  libpcap-devel-static
BuildRequires:  pkgconfig(liblzma)
# Disabled for Leap builds
#BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxml-2.0) 
BuildRequires:  pkgconfig(zlib)

#Graphics
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libpng16)

#Display
BuildRequires:  wxWidgets-3_0-devel
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(x11)

#Audio
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(soundtouch)

%description
Sony PlayStation 2 emulator. Requires a BIOS image in %{_libdir}/%{name}/bios
or in .%{name}/bios in your HOME directory (will be created when you first run
PCSX2). Check http://www.pcsx2.net/guide.php#Bios for details on which files
you need and how to obtain them.

%prep
%setup -q

#Avoid fatal cmake error when it cannot find sdl2 for onepad
sed -i 's|print_dep("Skip build of onepad: miss some dependencies" "${msg_dep_onepad}")||g' cmake/SelectPcsx2Plugins.cmake

%build
%cmake .. \
  -DCMAKE_BUILD_TYPE='Release' \
  -DUSER_CMAKE_C_FLAGS="-Wno-narrowing" \
  -DUSER_CMAKE_CXX_FLAGS="-Wno-narrowing" \
  -DPLUGIN_DIR='%{_libdir}/%{name}' \
  -DGAMEINDEX_DIR='%{_datadir}/%{name}' \
  -DDOC_DIR='%{_datadir}/doc/%{name}' \
  -DBIN_DIR='%{_bindir}' \
  -DXDG_STD='TRUE' \
  -DDISABLE_PCSX2_WRAPPER='TRUE' \
  -DPACKAGE_MODE='TRUE' \
  -DDISABLE_ADVANCE_SIMD='TRUE' \
  -DDISABLE_BUILD_DATE='TRUE' \
  -DGSDX_LEGACY='TRUE' \
  -DSDL2_API='TRUE'

%make_jobs

%install
%cmake_install

# move translations to main language dir if there isn't a sublang or delete
# translations not supported by distro at all
for i in $(ls %{buildroot}%{_datadir}/locale | grep _); do
  new=$(echo $i | sed "s:_.*::g")
  if [ ! -d %{_datadir}/locale/$i ]; then
    if [ -d %{_datadir}/locale/$new ]; then
      mv %{buildroot}%{_datadir}/locale/$i %{buildroot}%{_datadir}/locale/$new
    else
      rm -rf %{buildroot}%{_datadir}/locale/$i
    fi
  fi
done

%fdupes -s %{buildroot}
%find_lang %{name}_Main
%find_lang %{name}_Iconized

%check
%ctest

%files -f %{name}_Main.lang -f %{name}_Iconized.lang
%doc README.md
%license COPYING.LGPLv2.1 COPYING.LGPLv3 COPYING.GPLv2 COPYING.GPLv3
%{_bindir}/PCSX2
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/doc/%{name}
%{_datadir}/applications/PCSX2.desktop
%{_datadir}/pixmaps/PCSX2.xpm
%{_mandir}/man1/PCSX2.1%{?ext_man}

%changelog
