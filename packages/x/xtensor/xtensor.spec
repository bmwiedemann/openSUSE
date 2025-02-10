#
# spec file for package xtensor
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
Name:           xtensor
Version:        0.25.0
Release:        0
Summary:        Multi-dimensional arrays with broadcasting and lazy computing
License:        BSD-3-Clause
URL:            https://github.com/xtensor-stack/xtensor
Source0:        https://github.com/xtensor-stack/xtensor/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module breathe}
BuildRequires:  %{python_module sphinx_rtd_theme}
BuildRequires:  cmake
BuildRequires:  doctest-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  xtl-devel >= 0.7.5
Group:          Development/Libraries/C and C++

%description
xtensor is a C++ library meant for numerical analysis with multi-dimensional array expressions.

xtensor provides
   - an extensible expression system enabling lazy broadcasting.
   - an API following the idioms of the C++ standard library.
   - tools to manipulate array expressions and build upon xtensor.

Containers of xtensor are inspired by NumPy, the Python array programming library. Adaptors for existing data structures to be plugged into the expression system can easily be written.

%package devel
Summary:        Development files for xtensor
BuildArch:      noarch
Requires:       xtl-devel

%description devel
xtensor is a C++ library meant for numerical analysis with multi-dimensional array expressions.

xtensor provides
   - an extensible expression system enabling lazy broadcasting.
   - an API following the idioms of the C++ standard library.
   - tools to manipulate array expressions and build upon xtensor.

Containers of xtensor are inspired by NumPy, the Python array programming library. Adaptors for existing data structures to be plugged into the expression system can easily be written.

%package doc
Summary:        Documentation for xtensor
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
xtensor is a C++ library meant for numerical analysis with multi-dimensional array expressions.

xtensor provides
   - an extensible expression system enabling lazy broadcasting.
   - an API following the idioms of the C++ standard library.
   - tools to manipulate array expressions and build upon xtensor.

Containers of xtensor are inspired by NumPy, the Python array programming library. Adaptors for existing data structures to be plugged into the expression system can easily be written.

%prep
%setup -q

%build
%cmake -DCPP17:BOOL=ON -DBUILD_TESTS:BOOL=ON
%cmake_build

#build documentation
cd %{_builddir}/%{name}-%{version}/docs
make html

%install
%cmake_install

#install documentation
mkdir -p %{buildroot}/%{_docdir}/%{name}
cp -r %{_builddir}/%{name}-%{version}/docs/build/html/* %{buildroot}/%{_docdir}/%{name}

%fdupes -s %{buildroot}/%{_docdir}
%fdupes %{buildroot}/%{_prefix}

%check
%ctest

%files doc
%doc %{_docdir}/%{name}

%files devel
%license LICENSE
%{_includedir}/xtensor
%{_includedir}/xtensor.hpp
%{_datadir}/cmake/xtensor
%{_datadir}/pkgconfig/xtensor.pc

%changelog
