#
# spec file for package libdevil
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


# SONAME Version tags (*.so.$NUM)
%define libIL 1

Summary:        A full featured cross platform image library
License:        LGPL-2.1
Group:          System/Libraries
Name:           libdevil
Version:        1.7.8
Release:        1.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://openil.sourceforge.net/
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
BuildRequires:  Mesa-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  SDL-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  libjasper-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrender)

%description
Developer's Image Library (DevIL) is a programmer's library to develop
applications with very powerful image loading capabilities, yet is easy
for a developer to learn and use. Ultimate control of images is left
to the developer, so unnecessary conversions, etc. are not performed.
DevIL utilizes a simple, yet powerful, syntax. DevIL can load, save,
convert, manipulate, filter and display a wide variety of image formats.

Currently, DevIL can load .bmp, .cut, .dds, .doom, .gif, .ico, .jpg,
.lbm, .mdl, .mng, .pal, .pbm, .pcd, .pcx, .pgm, .pic, .png, .ppm,
.psd, .psp, .raw, .sgi, .tga and .tif .hdr files.
Formats supported for saving include .bmp, .dds, .h, .jpg, .pal,
.pbm, .pcx, .hdr, .pgm,.png, .ppm, .raw, .sgi, .tga and .tif.

DevIL currently supports the following APIs for display: OpenGL,
Windows GDI, SDL, DirectX and Allegro. Compilers that can compile
DevIL or use it include Djgpp, MSVC++, Linux gcc, Delphi, Visual
Basic, Power Basic and Dev-C++.


%package tools
Summary:        Tools that can be used when using DevIL libraries
License:        LGPL-2.1 and GPL-3.0+
Group:          System/Libraries
Requires:       libIL%{libIL} = %{version}

%description tools
Tools that can be used to work with DevIL libraries and convert various
formats.

%package -n libIL%{libIL}
Provides:       libdevil1 = %{version}
Obsoletes:      libdevil1 < %{version}
Summary:        A full featured cross platform image library
License:        LGPL-2.1
Group:          System/Libraries
%if 0%{?suse_version}
Requires(post): %install_info_prereq
Requires(preun): %install_info_prereq
%endif

%description -n  libIL%{libIL}
Developer's Image Library (DevIL) is a programmer's library to develop
applications with very powerful image loading capabilities, yet is easy
for a developer to learn and use. Ultimate control of images is left
to the developer, so unnecessary conversions, etc. are not performed.
DevIL utilizes a simple, yet powerful, syntax. DevIL can load, save,
convert, manipulate, filter and display a wide variety of image formats.

Currently, DevIL can load .bmp, .cut, .dds, .doom, .gif, .ico, .jpg,
.lbm, .mdl, .mng, .pal, .pbm, .pcd, .pcx, .pgm, .pic, .png, .ppm,
.psd, .psp, .raw, .sgi, .tga and .tif .hdr files.
Formats supported for saving include .bmp, .dds, .h, .jpg, .pal,
.pbm, .pcx, .hdr, .pgm,.png, .ppm, .raw, .sgi, .tga and .tif.

DevIL currently supports the following APIs for display: OpenGL,
Windows GDI, SDL, DirectX and Allegro. Compilers that can compile
DevIL or use it include Djgpp, MSVC++, Linux gcc, Delphi, Visual
Basic, Power Basic and Dev-C++.

%package -n DevIL-devel
Summary:        Development package
License:        LGPL-2.1
Group:          Development/Libraries/C and C++
Requires:       libIL%{libIL} = %{version}
Provides:       libdevil-devel = %{version}
Obsoletes:      libdevil-devel < %{version}

%description -n DevIL-devel
Developer's Image Library (DevIL) is a programmer's library to develop
applications with very powerful image loading capabilities, yet is easy
for a developer to learn and use. Ultimate control of images is left
to the developer, so unnecessary conversions, etc. are not performed.
DevIL utilizes a simple, yet powerful, syntax. DevIL can load, save,
convert, manipulate, filter and display a wide variety of image formats.

Currently, DevIL can load .bmp, .cut, .dds, .doom, .gif, .ico, .jpg,
.lbm, .mdl, .mng, .pal, .pbm, .pcd, .pcx, .pgm, .pic, .png, .ppm,
.psd, .psp, .raw, .sgi, .tga and .tif .hdr files.
Formats supported for saving include .bmp, .dds, .h, .jpg, .pal,
.pbm, .pcx, .hdr, .pgm,.png, .ppm, .raw, .sgi, .tga and .tif.

DevIL currently supports the following APIs for display: OpenGL,
Windows GDI, SDL, DirectX and Allegro. Compilers that can compile
DevIL or use it include Djgpp, MSVC++, Linux gcc, Delphi, Visual
Basic, Power Basic and Dev-C++.

This package contains the development libraries and headers.

%prep
%setup -q -n devil-%{version}
%patch0
%patch1
%patch2 -p1
%patch3 -p1
%patch4 -p2
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
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la

%preun -n libIL%{libIL}
%install_info_delete --info-dir=%{_infodir} %{_infodir}/DevIL_manual.info.gz

%post -n libIL%{libIL}
/sbin/ldconfig
%install_info --info-dir=%{_infodir} %{_infodir}/DevIL_manual.info.gz

%postun -n libIL%{libIL} -p /sbin/ldconfig

%files -n libIL%{libIL}
%defattr(-,root,root)
%{_libdir}/lib*.so.*
%doc AUTHORS COPYING CREDITS NEWS README README.unix TODO
%{_infodir}/DevIL_manual.info.*

%files -n DevIL-devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_includedir}/IL
%{_libdir}/pkgconfig/IL*.pc

%files tools
%defattr(-,root,root)
%{_bindir}/ilur

%changelog
