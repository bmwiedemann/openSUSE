#
# spec file for package snappy
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


%define libname libsnappy1
Name:           snappy
Version:        1.1.9
Release:        0
Summary:        A compressor/decompressor library favoring time
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/google/snappy/
Source0:        https://github.com/google/snappy/archive/%{version}.tar.gz
Source1:        snappy.pc
Source99:       baselibs.conf
Patch0:         use-system-test-libs.patch
Patch1:         fix-always-inline.patch
Patch2:         reenable-rtti.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  lzo-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(benchmark)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(zlib)

%description
Snappy is a compression/decompression library. It does not aim for maximum
compression, or compatibility with any other compression library; instead, it
aims for high speeds and reasonable compression.

%package -n %{libname}
Summary:        Shared library from snappy
Group:          System/Libraries

%description -n %{libname}
Snappy is a compression/decompression library. It does not aim for maximum
compression, or compatibility with any other compression library; instead, it
aims for high speeds and reasonable compression. For instance, compared to
the fastest mode of zlib, Snappy is an order of magnitude faster for most
inputs, but the resulting compressed files are anywhere from 20%% to 100%%
bigger. On a single core of a 1st-generation Core i7 processor in 64-bit
mode, Snappy compresses at about 250 MB/sec or more and decompresses at about
500 MB/sec or more.

This package holds the shared library of snappy.

%package devel
Summary:        Development files for snappy
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Snappy is a compression/decompression library. It does not aim for maximum
compression, or compatibility with any other compression library; instead, it
aims for high speeds and reasonable compression.

This package holds the development files for snappy.

%prep
%autosetup

%build
%cmake -DSNAPPY_USE_BUNDLED_GTEST=OFF -DSNAPPY_USE_BUNDLED_BENCHMARK_LIB=OFF
%make_build

%install
%cmake_install
install -d -m 755 %{buildroot}%{_libdir}/pkgconfig
install -m 644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%check
%ctest

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%{_libdir}/libsnappy.so.*

%files devel
%{_includedir}/snappy*.h
%{_libdir}/libsnappy.so
%dir %{_libdir}/cmake/Snappy/
%{_libdir}/cmake/Snappy/*
%{_libdir}/pkgconfig/%{name}.pc

%changelog
