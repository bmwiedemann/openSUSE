#
# spec file for package libwebp2
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define lname libwebp2-0_1_0
Name:           libwebp2
Version:        0.1.0~g350
Release:        0
Summary:        Library and tools for the WebP2 graphics format
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://chromium.googlesource.com/codecs/libwebp2/

Source:         %name-%version.tar.xz
Patch1:         lib.diff
BuildRequires:  cmake
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkg-config

%description
WebP 2 is an update to the WebP image format, currently in
development. It is not ready for general use, and the format is not
finalized.

%package tools
Summary:        The WebP command line tools
Group:          Productivity/Archiving/Compression

%description tools
WebP 2 is an update to the WebP image format, currently in
development. It is not ready for general use, and the format is not
finalized.
This subpackage contains command-line utilities to analyze,
decode and encode webp2 files.

%package -n %lname
Summary:        Library for the WebP graphics format
Group:          System/Libraries

%description -n %lname
WebP 2 is an update to the WebP image format, currently in
development. It is not ready for general use, and the format is not
finalized. Changes to the library can break compatibility with images
encoded with previous versions.

%package devel
Summary:        Development files for libwebp, a library for the WebP format
Group:          Development/Libraries/C and C++
Requires:       %lname = %version-%release

%description devel
WebP 2 is an update to the WebP image format, currently in
development. It is not ready for general use, and the format is not
finalized.
This subpackage contains the header files for the webp2 library.

%prep
%autosetup -p1

%build
%cmake -DWP2_ENABLE_SIMD:BOOL=OFF
%cmake_build

%install
%cmake_install

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files tools
%_bindir/cwp2
%_bindir/dwp2
%_mandir/man1/*

%files -n %lname
%_libdir/libwebp2.so.0*

%files devel
%license LICENSE
%_includedir/wp2/
%_libdir/libwebp2.so
/usr/lib*/wp2

%changelog
