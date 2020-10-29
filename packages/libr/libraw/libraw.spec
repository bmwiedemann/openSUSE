#
# spec file for package libraw
#
# Copyright (c) 2020 SUSE LLC
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


%define debug_build   0
%define asan_build    0

%define tar_name LibRaw
%define lver    20
%define lname	libraw%{lver}
Name:           libraw
Version:        0.20.2
Release:        0
Summary:        Library for reading RAW files obtained from digital photo cameras
License:        CDDL-1.0 OR LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://www.libraw.org/
#Git-Clone:	git://github.com/LibRaw/LibRaw
Source:         https://www.libraw.org/data/%tar_name-%version.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
# zlib for deflate DNG support
BuildRequires:  zlib-devel

%description
LibRaw is a library for reading RAW files obtained from digital photo
cameras (CRW/CR2, NEF, RAF, DNG, and others).

LibRaw is based on the source codes of the dcraw utility, where part of
drawbacks have already been eliminated and part will be fixed in future.

%package tools
Summary:        Tools for reading RAW files obtained from digital photo cameras
Group:          Productivity/Graphics/Other

%description tools
LibRaw is a library for reading RAW files obtained from digital photo
cameras (CRW/CR2, NEF, RAF, DNG, and others).

LibRaw is based on the source codes of the dcraw utility, where part of
drawbacks have already been eliminated and part will be fixed in future.

%package -n %lname
Summary:        Library for reading RAW files obtained from digital photo cameras
Group:          System/Libraries

%description -n %lname
LibRaw is a library for reading RAW files obtained from digital photo
cameras (CRW/CR2, NEF, RAF, DNG, and others).

LibRaw is based on the source codes of the dcraw utility, where part of
drawbacks have already been eliminated and part will be fixed in future.

%package devel
Summary:        Development files for libraw
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
LibRaw is a library for reading RAW files obtained from digital photo
cameras (CRW/CR2, NEF, RAF, DNG, and others).

LibRaw is based on the source codes of the dcraw utility, where part of
drawbacks have already been eliminated and part will be fixed in future.

%package devel-static
Summary:        Library for reading RAW files obtained from digital photo cameras
Group:          Development/Libraries/C and C++
Requires:       %name-devel = %version

%description devel-static
LibRaw is a library for reading RAW files obtained from digital photo
cameras (CRW/CR2, NEF, RAF, DNG, and others).

LibRaw is based on the source codes of the dcraw utility, where part of
drawbacks have already been eliminated and part will be fixed in future.

This package contains static libraries that applications can use to build
against LibRaw. LibRaw does not provide dynamic libraries.

%prep
%setup -q -n %{tar_name}-%{version}

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CXXFLAGS="%{optflags} -fPIC -DUSE_ZLIB"
%if %{debug_build}
export CXXFLAGS="$CXXFLAGS -O0"
%endif
export LIBS="$LIBS -lz"
autoreconf -fi
%configure
%if %{asan_build}
sed -i -e 's/\(^CXXFLAGS =.*\)/\1 -fsanitize=address/' \
       -e 's/\(^LIBS =.*\)/\1 -lasan/' \
       Makefile
%endif
make %{?_smp_mflags}

%install
find doc -type f -name "*.html" -exec chmod a-x "{}" "+"
mv doc manual
# The source tree has these with execute permissions for some reason
chmod -x Changelog.txt LICENSE.CDDL LICENSE.LGPL COPYRIGHT
chmod -x manual/index.html
# The Libraries
%make_install
find %buildroot -type f -name "*.la" -delete -print
# duplicated files
rm -rf %buildroot%_datadir/doc
%fdupes %buildroot/%_prefix

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files tools
%_bindir/*

%files devel
%doc Changelog.txt
%license COPYRIGHT LICENSE.CDDL LICENSE.LGPL
%doc manual
%_includedir/%name/
%_libdir/pkgconfig/*.pc
%_libdir/libraw.so
%_libdir/libraw_r.so

%files -n %lname
%_libdir/libraw.so.%{lver}*
%_libdir/libraw_r.so.%{lver}*

%files devel-static
%_libdir/libraw.a
%_libdir/libraw_r.a

%changelog
