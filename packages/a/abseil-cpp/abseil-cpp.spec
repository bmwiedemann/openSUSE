#
# spec file for package abseil-cpp
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


%define lname	libabsl2301_0_0
Name:           abseil-cpp
Version:        20230125.2
Release:        0
Summary:        C++11 libraries which augment the C++ stdlib
License:        Apache-2.0
URL:            https://abseil.io/
Source0:        https://github.com/abseil/abseil-cpp/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig
# PATCH-FIX-OPENSUSE options-{old,cxx17}.patch Ensure ABI stability regardless of compiler options
%if 0%{?suse_version} < 1550
Patch0:         options-old.patch
%else
Patch0:         options-cxx17.patch
%endif

%description
Abseil is a collection of C++11 libraries which augment the C++
standard library. It also provides features incorporated into C++14
and C++17 standards.

%package -n %{lname}
Summary:        C++11 libraries which augment the C++ stdlib
Obsoletes:      abseil-cpp < %{version}-%{release}
Provides:       abseil-cpp = %{version}-%{release}

%description -n %{lname}
Abseil is a collection of C++11 libraries which augment the C++
standard library. It also provides features incorporated into C++14
and C++17 standards.

%package devel
Summary:        Header files for Abseil
Requires:       %{lname} = %{version}

%description devel
Abseil is a collection of C++11 libraries which augment the C++
standard library.
This package contains headers and build system files for it.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}/%{_prefix}

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSE
%{_libdir}/libabsl_*.so.*

%files devel
%doc README.md
%{_includedir}/absl
%{_libdir}/cmake/absl
%{_libdir}/libabsl_*.so
%{_libdir}/pkgconfig/absl_*.pc

%changelog
