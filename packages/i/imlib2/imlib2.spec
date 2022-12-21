#
# spec file for package imlib2
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


%define lname	libImlib2-1
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150400
%bcond_without jxl
%else
%bcond_with jxl
%endif
%bcond_with svg
%bcond_with postscript
Name:           imlib2
Version:        1.10.0
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
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-shm) >= 1.9
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(zlib)
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
Recommends:     imlib2-loaders

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
Provides:       imlib2-loader_bmp
Provides:       imlib2-loader_bz2
Provides:       imlib2-loader_gif
Provides:       imlib2-loader_heif
Provides:       imlib2-loader_j2k
Provides:       imlib2-loader_jpeg
Provides:       imlib2-loader_png
Provides:       imlib2-loader_pnm
Provides:       imlib2-loader_tga
Provides:       imlib2-loader_tiff
Provides:       imlib2-loader_xpm
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

%prep
%setup -q

%build
%configure \
%ifarch %{ix86}
	--enable-mmx \
%else
	--disable-mmx \
%endif
%ifarch x86_64
	--enable-amd64 \
%endif
	--enable-shared \
	--enable-visibility-hiding \
	--enable-doc-build \
	--disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%defattr(-,root,root,0755)
%license COPYING
%doc AUTHORS README
%{_bindir}/imlib2_bumpmap
%{_bindir}/imlib2_colorspace
%{_bindir}/imlib2_conv
%{_bindir}/imlib2_load
%{_bindir}/imlib2_poly
%{_bindir}/imlib2_show
%{_bindir}/imlib2_test
%{_bindir}/imlib2_view
%{_bindir}/imlib2_grab
%attr(755,root,root) %dir %{_datadir}/imlib2
%{_datadir}/imlib2/*

%files -n %{lname}
%{_libdir}/libImlib2.so.1*

%files devel
%defattr(-,root,root,0755)
%{_libdir}/pkgconfig/imlib2.pc
%{_includedir}/*
%{_libdir}/lib*.so

%files filters
%attr(755,root,root) %dir %{_libdir}/imlib2
%attr(755,root,root) %{_libdir}/imlib2/filters

%files loaders
%attr(755,root,root) %dir %{_libdir}/imlib2
%attr(755,root,root) %{_libdir}/imlib2/loaders

%changelog
