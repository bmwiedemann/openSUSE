#
# spec file for package zxing-cpp
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


%define sover 1
Name:           zxing-cpp
Version:        1.0.5
Release:        0
Summary:        Library for processing 1D and 2D barcodes
License:        Apache-2.0 AND Zlib AND LGPL-2.1-with-Qt-Company-Qt-exception-1.1
Group:          Development/Languages/C and C++
URL:            https://github.com/nu-book/zxing-cpp/
Source0:        https://github.com/nu-book/zxing-cpp/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch1:         fix-library-installation-and-versioning.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
ZXing ("zebra crossing") is an multi-format 1D/2D barcode image
processing library. This package provides a C++ implementation.

%prep
%autosetup -p1

%build
%cmake -DBUILD_SHARED_LIBRARY=ON
%make_jobs

%install
%cmake_install

%package -n libZXingCore%{sover}
Summary:        Library for processing 1D and 2D barcodes
Group:          System/Libraries

%description -n libZXingCore%{sover}
ZXing ("zebra crossing") is an multi-format 1D/2D barcode image
processing library. This package provides a C++ implementation.

%post -n libZXingCore%{sover} -p /sbin/ldconfig
%postun -n libZXingCore%{sover} -p /sbin/ldconfig

%files -n libZXingCore%{sover}
%doc README.md
%license LICENSE.*
%{_libdir}/libZXingCore.so.%{sover}
%{_libdir}/libZXingCore.so.%{sover}.*

%package devel
Summary:        Header files for zxing, a library for processing 1D and 2D barcodes
Group:          Development/Languages/C and C++
Requires:       libZXingCore%{sover} = %{version}

%description devel
ZXing ("zebra crossing") is an multi-format 1D/2D barcode image
processing library. This package provides header files to use ZXing in
other applications.

%files devel
%license LICENSE.*
%{_includedir}/ZXing/
%{_libdir}/cmake/ZXing/
%{_libdir}/libZXingCore.so

%changelog
