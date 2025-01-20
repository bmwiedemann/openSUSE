#
# spec file for package NumCpp
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


%define __builder ninja
Name:           NumCpp
Version:        2.13.0
Release:        0
Summary:        C++ implementation of the Python Numpy library
License:        MIT
URL:            https://github.com/dpilger26/NumCpp
Source:         %{url}/archive/refs/tags/Version_%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM NumCpp-disable-pytest.patch badshah400@gmail.com -- Disable pytests that are incorrectly setup for pybind11 and enable gtest
Patch0:         NumCpp-disable-pytest.patch
# PATCH-FIX-UPSTREAM NumCpp-add-tests.patch badshah400@gmail.com -- Add tests to cmake so that they can be run using ctest
Patch1:         NumCpp-add-tests.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gtest
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_log-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-pybind11-devel
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(tbb)

%description
NumCpp is a templatized header-only C++ implementation of the Python NumPy library.

%package devel
Summary:        Header files for NumCpp
Requires:       libboost_date_time-devel
Requires:       libboost_headers-devel
Requires:       libboost_log-devel
Requires:       libboost_numpy3-devel
Requires:       libboost_python3-devel
Requires:       libboost_system-devel
Requires:       libboost_thread-devel
Requires:       python3-pybind11-devel
BuildArch:      noarch

%description devel
This package provides the header files for compiling code using NumCpp.

%prep
%autosetup -p1 -n %{name}-Version_%{version}

%build
%cmake \
  -DNUMCPP_USE_MULTITHREAD:BOOL=ON \
  -DBUILD_DOCS:BOOL=ON \
  -DBUILD_TESTS:BOOL=ON \
  -DBUILD_MULTIPLE_TEST:BOOL=ON \
  -DBUILD_CPPCHECK_TEST:BOOL=ON \
%{nil}
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}.hpp
%{_includedir}/%{name}/
%{_datadir}/%{name}/

%changelog
