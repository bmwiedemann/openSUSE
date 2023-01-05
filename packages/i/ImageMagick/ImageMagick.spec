#
# spec file for package ImageMagick
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


%define debug_build    0
%define asan_build     0
%define maj            7
%define mfr_version    %{maj}.1.0
%define mfr_revision   57
%define quantum_depth  16
%define source_version %{mfr_version}-%{mfr_revision}
%define clibver        10
%define cwandver       10
%define cxxlibver      5
%define libspec        -%{maj}_Q%{quantum_depth}HDRI
%define config_dir     ImageMagick-7
%define config_spec    config-7
# bsc#1088463
%define urw_base35_fonts 0

Name:           ImageMagick
Version:        %{mfr_version}.%{mfr_revision}
Release:        0
Summary:        Viewer and Converter for Images
License:        ImageMagick
Group:          Productivity/Graphics/Other
URL:            https://imagemagick.org/
Source0:        https://imagemagick.org/archive/releases/ImageMagick-%{mfr_version}-%{mfr_revision}.tar.xz
Source1:        baselibs.conf
Source2:        https://imagemagick.org/archive/releases/ImageMagick-%{mfr_version}-%{mfr_revision}.tar.xz.asc
Source3:        ImageMagick.keyring
# suse specific patches
Patch0:         ImageMagick-configuration-SUSE.patch
Patch2:         ImageMagick-library-installable-in-parallel.patch
#%%ifarch i586
#%%if %%{?suse_version} < 1550
# do not report test issues related to 32-bit architectures upstream,
# they do not want to dedicate any time to fix them:
# https://github.com/ImageMagick/ImageMagick/issues/1215
Patch4:         ImageMagick-filter.t-disable-Contrast.patch
#%%endif
#%%endif
BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  libwmf-devel
BuildRequires:  xdg-utils
BuildRequires:  xz-devel
BuildRequires:  zip
%if 0%{?suse_version} >= 1315
BuildRequires:  dejavu-fonts
%endif
%if 0%{?suse_version} >= 1315
BuildRequires:  libjbig-devel
%endif
%if 0%{?suse_version} >= 1315
%if 0%{?suse_version} > 1500
BuildRequires:  p7zip-full
%else
BuildRequires:  p7zip
%endif
BuildRequires:  pkgconfig
%endif
%if 0%{?suse_version} >= 1315
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libtiff-4) >= 4.0.3
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpmux)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
%if 0%{?suse_version} > 1315
BuildRequires:  pkgconfig(ijs)
# bsc#1088463
%if %{urw_base35_fonts}
BuildRequires:  urw-base35-fonts
%else
BuildRequires:  ghostscript-fonts-other
BuildRequires:  ghostscript-fonts-std
%endif
%else
BuildRequires:  ghostscript-fonts-other
BuildRequires:  ghostscript-fonts-std
BuildRequires:  ghostscript-library
%endif
%if 0%{?suse_version} > 1315
BuildRequires:  pkgconfig(libopenjp2) >= 2.1.0
%endif
%if 0%{?suse_version} > 1315
BuildRequires:  pkgconfig(lqr-1)
%endif
%else
BuildRequires:  OpenEXR-devel
BuildRequires:  fftw3-devel
BuildRequires:  freetype2-devel
BuildRequires:  ghostscript-fonts-other
BuildRequires:  ghostscript-fonts-std
BuildRequires:  ghostscript-library
BuildRequires:  libbz2-devel
BuildRequires:  libdjvulibre-devel
BuildRequires:  libexif-devel
BuildRequires:  libheif-devel
BuildRequires:  librsvg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml-devel
BuildRequires:  perl-parent
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(zlib)
%endif

%package -n perl-PerlMagick
Summary:        Perl interface for ImageMagick
Group:          Development/Libraries/Perl
Requires:       ImageMagick = %{version}
Requires:       libMagickCore%{libspec}%{clibver} = %{version}
Requires:       perl = %{perl_version}

%package devel
Summary:        Development files for ImageMagick's C interface
Group:          Development/Libraries/C and C++
Requires:       ImageMagick = %{version}
Requires:       glibc-devel
Requires:       libMagickCore%{libspec}%{clibver} = %{version}
Requires:       libMagickWand%{libspec}%{cwandver} = %{version}
# bnc#741947:
%if 0%{?suse_version} >= 1315
Requires:       pkgconfig(bzip2)
%else
Requires:       libbz2-devel
%endif

%if !%{debug_build}
%package extra
Summary:        Extra codecs for the ImageMagick image viewer/converter
Group:          Productivity/Graphics/Other
Requires:       ImageMagick = %{version}
Requires:       libMagickCore%{libspec}%{clibver} = %{version}
Recommends:     autotrace
Recommends:     dcraw
Recommends:     hp2xx
Recommends:     libwmf
Recommends:     netpbm
Recommends:     transfig
%endif

%package -n libMagickCore%{libspec}%{clibver}
Summary:        C runtime library for ImageMagick
Group:          Productivity/Graphics/Other
Recommends:     ghostscript
Suggests:       %{name}-extra = %{version}
Requires:       imagick-%{config_spec}
Recommends:     %{config_spec}-SUSE

%package -n libMagickWand%{libspec}%{cwandver}
Summary:        C runtime library for ImageMagick
Group:          Productivity/Graphics/Other

%package -n libMagick++%{libspec}%{cxxlibver}
Summary:        C++ interface runtime library for ImageMagick
Group:          Development/Libraries/C and C++
Requires:       %{name}

%package -n libMagick++-devel
Summary:        Development files for ImageMagick's C++ interface
Group:          Development/Libraries/C and C++
Requires:       libMagick++%{libspec}%{cxxlibver} = %{version}
Requires:       libstdc++-devel
%if 0%{?suse_version} >= 1315
Requires:       pkgconfig(ImageMagick) = %{mfr_version}
%else
Requires:       %{name}-devel = %{version}
%endif

%package doc
Summary:        Document Files for ImageMagick Library
Group:          Documentation/HTML
%if 0%{?suse_version} >= 1315
BuildArch:      noarch
%endif

%package %{config_spec}-upstream
Summary:        Upstream Configuration Files
Group:          Development/Libraries/C and C++
Provides:       imagick-%{config_spec}
Requires(post): update-alternatives
Requires(postun):update-alternatives

%package %{config_spec}-SUSE
Summary:        Upstream Configuration Files
Group:          Development/Libraries/C and C++
Provides:       imagick-%{config_spec}
Requires(post): update-alternatives
Requires(postun):update-alternatives

%description
ImageMagick is a robust collection of tools and libraries to read,
write, and manipulate an image in many image formats, including popular
formats like TIFF, JPEG, PNG, PDF, PhotoCD, and GIF. With ImageMagick,
you can create images dynamically, making it suitable for Web
applications. You can also resize, rotate, sharpen, color-reduce, or
add special effects to an image and save your completed work in many
different image formats. Image processing operations are available from
the command line as well as through C, C++, and Perl-based programming
interfaces.

%description devel
ImageMagick is a robust collection of tools and libraries to read,
write, and manipulate an image in many image formats, including popular
formats like TIFF, JPEG, PNG, PDF, PhotoCD, and GIF. With ImageMagick,
you can create images dynamically, making it suitable for Web
applications. You can also resize, rotate, sharpen, color-reduce, or
add special effects to an image and save your completed work in many
different image formats. Image processing operations are available from
the command line as well as through C, C++, and Perl-based programming
interfaces.

%if !%{debug_build}
%description extra
This package adds support for djvu, wmf and jpeg2000 formats and
installs optional helper applications.

ImageMagick is a robust collection of tools and libraries to read,
write, and manipulate an image in many image formats, including popular
formats like TIFF, JPEG, PNG, PDF, PhotoCD, and GIF. With ImageMagick,
you can create images dynamically, making it suitable for Web
applications. You can also resize, rotate, sharpen, color-reduce, or
add special effects to an image and save your completed work in many
different image formats. Image processing operations are available from
the command line as well as through C, C++, and Perl-based programming
interfaces.
%endif

%description -n libMagickCore%{libspec}%{clibver}
ImageMagick is a robust collection of tools and libraries to read,
write, and manipulate an image in many image formats, including popular
formats like TIFF, JPEG, PNG, PDF, PhotoCD, and GIF. With ImageMagick,
you can create images dynamically, making it suitable for Web
applications. You can also resize, rotate, sharpen, color-reduce, or
add special effects to an image and save your completed work in many
different image formats. Image processing operations are available from
the command line as well as through C, C++, and Perl-based programming
interfaces.

%description -n libMagickWand%{libspec}%{cwandver}
ImageMagick is a robust collection of tools and libraries to read,
write, and manipulate an image in many image formats, including popular
formats like TIFF, JPEG, PNG, PDF, PhotoCD, and GIF. With ImageMagick,
you can create images dynamically, making it suitable for Web
applications. You can also resize, rotate, sharpen, color-reduce, or
add special effects to an image and save your completed work in many
different image formats. Image processing operations are available from
the command line as well as through C, C++, and Perl-based programming
interfaces.

%description -n perl-PerlMagick
PerlMagick is an objected-oriented Perl interface to ImageMagick. Use
the module to read, manipulate, or write an image or image sequence
from within a Perl script. This makes it suitable for Web CGI scripts.

%description -n libMagick++%{libspec}%{cxxlibver}
This is Magick++, the object-oriented C++ API for the ImageMagick
image-processing library.

Magick++ supports an object model inspired by PerlMagick. Magick++
should be faster than PerlMagick since it is written in a compiled
language which is not parsed at run-time. This makes it suitable for
Web CGI programs. Images support implicit reference counting so that
copy constructors and assignment incur almost no cost. The cost of
actually copying an image (if necessary) is done just before
modification and this copy is managed automatically by Magick++.
De-referenced copies are automatically deleted. The image objects
support value (rather than pointer) semantics so it is trivial to
support multiple generations of an image in memory at one time.

%description -n libMagick++-devel
This is Magick++, the object-oriented C++ API for the ImageMagick
image-processing library.

Magick++ supports an object model inspired by PerlMagick. Magick++
should be faster than PerlMagick since it is written in a compiled
language which is not parsed at run-time. This makes it suitable for
Web CGI programs. Images support implicit reference counting so that
copy constructors and assignment incur almost no cost. The cost of
actually copying an image (if necessary) is done just before
modification and this copy is managed automatically by Magick++.
De-referenced copies are automatically deleted. The image objects
support value (rather than pointer) semantics so it is trivial to
support multiple generations of an image in memory at one time.

%description doc
HTML documentation for ImageMagick library and scene examples.

%description %{config_spec}-upstream
ImageMagick configuration as supplied by upstream. It does not
provide any security restrictions. ImageMagick will be vulnerable
for example by ImageTragick or PS/PDF coder issues. It should
be used in trusted environment. Version or maintenance updates
will not overwrite user changes in system configuration.

%description %{config_spec}-SUSE
ImageMagick configuration as provide by SUSE. It is more security
aware than config-upstream variant. It does disable some coders,
that are insecure by design to prevent user to use them
inadvertently. Configuration can be subject of change by future
version and maintenance updates and system changes will not be
preserved.

%prep
%setup -q -n ImageMagick-%{source_version}
%patch2 -p1
%ifarch i586
%if %{?suse_version} < 1550
%patch4 -p1
%endif
%endif

%build
# bsc#1088463
%if %{urw_base35_fonts}
sed -i 's:type1:otf:'      config/type-urw-base35.xml.in
sed -i 's:metrics=[^ ]*::' config/type-urw-base35.xml.in
sed -i 's:\.t1:.otf:'      config/type-urw-base35.xml.in
%endif
# make library binary package parallel installable
export MODULES_DIRNAME="modules%{libspec}%{clibver}"
export SHAREARCH_DIRNAME="config%{libspec}%{clibver}"
%if %{debug_build}
export CFLAGS="%{optflags} -O0"
export CXXFLAGS="%{optflags} -O0"
%endif
%configure \
  --disable-silent-rules \
  --enable-shared \
  --without-frozenpaths \
  --with-magick_plus_plus \
%if !%{debug_build}
  --with-modules \
%else
  --without-modules \
%endif
  --with-threads \
%if %{urw_base35_fonts}
  --with-urw-base35-font-dir=/usr/share/fonts/truetype \
%else
  --with-gs-font-dir=/usr/share/fonts/ghostscript \
%endif
  --with-perl \
  --with-perl-options="INSTALLDIRS=vendor %{?perl_prefix} CC='gcc -L$PWD/magick/.libs' LDDLFLAGS='-shared -L$PWD/magick/.libs'" \
  --disable-static \
  --with-gvc \
  --with-djvu \
  --with-fftw \
  --with-lcms \
  --with-jbig \
%if 0%{?suse_version} > 1315
  --with-openjp2 \
%endif
  --with-openexr \
  --with-rsvg \
  --with-webp \
  --with-wmf \
  --with-quantum-depth=%{quantum_depth} \
  --without-gcc-arch \
  --enable-pipes=no \
  --enable-reproducible-build=yes \
  --disable-openmp
%if %{asan_build}
sed -i -e 's/\(^CFLAGS.*\)/\1 -fsanitize=address/' \
       -e 's/\(^LIBS =.*\)/\1 -lasan/' \
       Makefile
%endif
# don't build together, PerlMagick could be miscompiled when using parallel build[1]
# [1] http://pkgs.fedoraproject.org/cgit/ImageMagick.git/tree/ImageMagick.spec
make %{?_smp_mflags} all
make -j1 perl-build
# mostly because */demo is used later with %check
# polutting dir with .libs etc.
cp -r Magick++/demo Magick++/examples
cp -r PerlMagick/demo PerlMagick/examples
# other improvements
chmod -x PerlMagick/demo/*.pl

%check
exit 0
%if %{debug_build} || %{asan_build}
# testsuite does not succeed for some reason
# research TODO
exit 0
%endif
%ifarch i586
# do not report test issues related to 32-bit architectures upstream,
# they do not want to dedicate any time to fix them:
# https://github.com/ImageMagick/ImageMagick/issues/1215
rm PerlMagick/t/montage.t
sed -i -e 's:averageImages ::' -e 's:1..13:1..12:' Magick++/tests/tests.tap
%endif
make %{?_smp_mflags} check
export MAGICK_CODER_MODULE_PATH=$PWD/coders/.libs
export MAGICK_CODER_FILTER_PATH=$PWD/filters/.libs
export MAGICK_CONFIGURE_PATH=$PWD/config
cd PerlMagick
%if 0%{?suse_version} >= 1315
make %{?_smp_mflags} test
%else
make test_dynamic
%endif
cd ..

%install
%if 0%{?suse_version} >= 1315
%make_install pkgdocdir=%{_defaultdocdir}/%{name}-%{maj}/
%else
make install \
     DESTDIR=%{buildroot} \
     pkgdocdir=%{_defaultdocdir}/%{name}-%{maj}/
%endif
# configuration magic
mv -t %{buildroot}%{_sysconfdir}/%{name}* %{buildroot}%{_datadir}/%{name}*/*.xml
mv %{buildroot}%{_sysconfdir}/%{config_dir}{,-upstream}
cp -r %{buildroot}%{_sysconfdir}/%{config_dir}{-upstream,-SUSE}
patch --fuzz=0 --dir %{buildroot}%{_sysconfdir}/%{config_dir}-SUSE < %{PATCH0}
mkdir -p  %{buildroot}%{_sysconfdir}/alternatives/
ln -sf %{_sysconfdir}/alternatives/%{config_dir} %{buildroot}%{_sysconfdir}/%{config_dir}
# symlink header file relative to /usr/include/ImageMagick-7/
# so that inclusions like wand/*.h and magick/*.h work
ln -s ./MagickCore %{buildroot}%{_includedir}/%{name}-%{maj}/magick
ln -s ./MagickWand %{buildroot}%{_includedir}/%{name}-%{maj}/wand
# these will be included via %doc
rm -r %{buildroot}%{_datadir}/doc/%{name}-%{maj}/
rm %{buildroot}%{_libdir}/*.la
# remove RPATH from perl module
perl_module=$(find %{buildroot}%{_prefix}/lib/perl5 -name '*.so')
chmod 755 $perl_module
chrpath -d $perl_module
chmod 555 $perl_module
# remove %%{buildroot} from distributed file
sed -i 's:%{buildroot}::' %{buildroot}/%{_libdir}/ImageMagick-%{mfr_version}/config%{libspec}%{clibver}/configure.xml
#remove duplicates
%fdupes -s %{buildroot}%{_defaultdocdir}/%{name}-%{maj}
%fdupes -s %{buildroot}%{_includedir}/%{name}-%{maj}
%fdupes -s %{buildroot}%{_libdir}/pkgconfig
%perl_process_packlist

%post -n libMagickCore%{libspec}%{clibver} -p /sbin/ldconfig
%postun -n libMagickCore%{libspec}%{clibver} -p /sbin/ldconfig
%post -n libMagickWand%{libspec}%{cwandver} -p /sbin/ldconfig
%postun -n libMagickWand%{libspec}%{cwandver} -p /sbin/ldconfig
%post -n libMagick++%{libspec}%{cxxlibver} -p /sbin/ldconfig
%postun -n libMagick++%{libspec}%{cxxlibver} -p /sbin/ldconfig

%pretrans %{config_spec}-upstream -p <lua>
-- this %pretrans to be removed soon [bug#1122033#c37]
path = "%{_sysconfdir}/%{config_dir}"
st = posix.stat(path)
if st and st.type == "directory" then
  os.remove(path .. ".rpmmoved")
  os.rename(path, path .. ".rpmmoved")
end

%post %{config_spec}-upstream
%{_sbindir}/update-alternatives --quiet --install %{_sysconfdir}/%{config_dir}  %{config_dir}   %{_sysconfdir}/%{config_dir}-upstream  1

%postun %{config_spec}-upstream
if [ ! -d %{_sysconfdir}/%{config_dir}-upstream ] ; then
    %{_sbindir}/update-alternatives --quiet --remove %{config_dir}  %{_sysconfdir}/%{config_dir}-upstream
fi

%pretrans %{config_spec}-SUSE -p <lua>
-- this %pretrans to be removed soon [bug#1122033#c37]
path = "%{_sysconfdir}/%{config_dir}"
st = posix.stat(path)
if st and st.type == "directory" then
  os.remove(path .. ".rpmmoved")
  os.rename(path, path .. ".rpmmoved")
end

%post %{config_spec}-SUSE
%{_sbindir}/update-alternatives --quiet --install %{_sysconfdir}/%{config_dir}  %{config_dir}   %{_sysconfdir}/%{config_dir}-SUSE      10

%postun %{config_spec}-SUSE
if [ ! -d %{_sysconfdir}/%{config_dir}-SUSE ] ; then
    %{_sbindir}/update-alternatives --quiet --remove %{config_dir}  %{_sysconfdir}/%{config_dir}-SUSE
fi

%files
%license LICENSE
%doc NEWS.txt
%{_bindir}/[^MW]*
%{_mandir}/man1/*
%exclude %{_mandir}/man1/*-config.1%{ext_man}

%files -n libMagickCore%{libspec}%{clibver}
%license LICENSE
%{_libdir}/libMagickCore*.so.%{clibver}*
%dir %{_libdir}/ImageMagick*
%if !%{debug_build}
%dir %{_libdir}/ImageMagick*/modules*
%dir %{_libdir}/ImageMagick*/modules*/*
%exclude %{_libdir}/ImageMagick*/modules*/*/wmf.*
%if 0%{?suse_version} > 1315
%exclude %{_libdir}/ImageMagick*/modules*/*/jp2.*
%endif
%exclude %{_libdir}/ImageMagick*/modules*/*/djvu.*
%{_libdir}/ImageMagick*/modules*/*/*.so
# don't remove la files, see bnc#579798
%{_libdir}/ImageMagick*/modules*/*/*.la
%endif
%{_libdir}/ImageMagick*/config*

%files -n libMagickWand%{libspec}%{cwandver}
%{_libdir}/libMagickWand*.so.%{cwandver}*

%if !%{debug_build}
%files extra
%{_libdir}/ImageMagick*/modules*/*/wmf.so
# don't remove la files, see bnc#579798
%if 0%{?suse_version} > 1315
%{_libdir}/ImageMagick*/modules*/*/jp2.so
%{_libdir}/ImageMagick*/modules*/*/jp2.la
%endif
%{_libdir}/ImageMagick*/modules*/*/djvu.so
%{_libdir}/ImageMagick*/modules*/*/djvu.la
%endif

%files devel
%{_libdir}/libMagickCore*.so
%{_libdir}/libMagickWand*.so
%dir %{_includedir}/ImageMagick*
%{_includedir}/ImageMagick*/MagickCore
%{_includedir}/ImageMagick*/MagickWand
%{_includedir}/ImageMagick*/magick
%{_includedir}/ImageMagick*/wand
%{_bindir}/MagickCore-config
%{_bindir}/MagickWand-config
%{_libdir}/pkgconfig/MagickCore*.pc
%{_libdir}/pkgconfig/ImageMagick*.pc
%{_libdir}/pkgconfig/MagickWand*.pc
%{_mandir}/man1/*-config.1%{ext_man}
%exclude %{_mandir}/man1/Magick++-config.1%{ext_man}

%files -n perl-PerlMagick
%doc PerlMagick/README.txt
%doc PerlMagick/examples
%{_mandir}/man3/*
%{perl_vendorarch}/auto/Image
%{perl_vendorarch}/Image

%files -n libMagick++%{libspec}%{cxxlibver}
%{_libdir}/libMagick++*.so.%{cxxlibver}*

%files -n libMagick++-devel
%doc Magick++/examples
%doc Magick++/NEWS Magick++/README Magick++/AUTHORS
%{_libdir}/libMagick++*.so
%{_includedir}/ImageMagick*/Magick++.h
%{_includedir}/ImageMagick*/Magick++
%{_bindir}/Magick++-config
%{_libdir}/pkgconfig/Magick++*.pc
%{_mandir}/man1/Magick++-config.1%{ext_man}

%files doc
%{_defaultdocdir}/%{name}-%{maj}

%files %{config_spec}-upstream
%dir %{_sysconfdir}/ImageMagick*-upstream/
%config(noreplace) %{_sysconfdir}/ImageMagick*-upstream/*
%{_sysconfdir}/%{config_dir}
%ghost %{_sysconfdir}/alternatives/%{config_dir}

%files %{config_spec}-SUSE
%dir %{_sysconfdir}/ImageMagick*-SUSE/
%config %{_sysconfdir}/ImageMagick*-SUSE/*
%{_sysconfdir}/%{config_dir}
%ghost %{_sysconfdir}/alternatives/%{config_dir}

%changelog
