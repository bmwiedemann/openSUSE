#
# spec file for package freerdp
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


%if 0%{?suse_version} > 1500 && 0%{?is_opensuse}
%global _with_ffmpeg 1
#global _with_openh264 1
%global _with_soxr 1
%global _with_lame 1
%else
%if 0%{?sle_version} >= 150200 && 0%{?is_opensuse}
%global _with_ffmpeg 1
%endif
%endif

%global _with_gss 1

%define major_version 3
%define libfreerdp_package %{major_version}-%{major_version}
%define rdtk_version 0
%define rdtk_package %{rdtk_version}-%{rdtk_version}
%define uwac_version 0
%define uwac_package %{uwac_version}-%{uwac_version}

Name:           freerdp
Version:        3.10.3
Release:        0
Summary:        Remote Desktop Viewer Client
License:        Apache-2.0
Group:          Productivity/Networking/Other
URL:            https://www.freerdp.com/
Source0:        https://github.com/FreeRDP/FreeRDP/archive/%{version}.tar.gz#/FreeRDP-%{version}.tar.gz
Source1:        freerdp-rpmlintrc
BuildRequires:  chrpath
BuildRequires:  cmake >= 2.8
BuildRequires:  cups-devel
BuildRequires:  ed
BuildRequires:  fdupes
# doesn't compile correctly with older gcc's
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  libgsm-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(icu-i18n)
%{?_with_gss:BuildRequires:  pkgconfig(krb5) >= 1.13}
%{?_with_ffmpeg:
BuildRequires:  pkgconfig(libavcodec) >= 57.48.101
BuildRequires:  pkgconfig(libavutil)
}
BuildRequires:  pkgconfig(libcjson)
BuildRequires:  pkgconfig(libjpeg)
%{?_with_lame:BuildRequires:  pkgconfig(libmp3lame)}
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libpkcs11-helper-1)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(liburiparser)
BuildRequires:  pkgconfig(libusb-1.0)
%{?_with_openh264:BuildRequires:  pkgconfig(openh264)}
BuildRequires:  pkgconfig(openssl)
%{?_with_soxr:BuildRequires:  pkgconfig(soxr)}
BuildRequires:  xmlto
# Upstream use SDL3, but SDL3 does not exist in Leap and SDL3_ttf does not exists in Leap and Tumbleweed.
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(zlib)
# force installation of latest library version
Requires:       lib%{name}%{libfreerdp_package} = %{version}-%{release}

%description
FreeRDP is a client-side implementation of the Remote Desktop Protocol (RDP)
following the Microsoft Open Specifications. This package provides the client
application.

%package sdl
Summary:        Remote Desktop Viewer Client
Group:          Productivity/Networking/Other

%description sdl
FreeRDP is a client-side implementation of the Remote Desktop Protocol (RDP)
following the Microsoft Open Specifications. This package provides the
sdl-based client application.

%package wayland
Summary:        Remote Desktop Viewer Client
Group:          Productivity/Networking/Other

%description wayland
FreeRDP is a client-side implementation of the Remote Desktop Protocol (RDP)
following the Microsoft Open Specifications. This package provides the
wayland-based client application.

%package server
Summary:        Remote Desktop Server
Group:          Productivity/Networking/Other

%description server
This package contains a server-side implementation which can export a desktop
via the Remote Desktop Protocol (RDP) following the Microsoft Open
Specifications.

%package proxy
Summary:        Remote Desktop Security and Monitorig Proxy Server
Group:          Productivity/Networking/Other

%description proxy
This package contains a proxy that allows to select specific features and
channels allowed for all connections passing through.
It allows monitoring of the running sessions.

%package -n %{name}-proxy-plugins
Summary:        Plugins for the Security and Monitorig Proxy Server
Group:          Productivity/Networking/Other
Requires:       %{name}-proxy = %{version}-%{release}

%description -n %{name}-proxy-plugins
This package contains the following plugins for the proxy server:
* bitmap-filter
* capture
* demo
* dyn-channel-dump

%package -n lib%{name}%{libfreerdp_package}
Summary:        Remote Desktop Viewer client library
Group:          System/Libraries

%description -n lib%{name}%{libfreerdp_package}
FreeRDP is a client-side implementation of the Remote Desktop Protocol (RDP)
following the Microsoft Open Specifications. This package provides the shared
libraries used by the client.

%package devel
Summary:        Development Files for freerdp
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{libfreerdp_package} = %{version}-%{release}
Requires:       lib%{name}-server-proxy%{libfreerdp_package}
Requires:       winpr-devel = %{version}-%{release}
Obsoletes:      %{name}-server-proxy%{libfreerdp_package}-devel < %{version}-%{release}
Provides:       %{name}-server-proxy%{libfreerdp_package}-devel = %{version}-%{release}

%description devel
This package contains development files necessary for developing applications
based on libfreerdp.

%package -n     libwinpr%{libfreerdp_package}
Summary:        Windows Portable Runtime
Group:          System/Libraries

%description -n libwinpr%{libfreerdp_package}
WinPR provides API compatibility for applications targeting non-Windows
environments. When on Windows, the original native API is being used instead of
the equivalent WinPR implementation, without having to modify the code using it.

%package -n winpr-devel
Summary:        Windows Portable Runtime development files
Group:          Development/Languages/C and C++
Requires:       cmake >= 2.8
# WinPRTargets-*.cmake defines targets for winpr-hash and winpr-makecert
Requires:       freerdp-server = %{version}-%{release}
Requires:       libwinpr%{libfreerdp_package} = %{version}-%{release}
Obsoletes:      libwinpr2-devel < %{version}-%{release}
Provides:       libwinpr2-devel = %{version}-%{release}

%description -n winpr-devel
This package contains header files for developing applications that
use the winpr and winpr-tools libraries.

%package -n     libuwac%{uwac_package}
Summary:        Use wayland as a client
Group:          System/Libraries

%description -n libuwac%{uwac_package}
Using wayland as a client (uwac) is a library to provide common
functionality for wayland clients.

%package -n uwac%{uwac_version}-devel
Summary:        Remote Desktop Toolkit libuwac development files
Group:          Development/Languages/C and C++
Requires:       cmake >= 2.8
Requires:       libuwac%{uwac_package} = %{version}-%{release}
Obsoletes:      libuwac%{uwac_version}-devel < %{version}-%{release}
Provides:       libuwac%{uwac_version}-devel = %{version}-%{release}
Obsoletes:      uwac%{uwac_version}-%{uwac_version}-devel < %{version}-%{release}
Provides:       uwac%{uwac_version}-%{uwac_version}-devel = %{version}-%{release}

%description -n uwac%{uwac_version}-devel
This package contains header files for developing applications that
use the uwac library.

%package -n librdtk%{rdtk_package}
Summary:        FreeRDP Toolkit
Group:          System/Libraries

%description -n librdtk%{rdtk_package}
This package contains the library for the Remote Desktop Toolkit.

%package -n rdtk%{rdtk_version}-devel
Summary:        FreeRDP Toolkit development files
Group:          Development/Languages/C and C++
Requires:       librdtk%{rdtk_package} = %{version}-%{release}

%description -n rdtk%{rdtk_version}-devel
This package contains the development files for RDTK.

%package -n lib%{name}-server-proxy%{libfreerdp_package}
Summary:        FreeRDP Server Proxy library
Group:          System/Libraries

%description -n lib%{name}-server-proxy%{libfreerdp_package}
This package contains the FreeRDP Server Proxy library files.

%prep
%autosetup -p1 -n FreeRDP-%{version}

%build
if [ -z "$SOURCE_DATE_EPOCH" ]; then
find . -type f -name "*.c" -exec perl -i -pe 's{__(DATE|TIME)__}{""}g' "{}" "+"
fi

%if 0%{?suse_version} < 1600
export CXX=g++-12
%endif

%cmake \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_INSTALL_LIBDIR=%{_lib} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_EXE_LINKER_FLAGS="-pie" \
        -DCMAKE_SKIP_RPATH=TRUE \
        -DCMAKE_SKIP_INSTALL_RPATH=TRUE \
        -DWITH_ALSA=ON \
        -DWITH_CAIRO=ON \
        -DWITH_CUPS=ON \
        -DWITH_CHANNELS=ON -DBUILTIN_CHANNELS=OFF \
        -DWITH_PLUGIN_RPATH_ONLY=ON \
        -DWITH_CLIENT=ON \
        -DWITH_DIRECTFB=OFF \
        -DWITH_FFMPEG=%{?_with_ffmpeg:ON}%{?!_with_ffmpeg:OFF} \
        -DWITH_DSP_FFMPEG=%{?_with_ffmpeg:ON}%{?!_with_ffmpeg:OFF} \
        -DWITH_GSM=ON \
        -DWITH_GSSAPI=%{?_with_gss:ON}%{?!_with_gss:OFF} \
        -DWITH_GSTREAMER_1_0=ON -DWITH_GSTREAMER_0_10=OFF \
        -DWITH_ICU=ON \
        -DWITH_IPP=OFF \
        -DWITH_JPEG=ON \
        -DWITH_LAME=%{?_with_lame:ON}%{?!_with_lame:OFF} \
        -DWITH_MANPAGES=ON \
        -DWITH_OPENH264=%{?_with_openh264:ON}%{?!_with_openh264:OFF} \
        -DWITH_OPENSSL=ON \
        -DWITH_PCSC=ON \
        -DWITH_PULSE=ON \
        -DWITH_SERVER=ON \
        -DWITH_SERVER_INTERFACE=ON \
        -DWITH_SHADOW_X11=ON \
        -DWITH_SHADOW_MAC=ON \
        -DWITH_SAMPLE=OFF \
        -DWITH_SOXR=%{?_with_soxr:ON}%{?!_with_soxr:OFF} \
        -DWITH_WAYLAND=ON \
        -DWITH_X11=ON \
        -DWITH_XCURSOR=ON \
        -DWITH_XEXT=ON \
        -DWITH_XKBFILE=ON \
        -DWITH_XI=ON \
        -DWITH_XINERAMA=ON \
        -DWITH_XRENDER=ON \
        -DWITH_XTEST=ON \
        -DWITH_XV=ON \
        -DWITH_ZLIB=ON \
%ifarch x86_64
        -DWITH_SSE2=ON \
%else
        -DWITH_SSE2=OFF \
%endif
%ifarch armv7hl
        -DARM_FP_ABI=hard \
        -DWITH_NEON=OFF \
%endif
%ifarch armv7hnl
        -DARM_FP_ABI=hard \
        -DWITH_NEON=ON \
%endif
%ifarch armv5tel armv6l armv7l
        -DARM_FP_ABI=soft \
        -DWITH_NEON=OFF \
%endif
        -DCHANNEL_GEOMETRY=ON -DCHANNEL_GEOMETRY_CLIENT=ON \
        -DCHANNEL_URBDRC=ON \
        -DCHANNEL_URBDRC_CLIENT=ON

%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{_libdir}/cmake/

%ldconfig_scriptlets -n lib%{name}%{libfreerdp_package}
%ldconfig_scriptlets -n libwinpr%{libfreerdp_package}
%ldconfig_scriptlets -n libuwac%{uwac_package}
%ldconfig_scriptlets -n librdtk%{rdtk_package}
%ldconfig_scriptlets -n lib%{name}-server-proxy%{libfreerdp_package}

%files
%{_bindir}/x%{name}
%{_mandir}/man1/x%{name}.1%{?ext_man}
%{_mandir}/man7/wlog.7%{?ext_man}

%files sdl
%{_bindir}/sdl-%{name}
%{_mandir}/man1/sdl-freerdp.1%{?ext_man}

%files wayland
%{_bindir}/wl%{name}
%{_mandir}/man1/wl%{name}.1%{?ext_man}

%files server
%{_bindir}/%{name}-shadow-cli
%{_bindir}/winpr-hash
%{_bindir}/winpr-makecert
%{_mandir}/man1/%{name}-shadow-cli.1%{?ext_man}
%{_mandir}/man1/winpr-hash.1%{?ext_man}
%{_mandir}/man1/winpr-makecert.1%{?ext_man}

%files proxy
%{_bindir}/%{name}-proxy
%{_mandir}/man1/freerdp-proxy.1%{?ext_man}

%files -n %{name}-proxy-plugins
%dir %{_libdir}/%{name}%{major_version}
%dir %{_libdir}/%{name}%{major_version}/proxy
%{_libdir}/%{name}%{major_version}/proxy/proxy-bitmap-filter-plugin.so
%{_libdir}/%{name}%{major_version}/proxy/proxy-demo-plugin.so
%{_libdir}/%{name}%{major_version}/proxy/proxy-dyn-channel-dump-plugin.so

%files -n lib%{name}%{libfreerdp_package}
%license LICENSE
%{_libdir}/lib%{name}%{major_version}.so.*
%{_libdir}/lib%{name}-client%{major_version}.so.*
%{_libdir}/lib%{name}-shadow%{major_version}.so.*
%{_libdir}/lib%{name}-server%{major_version}.so.*
%{_libdir}/lib%{name}-shadow-subsystem%{major_version}.so.*

%files devel
%dir %{_libdir}/cmake/FreeRDP-Proxy3
%dir %{_libdir}/cmake/WinPR-tools3
%{_libdir}/cmake/FreeRDP%{major_version}
%{_libdir}/cmake/FreeRDP-Client%{major_version}
%{_libdir}/cmake/FreeRDP-Server%{major_version}
%{_libdir}/cmake/FreeRDP-Shadow%{major_version}
%{_libdir}/cmake/FreeRDP-Proxy%{major_version}/FreeRDP-ProxyConfig.cmake
%{_libdir}/cmake/FreeRDP-Proxy%{major_version}/FreeRDP-ProxyConfigVersion.cmake
%{_libdir}/cmake/FreeRDP-Proxy%{major_version}/FreeRDP-ProxyTargets-relwithdebinfo.cmake
%{_libdir}/cmake/FreeRDP-Proxy%{major_version}/FreeRDP-ProxyTargets.cmake
%{_libdir}/cmake/WinPR-tools%{major_version}/WinPR-toolsConfig.cmake
%{_libdir}/cmake/WinPR-tools%{major_version}/WinPR-toolsConfigVersion.cmake
%{_libdir}/cmake/WinPR-tools%{major_version}/WinPR-toolsTargets-relwithdebinfo.cmake
%{_libdir}/cmake/WinPR-tools%{major_version}/WinPR-toolsTargets.cmake
%{_includedir}/%{name}%{major_version}
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}%{major_version}.pc
%{_libdir}/pkgconfig/%{name}-client%{major_version}.pc
%{_libdir}/pkgconfig/%{name}-server%{major_version}.pc
%{_libdir}/pkgconfig/%{name}-shadow%{major_version}.pc
%{_libdir}/pkgconfig/%{name}-server-proxy%{major_version}.pc

%files -n libwinpr%{libfreerdp_package}
%license LICENSE
%{_libdir}/libwinpr%{major_version}.so.*
%{_libdir}/libwinpr-tools%{major_version}.so.*

%files -n winpr-devel
%{_libdir}/cmake/WinPR%{major_version}
%{_includedir}/winpr%{major_version}
%{_libdir}/libwinpr%{major_version}.so
%{_libdir}/libwinpr-tools%{major_version}.so
%{_libdir}/pkgconfig/winpr%{major_version}.pc
%{_libdir}/pkgconfig/winpr-tools%{major_version}.pc

%files -n libuwac%{uwac_package}
%license LICENSE
%{_libdir}/libuwac%{uwac_version}.so.*

%files -n uwac%{uwac_version}-devel
%{_libdir}/cmake/uwac%{uwac_version}
%{_includedir}/uwac%{uwac_version}
%{_libdir}/libuwac%{uwac_version}.so
%{_libdir}/pkgconfig/uwac%{uwac_version}.pc

%files -n librdtk%{rdtk_package}
%{_libdir}/librdtk%{rdtk_version}.so.*

%files -n rdtk%{rdtk_version}-devel
%{_libdir}/cmake/rdtk%{rdtk_version}
%{_includedir}/rdtk%{rdtk_version}
%{_libdir}/librdtk%{rdtk_version}.so
%{_libdir}/pkgconfig/rdtk%{rdtk_version}.pc

%files -n lib%{name}-server-proxy%{libfreerdp_package}
%{_libdir}/libfreerdp-server-proxy%{major_version}.so.*

%changelog
