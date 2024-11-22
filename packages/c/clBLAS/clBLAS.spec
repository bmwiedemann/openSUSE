#
# spec file for package clBLAS
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


%define sover 2
%define shlib lib%{name}%{sover}
# TODO: Tests do not build with the current version of system gtest
%bcond_with tests
Name:           clBLAS
Version:        2.12+git.20170323.cf91139
Release:        0
Summary:        BLAS functions written in OpenCL
License:        Apache-2.0
URL:            https://github.com/clMathLibraries/clBLAS
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM - https://github.com/clMathLibraries/clBLAS/pull/362
Patch1:         https://github.com/clMathLibraries/clBLAS/pull/362.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
%if %{with tests}
BuildRequires:  blas-devel
BuildRequires:  gtest
%endif

%description
%{name} is a software library containing BLAS functions written in OpenCL. The
complete set of BLAS level 1, 2 and 3 routines is implemented. In addition to
GPU devices, the library also supports running on CPU devices to facilitate
debugging and multicore programming.

%package -n %{shlib}
Summary:        Shared library for clBLAS - a BLAS library for OpenCL

%description -n %{shlib}
%{name} is a software library containing BLAS functions written in OpenCL. The
complete set of BLAS level 1, 2 and 3 routines is implemented. In addition to
GPU devices, the library also supports running on CPU devices to facilitate
debugging and multicore programming.

This package provides the shared libs for %{name}.

%package devel
Summary:        Headers and devel files for clBLAS - a BLAS library for OpenCL
Requires:       %{shlib} = %{version}

%description devel
%{name} is a software library containing BLAS functions written in OpenCL. The
complete set of BLAS level 1, 2 and 3 routines is implemented. In addition to
GPU devices, the library also supports running on CPU devices to facilitate
debugging and multicore programming.

This package provides the headers and sources needed for developing software
against clBLAS.

%prep
%autosetup -p1

%build
pushd src
%cmake \
  -DBUILD_TEST:BOOL=%{?with_tests:ON}%{!?with_tests:OFF} \
	%{nil}
%cmake_build

%install
pushd src
%cmake_install

%if %{with tests}
%check
pushd src
%endif

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%license LICENSE
%{_libdir}/*.so.*

%files devel
%license LICENSE
%doc CHANGELOG README.md
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/*.pc

%changelog
