#
# spec file for package python-toolz
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


%{?sle15_python_module_pythons}
Name:           python-toolz
Version:        0.12.1
Release:        0
Summary:        List processing tools and functional utilities for python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pytoolz/toolz/
Source:         https://files.pythonhosted.org/packages/source/t/toolz/toolz-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A set of python utility functions for iterators, functions, and dictionaries.

%prep
%setup -q -n toolz-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k "not test_inspect_wrapped_property"

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/toolz/
%{python_sitelib}/tlz/
%{python_sitelib}/toolz-%{version}.dist-info

%changelog
