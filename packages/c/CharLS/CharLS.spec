#
# spec file for package CharLS
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


%define so_ver 2
Name:           CharLS
Version:        2.4.1
Release:        0
Summary:        A JPEG-LS library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/team-charls/charls/
Source0:        https://github.com/team-charls/charls/archive/refs/tags/%{version}.tar.gz#/charls-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
An optimized implementation of the JPEG-LS standard for lossless and
near-lossless image compression. JPEG-LS is a low-complexity standard that
matches JPEG 2000 compression ratios. In terms of speed, CharLS outperforms
open source and commercial JPEG LS implementations.

%package devel
Summary:        Libraries and headers for CharLS
Group:          Development/Libraries/C and C++
Requires:       libcharls%{so_ver} = %{version}

%description devel
This package contains libraries and headers for CharLS.

%package -n libcharls%{so_ver}
Summary:        A JPEG-LS library
Group:          System/Libraries

%description -n libcharls%{so_ver}
An optimized implementation of the JPEG-LS standard for lossless and
near-lossless image compression. JPEG-LS is a low-complexity standard that
matches JPEG 2000 compression ratios. In terms of speed, CharLS outperforms
open source and commercial JPEG LS implementations.

%prep
%setup -q -n charls-%{version}

%build
%cmake \
 -DBUILD_SHARED_LIBS=ON \
 -DBUILD_TESTING=ON
%make_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.
ctest .

%post -n libcharls%{so_ver} -p /sbin/ldconfig
%postun -n libcharls%{so_ver} -p /sbin/ldconfig

%files devel
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_includedir}/charls/
%{_libdir}/*.so
%{_libdir}/cmake/charls/
%{_libdir}/pkgconfig/*.pc

%files -n libcharls%{so_ver}
%{_libdir}/libcharls.so.%{so_ver}*

%changelog
