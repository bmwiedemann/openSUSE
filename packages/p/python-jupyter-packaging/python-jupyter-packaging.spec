#
# spec file for package python-jupyter-packaging
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-jupyter-packaging
Version:        0.7.12
Release:        0
Summary:        Jupyter Packaging Utilities
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/jupyter-packaging
Source:         https://files.pythonhosted.org/packages/source/j/jupyter-packaging/jupyter-packaging-%{version}.tar.gz
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-packaging
%python_subpackages

%description
This package contains utilities for making Python packages
with and without accompanying JavaScript packages

%prep
%setup -q -n jupyter-packaging-%{version}
sed -i 's/\r$//' README.md
sed -i -e '/^#!\//, 1d' jupyter_packaging/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_install and test_datafiles_install call pip which wants to check the online cache
%pytest -k "not (test_install or test_datafiles_install)"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
