#
# spec file for package libdeflate
#
# Copyright (c) 2022 SUSE LLC
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


%define major 0
%define libname %{name}%{major}
Name:           libdeflate
Version:        1.15
Release:        0
Summary:        Library for DEFLATE/zlib/gzip compression and decompression
License:        BSD-2-Clause
URL:            https://github.com/ebiggers/libdeflate
Source:         https://github.com/ebiggers/libdeflate/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  zlib-devel

%description
libdeflate is a library for whole-buffer DEFLATE-based compression
and decompression. It supports raw, zlib-wrapped and gzip-wrapped DEFLATE.
It is significantly faster than zlib and gzip (+72-187%%).
In addition, libdeflate provides optional high compression modes
above zlib's "level 9".

%package -n    %{libname}
Summary:        Library for DEFLATE/zlib/gzip compression and decompression

%description -n    %{libname}
libdeflate is a library for whole-buffer DEFLATE-based compression
and decompression. It supports raw, zlib-wrapped and gzip-wrapped DEFLATE.
It is significantly faster than the zlib library:

 - decompression speedup over gzip-1.10 is 2.28x (generic), 2.87x (AVX2)
 - compression speedup over gzip is 1.72x (generic), 2.23x (AVX2)

In addition, libdeflate provides optional high compression modes
above zlib's "level 9".

%package tools
Summary:        File compression utility

%description tools
A gzip implementation that uses libdeflate which is significantly
faster than the GNU gzip implementation (+72-187%%).

%package devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
find %{buildroot} -type f -name "*.a" -delete -print

# Delete libdeflate-gunzip and replace with symlink libdeflate-gzip to fix dwz break with hardlink.
# boo#1180984
rm %{buildroot}%{_bindir}/libdeflate-gunzip
ln -s ./libdeflate-gzip %{buildroot}%{_bindir}/libdeflate-gunzip

%check
%ctest

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files tools
%{_bindir}/libdeflate-gzip
%{_bindir}/libdeflate-gunzip

%files -n %{libname}
%{_libdir}/libdeflate.so.%{major}

%files devel
%license COPYING
%doc README.md
%{_includedir}/libdeflate.h
%{_libdir}/libdeflate.so
%{_libdir}/cmake/libdeflate
%{_libdir}/pkgconfig/libdeflate.pc

%changelog
