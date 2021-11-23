#
# spec file for package libyami-utils
#
# Copyright (c) 2021 SUSE LLC
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


Name:           libyami-utils
Version:        1.3.2
Release:        0
Summary:        Collection of tools for development and testing of Libyami
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://github.com/intel/libyami-utils
Source0:        %{url}/archive/%{version}.tar.gz#/%name-%{version}.tar.gz

BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdrm_intel)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libyami) >= 0.6.1
# Intel graphics hardware only available on these platforms
ExclusiveArch:  x86_64

%description
This package provides decoder/encoder/vpp programs using libyami.
The associated programs provides access to the following hardware
functions when used with libva and intel-vaapi-driver on supported
Intel hardware:

Decoders:
MPEG-2, VC-1, WMV 9 (WMV3), H.264, HEVC (H.265), VP8, VP9,
and JPEG

Encoders:
H.264, HEVC (H.265), VP8, VP9, and JPEG

Video Processing:
Sharpening, Denoise, Deinterlace, Hue, Saturation, Brightness,
Contrast, CSC and scaling

Hardware requirements:
Intel Sandybridge, Ivybridge, Haswell, Broadwell, Skylake,
Kaby Lake
Intel Baytrail, Braswell, Apollo Lake

%prep
%autosetup -p1

%build
# We do not care that something is deprecated
export CXXFLAGS="-Wno-error=deprecated-declarations"
autoreconf -fiv
%configure \
        --disable-static \
        --enable-avformat="yes" \
        --enable-dmabuf="yes" \
        %{nil}
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_mandir}/man*/*

%changelog
