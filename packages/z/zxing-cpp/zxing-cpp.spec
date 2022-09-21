#
# spec file for package zxing-cpp
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define sover 1
Name:           zxing-cpp
Version:        1.2.0
Release:        0
Summary:        Library for processing 1D and 2D barcodes
License:        Apache-2.0 AND Zlib AND LGPL-2.1-with-Qt-Company-Qt-exception-1.1
Group:          Development/Languages/C and C++
URL:            https://github.com/nu-book/zxing-cpp/
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE cmake-check-system-first.patch -- Search system for needed libraries first
Patch0:         cmake-check-system-first.patch
# PATCH-FIX-UPSTREAM 269.patch -- Update stb_image/stb_image_write
Patch1:         269.patch
# PATCH-FIX-UPSTREAM 0001-test-update-to-libfmt-v9.0.0.patch -- fmt 9 compatibility
Patch2:         0001-test-update-to-libfmt-v9.0.0.patch
BuildRequires:  pkgconfig
# Use cmake3 package on SLE12 because cmake is too old (version 3.5)
%if !0%{?is_opensuse} && 0%{?sle_version} < 150000
BuildRequires:  cmake3-full >= 3.10
BuildRequires:  gcc11-c++
%else
BuildRequires:  cmake >= 3.10
BuildRequires:  gcc-c++
%endif
# only TW has fmt
%if 0%{?suse_version} > 1500
# For blackbox tests
BuildRequires:  cmake(fmt) >= 7.1.2
%endif

%description
ZXing ("zebra crossing") is an multi-format 1D/2D barcode image
processing library. This package provides a C++ implementation.

%package -n libZXing%{sover}
Summary:        Library for processing 1D and 2D barcodes
# called libZXing in the 1.1.0 update
Group:          System/Libraries
Provides:       libZXingCore%{sover} = %{version}
Obsoletes:      libZXingCore%{sover} < %{version}

%description -n libZXing%{sover}
ZXing ("zebra crossing") is an multi-format 1D/2D barcode image
processing library. This package provides a C++ implementation.

%package devel
Summary:        Header files for zxing, a library for processing 1D and 2D barcodes
Group:          Development/Languages/C and C++
Requires:       libZXing%{sover} = %{version}

%description devel
ZXing ("zebra crossing") is an multi-format 1D/2D barcode image
processing library. This package provides header files to use ZXing in
other applications.

%prep
%autosetup -p1

%build
# Use g++-11 to build a C++17 codebase
# Examples require QT5-base/multimedia, but doing so creates a cycle
# Blackbox tests require fmt
%cmake \
    -DBUILD_EXAMPLES=OFF \
%if !0%{?is_opensuse} && 0%{?sle_version} < 150000
    -DCMAKE_CXX_COMPILER=/usr/bin/g++-11 \
%endif
%if 0%{?suse_version} < 1550
    -DBUILD_BLACKBOX_TESTS=OFF
%endif

%cmake_build

%install
%cmake_install

%check
%if 0%{?sle_version}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%endif
%ctest

%post -n libZXing%{sover} -p /sbin/ldconfig
%postun -n libZXing%{sover} -p /sbin/ldconfig

%files -n libZXing%{sover}
%doc README.md
%license LICENSE.*
%{_libdir}/libZXing.so.%{sover}
%{_libdir}/libZXing.so.%{sover}.*

%files devel
%license LICENSE.*
%{_includedir}/ZXing/
%{_libdir}/cmake/ZXing/
%{_libdir}/libZXing.so
%{_libdir}/pkgconfig/zxing.pc

%changelog
