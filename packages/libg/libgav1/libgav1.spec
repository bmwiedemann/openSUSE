#
# spec file for package libgav1
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define lname   libgav1-1
Name:           libgav1
Version:        0.18.0
Release:        0
Summary:        AV1 video decoding library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://chromium.googlesource.com/codecs/libgav1/
Source:         %name-%version.tar.xz
Patch1:         gcc13.diff
BuildRequires:  cmake >= 3.7.1
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  xz

%description
libgav1 is a Main profile (0) & High profile (1) compliant AV1 decoder written
in C++ and also offering a C API.

%package -n %lname
Summary:        AV1 video decoding library
Group:          System/Libraries

%description -n %lname
libgav1 is a Main profile (0) & High profile (1) compliant AV1 decoder written
in C++ and also offering a C API.

%package devel
Summary:        Development for libgav1, an AV1 video decoder
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libgav1 is a Main profile (0) & High profile (1) compliant AV1 decoder written
in C++ and also offering a C API.

This subpackage contains the header files.

%prep
%autosetup -p1
mkdir third_party
ln -s /usr/src/abseil-cpp third_party/abseil-cpp

%build
%cmake \
	-DLIBGAV1_ENABLE_EXAMPLES:BOOL=OFF \
	-DLIBGAV1_ENABLE_TESTS:BOOL=OFF \
	-DLIBGAV1_THREADPOOL_USE_STD_MUTEX=1 \
	-DBUILD_SHARED_LIBS:BOOL=ON
%cmake_build

%install
%cmake_install
rm -fv %buildroot/%_libdir/*.a

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libgav1.so.*
%license LICENSE

%files devel
%_includedir/gav1/
%_libdir/pkgconfig/*.pc
%_libdir/*.so
%_datadir/cmake/

%changelog
