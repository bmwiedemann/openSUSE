#
# spec file for package blaspp
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


%define so_ver 1
%define __builder ninja
Name:           blaspp
Version:        2024.05.31
Release:        0
Summary:        C++ API for the Basic Linear Algebra Subroutines
License:        BSD-3-Clause
URL:            https://icl.utk.edu/slate/
Source:         https://github.com/icl-utk-edu/blaspp/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(blas)
# Section For tests
BuildRequires:  cmake(cblas)
BuildRequires:  cmake(lapack)
BuildRequires:  cmake(testsweeper)
# /Section

%description
The objective of BLAS++ is to provide a performance oriented API for
development in the C++ language, that, for the most part, preserves established
conventions, while, at the same time, takes advantages of modern C++ features,
such as: namespaces, templates, exceptions, etc.

%package -n libblaspp%{so_ver}
Summary:        Shared library for blaspp

%description -n libblaspp%{so_ver}
This package provides the shared library for blaspp.

%package -n blaspp-devel
Summary:        Headers and sources for developing with blaspp
Requires:       libblaspp%{so_ver} = %{version}
Requires:       pkgconfig(blas)

%description -n blaspp-devel
This package provides the headers and sources needed for developing apps
against blaspp.

%prep
%autosetup -p1

%build
%cmake \
	-Dcolor=no \
	-Duse_openmp=yes \
	-Dbuild_tests=yes \
	%{nil}
%cmake_build

%install
%cmake_install

%check
pushd %{__builddir}/test
python3 run_tests.py --quick
popd

%ldconfig_scriptlets -n libblaspp%{so_ver}

%files -n libblaspp%{so_ver}
%license LICENSE
%{_libdir}/libblaspp.so.%{so_ver}*

%files -n blaspp-devel
%license LICENSE
%{_includedir}/blas.hh
%{_includedir}/blas/
%{_libdir}/libblaspp.so
%{_libdir}/cmake/blaspp/

%changelog
