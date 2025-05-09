#
# spec file for package xsimd
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


%{?sle15_python_module_pythons}
Name:           xsimd
Version:        13.0.0
Release:        0
Summary:        C++ wrappers for SIMD intrinsics
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://xsimd.readthedocs.io/en/latest/
Source0:        https://github.com/xtensor-stack/xsimd/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- https://mail.kde.org/pipermail/distributions/2024-July/001511.html
Patch0:         0001-Fix-xsimd-available_architectures-.has-for-sve-and-r.patch
Patch1:         0002-Fix-detection-of-SSE-AVX-AVX512-when-they-are-explic.patch
BuildRequires:  %{python_module breathe}
BuildRequires:  %{python_module sphinx_rtd_theme}
BuildRequires:  cmake
BuildRequires:  doctest-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  cmake(GTest)

%description
SIMD (Single Instruction, Multiple Data) is a feature of microprocessors that
has been available for many years. SIMD instructions perform a single operation
on a batch of values at once, and thus provide a way to significantly accelerate
code execution. However, these instructions differ between microprocessor
vendors and compilers.

xsimd provides a unified means for using these features for library authors.
Namely, it enables manipulation of batches of numbers with the same arithmetic
operators as for single values. It also provides accelerated implementation of
common mathematical functions operating on batches.

%prep
%autosetup -p1

%build
%cmake -DBUILD_TESTS:BOOL=ON

%cmake_build

# Build documentation
%make_build -C %{_builddir}/%{name}-%{version}/docs html

%install
%cmake_install

#install documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r %{_builddir}/%{name}-%{version}/docs/build/html/* %{buildroot}%{_docdir}/%{name}

%check
%ctest

%package devel
Summary:        Development files for xsimd

%description devel
SIMD (Single Instruction, Multiple Data) is a feature of microprocessors that
has been available for many years. SIMD instructions perform a single operation
on a batch of values at once, and thus provide a way to significantly accelerate
code execution. However, these instructions differ between microprocessor
vendors and compilers.

xsimd provides a unified means for using these features for library authors.
Namely, it enables manipulation of batches of numbers with the same arithmetic
operators as for single values. It also provides accelerated implementation of
common mathematical functions operating on batches.

This package contains the developments files needed to use xsimd

%files devel
%license LICENSE
%{_includedir}/xsimd
%{_libdir}/cmake/xsimd
%{_libdir}/pkgconfig/xsimd.pc

%package doc
Summary:        Documentation for xsimd
Group:          Documentation/HTML

%description doc
SIMD (Single Instruction, Multiple Data) is a feature of microprocessors that
has been available for many years. SIMD instructions perform a single operation
on a batch of values at once, and thus provide a way to significantly accelerate
code execution. However, these instructions differ between microprocessor
vendors and compilers.

xsimd provides a unified means for using these features for library authors.
Namely, it enables manipulation of batches of numbers with the same arithmetic
operators as for single values. It also provides accelerated implementation of
common mathematical functions operating on batches.

This package contains the xsimd documentation

%files doc
%doc %{_docdir}/%{name}

%changelog
