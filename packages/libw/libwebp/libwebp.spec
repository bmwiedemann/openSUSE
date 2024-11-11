#
# spec file for package libwebp
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


Name:           libwebp
Version:        1.4.0
Release:        0
Summary:        Library and tools for the WebP graphics format
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://developers.google.com/speed/webp/
#Git-Clone:	https://chromium.googlesource.com/webm/libwebp/
Source:         https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-%version.tar.gz
Source2:        https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-%version.tar.gz.asc
Source3:        %name.keyring
Source4:        baselibs.conf

BuildRequires:  cmake
BuildRequires:  giflib-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)

%description
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package tools
Summary:        The WebP command line tools
Group:          Productivity/Archiving/Compression
#O/P added in 12.2
Obsoletes:      webp-tools < %version-%release
Provides:       webp-tools = %version-%release

%description tools
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package -n libwebp7
Summary:        Library for the WebP graphics format
Group:          System/Libraries

%description -n libwebp7
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package -n libwebpdemux2
Summary:        Library for extraction of data and images from WebP container files
Group:          System/Libraries

%description -n libwebpdemux2
The WebP Demux API enables extraction of images and extended format
data from WebP files. This API currently supports reading of XMP/EXIF
metadata, ICC profile and animated images.

%package -n libwebpmux3
Summary:        Library for reading/adding data to WebP container files
Group:          System/Libraries

%description -n libwebpmux3
The WebP Mux API contains methods for adding data to and reading data
from WebP files. This API currently supports XMP/EXIF metadata, ICC
profile and animation.

%package -n libwebpdecoder3
Summary:        Library for decoding WebP graphics format
Group:          System/Libraries

%description -n libwebpdecoder3
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package -n libsharpyuv0
Summary:        Library for sharpening YUV option in WebP
Group:          System/Libraries

%description -n libsharpyuv0
Library that provides the sharpening YUV option for better WebP images.

%package -n libwebpextras0
Summary:        Library for decoding WebP graphics format
Group:          System/Libraries

%description -n libwebpextras0
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently. This package contains shared libraries for less
common imports - WebPImportGray/WebPImportRGB565/WebPImportRGB4444.

%package devel
Summary:        Development files for libwebp, a library for the WebP format
Group:          Development/Libraries/C and C++
Requires:       libsharpyuv0 = %version
Requires:       libwebp7 = %version
Requires:       libwebpdecoder3 = %version
Requires:       libwebpdemux2 = %version
Requires:       libwebpmux3 = %version
%if %{with extras}
Requires:       libwebpextras0 = %version
%endif

%description devel
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
find "%buildroot" -type f -name "*.la" -delete -print

%post   -n libwebp7 -p /sbin/ldconfig
%postun -n libwebp7 -p /sbin/ldconfig
%post   -n libwebpdemux2 -p /sbin/ldconfig
%postun -n libwebpdemux2 -p /sbin/ldconfig
%post   -n libwebpmux3 -p /sbin/ldconfig
%postun -n libwebpmux3 -p /sbin/ldconfig
%post   -n libwebpdecoder3 -p /sbin/ldconfig
%postun -n libwebpdecoder3 -p /sbin/ldconfig
%post   -n libsharpyuv0 -p /sbin/ldconfig
%postun -n libsharpyuv0 -p /sbin/ldconfig
%post   -n libwebpextras0 -p /sbin/ldconfig
%postun -n libwebpextras0 -p /sbin/ldconfig

%files -n libwebp-tools
%_bindir/*
%_mandir/man*/*

%files -n libwebp7
%_libdir/libwebp.so.*

%files -n libwebpdemux2
%_libdir/libwebpdemux.so.*

%files -n libwebpmux3
%_libdir/libwebpmux.so.*

%files -n libwebpdecoder3
%_libdir/libwebpdecoder.so.*

%files -n libsharpyuv0
%_libdir/libsharpyuv.so.*

%if %{with extras}
%files -n libwebpextras0
%_libdir/libwebpextras.so.*
%endif

%files devel
%_libdir/libwebp*.so
%_libdir/libsharpyuv.so
%_includedir/webp/
%_libdir/pkgconfig/libwebp*.pc
%_libdir/pkgconfig/libsharpyuv.pc
%_datadir/WebP/

%changelog
