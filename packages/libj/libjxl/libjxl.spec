#
# spec file for package libjxl
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


%define lname   libjxl0_10
%if "@BUILD_FLAVOR@" == "gtk"
Name:           libjxl-gtk
%bcond_without gtk
%else
Name:           libjxl
%bcond_with gtk
%endif
Version:        0.10.2
Release:        0
Summary:        JPEG XL reference implementation
License:        BSD-3-Clause
URL:            https://jpegxl.info/
#Git-Clone:     https://github.com/libjxl/libjxl
Source:         https://github.com/libjxl/libjxl/archive/refs/tags/v%version.tar.gz
Source1:        baselibs.conf
Source2:        skcms.tar
Patch1:         system-jpeg.diff
BuildRequires:  asciidoc
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkg-config
%if %{with gtk}
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.36
BuildRequires:  pkgconfig(gimp-2.0) >= 2.10
BuildRequires:  pkgconfig(gimpui-2.0) >= 2.10
%endif
BuildRequires:  giflib-devel >= 5.1
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
BuildRequires:  pkgconfig(libhwy) >= 1.0.7
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
%{?suse_build_hwcaps_libs}
%if %{with gtk}
Provides:       bundled(skcms) = 0
%endif

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

%package -n gdk-pixbuf-loader-jxl
Summary:        A gdk-pixbuf loader for JPEG-XL using libjxl
Supplements:    (%lname and gdk-pixbuf)
%if %{with gtk}
%gdk_pixbuf_loader_requires
%endif

%description -n gdk-pixbuf-loader-jxl
This package provides a libjxl-based gdk-pixbuf loader for JPEG XL files.

%package -n gimp-plugin-jxl
Summary:        Plugin for GIMP to enable working with JPEG XL files
Supplements:    (%lname and gimp)

%description -n gimp-plugin-jxl
This package provides a plugin for GIMP 2.0 to enable it to work with JPEG XL files.

%package -n jxl-thumbnailer
Summary:        Generate thumbnails for JPEG XL files
BuildArch:      noarch

%description -n jxl-thumbnailer
This package provides a thumbnailer to render for JPEG XL file thumbnails,
for example, on file-browsers.

%prep
%autosetup -n libjxl-%version -a2 -p1
mv skcms third_party/

%build
%cmake -DJPEGXL_FORCE_SYSTEM_HWY=ON -DJPEGXL_FORCE_SYSTEM_BROTLI=ON \
	-DJPEGXL_FORCE_SYSTEM_LCMS2=OFF -DBUILD_TESTING=OFF \
%if %{with gtk}
	-DJPEGXL_ENABLE_PLUGINS=ON -DJPEGXL_ENABLE_SKCMS=ON \
%endif
	-DJPEGXL_ENABLE_SJPEG=OFF -DJPEGXL_ENABLE_DOXYGEN=OFF \
	-DJPEGXL_ENABLE_JPEGLI=ON
%cmake_build

%install
%cmake_install
b="%buildroot"
rm -fv "$b/%_libdir"/*.a
%if %{with gtk}
rm -Rf "$b/%_libdir"/libjxl* "$b/%_bindir" "$b/%_includedir" "$b/%_libdir/pkgconfig" "$b/%_mandir"
%endif

%ldconfig_scriptlets -n %lname

%post -n gdk-pixbuf-loader-jxl
%gdk_pixbuf_loader_post

%postun -n gdk-pixbuf-loader-jxl
%gdk_pixbuf_loader_postun

%if %{without gtk}

%files -n %lname
%license LICENSE
%_libdir/libjxl*.so.*

%files tools
%_bindir/?jpegli
%_bindir/*xl*
%_mandir/man*/*xl*

%files devel
%_includedir/jxl/
%_libdir/libjxl*.so
%_libdir/pkgconfig/*.pc

%else

%files -n gdk-pixbuf-loader-jxl
%_datadir/mime/packages/*
%_libdir/gdk-pixbuf-2.0/*/loaders/libpixbufloader-jxl.so

%files -n gimp-plugin-jxl
%_libdir/gimp/2.0/plug-ins/file-jxl/

%files -n jxl-thumbnailer
%dir %_datadir/thumbnailers
%_datadir/thumbnailers/*.thumbnailer

%endif

%changelog
