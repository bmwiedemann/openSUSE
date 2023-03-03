#
# spec file for package folly
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


%define lname libfolly-v2023_02_27_00
Name:           folly
Version:        2023.02.27.00
Release:        0
Summary:        A C++ utility library
License:        MIT
URL:            https://github.com/facebook/folly
Source:         https://github.com/facebook/folly/releases/download/v%version/folly-v%version.tar.gz
BuildRequires:  binutils-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  double-conversion-devel
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  gflags-devel-static
BuildRequires:  glog-devel
BuildRequires:  libaio-devel
BuildRequires:  libboost_context-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libbz2-devel
%if 0%{?suse_version} >= 1550
# new versioning with x.y.z after 20210528
BuildRequires:  libdwarf-devel-static
%else
BuildRequires:  libdwarf-devel-static >= 20170103
%endif
BuildRequires:  libevent-devel
BuildRequires:  liblz4-devel
BuildRequires:  libsodium-devel
BuildRequires:  libunwind-devel
BuildRequires:  liburing-devel
BuildRequires:  libzstd-devel
BuildRequires:  libzstd-devel-static
BuildRequires:  lzlib-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  snappy-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel-static

%description
Folly is a C++ utility library developed at Facebook.

%package -n %lname
Summary:        A C++ utility library
Group:          System/Libraries

%description -n %lname
This contains the shared libraries for folly, a C++ utility library developed
at Facebook.

%package devel
Summary:        Development files for folly, a utility library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Development files library for folly, a C++ utility library.

%prep
%autosetup -p1 -c folly-%version

%build
# Since its introduction for ABI purposes, PACKAGE_VERSION was never
# again modified *sigh*
#
%cmake -DCMAKE_CXX_FLAGS="%optflags -ffat-lto-objects" \
	-DBUILD_SHARED_LIBS:BOOL=ON -DPACKAGE_VERSION="v%version" \
	-DCMAKE_LIBRARY_ARCHITECTURE="%_target_cpu"
%cmake_build

%install
%cmake_install

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libfolly*.so.*

%files devel
%_includedir/%name/
/usr/lib/cmake/
%_libdir/pkgconfig/lib%name.pc
%_libdir/libfolly*.so

%changelog
