#
# spec file for package bandicoot
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover 3
%define shlib lib%{name}%{sover}
Name:           bandicoot
Version:        3.1.0
Release:        0
Summary:        C++ library for GPU accelerated linear algebra
License:        Apache-2.0
URL:            https://coot.sourceforge.io/
Source:         https://sourceforge.net/projects/coot/files/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libopenblas_openmp-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-cpp-headers
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(clBLAS)

%description
Bandicoot is a GPU linear algebra library (matrix maths) for the C++ language,
aiming towards a good balance between speed and ease of use. It provides
high-level syntax and functionality deliberately similar to Matlab.

%package -n %{shlib}
Summary:        Shared library for %{name}

%description -n %{shlib}
Bandicoot is a GPU linear algebra library (matrix maths) for the C++ language,
aiming towards a good balance between speed and ease of use. It provides
high-level syntax and functionality deliberately similar to Matlab.

This package provides the shared library for %{name}.

%package devel
Summary:        Headers and source for developing against %{name}
Requires:       %{shlib} = %{version}

%description devel
Bandicoot is a GPU linear algebra library (matrix maths) for the C++ language,
aiming towards a good balance between speed and ease of use. It provides
high-level syntax and functionality deliberately similar to Matlab.

This package provides headers and sources for developing against %{name}.

%prep
%autosetup

%build
%cmake -DOPENBLAS_PROVIDES_LAPACK:BOOL=true
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %{shlib}

%files -n %{shlib}
%license LICENSE.txt
%{_libdir}/*.so.*

%files devel
%license LICENSE.txt
%doc README.md
%{_datadir}/Bandicoot/
%{_includedir}/%{name}
%{_includedir}/%{name}_bits/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
