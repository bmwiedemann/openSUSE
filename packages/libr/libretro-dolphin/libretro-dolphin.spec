#
# spec file for package libretro-dolphin
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


Name:           libretro-dolphin
Version:        0~git20200831
Release:        0
Summary:        Dolphin libretro core for Nintendo GameCube and Wii emulation
License:        GPL-3.0-only
Group:          System/Emulators/Other
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  Mesa-devel
BuildRequires:  cmake
%if 0%{?suse_version} > 1520
BuildRequires:  gcc9-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  mbedtls-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(hidapi-hidraw)
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(miniupnpc)
BuildRequires:  pkgconfig(openthreads)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(sfml-network)
BuildRequires:  pkgconfig(sfml-system)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(zlib)
ExcludeArch:    %arm ppc64 ppc64le

%description
Dolphin is an emulator for running GameCube and Wii games on Windows, Linux,
macOS, and recent Android devices. It's licensed under the terms of the GNU
General Public License, version 2 or later (GPLv2+). This package is for
RetroArch/libretro front-end.

%prep
%setup -q

%build
%if 0%{?suse_version} > 1520
export CC=gcc-9
export CXX=g++-9
%endif
mkdir build
cd build
cmake .. \
    -DLIBRETRO=ON \
    -DLIBRETRO_STATIC=1 \
    -DENABLE_QT=0 \
    -DCMAKE_BUILD_TYPE=Release \
    -DDISTRIBUTOR=openSUSE \
    -DUSE_SHARED_ENET=ON \
    -DUSE_UPNP=ON
make

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp build/dolphin_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/dolphin_libretro.so

%changelog
