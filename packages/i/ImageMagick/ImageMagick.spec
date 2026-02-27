#
# spec file for package ImageMagick
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global flavor          @BUILD_FLAVOR@%{nil}

%define debug_build    0
%define asan_build     0
%define mfr_version    7.1.2
%define mfr_revision   15
%define quantum_depth  16
%define source_version %{mfr_version}-%{mfr_revision}
%define clibver        10
%define cwandver       10
%define cxxlibver      5
%define libspec        -7_Q%{quantum_depth}HDRI
%define config_dir     IM-7
%define test_verbose   1
# bsc#1088463, https://github.com/ImageMagick/ImageMagick/issues/8261
%define urw_base35_fonts 0
# do/don't pull djvulibre dependency
%bcond_without djvu

Name:           ImageMagick
Version:        %{mfr_version}.%{mfr_revision}
Release:        0
Summary:        Viewer and Converter for Images
License:        ImageMagick
Group:          Productivity/Graphics/Other
URL:            https://imagemagick.org/
Source0:        https://imagemagick.org/archive/releases/ImageMagick-%{source_version}.tar.xz
Source1:        baselibs.conf
Source2:        https://imagemagick.org/archive/releases/ImageMagick-%{source_version}.tar.xz.asc
Source3:        ImageMagick.keyring
# do not block read access to own config files
Patch0:         ImageMagick_policy_etc.patch
# SUSE configuration
Patch1:         ImageMagick-configuration-SUSE.patch
# library installation
Patch2:         ImageMagick-library-installable-in-parallel.patch
# disable failing tests
Patch5:         ImageMagick-s390x-disable-tests.patch

BuildRequires:  chrpath
BuildRequires:  dejavu-fonts
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libjbig-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  libwmf-devel
BuildRequires:  pkgconfig
BuildRequires:  xdg-utils
BuildRequires:  xz-devel
BuildRequires:  zip
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(ijs)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libopenjp2) >= 2.1.0
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libtiff-4) >= 4.0.3
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpmux)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lqr-1)
BuildRequires:  pkgconfig(pango)
%if %{with djvu}
BuildRequires:  pkgconfig(ddjvuapi)
%endif
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(libjxl)
%endif
# bsc#1088463
%if %{urw_base35_fonts}
BuildRequires:  urw-base35-fonts
%else
BuildRequires:  ghostscript-fonts-other
BuildRequires:  ghostscript-fonts-std
%endif

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

# BEGIN NIL FLAVOR
%if "%{flavor}" == ""

%package -n perl-PerlMagick
Summary:        Perl interface for ImageMagick
Group:          Development/Libraries/Perl
Requires:       ImageMagick = %{version}
Requires:       libMagickCore%{libspec}%{clibver} = %{version}
Requires:       perl = %{perl_version}

%description -n perl-PerlMagick
PerlMagick is an objected-oriented Perl interface to ImageMagick. Use
the module to read, manipulate, or write an image or image sequence
from within a Perl script. This makes it suitable for Web CGI scripts.

%package devel
Summary:        Development files for ImageMagick's C interface
Group:          Development/Libraries/C and C++
Requires:       ImageMagick = %{version}
Requires:       glibc-devel
Requires:       libMagickCore%{libspec}%{clibver} = %{version}
Requires:       libMagickWand%{libspec}%{cwandver} = %{version}
# bnc#741947:
Requires:       pkgconfig(bzip2)

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

%description extra
This package adds support for djvu, wmf and jpeg2000 formats and
installs optional helper applications.
%endif

%package -n libMagickCore%{libspec}%{clibver}
Summary:        C runtime library for ImageMagick
Group:          Productivity/Graphics/Other
Requires:       imagick-config-7
Recommends:     ImageMagick-config-7-SUSE
Recommends:     ghostscript
Suggests:       ImageMagick-extra = %{version}
Recommends:     ImageMagick

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

%package -n libMagickWand%{libspec}%{cwandver}
Summary:        C runtime library for ImageMagick
Group:          Productivity/Graphics/Other
Recommends:     ImageMagick

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

%package -n libMagick++%{libspec}%{cxxlibver}
Summary:        C++ interface runtime library for ImageMagick
Group:          Development/Libraries/C and C++
Recommends:     ImageMagick

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

%package -n libMagick++-devel
Summary:        Development files for ImageMagick's C++ interface
Group:          Development/Libraries/C and C++
Requires:       libMagick++%{libspec}%{cxxlibver} = %{version}
Requires:       libstdc++-devel
Requires:       pkgconfig(ImageMagick) = %{mfr_version}

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

%package doc
Summary:        Document Files for ImageMagick Library
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
HTML documentation for ImageMagick library and scene examples.

%package config-7-SUSE
Summary:        SUSE Provided Configuration
Group:          Development/Libraries/C and C++
Provides:       imagick-config-7
Conflicts:      imagick-config-7
BuildArch:      noarch

%description config-7-SUSE
ImageMagick configuration as provided by SUSE. It is upstream 'secure'
policy plus disable few other coders for reading and/or writing.

%prep
%setup -q -n ImageMagick-%{source_version}
%patch -P 0 -p1
# default policy (SUSE)
cp config/policy-secure.xml config/policy.xml
%patch -P 1 -p1
%patch -P 2 -p1
%ifarch s390x
%patch -P 5 -p1
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
export CONFIGURE_RELATIVE_PATH=%{config_dir}
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
  --with-urw-base35-font-dir=%{_datadir}/fonts/truetype \
%else
  --with-gs-font-dir=%{_datadir}/fonts/ghostscript \
%endif
  --with-perl \
  --with-perl-options="INSTALLDIRS=vendor INSTALLVENDORARCH=%{perl_vendorarch} INSTALLVENDORMAN3DIR=/usr/share/man/man3" \
  --disable-static \
  --with-gvc \
%if %{with ddjvuapi}
  --with-djvu \
%endif
  --with-fftw \
  --with-lcms \
  --with-jbig \
  --with-openjp2 \
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
%make_build all
%make_build -j1 perl-build
# mostly because */demo is used later with %%check
# polutting dir with .libs etc.
cp -r Magick++/demo Magick++/examples
cp -r PerlMagick/demo PerlMagick/examples
# other improvements
chmod -x PerlMagick/demo/*.pl
exit 0

%check
%ifarch i586
# do not report test issues related to 32-bit architectures upstream,
# they do not want to dedicate any time to fix them:
# https://github.com/ImageMagick/ImageMagick/issues/1215
exit 0
%endif
%if %{debug_build} || %{asan_build}
# testsuite does not succeed for some reason
# research TODO
exit 0
%endif
# ensure we do not block any coder by security policy
cp config/policy-open.xml config/policy.xml
%make_build check
export MAGICK_CODER_MODULE_PATH=$PWD/coders/.libs
export MAGICK_CODER_FILTER_PATH=$PWD/filters/.libs
export MAGICK_CONFIGURE_PATH=$PWD/config
cd PerlMagick
%if %{test_verbose}
sed -i 's:TEST_VERBOSE=0:TEST_VERBOSE=1:' Makefile
%endif
%make_build test
cd ..

%install
%make_install pkgdocdir=%{_defaultdocdir}/ImageMagick-7/
cp config/policy.xml %{buildroot}%{_sysconfdir}/%{config_dir}
# symlink header file relative to /usr/include/ImageMagick-7/
# so that inclusions like wand/*.h and magick/*.h work
ln -s ./MagickCore %{buildroot}%{_includedir}/ImageMagick-7/magick
ln -s ./MagickWand %{buildroot}%{_includedir}/ImageMagick-7/wand
# these will be included via %%doc
rm -r %{buildroot}%{_datadir}/doc/ImageMagick-7/
rm %{buildroot}%{_libdir}/*.la
# remove RPATH from perl module
perl_module=$(find %{buildroot}%{_prefix}/lib/perl5 -name '*.so')
chmod 755 $perl_module
chrpath -d $perl_module
chmod 555 $perl_module
# remove %%{buildroot} from distributed file
sed -i 's:%{buildroot}::' %{buildroot}/%{_libdir}/ImageMagick-%{mfr_version}/config%{libspec}%{clibver}/configure.xml
#remove duplicates
%fdupes -s %{buildroot}%{_defaultdocdir}/ImageMagick-7
%fdupes -s %{buildroot}%{_includedir}/ImageMagick-7
%fdupes -s %{buildroot}%{_libdir}/pkgconfig
%perl_process_packlist

%post -n libMagickCore%{libspec}%{clibver} -p /sbin/ldconfig
%postun -n libMagickCore%{libspec}%{clibver} -p /sbin/ldconfig
%post -n libMagickWand%{libspec}%{cwandver} -p /sbin/ldconfig
%postun -n libMagickWand%{libspec}%{cwandver} -p /sbin/ldconfig
%post -n libMagick++%{libspec}%{cxxlibver} -p /sbin/ldconfig
%postun -n libMagick++%{libspec}%{cxxlibver} -p /sbin/ldconfig

%files
%license LICENSE
%{_bindir}/[^MW]*
%{_mandir}/man1/*
%exclude %{_mandir}/man1/*-config.1%{ext_man}
%{_datadir}/ImageMagick-7
%{_sysconfdir}/%{config_dir}
%exclude %{_sysconfdir}/%{config_dir}/policy.xml

%files -n libMagickCore%{libspec}%{clibver}
%license LICENSE
%{_libdir}/libMagickCore*.so.%{clibver}*
%dir %{_libdir}/ImageMagick*
%if !%{debug_build}
%dir %{_libdir}/ImageMagick*/modules*
%dir %{_libdir}/ImageMagick*/modules*/*
%exclude %{_libdir}/ImageMagick*/modules*/*/wmf.*
%exclude %{_libdir}/ImageMagick*/modules*/*/jp2.*
%if %{with djvu}
%exclude %{_libdir}/ImageMagick*/modules*/*/djvu.*
%endif
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
%{_libdir}/ImageMagick*/modules*/*/jp2.so
%{_libdir}/ImageMagick*/modules*/*/jp2.la
%if %{with djvu}
%{_libdir}/ImageMagick*/modules*/*/djvu.so
%{_libdir}/ImageMagick*/modules*/*/djvu.la
%endif
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
%{_mandir}/man1/*-config.1%{?ext_man}
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
%doc Magick++/AUTHORS
%{_libdir}/libMagick++*.so
%{_includedir}/ImageMagick*/Magick++.h
%{_includedir}/ImageMagick*/Magick++
%{_bindir}/Magick++-config
%{_libdir}/pkgconfig/Magick++*.pc
%{_mandir}/man1/Magick++-config.1%{?ext_man}

%files doc
%{_defaultdocdir}/ImageMagick-7

%files config-7-SUSE
%{_sysconfdir}/%{config_dir}/policy.xml

%endif
# END NIL FLAVOR

%if "%{flavor}" == "config_open"
%package config-7-upstream-open
Summary:        Open ImageMagick Security Policy
Group:          Development/Libraries/C and C++
Provides:       imagick-config-7
Obsoletes:      config-7-upstream < %{version}
Provides:       config-7-upstream = %{version}
Conflicts:      imagick-config-7
BuildArch:      noarch

%description config-7-upstream-open
This policy is designed for usage in secure settings like those
protected by firewalls or within Docker containers. Within this framework,
ImageMagick enjoys broad access to resources and functionalities. This policy
provides convenient and adaptable options for image manipulation. However,
it's important to note that it might present security vulnerabilities in
less regulated conditions. Thus, organizations should thoroughly assess
the appropriateness of the open policy according to their particular use
case and security prerequisites.

%prep
%setup -q -n ImageMagick-%{source_version}

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{config_dir}/
cp config/policy-open.xml %{buildroot}%{_sysconfdir}/%{config_dir}/policy.xml

%files config-7-upstream-open
%dir %{_sysconfdir}/%{config_dir}
%config(noreplace) %{_sysconfdir}/%{config_dir}/policy.xml
%endif

%if "%{flavor}" == "config_limited"
%package config-7-upstream-limited
Summary:        Limited ImageMagick Security Policy
Group:          Development/Libraries/C and C++
Provides:       imagick-config-7
Conflicts:      imagick-config-7
BuildArch:      noarch

%description config-7-upstream-limited
The primary objective of the limited security policy is to find a
middle ground between convenience and security. This policy involves the
deactivation of potentially hazardous functionalities, like specific coders
such as SVG or HTTP. Furthermore, it establishes several constraints on
the utilization of resources like memory, storage, and processing duration,
all of which are adjustable. This policy proves advantageous in situations
where there's a need to mitigate the potential threat of handling possibly
malicious or demanding images, all while retaining essential capabilities
for prevalent image formats.

%prep
%setup -q -n ImageMagick-%{source_version}

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{config_dir}/
cp config/policy-limited.xml %{buildroot}%{_sysconfdir}/%{config_dir}/policy.xml

%files config-7-upstream-limited
%dir %{_sysconfdir}/%{config_dir}
%config(noreplace) %{_sysconfdir}/%{config_dir}/policy.xml
%endif

%if "%{flavor}" == "config_secure"
%package config-7-upstream-secure
Summary:        Secure ImageMagick Security Policy
Group:          Development/Libraries/C and C++
Provides:       imagick-config-7
Conflicts:      imagick-config-7
BuildArch:      noarch

%description config-7-upstream-secure
This stringent security policy prioritizes the implementation of
rigorous controls and restricted resource utilization to establish a
profoundly secure setting while employing ImageMagick. It deactivates
conceivably hazardous functionalities, including specific coders like
SVG or HTTP. The policy promotes the tailoring of security measures to
harmonize with the requirements of the local environment and the guidelines
of the organization. This protocol encompasses explicit particulars like
limitations on memory consumption, sanctioned pathways for reading and
writing, confines on image sequences, the utmost permissible duration of
workflows, allocation of disk space intended for image data, and even an
undisclosed passphrase for remote connections. By adopting this robust
policy, entities can elevate their overall security stance and alleviate
potential vulnerabilities.

%prep
%setup -q -n ImageMagick-%{source_version}

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{config_dir}/
cp config/policy-secure.xml %{buildroot}%{_sysconfdir}/%{config_dir}/policy.xml

%files config-7-upstream-secure
%dir %{_sysconfdir}/%{config_dir}
%config(noreplace) %{_sysconfdir}/%{config_dir}/policy.xml
%endif

%if "%{flavor}" == "config_websafe"
%package config-7-upstream-websafe
Summary:        Web-safe ImageMagick Security Policy
Group:          Development/Libraries/C and C++
Provides:       imagick-config-7
Conflicts:      imagick-config-7
BuildArch:      noarch

%description config-7-upstream-websafe
This security protocol designed for web-safe usage focuses on situations
where ImageMagick is applied in publicly accessible contexts, like websites.
It deactivates the capability to read from or write to any image formats
other than web-safe formats like GIF, JPEG, and PNG. Additionally, this
policy prohibits the execution of image filters and indirect reads, thereby
thwarting potential security breaches. By implementing these limitations,
the web-safe policy fortifies the safeguarding of systems accessible to
the public, reducing the risk of exploiting ImageMagick's capabilities
for potential attacks.

%prep
%setup -q -n ImageMagick-%{source_version}

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{config_dir}/
cp config/policy-websafe.xml %{buildroot}%{_sysconfdir}/%{config_dir}/policy.xml

%files config-7-upstream-websafe
%dir %{_sysconfdir}/%{config_dir}
%config(noreplace) %{_sysconfdir}/%{config_dir}/policy.xml
%endif

%changelog
