#
# spec file for package libavif
#
# Copyright (c) 2023 SUSE LLC
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


%if 0%{?suse_version} >= 1550
%bcond_without aom
%bcond_without yuv
%else
%bcond_with aom
%bcond_with yuv
%endif

# Also update baselibs.conf if you bump the version
%global lib_soversion 15
%global lib_name libavif%{lib_soversion}

Name:           libavif
Version:        0.11.1
Release:        0
Summary:        Library for encoding and decoding .avif files
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/AOMediaCodec/libavif
#
Source:         https://github.com/AOMediaCodec/libavif/archive/v%{version}/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
#
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libjpeg8-devel
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(rav1e) >= 0.5.0
%if %{with aom}
BuildRequires:  pkgconfig(aom) >= 2.0.0
%endif
%if %{with yuv}
BuildRequires:  pkgconfig(libyuv)
%endif

%description
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

%package -n avif-tools
Summary:        Tools for libavif
Group:          Productivity/Graphics/Convertors
Provides:       libavif-tools = %{version}
Obsoletes:      libavif-tools < %{version}

%description -n avif-tools
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

This package holds the commandline tools for libavif.

%package -n %{lib_name}
#
Summary:        Shared library from libavif
Group:          Development/Libraries/C and C++

%description -n %{lib_name}
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

This package holds the shared library for libavif.

%package     -n gdk-pixbuf-loader-libavif
Summary:        AVIF image loader for GTK+ applications
Group:          Development/Libraries/C and C++

%description -n gdk-pixbuf-loader-libavif
A pixbuf-loader plugin to load AVIF images in GTK+ applications.

%package devel
Requires:       %{lib_name} = %{version}-%{release}
#
Summary:        Development files for libavif
Group:          Development/Libraries/C and C++

%description devel
This library aims to be a friendly, portable C implementation of the AV1 Image
File Format, as described here:

https://aomediacodec.github.io/av1-avif/

This package holds the development files for libavif.

%prep
%autosetup -p1

%build
%cmake \
 -DAVIF_CODEC_RAV1E:BOOL=ON \
 -DAVIF_CODEC_DAV1D:BOOL=ON \
 %if %{with aom}
 -DAVIF_CODEC_AOM:BOOL=ON \
 %endif
 -DAVIF_BUILD_APPS:BOOL=ON \
 -DAVIF_BUILD_EXAMPLES:BOOL=ON \
 -DAVIF_BUILD_GDK_PIXBUF=ON
%cmake_build

%install
%cmake_install

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
%doc *.md
%license LICENSE
%{_bindir}/avifdec
%{_bindir}/avifenc

%files -n gdk-pixbuf-loader-libavif
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-avif.so
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/avif.thumbnailer

%changelog
