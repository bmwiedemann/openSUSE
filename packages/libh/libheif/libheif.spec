#
# spec file for package libheif
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


%define gdk_pixbuf_binary_version 2.10.0
%bcond_with x265
Name:           libheif
Version:        1.14.1
Release:        0
Summary:        HEIF/AVIF file format decoder and encoder
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://github.com/strukturag/libheif
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(rav1e)
%endif
%if %{with x265}
BuildRequires:  pkgconfig(libde265)
BuildRequires:  pkgconfig(x265)
%endif

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
Supplements:    (libheif1 and libgdk_pixbuf-2_0-0)

%description -n gdk-pixbuf-loader-libheif
A ISO/IEC 23008-12:2017 HEIF file format decoder and encoder.

This package contains the GDK PixBuf Loader for %{name}.

%if %{with x265}
%package -n heif-examples
Summary:        Example binary programs for %{name}
Group:          Productivity/Graphics/Other
Requires:       libheif1 = %{version}-%{release}

%description -n heif-examples
A ISO/IEC 23008-12:2017 HEIF file format decoder and encoder.

This package contains example binary programs for %{name}.

%package -n heif-thumbnailer
Summary:        Thumbnailer for HEIF/AVIF image files
Group:          Productivity/Graphics/Other
Requires:       libheif1 = %{version}-%{release}
Supplements:    libheif1

%description -n heif-thumbnailer
Allows to show thumbnail previews of HEIF and AVIF images using %{name}.
%endif

%prep
%autosetup -p1

%build
%if %{with x265}
%cmake \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DCMAKE_INSTALL_RPATH_USE_LINK_PATH:BOOL=OFF \
    -DPLUGIN_DIRECTORY=%{_libexecdir}/libheif
%else
%cmake \
    -DWITH_LIBDE265=OFF \
    -DWITH_X265=OFF \
    -DWITH_EXAMPLES=OFF \
    -DPLUGIN_DIRECTORY=%{_libexecdir}/libheif
%endif
%cmake_build

%install
%cmake_install
%if %{with x265}
#Install examples and man pages
install -d -m 0755 %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1/
for e in heif-convert \
         heif-enc \
         heif-info \
         heif-thumbnailer
         do
            install -m 0755 build/examples/$e %{buildroot}%{_bindir}/$e
            install -m 0644 examples/$e.1 %{buildroot}%{_mandir}/man1/$e.1
         done
%else
rm -f %{buildroot}%{_datadir}/mime/packages/avif.xml
rm -f %{buildroot}%{_datadir}/mime/packages/heif.xml
rm -f %{buildroot}%{_datadir}/thumbnailers/heif.thumbnailer
%endif
%fdupes -s %{buildroot}%{_includedir}

%post -n libheif1 -p /sbin/ldconfig
%postun -n libheif1 -p /sbin/ldconfig

%post -n gdk-pixbuf-loader-libheif
%{gdk_pixbuf_loader_post}

%postun -n gdk-pixbuf-loader-libheif
%{gdk_pixbuf_loader_postun}

%files -n libheif1
%license COPYING
%{_libdir}/libheif.so.*
%{_libexecdir}/libheif

%files devel
%doc README.md
%{_includedir}/libheif
%{_libdir}/libheif.so
%{_libdir}/cmake/libheif
%{_libdir}/pkgconfig/libheif.pc

%files -n gdk-pixbuf-loader-libheif
%{_libdir}/gdk-pixbuf-2.0/%{gdk_pixbuf_binary_version}/loaders/*.so

%if %{with x265}
%files -n heif-examples
%{_bindir}/heif-convert
%{_bindir}/heif-enc
%{_bindir}/heif-info
%{_mandir}/man1/heif-convert.1%{?ext_man}
%{_mandir}/man1/heif-enc.1%{?ext_man}
%{_mandir}/man1/heif-info.1%{?ext_man}

%files -n heif-thumbnailer
%{_bindir}/heif-thumbnailer
%{_datadir}/mime/packages/avif.xml
%{_datadir}/mime/packages/heif.xml
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/heif.thumbnailer
%{_mandir}/man1/heif-thumbnailer.1%{?ext_man}
%endif

%changelog
