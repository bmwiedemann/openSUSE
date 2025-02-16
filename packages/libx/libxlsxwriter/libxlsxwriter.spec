#
# spec file for package libxlsxwriter
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


%define libname libxlsxwriter7

Name:           libxlsxwriter
Version:        1.2.0
Release:        0
Summary:        A C library for creating Excel XLSX files
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/jmcnamara/libxlsxwriter
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(zlib)
# Tests
BuildRequires:  python3-pytest

%description
A C library for creating Excel XLSX files.

%package -n %{libname}
Summary:        A C library for creating Excel XLSX files
Group:          System/Libraries

%description -n %{libname}
Libxlsxwriter is a C library for creating Excel XLSX files.

This package holds the shared library files.

%package devel
Summary:        Headers for libxlsxwriter
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Libxlsxwriter is a C library for creating Excel XLSX files.

This package holds the development files.

%prep
%autosetup -p1

%build
%cmake -DUSE_SYSTEM_MINIZIP=ON -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ifnarch s390x
%ctest
%endif

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license License.txt
%{_libdir}/libxlsxwriter.so.*

%files devel
%license License.txt
%doc Changes.txt Readme.md CONTRIBUTING.md
%{_includedir}/xlsxwriter.h
%{_includedir}/xlsxwriter/
%{_libdir}/pkgconfig/xlsxwriter.pc
%{_libdir}/libxlsxwriter.so

%changelog
