#
# spec file for package libheif
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%define gdk_pixbuf_binary_version 2.10.0
%bcond_with x265
%bcond_with kvazaar
%bcond_with svtenc
%if 0%{?suse_version} > 1500
%ifarch aarch64 riscv64 x86_64
%bcond_without svtenc
%endif
%endif

Name:           libheif
Version:        1.19.1
Release:        0
Summary:        HEIF/AVIF file format decoder and encoder
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://github.com/strukturag/libheif
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-FIX=OPENSUSE - HEVC encoding is unavailable by default
Patch0:         only-run-test-when-HEVC-encoder-available.patch
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 8
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
%if %{with kvazaar}
BuildRequires:  pkgconfig(kvazaar)
%endif
BuildRequires:  pkgconfig(rav1e)
%if %{with svtenc}
BuildRequires:  pkgconfig(SvtAv1Enc)
%endif
%if %{with x265}
BuildRequires:  pkgconfig(libde265)
BuildRequires:  pkgconfig(x265)
%endif
%if %{with test}
BuildArch:      noarch
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

%package aom
Summary:        Plugin AOM encoder and decoder for AVIF
Group:          System/Libraries
Supplements:    libheif1
Requires:       libheif1 = %{version}-%{release}

%description aom
This plugin provides the AOM encoder and decoder for AVIF to libheif. Packaged separately
so that the libraries it requires are not pulled in by default by libheif.

%package dav1d
Summary:        Plugin dav1d decoder for AVIF
Group:          System/Libraries
Supplements:    libheif1
Requires:       libheif1 = %{version}-%{release}

%description dav1d
This plugin provides the dav1d encoder for AVIF to libheif. Packaged separately
so that the libraries it requires are not pulled in by default by libheif.

%package ffmpeg
Summary:        Plugin FFMPEG decoder (HW acc) for HEIC
Group:          System/Libraries
Supplements:    libheif1
Requires:       libheif1 = %{version}-%{release}

%description ffmpeg
This plugin provides the FFMPEG decoder (HW acc) for HEIC to libheif. Packaged separately
so that the libraries it requires are not pulled in by default by libheif.

%package jpeg
Summary:        Plugin encoder and decoder for JPEG in HEIF
Group:          System/Libraries
Supplements:    libheif1
Requires:       libheif1 = %{version}-%{release}

%description jpeg
This plugin provides the encoder and decoder for JPEG in HEIF to libheif. Packaged separately
so that the libraries it requires are not pulled in by default by libheif.

%if %{with kvazaar}
%package kvazaar
Summary:        Plugin kvazaar encoder for HEIC
Group:          System/Libraries
Supplements:    libheif1
Requires:       libheif1 = %{version}-%{release}

%description kvazaar
This plugin provides the kvazaar encoder for HEIC to libheif. Packaged separately
so that the libraries it requires are not pulled in by default by libheif.
%endif

%package openjpeg
Summary:        Plugin OpenJPEG J2K encoder and decoder for JPEG-2000 in HEIF
Group:          System/Libraries
Supplements:    libheif1
Requires:       libheif1 = %{version}-%{release}

%description openjpeg
This plugin provides the OpenJPEG J2K encoder and decoder for JPEG to libheif. Packaged separately
so that the libraries it requires are not pulled in by default by libheif.

%package rav1e
Summary:        Plugin rav1e encoder for AVIF
Group:          System/Libraries
Supplements:    libheif1
Requires:       libheif1 = %{version}-%{release}

%description rav1e
This plugin provides the rav1e encoder for AVIF to libheif. Packaged separately
so that the libraries it requires are not pulled in by default by libheif.

%if %{with svtenc}
%package svtenc
Summary:        Plugin SVT-AV1 encoder for AVIF
Group:          System/Libraries
Supplements:    libheif1
Requires:       libheif1 = %{version}-%{release}

%description svtenc
This plugin provides the SVT-AV1 encoder for AVIF to libheif. Packaged separately
so that the libraries it requires are not pulled in by default by libheif.
%endif

%if %{with x265}
%package HEIF
Summary:        Plugin for HEIF decoder and encoder
Group:          System/Libraries
Supplements:    libheif1
Requires:       libheif1 = %{version}-%{release}

%description HEIF
This plugin provides an decoder and encoder for HEIF to libheif. Packaged separately
so that the libraries it requires are not pulled in by default by libheif.
%endif

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
Requires:       libheif1 = %{version}-%{release}

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
Supplements:    libheif1
Requires:       libheif1 = %{version}-%{release}

%description -n heif-thumbnailer
Allows to show thumbnail previews of HEIF and AVIF images using %{name}.
%endif

%prep
%autosetup -p1

%build
# https://github.com/strukturag/libheif/issues/1281
sed -i '/add_libheif_test(encode)/d' tests/CMakeLists.txt
%cmake \
%if %{with test}
        --preset=testing \
%else
	-DWITH_AOM_DECODER=ON \
	-DWITH_AOM_DECODER_PLUGIN=ON \
	-DWITH_AOM_ENCODER=ON \
	-DWITH_AOM_ENCODER_PLUGIN=ON \
	-DWITH_DAV1D=ON \
	-DWITH_DAV1D_PLUGIN=ON \
%if %{with x265}
	-DWITH_X265=ON \
	-DWITH_LIBDE265=ON \
	-DWITH_X265_PLUGIN=ON \
	-DWITH_LIBDE265_PLUGIN=ON \
	-DWITH_EXAMPLES=ON \
%else
	-DWITH_LIBDE265=OFF \
	-DWITH_X265=OFF \
	-DWITH_EXAMPLES=OFF \
%endif
	-DWITH_RAV1E=ON \
	-DWITH_RAV1E_PLUGIN=ON \
%if %{with svtenc}
	-DWITH_SvtEnc=ON \
	-DWITH_SvtEnc_PLUGIN=ON \
%else
	-DWITH_SvtEnc=OFF \
%endif
	-DWITH_JPEG_DECODER=ON \
	-DWITH_JPEG_DECODER_PLUGIN=ON \
	-DWITH_JPEG_ENCODER=ON \
	-DWITH_JPEG_ENCODER_PLUGIN=ON \
	-DWITH_UNCOMPRESSED_CODEC=ON \
%if %{with kvazaar}
	-DWITH_KVAZAAR=ON \
	-DWITH_KVAZAAR_PLUGIN=ON \
%else
	-DWITH_KVAZAAR=OFF \
%endif
	-DWITH_OpenH264_DECODER=OFF \
	-DWITH_OpenJPEG_DECODER=ON \
	-DWITH_OpenJPEG_DECODER_PLUGIN=ON \
	-DWITH_OpenJPEG_ENCODER=ON \
	-DWITH_OpenJPEG_ENCODER_PLUGIN=ON \
	-DWITH_FFMPEG_DECODER=ON \
	-DWITH_FFMPEG_DECODER_PLUGIN=ON \
	-DCMAKE_SKIP_RPATH=ON \
	-DBUILD_TESTING=OFF \
	-DWITH_REDUCED_VISIBILITY=ON \
	-DWITH_DEFLATE_HEADER_COMPRESSION=ON \
	-DWITH_LIBSHARPYUV=ON \
	-DWITH_FUZZERS=OFF \
%if 0%{?suse_version} <= 1500
	-DCMAKE_CXX_FLAGS="-pthread" \
%endif
	-DPLUGIN_DIRECTORY=%{_libexecdir}/libheif \
%endif
	%nil
%cmake_build

%if %{with test}
%check
cd build
export LD_LIBRARY_PATH=$(pwd)/libheif
make test
%endif

%if !%{with test}

%install
%cmake_install
%if %{with x265}
#Install examples and man pages
install -d -m 0755 %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1/
for e in heif-dec \
         heif-enc \
         heif-info \
         heif-thumbnailer
         do
            install -m 0755 build/examples/$e %{buildroot}%{_bindir}/$e
            chrpath --delete %{buildroot}%{_bindir}/$e
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
%dir %{_libexecdir}/libheif

%files aom
%{_libexecdir}/libheif/libheif-aomdec.so
%{_libexecdir}/libheif/libheif-aomenc.so

%files dav1d
%{_libexecdir}/libheif/libheif-dav1d.so

%files ffmpeg
%{_libexecdir}/libheif/libheif-ffmpegdec.so

%files jpeg
%{_libexecdir}/libheif/libheif-jpegdec.so
%{_libexecdir}/libheif/libheif-jpegenc.so

%if %{with kvazaar}
%files kvazaar
%{_libexecdir}/libheif/libheif-kvazaar.so
%endif

%files openjpeg
%{_libexecdir}/libheif/libheif-j2kdec.so
%{_libexecdir}/libheif/libheif-j2kenc.so

%files rav1e
%{_libexecdir}/libheif/libheif-rav1e.so

%if %{with svtenc}
%files svtenc
%{_libexecdir}/libheif/libheif-svtenc.so
%endif

%if %{with x265}
%files HEIF
%{_libexecdir}/libheif/libheif-libde265.so
%{_libexecdir}/libheif/libheif-x265.so
%endif

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
%{_bindir}/heif-dec
%{_bindir}/heif-enc
%{_bindir}/heif-info
%{_mandir}/man1/heif-dec.1%{?ext_man}
%{_mandir}/man1/heif-enc.1%{?ext_man}
%{_mandir}/man1/heif-info.1%{?ext_man}

%files -n heif-thumbnailer
%{_bindir}/heif-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/heif.thumbnailer
%{_mandir}/man1/heif-thumbnailer.1%{?ext_man}
%endif

%endif

%changelog
