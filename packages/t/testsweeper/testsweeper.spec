#
# spec file for package testsweeper
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

%global flavor @BUILD_FLAVOR@%{nil}
%global pname testsweeper
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define __builder ninja
Name:           testsweeper%{?psuffix}
Version:        2024.05.31
Release:        0
Summary:        C++ testing framework for parameter sweeps
License:        BSD-3-Clause
URL:            https://github.com/icl-utk-edu/testsweeper
Source:         %{url}/releases/download/v%{version}/testsweeper-%{version}.tar.gz
BuildRequires:  cmake >= 3.15
BuildRequires:  gcc-c++
BuildRequires:  ninja 
%if %{with test}
BuildRequires:  python3
BuildRequires:  lapack-devel
BuildRequires:  cblas-devel
BuildRequires:  cmake(testsweeper) = %{version}
%endif

%description
TestSweeper is a C++ testing framework for parameter sweeps. It handles parsing
command line options, iterating over the test space, and printing results. This
simplifies test functions by allowing them to concentrate on setting up and
solving one problem at a time.

%package -n lib%{name}1
Summary:        Shared library for testsweeper, a C++ testing framework for parameter sweeps

%description -n lib%{name}1
TestSweeper is a C++ testing framework for parameter sweeps. It handles parsing
command line options, iterating over the test space, and printing results. This
simplifies test functions by allowing them to concentrate on setting up and
solving one problem at a time.

This package provides the share library for %{name}.

%package -n %{name}-devel
Summary:        Headers and sources for developing apps against testsweeper
Requires:       lib%{name}1 = %{version}

%description -n %{name}-devel
TestSweeper is a C++ testing framework for parameter sweeps. It handles parsing
command line options, iterating over the test space, and printing results. This
simplifies test functions by allowing them to concentrate on setting up and
solving one problem at a time.

This package provides the headers and sources needed to develop apps against
testsweeper.

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
%cmake -Dcolor=OFF \
       -Duse_openmp=ON \
       -Dbuild_tests=%{?with_test:ON}%{!?with_test:OFF} \
       %{nil}
%cmake_build

%install
%if %{without test}
%cmake_install

%ldconfig_scriptlets -n lib%{name}1

%files -n lib%{name}1
%license LICENSE
%{_libdir}/lib%{name}.so.1*

%files -n %{name}-devel
%license LICENSE
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/testsweeper/
%{_includedir}/testsweeper.hh

%else

%check
pushd %{__builddir}/test
python3 ./run_tests.py
popd

%endif

%changelog
