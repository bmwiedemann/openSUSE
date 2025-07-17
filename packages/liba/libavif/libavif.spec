#
# spec file for package libavif
#
# Copyright (c) 2025 SUSE LLC
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


# Also update baselibs.conf if you bump the version
%global lib_soversion 16
%global lib_name libavif%{lib_soversion}
%global libargparse ee74d1b53bd680748af14e737378de57e2a0a954

# currently disabled
%bcond_with     man_pages
%bcond_with     tests

%if 0%{?sle_version} > 150400 || 0%{?suse_version} >= 1599
%ifarch aarch64 x86_64
%bcond_without  SvtAv1Enc
%else
%bcond_with     SvtAv1Enc
%endif
%endif

Name:           libavif
Version:        1.3.0
Release:        0
Summary:        Library for encoding and decoding .avif files
License:        BSD-2-Clause
URL:            https://github.com/AOMediaCodec/libavif
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source10:       https://github.com/kmurray/libargparse/archive/%{libargparse}/libargparse-%{libargparse}.tar.gz
Source99:       baselibs.conf
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(aom) >= 2.0.0
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng) >= 1.6.32
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libyuv)
BuildRequires:  pkgconfig(rav1e) >= 0.5.0
%if %{with SvtAv1Enc}
BuildRequires:  pkgconfig(SvtAv1Enc)
%endif
%if %{with man_pages}
BuildRequires:  pandoc
%endif
%if %{with tests}
BuildRequires:  ImageMagick
BuildRequires:  pkgconfig(gtest)
%endif
%if 0%{?suse_version} < 1600
BuildRequires:  gcc11-PIE
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libsharpyuv)
%endif

%description
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

%package -n avif-tools
Summary:        Tools for libavif
License:        BSD-2-Clause AND MIT
Provides:       libavif-tools = %{version}
Provides:       bundled(libargparse) = 20211125.ee74d1b
Obsoletes:      libavif-tools < %{version}

%description -n avif-tools
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

This package holds the commandline tools for libavif.

%package -n %{lib_name}
#
Summary:        Shared library from libavif

%description -n %{lib_name}
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

This package holds the shared library for libavif.

%package -n gdk-pixbuf-loader-libavif
Summary:        AVIF image loader for GTK+ applications

%description -n gdk-pixbuf-loader-libavif
A pixbuf-loader plugin to load AVIF images in GTK+ applications.

%package devel
#
Summary:        Development files for libavif
Requires:       %{lib_name} = %{version}

%description devel
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

This package holds the development files for libavif.

%prep
%autosetup -p1

mkdir ext/libargparse
tar -xf %{SOURCE10} --strip-components=1 -C ext/libargparse

%build
%define __builder ninja
%cmake \
%if 0%{?suse_version} < 1600
	-DCMAKE_C_COMPILER=gcc-11	\
	-DCMAKE_CXX_COMPILER=g++-11	\
	-DAVIF_LIBSHARPYUV:BOOL=OFF	\
%else
	-DAVIF_LIBSHARPYUV=SYSTEM	\
%endif
%if %{with SvtAv1Enc}
	-DAVIF_CODEC_SVT=SYSTEM		\
%endif
%if %{with man_pages}
	-DAVIF_BUILD_MAN_PAGES:BOOL=ON	\
%endif
%if %{with tests}
	-DAVIF_BUILD_TESTS:BOOL=ON	\
	-DAVIF_GTEST=SYSTEM		\
%endif
	-DAVIF_CODEC_AOM=SYSTEM		\
	-DAVIF_CODEC_DAV1D=SYSTEM	\
	-DAVIF_CODEC_RAV1E=SYSTEM	\
	-DAVIF_JPEG=SYSTEM		\
	-DAVIF_LIBXML2=SYSTEM		\
	-DAVIF_LIBYUV=SYSTEM		\
	-DAVIF_ZLIBPNG=SYSTEM		\
	-DAVIF_BUILD_APPS:BOOL=ON	\
	-DAVIF_BUILD_EXAMPLES:BOOL=ON	\
	-DAVIF_BUILD_GDK_PIXBUF:BOOL=ON
%cmake_build

%install
%cmake_install

%check
export PATH=%{buildroot}%{_bindir}:$PATH
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH
avifdec --version
avifenc --version
%if %{with tests}
%ifarch ppc64le
skip="-E avifgainmaptest"
%endif
%ctest --parallel 1 --timeout 60 --verbose $skip
%endif

%ldconfig_scriptlets -n %{lib_name}

%files -n %{lib_name}
%license LICENSE
%{_libdir}/libavif.so.%{lib_soversion}*

%files devel
%license LICENSE
%{_libdir}/libavif.so
%{_includedir}/avif/
%{_libdir}/cmake/libavif/
%{_libdir}/pkgconfig/libavif.pc

%files -n avif-tools
%doc CHANGELOG.md README.md SECURITY.md
%license LICENSE
%{_bindir}/avifdec
%{_bindir}/avifenc
%{_bindir}/avifgainmaputil
%if %{with man_pages}
%{_mandir}/man1/avifdec.1%{?ext_man}
%{_mandir}/man1/avifenc.1%{?ext_man}
%endif

%files -n gdk-pixbuf-loader-libavif
%license LICENSE
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-avif.so
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/avif.thumbnailer

%changelog
