#
# spec file for package python-pybind11
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pybind11
Version:        2.4.2
Release:        0
Summary:        Module for operability between C++11 and Python
License:        BSD-3-Clause
URL:            https://github.com/pybind/pybind11
Source:         https://github.com/pybind/pybind11/archive/v%{version}.tar.gz#/pybind11-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
pybind11 is a header-only library that exposes C++ types in Python
and vice versa, mainly to create Python bindings of existing C++
code. It can reduce boilerplate code in traditional extension modules
by inferring type information using compile-time introspection.

%package -n %{name}-devel
Summary:        Development files for pybind11
Requires:       %{name} = %{version}
Requires:       python-devel
Provides:       %{python_module %{name}-devel}

%description -n %{name}-devel
This package contains files for developing applications using pybind11.

%prep
%setup -q -n pybind11-%{version}

%build
%python_build
# calling cmake to install header to right location and
# generate cmake include files
%cmake
%cmake_build

%install
%python_install
%cmake_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# removing duplciated header files
rm -rv %{buildroot}%{_includedir}/python2.*/pybind11/
rm -rv %{buildroot}%{_includedir}/python3.*/pybind11

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%files -n %{name}-devel
%{_includedir}/pybind11
%license LICENSE
%{_datadir}/cmake/pybind11

%changelog
