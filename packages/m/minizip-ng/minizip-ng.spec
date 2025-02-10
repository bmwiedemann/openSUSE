#
# spec file for package minizip-ng
#
# Copyright (c) 2025 SUSE LLC
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


%define build_flavor @BUILD_FLAVOR@%{nil}
%define pkg_name minizip-ng

# TODO
%if "%{build_flavor}" == "compat"
Name:           minizip
%global         soname libminizip1
%global         compat_mode ON
%else
Name:           minizip-ng
%global         soname libminizip-ng4
%global         compat_mode OFF
%endif

Version:        4.0.8
Release:        0
Summary:        Companion library to zlib-ng for reading and writing ZIP files
License:        Zlib
URL:            https://github.com/zlib-ng/minizip-ng
Source:         https://github.com/zlib-ng/minizip-ng/archive/refs/tags/%version.tar.gz
BuildRequires:  cmake >= 3.11.0
BuildRequires:  gcc-c++
BuildRequires:  gtest
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib-ng)

%description
%{name} is a ZIP file manipulation library.

It has support for:
* Basic read-write operation on zip archives (adding files and removing
  files) on a high-level and also raw zip entry data
* ZIP64 extension for large files
* Zlib, BZIP2, LZMA, XZ, and ZSTD compression methods
* PKWARE- and Winzip-AES styles password protection
* NTFS timestamp support for UTC last modified, last accessed, and creation dates
* zip archive splitting
* Follow/store symbolic links
* UTF-8, cp437, cp932, cp936 and cp950 filename character set support

%package devel
Summary:        Development files for %{name}
Requires:       %{soname} = %{version}

%description devel
This package contains the C header and CMake config files.

%package -n %{soname}
Summary:        Companion library to zlib-ng for reading and writing ZIP files
Group:          System/Libraries

%description -n %{soname}
%{name} is a ZIP file manipulation library.

It has support for:
* Basic read-write operation on zip archives (adding files and removing
  files) on a high-level and also raw zip entry data
* ZIP64 extension for large files
* Zlib, BZIP2, LZMA, XZ, and ZSTD compression methods
* PKWARE- and Winzip-AES styles password protection
* NTFS timestamp support for UTC last modified, last accessed, and creation dates
* zip archive splitting
* Follow/store symbolic links
* UTF-8, cp437, cp932, cp936 and cp950 filename character set support

%prep
%autosetup -p1 -n %{pkg_name}-%{version}

%build
%cmake \
    -DMZ_COMPAT:BOOL=%{compat_mode} \
    -DSKIP_INSTALL_BINARIES:BOOL=ON \
    -DMZ_SIGNING:BOOL=ON  \
    -DMZ_FORCE_FETCH_LIBS:BOOL=OFF \
    -DMZ_BUILD_TESTS:BOOL=ON \
    -DMZ_BUILD_UNIT_TESTS:BOOL=ON

%cmake_build

%install
%cmake_install

%check
cd build && ctest --output-on-failure %{version}

%files devel
%license LICENSE
%{_includedir}/minizip*/
%{_libdir}/cmake/minizip*/
%{_libdir}/libminizip*.so
%{_libdir}/pkgconfig/minizip*.pc
%doc *.md
%doc doc/

%ldconfig_scriptlets -n %{soname}

%files -n %{soname}
%license LICENSE
%{_libdir}/libminizip*.so.*

%changelog
