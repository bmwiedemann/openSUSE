#
# spec file for package libdevil
#
# Copyright (c) 2021 SUSE LLC
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


# SONAME Version tags (*.so.$NUM)
%define libIL 1
Name:           libdevil
Version:        1.7.8
Release:        0
Summary:        A cross-platform image library
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            http://openil.sourceforge.net/
Source:         http://sourceforge.net/projects/openil/files/DevIL/1.7.8/DevIL-%{version}.tar.gz
Patch0:         DevIL-%{version}-return-random-data.patch
# From Gentoo
Patch1:         DevIL-%{version}-CVE-2009-3994.patch
# From Gentoo
Patch2:         DevIL-%{version}-libpng14.patch
# From Fedora
Patch3:         DevIL-%{version}-gcc5.patch
# PATCH-FIX-UPSTREAM
Patch4:         jp2-remove-use-of-uchar-define.patch
# build with openexr3
Patch5:         libdevil-openexr3.patch
BuildRequires:  Mesa-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  SDL-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrender)

%description
Developer's Image Library (DevIL) is a programmer's library to
develop applications with image loading capabilities. Control of
images is left to the developer, so unnecessary conversions, etc. are
not performed. DevIL can load, save, convert, manipulate, filter and
display a wide variety of image formats.

Currently, DevIL can load .bmp, .cut, .dds, .doom, .gif, .ico, .jpg,
.lbm, .mdl, .mng, .pal, .pbm, .pcd, .pcx, .pgm, .pic, .png, .ppm,
.psd, .psp, .raw, .sgi, .tga and .tif .hdr files.
Formats supported for saving include .bmp, .dds, .h, .jpg, .pal,
.pbm, .pcx, .hdr, .pgm,.png, .ppm, .raw, .sgi, .tga and .tif.

DevIL currently supports the following APIs for display: OpenGL,
SDL and Allegro.

%package tools
Summary:        Tools that can be used when using DevIL libraries
License:        GPL-3.0-or-later AND LGPL-2.1-only
Group:          Development/Tools/Other
Requires:       libIL%{libIL} = %{version}

%description tools
Tools that can be used to work with DevIL libraries and convert various
formats.

%package -n libIL%{libIL}
Summary:        A cross-platform image library
License:        LGPL-2.1-only
Group:          System/Libraries
Provides:       libdevil1 = %{version}
Obsoletes:      libdevil1 < %{version}
%if 0%{?suse_version}
Requires(post): %{install_info_prereq}
Requires(preun):%{install_info_prereq}
%endif

%description -n  libIL%{libIL}
Developer's Image Library (DevIL) is a programmer's library to
develop applications with image loading capabilities. Control of
images is left to the developer, so unnecessary conversions, etc. are
not performed. DevIL can load, save, convert, manipulate, filter and
display a wide variety of image formats.

Currently, DevIL can load .bmp, .cut, .dds, .doom, .gif, .ico, .jpg,
.lbm, .mdl, .mng, .pal, .pbm, .pcd, .pcx, .pgm, .pic, .png, .ppm,
.psd, .psp, .raw, .sgi, .tga and .tif .hdr files.
Formats supported for saving include .bmp, .dds, .h, .jpg, .pal,
.pbm, .pcx, .hdr, .pgm,.png, .ppm, .raw, .sgi, .tga and .tif.

DevIL currently supports the following APIs for display: OpenGL,
SDL and Allegro.

%package -n DevIL-devel
Summary:        Header files for Developers Image Library
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
Requires:       libIL%{libIL} = %{version}
Provides:       libdevil-devel = %{version}
Obsoletes:      libdevil-devel < %{version}

%description -n DevIL-devel
Developer's Image Library (DevIL) is a programmer's library to develop
applications with image loading capabilities.

This package contains the development libraries and headers.

%prep
%setup -q -n devil-%{version}
%patch0
%patch1
%patch2 -p1
%patch3 -p1
%patch4 -p2
%patch5 -p1
# FIXME: src-IL/src/il_wdp.c unclear license: https://jxrlib.codeplex.com can stand as replacement
# make sure we don't compile this accidentally
> src-IL/src/il_wdp.c

%build
%configure \
	--disable-static \
	--enable-shared \
	--enable-ILUT \
	--enable-ILU \
	--disable-wdp \
	--disable-lcms \
	--disable-sse3
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%preun -n libIL%{libIL}
%install_info_delete --info-dir=%{_infodir} %{_infodir}/DevIL_manual.info.gz

%post -n libIL%{libIL}
/sbin/ldconfig
%install_info --info-dir=%{_infodir} %{_infodir}/DevIL_manual.info.gz

%postun -n libIL%{libIL} -p /sbin/ldconfig

%files -n libIL%{libIL}
%{_libdir}/lib*.so.*
%license COPYING
%doc AUTHORS CREDITS NEWS README README.unix TODO
%{_infodir}/DevIL_manual.info%{?ext_info}

%files -n DevIL-devel
%{_libdir}/lib*.so
%{_includedir}/IL
%{_libdir}/pkgconfig/IL*.pc

%files tools
%{_bindir}/ilur

%changelog
