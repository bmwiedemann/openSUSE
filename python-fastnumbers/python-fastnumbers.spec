#
# spec file for package python-fastnumbers
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
Name:           python-fastnumbers
Version:        2.2.1
Release:        0
Summary:        Drop-in replacement for Python's int and float
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/SethMMorton/fastnumbers
Source:         https://files.pythonhosted.org/packages/source/f/fastnumbers/fastnumbers-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest-faulthandler}
BuildRequires:  %{python_module pytest}
BuildRequires:  python3-testsuite
# /SECTION
%python_subpackages

%description
fastnumbers is a Python module with three objectives:

1. To provide drop-in replacements for the Python built-in `int` and
   `float` that, on average, are around 2x faster. These functions
   should behave identically to the Python built-ins except for a few
   specific corner-cases as mentioned in the API documentation.
2. To provide a set of convenience functions that wrap the above int
   and float replacements and provide error handling.
3. To provide a set of functions that can be used to identify whether
   an input could be converted to int or float.

%prep
%setup -q -n fastnumbers-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
pytest-%{$python_bin_suffix}
}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
