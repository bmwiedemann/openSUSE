#
# spec file for package librtprocess
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


Name:           librtprocess
Version:        0.12.0+20230627
Release:        0
Summary:        A collection of functions for processing photos
License:        BSL-1.0 AND GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/CarVac/librtprocess
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(glibmm-2.4)
%define libname librtprocess0

%description
This is a project that aims to make some of RawTherapee's highly optimized raw
processing routines readily available for other FOSS photo editing software.

%package -n %{libname}
Group:          Development/Libraries/C and C++
Summary:        Shared library for librtprocess

%description -n %{libname}
This is a project that aims to make some of RawTherapee's highly optimized raw
processing routines readily available for other FOSS photo editing software.

This package holds the shared library.

%package devel
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Summary:        Development files for librtprocess

%description devel
This is a project that aims to make some of RawTherapee's highly optimized raw
processing routines readily available for other FOSS photo editing software.

This package holds the development files.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE.txt
%{_libdir}/librtprocess.so.*

%files devel
%doc README.md
%license LICENSE.txt
%{_includedir}/rtprocess/
%{_libdir}/cmake/rtprocess/
%{_libdir}/librtprocess.so
%{_libdir}/pkgconfig/rtprocess.pc

%changelog
