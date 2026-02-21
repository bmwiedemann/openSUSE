#
# spec file for package obs-studio
#
# Copyright (c) 2026 SUSE LLC
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

Name:           obs-studio
Version:        32.0.4
Release:        0
Summary:        Free and open source software for video recording and live streaming
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://obsproject.com/
Source:         obs-studio-%{version}.tar.xz
Patch0:         disable-x264.patch
Patch1:         optional-browser-websocket.patch
BuildRequires:  AMF-devel
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.28
BuildRequires:  cmake(LibDataChannel) >= 0.21.0
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  ffmpeg-7-mini-devel >= 6.1
BuildRequires:  hicolor-icon-theme
BuildRequires:  mbedtls-devel >= 3.4.0
BuildRequires:  pciutils-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(asio)
BuildRequires:  pkgconfig(ffnvcodec) >= 12.2.0.0
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(jansson) >= 2.14
BuildRequires:  pkgconfig(libcurl) >= 6.1
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.65
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(librist)
BuildRequires:  pkgconfig(luajit) >= 2.1.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(rnnoise)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(srt) >= 1.5.3
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vlc-plugin)
BuildRequires:  pkgconfig(vpl)
BuildRequires:  pkgconfig(websocketpp) >= 0.8
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  python3-devel
BuildRequires:  qrcodegen-devel >= 1.8.0
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-base-private-devel
BuildRequires:  qt6-gui-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-wayland-devel
BuildRequires:  simde-devel
BuildRequires:  sndio-devel
BuildRequires:  swig >= 4.0.2
BuildRequires:  update-desktop-files
BuildRequires:  uthash-devel >= 2.3.0
BuildRequires:  wayland-devel
Recommends:     obs-vkcapture
Recommends:     obs-pipewire-audio-capture
Recommends:     obs-aitum-multistream

%description
OBS Studio is software designed for capturing, compositing, encoding, recording, and streaming video content, efficiently.

%package devel
Summary:        A recording/broadcasting program - Development Files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Devel files for OBS Studio is software designed for capturing, compositing, encoding, recording, and streaming video content, efficiently.

%prep
%autosetup -p1

%build
# NOTE:
# x264 support is disabled due to licensing incompatibilities with distribution
# policies. Even when libx264 is present on the build system, detection is
# forcibly disabled to avoid accidental linkage.
#
# OpenH264 is used as the supported H.264 encoder backend instead.
#
# The obs-browser and obs-websocket plugins are disabled in-tree and are expected
# to be provided as external plugins, allowing independent updates and clearer
# licensing separation.
cmake -B build/ \
  -DENABLE_X264=OFF \
  -DENABLE_BROWSER=OFF \
  -DENABLE_PLUGINS=ON \
  -DUNIX_STRUCTURE=1 \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DENABLE_NATIVE_NVENC=ON \
  -DENABLE_JACK=ON \
  -DENABLE_SNDIO=ON \
  -DENABLE_AJA=OFF \
  -DOBS_COMPILE_DEPRECATION_AS_WARNING=ON \
  -DOBS_VERSION_OVERRIDE=%{version}
make -C build/

%install
%cmake_install
find %{buildroot} \( -name '.keepme' -o -name '.gitkeep' \) -delete

%fdupes %{buildroot}%{_datadir}/obs
%fdupes %{buildroot}%{_libdir}/cmake

%check
#nothing to do

%post
/sbin/ldconfig
%icon_theme_cache_post

%postun
/sbin/ldconfig
%icon_theme_cache_postun

%files
%license COPYING COMMITMENT
%doc README.rst CONTRIBUTING.rst
%{_bindir}/obs
%ifarch x86_64
%{_bindir}/obs-nvenc-test
%endif
%{_bindir}/obs-ffmpeg-mux
%{_libdir}/obs-plugins
%dir %{_libdir}/obs-scripting
%{_libdir}/obs-scripting/obslua.so
%{_libdir}/obs-scripting/obspython.py
%{_libdir}/obs-scripting/_obspython.so
%{_libdir}/libobs-scripting.so.*
%{_libdir}/libobs.so.*
%{_libdir}/libobs-frontend-api.so.*
%{_libdir}/libobs-opengl.so.*
%{_datadir}/applications/com.obsproject.Studio.desktop
%{_datadir}/icons/hicolor/*/apps/com.obsproject.Studio.png
%{_datadir}/icons/hicolor/scalable/apps/com.obsproject.Studio.svg
%{_datadir}/metainfo/com.obsproject.Studio.metainfo.xml
%{_datadir}/obs

%files devel
%{_libdir}/cmake
%{_libdir}/libobs.so
%{_libdir}/libobs-frontend-api.so
%{_libdir}/libobs-opengl.so
%{_libdir}/libobs-scripting.so
%{_libdir}/pkgconfig/libobs.pc
%{_libdir}/pkgconfig/obs-frontend-api.pc
%{_includedir}/obs

%changelog
