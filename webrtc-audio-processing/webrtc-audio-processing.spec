# vim: set sw=4 ts=4 et nu:
#
# spec file for package webrtc-audio-processing
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define soname      1
# Please submit bugfixes or comments via http://bugs.opensuse.org/
Name:           webrtc-audio-processing
Version:        0.3
Release:        0
Summary:        Real-Time Communication Library for Web Browsers
License:        BSD-3-Clause
Group:          System/Libraries
Url:            http://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/
Source:         http://freedesktop.org/software/pulseaudio/webrtc-audio-processing/webrtc-audio-processing-%{version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAN big_endian_support.patch https://bugs.freedesktop.org/show_bug.cgi?id=95738
Patch1:         big_endian_support.patch
# PATCH-FIX-UPSTREAN big_endian_support.patch https://bugs.freedesktop.org/show_bug.cgi?id=95738
Patch2:         big_endian_support_2.patch
# PATCH-FIX-OPENSUSE webrtc-(ppc64|s390x|aarch64).patch
Patch100:       webrtc-ppc64.patch
Patch101:       webrtc-s390x.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n libwebrtc_audio_processing%{soname}
Summary:        Real-Time Communication Library for Web Browsers
Group:          System/Libraries

%description -n libwebrtc_audio_processing%{soname}
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n libwebrtc_audio_processing-devel
Summary:        Real-Time Communication Library for Web Browsers
Group:          Development/Libraries/C and C++
Requires:       libwebrtc_audio_processing%{soname} = %{version}

%description -n libwebrtc_audio_processing-devel
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%package -n libwebrtc_audio_processing-devel-static
Summary:        Real-Time Communication Library for Web Browsers
Group:          Development/Libraries/C and C++
Requires:       libwebrtc_audio_processing-devel = %{version}

%description -n libwebrtc_audio_processing-devel-static
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%prep
%setup -q -T -c "%{name}-%{version}"
xz --decompress --stdout "%{SOURCE0}" | tar xf - --strip-components=1
sed -i 's/\r$//' AUTHORS
%patch1 -p1
%patch2 -p1
%patch100
%patch101

%build
%configure
make %{?_smp_mflags} V=1

%install
%makeinstall

rm -f "%{buildroot}%{_libdir}"/*.la

%post   -n libwebrtc_audio_processing%{soname} -p /sbin/ldconfig

%postun -n libwebrtc_audio_processing%{soname} -p /sbin/ldconfig

%files -n libwebrtc_audio_processing%{soname}
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README.md UPDATING.md
%{_libdir}/libwebrtc_audio_processing.so.%{soname}
%{_libdir}/libwebrtc_audio_processing.so.%{soname}.*.*

%files -n libwebrtc_audio_processing-devel
%defattr(-,root,root)
%{_includedir}/webrtc_audio_processing
%{_libdir}/libwebrtc_audio_processing.so
%{_libdir}/pkgconfig/webrtc-audio-processing.pc

%files -n libwebrtc_audio_processing-devel-static
%defattr(-,root,root)
%{_libdir}/libwebrtc_audio_processing.a

%changelog
