#
# spec file for package pcsx2
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


Name:           pcsx2
Version:        2.7.121~git20260215
Release:        0
Summary:        Sony PlayStation 2 Emulator
License:        GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only
URL:            http://pcsx2.net/
Source0:        %{name}-%{version}.tar.xz
Source1:        https://github.com/PCSX2/pcsx2_patches/releases/download/latest/patches.zip
ExclusiveArch:  x86_64
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fast_float-devel
BuildRequires:  fdupes
BuildRequires:  gtest
BuildRequires:  kddockwidgets-qt6-devel
BuildRequires:  libaio-devel
BuildRequires:  libbacktrace-devel
BuildRequires:  libpcap-devel-static
BuildRequires:  libzip-tools
BuildRequires:  libzstd-devel-static
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  sndio-devel
BuildRequires:  unzip
BuildRequires:  cmake(glslang)
BuildRequires:  cmake(ryml)
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6WaylandClient)
BuildRequires:  pkgconfig(Qt6WaylandCompositor)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(plutosvg)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sdl3)
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)

%description
Sony PlayStation 2 emulator. Requires a BIOS image in %{_libdir}/%{name}/bios
or in .%{name}/bios in your HOME directory (will be created when you first run
PCSX2). Check http://www.pcsx2.net/guide.php#Bios for details on which files
you need and how to obtain them.

%prep
%autosetup -p1 -a 1
sed -i 's/"Unknown"/"%{version}"/g' cmake/Pcsx2Utils.cmake

%build
# -DDISABLE_ADVANCE_SIMD=ON: the name of this option is misleading. it actually
# build multiple binary for different instruction sets. it is more compatible
# to both old and new CPU.
mkdir build
cd build
cmake ..\
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_C_COMPILER=clang \
  -DCMAKE_CXX_COMPILER=clang++ \
  -DX11_API=ON \
  -DWAYLAND_API=ON \
  -DENABLE_SETCAP=OFF \
  -DDISABLE_ADVANCE_SIMD=ON

%cmake_build

%install
# pcsx2 doesn't support make install anymore, we have to do it manually
mkdir -p %{buildroot}%{_libdir}/%{name}
cp -r build/bin/* %{buildroot}%{_libdir}/%{name}

cp %{SOURCE1} %{buildroot}%{_libdir}/%{name}/resources

mkdir -p %{buildroot}%{_bindir}
ln -s %{_libdir}/%{name}/%{name}-qt %{buildroot}%{_bindir}/%{name}-qt

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/512x512/apps
cp bin/resources/icons/AppIconLarge.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/PCSX2.png

mkdir -p %{buildroot}%{_datadir}/applications
cp .github/workflows/scripts/linux/pcsx2-qt.desktop %{buildroot}%{_datadir}/applications/net.pcsx2.PCSX2.desktop

# a simple trick to fill git version and git date...
sed -i -e "s/@GIT_VERSION@\" date=\"@GIT_DATE@/%{version}/" .github/workflows/scripts/linux/pcsx2-qt.metainfo.xml.in
sed -i -e "s/~git/\" date=\"/" .github/workflows/scripts/linux/pcsx2-qt.metainfo.xml.in
mkdir -p %{buildroot}%{_datadir}/metainfo
cp .github/workflows/scripts/linux/pcsx2-qt.metainfo.xml.in %{buildroot}%{_datadir}/metainfo/net.pcsx2.PCSX2.appdata.xml

%fdupes -s %{buildroot}

%check

%ctest

%files
%doc README.md
%license COPYING.GPLv3
%{_bindir}/%{name}-qt
%{_libdir}/%{name}
%{_datadir}/applications/net.pcsx2.PCSX2.desktop
%{_datadir}/icons/hicolor/512x512/apps/PCSX2.png
%{_datadir}/metainfo/net.pcsx2.PCSX2.appdata.xml

%changelog
