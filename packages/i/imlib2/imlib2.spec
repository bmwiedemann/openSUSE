#
# spec file for package imlib2
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define lname	libImlib2-1
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150400
%bcond_without jxl
%else
%bcond_with jxl
%endif
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150600
%bcond_without heif
%else
%bcond_with heif
%endif
%bcond_without svg
%bcond_with postscript
Name:           imlib2
Version:        1.12.5
Release:        0
Summary:        Image handling and conversion library
License:        BSD-3-Clause
Group:          Development/Libraries/X11
URL:            https://sourceforge.net/projects/enlightenment
Source:         https://downloads.sourceforge.net/project/enlightenment/imlib2-src/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  giflib-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(libyuv)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-shm) >= 1.9
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(zlib)
Recommends:     imlib2-loaders
%if %{with heif}
BuildRequires:  pkgconfig(libheif)
%endif
%if %{with jxl}
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libjxl_threads)
%endif
%if %{with svg}
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.46
%endif
%if %{with postscript}
BuildRequires:  pkgconfig(libspectre)
%endif

%description
Imlib2 is an advanced replacement library for libraries like libXpm
that provides many more features with much greater flexibility and
speed than standard libraries, including font rasterization, rotation,
RGBA space rendering and blending, dynamic binary filters, scripting,
and more.

%package -n %{lname}
Summary:        Image handling and conversion library
Group:          System/Libraries

%description -n %{lname}
Imlib2 is an advanced replacement library for libraries like libXpm
that provides many more features with much greater flexibility and
speed than standard libraries, including font rasterization, rotation,
RGBA space rendering and blending, dynamic binary filters, scripting,
and more.

%package devel
Summary:        Imlib 2 - development libraries
Group:          Development/Libraries/X11
Requires:       %{lname} = %{version}
Requires:       xorg-x11-libX11-devel

%description devel
These are the development headers and library for imlib2.

%package filters
Summary:        Imlib 2 - plugin filters
Group:          Development/Libraries/X11
Requires:       %{lname} = %{version}

%description filters
This package has the basic set of plugin filters that come with Imlib2.

%package loaders
Summary:        Imlib 2 - image loaders
Group:          Development/Libraries/X11
Provides:       imlib2-loader_argb
Provides:       imlib2-loader_avif
Provides:       imlib2-loader_bmp
Provides:       imlib2-loader_bz2
Provides:       imlib2-loader_gif
Provides:       imlib2-loader_heif
Provides:       imlib2-loader_j2k
Provides:       imlib2-loader_jpeg
Provides:       imlib2-loader_png
Provides:       imlib2-loader_pnm
Provides:       imlib2-loader_raw
Provides:       imlib2-loader_tga
Provides:       imlib2-loader_tiff
Provides:       imlib2-loader_webp
Provides:       imlib2-loader_xpm
Provides:       imlib2-loader_xz
Provides:       imlib2-loader_yuv
Provides:       imlib2-loader_zlib
%if %{with jxl}
Provides:       imlib2-loader_jxl
%endif
%if %{with svg}
Provides:       imlib2-loader_svg
%endif
%if %{with postscript}
Provides:       imlib2-loader_ps
%endif

%description loaders
This package contains the imlib2 image loaders for: argb, bmp, gif,
jpeg, png, pnm, tga, tiff, xpm, j2k, heif, jxl.

%package demo
Summary:        Imlib 2 - demo programs
Group:          Development/Libraries/X11
Requires:       %{lname} = %{version}

%description demo
This package contains the imlib2 demo programs.

%prep
%autosetup -p1

%build
%configure \
	--disable-mmx \
%ifarch x86_64
	--enable-amd64 \
%endif
	--enable-shared \
	--enable-visibility-hiding \
	--enable-doc-build \
	--disable-static \
        --enable-werror \
        --disable-rtld-local-support \
%if %{with jxl}
	--with-jxl \
%endif
%if %{with svg}
	--with-svg \
%endif
%if %{with postscript}
	--with-ps \
%endif
%{?nil}

%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n %{lname}

%files
%license COPYING
%doc AUTHORS README
%attr(755,root,root) %dir %{_datadir}/imlib2
%{_datadir}/imlib2/*

%files -n %{lname}
%license COPYING
%{_libdir}/libImlib2.so.1*

%files devel
%license COPYING
%{_libdir}/pkgconfig/imlib2.pc
%{_includedir}/*
%{_libdir}/lib*.so

%files filters
%license COPYING
%attr(755,root,root) %dir %{_libdir}/imlib2
%attr(755,root,root) %{_libdir}/imlib2/filters

%files loaders
%license COPYING
%attr(755,root,root) %dir %{_libdir}/imlib2
%attr(755,root,root) %{_libdir}/imlib2/loaders

%files demo
%{_bindir}/imlib2_*

%changelog
