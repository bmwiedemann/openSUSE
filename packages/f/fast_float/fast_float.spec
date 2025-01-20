#
# spec file for package fast_float
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


Name:           fast_float
Version:        7.0.0
Release:        0
Summary:        A fast number parsing library
License:        Apache-2.0 OR BSL-1.0 OR MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/fastfloat/fast_float
Source:         https://github.com/fastfloat/fast_float/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  cmake(doctest)

%description
The fast_float library provides fast header-only implementations for the C++
from_chars functions for float and double types as well as integer types.

%package devel
BuildArch:      noarch
Summary:        Development and header files for %{name}

%description devel
The fast_float library provides fast header-only implementations for the C++
from_chars functions for float and double types as well as integer types.

%prep
%autosetup -p1

%build
%cmake \
  -DFASTFLOAT_TEST:BOOL=ON \
  -DFASTFLOAT_SUPPLEMENTAL_TESTS:BOOL=OFF \
  -DSYSTEM_DOCTEST:BOOL=ON \
  %{nil}
#exit 1
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE-APACHE LICENSE-BOOST LICENSE-MIT
%doc README.md
%{_includedir}/fast_float
%dir %{_datadir}/cmake
%{_datadir}/cmake/FastFloat

%changelog
