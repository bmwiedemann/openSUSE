#
# spec file for package sdrangel
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2026, Martin Hauke <mardnh@gmx.de>
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

# Don't build with LTO since it breaks sdrangel
%define _lto_cflags %{nil}
%ifarch %{ix86} %{arm}
%bcond_with    fec
%else
%bcond_without fec
%endif
%bcond_without freedv
%bcond_with qt6
Name:           sdrangel
Version:        8.0.0
Release:        0
Summary:        SDR/Analyzer frontend for Airspy, BladeRF, HackRF, RTL-SDR and FunCube
License:        GPL-3.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://github.com/f4exb/sdrangel
Source:         https://github.com/f4exb/sdrangel/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  dsdcc-devel >= 1.9.3
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
%if 0%{with qt6}
#BuildRequires:  libQt6Gui-private-headers-devel
#BuildRequires:  qt6-core-private-devel
%else
BuildRequires:  libQt5Gui-private-headers-devel
%endif
BuildRequires:  libboost_headers-devel
BuildRequires:  limesuite-devel
BuildRequires:  pkgconfig
BuildRequires:  serialdv-devel
%if 0%{with qt6}
BuildRequires:  pkgconfig(Qt6Charts)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6QuickWidgets)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6MultimediaWidgets)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6Positioning)
BuildRequires:  pkgconfig(Qt6SerialPort)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6StateMachine)
BuildRequires:  pkgconfig(Qt6WebSockets)
BuildRequires:  pkgconfig(Qt6Widgets)
%else
BuildRequires:  pkgconfig(Qt5Charts)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gamepad)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Positioning)
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5TextToSpeech)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5WebSockets)
BuildRequires:  pkgconfig(Qt5Widgets)
%endif
BuildRequires:  pkgconfig(SoapySDR)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(faad2)
BuildRequires:  pkgconfig(codec2)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(libairspy)
BuildRequires:  pkgconfig(libairspyhf)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libbladeRF)
BuildRequires:  pkgconfig(libhackrf)
BuildRequires:  pkgconfig(libiio)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(librtlsdr)
BuildRequires:  pkgconfig(libswscale)
# It does not build with libmirisdr from upstream
# https://github.com/f4exb/libmirisdr-4 is needed
#BuildRequires:  pkgconfig(libmirisdr)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxtrx)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(uhd)
Requires:       python3-requests
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(opencv4)
%else
BuildRequires:  pkgconfig(opencv)
%endif
%if 0%{with fec}
BuildRequires:  pkgconfig(libcm256cc)
BuildRequires:  pkgconfig(nanomsg)
%endif
%if 0%{with freedv}
BuildRequires:  pkgconfig(codec2)
%endif

%description
SDRangel is an Open Source Qt5/OpenGL SDR and signal analyzer frontend
to various hardware.

%prep
%setup -q
sed -i 's/\r$//' Readme.md
sed -i 's|#!%{_bindir}/env python|#!%{_bindir}/python3|g' swagger/sdrangel/examples/*.py

%build
export CXXFLAGS="%{optflags} -Wno-return-type -fpermissive"
%cmake \
%if 0%{with qt6}
  -DENABLE_QT6=ON \
%endif
  -DCMAKE_SHARED_LINKER_FLAGS="" \
  -DCMAKE_SKIP_RPATH:BOOL=OFF \
  -DCMAKE_BUILD_TYPE=Release \
  -DENABLE_DISTRIBUTION=ON \
%ifarch i586 x86_64
  -DFORCE_SSE41=ON \
%endif
  -DRX_SAMPLE_24BIT=ON
%make_jobs

%install
%cmake_install
rm %{buildroot}%{_datadir}/sdrangel/Readme.md
rm %{buildroot}%{_bindir}/tools.json

%files
%license LICENSE
%doc Readme.md
%doc swagger/sdrangel/examples/
%{_bindir}/sdrangel
%{_bindir}/sdrangel-%{version}-linux.mcpb
%{_bindir}/sdrangelbench
%{_bindir}/sdrangelsrv
%{_bindir}/sdrangel-mcp-bridge

%dir %{_libdir}//sdrangel
%{_libdir}/sdrangel/lib*
%{_libdir}/sdrangel/plugins
%{_libdir}/sdrangel/pluginssrv
%{_datadir}/applications/sdrangel.desktop
%{_datadir}/icons/hicolor/scalable/apps/sdrangel_icon.svg
%{_datadir}/metainfo/org.sdrangel.SDRangel.metainfo.xml

%changelog
