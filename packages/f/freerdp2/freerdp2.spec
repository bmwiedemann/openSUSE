#
# spec file for package freerdp2
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

Name:           freerdp2
Version:        2.11.7
Release:        0
Summary:        Remote Desktop Viewer Client
License:        Apache-2.0
Group:          Productivity/Networking/Other
URL:            https://www.freerdp.com/
Source0:        https://github.com/FreeRDP/FreeRDP/releases/download/%{version}/freerdp-%{version}.tar.gz
Source1:        freerdp2-rpmlintrc
# PATCH-FIX-UPSTREAM https://github.com/FreeRDP/FreeRDP/pull/7476
Patch0:         0001-Make-H.264-codec-optional-during-runtime.patch
# PATCH-FIX-OPENSUSE -- Don't let 'cmake(WinPR)' require unneeded tools
Patch1:         0001-Don-t-add-winpr-cli-tools-to-exported-CMake-targets.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2024-32661.patch CVE-2024-32661 bsc#1223348 yu.daike@suse.com -- client NULL pointer dereference
Patch2:         freerdp-CVE-2024-32661.patch
# PATCH-FIX-UPSTREAM -- gcc 14 compat
Patch3:         0001-info-Fix-incompatible-pointer-type.patch
Patch4:         0002-redirection-Fix-incompatible-pointer-type.patch
Patch5:         0003-redirection-Fix-incompatible-pointer-type.patch
Patch6:         0004-X11-fix-pointer-integer-type-mismatch.patch
Patch7:         0005-client-wayland-fix-const-correctness.patch
Patch8:         0006-warnings-fix-Wincompatible-pointer-types.patch
Patch9:         0007-server-proxy-deactivate-capture-module.patch
# PATCH-FIX-UPSTREAM -- ffmpeg 7 compat
Patch10:        0001-Fix-build-with-ffmpeg-7.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-22852.patch bsc#1256718 yfjiang@suse.com -- free up old audio formats
Patch12:        freerdp-CVE-2026-22852.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-22854.patch bsc#1256720 yfjiang@suse.com -- fix constant type
Patch13:        freerdp-CVE-2026-22854.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-22856.patch bsc#1256722 yfjiang@suse.com -- explicitly lock serial->IrpThreads
Patch15:        freerdp-CVE-2026-22856.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-22859.patch bsc#1256725 yfjiang@suse.com -- check interface indices before use
Patch17:        freerdp-CVE-2026-22859.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-23530.patch bsc#1256940 yfjiang@suse.com -- [codec,planar] fix decoder length checks
Patch18:        freerdp-CVE-2026-23530.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-23531.patch bsc#1256941 yfjiang@suse.com -- [codec,clear] fix missing length checks
Patch19:        freerdp-CVE-2026-23531.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-23532.patch bsc#1256942 yfjiang@suse.com -- [gdi,gfx] properly clamp SurfaceToSurface
Patch20:        freerdp-CVE-2026-23532.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-23534.patch bsc#1256944 yfjiang@suse.com -- [codec,clear] fix off by one length check
Patch22:        freerdp-CVE-2026-23534.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-24491.patch bsc#1257981 mgorse@suse.com -- [channels,drdynvc] reset channel_callback before close
Patch23:        freerdp-CVE-2026-24491.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-24675.patch bsc#1257982 mgorse@suse.com -- [channels,urbdrc] do not free MsConfig on failure
Patch24:        freerdp-CVE-2026-24675.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-24676.patch bsc#1257983 mgorse@suse.com -- [channels,audin] reset audin->format
Patch25:        freerdp-CVE-2026-24676.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-24679.patch bsc#1257986 mgorse@suse.com -- [channels,urbdrc] ensure InterfaceNumber is within range
Patch26:        freerdp-CVE-2026-24679.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-24681.patch bsc#1257988 mgorse@suse.com -- [channels,urbdrc] cancel all usb transfers on channel close
Patch27:        freerdp-CVE-2026-24681.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-24682.patch bsc#1257989 mgorse@suse.com -- [channels,audin] fix audin_server_recv_formats cleanup
Patch28:        freerdp-CVE-2026-24682.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-24683.patch bsc#1257990 mgorse@suse.com -- [channels,ainput] lock context when updating listener
Patch29:        freerdp-CVE-2026-24683.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-24684.patch bsc#1257991 mgorse@suse.com -- [channels,rdpsnd] terminate thread before free
Patch30:        freerdp-CVE-2026-24684.patch
# PATCH-FIX-UPSTREAM freerdp-CVE-2026-24684-2.patch bsc#1257991 mgorse@suse.com -- [channel,rdpsnd] only clean up thread before free
Patch31:        freerdp-CVE-2026-24684-2.patch
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
BuildRequires:  pkgconfig(zlib)
%{?_with_ffmpeg:
BuildRequires:  pkgconfig(libavcodec) >= 57.48.101
BuildRequires:  pkgconfig(libavutil)
}
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
# force installation of latest library version
Requires:       libfreerdp%{libfreerdp_package} = %{version}-%{release}

%description
FreeRDP is a client-side implementation of the Remote Desktop Protocol (RDP)
following the Microsoft Open Specifications. This package provides the client
application.

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

%package -n libfreerdp%{libfreerdp_package}
Summary:        Remote Desktop Viewer client library
Group:          System/Libraries
Obsoletes:      libfreerdp < %{version}-%{release}
Provides:       libfreerdp = %{version}-%{release}
Obsoletes:      libfreerdp2 < %{version}-%{release}
Provides:       libfreerdp2 = %{version}-%{release}

%description -n libfreerdp%{libfreerdp_package}
FreeRDP is a client-side implementation of the Remote Desktop Protocol (RDP)
following the Microsoft Open Specifications. This package provides the shared
libraries used by the client.

%package devel
Summary:        Development Files for freerdp
Group:          Development/Libraries/C and C++
Requires:       libfreerdp%{libfreerdp_package} = %{version}-%{release}
Requires:       winpr2-devel = %{version}-%{release}

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

%package -n winpr2-devel
Summary:        Windows Portable Runtime development files
Group:          Development/Languages/C and C++
Requires:       cmake >= 2.8
Requires:       libwinpr%{libfreerdp_package} = %{version}-%{release}
Obsoletes:      libwinpr2-devel < %{version}-%{release}
Provides:       libwinpr2-devel = %{version}-%{release}

%description -n winpr2-devel
This package contains header files for developing applications that
use the winpr and winpr-tools libraries.

%prep
%autosetup -p1 -n freerdp-%{version}

%build
if [ -z "$SOURCE_DATE_EPOCH" ]; then
find . -type f -name "*.c" -exec perl -i -pe 's{__(DATE|TIME)__}{""}g' "{}" "+"
fi

%cmake \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_INSTALL_LIBDIR=%{_lib} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_EXE_LINKER_FLAGS="-pie" \
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
        -DWITH_SHADOW_X11=OFF \
        -DWITH_SHADOW_MAC=OFF \
        -DWITH_SOXR=%{?_with_soxr:ON}%{?!_with_soxr:OFF} \
        -DWITH_WAYLAND=OFF \
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

# Update names to not conflict with the ones from freerdp3
mv %{buildroot}%{_bindir}/xfreerdp %{buildroot}%{_bindir}/x%{name}
mv %{buildroot}%{_mandir}/man1/xfreerdp.1 %{buildroot}%{_mandir}/man1/x%{name}.1

mv %{buildroot}%{_bindir}/freerdp-shadow-cli %{buildroot}%{_bindir}/%{name}-shadow-cli
mv %{buildroot}%{_bindir}/winpr-hash %{buildroot}%{_bindir}/winpr2-hash
mv %{buildroot}%{_bindir}/winpr-makecert %{buildroot}%{_bindir}/winpr2-makecert
mv %{buildroot}%{_mandir}/man1/freerdp-shadow-cli.1 %{buildroot}%{_mandir}/man1/%{name}-shadow-cli.1
mv %{buildroot}%{_mandir}/man1/winpr-hash.1 %{buildroot}%{_mandir}/man1/winpr2-hash.1
mv %{buildroot}%{_mandir}/man1/winpr-makecert.1 %{buildroot}%{_mandir}/man1/winpr2-makecert.1
mv %{buildroot}%{_mandir}/man7/wlog.7 %{buildroot}%{_mandir}/man7/wlog2.7
mv %{buildroot}%{_bindir}/freerdp-proxy %{buildroot}%{_bindir}/%{name}-proxy

%post   -n libfreerdp%{libfreerdp_package} -p /sbin/ldconfig
%postun -n libfreerdp%{libfreerdp_package} -p /sbin/ldconfig
%post -n libwinpr%{libfreerdp_package} -p /sbin/ldconfig
%postun -n libwinpr%{libfreerdp_package} -p /sbin/ldconfig

%files
%{_bindir}/x%{name}
%{_mandir}/man1/x%{name}.1%{?ext_man}

%files server
%{_bindir}/%{name}-shadow-cli
%{_bindir}/winpr2-hash
%{_bindir}/winpr2-makecert
%{_mandir}/man1/%{name}-shadow-cli.1%{?ext_man}
%{_mandir}/man1/winpr2-hash.1%{?ext_man}
%{_mandir}/man1/winpr2-makecert.1%{?ext_man}

%files proxy
%{_bindir}/%{name}-proxy

%files -n libfreerdp%{libfreerdp_package}
%license LICENSE
%{_libdir}/libfreerdp%{major_version}.so.*
%{_libdir}/libfreerdp-client%{major_version}.so.*
%{_libdir}/libfreerdp-shadow%{major_version}.so.*
%{_libdir}/libfreerdp-server%{major_version}.so.*
%{_libdir}/libfreerdp-shadow-subsystem%{major_version}.so.*
%dir %{_libdir}/freerdp%{major_version}
%{_libdir}/freerdp%{major_version}/*.so

%files devel
%{_libdir}/cmake/FreeRDP%{major_version}
%{_libdir}/cmake/FreeRDP-Client%{major_version}
%{_libdir}/cmake/FreeRDP-Server%{major_version}
%{_libdir}/cmake/FreeRDP-Shadow%{major_version}
%{_includedir}/freerdp%{major_version}
%{_libdir}/libfreerdp*.so
%{_libdir}/pkgconfig/freerdp%{major_version}.pc
%{_libdir}/pkgconfig/freerdp-client%{major_version}.pc
%{_libdir}/pkgconfig/freerdp-server%{major_version}.pc
%{_libdir}/pkgconfig/freerdp-shadow%{major_version}.pc

%files -n libwinpr%{libfreerdp_package}
%license LICENSE
%{_libdir}/libwinpr%{major_version}.so.*
%{_libdir}/libwinpr-tools%{major_version}.so.*
%{_mandir}/man7/wlog2.7%{?ext_man}

%files -n winpr2-devel
%{_libdir}/cmake/WinPR%{major_version}
%{_includedir}/winpr%{major_version}
%{_libdir}/libwinpr%{major_version}.so
%{_libdir}/libwinpr-tools%{major_version}.so
%{_libdir}/pkgconfig/winpr%{major_version}.pc
%{_libdir}/pkgconfig/winpr-tools%{major_version}.pc

%changelog
