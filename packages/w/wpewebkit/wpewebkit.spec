#
# spec file for package wpewebkit
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


%define _apiver       2.0
%define _wksover      2_0-1
%define _sonameverpkg 2_0

Name:           wpewebkit
### FIXME ### Drop the disabling of LTO on next release/versionbump
%define _lto_cflags %{nil}
Version:        2.44.2
Release:        0
Summary:        Library for rendering web content, WPE Port
License:        BSD-3-Clause AND LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://wpewebkit.org/
Source:         %{url}/releases/%{name}-%{version}.tar.xz

BuildRequires:  bubblewrap
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gperf >= 3.0.1
BuildRequires:  libbacktrace-devel
BuildRequires:  libicu-devel >= 61.2
BuildRequires:  memory-constraints
BuildRequires:  ninja
BuildRequires:  perl >= 5.10.0
BuildRequires:  python3
BuildRequires:  ruby >= 2.5
BuildRequires:  unifdef
BuildRequires:  xdg-dbus-proxy
BuildRequires:  pkgconfig(atk) >= 2.16.0
BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(cairo) >= 1.16.0
BuildRequires:  pkgconfig(epoxy) >= 1.5.4
BuildRequires:  pkgconfig(freetype2) >= 2.9.0
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glib-2.0) >= 2.70.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.18.4
BuildRequires:  pkgconfig(gstreamer-allocators-1.0) >= 1.18.4
BuildRequires:  pkgconfig(gstreamer-app-1.0) >= 1.18.4
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 1.18.4
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.18.4
BuildRequires:  pkgconfig(gstreamer-codecparsers-1.0) >= 1.18.4
BuildRequires:  pkgconfig(gstreamer-fft-1.0) >= 1.18.4
BuildRequires:  pkgconfig(gstreamer-gl-1.0) >= 1.18.4
BuildRequires:  pkgconfig(gstreamer-mpegts-1.0) >= 1.4.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.18.4
BuildRequires:  pkgconfig(gstreamer-rtp-1.0) >= 1.18.4
BuildRequires:  pkgconfig(gstreamer-sdp-1.0) >= 1.18.4
BuildRequires:  pkgconfig(gstreamer-tag-1.0) >= 1.18.4
BuildRequires:  pkgconfig(gstreamer-transcoder-1.0) >= 1.18.4
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.18.4
BuildRequires:  pkgconfig(gstreamer-webrtc-1.0) >= 1.18.4
BuildRequires:  pkgconfig(harfbuzz) >= 1.4.2
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libavif) >= 0.9.0
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libgcrypt) >= 1.7.0
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl) >= 0.7.0
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsoup-3.0) >= 3.0.0
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwoff2common) >= 1.0.2
BuildRequires:  pkgconfig(libwoff2dec)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.8.0
BuildRequires:  pkgconfig(libxslt) >= 1.1.7
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(wayland-client) >= 1.15
BuildRequires:  pkgconfig(wayland-egl) >= 1.15
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server) >= 1.15
BuildRequires:  pkgconfig(wpe-1.0)
BuildRequires:  pkgconfig(wpebackend-fdo-1.0) >= 1.3.0
BuildRequires:  pkgconfig(xkbcommon) >= 0.4.0
BuildRequires:  pkgconfig(zlib)

%description
WPE allows embedders to create simple and performant systems based on
Web platform technologies. It is designed with hardware acceleration
in mind, leveraging common 3D graphics APIs for best performance.

%package -n libWPEWebKit-%{_wksover}
Summary:        Library for rendering web content, WPE port
Group:          System/Libraries
Requires:       %{name}-%{_sonameverpkg}-injected-bundles
Requires:       bubblewrap
Requires:       xdg-dbus-proxy
Provides:       libWPEWebKit-{_apiver}

%description -n libWPEWebKit-%{_wksover}
WPE allows embedders to create simple and performant systems based on
Web platform technologies. It is designed with hardware acceleration
in mind, leveraging common 3D graphics APIs for best performance.

%package -n wpewebkit-%{_sonameverpkg}-injected-bundles
Summary:        Injected bundles for wpewebkit
Group:          System/Libraries

%description -n wpewebkit-%{_sonameverpkg}-injected-bundles
WPE allows embedders to create simple and performant systems based on
Web platform technologies. It is designed with hardware acceleration
in mind, leveraging common 3D graphics APIs for best performance.

%package -n libWPEWebInspectorResources
Summary:        WPEWebInspectorResources tool
Group:          System/Libraries

%description -n libWPEWebInspectorResources
WPE allows embedders to create simple and performant systems based on
Web platform technologies. It is designed with hardware acceleration
in mind, leveraging common 3D graphics APIs for best performance.

%package -n WPEWebDriver
Summary:        WebDriver service implementation for WPE  WebKit
Group:          System/Libraries

%description -n WPEWebDriver
WPE allows embedders to create simple and performant systems based on
Web platform technologies. It is designed with hardware acceleration
in mind, leveraging common 3D graphics APIs for best performance.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libWPEWebKit-%{_wksover} = %{version}

%description    devel
WPE allows embedders to create simple and performant systems based on
Web platform technologies. It is designed with hardware acceleration
in mind, leveraging common 3D graphics APIs for best performance.

%package        minibrowser
Summary:        MiniBrowser from WebKit
Group:          Development/Tools/Other
Requires:       libWPEWebKit-%{_wksover} = %{version}

%description    minibrowser
A small test browswer from webkit, useful for testing features and
embedded mini browsers.

%prep
%autosetup -p1

%build
# Not eat all memory
%define _dwz_low_mem_die_limit 40000000
%define _dwz_max_die_limit 250000000
%limit_build -m 2500

# Use linker flags to reduce memory consumption
%global optflags %(echo %{optflags} -Wl,--no-keep-memory -Wl,--reduce-memory-overheads | sed 's/-g /-g1 /')
export CFLAGS="%{optflags} $(pkg-config --cflags wayland-client xkbcommon)"
export CXXFLAGS="%{optflags} $(pkg-config --cflags wayland-client xkbcommon)"
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DENABLE_DOCUMENTATION=OFF \
  -DENABLE_INTROSPECTION=OFF \
  -DPORT=WPE \
  -DENABLE_MINIBROWSER=ON \
  -DUSE_AVIF=ON \
  -DLIBEXEC_INSTALL_DIR=%{_libexecdir}/libWPEWebKit-%{_wksover} \
%ifarch aarch64
  -DENABLE_JIT=OFF \
  -DUSE_SYSTEM_MALLOC=ON \
%endif
%ninja_build

%install
%ninja_install -C build

%ldconfig_scriptlets -n libWPEWebKit-%{_wksover}

%files -n libWPEWebKit-%{_wksover}
%dir %{_libdir}/wpe-webkit-%{_apiver}
%exclude %{_libexecdir}/libWPEWebKit-%{_wksover}/MiniBrowser
%{_libexecdir}/libWPEWebKit-%{_wksover}
%{_libdir}/libWPEWebKit-%{_apiver}.so.*
%doc NEWS

%files -n wpewebkit-%{_sonameverpkg}-injected-bundles
%dir %{_libdir}/wpe-webkit-%{_apiver}/injected-bundle
%{_libdir}/wpe-webkit-%{_apiver}/injected-bundle/libWPEInjectedBundle.so

%files -n libWPEWebInspectorResources
%{_libdir}/wpe-webkit-%{_apiver}/libWPEWebInspectorResources.so

%files -n WPEWebDriver
%{_bindir}/WPEWebDriver

%files devel
%{_includedir}/wpe-webkit-%{_apiver}
%{_libdir}/libWPEWebKit-%{_apiver}.so
%{_libdir}/pkgconfig/wpe-webkit-%{_apiver}.pc
%{_libdir}/pkgconfig/wpe-web-process-extension-%{_apiver}.pc

%files minibrowser
%{_libexecdir}/libWPEWebKit-%{_wksover}/MiniBrowser

%changelog
