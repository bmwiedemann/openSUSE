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
Version:        2.3.0
Release:        0
Summary:        Module for operability between C++11 and Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/pybind/pybind11
Source:         https://files.pythonhosted.org/packages/53/bc/0880e869d1a4bfd7954835d67e6d5e2c8a30c3fd6372134a4be79a842a4c/pybind11-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
pybind11 is a header-only library that exposes C++ types in Python
and vice versa, mainly to create Python bindings of existing C++
code. It can reduce boilerplate code in traditional extension modules
by inferring type information using compile-time introspection.

%package devel
Summary:        Development files for pybind11
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       python-devel

%description devel
This package contains files for developing applications using pybind11.


%prep
%setup -q -n pybind11-%{version}

echo "python_files devel = %{python_files devel}"

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%files %{python_files devel}
%defattr(-,root,root)
%license LICENSE
%{python_sysconfig_path include}

%changelog
