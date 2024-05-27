#
# spec file for package xtensor-python
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


Name:           xtensor-python
Version:        0.27.0
Release:        0
Summary:        Python bindings for the xtensor C++ multi-dimensional array library
License:        BSD-3-Clause
URL:            https://github.com/xtensor-stack/xtensor-python
Source0:        https://github.com/xtensor-stack/xtensor-python/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Install-as-arch-independent.patch
BuildRequires:  cmake
BuildRequires:  doctest-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gtest
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  python3-breathe
BuildRequires:  python3-numpy-devel
BuildRequires:  xtensor-devel >= 0.25.0
BuildRequires:  cmake(pybind11) >= 2.6.1
Group:          Development/Libraries/C and C++

%description
Enables inplace use of numpy arrays in C++ with all the benefits from xtensor:
  * C++ universal function and broadcasting,
  * STL - compliant APIs,
  * A broad coverage of numpy APIs.

The Python bindings for xtensor are based on the pybind11 C++ library, which
enables seamless interoperability between C++ and Python.

%package devel
Summary:        Development files for xtensor-python
BuildArch:      noarch
Requires:       xtensor-devel

%description devel
Enables inplace use of numpy arrays in C++ with all the benefits from xtensor:
  * C++ universal function and broadcasting,
  * STL - compliant APIs,
  * A broad coverage of numpy APIs.

The Python bindings for xtensor are based on the pybind11 C++ library, which
enables seamless interoperability between C++ and Python.

%package doc
Summary:        Documentation for xtensor-python
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
Enables inplace use of numpy arrays in C++ with all the benefits from xtensor:
  * C++ universal function and broadcasting,
  * STL - compliant APIs,
  * A broad coverage of numpy APIs.

The Python bindings for xtensor are based on the pybind11 C++ library, which
enables seamless interoperability between C++ and Python.

%prep
%autosetup -p1

%build
%cmake -DBUILD_TESTS:BOOL=ON
%cmake_build

#build documentation
cd %{_builddir}/%{name}-%{version}/docs
make html

%install
%cmake_install

#install documentation
mkdir -p %{buildroot}/%{_docdir}/%{name}
cp -r %{_builddir}/%{name}-%{version}/docs/build/html/* %{buildroot}/%{_docdir}/%{name}

%check
%cmake_build -C %{__builddir} xtest

%files doc
%doc %{_docdir}/%{name}

%files devel
%license LICENSE
%{_includedir}/xtensor-python
%{_datadir}/cmake/xtensor-python

%changelog
