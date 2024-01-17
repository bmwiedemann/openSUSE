#
# spec file for package benchmark
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


%define soname  lib%{name}
%define sover   1
Name:           benchmark
Version:        1.7.1
Release:        0
Summary:        A microbenchmark support library
License:        Apache-2.0
URL:            https://github.com/google/benchmark
Source:         %{name}-%{version}.tar.gz
Patch0:         gcc12-disable-Werror=maybe-uninitialized.patch
BuildRequires:  cmake >= 3.5.1
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  pkgconfig

%description
A library to support the benchmarking of functions, similar to unit-tests.

%package -n %{soname}%{sover}
Summary:        Shared library for google benchmark

%description -n %{soname}%{sover}
A library to support the benchmarking of functions, similar to unit-tests.

%package devel
Summary:        Development files for google benchmark
Requires:       %{soname}%{sover} = %{version}

%description devel
Development files for google benchmark library

%prep
%autosetup

%build
sed -e 's|lib_install_dir "lib/"|lib_install_dir "%{_libdir}/"|g' \
    -e 's|config_install_dir "lib/cmake|config_install_dir "%{_libdir}/cmake|g' \
    -e 's|pkgconfig_install_dir "lib/pkgconfig"|pkgconfig_install_dir "%{_libdir}/pkgconfig"|g' \
    -i src/CMakeLists.txt
sed -e 's|libdir=${prefix}/lib|libdir=${prefix}/%{_lib}|' \
    -i cmake/benchmark.pc.in

%cmake \
  -DBENCHMARK_ENABLE_LTO=on \
  -DBENCHMARK_ENABLE_GTEST_TESTS=false \
  -DBENCHMARK_ENABLE_TESTING=true
%cmake_build

%install
%cmake_install
# dont ship debug stuff
rm -rf %{buildroot}%{_libexecdir}/debug
# doc will be installed in different location
rm -rf %{buildroot}%{_datadir}/doc/benchmark

%check
# path needs to be exported otherwise unit tests will fail
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{_builddir}/%{name}-%{version}/build/src/
%ctest

%post -n %{soname}%{sover} -p /sbin/ldconfig
%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files -n %{soname}%{sover}
%license LICENSE
%doc README.md AUTHORS
%{_libdir}/%{soname}.so.%{sover}*
%{_libdir}/%{soname}_main.so.%{sover}*

%files devel
%license LICENSE
%doc README.md AUTHORS docs/*
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{soname}.so
%{_libdir}/%{soname}_main.so
%{_includedir}/%{name}

%changelog
