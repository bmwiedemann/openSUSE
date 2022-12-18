#
# spec file for package freerdp
#
# Copyright (c) 2022 SUSE LLC
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

# enable -DWITH_GSSAPI=ON again after #gh/FreeRDP/FreeRDP/4348 has been fixed
#global _with_gss 1

%define major_version 2
%define libfreerdp_package %{major_version}-%{major_version}
%define uwac_version 0
%define uwac_package %{uwac_version}-%{uwac_version}
%ifarch aarch64 %{arm}
%define _lto_cflags %{nil}
%endif

Name:           freerdp
Version:        2.9.0
Release:        0
Summary:        Remote Desktop Viewer Client
License:        Apache-2.0
Group:          Productivity/Networking/Other
URL:            https://www.freerdp.com/
Source0:        https://github.com/FreeRDP/FreeRDP/archive/%{version}.tar.gz#/FreeRDP-%{version}.tar.gz
Source1:        freerdp-rpmlintrc
# PATCH-FIX-UPSTREAM freerdp-channels-off-link-fix.diff -- based on https://github.com/FreeRDP/FreeRDP/pull/7235
Patch0:         freerdp-builtin-channels-off-link-fix.diff
# PATCH-FIX-UPSTREAM https://github.com/FreeRDP/FreeRDP/pull/7476
Patch1:         0001-Make-H.264-codec-optional-during-runtime.patch
# PATCH-FIX-UPSTREAM https://github.com/FreeRDP/FreeRDP/pull/8551 -- slightly modified: see -DWITH_PLUGIN_RPATH_ONLY
Patch2:         freerdp-fix-rpath-settings.diff
BuildRequires:  chrpath
BuildRequires:  cmake >= 2.8
BuildRequires:  cups-devel
BuildRequires:  ed
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libgsm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(icu-i18n)
%{?_with_gss:BuildRequires:  pkgconfig(krb5) >= 1.13}
%{?_with_lame:BuildRequires:  libmp3lame-devel}
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libusb-1.0)
%{?_with_openh264:BuildRequires:  libopenh264-devel}
BuildRequires:  pkgconfig(openssl)
%{?_with_soxr:BuildRequires:  pkgconfig(soxr)}
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
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
%{?_with_ffmpeg:
BuildRequires:  pkgconfig(libavcodec) >= 57.48.101
BuildRequires:  pkgconfig(libavutil)
}
# force installation of latest library version
Requires:       lib%{name}%{libfreerdp_package} = %{version}-%{release}

%description
FreeRDP is a client-side implementation of the Remote Desktop Protocol (RDP)
following the Microsoft Open Specifications. This package provides the client
application.

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

%package -n lib%{name}%{libfreerdp_package}
Summary:        Remote Desktop Viewer client library
Group:          System/Libraries
Obsoletes:      lib%{name} < %{version}-%{release}
Provides:       lib%{name} = %{version}-%{release}
Obsoletes:      lib%{name}2 < %{version}-%{release}
Provides:       lib%{name}2 = %{version}-%{release}

%description -n lib%{name}%{libfreerdp_package}
FreeRDP is a client-side implementation of the Remote Desktop Protocol (RDP)
following the Microsoft Open Specifications. This package provides the shared
libraries used by the client.

%package devel
Summary:        Development Files for freerdp
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{libfreerdp_package} = %{version}-%{release}
Requires:       winpr-devel = %{version}-%{release}

%description devel
This package contains development files necessary for developing applications
based on libfreerdp.

%package -n     libwinpr%{libfreerdp_package}
Summary:        Windows Portable Runtime
Group:          Productivity/Networking/Other
Obsoletes:      libwinpr2 < %{version}-%{release}
Provides:       libwinpr2 = %{version}-%{release}

%description -n libwinpr%{libfreerdp_package}
WinPR provides API compatibility for applications targeting non-Windows
environments. When on Windows, the original native API is being used instead of
the equivalent WinPR implementation, without having to modify the code using it.

%package -n winpr-devel
Summary:        Windows Portable Runtime development files
Group:          Development/Languages/C and C++
Requires:       cmake >= 2.8
Requires:       libwinpr%{libfreerdp_package} = %{version}-%{release}
Obsoletes:      libwinpr2-devel < %{version}-%{release}
Provides:       libwinpr2-devel = %{version}-%{release}

%description -n winpr-devel
This package contains header files for developing applications that
use the winpr and winpr-tools libraries.

%package -n     libuwac%{uwac_package}
Summary:        Use wayland as a client
Group:          Productivity/Networking/Other

%description -n libuwac%{uwac_package}
Using wayland as a client (uwac) is a library to provide common
functionality for wayland clients.

%package -n uwac%{uwac_package}-devel
Summary:        Remote Desktop Toolkit libuwac development files
Group:          Development/Languages/C and C++
Requires:       cmake >= 2.8
Requires:       libuwac%{uwac_package} = %{version}-%{release}
Obsoletes:      libuwac0-devel < %{version}-%{release}
Provides:       libuwac0-devel = %{version}-%{release}

%description -n uwac%{uwac_package}-devel
This package contains header files for developing applications that
use the uwac library.

%prep
%autosetup -p1 -n FreeRDP-%{version}

%build
if [ -z "$SOURCE_DATE_EPOCH" ]; then
find . -type f -name "*.c" -exec perl -i -pe 's{__(DATE|TIME)__}{""}g' "{}" "+"
fi
export LDFLAGS="-pie"
export CFLAGS="%{optflags} -fPIE -pie"

%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_INSTALL_LIBDIR=%{_lib} \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DWITH_ALSA=ON \
	-DWITH_CAIRO=ON \
	-DWITH_CUPS=ON \
	-DWITH_CHANNELS=ON -DBUILTIN_CHANNELS=OFF \
	-DWITH_PLUGIN_RPATH_ONLY=ON \
        -DWITH_CLIENT=ON \
        -DWITH_DIRECTFB=OFF \
        -DWITH_FFMPEG=%{?_with_ffmpeg:ON}%{?!_with_ffmpeg:OFF} \
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

%make_build

%install
cd build
%make_install
%fdupes %{buildroot}%{_libdir}/cmake/

%post   -n lib%{name}%{libfreerdp_package} -p /sbin/ldconfig
%postun -n lib%{name}%{libfreerdp_package} -p /sbin/ldconfig
%post -n libwinpr%{libfreerdp_package} -p /sbin/ldconfig
%postun -n libwinpr%{libfreerdp_package} -p /sbin/ldconfig
%post -n libuwac%{uwac_package} -p /sbin/ldconfig
%postun -n libuwac%{uwac_package} -p /sbin/ldconfig

%files
%{_bindir}/x%{name}
%{_mandir}/man1/x%{name}.1%{?ext_man}
%{_mandir}/man7/wlog.7%{?ext_man}

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

%files -n lib%{name}%{libfreerdp_package}
%license LICENSE
%{_libdir}/lib%{name}%{major_version}.so.*
%{_libdir}/lib%{name}-client%{major_version}.so.*
%{_libdir}/lib%{name}-shadow%{major_version}.so.*
%{_libdir}/lib%{name}-server%{major_version}.so.*
%{_libdir}/lib%{name}-shadow-subsystem%{major_version}.so.*
%dir %{_libdir}/freerdp2
%{_libdir}/freerdp2/*.so

%files devel
%{_libdir}/cmake/FreeRDP%{major_version}
%{_libdir}/cmake/FreeRDP-Client%{major_version}
%{_libdir}/cmake/FreeRDP-Server%{major_version}
%{_libdir}/cmake/FreeRDP-Shadow%{major_version}
%{_includedir}/%{name}%{major_version}
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}%{major_version}.pc
%{_libdir}/pkgconfig/%{name}-client%{major_version}.pc
%{_libdir}/pkgconfig/%{name}-server%{major_version}.pc
%{_libdir}/pkgconfig/%{name}-shadow%{major_version}.pc

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

%files -n uwac%{uwac_package}-devel
%{_libdir}/cmake/uwac%{uwac_version}
%{_includedir}/uwac%{uwac_version}
%{_libdir}/libuwac%{uwac_version}.so
%{_libdir}/pkgconfig/uwac%{uwac_version}.pc

%changelog
