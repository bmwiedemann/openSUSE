#
# spec file for package netpbm
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
%define ubsan_build    0
%define libmaj  11
%define libmin  96
%define libver  %{libmaj}.%{libmin}
Name:           netpbm
Version:        10.96.4
Release:        0
Summary:        A Graphics Conversion Package
License:        BSD-3-Clause AND GPL-2.0-or-later AND IJG AND MIT AND SUSE-Public-Domain
Group:          Productivity/Graphics/Convertors
URL:            http://netpbm.sourceforge.net/
Source:         netpbm-%{version}-nohpcdtoppm-noppmtompeg.tar.bz2
Source1:        netpbm-%{version}-documentation.tar.bz2
Source2:        baselibs.conf
Source3:        prepare-src-tarball.sh
# SUSE specific
Patch0:         %{name}-make.patch
# neccessary for running with ASAN
Patch1:         %{name}-tmpfile.patch
Patch2:         %{name}-security-code.patch
Patch3:         %{name}-security-scripts.patch
Patch4:         %{name}-gcc-warnings.patch
Patch5:         makeman-py3.patch
# PATCH-FIX-UPSTREAM fix bad use of plain char
Patch6:         signed-char.patch
# bsc#1144255 disable jpeg2k support due to removal of jasper
Patch8:         netpbm-disable-jasper.patch
# PATCH-FIX-UPSTREAM fix arithmetic overflow in ppmforge (https://sourceforge.net/p/netpbm/code/4428/)
Patch9:         ppmforge-fix-overflow.patch
BuildRequires:  flex
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
# needed for the makeman
BuildRequires:  python3-base
BuildRequires:  pkgconfig(x11)
Provides:       pbmplus

%description
These are the Portable Bitmap Plus Utilities.

This package provides tools for graphics conversion. Using these
tools, images can be converted from virtually any format into any
other format. A few of the supported formats include: GIF,
PC-Paintbrush, IFF ILBM, Gould Scanner file, MTV ray tracer, Atari
Degas .pi1 and .pi3, Macintosh PICT, HP Paintjet file, QRT raytracer,
AUTOCAD slide, Atari Spectrum (compressed and uncompressed), Andrew
Toolkit raster object, and many more. On top of that, man pages are
included for all tools.

%package -n libnetpbm%{libmaj}
Summary:        Libraries for the NetPBM (NetPortableBitmap) Graphic Formats
Group:          System/Libraries
Provides:       libnetpbm = %{version}
Obsoletes:      libnetpbm < %{version}

%description -n libnetpbm%{libmaj}
These are the libs for the netpbm graphic formats. The tools can be
found in the netpbm package. The sources are contained in the netpbm
source package.

%package -n libnetpbm-devel
Summary:        Header files for the NetPBM libraries
Group:          Development/Libraries/C and C++
Requires:       libnetpbm%{libmaj} = %{version}

%description -n libnetpbm-devel
These are the libs for the netpbm graphic formats. The tools can be
found in the netpbm package. The sources are contained in the netpbm
source package.

%prep
%setup -q -D -a 1
%autopatch -p1
mkdir pnmtopalm # for %%doc pnmtopalm
cp -p converter/other/pnmtopalm/{LICENSE,README} pnmtopalm

%build
# netpbm has _interactive_ configure perl script
cp config.mk.in config.mk # recomended by upstream, see doc/INSTALL
sed -i "s:STATICLIB_TOO = y:STATICLIB_TOO = n:" config.mk
# following two added 10.66.0, reported upstream
# recipe for target 'converter/install.manweb' failed
echo 'install.manweb:' >> converter/ppm/hpcdtoppm/Makefile
# dtto for ppmtompeg
echo 'install.manweb:' >> converter/ppm/ppmtompeg/Makefile
export CFLAGS="%{optflags} -flax-vector-conversions -Wno-return-type"
%if %{debug_build}
export CFLAGS="$CFLAGS -O0"
%endif
%if %{asan_build}
export CFLAGS="$CFLAGS -fsanitize=address -fno-sanitize-recover=all"
export LDFLAGS="$LDFLAGS -fsanitize=address"
%endif
%if %{ubsan_build}
export CFLAGS="$CFLAGS -fsanitize=undefined -fno-sanitize-recover=all"
export LDFLAGS="$LDFLAGS -fsanitize=undefined"
%endif
make %{?_smp_mflags} CFLAGS="$CFLAGS"
rm doc/INSTALL
#
# convert html to man pages
cd netpbm.sourceforge.net/doc
 ../../buildtools/makeman *.html
for i in 1 3 5 ; do
  mkdir -p ../../man/man${i}
  mv *.${i} ../../man/man${i}
done

%install
# netpbm has _interactive_ install perl script, see doc/INSTALL
make pkgdir=`pwd`/package package STRIPFLAG=
#
mkdir -p %{buildroot}%{_prefix}/{bin,include,%{_lib},share/man,share/%{name}}
cp -pd  package/bin/* 		%{buildroot}%{_bindir}
cp -pd  package/lib/*.so* 	%{buildroot}%{_libdir}
ln -s   libnetpbm.so.%{libver} 	%{buildroot}%{_libdir}/libnetpbm.so
cp -prd package/include/netpbm 	%{buildroot}%{_includedir}
cp -prd man/* 			%{buildroot}%{_mandir}
install -m 644 converter/other/pnmtopalm/*.map \
				%{buildroot}%{_datadir}/%{name}
rm %{buildroot}%{_bindir}/g3topbm # conflict with g3utils
rm %{buildroot}%{_bindir}/pstopnm # disable due security reasons, e. g. [bsc#1105592]

%post   -n libnetpbm%{libmaj} -p /sbin/ldconfig
%postun -n libnetpbm%{libmaj} -p /sbin/ldconfig

%check
%if %{asan_build}
export LSAN_OPTIONS="detect_leaks=0"
%endif
%if %{ubsan_build}
export UBSAN_OPTIONS="print_stacktrace=1"
%endif
# do not run unneccesary tests
sed -i '/all-in-place/d'   test/Test-Order
sed -i '/legacy-names/d'   test/Test-Order
# picttoppm.c: #error "Unfixable. Don't ship me"
sed -i '/pict-roundtrip/d' test/Test-Order
# pstopnm is not shipped
sed -i '/^l\?ps.*\.test/d' test/Test-Order
# new winicon-roundtrip2.test failure reported to bryanh@giraffe-data.com on 2020-12-29
# $ LD_LIBRARY_PATH=lib PATH=package/bin pamtowinicon -pngthreshold=1 package-test-tmp/testimg1.pam
# pamtowinicon: bad magic number 0xf0f - not a PAM, PPM, PGM, or PBM file
# $
sed -i '/winicon-roundtrip2.test/d'  test/Test-Order
mkdir package-test-{tmp,results}
make pkgdir=`pwd`/package tmpdir=`pwd`/package-test-tmp RESULTDIR=`pwd`/package-test-results check-package

%files
%doc README doc/* netpbm.sourceforge.net/doc
%doc pnmtopalm/
%{_mandir}/man1/*%{ext_man}
%{_mandir}/man5/*%{ext_man}
%{_bindir}/*
%{_datadir}/%{name}

%files -n libnetpbm%{libmaj}
%{_libdir}/lib*.so.%{libmaj}
%{_libdir}/lib*.so.%{libver}

%files -n libnetpbm-devel
%{_includedir}/%{name}
%{_libdir}/lib*.so
%{_mandir}/man3/*%{ext_man}

%changelog
