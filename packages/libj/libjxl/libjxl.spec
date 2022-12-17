#
# spec file for package libjxl
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


Name:           libjxl
%define lname   libjxl0_7
Version:        0.7.0
Release:        0
Summary:        JPEG XL reference implementation
License:        BSD-3-Clause
URL:            https://jpegxl.info/
#Git-Clone:     https://github.com/libjxl/libjxl
Source:         https://github.com/libjxl/libjxl/archive/refs/tags/v%version.tar.gz
Source1:        baselibs.conf
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
BuildRequires:  pkgconfig(libhwy) >= 1.0

%description
JPEG XL is a raster-graphics file format that supports both lossy and
lossless compression.

This is the reference implementation of JPEG XL, with encoder and decoder.

%package -n %lname
Summary:        Library for encoding and decoding JPEG XL raster graphic images

%description -n %lname
JPEG XL is a raster-graphics file format that supports both lossy and
lossless compression.

%package devel
Summary:        Development for libjxl, an en-/decoder for JPEG XL
Requires:       %lname = %version

%description devel
JPEG XL is a raster-graphics file format that supports both lossy and
lossless compression.

This is the reference implementation of JPEG XL, with encoder and decoder.

%package tools
Summary:        Command-line utilities to convert from/to JPEG XL

%description tools
Command-line utilities to convert from/to JPEG XL.

%prep
%autosetup -p1

%build
%cmake -DJPEGXL_FORCE_SYSTEM_HWY=ON -DJPEGXL_FORCE_SYSTEM_BROTLI=ON \
	-DJPEGXL_FORCE_SYSTEM_LCMS2=ON -DBUILD_TESTING=OFF \
	-DJPEGXL_ENABLE_PLUGINS=OFF -DJPEGXL_ENABLE_SKCMS=OFF \
	-DJPEGXL_ENABLE_SJPEG=OFF

%install
%cmake_install
rm -fv %buildroot/%_libdir/*.a

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license LICENSE
%_libdir/libjxl*.so.*

%files tools
%_bindir/cjpeg_hdr
%_bindir/*xl*

%files devel
%_includedir/jxl/
%_libdir/libjxl.so
%_libdir/libjxl_threads.so
%_libdir/pkgconfig/*.pc

%changelog
