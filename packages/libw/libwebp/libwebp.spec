#
# spec file for package libwebp
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libwebp
Version:        1.0.3
Release:        0
Summary:        Library and tools for the WebP graphics format
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            https://developers.google.com/speed/webp/

#Git-Clone:	http://git.chromium.org/webm/libwebp.git
Source:         http://downloads.webmproject.org/releases/webp/%name-%version.tar.gz
Source2:        http://downloads.webmproject.org/releases/webp/%name-%version.tar.gz.asc
Source3:        %name.keyring
Source4:        baselibs.conf
BuildRequires:  freeglut-devel
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkg-config

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
Requires:       libwebp7 = %version
Requires:       libwebpdemux2 = %version
Requires:       libwebpmux3 = %version
Requires:       libwebpdecoder3 = %version
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
%configure --disable-static \
	--enable-libwebpmux --enable-libwebpdemux \
	--enable-libwebpdecoder --enable-libwebpextras
make %{?_smp_mflags} V=1

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n libwebp7 -p /sbin/ldconfig
%postun -n libwebp7 -p /sbin/ldconfig
%post   -n libwebpdemux2 -p /sbin/ldconfig
%postun -n libwebpdemux2 -p /sbin/ldconfig
%post   -n libwebpmux3 -p /sbin/ldconfig
%postun -n libwebpmux3 -p /sbin/ldconfig
%post   -n libwebpdecoder3 -p /sbin/ldconfig
%postun -n libwebpdecoder3 -p /sbin/ldconfig
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

%if %{with extras}
%files -n libwebpextras0
%_libdir/libwebpextras.so.*
%endif

%files devel
%_libdir/libwebp*.so
%_includedir/webp/
%_libdir/pkgconfig/libwebp*.pc

%changelog
