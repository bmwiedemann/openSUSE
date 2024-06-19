#
# spec file for package lapackpp
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


Name:           lapackpp
Version:        2024.05.31
Release:        0
Summary:        C++ API for the Linear Algebra PACKage
License:        BSD-3-Clause
URL:            https://icl.utk.edu/slate/
Source:         https://github.com/icl-utk-edu/lapackpp/releases/download/v%{version}/lapackpp-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  cmake(blaspp)
BuildRequires:  cmake(lapack)
# Section For tests
BuildRequires:  python3
BuildRequires:  cmake(cblas)
BuildRequires:  cmake(lapacke)
BuildRequires:  cmake(testsweeper)
# /Section

%description
LAPACK++ is a C++ wrapper around LAPACK and LAPACK-like linear algebra libraries.

%package -n liblapackpp1
Summary:        Shared library for lapackpp

%description -n liblapackpp1
This package provides the shared library for lapackpp.

%package -n lapackpp-devel
Summary:        Headers and sources for developing against lapackpp
Requires:       liblapackpp1 = %{version}
Requires:       cmake(blaspp)
Requires:       cmake(lapack)

%description -n lapackpp-devel
This package provides the headers and sources needed for developing apps
against lapackpp.

%prep
%autosetup -p1

%build
%cmake \
  -Dcolor=no \
  -Dbuild_tests=yes \
  %{nil}
%cmake_build

%install
%cmake_install

%check
pushd %{__builddir}/test
python3 run_tests.py --quick
popd

%ldconfig_scriptlets -n liblapackpp1

%files -n liblapackpp1
%license LICENSE
%{_libdir}/liblapackpp.so.1*

%files -n lapackpp-devel
%license LICENSE
%{_includedir}/lapack.hh
%{_includedir}/lapack/
%{_libdir}/liblapackpp.so
%{_libdir}/cmake/lapackpp/

%changelog
