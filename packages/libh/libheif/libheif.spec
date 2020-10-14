#
# spec file for package libheif
#
# Copyright (c) 2020 SUSE LLC
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

%define gdk_pixbuf_binary_version 2.10.0

Name:           libheif
Version:        1.9.1
Release:        0
Summary:        HEIF/AVIF file format decoder and encoder
#
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://github.com/strukturag/libheif
#
Source0:        https://github.com/strukturag/libheif/releases/download/v%{version}/%{name}-%{version}.tar.gz
#
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(dav1d)
%if 0%{?sle_version} > 150200 || 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(rav1e)
%endif
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  gcc-c++
Recommends:     %{name}-lang


%description
libheif is an ISO/IEC 23008-12:2017 HEIF and AVIF (AV1 Image File Format) file
format decoder and encoder.

HEIF and AVIF are new image file formats employing HEVC (H.265) or AV1 image
coding, respectively, for the best compression ratios currently possible.


%package -n libheif1
Summary:        HEIF/AVIF file format decoder and encoder
Group:          System/Libraries

%description -n libheif1
libheif is an ISO/IEC 23008-12:2017 HEIF and AVIF (AV1 Image File Format) file
format decoder and encoder.

HEIF and AVIF are new image file formats employing HEVC (H.265) or AV1 image
coding, respectively, for the best compression ratios currently possible.

For AVIF libaom, dav1d, or rav1e are used as codecs. HEIF support is not
provided.

%package devel
Summary:        Devel Package for %{name}
Group:          Development/Libraries/C and C++
Requires:       libheif1 = %{version}-%{release}


%description devel
libheif is a ISO/IEC 23008-12:2017 HEIF file format decoder and encoder. 
This package contains the header files.


%package -n gdk-pixbuf-loader-libheif
Summary:        GDK PixBuf Loader for %{name}
Group:          System/Libraries


%description -n gdk-pixbuf-loader-libheif
A ISO/IEC 23008-12:2017 HEIF file format decoder and encoder.

This package contains the GDK PixBuf Loader for %{name}.


%prep
%autosetup -p1


%build
%cmake \
    -DWITH_LIBDE265=OFF \
    -DWITH_X265=OFF \
    -DWITH_EXAMPLES=OFF

%cmake_build


%install
%cmake_install

%fdupes -s %{buildroot}%{_includedir}


%post -n libheif1 -p /sbin/ldconfig
%postun -n libheif1 -p /sbin/ldconfig


%files -n libheif1
%license COPYING
%{_libdir}/libheif.so.*


%files devel
%doc README.md
%{_includedir}/libheif
%{_libdir}/libheif.so
%{_libdir}/cmake/libheif
%{_libdir}/pkgconfig/libheif.pc


%files -n gdk-pixbuf-loader-libheif
%{_libdir}/gdk-pixbuf-2.0/%{gdk_pixbuf_binary_version}/loaders/*.so

%changelog
