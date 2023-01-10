#
# spec file for package GraphicsMagick
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


%define asan_build    0
%define debug_build   0

%define quant 16
%define base_version 1.3
%define so_ver          3
%define pp_so_ver       12
%define wand_so_ver     2
Name:           GraphicsMagick
Version:        1.3.39
Release:        0
Summary:        Viewer and Converter for Images
License:        MIT
Group:          Productivity/Graphics/Convertors
URL:            http://www.GraphicsMagick.org/
Source:         https://downloads.sourceforge.net/project/graphicsmagick/graphicsmagick/%{version}/%{name}-%{version}.tar.xz
Patch0:         GraphicsMagick-perl-linkage.patch
Patch1:         GraphicsMagick-disable-insecure-coders.patch
BuildRequires:  cups-client
BuildRequires:  dcraw
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  ghostscript-fonts-std
%if 0%{?suse_version} >= 1315
BuildRequires:  libjbig-devel
BuildRequires:  libltdl-devel
%endif
BuildRequires:  libwmf-devel
%if 0%{?suse_version} >= 1315
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpmux)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(zlib)
%else
BuildRequires:  freetype2-devel
BuildRequires:  libbz2-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%endif
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(libjxl)
%endif

%description
GraphicsMagick provides an image manipulation and translation
utility. It is capable of displaying still images and animations
using the X Window system which provides an interface for
interactively editing images, and is capable of importing selected
windows or the entire desktop. It can read and write over 88 image
formats, including JPEG, TIFF, WMF, SVG, PNG, PNM, GIF, andPhoto CD.
It also allows to resize, rotate, sharpen, color reduce, or add
special effects to an image and to save the result to any supported
format. GraphicsMagick may be used to create animated or transparent
.gifs, to composite images, and to create thumbnail images.

This package is compiled with Q%{quant}, which means that it provides better
performance on %{quant} bit images and less.

%package     -n libGraphicsMagick-Q%{quant}-%{so_ver}
Summary:        The GraphicsMagick image conversion runtime library
Group:          System/Libraries
Requires:       libGraphicsMagick3-config = %{version}

%description -n libGraphicsMagick-Q%{quant}-%{so_ver}
GraphicsMagick provides an image manipulation and translation utility
and library. It can read and write over 88 image formats, including
JPEG, TIFF, WMF, SVG, PNG, PNM, GIF, andPhoto CD. It also allows to
resize, rotate, sharpen, color reduce, or add special effects to an
image and to save the result to any supported format. GraphicsMagick
may be used to create animated or transparent .gifs, to composite
images, and to create thumbnail images.

This package is compiled with Q%{quant}, that means it provides better
performance on %{quant} and less bit images.

%package     -n libGraphicsMagick%{so_ver}-config
Summary:        Configuration for the GraphicsMagick image conversion library
Group:          System/Libraries

%description -n libGraphicsMagick%{so_ver}-config
GraphicsMagick provides an image manipulation and translation utility
and library. It can read and write over 88 image formats, including
JPEG, TIFF, WMF, SVG, PNG, PNM, GIF, andPhoto CD. It also allows to
resize, rotate, sharpen, color reduce, or add special effects to an
image and to save the result to any supported format. GraphicsMagick
may be used to create animated or transparent .gifs, to composite
images, and to create thumbnail images.

This package contains GraphicsMagick library configuration files.

%package     -n libGraphicsMagickWand-Q%{quant}-%{wand_so_ver}
Summary:        Runtime library for the GraphicsMagick image conversion library
Group:          System/Libraries

%description -n libGraphicsMagickWand-Q%{quant}-%{wand_so_ver}
GraphicsMagick provides an image manipulation and translation utility
and library. It can read and write over 88 image formats, including
JPEG, TIFF, WMF, SVG, PNG, PNM, GIF, andPhoto CD. It also allows to
resize, rotate, sharpen, color reduce, or add special effects to an
image and to save the result to any supported format. GraphicsMagick
may be used to create animated or transparent .gifs, to composite
images, and to create thumbnail images.

This package is compiled with Q%{quant}, that means it provides better
performance on %{quant} and less bit images.

%package        devel
Summary:        Development files for the GraphicsMagick C language API
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libGraphicsMagick-Q%{quant}-%{so_ver} = %{version}
Requires:       libGraphicsMagickWand-Q%{quant}-%{wand_so_ver} = %{version}

%description    devel
GraphicsMagick provides an image manipulation and translation utility
and library. It can read and write over 88 image formats, including
JPEG, TIFF, WMF, SVG, PNG, PNM, GIF, andPhoto CD. It also allows to
resize, rotate, sharpen, color reduce, or add special effects to an
image and to save the result to any supported format. GraphicsMagick
may be used to create animated or transparent .gifs, to composite
images, and to create thumbnail images.

%package     -n perl-GraphicsMagick
Summary:        Perl interface for the GraphicsMagick image conversion library
Group:          Development/Languages/Perl
Requires:       %{name} = %{version}
Requires:       perl = %{perl_version}

%description -n perl-GraphicsMagick
GraphicsMagick provides an image manipulation and translation utility
and library. It can read and write over 88 image formats, including
JPEG, TIFF, WMF, SVG, PNG, PNM, GIF, andPhoto CD. It also allows to
resize, rotate, sharpen, color reduce, or add special effects to an
image and to save the result to any supported format. GraphicsMagick
may be used to create animated or transparent .gifs, to composite
images, and to create thumbnail images.

This package contains perl interface to GraphicsMagick library.

%package     -n libGraphicsMagick++-Q%{quant}-%{pp_so_ver}
Summary:        C++ interface for the GraphisMagick image conversion library
Group:          System/Libraries

%description -n libGraphicsMagick++-Q%{quant}-%{pp_so_ver}
GraphicsMagick provides an image manipulation and translation utility
and library. It can read and write over 88 image formats, including
JPEG, TIFF, WMF, SVG, PNG, PNM, GIF, andPhoto CD. It also allows to
resize, rotate, sharpen, color reduce, or add special effects to an
image and to save the result to any supported format. GraphicsMagick
may be used to create animated or transparent .gifs, to composite
images, and to create thumbnail images.

This subpackage contains C++ interface to GraphicsMagick library.

%package     -n libGraphicsMagick++-devel
Summary:        Development files for the GraphicsMagick C++ language API
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       c++_compiler
Requires:       libGraphicsMagick++-Q%{quant}-%{pp_so_ver} = %{version}
Provides:       GraphicsMagick-C++-devel
Obsoletes:      GraphicsMagick-C++-devel <= 1.1.7

%description -n libGraphicsMagick++-devel
GraphicsMagick provides an image manipulation and translation utility
and library. It can read and write over 88 image formats, including
JPEG, TIFF, WMF, SVG, PNG, PNM, GIF, andPhoto CD. It also allows to
resize, rotate, sharpen, color reduce, or add special effects to an
image and to save the result to any supported format. GraphicsMagick
may be used to create animated or transparent .gifs, to composite
images, and to create thumbnail images.

%prep
%setup -q
%autopatch -p1

%build
# This shouldn't be there yet.
rm -f PerlMagick/Makefile.PL
%if !%{debug_build}
export CFLAGS="%{optflags} -fPIE"
%else
export CFLAGS="%{optflags} -O0"
export CXXFLAGS="%{optflags} -O0"
%endif
%configure --enable-shared --disable-static \
%if !%{debug_build}
        --with-modules \
%else
        --without-modules \
%endif
	--with-frozenpaths \
	--without-dps \
	--without-jp2 \
	--without-perl \
	--without-trio \
	--without-zstd \
	--with-magick-plus-plus \
	--with-quantum-depth=%{quant} \
	--enable-quantum-library-names \
	--docdir=%{_defaultdocdir}/%{name} \
	--with-x \
	--x-libraries=%{_libdir} \
	--x-includes=%{_prefix}/include
%if %{asan_build}
sed -i -e 's/\(^CFLAGS.*\)/\1 -fsanitize=address/' \
       -e 's/\(^LIBS =.*\)/\1 -lasan/' \
       Makefile
%endif

# sanity check to prevent ghostscript support from being reenabled
# for reasoning see bsc#1122792
grep -q -- -DHasGS Makefile && GS_ENABLED=1
if [ ! -z "$GS_ENABLED" ]; then
	echo "Refusing to build with ghostscript support (-DHasGS)" 1>&2
	echo "See bsc#1122792 for the security implications" 1>&2
	exit 1
fi

%if !%{debug_build}
make %{?_smp_mflags} LDFLAGS="-pie"
%else
make %{?_smp_mflags}
%endif
cd PerlMagick
perl Makefile.PL
make %{?_smp_mflags} LD_RUN_PATH="%{_libdir}"

%install
%if 0%{?suse_version} >= 1315
%make_install
%else
make install \
     DESTDIR=%{buildroot} \
     pkgdocdir=%{_defaultdocdir}/%{name}-%{maj}/
%endif
rm -f %{buildroot}%{_libdir}/libGraphicsMagick.la
rm -f %{buildroot}%{_libdir}/libGraphicsMagick++.la
rm -f %{buildroot}%{_libdir}/libGraphicsMagickWand.la
cp ChangeLog* *.txt %{buildroot}/%{_defaultdocdir}/%{name}
cd PerlMagick
make DESTDIR=%{buildroot} LD_RUN_PATH="%{_libdir}" install_vendor
%perl_process_packlist
# Remove unpackaged files.
rm -f `find %{buildroot}%{_libdir}/perl*/ -name perllocal.pod -type f`
rm -f `find %{buildroot}%{_libdir}/perl*/ -name .packlist -type f`
# perl modules are in lib even on 64 bit arch
rm -f `find %{buildroot}%{_prefix}/lib/perl*/ -name perllocal.pod -type f`
rm -f `find %{buildroot}%{_prefix}/lib/perl*/ -name .packlist -type f`
rm -f %{buildroot}%{_localstatedir}/adm/perl-modules/GraphicsMagick

%check
%if %{asan_build}
# ASAN needs /proc to be mounted
exit 0
%endif
make %{?_smp_mflags} check
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PWD/magick/.libs:$PWD/wand/.libs
export MAGICK_CODER_MODULE_PATH=$PWD/coders/.libs
export MAGICK_CONFIGURE_PATH=$PWD/config
cd PerlMagick
# bsc#1105592
rm -r t/ps
make test

%post -n libGraphicsMagick-Q%{quant}-%{so_ver} -p /sbin/ldconfig
%postun -n libGraphicsMagick-Q%{quant}-%{so_ver} -p /sbin/ldconfig
%post -n libGraphicsMagickWand-Q%{quant}-%{wand_so_ver} -p /sbin/ldconfig
%postun -n libGraphicsMagickWand-Q%{quant}-%{wand_so_ver} -p /sbin/ldconfig
%post -n libGraphicsMagick++-Q%{quant}-%{pp_so_ver} -p /sbin/ldconfig
%postun -n libGraphicsMagick++-Q%{quant}-%{pp_so_ver} -p /sbin/ldconfig

%files
%if 0%{?suse_version} < 1315
%defattr(-,root,root)
%endif
%docdir %{_defaultdocdir}/%{name}
%{_defaultdocdir}/%{name}
%doc %{_datadir}/%{name}-%{version}
%exclude %{_datadir}/%{name}-%{version}/config
%attr(755, root, root) %{_bindir}/gm
%{_mandir}/man1/gm.1%{ext_man}
%{_mandir}/man4/*%{ext_man}
%{_mandir}/man5/*%{ext_man}

%files -n libGraphicsMagick-Q%{quant}-%{so_ver}
%if 0%{?suse_version} < 1315
%defattr(-,root,root)
%endif
%{_libdir}/lib%{name}-Q%{quant}.so.*
%dir %{_libdir}/%{name}-%{version}
%if !%{debug_build}
%dir %{_libdir}/%{name}-%{version}/modules-Q%{quant}
%dir %{_libdir}/%{name}-%{version}/modules-Q%{quant}/coders
%dir %{_libdir}/%{name}-%{version}/modules-Q%{quant}/filters
%{_libdir}/%{name}-%{version}/modules-Q%{quant}/*/*.so
%{_libdir}/%{name}-%{version}/modules-Q%{quant}/*/*.la
%endif

%files -n libGraphicsMagick%{so_ver}-config
%if 0%{?suse_version} < 1315
%defattr(-,root,root)
%endif
%dir %{_libdir}/%{name}-%{version}/config
%{_libdir}/%{name}-%{version}/config/*.mgk
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/config

%files -n libGraphicsMagickWand-Q%{quant}-%{wand_so_ver}
%if 0%{?suse_version} < 1315
%defattr(-,root,root)
%endif
%{_libdir}/lib%{name}Wand-Q%{quant}.so.*

%files devel
%if 0%{?suse_version} < 1315
%defattr(-,root,root)
%endif
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}/wand
%{_includedir}/%{name}/wand/*
%dir %{_includedir}/%{name}/magick
%{_includedir}/%{name}/magick/*
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}Wand.so
%if !%{debug_build}
%dir %{_libdir}/%{name}-%{version}/modules-Q%{quant}
%endif
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}Wand.pc
%attr(755, root, root) %{_bindir}/%{name}-config
%attr(755, root, root) %{_bindir}/%{name}Wand-config
%{_mandir}/man1/%{name}-config.1%{ext_man}
%{_mandir}/man1/%{name}Wand-config.1%{ext_man}

%files -n perl-GraphicsMagick
%dir %{perl_vendorarch}/Graphics
%dir %{perl_vendorarch}/auto/Graphics
%dir %{perl_vendorarch}/auto/Graphics/Magick
%{perl_vendorarch}/Graphics/Magick.pm
%{perl_vendorarch}/auto/Graphics/Magick/*
%{_mandir}/man3/*%{ext_man}

%files -n libGraphicsMagick++-Q%{quant}-%{pp_so_ver}
%if 0%{?suse_version} < 1315
%defattr(-,root,root)
%endif
%{_libdir}/lib%{name}++-Q%{quant}.so.*

%files -n libGraphicsMagick++-devel
%if 0%{?suse_version} < 1315
%defattr(-,root,root)
%endif
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}/Magick++
%{_includedir}/%{name}/Magick++.h
%{_includedir}/%{name}/Magick++/*
%{_libdir}/lib%{name}++.so
%{_libdir}/pkgconfig/%{name}++.pc
%attr(755, root, root) %{_bindir}/%{name}++-config
%{_mandir}/man1/%{name}++-config.1%{ext_man}

%changelog
