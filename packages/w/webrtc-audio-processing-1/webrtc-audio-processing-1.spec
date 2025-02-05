# vim: set sw=4 ts=4 et nu:
#
# spec file for package webrtc-audio-processing-1
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


%define pkg_soname  1-3
%define soname      3
# Please submit bugfixes or comments via http://bugs.opensuse.org/
Name:           webrtc-audio-processing-1
Version:        1.3
Release:        0
Summary:        Real-Time Communication Library for Web Browsers
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/
Source:         webrtc-audio-processing-%{version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM fix-build.patch alarrosa@suse.com -- Fix a number of "control reaches end of non-void function" errors
Patch0:         fix-build.patch
# PATCH-FIX-UPSTREAN big_endian_support.patch https://bugs.freedesktop.org/show_bug.cgi?id=95738
Patch1:         big_endian_support.patch
# PATCH-FIX-UPSTREAN big_endian_support.patch https://bugs.freedesktop.org/show_bug.cgi?id=95738
Patch2:         big_endian_support_2.patch
Patch3:         fix-i586.patch
# PATCH-FIX-OPENSUSE webrtc-(ppc64|s390x|aarch64).patch
Patch100:       webrtc-ppc64.patch
Patch101:       webrtc-s390x.patch
# PATCH-FIX-OPENSUSE reduce-meson-dep.patch
Patch102:       reduce-meson-dep.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  meson >= 0.59.4
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  cmake(absl)
ExcludeArch:    s390 s390x ppc64

%description
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n libwebrtc-audio-processing-%{pkg_soname}
Summary:        Real-Time Communication Library for Web Browsers
Group:          System/Libraries

%description -n libwebrtc-audio-processing-%{pkg_soname}
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n libwebrtc-audio-processing-1-devel
Summary:        Real-Time Communication Library for Web Browsers
Group:          Development/Libraries/C and C++
Requires:       libwebrtc-audio-processing-%{pkg_soname} = %{version}

%description -n libwebrtc-audio-processing-1-devel
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n libwebrtc-audio-processing-1-devel-static
Summary:        Real-Time Communication Library for Web Browsers
Group:          Development/Libraries/C and C++
Requires:       libwebrtc-audio-processing-1-devel = %{version}

%description -n libwebrtc-audio-processing-1-devel-static
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n libwebrtc-audio-coding-%{pkg_soname}
Summary:        Real-Time Communication Library for Web Browsers
Group:          System/Libraries

%description -n libwebrtc-audio-coding-%{pkg_soname}
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n libwebrtc-audio-coding-1-devel
Summary:        Real-Time Communication Library for Web Browsers
Group:          Development/Libraries/C and C++
Requires:       libwebrtc-audio-coding-%{pkg_soname} = %{version}

%description -n libwebrtc-audio-coding-1-devel
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n libwebrtc-audio-coding-1-devel-static
Summary:        Real-Time Communication Library for Web Browsers
Group:          Development/Libraries/C and C++
Requires:       libwebrtc-audio-coding-1-devel = %{version}

%description -n libwebrtc-audio-coding-1-devel-static
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%prep
%autosetup -p1 -N -n webrtc-audio-processing-%{version}
sed -i 's/\r$//' AUTHORS
%patch -P 0 -p1
#%%patch -P 1 -p1
#%%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 100 -p1
%patch -P 101 -p1
%patch -P 102 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%meson \
	-Dc_std=gnu11 \
	-Dcpp_std=gnu++17 \
	-Ddefault_library=both \
	-Dc_args="${CFLAGS} ${LDFLAGS}" \
	-Dcpp_args="${CXXFLAGS} ${LDFLAGS}" \
	%{nil}
%meson_build

%install
%meson_install

find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libwebrtc-audio-processing-%{pkg_soname} -p /sbin/ldconfig
%postun -n libwebrtc-audio-processing-%{pkg_soname} -p /sbin/ldconfig
%post   -n libwebrtc-audio-coding-%{pkg_soname} -p /sbin/ldconfig
%postun -n libwebrtc-audio-coding-%{pkg_soname} -p /sbin/ldconfig

%files -n libwebrtc-audio-processing-%{pkg_soname}
%license COPYING
%doc AUTHORS NEWS README.md UPDATING.md
%{_libdir}/libwebrtc-audio-processing-1.so.%{soname}*

%files -n libwebrtc-audio-processing-1-devel
%{_includedir}/webrtc-audio-processing-1
%{_libdir}/libwebrtc-audio-processing-1.so
%{_libdir}/pkgconfig/webrtc-audio-processing-1.pc

%files -n libwebrtc-audio-processing-1-devel-static
%{_libdir}/libwebrtc-audio-processing-1.a

%files -n libwebrtc-audio-coding-%{pkg_soname}
%license COPYING
%doc AUTHORS NEWS README.md UPDATING.md
%{_libdir}/libwebrtc-audio-coding-1.so.%{soname}*

%files -n libwebrtc-audio-coding-1-devel
%{_libdir}/libwebrtc-audio-coding-1.so
%{_libdir}/pkgconfig/webrtc-audio-coding-1.pc

%files -n libwebrtc-audio-coding-1-devel-static
%{_libdir}/libwebrtc-audio-coding-1.a

%changelog
