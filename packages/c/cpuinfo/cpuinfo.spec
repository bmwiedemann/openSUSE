#
# spec file for package cpuinfo
#
# Copyright (c) 2024 SUSE LLC
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


Name:           cpuinfo
Version:        0~git1720582619.ca67895
Release:        0
Summary:        Tools for obtaining CPU information
License:        BSD-2-Clause
URL:            https://github.com/pytorch/cpuinfo
Source:         %name-%version.tar.xz
Patch1: soname.patch
BuildRequires:  cmake
ExcludeArch: s390x

%description
cpuinfo is a library to detect essential for performance optimization
information about host CPU.

%define lname libcpuinfo0
%package -n %lname
Summary:        CPU INFOrmation library

%description -n %lname
cpuinfo is a library to detect essential for performance optimization
information about host CPU.

It offers detection of SoC and information about cores, cache,
toplogy and supported instruction sets.

%package devel
Summary:        Headers for the cpuinfo library
Requires:       %lname = %version-%release

%description devel
cpuinfo is a library to detect essential for performance optimization
information about host CPU.

This subpackage contains development files like headers and cmake
scripts.

%prep
%autosetup -p1

%build
# tests need extra packages, which are considered to be downloaded during build
# needs a second step to add these ...
%cmake .. \
  -DCPUINFO_LIBRARY_TYPE=shared \
  -DUSE_SYSTEM_LIBS=ON \
  -DCPUINFO_BUILD_UNIT_TESTS=OFF \
  -DCPUINFO_BUILD_MOCK_TESTS=OFF \
  -DCPUINFO_BUILD_BENCHMARKS=OFF

%install
%cmake_install
mkdir -p %buildroot/usr/share/cmake
mv %buildroot/usr/share/{,cmake/}cpuinfo

%ldconfig_scriptlets -n %lname

%files
%license LICENSE
%doc README.md
%_bindir/cache-info
%_bindir/cpu-info
%_bindir/isa-info
%ifarch %ix86 x86_64
%_bindir/cpuid-dump
%endif

%files -n %lname
%_libdir/libcpuinfo.so.*

%files devel
%_includedir/cpuinfo.h
%_libdir/libcpuinfo.so
%_libdir/pkgconfig/libcpuinfo.pc
%_datadir/cmake/cpuinfo

%changelog
