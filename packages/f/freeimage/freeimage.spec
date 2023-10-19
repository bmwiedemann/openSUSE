#
# spec file for package freeimage
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


%define tag_ver 3.19.0
%define so_ver 3
Name:           freeimage
Version:        3.18.0.1909
Release:        0
Summary:        Multi-format Image Decoder Library
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://freeimage.sourceforge.io/
Source0:        %{name}-%{version}.tar.xz
Patch0:         unbundle.patch
# PATCH-FIX-OPENSUSE doxygen.patch asterios.dramis@gmail.com -- Fix documentation building (Based on patch from Fedora)
Patch1:         doxygen.patch
# PATCH-FIX-OPENSUSE makefiles_fixes.patch asterios.dramis@gmail.com -- Fix CFLAGS and CXXFLAGS, removed -s (strip) option, add missing symlinks for libfreeimageplus, remove root user from install
Patch3:         makefiles_fixes.patch
# build with openexr3
Patch9:         freeimage-openexr3.patch
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  jxrlib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(zlib)

%description
FreeImage is a library for developers who would like to support
graphics image formats like PNG, BMP, JPEG, TIFF and others as needed
by today's multimedia applications.

%package devel
Summary:        Development Files for FreeImage
Requires:       lib%{name}%{so_ver} = %{version}
Requires:       lib%{name}plus%{so_ver} = %{version}
# libfreeimage-devel was last used at version 3.10.0
Provides:       lib%{name}-devel = %{version}
Obsoletes:      lib%{name}-devel < %{version}

%description devel
This package provides development libraries and headers needed to build
software using FreeImage.

%package -n lib%{name}%{so_ver}
Summary:        Multi-format Image Decoder Library

%description -n lib%{name}%{so_ver}
FreeImage is a library for developers who would like to support
graphics image formats like PNG, BMP, JPEG, TIFF and others as needed
by today's multimedia applications.

%package -n lib%{name}plus%{so_ver}
Summary:        Multi-format Image Decoder Library

%description -n lib%{name}plus%{so_ver}
FreeImage is a library for developers who would like to support
graphics image formats like PNG, BMP, JPEG, TIFF and others as needed
by today's multimedia applications.

%prep
%autosetup -p1

%build
# access to libtiff/libjpeg internals requires internal headers, requires
# bundled copy of the libs, which is a no-no.
# Disable the affected components without removing files (which may be
# referenced in the build system).
#
: >Source/FreeImage/PluginG3.cpp >Source/Metadata/XTIFF.cpp \
	>Source/FreeImageToolkit/JPEGTransform.cpp \
	>Source/FreeImage/PluginTIFF.cpp

# sanitize encodings / line endings
for file in `find . -type f -name '*.c' -or -name '*.cpp' -or -name '*.h' -or -name '*.txt' -or -name Makefile`; do
  iconv --from=ISO-8859-15 --to=UTF-8 $file > $file.new && \
  sed -i 's|\r||g' $file.new && \
  touch -r $file $file.new && mv $file.new $file
done

sh ./gensrclist.sh
sh ./genfipsrclist.sh
if grep -q 'SRCS = $' Makefile.srcs; then
	echo "Empty source list generated. Broken OBS package."
	exit 1
fi

export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%make_build -f Makefile.gnu
%make_build -f Makefile.fip

pushd Wrapper/FreeImagePlus/doc
doxygen FreeImagePlus.dox
popd

%install
%make_install INSTALLDIR=%{buildroot}%{_libdir}
make -f Makefile.fip DESTDIR=%{buildroot} INSTALLDIR=%{buildroot}%{_libdir} install

# Remove static libraries
rm -f %{buildroot}%{_libdir}/*.a

%post -n lib%{name}%{so_ver} -p /sbin/ldconfig
%postun -n lib%{name}%{so_ver} -p /sbin/ldconfig
%post -n lib%{name}plus%{so_ver} -p /sbin/ldconfig
%postun -n lib%{name}plus%{so_ver} -p /sbin/ldconfig

%files devel
%doc Whatsnew.txt license-*.txt
%doc Wrapper/FreeImagePlus/doc/html/
%{_includedir}/FreeImage.h
%{_includedir}/FreeImagePlus.h
%{_libdir}/libfreeimage.so
%{_libdir}/libfreeimageplus.so

%files -n lib%{name}%{so_ver}
%{_libdir}/lib%{name}.so.3*
%{_libdir}/lib%{name}-%{tag_ver}.so

%files -n lib%{name}plus%{so_ver}
%{_libdir}/lib%{name}plus.so.3*
%{_libdir}/lib%{name}plus-%{tag_ver}.so

%changelog
